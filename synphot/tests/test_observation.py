# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test observation.py module."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os

# THIRD-PARTY
import numpy as np

try:
    import scipy  # pylint: disable=W0611
except ImportError:
    HAS_SCIPY = False
else:
    HAS_SCIPY = True

# ASTROPY
from astropy import units as u
from astropy.modeling.models import Const1D
from astropy.tests.helper import pytest, remote_data
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .test_units import _area
from .. import exceptions, units
from ..models import (BlackBodyNorm1D, Box1D, ConstFlux1D, Empirical1D,
                      GaussianFlux1D)
from ..observation import Observation
from ..spectrum import SourceSpectrum, SpectralElement

# Global test data files
_specfile = get_pkg_data_filename(
    os.path.join('data', 'grw_70d5824_stisnic_005.fits'))
_bandfile = get_pkg_data_filename(
    os.path.join('data', 'hst_acs_hrc_f555w.fits'))


@pytest.mark.skipif('not HAS_SCIPY')
class TestObservation(object):
    """Test Observation (most of them)."""
    def setup_class(self):
        sp = SourceSpectrum(
            ConstFlux1D, amplitude=u.Quantity(1, units.FLAM),
            meta={'warnings': {'w1': 'spec warn', 'w2': 'foo'}})
        bp = SpectralElement.from_file(_bandfile)
        bp.warnings = {'w1': 'band warn'}
        w = np.arange(1000, 11001, dtype=np.float64)
        self.obs = Observation(sp, bp, binset=w)

    def test_invalid_input_spec(self):
        with pytest.raises(exceptions.SynphotError):
            obs2 = Observation(self.obs.bandpass, self.obs.bandpass)
        with pytest.raises(exceptions.SynphotError):
            obs2 = Observation(self.obs.spectrum, self.obs.spectrum)

    def test_inherit_warnings(self):
        assert sorted(self.obs.warnings) == ['w1', 'w2']
        assert self.obs.warnings['w1'] == 'band warn'

    def test_disjoint_spec(self):
        """The rest of overlap logic is tested in `TestInitWithForce`."""
        sp = SourceSpectrum(
            Empirical1D, x=[39999.9, 40000, 40001, 40001.1], y=[0, 1, 1, 0])
        with pytest.raises(exceptions.DisjointError):
            obs2 = Observation(sp, self.obs.bandpass)

    def test_taper(self):
        with pytest.raises(NotImplementedError):
            obs2 = self.obs.taper()

    def test_binned_data(self):
        # Binned flux
        np.testing.assert_array_equal(self.obs.binflux[:10], 0)
        np.testing.assert_array_equal(self.obs.binflux[-10:], 0)
        np.testing.assert_allclose(
            self.obs.sample_binned(wavelengths=self.obs.binset[5000:5010],
                                   flux_unit=units.FLAM).value,
            [0.12265425, 0.12226972, 0.12184207, 0.12141429, 0.12098646,
             0.1205586, 0.1201307, 0.11970269, 0.11927488, 0.11884699],
            rtol=1e-4)

        # Binned wave and flux
        w, y = self.obs._get_binned_arrays(
            [599.9999999999, 600.4, 600.9] * u.nm, units.FLAM)
        np.testing.assert_allclose(w.value, [600, 600.4, 600.9])
        np.testing.assert_allclose(
            y.value, [0.12265425, 0.12098646, 0.11884699], rtol=1e-4)

        w, y = self.obs._get_binned_arrays(None, units.PHOTLAM)
        np.testing.assert_array_equal(w, self.obs.binset)
        np.testing.assert_array_equal(y, self.obs.binflux)

        # Bin edges
        np.testing.assert_array_equal(
            self.obs.bin_edges.value[:10],
            [999.5, 1000.5, 1001.5, 1002.5, 1003.5, 1004.5, 1005.5, 1006.5,
             1007.5, 1008.5])
        np.testing.assert_array_equal(
            self.obs.bin_edges.value[5000:5010],
            [5999.5, 6000.5, 6001.5, 6002.5, 6003.5, 6004.5, 6005.5, 6006.5,
             6007.5, 6008.5])
        np.testing.assert_array_equal(
            self.obs.bin_edges.value[-10:],
            [10991.5, 10992.5, 10993.5, 10994.5, 10995.5, 10996.5, 10997.5,
             10998.5, 10999.5, 11000.5])

    def test_reversed_binset(self):
        obs2 = Observation(
            self.obs.spectrum, self.obs.bandpass, binset=self.obs.binset[::-1])
        np.testing.assert_array_equal(obs2.binset, self.obs.binset)
        np.testing.assert_array_equal(obs2.binflux, self.obs.binflux)
        np.testing.assert_array_equal(obs2.bin_edges, self.obs.bin_edges)

    def test_sampled_binned_exceptions(self):
        with pytest.raises(exceptions.InterpolationNotAllowed):
            y = self.obs.sample_binned([6000, 6004.5, 6009])
        with pytest.raises(exceptions.UnsortedWavelength):
            y = self.obs.sample_binned([6004, 6000, 6009])

    @pytest.mark.parametrize(
        ('cenwave', 'ans'),
        [(500 * u.nm, [499.9, 500.1] * u.nm),
         (5000, [4999, 5001] * u.AA)])
    def test_binned_waverange(self, cenwave, ans):
        w = self.obs.binned_waverange(cenwave, 2, mode='none')
        np.testing.assert_allclose(w, ans)

    def test_binned_pixelrange(self):
        w = [499.95, 500.05] * u.nm
        assert self.obs.binned_pixelrange(w, mode='round') == 1

    def test_default_binset_from_bandpass(self):
        obs2 = Observation(self.obs.spectrum, self.obs.bandpass)
        np.testing.assert_array_equal(obs2.binset, self.obs.bandpass.waveset)

    def test_default_binset_from_spectrum(self):
        x0 = 5000  # Angstrom
        totflux = units.convert_flux(x0, 1 * units.FLAM, units.PHOTLAM).value

        sp = SourceSpectrum(GaussianFlux1D, mean=x0, total_flux=totflux,
                            fwhm=10)
        bp = SpectralElement(Const1D, amplitude=1)
        obs2 = Observation(sp, bp, force='extrap')
        np.testing.assert_array_equal(obs2.binset, sp.waveset)

    def test_undefined_binset(self):
        bp = SpectralElement(Const1D, amplitude=1)
        with pytest.raises(exceptions.UndefinedBinset):
            obs2 = Observation(self.obs.spectrum, bp)

    def test_as_spectrum(self):
        w = np.arange(6000, 6005)
        sp1 = self.obs.as_spectrum(binned=True, wavelengths=w)  # Binned
        sp2 = self.obs.as_spectrum(binned=False, wavelengths=w)  # Sampled
        np.testing.assert_allclose(
            sp1(sp1.waveset), sp2(sp2.waveset), rtol=1e-3)


