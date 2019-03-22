# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test units.py module.

.. note:: VEGAMAG conversion is tested in test_spectrum.py.

"""
from __future__ import absolute_import, division, print_function

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u

# LOCAL
from .. import exceptions, units

# Wavelength conversions
_wave_angstrom = [0.1, 5000.0, 10000.0] * u.AA
_wavenum_micron = [1e+5, 2.0, 1.0] * (u.micron ** -1)
_freq = [2.99792458e+19, 5.99584916e+14, 2.99792458e+14] * u.Hz

# Flux conversions
# http://ssb.stsci.edu/cdbs/supplemental_calspec/grw_70d5824_stisnic_002.ascii
_area = 45238.93416 * units.AREA  # HST
_wave = [4956.8, 4959.55, 4962.3] * u.AA
_flux_photlam = [9.7654e-3, 1.003896e-2, 9.78473e-3] * units.PHOTLAM
_flux_photnu = [8.00335589e-14, 8.23668949e-14, 8.03700310e-14] * units.PHOTNU
_flux_flam = [3.9135e-14, 4.0209e-14, 3.9169e-14] * units.FLAM
_flux_fnu = [3.20735792e-25, 3.29903646e-25, 3.21727226e-25] * units.FNU
_flux_jy = [3.20735792e-2, 3.29903646e-2, 3.21727226e-2] * u.Jy
_flux_count = [1214.88479883, 1248.91795446, 1217.28946691] * u.count
_flux_stmag = [12.41858665, 12.38919182, 12.41764379] * u.STmag
_flux_abmag = [12.63463143, 12.60403221, 12.63128047] * u.ABmag
_flux_obmag = [-7.71133775, -7.74133477, -7.71348466] * units.OBMAG
_flux_vegamag = [12.72810665, 12.69861694, 12.72605148] * units.VEGAMAG


def test_implicit_assumptions():
    """These assumptions must be valid for proper conversions."""
    assert units.HC.unit == u.AA * u.erg
    assert units.AREA.physical_type == 'area'
    assert units.THROUGHPUT.physical_type == 'dimensionless'
    np.testing.assert_allclose(units.SR_PER_ARCSEC2, 2.3504430539097885e-11)


@pytest.mark.parametrize(
    ('in_u', 'out_u'),
    [('angstroms', u.AA),
     ('inversemicrons', u.micron ** -1),
     ('transmission', units.THROUGHPUT),
     ('TRANSMISSION', units.THROUGHPUT),
     ('extinction', units.THROUGHPUT),
     ('emissivity', units.THROUGHPUT),
     ('photlam', units.PHOTLAM),
     ('photnu', units.PHOTNU),
     ('flam', units.FLAM),
     ('fnu', units.FNU),
     ('stmag', u.STmag),
     ('abmag', u.ABmag),
     ('obmag', units.OBMAG),
     ('vegamag', units.VEGAMAG),
     ('Kelvin', u.K),
     (u.m, u.m)])
def test_validate_unit(in_u, out_u):
    """Test unit validation."""
    assert units.validate_unit(in_u) == out_u


@pytest.mark.parametrize(
    ('in_u', 'out_u'),
    [('angstroms', u.AA),
     ('inversemicrons', u.micron ** -1),
     ('Hz', u.Hz)])
def test_validate_wave_unit(in_u, out_u):
    """Test wavelength unit validation."""
    assert units.validate_wave_unit(in_u) == out_u


def test_validate_unit_exceptions():
    """Test that unit validation raises appropriate exceptions."""
    with pytest.raises(exceptions.SynphotError):
        units.validate_unit(10)
    with pytest.raises(ValueError):
        units.validate_unit('foo')
    with pytest.raises(exceptions.SynphotError):
        units.validate_wave_unit('Kelvin')


@pytest.mark.parametrize(
    ('in_val', 'out_u', 'eqv', 'ans'),
    [(100.0, units.AREA, [], 100.0),
     (100.0 * units.AREA, u.m * u.m, [], 0.01),
     (_wave_angstrom, u.micron ** -1, u.spectral(), _wavenum_micron.value)])
def test_validate_quantity(in_val, out_u, eqv, ans):
    """Test quantity validation."""
    result = units.validate_quantity(in_val, out_u, equivalencies=eqv)
    np.testing.assert_allclose(result.value, ans)
    assert result.unit == out_u


@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans'),
    [(_wave_angstrom, u.Hz, _freq),
     (_freq, u.AA, _wave_angstrom),
     (_wave_angstrom, u.micron ** -1, _wavenum_micron),
     (_wavenum_micron, u.AA, _wave_angstrom),
     (_freq, u.micron ** -1, _wavenum_micron),
     (_wavenum_micron, u.Hz, _freq)])
def test_wave_conversion(in_q, out_u, ans):
    """Full equivalencies test with direct conversion."""
    result = in_q.to(out_u, equivalencies=u.spectral())
    np.testing.assert_allclose(result.value, ans.value)
    assert result.unit == ans.unit


@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans', 'support_scalar'),
    [(_flux_photlam.value, units.PHOTLAM, _flux_photlam, True),
     (_flux_photlam, u.count, _flux_count, False),
     (_flux_count, units.PHOTLAM, _flux_photlam, False),
     (_flux_photlam, units.OBMAG, _flux_obmag, False),
     (_flux_obmag, units.PHOTLAM, _flux_photlam, False),
     (_flux_count, units.OBMAG, _flux_obmag, False),
     (_flux_obmag, u.count, _flux_count, False),
     (_flux_photlam, units.FLAM, _flux_flam, True),
     (_flux_flam, units.PHOTLAM, _flux_photlam, True),
     (_flux_photlam, u.STmag, _flux_stmag, True),
     (_flux_stmag, units.PHOTLAM, _flux_photlam, True),
     (_flux_flam, u.STmag, _flux_stmag, True),
     (_flux_stmag, units.FLAM, _flux_flam, True),
     (_flux_photlam, units.PHOTNU, _flux_photnu, True),
     (_flux_photnu, units.PHOTLAM, _flux_photlam, True),
     (_flux_photlam, units.FNU, _flux_fnu, True),
     (_flux_fnu, units.PHOTLAM, _flux_photlam, True),
     (_flux_photlam, u.ABmag, _flux_abmag, True),
     (_flux_abmag, units.PHOTLAM, _flux_photlam, True),
     (_flux_fnu, u.ABmag, _flux_abmag, True),
     (_flux_abmag, units.FNU, _flux_fnu, True),
     (_flux_fnu, u.STmag, _flux_stmag, True),
     (_flux_fnu, u.mJy, _flux_jy.to(u.mJy), True),
     (_flux_photlam, u.Jy, _flux_jy, True),
     (_flux_jy, units.PHOTLAM, _flux_photlam, True),
     (_flux_flam, u.Jy, _flux_jy, True),
     (np.zeros(3) * units.FNU, units.FLAM, np.zeros(3) * units.FLAM, True)])
def test_flux_conversion(in_q, out_u, ans, support_scalar):
    """Test flux conversion, except VEGAMAG."""
    result = units.convert_flux(_wave, in_q, out_u, area=_area)
    np.testing.assert_allclose(result.value, ans.value, rtol=1e-6)
    assert result.unit == ans.unit

    # Scalar should work, except for count and OBMAG, which need bin centers.
    if support_scalar:
        i = 0
        result = units.convert_flux(_wave[i], in_q[i], out_u, area=_area)
        np.testing.assert_allclose(result.value, ans[i].value, rtol=1e-6)
        assert result.unit == ans[i].unit


def test_flux_conversion_exceptions():
    """Test for appropriate exceptions."""
    # Invalid flux unit
    with pytest.raises(u.UnitsError):
        units.convert_flux(_wave, _wave, units.PHOTLAM)
    with pytest.raises(u.UnitsError):
        units.convert_flux(_wave, _flux_photlam, u.AA)

    # Missing Vega spectrum
    with pytest.raises(exceptions.SynphotError):
        units.convert_flux(_wave, _flux_fnu, units.VEGAMAG, vegaspec=None)

    # Missing area
    with pytest.raises(exceptions.SynphotError):
        units.convert_flux(_wave, _flux_photlam, u.count, area=None)
    with pytest.raises(exceptions.SynphotError):
        units.convert_flux(_wave, _flux_obmag, units.PHOTLAM, area=None)
