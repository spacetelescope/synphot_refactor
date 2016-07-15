# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and related functionalities."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np

try:
    import scipy  # pylint: disable=W0611
except ImportError:
    HAS_SCIPY = False
else:
    HAS_SCIPY = True

# ASTROPY
from astropy import modeling
from astropy import units as u
from astropy.io import fits
from astropy.modeling.models import (
    BrokenPowerLaw1D, Const1D, ExponentialCutoffPowerLaw1D, LogParabola1D,
    PowerLaw1D, RedshiftScaleFactor)
from astropy.tests.helper import pytest, remote_data
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

# GLOBAL VARIABLES
_vspec = None  # Loaded in test_load_vspec()


@remote_data
@pytest.mark.skipif('not HAS_SCIPY')
def test_load_vspec():
    """Load VEGA spectrum once here to be used later."""
    global _vspec
    _vspec = SourceSpectrum.from_vega(encoding='binary')


@remote_data
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


@remote_data
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
    bp = SpectralElement.from_filter(filtername, encoding='binary')
    assert isinstance(bp.model, Empirical1D)
    assert filtername in bp.meta['expr']


def test_filter_exception():
    """Test SpectralElement from_filter() exception."""
    with pytest.raises(exceptions.SynphotError):
        bp = SpectralElement.from_filter('foo')


@pytest.mark.skipif('not HAS_SCIPY')
class TestEmpiricalSourceFromFile(object):
    """This is the most common model used in ASTROLIB PYSYNPHOT."""
    def setup_class(self):
        specfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'))
        self.sp = SourceSpectrum.from_file(specfile)

    def test_invalid_flux_unit(self):
        with pytest.raises(exceptions.SynphotError):
            sp = SourceSpectrum(Empirical1D, x=_wave, y=_flux_vegamag)

    def test_metadata(self):
        assert 'SourceSpectrum' in str(self.sp)
        assert self.sp.meta['header']['SIMPLE']  # From FITS header
        assert self.sp.warnings == {}
        assert self.sp.z == 0
        np.testing.assert_allclose(
            self.sp.waverange.value, [3479.99902344, 10500.00097656])

    def test_call(self):
        w = self.sp.model.x.value[5000:5004]
        y = units.convert_flux(w, self.sp(w), units.FLAM)
        np.testing.assert_allclose(
            w, [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            y.value,
            [1.87284130e-15, 1.85656811e-15, 1.84030867e-15, 1.82404183e-15])

    def test_neg_flux(self):
        w = [1000, 5000, 9000]
        sp = SourceSpectrum(Empirical1D, x=w, y=[100, -45, 5e-17])
        np.testing.assert_array_equal(sp(w).value, [100, 0, 5e-17])
        assert 'NegativeFlux' in sp.warnings

    def test_conversion(self):
        x = 0.60451641 * u.micron
        w, y = self.sp._get_arrays(x, units.FNU)
        np.testing.assert_allclose(x.value, w.value)
        np.testing.assert_allclose(y.value, 2.282950185743497e-26, rtol=1e-6)

    def test_integrate(self):
        # Whole range
        f = self.sp.integrate(flux_unit=units.FLAM)
        np.testing.assert_allclose(f.value, 8.460125829057308e-12, rtol=1e-5)

        # Given range
        f = self.sp.integrate(wavelengths=_wave, flux_unit=units.FLAM)
        np.testing.assert_allclose(f.value, 4.810058069909525e-14, rtol=1e-5)

    def test_taper(self):
        # Original spectrum already tapered -- nothing done
        sp = self.sp.taper()
        assert sp is self.sp

        # Tapering is done
        sp2 = SourceSpectrum(Empirical1D, x=_wave, y=_flux_photlam)
        sp = sp2.taper()
        x, y = sp._get_arrays(None, units.FLAM)
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
            bp = SpectralElement(Empirical1D, x=_wave, y=_flux_photlam)

    def test_call(self):
        w = self.bp.model.x.value[5000:5004]
        y = self.bp(w)
        np.testing.assert_allclose(
            w, [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            y.value, [0.0920415, 0.09125588, 0.09047068, 0.08968487])

    def test_integrate(self):
        # Whole range (same as EQUVW)
        f = self.bp.integrate()
        np.testing.assert_allclose(f.value, 272.01081629459344)

        # Given range
        f = self.bp.integrate(wavelengths=_wave)
        np.testing.assert_allclose(f.value, 1.2062975715374322, rtol=2.5e-6)

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

        w = self.bp.rmswidth(threshold=0.01*u.dimensionless_unscaled)
        np.testing.assert_allclose(w.value, 357.43298216917754, rtol=1e-4)

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold=0.01*u.AA)
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.rmswidth(threshold='foo')

    def test_fwhm(self):
        """This also calls PHOTBW."""
        w = self.bp.fwhm()
        np.testing.assert_allclose(w.value, 841.09, rtol=2.5e-5)

        w = self.bp.fwhm(threshold=0.01*u.dimensionless_unscaled)
        np.testing.assert_allclose(w.value, 836.2879507505378, rtol=2.5e-5)

        # Zero value
        w = self.bp.fwhm(wavelengths=[2e6, 2.1e6])
        assert w.value == 0

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            w = self.bp.fwhm(threshold=0.01*u.AA)
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
        bp2 = SpectralElement(Box1D, amplitude=1, x_0=500*u.nm, width=10*u.nm)
        y = bp2([4000, 4949.95, 5000])
        np.testing.assert_array_equal(y.value, [0, 0, 1])

    def test_fwhm(self):
        # You would think FWHM of a box is the width but
        # not according to IRAF SYNPHOT.
        np.testing.assert_allclose(self.bp.fwhm().value, 67.977,
                                   rtol=1e-3)  # 0.1%

    def test_multi_n_models(self):
        """This is not allowed."""
        with pytest.raises(exceptions.SynphotError):
            bp = SpectralElement(
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
        self.sp = SourceSpectrum(
            GaussianFlux1D, total_flux=1, mean=4000, fwhm=100)

    def test_eval(self):
        y = self.sp([3900, 4000, 4060])
        np.testing.assert_allclose(
            y.value, [0.00058715, 0.00939437, 0.00346246], rtol=1e-5)

    def test_totalflux(self):
        # PHOTLAM
        val = self.sp.integrate().value
        np.testing.assert_allclose(val, 1, rtol=1e-5)

        # FLAM
        x0 = (400 * u.nm).to(u.AA).value
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM).value
        fwhm = (10 * u.nm).to(u.AA)
        sp2 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=fwhm)
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


