# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and related functionalities for bandpass."""

# STDLIB
import os

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u
from astropy.modeling.models import Const1D
from astropy.tests.helper import assert_quantity_allclose
from astropy.utils.data import get_pkg_data_filename
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from synphot.tests.test_units import _area, _wave, _flux_photlam
from synphot import exceptions, units
from synphot.compat import HAS_SPECUTILS  # noqa
from synphot.models import Box1D, Empirical1D, GaussianAbsorption1D
from synphot.spectrum import SpectralElement


@pytest.mark.remote_data
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


class TestEmpiricalBandpassFromFile:
    """This is the most common model used in ASTROLIB PYSYNPHOT."""
    def setup_class(self):
        bandfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w.fits'),
            package='synphot.tests')
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
        assert_quantity_allclose(f, 272.01081629459344 * u.AA)

        # Given range
        f = self.bp.integrate(wavelengths=_wave)
        assert_quantity_allclose(f, 1.2062975715374322 * u.AA, rtol=2.5e-6)

    def test_avgwave(self):
        """Compare AVGWAVE with old SYNPHOT result."""
        w = self.bp.avgwave()
        assert_quantity_allclose(w, 5367.9 * u.AA, rtol=1e-5)

    def test_barlam(self):
        """Test BARLAM (no old SYNPHOT result available)."""
        w = self.bp.barlam()
        assert_quantity_allclose(w, 5331.8945 * u.AA, rtol=1e-5)

    def test_pivot(self):
        """Compare PIVWV with ASTROLIB PYSYNPHOT result."""
        w = self.bp.pivot()
        assert_quantity_allclose(w, 5355.863596422962 * u.AA, rtol=1e-6)

    def test_uresp(self):
        """Compare URESP with old SYNPHOT result."""
        uresp = self.bp.unit_response(area=_area)
        assert_quantity_allclose(uresp, 3.00737e-19 * units.FLAM, rtol=1e-4)

    def test_rmswidth(self):
        w = self.bp.rmswidth()
        assert_quantity_allclose(w, 359.55954282883687 * u.AA, rtol=1e-4)

        w = self.bp.rmswidth(threshold=0.01 * u.dimensionless_unscaled)
        assert_quantity_allclose(w, 357.43298216917754 * u.AA, rtol=1e-4)

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            self.bp.rmswidth(threshold=0.01 * u.AA)
        with pytest.raises(exceptions.SynphotError):
            self.bp.rmswidth(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            self.bp.rmswidth(threshold='foo')

    def test_fwhm(self):
        """This also calls PHOTBW."""
        w = self.bp.fwhm()
        assert_quantity_allclose(w, 841.09 * u.AA, rtol=2.5e-5)

        w = self.bp.fwhm(threshold=0.01 * u.dimensionless_unscaled)
        assert_quantity_allclose(w, 836.2879507505378 * u.AA, rtol=2.5e-5)

        # Zero value
        w = self.bp.fwhm(wavelengths=[2e6, 2.1e6])
        assert w.value == 0

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            self.bp.fwhm(threshold=0.01 * u.AA)
        with pytest.raises(exceptions.SynphotError):
            self.bp.fwhm(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            self.bp.fwhm(threshold='foo')

    def test_tlambda(self):
        f = self.bp.tlambda()
        assert_quantity_allclose(f, 0.22808, rtol=1e-4)

    def test_tpeak(self):
        """Compare TPEAK with old SYNPHOT result."""
        f = self.bp.tpeak()
        assert_quantity_allclose(f, 0.241445)

    def test_wpeak(self):
        w = self.bp.wpeak()
        assert_quantity_allclose(w, 5059.8 * u.AA, rtol=1e-5)

    def test_equivwidth(self):
        """Compare EQUVW with ASTROLIB PYSYNPHOT result."""
        w = self.bp.equivwidth()
        assert_quantity_allclose(w, 272.01081629459344 * u.AA, rtol=1e-6)

    def test_rectw(self):
        """Compare RECTW with old SYNPHOT result."""
        w = self.bp.rectwidth()
        assert_quantity_allclose(w, 1126.588 * u.AA, rtol=1e-5)

    def test_qtlam(self):
        qtlam = self.bp.efficiency()
        assert_quantity_allclose(qtlam, 0.050901, rtol=1e-4)

    def test_emflx(self):
        """Compare EMFLX with old SYNPHOT result."""
        f = self.bp.emflx(area=_area)
        assert_quantity_allclose(f, 3.586622e-16 * units.FLAM, rtol=2.5e-5)


class TestBoxBandpass:
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
        assert_quantity_allclose(self.bp.fwhm(), 67.977 * u.AA,
                                 rtol=1e-3)  # 0.1%

    def test_taper(self):
        bp2 = self.bp.taper(np.arange(499, 501.01, 0.01) * u.nm)
        y = bp2([498.9, 499, 500, 501, 501.1] * u.nm)
        assert_quantity_allclose(y, [0, 1, 1, 1, 0])

    def test_integrate(self):
        ans = 100 * u.AA
        assert_quantity_allclose(self.bp.integrate(), ans)
        assert_quantity_allclose(
            self.bp.integrate(integration_type='analytical'), ans)

        with pytest.raises(exceptions.SynphotError,
                           match='flux_unit cannot be used'):
            self.bp.integrate(integration_type='analytical', flux_unit='flam')

    def test_multi_n_models(self):
        """This is not allowed."""
        with pytest.raises(exceptions.SynphotError):
            SpectralElement(
                Box1D, amplitude=[1, 1], x_0=[5000, 6000],
                width=[100, 1], n_models=2)


class TestBuildModelsBandpass:
    """Test compatiblity with other models not tested above."""
    def test_GaussianAbsorption1D(self):
        """This should be unitless, not a source spectrum."""
        bp = SpectralElement(
            GaussianAbsorption1D, amplitude=0.8, mean=5500, stddev=50)
        y = bp([5300, 5500, 5700])
        assert_quantity_allclose(y, [0.99973163, 0.2, 0.99973163])


@pytest.mark.skipif('not HAS_SPECUTILS')
class TestSpecutilsBridgeBandpass:
    def test_from_spectrum1d_Empirical1D_bandpass(self):
        import specutils

        lamb = [1000, 5000, 10000] * u.AA
        thru = [0, 1, -1] * units.THROUGHPUT
        spec = specutils.Spectrum1D(spectral_axis=lamb, flux=thru)
        with pytest.warns(AstropyUserWarning,
                          match=r'contained negative flux or throughput'):
            bp = SpectralElement.from_spectrum1d(spec, keep_neg=False)

        w = bp.waveset
        assert isinstance(bp.model, Empirical1D)
        assert_quantity_allclose(w, lamb)
        assert_quantity_allclose(bp(w), [0, 1, 0])

    def test_from_spectrum1d_Empirical1D_bandpass_masked(self):
        import specutils

        lamb = [1000, 5000, 10000] * u.AA
        thru = [0, 1, -1] * units.THROUGHPUT
        mask = np.array([False, False, True])
        spec = specutils.Spectrum1D(spectral_axis=lamb, flux=thru, mask=mask)
        bp = SpectralElement.from_spectrum1d(spec, keep_neg=False)

        w = bp.waveset
        assert isinstance(bp.model, Empirical1D)
        assert_quantity_allclose(w, [1000, 5000] * u.AA)
        assert_quantity_allclose(bp(w), [0, 1])

    def test_to_spectrum1d_Empirical1D_bandpass(self):
        lamb = [1000, 5000, 10000] * u.AA
        thru = [0, 1, 0]
        bp = SpectralElement(Empirical1D, points=lamb, lookup_table=thru)
        spec = bp.to_spectrum1d()

        assert_quantity_allclose(spec.spectral_axis, lamb)
        assert_quantity_allclose(spec.flux, thru)

    def test_to_spectrum1d_Const1D(self):
        thru = 0.88
        bp = SpectralElement(Const1D, amplitude=thru)

        with pytest.raises(exceptions.SynphotError) as e:
            spec = bp.to_spectrum1d()
        assert 'Provide wavelengths for sampling' in str(e.value)

        w = [100, 500, 1000] * u.nm
        spec = bp.to_spectrum1d(wavelengths=w)

        assert_quantity_allclose(spec.spectral_axis, w)
        assert_quantity_allclose(spec.flux, thru)

    def test_to_spectrum1d_compound_bandpass(self):
        from specutils.analysis import line_flux

        box = SpectralElement(
            Box1D, amplitude=0.5, x_0=5000 * u.AA, width=1 * u.AA)
        bp = box * box
        spec = bp.to_spectrum1d()

        w = bp.waveset
        integrated_thru = bp.integrate()
        assert_quantity_allclose(spec.spectral_axis, w)
        assert_quantity_allclose(spec.flux, bp(w))
        assert_quantity_allclose(integrated_thru, 0.25 * u.AA)
        assert_quantity_allclose(integrated_thru, line_flux(spec))
