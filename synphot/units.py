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


__all__ = ['H', 'C', 'HC', 'AREA', 'THROUGHPUT', 'PHOTLAM', 'PHOTNU', 'FLAM',
           'FNU', 'STMAG', 'ABMAG', 'OBMAG', 'VEGAMAG', 'ABZERO', 'STZERO',
           'spectral_density_mag', 'spectral_density_vega',
           'spectral_density_count', 'validate_unit', 'validate_quantity']


#-------------------#
# General constants #
#-------------------#

H = const.h.cgs  # Planck's constant in erg * sec
C = const.c.to('AA/s')  # Speed of light in Angstrom/sec
HC = H * C

#---------------#
# synphot units #
#---------------#

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

# Register with astropy units
u.add_enabled_units([PHOTLAM, PHOTNU, FLAM, FNU, STMAG, ABMAG, OBMAG, VEGAMAG])

#-----------------#
# Flux conversion #
#-----------------#

ABZERO = u.Quantity(-48.6, unit=u.mag)
STZERO = u.Quantity(-21.1, unit=u.mag)


def spectral_density_mag(wav, magname):
    """Flux equivalencies between PHOTLAM and ABMAG/STMAG.

    Parameters
    ----------
    wav : `astropy.units.quantity.Quantity`
        Quantity associated with values being converted
        (e.g., wavelength or frequency).

    magname : {'abmag', 'stmag'}
        Indicates ABMAG or STMAG. Case-insensitive.
        This is needed because `astropy.units` cannot distinguish
        between different types of magnitudes.

    Returns
    -------
    eqv : list
        List of equivalencies.

    Raises
    ------
    astropy.units.core.UnitsError
        Invalid magnitude system.

    """
    magname = magname.lower()
    wav = wav.to(u.AA, equivalencies=u.spectral()).value

    if magname == 'abmag':
        eqv = [
            (PHOTLAM, ABMAG,
             lambda x: -2.5 * np.log10(H.value * x * wav) + ABZERO.value,
             lambda x: 10**(-0.4 * (x - ABZERO.value)) / (H.value * wav))]
    elif magname == 'stmag':
        eqv = [
            (PHOTLAM, STMAG,
             lambda x: -2.5 * np.log10(HC.value * x / wav) + STZERO.value,
             lambda x: wav * 10**(-0.4 * (x - STZERO.value)) / HC.value)]
    else:
        raise u.UnitsError('{0} is not supported.'.format(magname))

    return eqv


def spectral_density_vega(wav, vegaflux):
    """Flux equivalencies between PHOTLAM and VEGAMAG.

    Parameters
    ----------
    wav : `astropy.units.quantity.Quantity`
        Quantity associated with values being converted
        (e.g., wavelength or frequency).

    vegaflux : `astropy.units.quantity.Quantity`
        Flux of Vega at ``wav``.

    Returns
    -------
    eqv : list
        List of equivalencies.

    """
    vega_photlam = vegaflux.to(
        PHOTLAM, equivalencies=u.spectral_density(wav)).value

    def converter(x):
        """Set nan/inf to -99 mag."""
        val = -2.5 * np.log10(x / vega_photlam)
        result = np.zeros(val.shape, dtype=np.float64) - 99
        mask = np.isfinite(val)
        result[mask] = val[mask]
        return result

    def iconverter(x):
        return vega_photlam * 10**(-0.4 * x)

    return [(PHOTLAM, VEGAMAG, converter, iconverter)]


def spectral_density_count(wav, area):
    """Flux equivalencies between PHOTLAM and count/OBMAG.

    Parameters
    ----------
    wav : `astropy.units.quantity.Quantity`
        Quantity associated with values being converted
        (e.g., wavelength or frequency).

    area : `astropy.units.quantity.Quantity`
        Telescope collecting area.

    Returns
    -------
    eqv : list
        List of equivalencies.

    """
    from .binning import calculate_bin_widths, calculate_bin_edges

    wav = wav.to(u.AA, equivalencies=u.spectral())
    area = area.to(AREA)
    bin_widths = calculate_bin_widths(calculate_bin_edges(wav))
    factor = bin_widths.value * area.value

    def converter_count(x):
        return x * factor

    def iconverter_count(x):
        return x / factor

    def converter_obmag(x):
        return -2.5 * np.log10(x * factor)

    def iconverter_obmag(x):
        return 10**(-0.4 * x) / factor

    return [(PHOTLAM, u.count, converter_count, iconverter_count),
            (PHOTLAM, OBMAG, converter_obmag, iconverter_obmag)]


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
            output_unit = u.micron ** -1
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
