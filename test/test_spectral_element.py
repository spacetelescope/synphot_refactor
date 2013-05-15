import numpy as np

import pysynphot.spectrum as spec
from pysynphot import ObsBandpass

# test that SpectralElement.sample respects internal units
def test_sample_units():
  defwave = np.linspace(0.1, 1, 10)
  defthru = defwave
  
  s = spec.ArraySpectralElement(defwave, defthru, 'm', 'TestArray')
  
  angwave = defwave * 1.e10
  
  np.testing.assert_allclose(s(angwave), s.sample(defwave))


# test that SpectralElement.photbw returns results similar to Synphot
# test for similarity to within 0.1%
def test_photbw_acs_hrc_f555w():
  mode = 'acs,hrc,f555w'
  
  # from Synphot
  ref_photbw = 357.17
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_acs_sbc_f122m():
  mode = 'acs,sbc,f122m'
  
  # from Synphot
  ref_photbw = 91.063
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_acs_wfc1_f775w_pol_v():
  mode = 'acs,wfc1,f775w,pol_v'
  
  # from Synphot
  ref_photbw = 444.05
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_cos_boa_nuv_mirrora():
  mode = 'cos,boa,nuv,mirrora'
  
  # from Synphot
  ref_photbw = 370.65
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_nicmos_1_f090m_dn():
  mode = 'nicmos,1,f090m,dn'
  
  # from Synphot
  ref_photbw = 559.59
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_stis_02x29_mirror_fuvmama():
  mode = 'stis,0.2x29,mirror,fuvmama'
  
  # from Synphot
  ref_photbw = 134.79
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_wfc3_ir_f164n():
  mode = 'wfc3,ir,f164n'
  
  # from Synphot
  ref_photbw = 700.05
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_wfc3_uvis1_f336w():
  mode = 'wfc3,uvis1,f336w'
  
  # from Synphot
  ref_photbw = 158.44
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)


def test_photbw_wfc3_uvis2_f336w():
  mode = 'wfc3,uvis2,f336w'
  
  # from Synphot
  ref_photbw = 158.36
  
  band = ObsBandpass(mode)
  
  test_photbw = band.photbw()
  
  np.testing.assert_allclose(ref_photbw, test_photbw, rtol=0.001)
