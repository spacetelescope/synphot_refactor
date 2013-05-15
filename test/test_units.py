from __future__ import division

import testutil
import numpy as N
import unittest

from pysynphot.spectrum import ArraySourceSpectrum as ArraySpectrum
from pysynphot import extinction, spectrum, refs
from pysynphot import BlackBody

# Code Under Test:
from pysynphot import units

class AddInverseMicron(testutil.FPTestCase):
    def setUp(self):
        self.x=units.Units('1/um')
        self.mwave=extinction._buildDefaultWaveset()[0:10]
        self.awave=(refs._default_waveset.copy()[::10])[0:10]
        
    def teststr(self):
        self.failUnless(str(self.x)=='1/um')

    def testunittoang(self):
        test=self.x.Convert(self.mwave,'angstrom')
        self.assertApproxNumpy(test,self.awave)

    def testunitfromang1(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'1/um')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang2(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'InverseMicron')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang3(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'inversemicrons')
        self.assertApproxNumpy(test,self.mwave)
        
        
    def testfromang(self):
        test=ArraySpectrum(wave=self.awave,
                             flux=N.ones(self.awave.shape),
                             waveunits='angstrom',
                             fluxunits='flam')
        test.convert('1/um')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertApproxNumpy(test.wave,self.mwave)

    def testcreate(self):
        test=ArraySpectrum(wave=self.mwave,
                             flux=N.ones(self.mwave.shape),
                             waveunits='1/um',
                             fluxunits='flam')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertEqualNumpy(test.wave,self.mwave)
                        
    def testtoang(self):
        test=ArraySpectrum(wave=self.mwave,
                            flux=N.ones(self.mwave.shape),
                            waveunits='1/um',
                            fluxunits='flam')
        
        test.convert('angstrom')
        self.failUnless(isinstance(test.waveunits,units.Angstrom))
        self.assertApproxNumpy(test.wave,self.awave)
                                                

class TestmuJy(testutil.FPTestCase):

    """Tests certain attributes of the micro Jansky (muJy)
       class, including how the units are referenced, and 
       the conversion to and from the units.
    """

    # The tests below for the muJy class are in partial fulfillment of Ticket #102

    def setUp(self):
        self.x=units.Units('mujy')

        # creates a 10 element array of simulated wavelength values in Angstroms
        self.awave=(refs._default_waveset.copy()[::10])[0:10]

        # Creates a 10 element array of ones
        self.flux=N.ones(self.awave.shape)

        # Create reference values based on Jansky class to 
        # be used in verifying the Micro Jansky class
        self.ref_photlam=units.Units('jy').ToPhotlam(self.awave,self.flux)*(1.0e-6)
        
        self.ref_mujy=units.Units('photlam').ToJy(self.awave,self.flux)*(1.0e6)

    def teststr(self):
        # Verify that units entered are correct
        self.failUnless(str(self.x)=='mujy')

    def testunittophotlam(self):
        # Verify that the conversion from muJy to photlam is correct
        test=self.x.ToPhotlam(self.awave,self.flux)
        self.assertApproxNumpy(self.ref_photlam,test)
        
    def testfromphotlam1(self):
        # Verify that the conversion from photlam to muJy is correct
        photlam=units.Units('photlam')
        test=photlam.Convert(self.awave,self.flux,'mujy')
        print ' '
        print 'TEST: ',test
        print ' '
        print 'SELF REF MUJY: ',self.ref_mujy
        print ' '
        self.assertApproxNumpy(test,self.ref_mujy)

    def testfromphotlam2(self):
        # Verify that the conversion from photlam to muJy is correct
        photlam=units.Units('photlam')
        test=photlam.Convert(self.awave,self.flux,'microjy')
        self.assertApproxNumpy(test,self.ref_mujy)

    def testfromphotlam3(self):
        # Verify that the conversion from photlam to muJy is correct
        photlam=units.Units('photlam')
        test=photlam.Convert(self.awave,self.flux,'ujy')
        self.assertApproxNumpy(test,self.ref_mujy)


