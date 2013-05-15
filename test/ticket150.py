from __future__ import division
import pysynphot as S
from pysynphot.observation import Observation
from pysynphot import spparser
from pysynphot.exceptions import OverlapError
import os, sys
import testutil
import numpy as N

from pysynphot import locations, refs


old_comptable = None
old_vegafile = None


def setUpModule():
    # Freeze the version of the comptable so tests are not susceptible to
    # updates to CDBS
    global old_comptable
    global old_vegafile

    cmptb_name = os.path.join('mtab', 't260548pm_tmc.fits')
    old_comptable = refs.COMPTABLE
    refs.COMPTABLE = locations._refTable(cmptb_name)
    print "%s:" % os.path.basename(__file__)
    print "  Tests are being run with %s" % refs.COMPTABLE

    # Also set the version of Vega for similar reasons
    old_vegafile = locations.VegaFile
    locations.VegaFile = os.path.join('crcalspec', 'alpha_lyr_stis_003.fits')
    print "Using Vega spectrum: %s" % locations.VegaFile


def tearDownModule():
    refs.COMPTABLE = old_comptable
    locations.VegaFile = old_vegafile


class RenormOverlap(testutil.FPTestCase):
    """Tests for strict rejection."""

    def setUp(self):
        # (re)discovery case: stis_rn_cases/stisC94
        self.sp = S.FileSpectrum('$PYSYN_CDBS/grid/kc96/starb2_template.fits')
        self.bp = S.ObsBandpass('cos,fuv,g130m,c1300')
        self.cmd = 'rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)'
        self.ref = 0.00718543  # expected renorm factor

    def testraise(self):
        self.assertRaises(OverlapError,
                          self.sp.renorm,
                          16.0,'stmag',self.bp)

    def testforce(self):
        sp2=self.sp.renorm(16.0,'stmag',self.bp,force=True)
        ratio=sp2.flux/self.sp.flux
        self.failUnless(N.all(1-abs(ratio/self.ref)<0.0001))

    def testparse(self):
        sp2=S.spparser.parse_spec(self.cmd)
        ratio=sp2.flux/self.sp.flux
        self.failUnless(N.all(1-abs(ratio/self.ref)<0.0001))

    def testfull(self):
        jv=S.ObsBandpass('johnson,v')
        try:
            sp2=self.sp.renorm(17.0,'abmag',jv)
        except ValueError,e:
            self.fail(e.message)



class SmarterOverlap(RenormOverlap):
    #If 99% of throughput on spectrum, go ahead but print warning
    def testsmart(self):
        #does not yet test warning
        acs=S.ObsBandpass('acs,hrc,f555w')
        try:
            sp2=self.sp.renorm(17.0,'abmag',acs)
        except ValueError,e:
            self.fail(e.message)


class CornerCase(testutil.FPTestCase):
    def setUp(self):
        #This case is deliberately constructed to have a waveset
        #that partially overlaps, but for which all the flux is
        #fully contained.
        self.bp=S.ObsBandpass('acs,hrc,f555w')
        w=wave=S.Waveset(1000,10000)
        f=N.zeros(w.shape)
        f[4000:4010]=1.0
        self.sp=S.ArraySpectrum(wave=w,flux=f,fluxunits='flam')

    def testpartial(self):
        self.assert_('partial',
                     self.bp.check_overlap(self.sp))

    def testsmart(self):
        try:
            sp2=self.sp.renorm(17.0,'abmag',self.bp)
        except ValueError,e:
            self.fail(e.message)


class BPIntegrate(testutil.FPTestCase):
    def setUp(self):
        #Box 100 A wide, centered at 1000
        self.bp=S.Box(1000,100)
        self.ref=100.0

    def testintegrate(self):
        tst=self.bp.integrate()
        self.assertEqual(self.ref,tst)

    def testsubint(self):
        w=self.bp.wave
        tst=self.bp.integrate(w[0:len(w)/2])
        #epsilon due to the nature of trapezoid integration
        self.assert_(abs(self.ref/2.0-tst)<=0.025)


