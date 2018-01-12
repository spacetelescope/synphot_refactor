# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test models.py module.

.. note::

    ``GaussianAbsorption1D`` and ``RedshiftScaleFactor`` are already being
    tested within existing Astropy PRs.

    ``get_waveset()`` is tested in test_spectrum.py.

"""
from __future__ import absolute_import, division, print_function

# STDLIB
import os

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
import astropy
from astropy import units as u
from astropy.utils import minversion
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import specio, units
from ..models import BlackBody1D, ConstFlux1D, Empirical1D, PowerLawFlux1D

try:
    import scipy
except ImportError:
    HAS_SCIPY = False
else:
    HAS_SCIPY = True

HAS_SCIPY = HAS_SCIPY and minversion(scipy, '0.14')
ASTROPY_LT_20 = not minversion(astropy, '2.0')


def setup_module(module):
    # https://github.com/astropy/astropy/issues/6383
    if not ASTROPY_LT_20:
        import astropy.constants as const
        from astropy.constants import si, astropyconst13

        const.sigma_sb = si.sigma_sb = astropyconst13.sigma_sb
        const.h = si.h = astropyconst13.h
        const.k_B = si.k_B = astropyconst13.k_B


def teardown_module(module):
    # https://github.com/astropy/astropy/issues/6383
    if not ASTROPY_LT_20:
        import astropy.constants as const
        from astropy.constants import si, astropyconst20
        const.sigma_sb = si.sigma_sb = astropyconst20.sigma_sb
        const.h = si.h = astropyconst20.h
        const.k_B = si.k_B = astropyconst20.k_B


class TestBlackBody1D(object):
    """Test BlackBody1D model."""
    def setup_class(self):
        self.m1 = BlackBody1D(temperature=5500)

    def test_lambda_max(self):
        np.testing.assert_allclose(self.m1.lambda_max, 5268.67, rtol=1e-5)

    def test_sampleset(self):
        f1 = self.m1(self.m1.sampleset())
        assert f1[0] == 0
        assert f1[-1] < self.m1(self.m1.lambda_max) * 0.05

    def test_eval(self):
        np.testing.assert_allclose(
            self.m1(np.arange(3000, 3100, 10)),
            [1.20906423e+17, 1.22815123e+17, 1.24735543e+17, 1.26667499e+17,
             1.28610806e+17, 1.30565276e+17, 1.32530722e+17, 1.34506953e+17,
             1.36493780e+17, 1.38491010e+17])

    def test_multi_n_models(self):
        m2 = BlackBody1D(temperature=[100, 10000], n_models=2)
        np.testing.assert_allclose(
            m2.lambda_max, [2.8977685e5, 2897.7685], rtol=1e-5)
        np.testing.assert_allclose(
            m2(20000), [2.14331496e-14, 3.55819086e+17])


class TestConstFlux1D(object):
    """Test ConstFlux1D model."""
    def setup_class(self):
        self.w = np.arange(1, 21000, 5000)

    @pytest.mark.parametrize(
        'amplitude',
        [1, 1 * units.PHOTNU, 1 * units.FLAM, 1 * units.FNU,
         1 * u.Jy, 1 * u.mJy])
    def test_linear(self, amplitude):
        if isinstance(amplitude, u.Quantity):
            ans = amplitude.value
            flux_unit = amplitude.unit
        else:
            ans = amplitude
            flux_unit = units.PHOTLAM

        m = ConstFlux1D(amplitude=amplitude)
        f = units.convert_flux(self.w, m(self.w) * units.PHOTLAM, flux_unit)

        assert m._flux_unit == flux_unit
        np.testing.assert_allclose(f.value, ans)

    @pytest.mark.parametrize(
        ('in_unit', 'out_unit', 'val'),
        [(u.STmag, units.FLAM, 3.63e-9),
         (u.ABmag, units.FNU, 3.63e-20)])
    def test_mag(self, in_unit, out_unit, val):
        m = ConstFlux1D(amplitude=0 * in_unit)
        f = units.convert_flux(self.w, m(self.w) * units.PHOTLAM, out_unit)
        np.testing.assert_allclose(f.value, val, rtol=2.5e-4)

    def test_multi_n_models(self):
        m = ConstFlux1D(amplitude=[1, 2], n_models=2)
        np.testing.assert_array_equal(m(1000), [1, 2])

    @pytest.mark.parametrize(
        'flux_unit', [u.count, units.OBMAG, units.VEGAMAG, u.AA])
    def test_invalid_units(self, flux_unit):
        with pytest.raises(NotImplementedError):
            ConstFlux1D(amplitude=1 * flux_unit)


@pytest.mark.skipif('not HAS_SCIPY')
class TestEmpirical1D(object):
    """Test Empirical1D model."""
    def setup_class(self):
        filename = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'))
        hdr, x, f = specio.read_spec(filename)
        y = units.convert_flux(x, f, units.PHOTLAM)
        self.flux_flam = f.value
        self.w = x.value
        self.m = Empirical1D(points=self.w, lookup_table=y.value)

    def test_sampleset(self):
        np.testing.assert_array_equal(self.m.sampleset(), self.w)

    def test_eval(self):
        # Sample at existing wavelength (no interpolation)
        x = self.w[5000]
        y = units.convert_flux(x, self.m(x), units.FLAM)
        np.testing.assert_allclose(y.value, self.flux_flam[5000])

        # Sampling with interpolation
        w = [4956.8, 4959.55, 4962.3]
        y = units.convert_flux(w, self.m(w), units.FLAM)
        np.testing.assert_allclose(
            y.value, [8.57166622e-15, 8.86174843e-15, 8.68707743e-15],
            rtol=1e-6)

        # Descending order
        w2 = w[::-1]
        f2 = self.m(w2)
        y = units.convert_flux(w2, f2, units.FLAM)
        np.testing.assert_allclose(
            y.value, [8.68707743e-15, 8.86174843e-15, 8.57166622e-15],
            rtol=1e-6)

        # New model with descending order
        m2 = Empirical1D(points=w2, lookup_table=f2)
        y = units.convert_flux(w, m2(w), units.FLAM)
        np.testing.assert_allclose(
            y.value, [8.57166622e-15, 8.86174843e-15, 8.68707743e-15],
            rtol=1e-6)

    @pytest.mark.parametrize(
        ('keep_neg', 'ans'),
        [(True, [-1.1, 0, 1.1]),
         (False, [0, 0, 1.1])])
    def test_neg_array(self, keep_neg, ans):
        m2 = Empirical1D(points=[1, 2, 3], lookup_table=[-1.1, 0, 1.1],
                         keep_neg=keep_neg)
        np.testing.assert_array_equal(m2([1, 2, 3]), ans)
        if not keep_neg:
            assert 'NegativeFlux' in m2.meta['warnings']

    @pytest.mark.parametrize(
        ('keep_neg', 'ans'),
        [(True, -1),
         (False, 0)])
    def test_neg_scalar(self, keep_neg, ans):
        m2 = Empirical1D(points=[1, 2, 3], lookup_table=[-1, 0, 1],
                         keep_neg=keep_neg)
        np.testing.assert_array_equal(m2(1), ans)
        if not keep_neg:
            assert 'NegativeFlux' in m2.meta['warnings']

    @pytest.mark.parametrize(
        ('tab', 'ans'),
        [([0, 1, 0], True),
         ([0, 1, 1], False)])
    def test_taper(self, tab, ans):
        m2 = Empirical1D(points=[1, 2, 3], lookup_table=tab)
        assert m2.is_tapered() is ans

    def test_extrap(self):
        """Test extrapolation of constant at both ends, as done in
        ASTROLIB PYSYNPHOT.
        """
        m2 = Empirical1D(
            points=[1000, 2000, 3000, 4000],
            lookup_table=[0.01, 5.0, 10.6, 1.5])
        assert m2(900) == 0.01
        assert m2(10000) == 1.5
        np.testing.assert_allclose(
            m2([900, 1000, 1500, 10000]), [0.01, 0.01, 2.505, 1.5])


class TestPowerLawFlux1D(object):
    """Test PowerLawFlux1D model."""
    def setup_class(self):
        self.w = np.arange(3000, 3100, 10)
        self.m = PowerLawFlux1D(amplitude=1, x_0=6000, alpha=4)

    def test_eval(self):
        assert self.m._flux_unit == units.PHOTLAM
        np.testing.assert_allclose(
            self.m(self.w),
            [16, 15.78843266, 15.58035072, 15.37568551, 15.17436992,
             14.97633838, 14.78152682, 14.5898726, 14.40131453, 14.21579277],
            rtol=1e-6)

    def test_normalization(self):
        assert self.m(self.m.x_0) == 1

    def test_multi_n_models(self):
        m2 = PowerLawFlux1D(
            amplitude=[1, 1] * units.FLAM, x_0=[0.3, 0.305] * u.micron,
            alpha=[4, 1], n_models=2)
        y = units.convert_flux(
            self.w, m2(self.w, model_set_axis=False) * units.PHOTLAM,
            units.FLAM)
        ans = [[1, 0.98677704, 0.97377192, 0.96098034, 0.94839812,
                0.93602115, 0.92384543, 0.91186704, 0.90008216, 0.88848705],
               [1.01666667, 1.01328904, 1.00993377, 1.00660066, 1.00328947,
                1, 0.99673203, 0.99348534, 0.99025974, 0.98705502]]
        np.testing.assert_allclose(y.value, ans, rtol=1e-6)

    @pytest.mark.parametrize('flux_unit', [u.STmag, u.ABmag])
    def test_valid_mag(self, flux_unit):
        m = PowerLawFlux1D(amplitude=1 * flux_unit, x_0=6000, alpha=4)
        assert m.amplitude == 1
        assert m._flux_unit == flux_unit

    @pytest.mark.parametrize(
        'flux_unit', [u.count, units.OBMAG, units.VEGAMAG, u.AA])
    def test_invalid_units(self, flux_unit):
        with pytest.raises(NotImplementedError):
            PowerLawFlux1D(amplitude=1 * flux_unit, x_0=5000, alpha=4)
