# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module handles synphot units that are not in `astropy.units`.

The actual conversions are in `synphot.spectrum` because they require
spectral information.

"""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import units as u

# LOCAL
from . import exceptions


__all__ = ['H', 'C', 'HC', 'INVERSE_AA', 'INVERSE_MICRON',
           'wave_conversion', 'AREA', 'THROUGHPUT', 'PHOTLAM',
           'PHOTNU', 'FLAM', 'FNU', 'STMAG', 'ABMAG', 'OBMAG',
           'VEGAMAG', 'ABZERO', 'STZERO', 'flux_conversion_wav',
           'flux_conversion_freq', 'flux_conversion_vegamag',
           'flux_conversion_nondensity', 'validate_unit', 'validate_quantity']


#-------------------#
# General constants #
#-------------------#

H = const.h.cgs  # Planck's constant in erg * sec
C = const.c.to('AA/s')  # Speed of light in Angstrom/sec
HC = H * C


#----------------------------#
# For wavelength conversions #
#----------------------------#

INVERSE_AA = u.def_unit(
    'inverse_angstrom', 1 / u.AA,
    format={'generic': '1/angstrom', 'console': '1/angstrom',
            'latex': r'\frac{1}{\AA}'})
INVERSE_MICRON = u.def_unit(
    'inverse_micron', 1 / u.micron,
    format={'generic': '1/um', 'console': '1/um', 'latex': r'\frac{1}{\mu m}'})
wave_conversion = u.spectral() + [
    (u.micron, INVERSE_MICRON, lambda x: 1.0 / x, lambda x: 1.0 / x),
    (u.Hz, INVERSE_AA, lambda x: x / C.value, lambda x: x * C.value) ]


#----------------------#
# For flux conversions #
#----------------------#

# Default unit of area covered by flux
AREA = u.cm * u.cm

# synphot unitless unit (using def_unit mess up arithmetic result unit string)
THROUGHPUT = u.dimensionless_unscaled

# synphot flux units
PHOTLAM = u.def_unit(
    'photlam', u.photon / (u.cm**2 * u.s * u.AA),
    format={'generic': 'PHOTLAM', 'console': 'PHOTLAM'})
PHOTNU = u.def_unit(
    'photnu',  u.photon / (u.cm**2 * u.s * u.Hz),
    format={'generic': 'PHOTNU', 'console': 'PHOTNU'})
FLAM = u.def_unit(
    'flam', u.erg / (u.cm**2 * u.s * u.AA),
    format={'generic': 'FLAM', 'console': 'FLAM'})
FNU = u.def_unit(
    'fnu',  u.erg / (u.cm**2 * u.s * u.Hz),
    format={'generic': 'FNU', 'console': 'FNU'})
STMAG = u.def_unit(
    'stmag', u.mag, format={'generic': 'STMAG', 'console': 'STMAG'})
ABMAG = u.def_unit(
    'abmag', u.mag, format={'generic': 'ABMAG', 'console': 'ABMAG'})
OBMAG = u.def_unit(
    'obmag', u.mag, format={'generic': 'OBMAG', 'console': 'OBMAG'})
VEGAMAG = u.def_unit(
    'vegamag', u.mag, format={'generic': 'VEGAMAG', 'console': 'VEGAMAG'})

# Magnitude zero points
ABZERO = u.Quantity(-48.6, unit=u.mag)
STZERO = u.Quantity(-21.1, unit=u.mag)


def _div_flux(fluxspec):
    """For PHOTLAM to VEGAMAG conversion."""
    val = -2.5 * np.log10(fluxspec[0] / fluxspec[1])
    result = np.zeros(val.shape, dtype=val.dtype) - 99
    mask = np.isfinite(val)
    result[mask] = val[mask]
    return result


# Flux equivalencies take one of the following:
#     waveflux = (wave, flux)
#     fluxspec = (flux, flux_vega)
#     fluxbinarea = (flux, bin, area)
#
# wave and bin in Angstrom, area in cm^2, flux_vega in PHOTLAM
#
# astropy cannot distinguish between different types of mags,
# so the equivalencies are separated here.
flux_conversion_wav = [
    (PHOTLAM, FLAM,
     lambda waveflux: HC.value * waveflux[1] / waveflux[0],
     lambda waveflux: waveflux[1] * waveflux[0] / HC.value),
    (PHOTLAM, STMAG,
     lambda waveflux: -2.5 * np.log10(
            HC.value * waveflux[1] / waveflux[0]) + STZERO.value,
     lambda waveflux: waveflux[0] * 10**(
            -0.4 * (waveflux[1] - STZERO.value)) / HC.value) ]
flux_conversion_freq = [
    (PHOTLAM, PHOTNU,
     lambda waveflux: waveflux[1] * waveflux[0]**2 / C.value,
     lambda waveflux: C.value * waveflux[1] / waveflux[0]**2),
    (PHOTLAM, FNU,
     lambda waveflux: H.value * waveflux[1] * waveflux[0],
     lambda waveflux: waveflux[1] / (waveflux[0] * H.value)),
    (PHOTLAM, ABMAG,
     lambda waveflux: -2.5 * np.log10(
            H.value * waveflux[1] * waveflux[0]) + ABZERO.value,
     lambda waveflux:  10**(
            -0.4 * (waveflux[1] - ABZERO.value)) / (H.value * waveflux[0])) ]
flux_conversion_vegamag = [
    (PHOTLAM, VEGAMAG, _div_flux,
     lambda fluxspec: fluxspec[1] * 10**(-0.4 * fluxspec[0])) ]
flux_conversion_nondensity = [
    (PHOTLAM, OBMAG,
     lambda fluxbinarea: -2.5 * np.log10(
            fluxbinarea[0] * fluxbinarea[1] * fluxbinarea[2]),
     lambda fluxbinarea: 10**(
            -0.4 * fluxbinarea[0]) / (fluxbinarea[1] * fluxbinarea[2])),
    (PHOTLAM, u.count,
     lambda fluxbinarea: fluxbinarea[0] * fluxbinarea[1] * fluxbinarea[2],
     lambda fluxbinarea: fluxbinarea[0] / (fluxbinarea[1] * fluxbinarea[2])) ]


#-----------------------------#
# Register with astropy units #
#-----------------------------#

u.add_enabled_units([INVERSE_AA, INVERSE_MICRON, PHOTLAM, PHOTNU, FLAM, FNU,
                     STMAG, ABMAG, OBMAG, VEGAMAG])


#--------------------#
# Utility functions  #
#--------------------#

def validate_unit(input_unit):
    """Validate unit.

    To be compatible with existing SYNPHOT data files:

        * 'angstroms' and 'inversemicrons' are accepted although
          unrecognized by astropy units
        * 'transmission' and 'extinction' are converted to astropy
          dimensionless unit

    Parameters
    ----------
    input_unit : str or `astropy.units.core.Unit`
        Unit to validate.

    Returns
    -------
    output_unit : `astropy.units.core.Unit`
        Validated unit.

    Raises
    ------
    synphot.exceptions.SynphotError
        If unit is invalid.

    """
    if isinstance(input_unit, basestring):
        input_unit_lowcase = input_unit.lower()

        if input_unit_lowcase == 'angstroms':
            output_unit = u.AA
        elif input_unit_lowcase == 'inversemicrons':
            output_unit = INVERSE_MICRON
        elif input_unit_lowcase in ('transmission', 'extinction'):
            output_unit = THROUGHPUT
        else:
            try:  # astropy.units is case-sensitive
                output_unit = u.Unit(input_unit)
            except ValueError:  # synphot is case-insensitive
                output_unit = u.Unit(input_unit_lowcase)

    elif isinstance(input_unit, u.UnitBase):
        output_unit = input_unit

    else:
        raise exceptions.SynphotError(
            '{0} must be a recognized string or '
            'astropy.units.core.Unit'.format(input_unit))

    return output_unit


def validate_quantity(input_value, output_unit, equivalencies=[]):
    """Validate quantity (value and unit).

    Parameters
    ----------
    input_value : number, array_like, or `astropy.units.quantity.Quantity`
        Quantity to validate. If not a Quantity, assumed to be
        already in output unit.

    output_unit : str or `astropy.units.core.Unit`
        Output quantity unit.

    equivalencies : list of equivalence pairs, optional
        See :func:`astropy.units.core.UnitBase.to`.
        Does not work for flux conversion
        (see :func:`synphot.spectrum.convert_fluxes`).

    Returns
    -------
    output_value : `astropy.units.quantity.Quantity`
        Validated quantity in given unit.

    """
    output_unit = validate_unit(output_unit)

    if isinstance(input_value, u.Quantity):
        output_value = input_value.to(output_unit, equivalencies=equivalencies)
    else:
        output_value = u.Quantity(input_value, unit=output_unit)

    return output_value