@pytest.mark.skipif('not HAS_SCIPY')
class TestInitWithForce(object):
    """Test forced initialization."""
    def setup_class(self):
        x = np.arange(3000, 4000)
        y = np.ones_like(x) * 0.75
        self.sp = SourceSpectrum(
            Empirical1D, x=x, y=y, meta={'expr': 'short flat'})
        self.bp = SpectralElement(
            Empirical1D, x=[3949.9, 3950, 4050, 4050.1], y=[0, 1, 1, 0])

    @pytest.mark.parametrize(
        ('force_type', 'ans'),
        [('taper', 0),
         ('extrap', 0.75)])
    def test_force(self, force_type, ans):
        obs = Observation(self.sp, self.bp, force=force_type)
        assert obs(4005).value == ans
        assert force_type in obs.warnings['PartialOverlap']

    def test_exceptions(self):
        with pytest.raises(exceptions.PartialOverlap):
            obs = Observation(self.sp, self.bp)
        with pytest.raises(exceptions.SynphotError):
            obs = Observation(self.sp, self.bp, force='foo')


class TestMathOperators(object):
    """Test Observation math operators."""
    def setup_class(self):
        sp = SourceSpectrum(ConstFlux1D, amplitude=1)
        bp = SpectralElement(Box1D, amplitude=1, x_0=5000, width=100)
        w = np.arange(1000, 10000)
        self.obs = Observation(sp, bp, binset=w)

    @pytest.mark.parametrize('is_scalar', [True, False])
    def test_mul(self, is_scalar):
        if is_scalar:
            other = 2
        else:
            other = SpectralElement(Const1D, amplitude=2)

        obs2 = self.obs * other
        np.testing.assert_allclose(obs2([1000, 5000]).value, [0, 2])
        np.testing.assert_allclose(
            obs2.sample_binned([4000, 4999]).value, [0, 2])

    def test_div(self):
        with pytest.raises(NotImplementedError):
            obs2 = self.obs / 2

    def test_addsub(self):
        with pytest.raises(NotImplementedError):
            obs2 = self.obs + self.obs
        with pytest.raises(NotImplementedError):
            obs2 = self.obs - self.obs


