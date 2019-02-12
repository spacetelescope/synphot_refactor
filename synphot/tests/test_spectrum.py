# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and related functionalities."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
import astropy
from astropy import modeling
from astropy import units as u
from astropy.io import fits
from astropy.modeling.models import (
    BrokenPowerLaw1D, Const1D, ExponentialCutoffPowerLaw1D, LogParabola1D,
    PowerLaw1D, RedshiftScaleFactor)
from astropy.utils import minversion
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .test_units import _area, _wave, _flux_jy, _flux_photlam, _flux_vegamag
from .. import exceptions, units
from ..models import (
    BlackBodyNorm1D, Box1D, ConstFlux1D, Empirical1D, Gaussian1D,
    GaussianAbsorption1D, GaussianFlux1D, Lorentz1D, MexicanHat1D,
    PowerLawFlux1D, get_waveset)
from ..observation import Observation
from ..spectrum import SourceSpectrum, SpectralElement

try:
    import scipy
except ImportError:
    HAS_SCIPY = False
else:
    HAS_SCIPY = True

HAS_SCIPY = HAS_SCIPY and minversion(scipy, '0.14')
ASTROPY_LT_20 = not minversion(astropy, '2.0')

# GLOBAL VARIABLES
_vspec = None  # Loaded in test_load_vspec()


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


@pytest.mark.remote_data
@pytest.mark.skipif('not HAS_SCIPY')
def test_load_vspec():
    """Load VEGA spectrum once here to be used later."""
    global _vspec
    _vspec = SourceSpectrum.from_vega()


@pytest.mark.remote_data
@pytest.mark.skipif('not HAS_SCIPY')
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
    np.testing.assert_allclose(result.value, ans.value, rtol=1e-2)
    assert result.unit == ans.unit

    # Scalar
    i = 0
    result = units.convert_flux(_wave[i], in_q[i], out_u, vegaspec=_vspec)
    np.testing.assert_allclose(result.value, ans[i].value, rtol=1e-2)
    assert result.unit == ans[i].unit


@pytest.mark.remote_data
@pytest.mark.skipif('not HAS_SCIPY')
@pytest.mark.parametrize(
    'filtername',
    ['bessel_j', 'bessel_h', 'bessel_k', 'cousins_r', 'cousins_i',
     'johnson_u', 'johnson_b', 'johnson_v', 'johnson_r', 'johnson_i',
     'johnson_j', 'johnson_k'])
def test_filter(filtername):
    """Test loading pre-defined bandpass.

    .. note::

        Filter data quality is not checked as it depends on the file.

    """
    bp = SpectralElement.from_filter(filtername)
    assert isinstance(bp.model, Empirical1D)
    assert filtername in bp.meta['expr']


def test_filter_exception():
    """Test SpectralElement from_filter() exception."""
    with pytest.raises(exceptions.SynphotError):
        SpectralElement.from_filter('foo')


