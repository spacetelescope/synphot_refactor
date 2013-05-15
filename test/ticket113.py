from __future__ import division
import sys
import os
import math
import numpy as N
import pysynphot as S
from pysynphot import locations
from pysynphot.catalog import Icat
from pysynphot import spparser as P

import testutil

class UnixCase(testutil.FPTestCase):
    def setUp(self):
        self.fname="/a/b/c/foo.fits"


    def testval(self):
        self.tokens=[self.fname]
        x=P.scan(self.fname)
        self.assertEqual(x[0].attr,self.tokens[0])

    def testlen(self):
        self.tokens=[self.fname]
        x=P.scan(self.fname)
        self.assertEqual(len(x),len(self.tokens))

class WindowsCase(UnixCase):
    def setUp(self):
        self.fname='C:/a/b/c/foo.fits'

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        result=testutil.testall(__name__,2)