@pytest.mark.skipif('not HAS_SCIPY')
class TestObsPar(object):
    """Test Observation values from IRAF SYNPHOT CALCPHOT,
    unless noted otherwise.

    """
    def setup_class(self):
        sp = SourceSpectrum.from_file(_specfile)
        bp = SpectralElement.from_file(_bandfile)
        self.obs = Observation(sp, bp)

    def test_avglam(self):
        """Tested for PHOTLAM only; no binning."""
        np.testing.assert_allclose(
            self.obs.avgwave().value, 5321.091, rtol=1e-5)

    def test_barlam(self):
        """Tested for PHOTLAM only; no binning."""
        np.testing.assert_allclose(self.obs.barlam().value, 5286.685, rtol=1e-5)

    def test_pivot(self):
        """Tested with value from ASTROLIB PYSYNPHOT; no binning."""
        np.testing.assert_allclose(self.obs.pivot().value, 5309.578, rtol=1e-5)

    def test_normalize(self):
        """Tested with value from ASTROLIB PYSYNPHOT; no binning."""
        obs2 = self.obs.normalize(1 * units.PHOTLAM, band=self.obs.bandpass)
        np.testing.assert_allclose(
            obs2.countrate(_area).value, 59517756.384, rtol=1e-5)

    @pytest.mark.parametrize(
        ('mode', 'ans'),
        [('efflerg', 5321.091),
         ('efflphot', 5344.312)])
    def test_efflam(self, mode, ans):
        np.testing.assert_allclose(
            self.obs.effective_wavelength(mode=mode, binned=False).value,
            ans, rtol=1e-4)
        np.testing.assert_allclose(
            self.obs.effective_wavelength(mode=mode, binned=True).value,
            ans, rtol=1e-4)

    def test_efflam_exception(self):
        with pytest.raises(exceptions.SynphotError):
            w = self.obs.effective_wavelength(mode='foo')

    @pytest.mark.parametrize(
        ('flux_unit', 'ans'),
        [(units.FLAM, 3.05E-14),
         (units.STMAG, 12.68878),
         (units.FNU, 2.92E-25),
         (units.ABMAG, 12.73669),
         (units.PHOTLAM, 0.008245),
         (units.PHOTNU, 7.82E-14),
         (u.count, 101462.5),
         (units.OBMAG, -12.5158),
         (u.Jy, 0.029196),
         (u.mJy, 29.19613)])
    def test_effstim(self, flux_unit, ans):
        """Test EFFSTIM for all supported flux units except VEGAMAG.

        .. note::

            ``binned``, ``waverange``, and ``force`` tested in `TestCountRate`.

        """
        np.testing.assert_allclose(
            self.obs.effstim(flux_unit=flux_unit, area=_area).value,
            ans, rtol=0.01)  # 1%

    def test_effstim_analytic(self):
        sp = SourceSpectrum(BlackBodyNorm1D, temperature=5000)
        bp = SpectralElement(Box1D, amplitude=1, x_0=5500, width=1)
        obs = Observation(sp, bp)
        np.testing.assert_allclose(
            obs.effstim(flux_unit=units.FLAM).value, 2.03E-15, rtol=0.01)  # 1%

    @remote_data
    def test_effstim_vegamag(self):
        vspec = SourceSpectrum.from_vega(encoding='binary')
        np.testing.assert_allclose(
            self.obs.effstim(flux_unit=units.VEGAMAG, vegaspec=vspec).value,
            12.74661, rtol=0.01)  # 1%

    def test_effstim_exceptions(self):
        with pytest.raises(exceptions.SynphotError):
            x = self.obs.effstim(flux_unit=u.mag)
        with pytest.raises(exceptions.SynphotError):
            x = self.obs.effstim(flux_unit=units.VEGAMAG)


