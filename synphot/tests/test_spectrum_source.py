# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and related functionalities for source spectrum."""

# STDLIB
import os
import warnings

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import modeling
from astropy import units as u
from astropy.io import fits
from astropy.modeling.models import (
    BrokenPowerLaw1D, Const1D, ExponentialCutoffPowerLaw1D, LogParabola1D,
    PowerLaw1D, RedshiftScaleFactor)
from astropy.tests.helper import assert_quantity_allclose
from astropy.utils.data import get_pkg_data_filename
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from synphot.tests.test_units import (
    _area, _wave, _flux_jy, _flux_photlam, _flux_vegamag
)
from synphot import exceptions, units
from synphot.compat import ASTROPY_LT_4_0
from synphot.compat import HAS_SPECUTILS  # noqa
from synphot.models import (
    BlackBodyNorm1D, Box1D, ConstFlux1D, Empirical1D, Gaussian1D,
    GaussianFlux1D, Lorentz1D, RickerWavelet1D, PowerLawFlux1D)
from synphot.observation import Observation
from synphot.spectrum import SourceSpectrum, SpectralElement

# GLOBAL VARIABLES
_vspec = None  # Loaded in test_load_vspec()


def setup_module(module):
    import astropy.constants as const
    from astropy.constants import si, astropyconst13

    const.sigma_sb = si.sigma_sb = astropyconst13.sigma_sb
    const.h = si.h = astropyconst13.h
    const.k_B = si.k_B = astropyconst13.k_B


def teardown_module(module):
    import astropy.constants as const

    if ASTROPY_LT_4_0:
        from astropy.constants import si, astropyconst20
        const.sigma_sb = si.sigma_sb = astropyconst20.sigma_sb
        const.h = si.h = astropyconst20.h
        const.k_B = si.k_B = astropyconst20.k_B
    else:
        from astropy.constants import si, astropyconst40
        const.sigma_sb = si.sigma_sb = astropyconst40.sigma_sb
        const.h = si.h = astropyconst40.h
        const.k_B = si.k_B = astropyconst40.k_B


@pytest.mark.remote_data
def test_load_vspec():
    """Load VEGA spectrum once here to be used later."""
    global _vspec
    _vspec = SourceSpectrum.from_vega()


@pytest.mark.remote_data
@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans'),
    [(_flux_photlam, units.VEGAMAG, _flux_vegamag),
     (_flux_vegamag, units.PHOTLAM, _flux_photlam),
     (_flux_jy, units.VEGAMAG, _flux_vegamag),
     (_flux_vegamag, u.Jy, _flux_jy)])
def test_flux_conversion_vega(in_q, out_u, ans):
    """Test Vega spectrum object and flux conversion with VEGAMAG.

    .. note:: 1% is good enough given Vega gets updated from time to time.

    """
    result = units.convert_flux(_wave, in_q, out_u, vegaspec=_vspec)
    assert_quantity_allclose(result, ans, rtol=1e-2)

    # Scalar
    i = 0
    result = units.convert_flux(_wave[i], in_q[i], out_u, vegaspec=_vspec)
    assert_quantity_allclose(result, ans[i], rtol=1e-2)


