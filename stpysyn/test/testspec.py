from __future__ import division
import sys
import os

import numpy as N
from stpysyn.test import testutil
from pysynphot import spectrum
import pysynphot as S
from pysynphot.units import WaveUnits, FluxUnits

## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()



class FitsHdrCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.FileSpectrum(os.path.join(os.path.dirname(__file__),
                                            'data',
                                            'alpha_lyr_stis_002.fits')
                               )

    def testheader(self):
        self.assert_(len(self.sp.fheader) > 0)

    def testhval(self):
        self.assertEqual(self.sp.fheader['TARGETID'],
                         'ALPHA_LYR')

class SpecTestCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                            'calspec',
                                            'alpha_lyr_stis_003.fits'))

    def testwave(self):
        wave=self.sp.wave
        self.assert_(isinstance(wave,N.ndarray))

    def testflux(self):
        flux=self.sp.flux
        self.assert_(isinstance(flux,N.ndarray))

    def testwaveunits(self):
        self.assert_(isinstance(self.sp.waveunits,WaveUnits))

    def testfluxunits(self):
        self.assert_(isinstance(self.sp.fluxunits,FluxUnits))

    def testcalltype(self):
        callval=self.sp(N.arange(3000,10000))
        self.assert_(isinstance(callval,N.ndarray))

    def testcallval(self):
        self.sp.convert('fnu')
        flux=self.sp.flux
        callval=self.sp(self.sp.wave)
        point=len(flux)/2
        self.assert_(flux[point] != callval[point])

    def testcallunits(self):
        self.sp.convert('flam')
        foo=self.sp.flux
        self.sp.convert('photlam')
        callval=self.sp(self.sp.wave)
        flux=self.sp.flux
        self.assert_(N.all(flux == callval))

class ZeroFluxTest(SpecTestCase):
    def setUp(self):
        self.sp=S.ArraySpectrum(N.arange(3000,6000,500),
                                N.array([1.0,0.5,0.2,0.0,0.0,0.0])*1e-14,
                                fluxunits='flam')


    def testcallval(self):
        self.sp.convert('fnu')
        flux=self.sp.flux
        callval=self.sp(self.sp.wave)
        point=len(flux)/2
        #becuase 0 flam does indeed equal 0 fnu
        self.assert_(flux[point] == callval[point])


class NegFluxTest(SpecTestCase):
    def setUp(self):
        self.sp=S.ArraySpectrum(N.arange(3000,6000,500),
                                N.array([1.0,0.5,0.2,0.1,-0.1,-0.3])*1e-14,
                                fluxunits='flam')

class NegFlamTest(NegFluxTest):
    def setUp(self):
        self.sp=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                            'calspec',
                                            'vb8_stisnic_001.fits'))
class NegMagTest(NegFluxTest):
    def setUp(self):
        self.sp=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                            'calobs',
                                            'alpha_lyr_006.fits'))

class GaussianTest(SpecTestCase):
    def setUp(self):
        self.sp=S.GaussianSource(1e-12,5000,30)

class UnitSpecTest(SpecTestCase):
    def setUp(self):
        self.sp=S.FlatSpectrum(10)

class PowerLawTest(SpecTestCase):
    def setUp(self):
        self.sp=spectrum.Powerlaw(6000,3)

class BlackBodyTest(SpecTestCase):
    def setUp(self):
        self.sp=S.BlackBody(60000)

class CompositeAnalTest(SpecTestCase):
    def setUp(self):
        self.sp=S.BlackBody(60000)+S.GaussianSource(1e-12,5000,30)

class CompositeFileTest(SpecTestCase):
    def setUp(self):
        self.comp1=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                            'calspec',
                                            'alpha_lyr_stis_003.fits'))
        self.comp2=S.FlatSpectrum(10)
        self.sp=self.comp1+self.comp2

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__,2)
    else:
        testutil.testall(__name__,2)