@pytest.mark.skipif('not HAS_SCIPY')
class TestCountRate(object):
    """Test countrate with Observation with well-defined ranges.

    .. note:: Use binned data except for :func:`test_waverange_no_bin`.

    """
    def setup_class(self):
        x = np.arange(1000, 1100, 0.5)
        y = units.convert_flux(
            x, u.Quantity(x - 1000, u.count), units.PHOTLAM, area=_area).value
        sp = SourceSpectrum(Empirical1D, x=x, y=y, meta={'expr': 'slope1'})
        bp = SpectralElement(
            Empirical1D, x=[1009.95, 1010, 1030, 1030.05],
            y=[0, 1, 1, 0], meta={'expr': 'handmade_box'})
        self.obs = Observation(sp, bp, binset=np.arange(1000, 1020))

    @pytest.mark.parametrize(
        ('w', 'ans'),
        [(None, 280.75),
         ([1000, 1019], 280.75),
         ([1013, 1016], 116),
         ([1012.8, 1016], 116),
         ([1013.2, 1016], 116)])
    def test_waverange(self, w, ans):
        """Use given wavelength range on binned data."""
        np.testing.assert_allclose(
            self.obs.countrate(_area, waverange=w).value, ans)

    def test_waverange_no_bin(self):
        """Use given wavelength range on native dataset.

        .. note:: Accuracy unsure as there was no precedent to test against.

        """
        w = [1000, 1019]
        np.testing.assert_allclose(
            self.obs.countrate(_area, waverange=w, binned=False).value, 271)

    @pytest.mark.parametrize(
        ('w', 'ans'),
        [([1016, 1026], 140),
         ([999, 1016], 172.75)])
    def test_force(self, w, ans):
        """Force calculation for partial overlap."""
        np.testing.assert_allclose(
            self.obs.countrate(_area, waverange=w, force=True).value, ans)

        # Must raise error without force
        with pytest.raises(exceptions.PartialOverlap):
            x = self.obs.countrate(_area, waverange=w)

    def test_disjoint_waverange(self):
        with pytest.raises(exceptions.DisjointError):
            x = self.obs.countrate(_area, waverange=[1020, 1030])


@pytest.mark.skipif('not HAS_SCIPY')
class TestCountRateNegFlux(object):
    """Test countrate with files containing negative flux/throughput values."""
    def setup_class(self):
        self.bp = SpectralElement.from_file(get_pkg_data_filename(
            os.path.join('data', 'cos_fuv_g130m_c1309_psa.fits')))
        self.spfile = get_pkg_data_filename(os.path.join('data', 'us7.txt'))

    @pytest.mark.parametrize(
        ('keep_neg', 'ans'),
        [(True, 1510.219531414891),
         (False, 1627.8250215634343)])
    def test_neg_handling(self, keep_neg, ans):
        sp = SourceSpectrum.from_file(self.spfile, keep_neg=keep_neg)
        obs = Observation(sp, self.bp)
        c = obs.countrate(_area)
        np.testing.assert_allclose(c.value, ans, rtol=1e-4)

        if not keep_neg:
            assert 'NegativeFlux' in obs.warnings