class TestPowerLawSource(object):
    """Test source spectrum with PowerLawFlux1D model."""
    def setup_class(self):
        self.sp = SourceSpectrum(PowerLawFlux1D, amplitude=1, x_0=6000,
                                 alpha=4)

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
        sp = SourceSpectrum(ConstFlux1D, amplitude=1*u.Jy)
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
    """Test spectrum overlap check."""
    def setup_class(self):
        self.sp = SourceSpectrum(
            Empirical1D, x=[2999.9, 3000, 6000, 6000.1], y=[0, 1, 1, 0])

    def test_full(self):
        bp = SpectralElement(
            Empirical1D, x=[999.9, 1000, 9000, 9000.1], y=[0, 1, 1, 0])
        assert self.sp.check_overlap(bp) == 'full'

    def test_partial_most(self):
        bp = SpectralElement(
            Empirical1D, x=[3000, 3001, 6000.1, 6000.2], y=[0, 1, 1, 0])
        assert self.sp.check_overlap(bp) == 'partial_most'

    def test_partial_notmost(self):
        bp = SpectralElement(
            Empirical1D, x=[3999.9, 4000, 4500, 4500.1], y=[0, 1, 1, 0])
        assert self.sp.check_overlap(bp) == 'partial_notmost'

        # Ensure zeroes in passband are not taken into account
        bp2 = SpectralElement(
            Empirical1D, x=[3000, 3001, 6000.1, 6000.2], y=[0, 1, 1, 0])
        bp3 = bp2 * bp
        assert self.sp.check_overlap(bp2) == 'partial_most'
        assert self.sp.check_overlap(bp3) == 'partial_notmost'

    def test_none(self):
        bp = SpectralElement(
            Empirical1D, x=[99.9, 100, 2999.9, 3000], y=[0, 1, 1, 0])
        assert self.sp.check_overlap(bp) == 'none'

    def test_special_cases(self):
        # Other has no waveset
        bp = SpectralElement(Const1D, amplitude=1)
        assert self.sp.check_overlap(bp) == 'full'

        # Self has no waveset
        bp = SpectralElement(Box1D, amplitude=1, x_0=5000, width=10)
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert sp.check_overlap(bp) == 'partial_notmost'

    def test_exceptions(self):
        with pytest.raises(exceptions.SynphotError):
            self.sp.check_overlap(1)


