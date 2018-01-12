# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test binning.py module."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os
import warnings

# THIRD PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u
from astropy.utils.data import get_pkg_data_filename
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from .. import binning, exceptions, specio
from ..utils import merge_wavelengths, generate_wavelengths


@pytest.mark.parametrize(
    ('in_arr', 'out_arr'),
    [(np.arange(10, 20, dtype=np.float), np.arange(9.5, 20)),
     (2 ** np.arange(1, 10), [1, 3, 6, 12, 24, 48, 96, 192, 384, 640])])
def test_calculate_bin_edges(in_arr, out_arr):
    """Test bin edge calculations for even and uneven bins."""
    edges = binning.calculate_bin_edges(in_arr)
    np.testing.assert_array_equal(edges.value, out_arr)
    assert edges.unit == u.AA


@pytest.mark.parametrize(
    ('in_arr', 'out_arr'),
    [([1, 2, 4, 10, 20], [1, 2, 6, 10]),
     ([1, 2], [1])])
def test_calculate_bin_widths(in_arr, out_arr):
    """Test bin width calculations for multiple and single bins."""
    widths = binning.calculate_bin_widths(in_arr)
    np.testing.assert_array_equal(widths.value, out_arr)
    assert widths.unit == u.AA


@pytest.mark.parametrize(
    ('in_arr', 'out_arr'),
    [([1, 2, 4, 10, 20], [1.5, 2.5, 5.5, 14.5]),
     ([1, 2], [1.5])])
def test_calculate_bin_centers(in_arr, out_arr):
    """Test bin center calculations."""
    centers = binning.calculate_bin_centers(in_arr)
    np.testing.assert_array_equal(centers.value, out_arr)
    assert centers.unit == u.AA


def test_center_edge_center_roundtrip():
    """Test that we get back the same centers."""
    centers = [1, 2, 4, 10, 20] * u.micron
    calc_centers = binning.calculate_bin_centers(
        binning.calculate_bin_edges(centers))
    np.testing.assert_array_equal(calc_centers.value, centers.value)
    assert calc_centers.unit == centers.unit


@pytest.mark.parametrize(
    ('arr'), [1 * u.AA, np.array([1]) * u.AA])
def test_calculate_bin_exceptions(arr):
    """Test binning.py raising appropriate exceptions."""
    with pytest.raises(exceptions.SynphotError):
        binning.calculate_bin_edges(arr)
    with pytest.raises(exceptions.SynphotError):
        binning.calculate_bin_widths(arr)
    with pytest.raises(exceptions.SynphotError):
        binning.calculate_bin_centers(arr)


