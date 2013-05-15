from __future__ import division

import sys
import os
import testutil

from pysynphot import spectrum,observationmode
from pysynphot import locations, refs


old_comptable = None


def setUpModule():
    #Freeze the version of the comptable so tests are not susceptible to
    # updates to CDBS
    global old_comptable
    cmptb_name = os.path.join('mtab','rcb1833hm_tmc.fits')
    old_comptable = refs.COMPTABLE
    refs.COMPTABLE = locations._refTable(cmptb_name)
    print "%s:" % os.path.basename(__file__)
    print "   Tests are being run with %s" % refs.COMPTABLE


def tearDownModule():
    refs.COMPTABLE = old_comptable


class ParmCase(testutil.FPTestCase):
    def setUp(self):
        self.omstring='acs,hrc,f555w,mjd#54000'
        self.parkey='mjd'
        self.parval=54000
        self.reffile=os.path.join(os.environ['PYSYN_CDBS'],'comp','acs',
                                  'acs_hrc_ccd_mjd_013_syn.fits[mjd#]')
        self.construct()


    def construct(self):
        self.om=observationmode.ObservationMode(self.omstring)
        self.rnames=[x for x in self.om._throughput_filenames if (x != 'clear')]
        try:
            self.idx=self.rnames.index(self.reffile)
        except ValueError:
            print "looking for ",self.reffile
            for fname in self.rnames:
                print fname

    def test1(self):
        "parm# in modes"
        self.assert_(self.parkey+'#' in self.om.modes)


    def test2(self):
        "filename has a #"
        self.assert_(self.reffile in self.om._throughput_filenames)

    def test3(self):
        "dict entry"
        self.assert_(self.om.pardict[self.parkey]==self.parval)

    def test4(self):
        "interpolated type"
        try:
            self.assert_(isinstance(self.om.components[self.idx].throughput,
                                spectrum.InterpolatedSpectralElement))
        except IndexError:
            print len(self.om.components)
            print self.idx


class TwoParms(testutil.FPTestCase):
    def setUp(self):
        self.omstring = 'acs,hrc,fr459m#4610,aper#0.3'
        self.pardict = {'fr459m': 4610,'aper': 0.3}
        self.om = observationmode.ObservationMode(self.omstring)

    def test1(self):
        "parm# in modes"
        for k in self.pardict:
            self.assert_(k + '#' in self.om.modes)



    def test3(self):
        "dict vals"
        for k in self.pardict:
            self.assert_(self.om.pardict[k] == self.pardict[k])


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)