class TestEmpiricalSourceFromFile:
    """This is the most common model used in ASTROLIB PYSYNPHOT."""
    def setup_class(self):
        specfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'),
            package='synphot.tests')
        self.sp = SourceSpectrum.from_file(specfile)

    def test_invalid_flux_unit(self):
        with pytest.raises(exceptions.SynphotError):
            SourceSpectrum(Empirical1D, points=_wave,
                           lookup_table=_flux_vegamag)

    def test_invalid_models(self):
        # Test not a Model subclass
        with pytest.raises(exceptions.SynphotError):
            SourceSpectrum(fits.HDUList)

        # Test unsupported model
        with pytest.raises(exceptions.SynphotError):
            SourceSpectrum(RedshiftScaleFactor)

    def test_metadata(self):
        assert 'SourceSpectrum' in str(self.sp)
        assert self.sp.meta['header']['SIMPLE']  # From FITS header
        assert self.sp.warnings == {}
        assert self.sp.z == 0
        assert_quantity_allclose(
            self.sp.waverange, [3479.99902344, 10500.00097656] * u.AA)

    def test_call(self):
        w = self.sp.model.points[0][5000:5004]
        y = self.sp(w, flux_unit=units.FLAM)
        y_ans = [1.87284130e-15, 1.85656811e-15, 1.84030867e-15,
                 1.82404183e-15] * units.FLAM
        np.testing.assert_allclose(
            w, [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        assert_quantity_allclose(y, y_ans)

    def test_neg_flux(self):
        w = [1000, 5000, 9000]
        with pytest.warns(AstropyUserWarning,
                          match=r'contained negative flux or throughput'):
            sp = SourceSpectrum(
                Empirical1D, points=w, lookup_table=[100, -45, 5e-17])
        np.testing.assert_array_equal(sp(w).value, [100, 0, 5e-17])
        assert 'NegativeFlux' in sp.warnings

    def test_conversion(self):
        x = 0.60451641 * u.micron
        w, y = self.sp._get_arrays(x, flux_unit=units.FNU)
        assert_quantity_allclose(x, w)
        assert_quantity_allclose(y, 2.282950185743497e-26 * units.FNU,
                                 rtol=1e-6)

    def test_integrate(self):
        expected_unit = u.erg / (u.cm**2 * u.s)
        # Whole range
        f = self.sp.integrate(flux_unit=units.FLAM)
        assert_quantity_allclose(f, 8.460125829057308e-12 * expected_unit,
                                 rtol=1e-5)

        # Given range
        f = self.sp.integrate(wavelengths=_wave, flux_unit=units.FLAM)
        assert_quantity_allclose(f, 4.810058069909525e-14 * expected_unit,
                                 rtol=1e-5)

        # Unsupported unit
        with pytest.raises(exceptions.SynphotError):
            self.sp.integrate(flux_unit=u.Jy)

    def test_taper(self):
        # Original spectrum already tapered -- nothing done
        sp = self.sp.taper()
        assert sp is self.sp

        # Tapering is done
        sp2 = SourceSpectrum(
            Empirical1D, points=_wave, lookup_table=_flux_photlam)
        sp = sp2.taper()
        x, y = sp._get_arrays(None, flux_unit=units.FLAM)
        assert_quantity_allclose(
            x, [4954.05152484, 4956.8, 4959.55, 4962.3, 4965.05152484] * u.AA)
        assert_quantity_allclose(
            y,
            [0, 3.9135e-14, 4.0209e-14, 3.9169e-14, 0] * units.FLAM, rtol=1e-6)


class TestBlackBodySource:
    """Test source spectrum with BlackBody1D model."""
    def setup_class(self):
        self.sp = SourceSpectrum(BlackBodyNorm1D, temperature=5500)

    def test_eval(self):
        w = np.arange(3000, 3100, 10)
        y = self.sp(w)
        assert_quantity_allclose(
            y,
            [0.00019318, 0.00019623, 0.0001993, 0.00020238, 0.00020549,
             0.00020861, 0.00021175, 0.00021491, 0.00021809,
             0.00022128] * units.PHOTLAM,
            rtol=2.5e-3)

    def test_integrate(self):
        ans_photlam = 12.39167258 * (u.ph / (u.cm * u.cm * u.s))
        ans_flam = 2.62716011e-11 * (u.erg / (u.cm * u.cm * u.s))

        assert_quantity_allclose(self.sp.integrate(), ans_photlam, rtol=1e-5)
        assert_quantity_allclose(
            self.sp.integrate(flux_unit='flam'), ans_flam, rtol=1e-5)
        assert_quantity_allclose(
            self.sp.integrate(integration_type='analytical', flux_unit='flam'),
            ans_flam, rtol=5e-3)

    @pytest.mark.xfail(reason='Cannot convert unit in analytical mode')
    def test_integrate_fixme(self):
        """Merge this into ``test_integrate()`` above when fixed."""
        ans_photlam = 12.39167258 * (u.ph / (u.cm * u.cm * u.s))
        assert_quantity_allclose(
            self.sp.integrate(integration_type='analytical'), ans_photlam)


class TestGaussianSource:
    """Test source spectrum with GaussianFlux1D model."""
    def setup_class(self):
        tf = 4.96611456e-12 * (u.erg / (u.cm * u.cm * u.s))
        self.sp = SourceSpectrum(
            GaussianFlux1D, total_flux=tf, mean=4000, fwhm=100)

    def test_eval(self):
        y = self.sp([3900, 4000, 4060])
        assert_quantity_allclose(
            y, [0.00058715, 0.00939437, 0.00346246] * units.PHOTLAM, rtol=1e-5)

    def test_totalflux(self):
        """Test Gaussian source integration.

        .. note::

            Analytic integral is more accurate because it does not rely on
            waveset definition.

        """
        # PHOTLAM
        f_ans = 1 * (u.ph / (u.cm**2 * u.s))
        assert_quantity_allclose(self.sp.integrate(), f_ans, rtol=1e-5)
        assert_quantity_allclose(
            self.sp.integrate(integration_type='analytical'), f_ans)

        # FLAM
        x0 = 400 * u.nm
        fwhm = 10 * u.nm
        sp2 = SourceSpectrum(
            GaussianFlux1D, total_flux=1, mean=x0, fwhm=fwhm)
        val_ans = 1 * (u.erg / (u.cm * u.cm * u.s))
        assert_quantity_allclose(
            sp2.integrate(flux_unit=units.FLAM), val_ans, rtol=1e-3)
        assert_quantity_allclose(
            sp2.integrate(flux_unit=units.FLAM, integration_type='analytical'),
            val_ans)

    def test_symmetry(self):
        assert_quantity_allclose(self.sp(3950), self.sp(4050))

    def test_fwhm(self):
        """Should round-trip back to the same bandpass FWHM."""
        m = self.sp.model
        bp = SpectralElement(
            Gaussian1D, mean=m.mean, amplitude=m.amplitude, stddev=m.stddev)
        assert_quantity_allclose(bp.fwhm(), 100 * u.AA, rtol=1e-3)  # 0.1%

    def test_alt_source(self):
        """Same source, different way to init."""
        sp2 = SourceSpectrum(
            GaussianFlux1D, amplitude=self.sp.model.amplitude.value,
            mean=self.sp.model.mean.value, stddev=self.sp.model.stddev.value)
        w = [3900, 4000, 4060] * u.AA
        assert_quantity_allclose(sp2(w), self.sp(w))


def test_gaussian_source_watts():
    """https://github.com/spacetelescope/synphot_refactor/issues/153"""
    mu = 1 * u.um
    fwhm = (0.01 / 0.42466) * u.um
    flux = 1 * (u.W / u.m**2)

    sp = SourceSpectrum(GaussianFlux1D, mean=mu, fwhm=fwhm, total_flux=flux)
    tf = sp.integrate(flux_unit=units.FLAM)
    assert_quantity_allclose(tf, flux, rtol=1e-4)


class TestPowerLawSource:
    """Test source spectrum with PowerLawFlux1D model."""
    def setup_class(self):
        self.sp = SourceSpectrum(PowerLawFlux1D, amplitude=1 * units.PHOTLAM,
                                 x_0=6000 * u.AA, alpha=4)
        self.w = np.arange(3000, 3100, 10) * u.AA

    def test_no_default_wave(self):
        assert self.sp.waverange == [None, None]

        with pytest.raises(exceptions.SynphotError,
                           match='waveset is undefined'):
            self.sp(None)

    def test_eval(self):
        y = self.sp(self.w)
        assert_quantity_allclose(
            y,
            [16, 15.78843266, 15.58035072, 15.37568551, 15.17436992,
             14.97633838, 14.78152682, 14.5898726, 14.40131453,
             14.21579277] * units.PHOTLAM,
            rtol=1e-6)

    def test_normalization(self):
        assert_quantity_allclose(self.sp(600 * u.nm), 1 * units.PHOTLAM)

    def test_integrate(self):
        ans_photlam = 1357.75787527 * (u.ph / (u.cm * u.cm * u.s))
        ans_flam = 8.8608168e-09 * (u.erg / (u.cm * u.cm * u.s))
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w), ans_photlam)
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w, flux_unit='flam'), ans_flam)
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w,
                              integration_type='analytical'),
            ans_photlam, rtol=1e-4)

    @pytest.mark.xfail(reason='Cannot convert unit of analytic integral')
    def test_integrate_wontfix(self):
        """Powerlaw in one flux unit might not be powerlaw anymore in
        another, so we cannot convert flux unit of analytical integration
        easily.
        """
        ans_flam = 8.8608168e-09 * (u.erg / (u.cm * u.cm * u.s))
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w, flux_unit='flam',
                              integration_type='analytical'), ans_flam)