class TestBinRange(object):
    """Test wavelength and pixel range calculations."""
    def setup_class(self):
        self.bins = generate_wavelengths(
            minwave=1003, maxwave=11001, delta=1.0, log=False)[0].value

    def test_wave_range_exceptions(self):
        """Test for appropriate wavelength range exceptions."""
        with pytest.raises(exceptions.SynphotError):
            binning.wave_range(self.bins, 5000, 100, mode='up')
        with pytest.raises(exceptions.SynphotError):
            binning.wave_range(self.bins, 5000, 1.3)
        with pytest.raises(exceptions.OverlapError):
            binning.wave_range(self.bins, 1010, 100)
        with pytest.raises(exceptions.OverlapError):
            binning.wave_range(self.bins, 11000, 1000)
        with pytest.raises(exceptions.OverlapError):
            binning.wave_range(self.bins, 600, 1000)

    def test_wave_range_mode_none(self):
        """Test wavelength range calculations for mode='none'."""
        w1, w2 = binning.wave_range(self.bins, 5000.4, 0, mode='none')
        assert w1 == w2
        w = binning.wave_range(self.bins, 5000, 2, mode='none')
        assert w == (4999, 5001)
        w = binning.wave_range(self.bins, 5000.25, 3, mode='none')
        assert w == (4998.75, 5001.75)
        w = binning.wave_range(self.bins, 5000.5, 4, mode='none')
        assert w == (4998.5, 5002.5)

    @pytest.mark.parametrize(
        ('cenwave', 'npix', 'ans', 'mode'),
        [(5002, 1, (5001.5, 5002.5), 'round'),
         (5005, 2, (5004.5, 5006.5), 'round'),
         (5005, 3, (5003.5, 5006.5), 'round'),
         (5004.25, 4, (5002.5, 5006.5), 'round'),
         (5004.25, 5, (5001.5, 5006.5), 'round'),
         (5004.5, 6, (5001.5, 5007.5), 'round'),
         (5004.5, 7, (5001.5, 5008.5), 'round'),
         (5004, 1, (5003.5, 5004.5), 'min'),
         (5004, 2, (5003.5, 5004.5), 'min'),
         (5004, 3, (5002.5, 5005.5), 'min'),
         (5006.25, 4, (5004.5, 5007.5), 'min'),
         (5006.25, 5, (5004.5, 5008.5), 'min'),
         (5006.5, 6, (5003.5, 5009.5), 'min'),
         (5006.5, 7, (5003.5, 5009.5), 'min'),
         (5004, 1, (5003.5, 5004.5), 'max'),
         (5004, 2, (5002.5, 5005.5), 'max'),
         (5004, 3, (5002.5, 5005.5), 'max'),
         (5006.25, 4, (5003.5, 5008.5), 'max'),
         (5006.25, 5, (5003.5, 5009.5), 'max'),
         (5006.5, 6, (5003.5, 5009.5), 'max'),
         (5006.5, 7, (5002.5, 5010.5), 'max')])
    def test_wave_range_mode(self, cenwave, npix, ans, mode):
        """Test wavelength range calculations for all modes."""
        w = binning.wave_range(self.bins, cenwave, npix, mode=mode)
        assert w == ans

    def test_wave_range_descending_order(self):
        """Make sure calculations are correct for bins in descending order."""
        cenwave = 5004.5
        npix = 7
        assert (binning.wave_range(self.bins, cenwave, npix) ==
                binning.wave_range(self.bins[::-1], cenwave, npix))

    def test_pixel_range_exceptions(self):
        """Test for appropriate pixel range exceptions."""
        with pytest.raises(exceptions.SynphotError):
            binning.pixel_range(self.bins, (5000, 5001), mode='up')
        with pytest.raises(exceptions.OverlapError):
            binning.pixel_range(self.bins, (500, 5001))
        with pytest.raises(exceptions.OverlapError):
            binning.pixel_range(self.bins, (5000, 50010))

    @pytest.mark.parametrize(
        ('waverange', 'ans', 'mode'),
        [((5000.5, 5006.5), 6, 'none'),
         ((5000, 5008), 8, 'none'),
         ((5000, 5000), 0, 'round'),
         ((4999.5, 5000.5), 1, 'round'),
         ((5000, 5002), 2, 'round'),
         ((4999.6, 5008.8), 9, 'round'),
         ((5000, 5002), 1, 'min'),
         ((5000.5, 5002.5), 2, 'min'),
         ((5000.5, 5004.4), 3, 'min'),
         ((5000.2, 5004.5), 4, 'min'),
         ((5000, 5000.1), 1, 'max'),
         ((5000.5, 5002.5), 2, 'max'),
         ((5000.5, 5002.6), 3, 'max'),
         ((5001.2, 5004.5), 4, 'max')])
    def test_pixel_range_mode(self, waverange, ans, mode):
        """Test pixel range calculations for all modes."""
        npix = binning.pixel_range(self.bins, waverange, mode=mode)
        assert npix == ans

    @pytest.mark.parametrize(
        ('waverange', 'ans', 'mode'),
        [((5000, 5000.1), 0.1, 'none'),
         ((4999.8, 5000), 0.2, 'none')])
    def test_pixel_range_almosteq(self, waverange, ans, mode):
        """Like :func:`test_pixel_range_mode` but without exact match."""
        npix = binning.pixel_range(self.bins, waverange, mode=mode)
        np.testing.assert_allclose(npix, ans)

    def test_pixel_range_descending_order(self):
        """Make sure calculations are correct for inputs in descending
        order."""
        waverange = np.array([4999.6, 5008.8])
        assert (binning.pixel_range(self.bins, waverange) ==
                binning.pixel_range(self.bins[::-1], waverange))
        assert (binning.pixel_range(self.bins, waverange) ==
                binning.pixel_range(self.bins, waverange[::-1]))


def test_calcbinflux():
    """Test both C-ext and Python versions of calcbinflux().

    This is a simplified version of
    :func:`synphot.observation.Observation.binspec`.

    """
    # Get bandpass data for interpolation.
    hdr, wave, thru = specio.read_fits_spec(
        get_pkg_data_filename(os.path.join('data', 'hst_acs_hrc_f555w.fits')),
        flux_col='THROUGHPUT', flux_unit=u.dimensionless_unscaled)

    # Binned data.
    bins = generate_wavelengths(
        minwave=6000, maxwave=6010, delta=1.0, log=False)[0]
    edges = binning.calculate_bin_edges(bins)

    # Merge bin edges and centers in with the natural waveset.
    spwave = merge_wavelengths(
        merge_wavelengths(wave.value, edges.value), bins.value)

    # Compute indices associated to each endpoint.
    indices = np.searchsorted(spwave, edges.value)
    i_beg = indices[:-1]
    i_end = indices[1:]

    # Prepare integration variables.
    # In old test, this was bandpass * 1 FLAM, which is just bandpass value.
    flux = np.interp(spwave, wave.value, thru.value)
    avflux = (flux[1:] + flux[:-1]) * 0.5
    deltaw = spwave[1:] - spwave[:-1]

    # PYTHON: Sum over each bin.
    binflux_py, intwave_py = binning._slow_calcbinflux(
        bins.size, i_beg, i_end, avflux, deltaw)

    # C-EXT: Sum over each bin.
    try:
        from .. import synphot_utils
    except ImportError:
        warnings.warn('synphot_utils import failed, C-ext test is skipped.',
                      AstropyUserWarning)
    else:
        binflux_c, intwave_c = synphot_utils.calcbinflux(
            bins.size, i_beg, i_end, avflux, deltaw)

        # Compare between Python and C-ext
        np.testing.assert_allclose(binflux_py, binflux_c)
        np.testing.assert_allclose(intwave_py, intwave_c)

    # Compare with expected values.
    # Flux values are inherited from old test, compare at 0.01% relative diff.
    flux_ans = np.array(
        [0.12265425, 0.12226972, 0.12184207, 0.12141429, 0.12098646, 0.1205586,
         0.1201307, 0.11970269, 0.11927488, 0.11884699])
    np.testing.assert_allclose(binflux_py, flux_ans, rtol=1e-4)
    np.testing.assert_array_equal(intwave_py, np.ones(bins.size))