class TestnJy(testutil.FPTestCase):

    """Tests certain attributes of the nano Jansky (nJy)
       class, including how the units are referenced, and 
       the conversion to and from the units.
    """

    # The tests below for the nJy class are in partial fulfillment of Ticket #102

    def setUp(self):
        self.x=units.Units('njy')

        # creates a 10 element array of simulated wavelength values in Angstroms
        self.awave=(refs._default_waveset.copy()[::10])[0:10]

        # Creates a 10 element array of ones
        self.flux=N.ones(self.awave.shape)

        # Create reference values based on Jansky class to 
        # be used in verifying the Nano Jansky class
        self.ref_photlam=units.Units('jy').ToPhotlam(self.awave,self.flux)*(1.0e-9)

        self.ref_njy=units.Units('photlam').ToJy(self.awave,self.flux)*(1.0e9)

    def teststr(self):
        # Verify that units entered are correct
        self.failUnless(str(self.x)=='njy')

    def testunittophotlam(self):
        # Verify that the conversion from muJy to photlam is correct
        test=self.x.ToPhotlam(self.awave,self.flux)
        self.assertApproxNumpy(self.ref_photlam,test)
        
    def testfromphotlam1(self):
        # Verify that the conversion from photlam to muJy is correct
        photlam=units.Units('photlam')
        test=photlam.Convert(self.awave,self.flux,'njy')
        self.assertApproxNumpy(test,self.ref_njy)

    def testfromphotlam2(self):
        # Verify that the conversion from photlam to muJy is correct
        photlam=units.Units('photlam')
        test=photlam.Convert(self.awave,self.flux,'nanojy')
        self.assertApproxNumpy(test,self.ref_njy)


class TestXJanskyTypicalUse(testutil.FPTestCase):

    """Tests normal use attributes of the muJy and nJy classes in
       relation to a larger portion of the code base, to verify 
       output, from a broader perspective, and values as they
       should appear, based on how the functions within the classes 
       are referenced and how they are converted.
    """

    # The general tests below for the muJy and nJy classes are in partial fulfillment of Ticket #102

    def setUp(self):
        self.bb = BlackBody(5500)
        self.bb.convert('jy')
        self.wave=self.bb.wave
        self.flux=self.bb.flux

    def testfluxconvert1(self):
        ref_flux=self.flux*1.0e6
        self.bb.convert('mujy')
        test_flux=self.bb.flux
        self.assertApproxNumpy(test_flux,ref_flux)
        
    def testfluxconvert2(self):
        ref_flux=self.flux*1.0e9
        self.bb.convert('njy')
        test_flux=self.bb.flux
        self.assertApproxNumpy(test_flux,ref_flux)
        
    def testwaveconvert1(self):
        self.bb.convert('mujy')
        test_wave=self.bb.wave
        self.assertApproxNumpy(test_wave,self.wave)
        
    def testwaveconvert2(self):
        ref_flux=self.flux*1.0e9
        self.bb.convert('njy')
        test_flux=self.bb.flux
        self.assertApproxNumpy(test_flux,ref_flux)

    def testunitstring1(self):
        self.bb.convert('mujy')
        test_units=str(self.bb.fluxunits)
        ref_units='mujy'
        self.failUnless(ref_units == test_units)

    def testunitstring2(self):
        self.bb.convert('microjy')
        test_units=str(self.bb.fluxunits)
        ref_units='mujy'
        self.failUnless(ref_units == test_units)

    def testunitstring3(self):
        self.bb.convert('ujy')
        test_units=str(self.bb.fluxunits)
        ref_units='mujy'
        self.failUnless(ref_units == test_units)

    def testunitstring4(self):
        self.bb.convert('njy')
        test_units=str(self.bb.fluxunits)
        ref_units='njy'
        self.failUnless(ref_units == test_units)

    def testunitstring5(self):
        self.bb.convert('nanojy')
        test_units=str(self.bb.fluxunits)
        ref_units='njy'
        self.failUnless(ref_units == test_units)

    def testfluxattribute(self):
        self.bb.convert('mujy')
        mflux=self.bb.flux

        self.bb.convert('njy')
        nflux=self.bb.flux

        ref=1000.0
        test_ratio=nflux/mflux
        test=test_ratio.mean()

        self.assertApproxNumpy(test,ref)
