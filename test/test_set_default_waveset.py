import numpy.testing as nptest

from pysynphot import refs


def setUpModule():
    pass


def tearDownModule():
    # Reset refs; specifically the default waveset
    reload(refs)


def test_log_num():
  refs.set_default_waveset(10, 20, 10)

  testref = [ 10.        ,  10.71773463,  11.48698355,  12.31144413,
              13.19507911,  14.14213562,  15.15716567,  16.24504793,
              17.41101127,  18.66065983]

  nptest.assert_allclose(testref,refs._default_waveset)

  refs.setref(waveset=(10, 20, 10))

  nptest.assert_allclose(testref,refs._default_waveset)

  refs.setref(waveset=(10, 20, 10, 'log'))

  nptest.assert_allclose(testref,refs._default_waveset)


def test_log_delta():
  refs.set_default_waveset(10, 20, delta=0.05)

  testref = [ 10.        ,  11.22018454,  12.58925412,  14.12537545,
              15.84893192,  17.7827941 ,  19.95262315]

  nptest.assert_allclose(testref,refs._default_waveset)


def test_linear_num():
  refs.set_default_waveset(10, 20, 10, log=False)

  testref = [ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.]

  nptest.assert_array_equal(refs._default_waveset, testref)

  refs.setref(waveset=(10, 20, 10, 'linear'))

  nptest.assert_allclose(testref,refs._default_waveset)


def test_linear_delta():
  refs.set_default_waveset(10, 20, delta=1, log=False)

  testref = [ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.]

  nptest.assert_array_equal(refs._default_waveset, testref)
