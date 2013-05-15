from __future__ import division
import sys
import os
import math

import numpy as N
import pyfits
import testutil
from pysynphot import units, locations, spectrum, refs
from pysynphot.obsbandpass import ObsBandpass
import pysynphot as S

## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()

class MergeTestCase(testutil.FPTestCase):
    """Demonstrate the problem described in ticket #34:
    Adding two identical tabular spectra loses a pixel in the resulting
    spectrum's table."""

    def testwave(self):
        """tickettest.MergeTestCase('testwave'): merge simple identical wavesets: #34"""
        foo=N.array(range(10,20),dtype=N.float64)
        x=spectrum.MergeWaveSets(foo,foo)
        self.assertEqualNumpy(foo,x)

class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
        self.sp = S.FileSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)

    def testwave(self):
        "ui_test.FileTestCase('testwave'): r164 wave"
        fitswave=self.openfits[1].data.field('wavelength')
        self.assertEqualNumpy(self.sp.wave, fitswave)

    def testflux(self):
        "ui_test.FileTestCase('testflux'): r164 flux"
        fitsflux=self.openfits[1].data.field('flux')
        self.assertApproxNumpy(self.sp.flux, fitsflux)

    def testname(self):
        "ui_test.FileTestCase('testname'): Tests r163"
        self.assert_(str(self.sp) == self.fname)
        self.assert_(self.sp.name == self.fname)

    def testresample(self):
        "ui_test.FileTestCase('testresample'): Tests #24"
        sp2=self.sp.resample(N.arange(10000,18000,2))
        self.failIf(sp2.fluxunits is None)
        #self.assertEqualNumpy(sp2.wave, N.arange(10000,18000,2))

    def testadd(self):
        "ui_test.FileTestCase('testadd'): Add two spectra"
        sp2=self.sp + self.sp
        sumflux = self.sp.flux + self.sp.flux
        self.assertEqualNumpy(sp2.flux,sumflux)

    def testmul(self):
        "ui_test.FileTestCase('testmul'): Multiply flux by band"
        bp=S.spectrum.Box(3000,50)
        sp1=self.sp * bp
        sp2=bp*self.sp
        self.assertEqualNumpy(sp1.flux,sp2.flux)

    def tearDown(self):
        self.openfits.close()

class TabTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
        self.old_sp = S.FileSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)
        fdata=self.openfits[1].data
        self.new_sp = S.ArraySpectrum(wave=fdata.field('wavelength'),
                                      flux=fdata.field('flux'),
                                      waveunits=self.openfits[1].header['tunit1'],
                                      fluxunits=self.openfits[1].header['tunit2'],
                                      name='table from feige66')


    def testwave(self):
        "ui_test.TabTestCase('testwave'): .wave equal"
        self.assertEqualNumpy(self.new_sp.wave, self.old_sp.wave)

    def testflux(self):
        "ui_test.TabTestCase('testflux'): .flux equal"
        self.assertEqualNumpy(self.new_sp.flux, self.old_sp.flux)

    def testwaveunits(self):
        "ui_test.TabTestCase('testwaveunits'): waveunits equal"
        self.assert_(type(self.new_sp.waveunits) == type(self.old_sp.waveunits))

    def testfluxunits(self):
        "ui_test.TabTestCase('testfluxunits'): fluxunits equal"
        self.assert_(type(self.new_sp.fluxunits) == type(self.old_sp.fluxunits))

    def testinternalwave(self):
        "ui_test.TabTetstCase('testinternalwave'): wavetabs equal"
        self.assertEqualNumpy(self.new_sp._wavetable, self.old_sp._wavetable)

    def testinternalflux(self):
        "ui_test.TabTestCase('testinternalflux)'): int. flux equal"
        self.assertEqualNumpy(self.new_sp._fluxtable, self.old_sp._fluxtable\
                                      )

    def testconvertflux(self):
        "ui_test.TabTestCase('testconvertflux'): convert the same way"
        self.old_sp.convert('vegamag')
        self.new_sp.convert('vegamag')
        self.assertEqualNumpy(self.new_sp.flux,self.old_sp.flux)


    def tearDown(self):
        self.openfits.close()