class TestBuildModelsSource:
    """Test compatiblity with other models not tested above."""
    def test_BrokenPowerLaw1D(self):
        sp = SourceSpectrum(
            BrokenPowerLaw1D, amplitude=1, x_break=6000, alpha_1=1,
            alpha_2=4)
        y = sp([5000, 6000, 7000])
        assert_quantity_allclose(y, [1.2, 1, 0.53977509] * units.PHOTLAM)

    def test_Const1D(self):
        sp = SourceSpectrum(Const1D, amplitude=1)
        y = sp([1, 1000, 1e6])
        assert_quantity_allclose(y, 1 * units.PHOTLAM, rtol=0)

    def test_ConstFlux1D(self):
        sp = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy)
        w = [1, 1000, 1e6] * u.AA
        with u.add_enabled_equivalencies(u.spectral_density(w)):
            assert_quantity_allclose(sp(w), 1 * u.Jy)

    def test_ExponentialCutoffPowerLaw1D(self):
        sp = SourceSpectrum(
            ExponentialCutoffPowerLaw1D, amplitude=1, x_0=6000,
            x_cutoff=10000, alpha=4)
        y = sp([5000, 6000, 10000])
        assert_quantity_allclose(
            y, [1.25770198, 0.54881164, 0.04767718] * units.PHOTLAM)

    def test_LogParabola1D(self):
        sp = SourceSpectrum(
            LogParabola1D, amplitude=1, x_0=6000, alpha=1, beta=4)
        y = sp([5000, 6000, 7000])
        assert_quantity_allclose(y, [1.0505953, 1, 0.77942375] * units.PHOTLAM)

    def test_Lorentz1D(self):
        sp = SourceSpectrum(Lorentz1D, amplitude=1, x_0=6000, fwhm=100)
        y = sp([5000, 6000, 7000])
        assert_quantity_allclose(
            y, [0.00249377, 1, 0.00249377] * units.PHOTLAM, rtol=1e-5)

    def test_RickerWavelet1D(self):
        sp = SourceSpectrum(RickerWavelet1D, amplitude=1, x_0=6000, sigma=100)
        y = sp([5000, 6000, 7000])
        assert_quantity_allclose(
            y, [-1.90946235e-20, 1, -1.90946235e-20] * units.PHOTLAM)

    def test_PowerLaw1D(self):
        sp = SourceSpectrum(PowerLaw1D, amplitude=1, x_0=6000, alpha=4)
        y = sp([5000, 6000, 7000])
        assert_quantity_allclose(y, [2.0736, 1, 0.53977509] * units.PHOTLAM)


