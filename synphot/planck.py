# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module handles
:ref:`Planck law for blackbody radiation <synphot-planck-law>`.

"""
from __future__ import absolute_import, division, print_function, unicode_literals

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import units as u

# LOCAL
from . import units


__all__ = ['bbfunc']

# Underflow and overflow limits taken from IRAF SYNPHOT
_VERY_SMALL = 1e-4
_VERY_LARGE = 85.0


def bbfunc(wavelengths, temperature):
    """Planck law for blackbody radiation in PHOTLAM per steradian.

    .. warning::

        Data points where overflow or underflow occurs will be set
        to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `~astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `~astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    Returns
    -------
    fluxes : `~astropy.units.quantity.Quantity`
        Blackbody radiation in PHOTLAM per steradian.

    """
    # Silence Numpy
    old_np_err_cfg = np.seterr(all='ignore')

    # Calculations must use Angstrom
    wavelengths = units.validate_quantity(
        wavelengths, u.AA, equivalencies=u.spectral()).astype(np.float64)

    # Calculations must use Kelvin
    temperature = units.validate_quantity(temperature, u.K).astype(np.float64)

    x = wavelengths * temperature

    # Catch division by zero
    mask = x > 0
    x = np.where(mask, units.HC / (const.k_B.cgs * x), 0.0)

    # Catch overflow/underflow
    mask = (x >= _VERY_SMALL) & (x < _VERY_LARGE)
    factor = np.where(mask, 1.0 / np.expm1(x), 0.0)

    # Convert FNU to PHOTLAM
    freq = u.Quantity(np.where(
        factor, wavelengths.to(u.Hz, equivalencies=u.spectral()), 0.0), u.Hz)
    bb_nu = 2.0 * const.h * factor * freq * freq * freq / const.c ** 2
    bb_lam = np.where(
        factor, units.FNU.to(units.PHOTLAM, bb_nu.cgs.value,
                             equivalencies=u.spectral_density(wavelengths)),
        0.0)

    # Restore Numpy settings
    dummy = np.seterr(**old_np_err_cfg)

    return u.Quantity(bb_lam, unit=units.PHOTLAM/u.sr)


# Replaced by ThermalSpectralElement.thermal_source() but kept for testing.
def _bb_photlam_arcsec(wavelengths, temperature):
    """Planck law for blackbody radiation in PHOTLAM per square arcsec.

    Parameters
    ----------
    wavelengths : array_like or `~astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `~astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    Returns
    -------
    fluxes : `~astropy.units.quantity.Quantity`
        Blackbody radiation in PHOTLAM per square arcsec.

    """
    fac = u.Quantity(u.rad.to(u.arcsec) ** 2, u.arcsec**2/u.sr)
    bb_photlam = bbfunc(wavelengths, temperature)
    return bb_photlam / fac


# Replaced by SourceSpectrum.from_blackbody() but kept for testing.
def _bb_photlam(wavelengths, temperature, r=const.R_sun, d=const.kpc):
    """Planck law for blackbody radiation in PHOTLAM,
    where the radiation is normalized to a star of given radius
    at a given distance.

    .. math::

        \\Omega = \\frac{\\pi r^{2}}{d^{2}}

    where :math:`\\Omega` is the solid angle in steradian, *r* is
    the radius of the star, and *d* is the distance.

    Parameters
    ----------
    wavelengths : array_like or `~astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `~astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    r : float or `~astropy.units.quantity.Quantity`
        Radius of the star. If not a Quantity, assumed to be in meter.
        Default is a solar radius.

    d : float or `~astropy.units.quantity.Quantity`
        Distance to the star. If not a Quantity, assumed to be in the
        same unit as ``r``. Default is 1 kpc.

    Returns
    -------
    fluxes : `~astropy.units.quantity.Quantity`
        Normalized blackbody radiation in PHOTLAM.

    """
    if not isinstance(r, u.Quantity):
        r = u.Quantity(r, u.m)

    d = units.validate_quantity(d, r.unit)
    fac = u.Quantity(np.pi * (r.value / d.value) ** 2, unit=u.sr)
    bb_photlam = bbfunc(wavelengths, temperature)

    return bb_photlam * fac