@pytest.mark.skipif('not HAS_SCIPY')
class TestEmpiricalSourceFromFile(object):
    """This is the most common model used in ASTROLIB PYSYNPHOT."""
    def setup_class(self):
        specfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'))
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
        np.testing.assert_allclose(
            self.sp.waverange.value, [3479.99902344, 10500.00097656])

    def test_call(self):
        w = self.sp.model.points[0][5000:5004]
        y = units.convert_flux(w, self.sp(w), units.FLAM)
        np.testing.assert_allclose(
            w, [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            y.value,
            [1.87284130e-15, 1.85656811e-15, 1.84030867e-15, 1.82404183e-15])

    def test_neg_flux(self):
        w = [1000, 5000, 9000]
        sp = SourceSpectrum(
            Empirical1D, points=w, lookup_table=[100, -45, 5e-17])
        np.testing.assert_array_equal(sp(w).value, [100, 0, 5e-17])
        assert 'NegativeFlux' in sp.warnings

    def test_conversion(self):
        x = 0.60451641 * u.micron
        w, y = self.sp._get_arrays(x, flux_unit=units.FNU)
        np.testing.assert_allclose(x.value, w.value)
        np.testing.assert_allclose(y.value, 2.282950185743497e-26, rtol=1e-6)

    def test_integrate(self):
        expected_unit = u.erg / (u.cm**2 * u.s)
        # Whole range
        f = self.sp.integrate(flux_unit=units.FLAM)
        np.testing.assert_allclose(f.value, 8.460125829057308e-12, rtol=1e-5)
        assert f.unit == expected_unit

        # Given range
        f = self.sp.integrate(wavelengths=_wave, flux_unit=units.FLAM)
        np.testing.assert_allclose(f.value, 4.810058069909525e-14, rtol=1e-5)
        assert f.unit == expected_unit

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
        np.testing.assert_allclose(
            x.value, [4954.05152484, 4956.8, 4959.55, 4962.3, 4965.05152484])
        np.testing.assert_allclose(
            y.value, [0, 3.9135e-14, 4.0209e-14, 3.9169e-14, 0], rtol=1e-6)


@pytest.mark.skipif('not HAS_SCIPY')
class TestEmpiricalBandpassFromFile(object):
    """This is the most common model used in ASTROLIB PYSYNPHOT."""
    def setup_class(self):
        bandfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w.fits'))
        self.bp = SpectralElement.from_file(bandfile)

    def test_invalid_flux_unit(self):
        with pytest.raises(u.UnitsError):
            SpectralElement(Empirical1D, points=_wave,
                            lookup_table=_flux_photlam)

    def test_call(self):
        w = self.bp.model.points[0][5000:5004]
        y = self.bp(w)
        np.testing.assert_allclose(
            w, [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            y.value, [0.0920415, 0.09125588, 0.09047068, 0.08968487])

    def test_integrate(self):
        # Whole range (same as EQUVW)
        f = self.bp.integrate()
        np.testing.assert_allclose(f.value, 272.01081629459344)
        assert f.unit == u.AA

        # Given range
        f = self.bp.integrate(wavelengths=_wave)
        np.testing.assert_allclose(f.value, 1.2062975715374322, rtol=2.5e-6)
        assert f.unit == u.AA

    def test_avgwave(self):
        """Compare AVGWAVE with old SYNPHOT result."""
        w = self.bp.avgwave()
        np.testing.assert_allclose(w.value, 5367.9, rtol=1e-5)

    def test_barlam(self):
        """Test BARLAM (no old SYNPHOT result available)."""
        w = self.bp.barlam()
        np.testing.assert_allclose(w.value, 5331.8945, rtol=1e-5)

    def test_pivot(self):
        """Compare PIVWV with ASTROLIB PYSYNPHOT result."""
        w = self.bp.pivot()
        np.testing.assert_allclose(w.value, 5355.863596422962, rtol=1e-6)

    def test_uresp(self):
        """Compare URESP with old SYNPHOT result."""
        uresp = self.bp.unit_response(area=_area)
        np.testing.assert_allclose(uresp.value, 3.00737e-19, rtol=1e-4)
        assert uresp.unit == units.FLAM

    def test_rmswidth(self):
        w = self.bp.rmswidth()
        np.testing.assert_allclose(w.value, 359.55954282883687, rtol=1e-4)

        w = self.bp.rmswidth(threshold=0.01 * u.dimensionless_unscaled)
        np.testing.assert_allclose(w.value, 357.43298216917754, rtol=1e-4)

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold=0.01 * u.AA)
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold='foo')

    def test_fwhm(self):
        """This also calls PHOTBW."""
        w = self.bp.fwhm()
        np.testing.assert_allclose(w.value, 841.09, rtol=2.5e-5)

        w = self.bp.fwhm(threshold=0.01 * u.dimensionless_unscaled)
        np.testing.assert_allclose(w.value, 836.2879507505378, rtol=2.5e-5)

        # Zero value
        w = self.bp.fwhm(wavelengths=[2e6, 2.1e6])
        assert w.value == 0

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.fwhm(threshold=0.01 * u.AA)
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.fwhm(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.fwhm(threshold='foo')

    def test_tlambda(self):
        f = self.bp.tlambda()
        np.testing.assert_allclose(f.value, 0.22808, rtol=1e-4)

    def test_tpeak(self):
        """Compare TPEAK with old SYNPHOT result."""
        f = self.bp.tpeak()
        np.testing.assert_allclose(f.value, 0.241445)

    def test_wpeak(self):
        w = self.bp.wpeak()
        np.testing.assert_allclose(w.value, 5059.8, rtol=1e-5)

    def test_equivwidth(self):
        """Compare EQUVW with ASTROLIB PYSYNPHOT result."""
        w = self.bp.equivwidth()
        np.testing.assert_allclose(w.value, 272.01081629459344, rtol=1e-6)
        assert w.unit == u.AA

    def test_rectw(self):
        """Compare RECTW with old SYNPHOT result."""
        w = self.bp.rectwidth()
        np.testing.assert_allclose(w.value, 1126.588, rtol=1e-5)

    def test_qtlam(self):
        qtlam = self.bp.efficiency()
        np.testing.assert_allclose(qtlam.value, 0.050901, rtol=1e-4)
        assert qtlam.unit == u.dimensionless_unscaled

    def test_emflx(self):
        """Compare EMFLX with old SYNPHOT result."""
        f = self.bp.emflx(area=_area)
        np.testing.assert_allclose(f.value, 3.586622e-16, rtol=2.5e-5)
        assert f.unit == units.FLAM


class TestBoxBandpass(object):
    """Test bandpass with Box1D model."""
    def setup_class(self):
        self.bp = SpectralElement(Box1D, amplitude=1, x_0=5000, width=100)

    def test_eval(self):
        # Box: Outside, boundary, inside
        y = self.bp([4000, 4949.95, 5000])
        np.testing.assert_array_equal(y.value, [0, 0, 1])

    def test_conversion(self):
        bp2 = SpectralElement(
            Box1D, amplitude=1, x_0=500 * u.nm, width=10 * u.nm)
        y = bp2([4000, 4949.95, 5000])
        np.testing.assert_array_equal(y.value, [0, 0, 1])

    def test_fwhm(self):
        # You would think FWHM of a box is the width but
        # not according to IRAF SYNPHOT.
        np.testing.assert_allclose(self.bp.fwhm().value, 67.977,
                                   rtol=1e-3)  # 0.1%

    def test_taper(self):
        bp2 = self.bp.taper(np.arange(499, 501.01, 0.01) * u.nm)
        y = bp2([498.9, 499, 500, 501, 501.1] * u.nm)
        np.testing.assert_allclose(y.value, [0, 1, 1, 1, 0])

    def test_multi_n_models(self):
        """This is not allowed."""
        with pytest.raises(exceptions.SynphotError):
            SpectralElement(
                Box1D, amplitude=[1, 1], x_0=[5000, 6000],
                width=[100, 1], n_models=2)


class TestBlackBodySource(object):
    """Test source spectrum with BlackBody1D model."""
    def setup_class(self):
        self.sp = SourceSpectrum(BlackBodyNorm1D, temperature=5500)

    def test_eval(self):
        w = np.arange(3000, 3100, 10)
        y = self.sp(w)
        np.testing.assert_allclose(
            y.value,
            [0.00019318, 0.00019623, 0.0001993, 0.00020238, 0.00020549,
             0.00020861, 0.00021175, 0.00021491, 0.00021809, 0.00022128],
            rtol=2.5e-3)


class TestGaussianSource(object):
    """Test source spectrum with GaussianFlux1D model."""
    def setup_class(self):
        tf = 4.96611456e-12 * u.erg / (u.cm * u.cm * u.s)
        self.sp = SourceSpectrum(
            GaussianFlux1D, total_flux=tf, mean=4000, fwhm=100)

    def test_eval(self):
        y = self.sp([3900, 4000, 4060])
        np.testing.assert_allclose(
            y.value, [0.00058715, 0.00939437, 0.00346246], rtol=1e-5)

    def test_totalflux(self):
        # PHOTLAM
        f = self.sp.integrate()
        np.testing.assert_allclose(f.value, 1, rtol=1e-5)
        assert f.unit == u.photon / (u.cm**2 * u.s)

        # FLAM
        x0 = (400 * u.nm).to(u.AA).value
        fwhm = (10 * u.nm).to(u.AA)
        sp2 = SourceSpectrum(
            GaussianFlux1D, total_flux=1, mean=x0, fwhm=fwhm)
        val = sp2.integrate(flux_unit=units.FLAM).value
        np.testing.assert_allclose(val, 1, rtol=1e-3)

    def test_symmetry(self):
        np.testing.assert_allclose(self.sp(3950), self.sp(4050))

    def test_fwhm(self):
        """Should round-trip back to the same bandpass FWHM."""
        m = self.sp.model
        bp = SpectralElement(
            Gaussian1D, mean=m.mean, amplitude=m.amplitude, stddev=m.stddev)
        np.testing.assert_allclose(bp.fwhm().value, 100, rtol=1e-3)  # 0.1%

    def test_alt_source(self):
        """Same source, different way to init."""
        sp2 = SourceSpectrum(
            GaussianFlux1D, amplitude=self.sp.model.amplitude.value,
            mean=self.sp.model.mean.value, stddev=self.sp.model.stddev.value)
        w = [3900, 4000, 4060] * u.AA
        np.testing.assert_allclose(sp2(w), self.sp(w))


def test_gaussian_source_watts():
    """https://github.com/spacetelescope/synphot_refactor/issues/153"""
    mu = 1 * u.um
    fwhm = (0.01 / 0.42466) * u.um
    flux = 1 * u.W / u.m**2

    sp = SourceSpectrum(GaussianFlux1D, mean=mu, fwhm=fwhm, total_flux=flux)
    tf = sp.integrate(flux_unit=units.FLAM)
    np.testing.assert_allclose(tf.to(flux.unit), flux, rtol=1e-4)


class TestPowerLawSource(object):
    """Test source spectrum with PowerLawFlux1D model."""
    def setup_class(self):
        self.sp = SourceSpectrum(PowerLawFlux1D, amplitude=1, x_0=6000,
                                 alpha=4)

    def test_no_default_wave(self):
        assert self.sp.waverange == [None, None]

        with pytest.raises(exceptions.SynphotError):
            self.sp(None)

    def test_eval(self):
        w = np.arange(3000, 3100, 10)
        y = self.sp(w)
        np.testing.assert_allclose(
            y.value,
            [16, 15.78843266, 15.58035072, 15.37568551, 15.17436992,
             14.97633838, 14.78152682, 14.5898726, 14.40131453, 14.21579277],
            rtol=1e-6)

    def test_normalization(self):
        np.testing.assert_allclose(self.sp(600 * u.nm).value, 1)


class TestBuildModels(object):
    """Test compatiblity with other models not tested above."""
    def test_BrokenPowerLaw1D(self):
        sp = SourceSpectrum(
            BrokenPowerLaw1D, amplitude=1, x_break=6000, alpha_1=1,
            alpha_2=4)
        y = sp([5000, 6000, 7000])
        np.testing.assert_allclose(y.value, [1.2, 1, 0.53977509])

    def test_Const1D(self):
        sp = SourceSpectrum(Const1D, amplitude=1)
        y = sp([1, 1000, 1e6])
        np.testing.assert_array_equal(y.value, 1)

    def test_ConstFlux1D(self):
        sp = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy)
        w = [1, 1000, 1e6]
        y = units.convert_flux(w, sp(w), u.Jy)
        np.testing.assert_allclose(y.value, 1)

    def test_ExponentialCutoffPowerLaw1D(self):
        sp = SourceSpectrum(
            ExponentialCutoffPowerLaw1D, amplitude=1, x_0=6000,
            x_cutoff=10000, alpha=4)
        y = sp([5000, 6000, 10000])
        np.testing.assert_allclose(
            y.value, [1.25770198, 0.54881164, 0.04767718])

    def test_GaussianAbsorption1D(self):
        """This should be unitless, not a source spectrum."""
        bp = SpectralElement(
            GaussianAbsorption1D, amplitude=0.8, mean=5500, stddev=50)
        y = bp([5300, 5500, 5700])
        np.testing.assert_allclose(y.value, [0.99973163, 0.2, 0.99973163])

    def test_LogParabola1D(self):
        sp = SourceSpectrum(
            LogParabola1D, amplitude=1, x_0=6000, alpha=1, beta=4)
        y = sp([5000, 6000, 7000])
        np.testing.assert_allclose(y.value, [1.0505953, 1, 0.77942375])

    def test_Lorentz1D(self):
        sp = SourceSpectrum(Lorentz1D, amplitude=1, x_0=6000, fwhm=100)
        y = sp([5000, 6000, 7000])
        np.testing.assert_allclose(
            y.value, [0.00249377, 1, 0.00249377], rtol=1e-5)

    def test_MexicanHat1D(self):
        sp = SourceSpectrum(MexicanHat1D, amplitude=1, x_0=6000, sigma=100)
        y = sp([5000, 6000, 7000])
        np.testing.assert_allclose(
            y.value, [-1.90946235e-20, 1, -1.90946235e-20])

    def test_PowerLaw1D(self):
        sp = SourceSpectrum(PowerLaw1D, amplitude=1, x_0=6000, alpha=4)
        y = sp([5000, 6000, 7000])
        np.testing.assert_allclose(y.value, [2.0736, 1, 0.53977509])


