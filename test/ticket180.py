from __future__ import division
import sys
import os
import unittest
import testutil
import pysynphot as S
import numpy as N



class AnalyticSP(testutil.FPTestCase):
    @testutil.skip
    def setUp(self):
        self.sp=S.FlatSpectrum(10)

    def testsp(self):
        tst=self.sp(5000)
        self.assert_(tst == 10)

    def testcompspec(self):
        self.sp=S.BlackBody(5500)+S.FlatSpectrum(1)
        tst=self.sp(3000)
        assert True
