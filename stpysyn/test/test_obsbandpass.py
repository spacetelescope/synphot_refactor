import unittest
import nose.tools

import pysynphot as S
import pysynphot.pysynexcept as exceptions

from pysynphot.obsbandpass import pixel_range, wave_range
from stpysyn.test import testutil

# test the obsbandpass.pixel_range() function
class TestPixelRangeFunc(unittest.TestCase):
  def setUp(self):
    bp = S.ObsBandpass('acs,hrc,f555w')
    self.bins = bp.binset

  def test_round_exception(self):
    self.assertRaises(ValueError, pixel_range, self.bins, (5000,5001), round='up')

  def test_low_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, pixel_range, self.bins, (500,5001))

  def test_high_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, pixel_range, self.bins, (5000,50010))

  def test_pixel_range_round_return0(self):
    num = pixel_range(self.bins,(5000,5000),round='round')
    self.assertEqual(num,0)

  def test_pixel_range_round_return1(self):
    num = pixel_range(self.bins,(4999.5,5000.5),round='round')
    self.assertEqual(num,1)

  def test_pixel_range_round_return2(self):
    num = pixel_range(self.bins,(5000,5002),round='round')
    self.assertEqual(num,2)

  def test_pixel_range_round_return9(self):
    num = pixel_range(self.bins,(4999.6,5008.8),round='round')
    self.assertEqual(num,9)

  def test_pixel_range_min_return1(self):
    num = pixel_range(self.bins,(5000,5002),round='min')
    self.assertEqual(num,1)

  def test_pixel_range_min_return2(self):
    num = pixel_range(self.bins,(5000.5,5002.5),round='min')
    self.assertEqual(num,2)

  def test_pixel_range_min_return3(self):
    num = pixel_range(self.bins,(5000.5,5004.4),round='min')
    self.assertEqual(num,3)

  def test_pixel_range_min_return4(self):
    num = pixel_range(self.bins,(5000.2,5004.5),round='min')
    self.assertEqual(num,4)

  def test_pixel_range_max_return1(self):
    num = pixel_range(self.bins,(5000,5000.1),round='max')
    self.assertEqual(num,1)

  def test_pixel_range_max_return2(self):
    num = pixel_range(self.bins,(5000.5,5002.5),round='max')
    self.assertEqual(num,2)

  def test_pixel_range_max_return3(self):
    num = pixel_range(self.bins,(5000.5,5002.6),round='max')
    self.assertEqual(num,3)

  def test_pixel_range_max_return4(self):
    num = pixel_range(self.bins,(5001.2,5004.5),round='max')
    self.assertEqual(num,4)

  def test_pixel_range_None_return01(self):
    num = pixel_range(self.bins,(5000,5000.1),round=None)
    nose.tools.assert_almost_equal(num,0.1)

  def test_pixel_range_None_return02(self):
    num = pixel_range(self.bins,(4999.8,5000),round=None)
    nose.tools.assert_almost_equal(num,0.2)

  def test_pixel_range_None_return6(self):
    num = pixel_range(self.bins,(5000.5,5006.5),round=None)
    nose.tools.assert_almost_equal(num,6)

  def test_pixel_range_None_return8(self):
    num = pixel_range(self.bins,(5000,5008),round=None)
    nose.tools.assert_almost_equal(num,8)


