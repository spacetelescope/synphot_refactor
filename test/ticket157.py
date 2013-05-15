from __future__ import division
import pysynphot as S
from pysynphot.observation import Observation
from pysynphot import spparser
import os, sys
import testutil
import numpy as N

from pysynphot import locations, refs

#Places used by test code
userdir   = os.path.join(os.path.dirname(__file__), 'data')
testdata  = os.path.join(locations.rootdir, 'calspec', 'feige66_002.fits')
testdir   = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

old_comptable = None
old_vegafile = None

def setUpModule():
    #Freeze the version of the comptable so tests are not susceptible to
    # updates to CDBS
    global old_comptable
    global old_vegafile

    old_comptable = refs.COMPTABLE
    cmptb_name = os.path.join('mtab', 'r1j2146sm_tmc.fits')
    refs.COMPTABLE = locations._refTable(cmptb_name)
    print "%s:" % os.path.basename(__file__)
    print "   Tests are being run with %s" % refs.COMPTABLE
    print "   Synphot comparison results were computed with r1j2146sm_tmc.fits"
    #Synphot comparison results are identified with the varname synphot_ref.

    #Also set the version of Vega for similar reasons
    old_vegafile = locations.VegaFile
    locations.VegaFile = os.path.join(testdir, 'alpha_lyr_stis_002.fits')
    print "Using Vega spectrum: %s" % locations.VegaFile


def tearDownModule():
    refs.COMPTABLE = old_comptable
    locations.VegaFile = old_vegafile


