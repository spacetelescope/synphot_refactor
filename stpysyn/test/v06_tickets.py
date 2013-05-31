from __future__ import division
import unittest

import numpy as N

from stpysyn.test import testutil
import pysynphot as S


class AnalyticBP(testutil.FPTestCase):

    def setUp(self):
        self.bp=S.Box(10000,100)

    def testbp1(self):
        tst=self.bp(10000)
        self.assert_(tst == 1.0)

    def testconstant(self):
        bp2 = self.bp * 3
        tst = bp2(10000)
        self.assert_(tst == 3)

    def testbp2(self):
        tst=self.bp(3000)
        self.assert_(tst == 0.0)

    def testbp3(self):
        tst=self.bp.sample(10000)
        self.assert_(tst == 1.0)

    def testbp4(self):
        tst=self.bp.sample(3000)
        self.assert_(tst == 0.0)

    def testflat(self):
        self.bp = S.UniformTransmission(0.5)
        tst = self.bp.sample(3000)
        self.assert_(tst == 0.5)



class Tabular(testutil.FPTestCase):
    def setUp(self):
        #Make arrays
        self.wv = N.arange(1000,2000)
        self.fl = N.zeros(self.wv.shape)
        self.fl[100:-100] = 10.0

    def testsp(self):
        self.sp=S.ArraySpectrum(self.wv,self.fl,
                                fluxunits='photlam')
        tst=self.sp(1500)
        self.assert_(tst == 10)

    def testcompsp(self):
        sp1=S.ArraySpectrum(self.wv,self.fl, fluxunits='photlam')
        sp2=S.ArraySpectrum(self.wv[48:],self.fl[48:]*2.3,
                            fluxunits='photlam')
        self.sp=sp1 + sp2
        tst=self.sp(1500)
        self.assert_(tst == 10+(10*2.3))


    def testbp(self):
        self.bp=S.ArrayBandpass(self.wv,self.fl)
        tst=self.bp(1500)
        self.assert_(tst == 10)

class TestDoesntError(unittest.TestCase):
    #Just test to make sure it doesn't raise an exception;
    #don't test that the actual value is correct

    def testobsband(self):
        self.bp=S.ObsBandpass('acs,hrc,f555w')
        tst=self.bp(3000)
        assert True


    def testicat(self):
        self.sp=S.Icat('k93models',4500,1,2)
        tst=self.sp(3000)
        assert True