@pytest.mark.skipif('not HAS_SCIPY')
class TestNormalize(object):
    """Test source spectrum normalization."""
    def setup_class(self):
        """``expr`` stores the equivalent IRAF SYNPHOT command."""
        # Blackbody: bb(5000)
        self.bb = SourceSpectrum(BlackBodyNorm1D, temperature=5000)

        # Gaussian emission line: em(5500, 250, 1e-13, flam)
        x0 = 5500
        totflux = units.convert_flux(
            x0, 1e-13 * units.FLAM, units.PHOTLAM).value
        self.em = SourceSpectrum(GaussianFlux1D, mean=x0, total_flux=totflux,
                                 fwhm=250)

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
        """This also tests force=True for 'partial_notmost' overlap."""
        sp = self._select_sp(sp_type)
        rn_sp = sp.normalize(rn_val, band=self.acs, force=True, area=_area)
        self._compare_countrate(rn_sp, ans_countrate)

        if sp_type == 'em':
            assert 'PartialRenorm' in rn_sp.warnings
            assert 'PartialRenorm' not in sp.warnings

    @remote_data
    @pytest.mark.parametrize(
        ('sp_type', 'ans_countrate'),
        [('bb', 115.9126),
         ('em', 27.2856)])
    def test_renorm_vegamag(self, sp_type, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.normalize(20 * units.VEGAMAG, band=self.abox,
                             vegaspec=_vspec)
        self._compare_countrate(rn_sp, ans_countrate)

    def test_renorm_noband(self):
        """No bandpass. This option is not offered by ASTROLIB PYSYNPHOT
        but can be indirectly calculated using a very large box as bandpass.

        """
        rn_sp = self.em.normalize(1 * u.ct, area=_area)
        x = rn_sp.integrate(flux_unit=u.ct, area=_area)
        ans = 10.615454634451927
        np.testing.assert_allclose(x.value, ans, rtol=1e-3)

    def test_exceptions(self):
        # Invalid passband
        with pytest.raises(exceptions.SynphotError):
            rn_sp = self.bb.normalize(10, band=np.ones(10))

        # Disjoint passband
        bp = SpectralElement(Box1D, amplitude=1, x_0=30000, width=1)
        with pytest.raises(exceptions.DisjointError):
            rn_sp = self.em.normalize(10, band=bp)

        # Partial overlap without force
        with pytest.raises(exceptions.PartialOverlap):
            rn_sp = self.em.normalize(1, band=self.acs)

        # Missing Vega spectrum
        with pytest.raises(exceptions.SynphotError):
            rn_sp = self.bb.normalize(10 * units.VEGAMAG, band=self.abox)

        # Zero flux
        sp = SourceSpectrum(Const1D, amplitude=0)
        with pytest.raises(exceptions.SynphotError):
            rn_sp = sp.normalize(100 * u.ct, band=self.abox, area=_area)


class TestWaveset(object):
    """Tests related to spectrum waveset."""
    def test_none(self):
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert sp.waveset is None

    def test_sampleset(self):
        x0 = 5000
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM).value
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=10)
        np.testing.assert_array_equal(sp.waveset.value, sp.model.sampleset())

    def test_box1d(self):
        bp = SpectralElement(Box1D, amplitude=1, x_0=5000, width=10)
        np.testing.assert_array_equal(bp.waveset.value, bp.model.sampleset())

    def test_composite_none(self):
        bp1 = SpectralElement(Box1D, amplitude=1, x_0=5000, width=10)
        bp2 = SpectralElement(Const1D, amplitude=2)
        bp = bp1 * bp2
        np.testing.assert_array_equal(bp.waveset, bp1.waveset)

    def test_composite(self):
        x0 = 5000
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM)
        g1 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=10)

        x0 = 6500
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM)
        g2 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=100)

        x0 = 7500
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM)
        g3 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=5)

        sp = (SpectralElement(Box1D, amplitude=1, x_0=1000, width=1) *
              (g1 + g2 + g3))
        np.testing.assert_allclose(
            sp.waveset.value[::100],
            [999.49, 1000.49, 5018.26041871, 6635.89148805, 7504.45893945])

    def test_redshift(self):
        x0 = 5000
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM)
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=10)
        sp.z = 1.3
        m = RedshiftScaleFactor(z=1.3)
        w_step25_z0 = [4976.64365049, 4987.260173, 4997.8766955, 5008.493218,
                       5019.10974051]
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
        totflux = units.convert_flux(x0, 1 * u.Jy, units.PHOTLAM)
        fwhm = 100
        self.sp_z0 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=fwhm)
        self.sp = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=x0, fwhm=fwhm)
        self.sp.z = 1.3

    def test_property(self):
        with pytest.raises(exceptions.SynphotError):
            self.sp.z = 1 * u.AA

        assert self.sp_z0.z == 0
        assert self.sp.z == 1.3

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


