# tests for the catalog module
import numpy as np

from stpysyn.test import testutil
import pysynphot as S
import pysynphot.Cache as Cache
import pysynphot.pysynexcept as exceptions

# this test passes before changes, and should pass after the changes
class ICatK93Test(testutil.FPTestCase):
  def setUp(self):
    self.sp = S.Icat('k93models', 6440, 0, 4.3)

  def test_wave(self):
    ref_wave1 = \
        np.array([  90.90000153,   93.50000763,   96.09999847,   97.70000458,
         99.59999847,  102.        ,  103.80000305,  105.6000061 ,
        107.70000458,  110.40000153,  114.        ,  117.79999542,
        121.30000305,  124.79999542,  127.09999847,  128.40000916,
        130.5       ,  132.3999939 ,  133.90000916,  136.6000061 ,
        139.80000305,  143.30000305,  147.19999695,  151.        ,
        155.20001221,  158.80000305,  162.00001526,  166.        ,
        170.30000305,  173.40000916,  176.80000305,  180.20001221,
        181.69999695,  186.1000061 ,  191.        ,  193.8999939 ,
        198.40000916,  201.80000305,  205.        ,  210.5       ,
        216.20001221,  219.80000305,  223.        ,  226.80000305,
        230.        ,  234.        ,  240.        ,  246.5       ,
        252.3999939 ,  256.80001831], dtype=np.float32)

    self.assertApproxNumpy(self.sp.wave[:50], ref_wave1)

    ref_wave2 = \
        np.array([   83800.,    84200.,    84600.,    85000.,    85400.,    85800.,
          86200.,    86600.,    87000.,    87400.,    87800.,    88200.,
          88600.,    89000.,    89400.,    89800.,    90200.,    90600.,
          91000.,    91400.,    91800.,    92200.,    92600.,    93000.,
          93400.,    93800.,    94200.,    94600.,    95000.,    95400.,
          95800.,    96200.,    96600.,    97000.,    97400.,    97800.,
          98200.,    98600.,    99000.,    99400.,    99800.,   100200.,
         200000.,   400000.,   600000.,   800000.,  1000000.,  1200000.,
        1400000.,  1600000.], dtype=np.float32)

    self.assertApproxNumpy(self.sp.wave[-50:], ref_wave2)

  def test_flux(self):
    ref_flux1 = \
        np.array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

    self.assertEqualNumpy(self.sp.flux[:50], ref_flux1)

    ref_flux2 = \
        np.array([  2.52510792e+03,   2.47883842e+03,   2.43311637e+03,
         2.38843415e+03,   2.34455095e+03,   2.30190141e+03,
         2.25982266e+03,   2.21930715e+03,   2.17950029e+03,
         2.14031198e+03,   2.10216378e+03,   2.06411734e+03,
         2.02789000e+03,   1.99191291e+03,   1.95752853e+03,
         1.92259620e+03,   1.88976666e+03,   1.85768178e+03,
         1.82475330e+03,   1.79369145e+03,   1.76356796e+03,
         1.73377904e+03,   1.70432192e+03,   1.67572220e+03,
         1.64739969e+03,   1.61997833e+03,   1.59299008e+03,
         1.56657219e+03,   1.54066436e+03,   1.51508799e+03,
         1.49065412e+03,   1.46606232e+03,   1.44255637e+03,
         1.41922753e+03,   1.39555249e+03,   1.37360936e+03,
         1.35179525e+03,   1.33041182e+03,   1.30944458e+03,
         1.28851215e+03,   1.26828580e+03,   1.24841065e+03,
         8.04744247e+01,   5.03657385e+00,   9.88851448e-01,
         3.10885179e-01,   1.26599425e-01,   6.07383728e-02,
         3.26344365e-02,   1.90505413e-02])

    self.assertApproxNumpy(self.sp.flux[-50:], ref_flux2)


# tests for changes related to ticket #211
# test that an exception is raised when making out of bounds requests
class TestIcatExceptions(testutil.FPTestCase):
  def test_logG_out_high(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 6440, 0, 10)

  def test_logG_out_low(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 6440, 0, -1)

  def test_Teff_out_high(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 1.e6, 0, 4.3)

  def test_Teff_out_low(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 100, 0, 4.3)

  def test_metallicity_out_high(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 6440, 2, 4.3)

  def test_metallicity_out_low(self):
    self.assertRaises(exceptions.ParameterOutOfBounds,S.Icat,'k93models', 6440, -6, 4.3)


# test changes for ticket #131
# test that the Cache.CATALOG_CACHE variable works as intended.
class TestCatalogCache(testutil.FPTestCase):
  def test_things_in_cache(self):

    fail = False
    self.tra = { }

    Cache.reset_catalog_cache()

    sp = S.Icat('k93models', 6440, 0, 4.3)

    self.assertTrue(len(Cache.CATALOG_CACHE) == 1)

    k = Cache.CATALOG_CACHE.keys()[0]

    from pysynphot.locations import irafconvert
    import os.path
    f = irafconvert("$PYSYN_CDBS/grid/k93models/catalog.fits")
    f = os.path.normpath(f)
    f = os.path.normcase(f)

    fixed_k = os.path.normpath(k)
    fixed_k = os.path.normcase(fixed_k)

    if fixed_k != f :
        self.tra['cache_found'] = k
        self.tra['cache_found_fixed'] = fixed_k
        self.tra['cache_expect'] = f
        fail = True

    if not isinstance(Cache.CATALOG_CACHE[k],list) :
        self.tra['cache_type_mismatch'] = str(type(Cache.CATALOG_CACHE[k]))
        fail = True

    if fail :
        raise AssertionError()

  def test_reset_catalog_cache(self):
    sp = S.Icat('k93models', 6440, 0, 4.3)

    self.assertTrue(len(Cache.CATALOG_CACHE) != 0)

    Cache.reset_catalog_cache()

    self.assertTrue(len(Cache.CATALOG_CACHE) == 0)


