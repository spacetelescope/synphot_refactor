from __future__ import division
import sys
import os
import tempfile
import math
import numpy as N
import pysynphot as S
from pysynphot import locations
from pysynphot.catalog import Icat
from pysynphot import spparser as P

import testutil 

#Places used by test code
userdir   = os.path.join(os.path.dirname(__file__),'data')
testdata  = os.path.join(locations.rootdir,'calspec','feige66_002.fits')


class WriteTestCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(10000)

    def testwrite(self):
        self.fname=os.path.basename(self.sp.name)+'.fits'
        self.sp.writefits(self.fname)

    def tearDown(self):
        os.remove(self.fname)

class ExtTestCase(WriteTestCase):
    def setUp(self):
        self.sp=P.interpret(P.parse(P.scan('ebmvx(0.5,gal1)')))

class FileSpecCase(WriteTestCase):
    def setUp(self):
        self.sp=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                        'calspec',
                                        'feige66_002.fits'))

class ArraySpCase(WriteTestCase):
    def setUp(self):
        self.sp=S.ArraySpectrum(N.arange(1,10000),
                                N.arange(9999)*2.5)
class FileBandCase(WriteTestCase):
    def setUp(self):
        self.sp=S.FileBandpass(os.path.join(os.environ['PYSYN_CDBS'],
                                            'comp',
                                            'nonhst',
                                            'johnson_v_003_syn.fits'))

class ObsBandCase(WriteTestCase):
    def setUp(self):
        self.sp=S.ObsBandpass('acs,hrc,f555w')

class UnitCase(WriteTestCase):
    def setUp(self):
        self.sp=S.FlatSpectrum(10.0,fluxunits='flam')

class PLCase(WriteTestCase):
    def setUp(self):
        self.sp=S.PowerLaw(10000,0.5)

class GaussianCase(WriteTestCase):
    def setUp(self):
        self.sp=S.GaussianSource(1e14,10000,10)

class CompSpecCase(WriteTestCase):
    def setUp(self):
        self.sp=S.BlackBody(10000)*S.ObsBandpass('acs,hrc,f555w')

class CompBpCase(WriteTestCase):
    def setUp(self):
        self.sp=S.ObsBandpass('acs,hrc,f555w')*S.FileBandpass((os.path.join(os.environ['PYSYN_CDBS'],
                                            'comp',
                                            'nonhst',
                                            'johnson_b_003_syn.fits')))

class IcatCase(WriteTestCase):
    def setUp(self):
        self.sp=Icat('k93models',3500,0.0,4.6)

class UniformBandCase(WriteTestCase):
    def setUp(self):
        self.sp=S.spectrum.UniformTransmission(0.7)

class BoxCase(WriteTestCase):
    def setUp(self):
        self.sp=S.spectrum.Box(7000,13.5)

class InterpCase(WriteTestCase):
    def setUp(self):
        self.sp=S.ObsBandpass('acs,hrc,f555w,mjd#54000')
        
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        result=testutil.testall(__name__,2)