@pytest.mark.skipif('not HAS_SCIPY')
class TestMathOperators(object):
    """Test spectrum math operators."""
    def setup_class(self):
        self.sp_1 = SourceSpectrum(
            Empirical1D, x=[3999.9, 4000.0, 5000.0, 6000.0, 6000.1],
            y=[0, 3.5e-14, 4e-14, 4.5e-14, 0] * units.FLAM)
        self.sp_2 = SourceSpectrum(
            Empirical1D, x=_wave, y=_flux_jy,
            fill_value='extrapolate', kind='nearest',
            meta={'PHOTLAM': [9.7654e-3, 1.003896e-2, 9.78473e-3]})
        self.bp_1 = SpectralElement(
            Empirical1D, x=[399.99, 400.01, 500.0, 590.0, 600.1] * u.nm,
            y=[0, 0.1, 0.2, 0.3, 0])

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
            ans = self.sp_1 + self.bp_1

    @pytest.mark.parametrize('x', [2, 2 * u.dimensionless_unscaled])
    def test_source_mul_scalar(self, x):
        w = self.sp_1.waveset.value
        ans1 = self.sp_1 * x
        np.testing.assert_allclose(
            ans1(w).value, [0, 0.01409552, 0.02013646, 0.02718424, 0],
            rtol=1e-6)

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.sp_1
            np.testing.assert_array_equal(ans1(w), ans2(w))

    def test_source_mul_spec(self):
        """Compare with ASTROLIB PYSYNPHOT. Also test bp * sp."""
        ans1 = self.sp_1 * self.bp_1
        ans2 = self.bp_1 * self.sp_1
        w = ans1.waveset
        np.testing.assert_allclose(
            ans1(w).value,
            [0, 3.52381254e-04, 7.04792712e-04, 2.01360717e-03, 3.97184014e-03,
             4.03718269e-05, 0, 0], rtol=1e-4)
        np.testing.assert_array_equal(ans1(w), ans2(w))

    def test_source_mul_exceptions(self):
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.sp_1 * self.sp_2
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.sp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.sp_1 * (1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.sp_1 * (1 * u.AA)

    def test_source_div(self):
        """Put real tests here when ``__truediv__`` is implemented."""
        with pytest.raises(NotImplementedError):
            ans = self.sp_1 / 2.0
        with pytest.raises(NotImplementedError):
            ans = self.sp_1 / self.bp_1

    def test_bandpass_addsub(self):
        """Not supported."""
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 + self.bp_1
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 + 2.0
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 - self.bp_1
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 - 2.0

    @pytest.mark.parametrize('x', [2.0, 2.0 * u.dimensionless_unscaled])
    def test_bandpass_mul_scalar(self, x):
        w = self.bp_1.waveset.value
        ans1 = self.bp_1 * x
        np.testing.assert_allclose(ans1(w).value, [0, 0.2, 0.4, 0.6, 0])

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.bp_1
            np.testing.assert_array_equal(ans1(w), ans2(w))

    def test_bandpass_mul_bandpass(self):
        ans = self.bp_1 * self.bp_1
        np.testing.assert_allclose(
            ans(ans.waveset).value, [0, 0.01, 0.04, 0.09, 0])

    def test_bandpass_mul_exceptions(self):
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.bp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.bp_1 * (1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            ans = self.bp_1 * (1 * u.AA)

    def test_bandpass_div(self):
        """Put real tests here when ``__truediv__`` is implemented."""
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 / 2.0
        with pytest.raises(NotImplementedError):
            ans = self.bp_1 / self.bp_1


@pytest.mark.skipif('not HAS_SCIPY')
class TestWriteSpec(object):
    """Test spectrum to_fits() method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.sp = SourceSpectrum(Empirical1D, x=_wave, y=_flux_photlam,
                                 meta={'expr': 'Test source'})
        self.bp = SpectralElement(Empirical1D, x=_wave, y=np.ones(_wave.shape),
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
            sp1.to_fits(outfile, clobber=True, trim_zero=False,
                        pad_zero_ends=False)
        else:
            sp1.to_fits(outfile, clobber=True, trim_zero=False,
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