class OverlapBug(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.ArraySpectrum(wave=N.arange(3000,4000),
                                flux=N.ones((1000,))*0.75,
                                name="Short flat")
        self.bp=S.Box(4000,100)
        self.refwave=4005
        self.refval=0.75

    def testoverlap(self):
        ans=self.bp.check_overlap(self.sp)
        self.failUnless(ans=='partial')

    def testtaper(self):
        self.obs=S.Observation(self.sp,self.bp,force='taper')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux.item(idx[0])
        self.assert_(test==0,'Expected 0, got %f'%test)

    def testextrap(self):
        self.obs=S.Observation(self.sp,self.bp,force='extrap')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux.item(idx[0])
        self.assertAlmostEqual(test,self.refval,msg='Expected %f, got %f'%(self.refval,test))

##     def testrange(self):
##         self.wt=N.array([3090, 3095, 4000,4005, 4010])
##         ans=self.sp(self.wt)
##         self.ref=N.array( [1.0, 1.0, 1.0, 0.0, 0.0])
##         self.assertEqualNumpy(self.ref,ans)

    def testraise(self):
        self.assertRaises(ValueError,
                          S.Observation,
                          self.sp, self.bp)


class DiscoveryCase(OverlapBug):
    def setUp(self):
        fname = os.path.join('data', 'qso_template.fits')
        self.old_cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        self.spstring='rn(z(spec(%s),0.03),band(johnson,v),18,vegamag)' %fname
        self.sp=spparser.parse_spec(self.spstring)
        self.sp.convert('photlam')
        self.bp=S.ObsBandpass('stis,ccd,g750l,c7751,s52x02')
        self.refwave=6200
        self.refval=2.97759742e-06

    def tearDown(self):
        os.chdir(self.old_cwd)

##     def testorig(self):
##         #This test fails unless the Observation has the "expected"
##         #behavior. Pre-fix, it will fail because that's the bug.
##         #Post-fix, it will have an error and end with an exception.
##           #It can be uncommented as a sanity check, but will never pass.
##
##         self.obs=S.Observation(self.sp,self.bp)
##         idx=N.where(self.obs.wave==self.refwave)
##         testval=self.obs.flux[idx[0]]
##         self.failUnless(testval == 0,'obs[%d]==%g'%(self.refwave,testval))

class BPOverlap(testutil.FPTestCase):
    def setUp(self):
        self.a=S.Box(4000,50)
        self.disjoint=S.Box(6000,100)
        self.full=S.Box(4000,100)
        self.partial=S.Box(4050,50)

    def testdisjoint(self):
        stat=self.a.check_overlap(self.disjoint)
        self.failUnless(stat == 'none')

    def testfull(self):
        stat=self.a.check_overlap(self.full)
        self.failUnless(stat == 'full')

    def testpartial(self):
        stat=self.a.check_overlap(self.partial)
        self.failUnless(stat == 'partial')


class BP03(BPOverlap):
    def setUp(self):
        self.a=S.ArrayBandpass(wave=N.arange(4000,5000),
                               throughput=N.ones(1000))
        self.disjoint=S.Box(1000,100)
        self.full=S.ArrayBandpass(wave=N.arange(3000,6000),
                                  throughput=N.ones(3000))
        self.partial=S.ArrayBandpass(wave=N.arange(500,4500),
                                     throughput=N.ones(4000))


class AnalyticCase(testutil.FPTestCase):
    def setUp(self):
        self.bb=S.BlackBody(5000)
        self.em=S.GaussianSource(3300,1,1)
        self.flat=S.FlatSpectrum(10)
        self.pl=S.PowerLaw(5000,-2)
        self.tspec=S.ArraySpectrum(self.bb.wave,self.bb.flux,
                                   fluxunits=self.bb.fluxunits)
        self.pl.writefits('ac_pl.fits')
        self.fspec=S.FileSpectrum('ac_pl.fits')

    def tearDown(self):
        os.unlink('ac_pl.fits')

    def testbb(self):
        self.assert_(self.bb.isAnalytic)

    def testfile(self):
        self.failIf(self.fspec.isAnalytic)

    def testtab(self):
        self.failIf(self.tspec.isAnalytic)

    def testcomp1(self):
        x=self.bb+self.em
        self.assert_(x.isAnalytic)

    def testcomp2(self):
        x=self.bb+self.tspec
        self.failIf(x.isAnalytic)

    def testcomp3(self):
        x=self.flat*2.6
        self.assert_(x.isAnalytic)

#These tests were part of the original nightly pysynphot test suite
#that began failing when #157 was implemented because they really
#did have partial overlap.

class CalcphotTestCase(testutil.FPTestCase):
    #Loosened accuracy for r618 (no taper)
    def setUp(self):
        testdata  = os.path.join(locations.rootdir, 'calspec',
                                 'feige66_002.fits')
        self.sp = S.FileSpectrum(testdata)
        self.bandpass = S.ObsBandpass('acs,hrc,f555w')
        self.refrate = 8.30680E+05
        self.reflam = 5304.462

    def testraises(self):
        self.assertRaises(ValueError,
                          S.Observation,
                          self.sp, self.bandpass)

    def testefflam(self):
        obs=S.Observation(self.sp, self.bandpass, force='extrap')
        tst=obs.efflam()
        self.assertApproxFP(tst, self.reflam, 1e-4)


    def testcountrate(self):
        obs=S.Observation(self.sp, self.bandpass, force='taper')
        tst=obs.countrate()
        self.assertApproxFP(tst, self.refrate, 1e-4)


class ETCTestCase_Imag2(testutil.FPTestCase):

    def setUp(self):
        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "acs,sbc,F140LP"
        self.refrate = 0.0877036
        self.setup2()

    def setup2(self):
       try:
            self.oldpath = os.path.abspath(os.curdir)
            if os.path.isdir(os.path.join(locations.specdir, 'generic')):
                os.chdir(os.path.join(locations.specdir, 'generic'))
            else:
                os.chdir(locations.specdir)
            self.sp = spparser.parse_spec(self.spectrum)
            self.sp = spparser.parse_spec(self.spectrum)
            self.bp = S.ObsBandpass(self.obsmode)
            self.parameters = ["spectrum=%s" % self.spectrum,
                               "instrument=%s" % self.obsmode]
       except AttributeError:
           pass

    def tearDown(self):
        os.chdir(self.oldpath)

    def testraises(self):
        #Replaced answer for r618 (no tapering)
        #The throughput files used in this case don't actually go
        #all the way to zero.
        self.assertRaises(ValueError,
                          S.Observation,
                          self.sp, self.bp)



    def tearDown(self):
        os.chdir(self.oldpath)



class ETCTestCase_Spec2a(ETCTestCase_Imag2):
    def setUp(self):
        self.spectrum = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
        self.obsmode = "stis,fuvmama,g140l,s52x2"
        self.syn_pysyn_id = 'stis_etc_cases:SpecSourcerateSpecCase2'
        self.refrate = 28935.7
        self.setup2()



    def testflux(self):
        self.obs=S.Observation(self.sp,self.bp,force='taper')
        self.obs.convert('counts')

        self.assertApproxFP(float(self.obs.binflux[500]), 35.5329)

## class ETC01(OverlapBug):


##         self.spectrum = "em(4300.0,1.0,9.999999960041972E-13,flam)"
##         self.obsmode = "stis,ccd,g430l"


##         self.spectrum = "em(4000.0,10.0,1.0000000168623835E-16,flam)"
##         self.obsmode = "acs,hrc,PR200L"

##         self.spectrum = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
##         self.obsmode = "stis,fuvmama,g140l,s52x2"

##         spectrum = "spectrum= rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
##         instrument = "instrument=stis,ccd"

##         spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
##         instrument = "instrument=acs,sbc,F140LP"

##         spectrum = "spectrum=em(3880.0,10.0,1.0000000168623835E-16,flam)"
##         instrument = "instrument=acs,wfc1,FR388N#3880"

##         testdata  = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
##         'obsmode':        'acs,hrc,f555w',