class FSSTestCase(testutil.FPTestCase):
    "Test operations on a FileSourceSpectrum"
    def setUp(self):
        self.fname = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
        self.old_sp = spectrum.TabularSourceSpectrum(self.fname)
        self.new_sp = spectrum.FileSourceSpectrum(self.fname)

    def testwave(self):
        "ui_test.FSSTestCase('testwave'): .wave equal"
        self.assertEqualNumpy(self.new_sp.wave, self.old_sp.wave)

    def testflux(self):
        "ui_test.FSSTestCase('testflux'): .flux equal"
        self.assertEqualNumpy(self.new_sp.flux, self.old_sp.flux)

    def testwaveunits(self):
        "ui_test.FSSTestCase('testwaveunits'): waveunits equal"
        self.assert_(type(self.new_sp.waveunits) == type(self.old_sp.waveunits))

    def testfluxunits(self):
        "ui_test.FSSTestCase('testfluxunits'): fluxunits equal"
        self.assert_(type(self.new_sp.fluxunits) == type(self.old_sp.fluxunits))

    def testinternalwave(self):
        "ui_test.FSSTestCase('testinternalwave'): waveteable equal"
        self.assertEqualNumpy(self.new_sp._wavetable, self.old_sp._wavetable)

    def testinternalflux(self):
        "ui_test.FSSTestCase('testinternalflux)'): int. flux equal"
        self.assertEqualNumpy(self.new_sp._fluxtable, self.old_sp._fluxtable)

    def testconvertflux(self):
        "ui_test.FSSTestCase('testconvertflux'): convert the same way"
        self.old_sp.convert('vegamag')
        self.new_sp.convert('vegamag')
        self.assertEqualNumpy(self.new_sp.flux,self.old_sp.flux)


class BandTestCase(testutil.FPTestCase):
    def setUp(self):
        cmptb_name=os.path.join('mtab','r1j2146sm_tmc.fits')
        self.old_comptable = refs.COMPTABLE
        refs.COMPTABLE = locations._refTable(cmptb_name)
        print "ui_Test.BandTests:"
        print "  Tests are being run with comptable",refs.COMPTABLE
        print "  Comparison results were computed with r1j2146sm_tmc.fits"

    def tearDown(self):
        refs.COMPTABLE = self.old_comptable

    def testomfail(self):
        "ui_test.BandTestCase('testomfail'): Tests #30"
        bp1=ObsBandpass('johnson,v')

    def testompass(self):
        "ui_test.BandTestCase('testompass'): Tests r172"
        bp1=ObsBandpass('acs,hrc,f555w')
        self.assert_(len(bp1) == 6)

class UnitTestCase(testutil.FPTestCase):
    def setUp(self):
        self.uspec=S.FlatSpectrum(1.0,fluxunits='flam')

    def testfnu(self):
        """Converted to fnu, it should not be flat.
        Can't test against 1.0 because there's computations & some
        numerical issues."""
        self.uspec.convert('fnu')
        self.failIf(self.uspec.flux.mean() == 1.0)

class EnforceUnitsCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(30000)
        self.waveunits='flam'
        self.fluxunits='angstrom'

    def testwavetype(self):
        """Make sure waveunits are really waveunits"""
        self.assertRaises(TypeError,
                          S.ArraySpectrum,
                          self.sp.wave,self.sp.flux,
                          self.waveunits)


    def testfluxtype(self):
        """Make sure fluxunits are really fluxunits"""
        self.assertRaises(TypeError,
                          S.ArraySpectrum,
                          self.sp.wave,self.sp.flux,
                          'angstrom',self.fluxunits)

class TabularCase(testutil.FPTestCase):
    """Test new ArraySpectrum inheriting from TabularSourceSpectrum"""
    def setUp(self):
        self.inwave=S.Waveset(1300,1800)
        self.influx=-2.5*N.log10(self.inwave**2)
        self.sp=S.ArraySpectrum(wave=self.inwave,flux=self.influx,
                                fluxunits='abmag')

    def testarrays(self):
        self.assertApproxNumpy(self.inwave,self.sp.wave)
        self.assertApproxNumpy(self.influx,self.sp.flux)

    def testunits(self):
        self.assert_(isinstance(self.sp.waveunits,units.Angstrom))
        self.assert_(isinstance(self.sp.fluxunits, units.ABMag))

    def testconvert(self):
        self.sp.convert('flam')
        self.failIf(N.any(self.influx == self.sp.flux))

    def teststring(self):
        foo=str(self.sp)

class Tab2(TabularCase):
    def setUp(self):
        self.inwave=S.Waveset(1300,1800)
        self.influx=N.random.lognormal(size=len(self.inwave))*1e-15
        self.sp=S.ArraySpectrum(wave=self.inwave,flux=self.influx,
                                waveunits='nm',fluxunits='fnu',
                                name='Tab2 spectrum')

    def testunits(self):
        self.assert_(isinstance(self.sp.waveunits,units.Nm))
        self.assert_(isinstance(self.sp.fluxunits, units.Fnu))

    def teststring(self):
        self.assert_(str(self.sp) == 'Tab2 spectrum')

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)
