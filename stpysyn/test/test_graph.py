from __future__ import division

# STDLIB
import os
from unittest import TestCase

# PYSYNPHOT
try:
    from pysynphot.graphtab import GraphTable
except ImportError:
    print "Warning, the tests won't run; GraphTable not yet implemented"

# LOCAL
from .testutil import skip


def make_tmg(strdata,tmgname):
    """Helper function"""
    with open(tmgname,'w') as out:
        out.write(strdata)
        out.flush()

##     tbhdu=fits.tcreate('data.txt',cdfile='cdfile.txt',hfile='h1.txt')
##     tbhdu.writeto(tmgname, clobber=True)


class GraphCase(TestCase):
    #Drat, put compname first like in real table
    old_simple1="""acs 1 20 clear clear
cos 1 20 clear clear
default 1 100 clear clear
noota 20 30 clear clear
default 20 30 hst_ota clear
ota 20 30 hst_ota clear
acs 30 10000 clear clear
cos 30 11000 clear clear
sbc 10000 10199 clear clear
hrc 10000 10150 clear clear
wfc1 10000 10100 clear clear
default 10100 10101 clear clear
default 10101 10130 acs_wfc_im123 clear
f606w 10130 10140 acs_f606w clear
f550m 10130 10140 acs_f550m clear
f555w 10130 10140 acs_f555w clear
default 10140 10300 clear clear
wfc1 10300 10310 acs_wfc_ebe_win12f clear
default 10310 10320 acs_wfc_ccd1 clear
mjd# 10310 10320 acs_wfc_ccd1_mjd clear
"""
    simple1="""clear  acs  1  20  clear
clear  cos  1  20  clear
clear  default  1  100  clear
clear  noota  20  30  clear
hst_ota  default  20  30  clear
hst_ota  ota  20  30  clear
clear  acs  30  10000  clear
clear  cos  30  11000  clear
clear  sbc  10000  10199  clear
clear  hrc  10000  10150  clear
clear  wfc1  10000  10100  clear
clear  default  10100  10101  clear
acs_wfc_im123  default  10101  10130  clear
acs_f606w  f606w  10130  10140  clear
acs_f550m  f550m  10130  10140  clear
acs_f555w  f555w  10130  10140  clear
clear  default  10140  10300  clear
acs_wfc_ebe_win12f  wfc1  10300  10310  clear
acs_wfc_ccd1  default  10310  10320  clear
acs_wfc_ccd1_mjd  mjd#  10310  10320  clear"""

    # Putting @skip on the setUp method is a shortcut to skip all tests in the
    # class (might be possible to write a @skip class decorator, but this is
    # fine for now)
    @skip
    def setUp(self):
        self.fname='/tmp/simple1.tmg'
        make_tmg(self.simple1, self.fname)
        self.G=GraphTable(self.fname)

    def tearDown(self):
        os.unlink(self.fname)
        #os.unlink('data.txt')

    def test1(self):
        self.instring='acs,wfc1,f555w'
        self.ref=['hst_ota',
                  'acs_wfc_im123',
                  'acs_f555w',
                  'acs_wfc_ebe_win12f',
                  'acs_wfc_ccd1']
        path =self.G.traverse(self.instring)
        self.assertEqual(self.ref, path.optical)

    def testparam(self):
        self.instring='acs,wfc1,f606w,mjd#70123'
        self.ref=['hst_ota',
                  'acs_wfc_im123',
                  'acs_f606w',
                  'acs_wfc_ebe_win12f',
                  'acs_wfc_ccd1_mjd']
        path = self.G.traverse(self.instring)
        self.assertEqual(self.ref, path.optical)

    def testnext(self):
        self.instring="acs"
        self.ref=set(['hrc','wfc1'])
        tst=self.G.getnext(self.instring)

    def testunused(self):
        self.instring="cos,foo"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)

    def testincomplete(self):
        self.instring="acs"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)

    def testambiguous(self):
        self.instring="acs,wfc1,f550m,f555w"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)


    #Included in validate: not separately available.
    #it -could- be, but that would be very inefficient
    #def testloopcheck(self):
    #    self.assert_(not self.G._loopcheck())

    #I think this test is no longer necessary. The new
    #structure is built of links and not dependent on order
    #of traversal? But better test that that's true using
    #a test file
    def testascending(self):
        self.assert_(self.G._ordercheck())

    #also included in validate but not separately
    #def testreachable(self):
    #    self.assert_(self.G._orphancheck())
    def testvalidate(self):
        #Performs all the earlier checks
        self.assert_(self.G.validate())

    def testallmodes(self):
        #Purpose: to generate all legal obsmodes.
        # G.all_nodes is for something else
        self.ref=set(['cos',
                      'acs, hrc',
                      'acs, wfc1, f606w',
                      'acs, wfc1, f550m',
                      'acs, wfc1, f555w'])
        tst=self.G.allmodes()
        self.assertEqual(self.ref,tst)


class ThermalCase(GraphCase):
    simpletherm="""something with thermal modes"""

    @skip
    def setUp(self):
        self.fname='/tmp/t2605492m_tmg.fits' #simpletherm_tmg.fits'
        self.G=GraphTable(self.fname)

    def test_consistent(self):
        self.assert_(self.G._thermback())

    def test_opt_therm(self):
        self.instring='nicmos,3,f222m'

        path =self.G.traverse(self.instring)
        #Or is this the right UI?
        #thm=self.G.traverse(self.instring,thermal=True)
        #The thermal path must be a superset of the optical path,
        #though it need not be a strict superset.
        self.assert_(set(path.thermal)>=set(path.optical))

    def test_therm(self):
        self.instring='nicmos,2,f187n'
        self.ref='tbd'
        path = self.G.traverse(self.instring)
        self.assertEqual(self.ref,path.thermal)

    def test_temp(self):
        #Do we really want to keep this interface?
        self.instring='nicmos,3,f222m,primary#320'
        self.ref='tbd'
        path =self.G.traverse(self.instring)
        #A better interface might be to specify temperature overrides
        #when calling the method
        #bp.thermback(primary=320)

class BadGraph(TestCase):
    badgraph="""clear acs 1 20 clear
clear acs 15 30 clear
clear acs 20 30 clear
clear cos 1 20 clear
clear cos 20 30 clear
clear cos 30 40 clear
clear cos 40 20 clear
"""
    @skip
    def setUp(self):
        self.fname='/tmp/badgraph_tmg.txt'
        f=open(self.fname,'w')
        f.write(self.badgraph)
        f.close()
        self.G=GraphTable(self.fname)

    def testorphan(self):
        msg = self.G.validate()
        self.assert_('unreachable' in ''.join(msg))

    def testloop(self):
        msg = self.G.validate()
        self.assert_('Loop' in ''.join(msg))

class MissingGraph(TestCase):
    #remove the last column of the simple graph case
    missinggraph=GraphCase.simple1.replace('clear\n','\n')
    @skip
    def setUp(self):
        self.fname='/tmp/missinggraph_tmg.txt'
        f=open(self.fname,'w')
        f.write(self.missinggraph)
        f.close()

    def tearDown(self):
        try:
            os.unlink(self.fname)
        except Exception: #ok
            pass

    def testconstructor(self):
        self.assertRaises(ValueError,
                          GraphTable,
                          self.fname)