class TestNormalize:
    """Test source spectrum normalization."""
    def setup_class(self):
        """``expr`` stores the equivalent IRAF SYNPHOT command."""
        # Blackbody: bb(5000)
        self.bb = SourceSpectrum(BlackBodyNorm1D, temperature=5000)

        # Gaussian emission line: em(5500, 250, 1e-13, flam)
        tf_unit = u.erg / (u.cm * u.cm * u.s)
        self.em = SourceSpectrum(GaussianFlux1D, mean=5500,
                                 total_flux=(1e-13 * tf_unit), fwhm=250)

        # ACS bandpass: band(acs,hrc,f555w)
        bandfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w.fits'),
            package='synphot.tests')
        self.acs = SpectralElement.from_file(bandfile)

        # Box bandpass: box(5500,1)
        self.abox = SpectralElement(Box1D, amplitude=1, x_0=5500, width=1)

    def _select_sp(self, sp_type):
        if sp_type == 'bb':
            sp = self.bb
        elif sp_type == 'em':
            sp = self.em
        else:
            sp = None
        return sp

    def _compare_countrate(self, rn_sp, ans_countrate):
        # Observation is needed to compare with expected count rate
        # although it is tested in test_observation.py
        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore', message=r'.*Source spectrum will be evaluated '
                r'outside pre-defined waveset.*', category=AstropyUserWarning)
            obs = Observation(rn_sp, self.acs, force='extrap')
        ct_rate = obs.countrate(_area)

        # 0.7% agreement with IRAF SYNPHOT COUNTRATE
        assert_quantity_allclose(
            ct_rate, ans_countrate * (u.ct / u.s), rtol=0.007)

    @pytest.mark.parametrize(
        ('sp_type', 'rn_val', 'ans_countrate'),
        [('bb', 1e-5, 117.9167),
         ('bb', 1e-16 * units.PHOTNU, 116.8613),
         ('bb', 1e-16 * units.FLAM, 326.4773),
         ('bb', 20 * u.STmag, 118.5366),
         ('bb', 1e-27 * units.FNU, 323.5549),
         ('bb', 20 * u.ABmag, 117.4757),
         ('bb', 1e-4 * u.Jy, 323.5547),
         ('bb', 0.1 * u.mJy, 323.5548),
         ('em', 1e-4, 277.4368),
         ('em', 1e-15 * units.PHOTNU, 274.9537),
         ('em', 1e-16 * units.FLAM, 76.81425),
         ('em', 18 * u.STmag, 175.9712),
         ('em', 1e-27 * units.FNU, 76.12671),
         ('em', 18 * u.ABmag, 174.3967),
         ('em', 1e-3 * u.Jy, 761.2667),
         ('em', 1 * u.mJy, 761.2666)])
    def test_renorm_density(self, sp_type, rn_val, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.normalize(rn_val, band=self.abox)
        self._compare_countrate(rn_sp, ans_countrate)

    @pytest.mark.parametrize(
        ('sp_type', 'rn_val', 'ans_countrate'),
        [('bb', 2 * u.count, 2),
         ('bb', -1 * units.OBMAG, 2.511886),
         ('em', 2 * u.count, 2),
         ('em', -1 * units.OBMAG, 2.511888)])
    def test_renorm_nondensity(self, sp_type, rn_val, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.normalize(rn_val, band=self.acs, area=_area)
        self._compare_countrate(rn_sp, ans_countrate)

    @pytest.mark.remote_data
    @pytest.mark.parametrize(
        ('sp_type', 'ans_countrate'),
        [('bb', 115.9126),
         ('em', 27.2856)])
    def test_renorm_vegamag(self, sp_type, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.normalize(20 * units.VEGAMAG, band=self.abox,
                             vegaspec=_vspec)
        self._compare_countrate(rn_sp, ans_countrate)

    def test_renorm_noband_jy(self):
        """Replace this with real test when it is implemented."""
        with pytest.raises(NotImplementedError):
            self.em.normalize(1e-23 * u.Jy)

    def test_renorm_partial_notmost(self):
        """Test force=True for 'partial_notmost' overlap."""
        sp = SourceSpectrum(Empirical1D, points=[5000, 6000],
                            lookup_table=[1, 1])
        with pytest.warns(AstropyUserWarning,
                          match=r'Spectrum is not defined everywhere'):
            rn_sp = sp.normalize(1e-23 * u.Jy, band=self.acs, force=True)
        assert 'PartialRenorm' in rn_sp.warnings
        assert 'PartialRenorm' not in sp.warnings

        # Partial overlap without force
        with pytest.raises(exceptions.PartialOverlap):
            sp.normalize(1, band=self.acs)

    def test_renorm_partial_most(self):
        """Test 'partial_most' overlap."""
        bp = SpectralElement(Box1D, amplitude=1, x_0=5600, width=870)
        with pytest.warns(AstropyUserWarning,
                          match=r'Spectrum is not defined everywhere'):
            rn_sp = self.em.normalize(1e-23 * u.Jy, band=bp)
        assert 'PartialRenorm' in rn_sp.warnings
        assert 'PartialRenorm' not in self.em.warnings
        assert '99%' in rn_sp.warnings['PartialRenorm']

    def test_exceptions(self):
        # Invalid passband
        with pytest.raises(exceptions.SynphotError):
            self.bb.normalize(10, band=np.ones(10))

        # Disjoint passband
        bp = SpectralElement(Box1D, amplitude=1, x_0=30000, width=1)
        with pytest.raises(exceptions.DisjointError):
            self.em.normalize(10, band=bp)

        # Missing Vega spectrum
        with pytest.raises(exceptions.SynphotError):
            self.bb.normalize(10 * units.VEGAMAG, band=self.abox)

        # Zero flux
        sp = SourceSpectrum(Const1D, amplitude=0)
        with pytest.raises(exceptions.SynphotError):
            sp.normalize(100 * u.ct, band=self.abox, area=_area)


class TestRedShift:
    """Test redshifted source spectrum.

    ``waveset`` already tested in `TestWaveset`.

    """
    def setup_class(self):
        x0 = 5000
        totflux = 1e-23 * (u.erg / (u.cm * u.cm * u.s))  # 1 Jy * Hz
        fwhm = 100
        self.sp_z0 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=fwhm)
        self.sp = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=fwhm)
        self.sp.z = 1.3

    def test_property(self):
        with pytest.raises(exceptions.SynphotError):
            self.sp.z = 1 * u.AA
        with pytest.raises(exceptions.SynphotError):
            self.sp.z_type = 'unknown_behavior'

        assert self.sp_z0.z == 0
        assert self.sp.z == 1.3
        assert self.sp_z0.z_type == self.sp.z_type == 'wavelength_only'

        assert isinstance(self.sp_z0.model, Gaussian1D)
        if ASTROPY_LT_4_0:
            assert isinstance(self.sp.model, modeling.core._CompoundModel)
        else:
            assert isinstance(self.sp.model, modeling.core.CompoundModel)

    def test_composite_redshift(self):
        sp2 = self.sp_z0 + self.sp  # centers: 5000, 11500
        sp2.z = 0.5  # centers: 7500, 17250
        assert_quantity_allclose(sp2([7500, 17250]), self.sp_z0(5000))

    def test_const_flux_redshift(self):
        """Constant flux in Jy is not constant in PHOTLAM."""
        sp_z0 = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy)
        sp = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy, z=1.3)
        assert_quantity_allclose(sp_z0(3000), sp(6900))

    def test_conserve_flux_redshift(self):
        """Test redshift behavior that conserves flux."""
        sp = SourceSpectrum(self.sp_z0.model, z=1.3, z_type='conserve_flux')
        fac = 1 / (1 + sp.z)
        wave = [5000, 11500]
        assert_quantity_allclose(sp(wave), self.sp(wave) * fac)
        assert_quantity_allclose(sp.integrate(), self.sp_z0.integrate())


