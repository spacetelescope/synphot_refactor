from __future__ import division
import os
import sys

import numpy as N

import pysynphot as S
from pysynphot.observation import Observation
from stpysyn.test import testutil


orig_ref = S.refs.getref()
testdir = os.path.join(os.path.dirname(__file__), 'data')


def setUpModule():
    #Specify a TMC file
    S.setref(comptable='mtab$t921857im_tmc.fits')


def tearDownModule():
    S.setref(comptable=orig_ref['comptable'])


class Keepneg(testutil.FPTestCase):
    def setUp(self):
        self.fname=os.path.join(testdir, 'data/us7.txt')
        self.refrate=2303.5 #provided by C. Oliveira
        self.bp=S.ObsBandpass('cos,fuv,g130m,c1309,psa')

    def testclip(self):
        self.sp=S.FileSpectrum(self.fname)
        self.obs=Observation(self.sp,self.bp)
        rate=self.obs.countrate()

        self.assert_(abs(rate-self.refrate)<1.0, msg="tst %f ref %f"%(rate,self.refrate))

    def testkeeprate(self):
        self.sp=S.FileSpectrum(self.fname,keepneg=True)
        self.obs=Observation(self.sp,self.bp)
        rate=self.obs.countrate()
        self.assert_(rate < self.refrate)

    def testkeepmin(self):
        self.sp=S.FileSpectrum(self.fname,keepneg=True)
        self.obs=Observation(self.sp,self.bp)
        self.assert_(self.obs.flux.min() < 0)

    def testarray(self):
        waves=N.arange(1000,6000,1000)
        flux=N.array([1.0,0.5,-0.5,0.75,1.0])
        self.sp=S.ArraySpectrum(wave=waves,flux=flux)
        self.assertEqual(self.sp.flux[2],0.0)



    def testarraykeep(self):
        waves=N.arange(1000,6000,1000)
        flux=N.array([1.0,0.5,-0.5,0.75,1.0])
        self.sp=S.ArraySpectrum(wave=waves,flux=flux,keepneg=True)
        self.assertEqual(self.sp.flux[2],-0.5)

    def testmagarray(self):
        waves=N.arange(1000,6000,1000)
        flux=N.array([1.0,0.5,-0.5,0.75,1.0])
        self.sp=S.ArraySpectrum(wave=waves,flux=flux,fluxunits='ABMag')
        self.assertAlmostEqual(self.sp.flux[2],-0.5,4)


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__, 2)