class OVBase(object):
    #Base class for the variants we can imagine
    #Implement all methods here
    def defarrays(self):
        #Supposes that the range variables have already been set
        w=N.arange(*self.sprange)
        f=N.zeros(w.shape)
        f[slice(*(self.spnonzero-w[0]))]+=1.0
        self.sp=S.ArraySpectrum(wave=w,flux=f)
        w=N.arange(*self.bprange)
        t=N.zeros(w.shape)
        t[slice(*(self.bpnonzero-w[0]))]+=1
        self.bp=S.ArrayBandpass(w,t)

    def testcurrent(self):
        ans=self.bp.check_overlap(self.sp)
        self.assertEqual(self.cref,ans)

    def testsig(self):
        if self.cref == 'partial':
            ans=self.bp.check_sig(self.sp)
            self.assertEqual(self.sref,ans)
        else:
            pass


class SpBp(OVBase,testutil.FPTestCase):
    #SPdef fully encloses BPdef: "full" overlap. Pass.
    def setUp(self):
        self.sprange=(1000,10000)
        self.spnonzero=self.sprange
        self.bprange=(5000,6000)
        self.bpnonzero=self.bprange
        OVBase.defarrays(self)
        self.cref='full'
        self.sref=True


class BpSp(OVBase,testutil.FPTestCase):
    #BPdef fully encloses SPdef: Insufficient overlap. Fail.
    def setUp(self):
        self.sprange=(5000,6000)
        self.spnonzero=self.sprange
        self.bprange=(1000,10000)
        self.bpnonzero=self.bprange
        OVBase.defarrays(self)
        self.cref='partial'
        self.sref=False


class SpPartial(OVBase,testutil.FPTestCase):
    #Partial overlap: return partial, require further processing
    def setUp(self):
        self.sprange=(1000,8000)
        self.bprange=(4000,10000)
        self.spnonzero=self.sprange
        self.bpnonzero=self.bprange
        OVBase.defarrays(self)
        self.cref='partial'
        self.sref=False #assuming they're all ones

#Now do variants where nonzero is different from range

class SpBpNz(OVBase, testutil.FPTestCase):
    #BP defined zero some places: still acceptable
    def setUp(self):
        self.sprange=(1000,10000)
        self.spnonzero=self.sprange
        self.bprange=(5000,6000)
        self.bpnonzero=(5500,5550)
        OVBase.defarrays(self)
        self.cref='full'
        self.sref=True


class BpSpNz(OVBase,testutil.FPTestCase):
    #Passes per current defn that looks at bp.nonzero, sp.def
    def setUp(self):
        self.sprange=(5000,6000)
        self.spnonzero=self.sprange
        self.bprange=(1000,10000)
        self.bpnonzero=(5500,5700)
        OVBase.defarrays(self)
        self.cref='full'
        self.sref=True


class SpPartialNz1(OVBase,testutil.FPTestCase):
    #Passes per current defn that looks at bp.nonzero, sp.def
    def setUp(self):
        self.sprange=(1000,8000)
        self.spnonzero=self.sprange
        self.bprange=(4000,10000)
        self.bpnonzero=(5000,6000)
        OVBase.defarrays(self)
        self.cref='full'
        self.sref=True


class SpPartialNz2(OVBase,testutil.FPTestCase):
    #This is still not acceptable:
    #the bandpass is nonzero in places where the spectrum is undefined.
    def setUp(self):
        self.sprange=(1000,8000)
        self.spnonzero=(5000,6000)
        self.bprange=(4000,10000)
        self.bpnonzero=self.bprange
        OVBase.defarrays(self)
        self.cref='partial'
        self.sref=False
## The following test relies on a subsequently abandoned spike
## using this toy wrange class. It doesn't run, so am abandoning it.

#Now let's make some that are complicated
#Use the toy wrange object for this for now.
## import wrange

## class Bpvary(OVBase,testutil.FPTestCase):
##     def setUp(self):
##         self.sprange=(1000,5000)
##         self.spnonzero=self.sprange
##         self.bprange=(4100,5100)
##         self.bpnonzero=self.bprange
##         OVBase.defarrays(self)
##         bp=wrange.Foobar(self.bp.wave,self.bp.throughput)
##         bp[4100:5000]=0.9
##         bp[5000:]=0.001
##         bp[4100]=0
##         bp[5099]=0 #must still use Python range rules
##         self.bp._throughputtable=bp.f

##         self.cref='partial'
##         self.sref=True

##     def testconstructed(self):
##         thru=self.bp.throughput
##         self.assert_(N.all(N.array([.001,.001,0.0]) == thru[-3:]))
