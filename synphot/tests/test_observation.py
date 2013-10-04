# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test observation.py module."""
from __future__ import division, print_function

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.io import fits
from astropy.tests.helper import pytest, remote_data
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import spectrum, synexceptions, units
from ..observation import Observation


__doctest_skip__ = ['*']

# HST primary mirror
_area = u.Quantity(45238.93416, units.AREA)

# Test data files
_bandfile = get_pkg_data_filename(
    os.path.join('data', 'hst_acs_hrc_f555w.fits'))
_specfile = get_pkg_data_filename(
    os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'))


class TestObservation(object):
    """Test Observation (most of them)."""
    def setup_class(self):
        self.flat_sp = spectrum.SourceSpectrum.from_flat_spectrum(units.FLAM)
        self.bp = spectrum.SpectralElement.from_file(_bandfile)
        self.binwave = np.arange(1000, 11001, dtype=np.float64)
        self.obs = Observation.from_spec_band(
            self.flat_sp, self.bp, binwave=self.binwave, area=_area)

    def test_instance(self):
        assert isinstance(self.obs, Observation)
        assert isinstance(self.obs, spectrum.SourceSpectrum)

    def test_binned_data(self):
        # Binned flux
        np.testing.assert_array_equal(self.obs.binflux.value[:10], 0)
        np.testing.assert_allclose(
            self.obs.binflux.value[5000:5010],
            [0.12265425, 0.12226972, 0.12184207, 0.12141429, 0.12098646,
             0.1205586, 0.1201307, 0.11970269, 0.11927488, 0.11884699],
            rtol=1e-4)
        np.testing.assert_array_equal(self.obs.binflux.value[-10:], 0)
        assert self.obs.binflux.unit == self.obs.flux.unit

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
        assert self.obs.bin_edges.unit == self.obs.wave.unit
        assert self.obs.bin_edges.unit == self.obs.binwave.unit

    def test_binspec_reversed_binwave(self):
        obs = Observation.from_spec_band(
            self.flat_sp, self.bp, binwave=self.binwave[::-1], area=_area)
        np.testing.assert_array_equal(
            obs.binflux.value, self.obs.binflux.value)
        np.testing.assert_array_equal(
            obs.binwave.value, self.obs.binwave.value)
        np.testing.assert_array_equal(
            obs.bin_edges.value, self.obs.bin_edges.value)
        assert obs.binflux.unit == self.obs.binflux.unit
        assert obs.bin_edges.unit == obs.binwave.unit == self.obs.binwave.unit

    @pytest.mark.parametrize(('binned'), [True, False])
    def test_set_data(self, binned):
        self.obs._set_data(binned)

        if binned:
            ans_wave = self.obs.binwave
            ans_flux = self.obs.binflux
        else:
            ans_wave = self.obs.wave
            ans_flux = self.obs.flux

        np.testing.assert_array_equal(self.obs._wave.value, ans_wave.value)
        np.testing.assert_array_equal(self.obs._flux.value, ans_flux.value)
        assert self.obs._wave.unit == ans_wave.unit
        assert self.obs._flux.unit == ans_flux.unit

    def test_redshift(self):
        """This method is disabled."""
        with pytest.raises(NotImplementedError):
            new_obs = self.obs.apply_redshift(0.5)

    def test_convert_flux(self):
        old_flux = self.obs.flux.copy()
        old_binflux = self.obs.binflux.copy()

        self.obs.convert_flux(units.PHOTNU)
        np.testing.assert_allclose(
            self.obs.flux.value[9000], 0.4387680117539201)
        np.testing.assert_allclose(
            self.obs.binflux.value[4000], 0.4870874388526275)
        np.testing.assert_array_equal(self.obs._flux.value, self.obs.flux.value)
        assert self.obs.flux.unit == self.obs.binflux.unit == units.PHOTNU

        # Convert back to original unit
        self.obs.convert_flux(old_flux.unit)
        np.testing.assert_allclose(self.obs.flux.value, old_flux.value)
        np.testing.assert_allclose(self.obs.binflux.value, old_binflux.value)

    def test_sampled_binned(self):
        flux = self.obs.sample_binned([6000, 6004, 6009])
        np.testing.assert_allclose(
            flux.value, [0.12265425, 0.12098646, 0.11884699], rtol=1e-4)
        assert flux.unit == self.obs.binflux.unit

        with pytest.raises(synexceptions.InterpolationNotAllowed):
            flux = self.obs.sample_binned([6000, 6004.5, 6009])

        with pytest.raises(synexceptions.UnsortedWavelength):
            flux = self.obs.sample_binned([6004, 6000, 6009])

    @pytest.mark.parametrize(
        ('cenwave', 'ans_w1', 'ans_w2'),
        [(u.Quantity(500, u.nm),
          u.Quantity(499.9, u.nm), u.Quantity(500.1, u.nm)),
         (5000, u.Quantity(4999, u.AA), u.Quantity(5001, u.AA))])
    def test_wave_range(self, cenwave, ans_w1, ans_w2):
        w1, w2 = self.obs.wave_range(cenwave, 2, mode='none')
        np.testing.assert_allclose(w1.value, ans_w1.value)
        np.testing.assert_allclose(w2.value, ans_w2.value)
        assert w1.unit == ans_w1.unit
        assert w2.unit == ans_w2.unit

    def test_pixel_range(self):
        npix = self.obs.pixel_range(
            [u.Quantity(499.95, u.nm), u.Quantity(500.05, u.nm)], mode='round')
        assert npix == 1

    def test_from_spec_band_default_binwave(self):
        obs = Observation.from_spec_band(self.flat_sp, self.bp)
        np.testing.assert_array_equal(
            obs.binwave.value, self.flat_sp.wave.value)
        assert obs.binwave.unit == self.flat_sp.wave.unit

    def test_from_spec_band_exceptions(self):
        # Invalid inputs
        with pytest.raises(synexceptions.SynphotError):
            obs = Observation.from_spec_band(self.bp, self.bp)
        with pytest.raises(synexceptions.SynphotError):
            obs = Observation.from_spec_band(self.flat_sp, self.flat_sp)

        # Disjoint passband
        with pytest.raises(synexceptions.DisjointError):
            obs = Observation.from_spec_band(
                spectrum.SourceSpectrum.from_gaussian(1, 40000, 1), self.bp)


class TestMathOperators(object):
    """Test Observation math operators."""
    def setup_class(self):
        sp = spectrum.SourceSpectrum.from_flat_spectrum(units.FLAM)
        bp = spectrum.SpectralElement.from_box(5000, 100)
        binwave = np.arange(1000, 10000)
        self.obs = Observation.from_spec_band(sp, bp, binwave=binwave)

        # Trim off zero throughput to avoid nan at div test
        self.other_bp = spectrum.SpectralElement.from_box(
            5000, 1000).trim_spectrum(4500, 5500) * 2

    def _get_other(self, is_scalar):
        if is_scalar:
            other = 2
        else:
            other = self.other_bp
        return other

    @pytest.mark.parametrize(
        ('op_type', 'is_scalar'),
        [('*', True),
         ('*', False),
         ('/', True),
         ('/', False)])
    def test_mul_div(self, op_type, is_scalar):
        """This is extensively tested in test_spectrum.py.
        Only simple test here for sanity check.

        """
        other = self._get_other(is_scalar)

        if op_type == '*':
            new_obs = self.obs * other
            ans = 2
        elif op_type == '/':
            new_obs = self.obs / other
            ans = 0.5

        # Native dataset
        assert new_obs.resample(5000).value == ans
        assert new_obs.resample(1000).value == 0

        # Binned dataset
        assert new_obs.binflux.value[4000] == ans
        assert new_obs.binflux.value[0] == 0

    @pytest.mark.parametrize(('is_scalar'), [True, False])
    def test_exceptions(self, is_scalar):
        """These operators are disabled."""
        other = self._get_other(is_scalar)

        with pytest.raises(NotImplementedError):
            new_obs = self.obs + other
        with pytest.raises(NotImplementedError):
            new_obs = self.obs - other


class TestObsPar(object):
    """Test Observation values from IRAF SYNPHOT CALCPHOT.

    .. note:: ``binned=True`` not tested.

    """
    def setup_class(self):
        self.obs = Observation.from_file(_specfile, area=_area)
        self.bp = spectrum.SpectralElement.from_file(_bandfile, area=_area)

    def test_avglam(self):
        """Tested for FLAM only."""
        avglam = self.obs.avgwave()
        np.testing.assert_allclose(avglam.value, 5298.11, rtol=1e-5)
        assert avglam.unit == u.AA

    def test_barlam(self):
        """Tested for FLAM only."""
        bar_lam = self.obs.barlam()
        np.testing.assert_allclose(bar_lam.value, 5264.181, rtol=1e-5)
        assert bar_lam.unit == u.AA

    @pytest.mark.parametrize(
        ('mode', 'ans'),
        [('efflerg', 5321.148),
         ('efflphot', 5344.384)])
    def test_efflam(self, mode, ans):
        eff_lam = self.obs.effective_wavelength(mode=mode)
        np.testing.assert_allclose(eff_lam.value, ans, rtol=1e-5)
        assert eff_lam.unit == u.AA

    def test_efflam_exceptions(self):
        with pytest.raises(synexceptions.SynphotError):
            eff_lam = self.obs.effective_wavelength(mode='foo')

    @pytest.mark.parametrize(
        ('flux_unit', 'ans'),
        [(None, 3.07e-14),
         (units.STMAG, 12.68222),
         (units.FNU, 2.94e-25),
         (units.ABMAG, 12.73013),
         (units.PHOTLAM, 8.295e-3),
         (units.PHOTNU, 7.87e-14),
         (u.count, 1.020766e+5),
         (units.OBMAG, -12.5223),
         (u.Jy, 2.9373e-2),
         (u.mJy, 29.37296)])
    def test_effstim(self, flux_unit, ans):
        """Test EFFSTIM for all supported flux units except VEGAMAG.

        .. note:: ``wave_range`` only tested in `TestCountRateBinned`.

        """
        eff_stim = self.obs.effstim(flux_unit=flux_unit, band=self.bp)
        np.testing.assert_allclose(eff_stim.value, ans, rtol=0.01)  # 1%

        if flux_unit is None:
            assert eff_stim.unit == units.FLAM
        else:
            assert eff_stim.unit == flux_unit

    @remote_data
    def test_effstim_vegamag(self):
        vspec = spectrum.SourceSpectrum.from_vega(
            cache=False, show_progress=False, area=_area, encoding='binary')
        eff_stim = self.obs.effstim(
            flux_unit=units.VEGAMAG, band=self.bp, vegaspec=vspec)
        np.testing.assert_allclose(eff_stim.value, 12.74005, rtol=1e-4)
        assert eff_stim.unit == units.VEGAMAG

    def test_effstim_exceptions(self):
        # Invalid flux unit
        with pytest.raises(synexceptions.SynphotError):
            eff_stim = self.obs.effstim(flux_unit=u.mag, band=self.bp)

        # Missing passband
        with pytest.raises(synexceptions.SynphotError):
            eff_stim = self.obs.effstim()

        # Disjoint passband
        with pytest.raises(synexceptions.DisjointError):
            eff_stim = self.obs.effstim(
                band=spectrum.SpectralElement.from_box(2000, 1))

        # Partial overlap passband
        with pytest.raises(synexceptions.OverlapError):
            eff_stim = self.obs.effstim(
                band=spectrum.SpectralElement.from_box(3500, 500))

        # Missing Vega spectrum
        with pytest.raises(synexceptions.SynphotError):
            eff_stim = self.obs.effstim(flux_unit=units.VEGAMAG, band=self.bp)


class TestCountRate(object):
    """Test countrate with Observation with well-defined ranges.

    .. note:: Use binned data except for :func:`test_waverange_no_bin`.

    """
    def setup_class(self):
        wave = np.arange(1000, 1100, 0.5)
        flux_flam = spectrum.convert_fluxes(
            wave, u.Quantity(wave - 1000, u.count), units.FLAM, area=_area)
        sp = spectrum.SourceSpectrum(
            wave, flux_flam, area=_area, header={'expr': 'slope1'})
        bp = spectrum.SpectralElement(
            [1000, 1009.95, 1010, 1030, 1030.05, 1100], [0, 0, 1, 1, 0, 0],
            area=_area, header={'expr': 'handmade_box'})
        self.obs = Observation.from_spec_band(
            sp, bp, binwave=np.arange(1000, 1020))

    def test_no_waverange(self):
        """Use all bins."""
        ct_rate = self.obs.countrate()
        np.testing.assert_allclose(ct_rate.value, 280.75, rtol=1e-4)
        assert ct_rate.unit == u.count

    @pytest.mark.parametrize(
        ('w1', 'w2', 'ans'),
        [(1000, 1019, 280.75),
         (1013, 1016, 116),
         (1012.8, 1016, 116),
         (1013.2, 1016, 116)])
    def test_waverange(self, w1, w2, ans):
        """Use given wavelength range."""
        ct_rate = self.obs.countrate(wave_range=[w1, w2])
        np.testing.assert_allclose(ct_rate.value, ans, rtol=1e-4)

    def test_waverange_no_bin(self):
        """Use given wavelength range on native dataset.

        .. note:: Accuracy unsure as there was no precedent to test against.

        """
        ct_rate = self.obs.countrate(wave_range=[1000, 1019], binned=False)
        np.testing.assert_allclose(ct_rate.value, 271, rtol=1e-4)

    @pytest.mark.parametrize(
        ('w1', 'w2', 'ans'),
        [(1016, 1026, 140),
         (999, 1016, 172.75)])
    def test_force(self, w1, w2, ans):
        """Force calculation for partial overlap."""
        ct_rate = self.obs.countrate(wave_range=[w1, w2], force=True)
        np.testing.assert_allclose(ct_rate.value, ans, rtol=1e-4)

        # Must raise error without force
        with pytest.raises(synexceptions.OverlapError):
            ct_rate = self.obs.countrate(wave_range=[w1, w2])

    def test_waverange_exceptions(self):
        # Invalid wavelength range
        with pytest.raises(synexceptions.SynphotError):
            ct_rate = self.obs.countrate(wave_range=[1016, 1013.2])

        # Disjoint wavelength range
        with pytest.raises(synexceptions.DisjointError):
            ct_rate = self.obs.countrate(wave_range=[1020, 1030])


class TestFromSpecBandForce(object):
    """Test from_spec_band() method with force."""
    def setup_class(self):
        self.sp = spectrum.SourceSpectrum(
            np.arange(3000, 4000, dtype=np.float64), np.ones(1000) * 0.75,
            header={'expr': 'short flat'})
        self.bp = spectrum.SpectralElement.from_box(4000, 100)
        self.refwave = u.Quantity(4005, u.AA)

    def test_exceptions(self):
        with pytest.raises(synexceptions.OverlapError):
            obs = Observation.from_spec_band(self.sp, self.bp)
        with pytest.raises(synexceptions.SynphotError):
            obs = Observation.from_spec_band(self.sp, self.bp, force='foo')

    @pytest.mark.parametrize(
        ('force_type', 'ans'),
        [('taper', 0),
         ('extrap', 0.75)])
    def test_taper(self, force_type, ans):
        obs = Observation.from_spec_band(self.sp, self.bp, force=force_type)
        flux = obs.resample(self.refwave)
        assert flux.value == ans
        assert flux.unit == units.FLAM
        assert force_type in obs.warnings['PartialOverlap']


class TestReadWriteObs(object):
    """Test from_file() and to_fits() methods (no binned data)."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.obs = Observation.from_file(_specfile)

    def test_no_bins(self):
        """Reading from file does not set binned data."""
        assert self.obs.binwave is None
        assert self.obs.binflux is None
        assert self.obs.bin_edges is None

        with pytest.raises(synexceptions.UndefinedBinset):
            self.obs._set_data(True)

    @pytest.mark.parametrize(('ext_hdr'), [None, {'foo': 'foo'}])
    def test_write(self, ext_hdr):
        outfile = os.path.join(self.outdir, 'outobs.fits')

        if ext_hdr is None:
            self.obs.to_fits(
                outfile, clobber=True, binned=False, trim_zero=False,
                pad_zero_ends=False)
        else:
            self.obs.to_fits(
                outfile, clobber=True, binned=False, trim_zero=False,
                pad_zero_ends=False, ext_header=ext_hdr)

        # Read it back in and check
        obs = Observation.from_file(outfile)

        np.testing.assert_allclose(obs.wave.value, self.obs.wave.value)
        np.testing.assert_allclose(obs.flux.value, self.obs.flux.value)
        assert obs.wave.unit == self.obs.wave.unit
        assert obs.flux.unit == self.obs.flux.unit

        hdr = fits.getheader(outfile, 1)
        assert 'expr' in hdr
        assert 'binned' in hdr
        if ext_hdr is not None:
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
