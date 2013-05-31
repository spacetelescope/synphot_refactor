from __future__ import division

import numpy as N

from stpysyn.test import testutil
import pysynphot as S


class FlipTest(testutil.FPTestCase):
    def setUp(self):
        self.waveup=N.arange(10000,10100,10)
        self.wavedown=self.waveup[::-1]
        self.T=N.arange(10)+5
        self.Tflip=self.T.copy()[::-1]
        self.up=S.ArrayBandpass(wave=self.waveup,
                                throughput=self.T)
        self.down=S.ArrayBandpass(wave=self.wavedown,
                                   throughput=self.T[::-1])

    def test1(self):
        "up(waveup)=T)"
        self.assertEqualNumpy(self.up(self.waveup), self.T)

    def test2(self):
        "down(wavedown)=Tflip"
        self.assertEqualNumpy(self.down(self.wavedown), self.Tflip)

    def test3(self):
        "up(wavedown)=Tflip"
        self.assertEqualNumpy(self.up(self.wavedown), self.Tflip)

    def test4(self):
        "down(waveup)=T"
        self.assertEqualNumpy(self.down(self.waveup), self.T)

class FlipSpec(FlipTest):
    def setUp(self):
        self.waveup=N.arange(10000,10100,10)
        self.wavedown=self.waveup[::-1]
        self.T=N.arange(10)+5
        self.Tflip=self.T.copy()[::-1]
        self.up=S.ArraySpectrum(wave=self.waveup,
                                flux=self.T)
        self.down=S.ArraySpectrum(wave=self.wavedown,
                                  flux=self.T[::-1])

class InterpTest(testutil.FPTestCase):
    def setUp(self):
        self.Y=N.arange(10)+5

    def test1(self):
        A=N.arange(10)
        X=N.arange(10)
        ans=N.interp(A,X,self.Y)
        self.assertEqualNumpy(ans,self.Y)

    def test2(self):
        A=N.arange(10)[::-1]
        X=N.arange(10)[::-1]
        ans=N.interp(A[::-1],X[::-1],self.Y[::-1])
        self.assertEqualNumpy(ans,self.Y[::-1])

    def test3(self):
        A=N.arange(10)
        X=N.arange(10)[::-1]
        ans=N.interp(A,X[::-1],self.Y[::-1])
        self.assertEqualNumpy(ans,self.Y[::-1])

    def test4(self):
        A=N.arange(10)[::-1]
        X=N.arange(10)
        ans=N.interp(A[::-1],X,self.Y)
        self.assertEqualNumpy(ans,self.Y)

