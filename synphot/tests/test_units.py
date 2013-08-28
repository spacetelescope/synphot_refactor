# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test units.py module.

.. note:: Flux conversion is tested in test_spectrum.py

"""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.tests.helper import pytest

# LOCAL
from .. import synexceptions, units


__doctest_skip__ = ['*']

_wave_angstrom = u.Quantity([0.1, 5000.0, 10000.0], unit=u.AA)
_wavenum_micron = u.Quantity([1e+5, 2.0, 1.0], unit=units.INVERSE_MICRON)
_freq = u.Quantity([2.99792458e+19, 5.99584916e+14, 2.99792458e+14], unit=u.Hz)


def test_implicit_assumptions():
    """These assumptions must be valid for proper conversions."""
    assert units.HC.unit == u.AA * u.erg
    assert units.INVERSE_AA.physical_type == 'wavenumber'
    assert units.INVERSE_MICRON.physical_type == 'wavenumber'
    assert units.AREA.physical_type == 'area'
    assert units.THROUGHPUT.physical_type == 'dimensionless'
    assert units.ABZERO.unit.decompose() == u.mag
    assert units.STZERO.unit.decompose() == u.mag


@pytest.mark.parametrize(
    ('in_u', 'out_u'),
    [('angstroms', u.AA),
     ('inversemicrons', units.INVERSE_MICRON),
     ('transmission', units.THROUGHPUT),
     ('TRANSMISSION', units.THROUGHPUT),
     ('extinction', units.THROUGHPUT),
     ('inverse_angstrom', units.INVERSE_AA),
     ('inverse_micron', units.INVERSE_MICRON),
     ('photlam', units.PHOTLAM),
     ('photnu', units.PHOTNU),
     ('flam', units.FLAM),
     ('fnu', units.FNU),
     ('stmag', units.STMAG),
     ('abmag', units.ABMAG),
     ('obmag', units.OBMAG),
     ('vegamag', units.VEGAMAG),
     ('Kelvin', u.K),
     (u.m, u.m)])
def test_validate_unit(in_u, out_u):
    """Test unit validation."""
    assert units.validate_unit(in_u) == out_u


def test_validate_unit_exceptions():
    """Test that unit validation raises appropriate exceptions."""
    with pytest.raises(synexceptions.SynphotError):
        x = units.validate_unit(10)
    with pytest.raises(ValueError):
        x = units.validate_unit('foo')


@pytest.mark.parametrize(
    ('in_val', 'out_u', 'eqv', 'ans'),
    [(100.0, units.AREA, [], 100.0),
     (u.Quantity(100.0, unit=units.AREA), u.m * u.m, [], 0.01),
     (_wave_angstrom, units.INVERSE_MICRON, units.wave_conversion,
      _wavenum_micron)])
def test_validate_quantity(in_val, out_u, eqv, ans):
    """Test quantity validation."""
    result = units.validate_quantity(in_val, out_u, equivalencies=eqv)
    np.testing.assert_allclose(result.value, ans)
    assert result.unit == out_u


@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans'),
    [(_wave_angstrom, u.Hz, _freq),
     (_freq, u.AA, _wave_angstrom),
     (_wave_angstrom, units.INVERSE_MICRON, _wavenum_micron),
     (_wavenum_micron, u.AA, _wave_angstrom),
     (_freq, units.INVERSE_MICRON, _wavenum_micron),
     (_wavenum_micron, u.Hz, _freq)])
def test_wave_conversion(in_q, out_u, ans):
    """Full equivalencies test with direct conversion."""
    result = in_q.to(out_u, equivalencies=units.wave_conversion)
    np.testing.assert_allclose(result.value, ans.value)
    assert result.unit == ans.unit
