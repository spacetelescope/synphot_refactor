# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test units.py module.

.. note:: Flux conversion is tested in test_spectrum.py

"""
from __future__ import absolute_import, division, print_function, unicode_literals

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.tests.helper import pytest

# LOCAL
from .. import exceptions, units


_wave_angstrom = u.Quantity([0.1, 5000.0, 10000.0], unit=u.AA)
_wavenum_micron = u.Quantity([1e+5, 2.0, 1.0], u.micron ** -1)
_freq = u.Quantity([2.99792458e+19, 5.99584916e+14, 2.99792458e+14], unit=u.Hz)


def test_implicit_assumptions():
    """These assumptions must be valid for proper conversions."""
    assert units.HC.unit == u.AA * u.erg
    assert units.AREA.physical_type == 'area'
    assert units.THROUGHPUT.physical_type == 'dimensionless'
    assert units.ABZERO.unit.decompose() == u.mag
    assert units.STZERO.unit.decompose() == u.mag


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
    with pytest.raises(exceptions.SynphotError):
        x = units.validate_unit(10)
    with pytest.raises(ValueError):
        x = units.validate_unit('foo')


@pytest.mark.parametrize(
    ('in_val', 'out_u', 'eqv', 'ans'),
    [(100.0, units.AREA, [], 100.0),
     (u.Quantity(100.0, unit=units.AREA), u.m * u.m, [], 0.01),
     (_wave_angstrom, u.micron ** -1, u.spectral(), _wavenum_micron)])
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