@pytest.mark.skipif('not HAS_SCIPY')
class TestCheckOverlap(object):
    """Test spectrum overlap check. This method is ever only used
    in the form of ``bp.check_overlap(sp)``, so that is what is
    tested here.
    """
    def setup_class(self):
        self.bp = SpectralElement(
            Empirical1D, points=[2999.9, 3000, 6000, 6000.1],
            lookup_table=[0, 1, 1, 0])

    def test_full(self):
        """As long as we don't have to extrapolate or taper
        source spectrum, it's okay.
        """
        sp = SourceSpectrum(
            Empirical1D, points=[999.9, 1000, 9000, 9000.1],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'full'

        sp = SourceSpectrum(
            Empirical1D, points=[3999.9, 4000, 4500, 4500.1],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'full'

    def test_partial_most(self):
        """99% overlap."""
        sp = SourceSpectrum(
            Empirical1D, points=[3005, 3005.1, 6000.1, 6000.2],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'partial_most'

    def test_partial_notmost(self):
        """Extrapolation or taper required."""
        sp = SourceSpectrum(
            Empirical1D, points=[3999.9, 4500.1], lookup_table=[1, 1])
        assert self.bp.check_overlap(sp) == 'partial_notmost'

    def test_none(self):
        """No overlap at all."""
        sp = SourceSpectrum(
            Empirical1D, points=[99.9, 100, 2999.8, 2999.9],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'none'

    def test_special_cases(self):
        """One of them has no waveset defined."""
        # Other has no waveset
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert self.bp.check_overlap(sp) == 'full'

        # Self has no waveset
        bp = SpectralElement(Const1D, amplitude=1)
        sp = SourceSpectrum(Box1D, amplitude=1, x_0=5000, width=10)
        assert bp.check_overlap(sp) == 'partial_notmost'

    def test_exceptions(self):
        """Invalid input."""
        with pytest.raises(exceptions.SynphotError):
            self.bp.check_overlap(1)


class TestForceExtrap(object):
    """Test forcing extrapolation on a source spectrum."""

    @pytest.mark.skipif('not HAS_SCIPY')
    @pytest.mark.parametrize('z', [0, 0.03])
    def test_empirical(self, z):
        sp = SourceSpectrum(Empirical1D, points=[1000, 2000, 3000, 4000],
                            lookup_table=[0.5, 0.6, 10.6, 1.5], fill_value=0)
        sp.z = z
        w = [900, 4300]
        np.testing.assert_allclose(sp(w).value, 0)  # No extrapolation

        is_forced = sp.force_extrapolation()  # Force extrapolation
        assert is_forced
        np.testing.assert_allclose(sp(w).value, [0.5, 1.5])

    def test_analytical(self):
        """Forcing is not possible."""
        sp = SourceSpectrum(GaussianFlux1D, mean=5500, total_flux=1, fwhm=10)
        w = [100, 10000]
        np.testing.assert_allclose(sp(w).value, 0)

        is_forced = sp.force_extrapolation()
        assert not is_forced
        np.testing.assert_allclose(sp(w).value, 0)


@pytest.mark.skipif('not HAS_SCIPY')
class TestNormalize(object):
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
            os.path.join('data', 'hst_acs_hrc_f555w.fits'))
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
        obs = Observation(rn_sp, self.acs, force='extrap')
        ct_rate = obs.countrate(_area)

        # 0.1% agreement with IRAF SYNPHOT COUNTRATE
        np.testing.assert_allclose(ct_rate.value, ans_countrate, rtol=1e-3)

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
        rn_sp = sp.normalize(1e-23 * u.Jy, band=self.acs, force=True)
        assert 'PartialRenorm' in rn_sp.warnings
        assert 'PartialRenorm' not in sp.warnings

        # Partial overlap without force
        with pytest.raises(exceptions.PartialOverlap):
            sp.normalize(1, band=self.acs)

    def test_renorm_partial_most(self):
        """Test 'partial_most' overlap."""
        bp = SpectralElement(Box1D, amplitude=1, x_0=5600, width=870)
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


class TestWaveset(object):
    """Tests related to spectrum waveset."""
    def test_none(self):
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert sp.waveset is None

    def test_sampleset(self):
        tf_unit = u.erg / (u.cm * u.cm * u.s)
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=(1 * tf_unit), mean=5000, fwhm=10)
        np.testing.assert_array_equal(sp.waveset.value, sp.model.sampleset())

    def test_box1d(self):
        bp = SpectralElement(Box1D, x_0=2000, width=1)
        w = bp.waveset.value

        np.testing.assert_array_equal(w, bp.model.sampleset())
        np.testing.assert_allclose(
            w[([0, 1, -2, -1], )], bp.model.sampleset(minimal=True))

    def test_composite_none(self):
        bp1 = SpectralElement(Box1D, amplitude=1, x_0=5000, width=10)
        bp2 = SpectralElement(Const1D, amplitude=2)
        bp = bp1 * bp2
        np.testing.assert_array_equal(bp.waveset, bp1.waveset)

    def test_composite(self):
        totflux = 1 * (u.erg / (u.cm * u.cm * u.s))
        g1 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=5000, fwhm=10)
        g2 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=6500, fwhm=100)
        g3 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=7500, fwhm=5)
        sp = SpectralElement(Box1D, x_0=1000, width=1) * (g1 + g2 + g3)
        np.testing.assert_allclose(
            sp.waveset.value[::100],
            [999.49, 1000.49, 5019.95906231, 6699.59062307, 7509.7672007])

    def test_redshift(self):
        tf_unit = u.erg / (u.cm * u.cm * u.s)
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=(1 * tf_unit), mean=5000, fwhm=10)
        sp.z = 1.3
        m = RedshiftScaleFactor(z=1.3)
        w_step25_z0 = [4978.76695499, 4989.3834775, 5000, 5010.6165225]
        np.testing.assert_allclose(sp.waveset.value[::25], m(w_step25_z0))

    def test_redshift_none(self):
        sp = SourceSpectrum(Const1D, amplitude=1, z=1.3)
        assert sp.waveset is None

    def test_exceptions(self):
        with pytest.raises(exceptions.SynphotError):
            get_waveset('foo')


