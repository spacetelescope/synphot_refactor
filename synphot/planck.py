# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module handles
:ref:`Planck law for blackbody radiation <synphot-planck-law>`.

"""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import units as u

# LOCAL
from . import units


__all__ = ['bbfunc', 'bb_photlam_arcsec', 'bb_photlam']


def bbfunc(wavelengths, temperature):
    """Planck law for blackbody radiation in PHOTLAM per steradian.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    Returns
    -------
    fluxes : `astropy.units.quantity.Quantity`
        Blackbody radiation in PHOTLAM per steradian.

    """
    if not isinstance(wavelengths, u.Quantity):
        wavelengths = u.Quantity(wavelengths, unit=u.AA)

    # Calculations must use Hz
    freq = wavelengths.to(u.Hz, equivalencies=u.spectral())

    # Calculations must use Kelvin
    temperature = units.validate_quantity(temperature, u.K)

    # Calculate blackbody radiation in FNU, then convert to PHOTLAM
    factor = np.expm1(const.h * freq / (const.k_B * temperature))
    bb_nu = 2 * const.h * freq * freq * freq / (const.c ** 2 * factor)
    bb_lam = units.FNU.to(units.PHOTLAM, bb_nu.cgs.value,
                          equivalencies=u.spectral_density(wavelengths))

    return u.Quantity(bb_lam, unit=units.PHOTLAM/u.sr)


def bb_photlam_arcsec(wavelengths, temperature):
    """Planck law for blackbody radiation in PHOTLAM per square arcsec.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    Returns
    -------
    fluxes : `astropy.units.quantity.Quantity`
        Blackbody radiation in PHOTLAM per square arcsec.

    """
    fac = u.Quantity(u.rad.to(u.arcsec) ** 2, u.arcsec**2/u.sr)
    bb_photlam = bbfunc(wavelengths, temperature)
    return bb_photlam / fac


def bb_photlam(wavelengths, temperature, r=const.R_sun, d=const.kpc):
    """Planck law for blackbody radiation in PHOTLAM,
    where the radiation is normalized to a star of given radius
    at a given distance.

    .. math::

        \\Omega = \\frac{\\pi r^{2}}{d^{2}}

    where :math:`\\Omega` is the solid angle in steradian, *r* is
    the radius of the star, and *d* is the distance.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    temperature : float or `astropy.units.quantity.Quantity`
        Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

    r : float or `astropy.units.quantity.Quantity`
        Radius of the star. If not a Quantity, assumed to be in meter.
        Default is a solar radius.

    d : float or `astropy.units.quantity.Quantity`
        Distance to the star. If not a Quantity, assumed to be in the
        same unit as ``r``. Default is 1 kpc.

    Returns
    -------
    fluxes : `astropy.units.quantity.Quantity`
        Normalized blackbody radiation in PHOTLAM.

    """
    if not isinstance(r, u.Quantity):
        r = u.Quantity(r, u.m)

    d = units.validate_quantity(d, r.unit)
    fac = u.Quantity(np.pi * (r.value / d.value) ** 2, unit=u.sr)
    bb_photlam = bbfunc(wavelengths, temperature)

    return bb_photlam * fac
