from __future__ import division
import os

import pyfits
import numpy as N

from stpysyn.test import testutil
import pysynphot as S
from pysynphot import spparser, exceptions


class Precision(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5000)

    def tearDown(self):
        os.unlink(self.fname)

    def testsingle(self):
        self.fname='/tmp/spsingle.fits'
        self.sp.writefits(self.fname,precision='single')
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'e')

    def testdouble(self):
        self.fname='/tmp/spdouble.fits'
        self.sp.writefits(self.fname,precision='double')
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'd')

    def testdefault(self):
        self.fname='/tmp/spdefault.fits'
        self.sp.writefits(self.fname)
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'd')

class PrecisionBP(Precision):
    def setUp(self):
        self.sp=S.ObsBandpass('acs,hrc,f555w')


class Sorted(testutil.FPTestCase):
    def setUp(self):
        self.fname='/tmp/epsilon.fits'
        self.old_cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        self.obsmode='wfc3,ir,f160w'
        self.spstring='rn(spec(data/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)'
        self.sp=spparser.parse_spec(self.spstring)
        self.sp.writefits(self.fname,precision='single')

    def tearDown(self):
        os.unlink(self.fname)
        os.chdir(self.old_cwd)

    def testoutputfix(self):
        sp=S.FileSpectrum(self.fname)
        idx=N.where(sp.wave == 500)
        num=len(idx[0])
        self.failIf(num != 1, "%d occurrences found"%num)

    def testinputfix(self):
        self.assertRaises(exceptions.DuplicateWavelength,
                          S.ArraySpectrum,
                          wave=N.array([1,2,3,4,4,5]),
                          flux=N.ones(6))

class SortedBP(Sorted):
    def setUp(self):
        self.fname='/tmp/bpesp.fits'
        self.bp=S.ArrayBandpass(wave=N.array([1,2,3,4,4.0000001,5]),
                                throughput=N.ones(6))
        self.bp.writefits(self.fname,precision='single')

    def tearDown(self):
        os.unlink(self.fname)

    def testoutputfix(self):
        bp=S.FileBandpass(self.fname)
        idx=N.where(bp.wave == 4)
        num=len(idx[0])
        self.failIf(num != 1, "%d occurrences found"%num)

    def testinputfix(self):
        self.assertRaises(exceptions.DuplicateWavelength,
                          S.ArrayBandpass,
                          wave=N.array([1,2,3,4,4,5]),
                          throughput=N.ones(6))
