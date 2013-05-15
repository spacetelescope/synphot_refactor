from __future__ import division
"""Tests varying legal cases for ASCII file spectrum data"""
import pysynphot as S
from pysynphot import exceptions
import os, sys
import testutil
import numpy as N

def writedata(fh,start=0,end=4000):
    wave=N.arange(10000,14000,dtype=N.float64)
    flux=N.ones(wave.shape,dtype=N.float64)
    for k in range(start,end):
        fh.write("%f   %f\n"%(wave[k],flux[k]))
    return end-start

def writeinline(fh):
    wave=N.arange(10000,14000,dtype=N.float64)
    flux=N.ones(wave.shape,dtype=N.float64)
    for k in range(len(wave)):
        fh.write("%f   %f   # Line %d\n"%(wave[k],flux[k],k))
    return len(wave)

def write3(fh):
    wave=N.arange(10000,15000,dtype=N.float64)
    flux=N.ones(wave.shape,dtype=N.float64)
    for k in range(len(wave)):
        fh.write("%f   %f   %f\n"%(wave[k],flux[k],wave[k]))
    return len(wave)

class goodcase(testutil.FPTestCase):
    def setUp(self):
        self.fname='goodfile.dat'
        fh=open(self.fname,'w')
        self.len=writedata(fh)
        fh.close()
        self.sp=S.FileSpectrum(self.fname)

    def tearDown(self):
        os.remove(self.fname)

    def testlength(self):
        self.assert_(self.len == len(self.sp.wave))

    def testgarbage(self):
        idx=N.isfinite(self.sp.flux)
        self.assert_(N.all(idx))


class header1(goodcase):
    def setUp(self):
        self.fname='head1.dat'
        fh=open(self.fname,'w')
        fh.write("#   wave      flux\n")
        fh.write("\n")
        self.len=writedata(fh)
        fh.close()
        self.sp=S.FileSpectrum(self.fname)

class header2(goodcase):
    def setUp(self):
        self.fname='head2.dat'
        fh=open(self.fname,'w')
        fh.write("#  1   wave\n")
        fh.write("#  2  flux\n")
        self.len=writedata(fh)
        fh.close()
        self.sp=S.FileSpectrum(self.fname)
class endblank(goodcase):
    def setUp(self):
        self.fname='blank.dat'
        fh=open(self.fname,'w')
        self.len=writedata(fh)
        for k in range(5):
            fh.write("\n")
        fh.close()
        self.sp=S.FileSpectrum(self.fname)

class midcomment(goodcase):
    def setUp(self):
        self.fname='midcomment.dat'
        fh=open(self.fname,'w')
        x1=writedata(fh,end=2000)
        fh.write("#middle of the file\n")
        fh.write("#  yet more middle of the file\n")
        x2=writedata(fh,start=2000)
        fh.close()
        self.len=x1+x2
        self.sp=S.FileSpectrum(self.fname)

class inline(goodcase):
    def setUp(self):
        self.fname='inline.dat'
        fh=open(self.fname,'w')
        self.len=writeinline(fh)
        fh.close()
        self.sp=S.FileSpectrum(self.fname)

class threecolumns(goodcase):
    def setUp(self):
        self.fname='3col.dat'
        fh=open(self.fname,'w')
        self.len=write3(fh)
        fh.close()
        self.sp=S.FileSpectrum(self.fname)

class badline(testutil.FPTestCase):
    def setUp(self):
        self.fname='badline.dat'
        fh=open(self.fname,'w')
        self.len=writedata(fh)
        fh.write("Hello world")
        fh.close()

    def tearDown(self):
        os.remove(self.fname)

    def testerror(self):
        self.assertRaises(exceptions.BadRow,S.FileSpectrum,self.fname)

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__, 2)
