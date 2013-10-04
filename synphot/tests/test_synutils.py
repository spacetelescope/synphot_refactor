# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test synutils.py module."""
from __future__ import division, print_function

# STDLIB
import os
import sys

# THIRD PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.tests.helper import pytest
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import synexceptions, synio, synutils, units


__doctest_skip__ = ['*']


@pytest.mark.parametrize(
    ('a', 'b', 'ans'),
    [(np.arange(5, 8), np.arange(10), 'full'),
     (np.arange(10), np.arange(5, 8), 'partial'),
     (np.arange(3), np.arange(2, 5), 'partial'),
     (np.arange(4, 8), np.arange(2, 5), 'partial'),
     (np.arange(3), np.arange(3, 6), 'none'),
     (np.arange(3, 6), np.arange(3), 'none')])
def test_overlap_status(a, b, ans):
    """Test overlap status validation."""
    assert synutils.overlap_status(a, b) == ans


def test_validate_totalflux():
    """Test integrated flux validation."""
    # Valid integrated flux
    synutils.validate_totalflux(0.01)

    # Invalid integrated flux
    with pytest.raises(synexceptions.SynphotError):
        synutils.validate_totalflux(-0.01)
    with pytest.raises(synexceptions.SynphotError):
        synutils.validate_totalflux(0)
    with pytest.raises(synexceptions.SynphotError):
        synutils.validate_totalflux(np.inf)
    with pytest.raises(synexceptions.SynphotError):
        synutils.validate_totalflux(np.nan)


def test_validate_wavelengths():
    """Test wavelengths validation."""
    # Valid wavelengths (ascending)
    a = np.arange(1, 11)
    synutils.validate_wavelengths(a)

    # Valid wavelengths (descending)
    a = a[::-1]
    wave = synutils.validate_wavelengths(u.Quantity(a, unit=u.micron))

    # Invalid wavelengths
    with pytest.raises(synexceptions.SynphotError):
        synutils.validate_wavelengths(u.Quantity(1.0, u.K))
    with pytest.raises(synexceptions.ZeroWavelength):
        synutils.validate_wavelengths(np.arange(10))
    with pytest.raises(synexceptions.UnsortedWavelength):
        synutils.validate_wavelengths([1000, 1002, 1001, 1003, 1004])
    with pytest.raises(synexceptions.DuplicateWavelength):
        synutils.validate_wavelengths([1000, 1001, 1002, 1003, 1003])


def test_tolength():
    """Test wavelength conversion to type length."""
    # Expected values
    wave = u.Quantity([5000.0, 6000.0, 7000.0], unit=u.AA)
    freq = units.C / wave
    w_micron = wave.to(u.micron)
    wn_micron = 1.0 / w_micron

    # Length
    x = synutils.to_length(wave)
    np.testing.assert_array_equal(x.value, wave.value)
    assert x.unit == u.AA

    # Frequency
    x = synutils.to_length(freq, wave_unit=u.micron)
    np.testing.assert_allclose(x.value, w_micron.value)
    assert x.unit == u.micron

    # Wave number
    x = synutils.to_length(wn_micron)
    np.testing.assert_allclose(x.value, wave.value)
    assert x.unit == u.AA

    # Invalid
    with pytest.raises(u.UnitsError):
        x = synutils.to_length(u.Quantity(1.0, u.Jy))


@pytest.mark.parametrize(
    ('num', 'delta', 'log', 'ans'),
    [(10, None, True, [10.0, 10.71773463, 11.48698355, 12.31144413,
                       13.19507911, 14.14213562, 15.15716567, 16.24504793,
                       17.41101127, 18.66065983]),
     (0, 0.05, True, [10.0, 11.22018454, 12.58925412, 14.12537545, 15.84893192,
                      17.7827941, 19.95262315]),
     (10, None, False, np.arange(10, 20)),
     (0, 1.0, False, np.arange(10, 20))])
def test_genwave(num, delta, log, ans):
    """Test wavelength generation."""
    wave, wave_str = synutils.generate_wavelengths(
        minwave=10, maxwave=20, num=num, delta=delta, log=log,
        wave_unit=u.micron)
    np.testing.assert_allclose(wave.value, ans)
    assert wave.unit == u.micron
    assert isinstance(wave_str, basestring)


class TestMergeWave(object):
    """Test wavelengths merging."""
    def setup_class(self):
        self.thres = 1e-12
        self.wave = [5000.0, 5000.01, 5000.02, 5000.03, 5000.04, 6000.0]

    def test_merge_thres(self):
        w = [5000.005, 5000.02 + self.thres, 5500.0, 6000.0]
        ans = [5000.0, 5000.005, 5000.01, 5000.02, 5000.03, 5000.04, 5500.0,
               6000.0]
        wave = synutils.merge_wavelengths(self.wave, w, threshold=self.thres)
        dw = wave[1:] - wave[:-1]
        np.testing.assert_allclose(wave, ans)
        assert np.all(dw > self.thres)

    def test_merge_same(self):
        wave =  synutils.merge_wavelengths(self.wave, self.wave)
        np.testing.assert_array_equal(wave, self.wave)


class TestTrapezoidIntegration(object):
    """Test integrator and utility functions that use it."""
    def setup_class(self):
        # Get bandpass data for integration.
        bandfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w.fits'))
        hdr, self.wave, self.thru = synio.read_fits_spec(
            bandfile, flux_col='THROUGHPUT', flux_unit=u.dimensionless_unscaled)

    def test_avgwave(self):
        """Compare AVGWAVE with old SYNPHOT result."""
        avg_wave = synutils.avg_wavelength(self.wave.value, self.thru.value)
        np.testing.assert_allclose(avg_wave, 5367.9, rtol=1e-5)

    def test_barlam(self):
        """Test BARLAM (no old SYNPHOT result available)."""
        bar_lam = synutils.barlam(self.wave.value, self.thru.value)
        np.testing.assert_allclose(bar_lam, 5331.8945)

    @pytest.mark.parametrize(('a'), [np.array([]), np.array([1])])
    def test_zero_ans(self, a):
        """Test that empty and single-element arrays return zero."""
        assert synutils.trapezoid_integration(a, a) == 0

    @pytest.mark.parametrize(
        ('a', 'b'),
        [(np.arange(5), np.arange(3)),
         (np.arange(10).reshape(5, 2), np.arange(10).reshape(5, 2))])
    def test_exceptions(self, a, b):
        """Test exceptions for shape mismatch and wrong dimensions."""
        with pytest.raises(ValueError):
            x = synutils.trapezoid_integration(a, b)

    def test_exception_ndim0(self):
        """Exception for ndim=0 is different between Python 2 and 3."""
        a = np.array(1)

        if sys.version_info < (3, 0):  # pragma: py2
            expected_err = ValueError
        else:  # pragma: py3
            expected_err = IndexError

        with pytest.raises(expected_err):
            x = synutils.trapezoid_integration(a, a)