class TestRedShift(object):
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
        assert isinstance(self.sp.model, modeling.core._CompoundModel)

    def test_composite_redshift(self):
        sp2 = self.sp_z0 + self.sp  # centers: 5000, 11500
        sp2.z = 0.5  # centers: 7500, 17250
        np.testing.assert_allclose(sp2([7500, 17250]), self.sp_z0(5000))

    def test_const_flux_redshift(self):
        """Constant flux in Jy is not constant in PHOTLAM."""
        sp_z0 = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy)
        sp = SourceSpectrum(ConstFlux1D, amplitude=1 * u.Jy, z=1.3)
        np.testing.assert_allclose(sp_z0(3000), sp(6900))

    def test_conserve_flux_redshift(self):
        """Test redshift behavior that conserves flux."""
        sp = SourceSpectrum(self.sp_z0.model, z=1.3, z_type='conserve_flux')
        fac = 1 / (1 + sp.z)
        wave = [5000, 11500]
        np.testing.assert_allclose(sp(wave), self.sp(wave) * fac)
        np.testing.assert_allclose(sp.integrate(), self.sp_z0.integrate())


@pytest.mark.skipif('not HAS_SCIPY')
class TestMathOperators(object):
    """Test spectrum math operators."""
    def setup_class(self):
        self.sp_1 = SourceSpectrum(
            Empirical1D, points=[3999.9, 4000.0, 5000.0, 6000.0, 6000.1],
            lookup_table=[0, 3.5e-14, 4e-14, 4.5e-14, 0] * units.FLAM)
        self.sp_2 = SourceSpectrum(
            Empirical1D, points=_wave, lookup_table=_flux_jy,
            meta={'PHOTLAM': [9.7654e-3, 1.003896e-2, 9.78473e-3]})
        self.bp_1 = SpectralElement(
            Empirical1D, points=[399.99, 400.01, 500.0, 590.0, 600.1] * u.nm,
            lookup_table=[0, 0.1, 0.2, 0.3, 0])

    def test_source_add(self):
        """Compare with ASTROLIB PYSYNPHOT."""
        ans = self.sp_1 + self.sp_2
        np.testing.assert_allclose(
            ans(ans.waveset).value,
            [0.00976521, 0.01681283, 0.01970276, 0.01998463, 0.0197387,
             0.01985257, 0.02337638, 0.00978454], rtol=1e-4)

    def test_source_sub(self):
        """Compare with ASTROLIB PYSYNPHOT."""
        ans = self.sp_1 - self.sp_2
        np.testing.assert_allclose(
            ans(ans.waveset).value,
            [-9.76520783e-03, -2.71758275e-03, 1.72346256e-04, -9.29051118e-05,
             1.69629843e-04, 2.83499328e-04, 3.80731187e-03, -9.78453651e-03],
            rtol=1e-4)

    def test_source_addsub_circular(self):
        """sp = sp + sp - sp"""
        ans = self.sp_1 + self.sp_1 - self.sp_1
        np.testing.assert_array_equal(ans(ans.waveset), self.sp_1(ans.waveset))

    def test_source_addsub_exception(self):
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 + self.bp_1

    @pytest.mark.parametrize('x', [2, 2 * u.dimensionless_unscaled])
    def test_source_mul_div_scalar(self, x):
        w = self.sp_1.waveset.value

        ans1 = self.sp_1 * x
        np.testing.assert_allclose(
            ans1(w).value, [0, 0.01409552, 0.02013646, 0.02718424, 0],
            rtol=1e-6)

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.sp_1
            np.testing.assert_array_equal(ans1(w), ans2(w))

        ans3 = self.sp_1 / x
        np.testing.assert_allclose(
            ans3(w).value, [0, 0.00352388, 0.00503411, 0.00679606, 0],
            atol=1e-7)

    def test_source_mul_div_spec(self):
        """Compare mul with ASTROLIB PYSYNPHOT. Also test bp * sp."""
        ans1 = self.sp_1 * self.bp_1
        ans2 = self.bp_1 * self.sp_1
        w = ans1.waveset[:-1]
        np.testing.assert_allclose(
            ans1(w).value,
            [0, 3.52381254e-04, 7.04792712e-04, 2.01360717e-03, 3.97184014e-03,
             4.03718269e-05, 0], rtol=1e-4)
        np.testing.assert_array_equal(ans1(w), ans2(w))

        ans3 = self.sp_1 / self.bp_1
        np.testing.assert_allclose(
            ans3(w).value,
            [0, 0.14095528, 0.07048066, 0.05034117, 0.04413243, 4.57601236, 0])

        ans4 = self.sp_1 / self.sp_1
        np.testing.assert_allclose(
            ans4([4000, 5000, 6000]), 1 * u.dimensionless_unscaled)

        # Dividing throughput by flux does not make sense.
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 / self.sp_1

    def test_source_mul_div_exceptions(self):
        """Only mul is tested but truediv uses the same validation."""
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * self.sp_2

        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * (1 - 1j)

        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * u.Quantity([1, 2])
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * u.Quantity(1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * (1 * u.AA)

    def test_bandpass_addsub(self):
        """Not supported."""
        with pytest.raises(NotImplementedError):
            self.bp_1 + self.bp_1
        with pytest.raises(NotImplementedError):
            self.bp_1 + 2.0
        with pytest.raises(NotImplementedError):
            self.bp_1 - self.bp_1
        with pytest.raises(NotImplementedError):
            self.bp_1 - 2.0

    @pytest.mark.parametrize('x', [2.0, 2.0 * u.dimensionless_unscaled])
    def test_bandpass_mul_div_scalar(self, x):
        w = self.bp_1.waveset.value

        ans1 = self.bp_1 * x
        np.testing.assert_allclose(ans1(w).value, [0, 0.2, 0.4, 0.6, 0])

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.bp_1
            np.testing.assert_array_equal(ans1(w), ans2(w))

        ans3 = self.bp_1 / x
        np.testing.assert_allclose(ans3(w).value, [0, 0.05, 0.1, 0.15, 0])

    def test_bandpass_mul_div_bandpass(self):
        ans1 = self.bp_1 * self.bp_1
        np.testing.assert_allclose(
            ans1(ans1.waveset).value, [0, 0.01, 0.04, 0.09, 0])

        w = [4000.1, 5000, 5900]  # Avoid div by zero
        ans2 = self.bp_1 / self.bp_1
        np.testing.assert_allclose(ans2(w), 1)

    def test_bandpass_mul_div_exceptions(self):
        """Only mul is tested but truediv uses the same validation."""
        class DummyObject(object):
            pass

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * DummyObject()

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * u.Quantity([1, 2])
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * u.Quantity(1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * (1 * u.AA)

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * (1 - 1j)


@pytest.mark.skipif('not HAS_SCIPY')
class TestWriteSpec(object):
    """Test spectrum to_fits() method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.sp = SourceSpectrum(
            Empirical1D, points=_wave, lookup_table=_flux_photlam,
            meta={'expr': 'Test source'})
        self.bp = SpectralElement(
            Empirical1D, points=_wave, lookup_table=np.ones(_wave.shape),
            meta={'expr': 'Test bandpass'})

    @pytest.mark.parametrize(
        ('is_sp', 'ext_hdr'),
        [(True, None),
         (True, {'foo': 'foo'}),
         (False, None),
         (False, {'foo': 'foo'})])
    def test_write(self, is_sp, ext_hdr):
        outfile = os.path.join(self.outdir, 'outspec.fits')

        if is_sp:
            sp1 = self.sp
        else:
            sp1 = self.bp

        if ext_hdr is None:
            sp1.to_fits(outfile, overwrite=True, trim_zero=False,
                        pad_zero_ends=False)
        else:
            sp1.to_fits(outfile, overwrite=True, trim_zero=False,
                        pad_zero_ends=False, ext_header=ext_hdr)

        # Read it back in and check
        sp2 = sp1.__class__.from_file(outfile)
        np.testing.assert_allclose(sp2(sp2.waveset), sp1(sp1.waveset))
        hdr = fits.getheader(outfile, 1)
        assert 'expr' in hdr
        if ext_hdr is not None:
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