# test the obsbandpass.wave_range() function
class TestWaveRangeFunc(unittest.TestCase):
  def setUp(self):
    bp = S.ObsBandpass('acs,hrc,f555w')
    self.bins = bp.binset

  def test_round_exception(self):
    self.assertRaises(ValueError, wave_range, self.bins, 5000, 100, round='up')

  def test_low_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, wave_range, self.bins, 1000, 100)

  def test_high_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, wave_range, self.bins, 11000, 100)

  def test_wave_range_None_0(self):
    w1, w2 = wave_range(self.bins,5000.4,0,round=None)
    self.assertEqual(w1,w2)

  def test_wave_range_None_2(self):
    w1, w2 = wave_range(self.bins,5000,2,round=None)
    self.assertEqual(w1,4999)
    self.assertEqual(w2,5001)

  def test_wave_range_None_3(self):
    w1, w2 = wave_range(self.bins,5000.25,3,round=None)
    self.assertEqual(w1,4998.75)
    self.assertEqual(w2,5001.75)

  def test_wave_range_None_4(self):
    w1, w2 = wave_range(self.bins,5000.5,4,round=None)
    self.assertEqual(w1,4998.5)
    self.assertEqual(w2,5002.5)

  def test_wave_range_round_1(self):
    w1, w2 = wave_range(self.bins,5002,1,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5002.5)

  def test_wave_range_round_2(self):
    w1, w2 = wave_range(self.bins,5005,2,round='round')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5006.5)

  def test_wave_range_round_3(self):
    w1, w2 = wave_range(self.bins,5005,3,round='round')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5006.5)

  def test_wave_range_round_4(self):
    w1, w2 = wave_range(self.bins,5004.25,4,round='round')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5006.5)

  def test_wave_range_round_5(self):
    w1, w2 = wave_range(self.bins,5004.25,5,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5006.5)

  def test_wave_range_round_6(self):
    w1, w2 = wave_range(self.bins,5004.5,6,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5007.5)

  def test_wave_range_round_7(self):
    w1, w2 = wave_range(self.bins,5004.5,7,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5008.5)

  def test_wave_range_min_1(self):
    w1, w2 = wave_range(self.bins,5004,1,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)

  def test_wave_range_min_2(self):
    w1, w2 = wave_range(self.bins,5004,2,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)

  def test_wave_range_min_3(self):
    w1, w2 = wave_range(self.bins,5004,3,round='min')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)

  def test_wave_range_min_4(self):
    w1, w2 = wave_range(self.bins,5006.25,4,round='min')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5007.5)

  def test_wave_range_min_5(self):
    w1, w2 = wave_range(self.bins,5006.25,5,round='min')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5008.5)

  def test_wave_range_min_6(self):
    w1, w2 = wave_range(self.bins,5006.5,6,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)

  def test_wave_range_min_7(self):
    w1, w2 = wave_range(self.bins,5006.5,7,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)

  def test_wave_range_max_1(self):
    w1, w2 = wave_range(self.bins,5004,1,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)

  def test_wave_range_max_2(self):
    w1, w2 = wave_range(self.bins,5004,2,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)

  def test_wave_range_max_3(self):
    w1, w2 = wave_range(self.bins,5004,3,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)

  def test_wave_range_max_4(self):
    w1, w2 = wave_range(self.bins,5006.25,4,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5008.5)

  def test_wave_range_max_5(self):
    w1, w2 = wave_range(self.bins,5006.25,5,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)

  def test_wave_range_max_6(self):
    w1, w2 = wave_range(self.bins,5006.5,6,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)

  def test_wave_range_max_7(self):
    w1, w2 = wave_range(self.bins,5006.5,7,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5010.5)


# test the obsbandpass.ObsModeBandpass.pixel_range() and .wave_range() methods
class TestPixelWaveRangeMethods(unittest.TestCase):
  def setUp(self):
    self.bp = S.ObsBandpass('acs,hrc,f555w')

  def test_pixel_range_waveunits(self):
    num = self.bp.pixel_range((499.95,500.05),waveunits='nm',round='round')
    self.assertEqual(num,1)

  def test_wave_range_waveunits(self):
    w1, w2 = self.bp.wave_range(500,2,waveunits='nm',round=None)
    self.assertEqual(w1,499.9)
    self.assertEqual(w2,500.1)


# test the spectrum.SpectralElement.unit_response method as it's run
# by obsbandpass.ObsModeBandpass objects. results compared to synphot bandpar.
class TestUnitResponse(testutil.FPTestCase):
  def setUp(self):
    graphtab = 'mtab$u921351jm_tmg.fits'
    comptab = 'mtab$v8h1925fm_tmc.fits'
    thermtab = 'mtab$tae17277m_tmt.fits'

    S.setref(graphtable=graphtab,
             comptable=comptab,
             thermtable=thermtab)

  def tearDown(self):
    S.setref()


  def test_acs_hrc_f555w(self):
    bp = S.ObsBandpass('acs,hrc,f555w')

    ref = 3.0074E-19

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_acs_wfc1_f555w_f814w(self):
    bp = S.ObsBandpass('acs,wfc1,f555w,f814w')

    ref = 1.7308E-13

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_acs_sbc_f125lp(self):
    bp = S.ObsBandpass('acs,sbc,f125lp')

    ref = 1.7218E-17

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_wfc3_uvis1_f395n(self):
    bp = S.ObsBandpass('wfc3,uvis1,f395n')

    ref = 5.9579E-18

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_wfc3_uvis2_fq924n(self):
    bp = S.ObsBandpass('wfc3,uvis2,fq924n')

    ref = 6.9039E-18

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_wfc3_ir_f140w(self):
    bp = S.ObsBandpass('wfc3,ir,f140w')

    ref = 1.4574E-20

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_wfc3_ir_f140w(self):
    bp = S.ObsBandpass('wfc3,ir,f140w')

    ref = 1.4574E-20

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_wfpc2_f555w(self):
    bp = S.ObsBandpass('wfpc2,f555w')

    ref = 4.8968E-19

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_cos_boa_fuv_g130m_c1309(self):
    bp = S.ObsBandpass('cos,boa,fuv,g130m,c1309')

    ref = 3.5520E-15

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

  def test_stis_ccd_f25ndq1_a2d4_mjd55555(self):
    bp = S.ObsBandpass('stis,ccd,f25ndq1,a2d4,mjd#55555')

    ref = 3.0650E-18

    test = bp.unit_response()

    self.assertApproxFP(test,ref,accuracy=1.e-4)

