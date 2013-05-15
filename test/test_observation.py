from __future__ import division

# tests for the observation.Observation class

import os.path
import unittest

import numpy as np

import pysynphot as S
from pysynphot import Observation, ObsBandpass, FlatSpectrum
from pysynphot import locations

import testutil

# test the Observaion.initbinflux method
class BinFluxCase(testutil.FPTestCase):
  def setUp(self):
    tmg = locations._refTable(os.path.join('mtab','u921351jm_tmg.fits'))
    tmc = locations._refTable(os.path.join('mtab','ub31649mm_tmc.fits'))
    
    spec = FlatSpectrum(1,fluxunits='flam')
    bandpass = ObsBandpass('acs,hrc,f555w',graphtable=tmg,comptable=tmc)
    
    self.obs = Observation(spec,bandpass)
    self.obs.initbinflux()
    
  def test_binflux(self): 
    front10 = np.zeros(10)
    back10 = np.zeros(10)
    mid10 = np.array([ 0.12265425,  0.12226972,  0.12184207,  0.12141429,  0.12098646,
        0.1205586 ,  0.1201307 ,  0.11970269,  0.11927488,  0.11884699])
        
    binflux = self.obs.binflux
    
    self.assertEqualNumpy(front10,binflux[:10])
    self.assertEqualNumpy(back10,binflux[-10:])
    self.assertApproxNumpy(mid10,binflux[5000:5010])
    
  def test_binedges(self):
    front10 = np.array([  999.5,  1000.5,  1001.5,  1002.5,  1003.5,  1004.5,  1005.5,
        1006.5,  1007.5,  1008.5])
    back10 = np.array([ 10991.5,  10992.5,  10993.5,  10994.5,  10995.5,  10996.5,
        10997.5,  10998.5,  10999.5,  11000.5])
    mid10 = np.array([ 5999.5,  6000.5,  6001.5,  6002.5,  6003.5,  6004.5,  6005.5,
        6006.5,  6007.5,  6008.5])
        
    bin_edges = self.obs._bin_edges
    
    self.assertEqualNumpy(front10,bin_edges[:10])
    self.assertEqualNumpy(back10,bin_edges[-10:])
    self.assertEqualNumpy(mid10,bin_edges[5000:5010])


# test for changes in ticket #198
# test the the bandpass .binset is the same as the Observation .binwave.
# should be since one comes from the other. also verifies that the bandpass
# has the .binset attribute, which is new in the fix to ticket 198.
def test_observation_binset():
  bp = S.ObsBandpass('acs,hrc,f555w')
  
  spec = S.FlatSpectrum(1)
  
  obs = S.Observation(spec,bp)
  
  assert (bp.binset == obs.binwave).all()
  
  
# test the Observation.pixel_range() and .wave_range() methods
class TestPixelWaveRangeMethods(unittest.TestCase):
  def setUp(self):
    bp = S.ObsBandpass('acs,hrc,f555w')
    spec = S.FlatSpectrum(1)
    
    self.obs = S.Observation(spec,bp)
    
  def test_pixel_range_waveunits(self):
    num = self.obs.pixel_range((499.95,500.05),waveunits='nm',round='round')
    self.assertEqual(num,1)
    
  def test_wave_range_waveunits(self):
    w1, w2 = self.obs.wave_range(500,2,waveunits='nm',round=None)
    self.assertEqual(w1,499.9)
    self.assertEqual(w2,500.1)
  
# test the multiplication (supported) and addition (disabled)

class TestArithmetic(unittest.TestCase):
  def setUp(self):
    sp = S.FlatSpectrum(1, fluxunits='counts')
    bp = S.Box(5000,100)
    binset = S.Waveset(1000,10000,1)
    self.obs = S.Observation(sp,bp,binset=binset)
    self.obs.convert('counts')

  def test_class(self):
    self.assert_(isinstance(self.obs, Observation))

  def test_mult_scalar(self):
    tst = self.obs*3
    self.assertAlmostEqual(tst.sample(5000), 3*self.obs.sample(5000))
    self.assertEqual(tst.sample(1000), 0)



  def test_mult_band(self):
    tst = self.obs * (S.Box(5000,1000)* 5)
    self.assertAlmostEqual(tst.sample(5000), 5*self.obs.sample(5000))
    self.assertEqual(tst.sample(1000), 0)


  def test_add_scalar(self):

    # is not allowed
    self.assertRaises(NotImplementedError,
                      self.obs.__add__,
                      3)

  def test_add_spectrum(self):
    # is not allowed
    wv=S.Waveset(1000,10000,1)
    other = S.ArraySpectrum(wave=wv,
                            flux=np.zeros(wv.shape)+10,
                            waveunits='angstroms',
                            fluxunits='counts')
    self.assertRaises(NotImplementedError,
                      self.obs.__add__,
                      other)

