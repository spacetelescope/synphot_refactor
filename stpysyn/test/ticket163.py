from __future__ import division

# STDLIB
import os
import unittest

# ASTROPY
from astropy.io import fits

# PYSYNPHOT
import pysynphot as S


class TestSpecCase(object):
    @classmethod
    def setUpClass(cls):
        #Write the file
        cls.sp=S.BlackBody(5500)
        cls.fname='/tmp/t163_spcase.fits'
        cls.sp.writefits(cls.fname)
        #Read the header
        cls.f=fits.open(cls.fname)
        cls.h0 = cls.f[0].header
        cls.h1 = cls.f[1].header

    @classmethod
    def tearDownClass(cls):
        cls.f.close()
        os.unlink(cls.fname)

    def testorigin(self):
        assert('origin' in self.h0)

    def testfname(self):
        assert(os.path.basename(self.fname) == self.h0['filename'])

        #test value of origin?
        #test for FITS-y comments?

    def testexpr(self):
        assert((str(self.sp)) == self.h1['expr'])

    def testformat(self):
        assert('G15.7' == self.h1['tdisp1'].strip().upper())
        #test value of graph, comptables?


class TestBandCase(TestSpecCase):

    @classmethod
    def setUpClass(cls):
        #Write the file
        #Warning, lying variable names!
        cls.sp=S.ObsBandpass('acs,hrc,f555w')
        cls.fname='/tmp/t163_bpcase.fits'
        cls.sp.writefits(cls.fname)
        #Read the header
        cls.f=fits.open(cls.fname)
        cls.h0 = cls.f[0].header
        cls.h1 = cls.f[1].header

    def testgrf(self):
        assert('grftable' in self.h1)

    def testcmp(self):
        assert('cmptable' in self.h1)


class TestKeywords(object):

    @classmethod
    def setUpClass(cls):
        #Write the file
        cls.sp=S.BlackBody(5500)
        cls.fname='/tmp/t163_spcase.fits'
        cls.addkeys = dict(sptype=('blackbody','Type of spectrum'),
                           bbtemp=(5500,))
        cls.sp.writefits(cls.fname, hkeys=cls.addkeys)
        #Read the header
        cls.f=fits.open(cls.fname)
        cls.h0 = cls.f[0].header

    @classmethod
    def tearDownClass(cls):
        cls.f.close()
        os.unlink(cls.fname)

    def testkeys(self):
        for k,v in self.addkeys.items():
            def keycheck(k,v):
                assert self.h0[k] == v[0]
            keycheck.name = 'testkeys_%s'%k
            keycheck.description = keycheck.name
            yield keycheck, k, v