@pytest.mark.skipif('not HAS_SPECUTILS')
class TestSpecutilsBridgeSource:
    def test_from_spectrum1d_Empirical1D_source(self):
        import specutils

        lamb = [1000, 5000, 10000] * u.AA
        flux = [0, -0.5e-17, 5.6e-17] * units.FLAM
        spec = specutils.Spectrum1D(spectral_axis=lamb, flux=flux)
        spec.meta['source'] = [1, 2, 3]
        with pytest.warns(AstropyUserWarning,
                          match=r'contained negative flux or throughput'):
            sp = SourceSpectrum.from_spectrum1d(spec, keep_neg=False)

        w = sp.waveset
        y = sp(w, flux_unit=units.FLAM)
        assert isinstance(sp.model, Empirical1D)
        assert sp.meta['header']['source'] == spec.meta['source']
        assert_quantity_allclose(w, lamb)
        assert_quantity_allclose(y, [0, 0, 5.6e-17] * units.FLAM)

        # Ensure metadata is copied, not referenced
        spec.meta['source'][1] = 99
        assert sp.meta['header']['source'] == [1, 2, 3]
        sp.meta['header']['source'][0] = 100
        assert spec.meta['source'] == [1, 99, 3]

    def test_from_spectrum1d_Empirical1D_source_masked(self):
        import specutils

        lamb = [1000, 5000, 10000] * u.AA
        flux = [0, -0.5e-17, 5.6e-17] * units.FLAM
        mask = np.array([False, True, False])
        spec = specutils.Spectrum1D(spectral_axis=lamb, flux=flux, mask=mask)
        sp = SourceSpectrum.from_spectrum1d(spec, keep_neg=False)

        w = sp.waveset
        y = sp(w, flux_unit=units.FLAM)
        assert_quantity_allclose(w, [1000, 10000] * u.AA)
        assert_quantity_allclose(y, [0, 5.6e-17] * units.FLAM)

    def test_to_spectrum1d_Empirical1D_source(self):
        lamb = [1000, 5000, 10000] * u.AA
        flux = [1.5, 0.5, 99.9] * u.nJy
        sp = SourceSpectrum(Empirical1D, points=lamb, lookup_table=flux,
                            meta={'source': 'foo'})
        spec = sp.to_spectrum1d(flux_unit=u.nJy)

        assert_quantity_allclose(spec.spectral_axis, lamb)
        assert_quantity_allclose(spec.flux, flux)
        assert spec.meta['source'] == 'foo'

        # Ensure redshifting does not change Spectrum1D
        sp.z = 0.1
        assert_quantity_allclose(spec.flux, flux)
        with pytest.raises(AssertionError):
            assert_quantity_allclose(sp(lamb, flux_unit=u.nJy), flux)

        # Unsupported flux unit
        with pytest.raises(exceptions.SynphotError) as e:
            sp.to_spectrum1d(flux_unit=u.count)
        assert 'Area is compulsory' in str(e.value)

    def test_to_spectrum1d_GaussianFlux1D(self):
        from specutils.analysis import gaussian_fwhm

        total_flux = 1 * (u.erg / u.s / u.cm / u.cm)
        fwhm = 10 * u.AA
        sp = SourceSpectrum(GaussianFlux1D, mean=5000 * u.AA, fwhm=fwhm,
                            total_flux=total_flux)
        spec = sp.to_spectrum1d(flux_unit=units.FLAM)

        assert_quantity_allclose(spec.spectral_axis, sp.waveset)
        assert_quantity_allclose(
            spec.flux, sp(sp.waveset, flux_unit=units.FLAM))
        assert_quantity_allclose(gaussian_fwhm(spec), fwhm, rtol=1e-5)
        assert spec.meta['expr'] == 'em(5000, 10, 1, FLAM)'

    def test_to_spectrum1d_ConstFlux1D(self):
        flux = 1 * units.PHOTLAM
        sp = SourceSpectrum(ConstFlux1D, amplitude=flux)

        with pytest.raises(exceptions.SynphotError) as e:
            spec = sp.to_spectrum1d()
        assert 'Provide wavelengths for sampling' in str(e.value)

        w = [100, 500, 1000] * u.nm
        spec = sp.to_spectrum1d(wavelengths=w)

        assert_quantity_allclose(spec.spectral_axis, w)
        assert_quantity_allclose(spec.flux, flux)
        assert len(spec.meta) == 0

    def test_to_spectrum1d_compound_source(self):
        from specutils.analysis import line_flux

        total_flux = 0.5 * (u.erg / u.s / u.cm / u.cm)
        fwhm = 1 * u.AA
        g1 = SourceSpectrum(GaussianFlux1D, mean=300 * u.nm, fwhm=fwhm,
                            total_flux=total_flux)
        g2 = SourceSpectrum(GaussianFlux1D, mean=400 * u.nm, fwhm=fwhm,
                            total_flux=total_flux)
        sp = g1 + g2
        spec = sp.to_spectrum1d(flux_unit=units.FLAM)
        integrated_flux = sp.integrate(flux_unit=units.FLAM)
        assert_quantity_allclose(
            integrated_flux, 1 * total_flux.unit, rtol=0.002)
        assert_quantity_allclose(integrated_flux, line_flux(spec), rtol=1e-5)
