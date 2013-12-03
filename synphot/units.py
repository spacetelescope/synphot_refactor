# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module handles synphot units that are not in `astropy.units`."""
from __future__ import absolute_import, division, print_function, unicode_literals

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
           'spectral_density_count', 'convert_flux', 'validate_unit',
           'validate_quantity']


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


def convert_flux(wavelengths, fluxes, out_flux_unit, **kwargs):
    """Perform :ref:`flux conversion <synphot-flux-conversion>`.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    fluxes : array_like or `astropy.units.quantity.Quantity`
        Flux values. If not a Quantity, assumed to be in PHOTLAM.

    out_flux_unit : str or `astropy.units.core.Unit`
        Output flux unit.

    area : float or `astropy.units.quantity.Quantity`
        Area that fluxes cover. If not a Quantity, assumed to be in cm^2.
        This value *must* be provided for conversions involving
        OBMAG and count, otherwise it is not needed.

    vegaspec : `synphot.spectrum.SourceSpectrum`
        Vega spectrum from :func:`synphot.spectrum.SourceSpectrum.from_vega`.
        This is *only* used for conversions involving VEGAMAG.

    Returns
    -------
    out_flux : `astropy.units.quantity.Quantity`
        Converted flux values.

    Raises
    ------
    astropy.units.core.UnitsError
        Conversion failed.

    synphot.exceptions.SynphotError
        Area or Vega spectrum is not given when needed.

    """
    if not isinstance(fluxes, u.Quantity):
        fluxes = u.Quantity(fluxes, unit=PHOTLAM)

    out_flux_unit = validate_unit(out_flux_unit)
    out_flux_unit_name = out_flux_unit.to_string()
    in_flux_unit_name = fluxes.unit.to_string()

    # No conversion necessary
    if in_flux_unit_name == out_flux_unit_name:
        return fluxes

    in_flux_type = fluxes.unit.physical_type
    out_flux_type = out_flux_unit.physical_type

    # Wavelengths must Quantity
    if not isinstance(wavelengths, u.Quantity):
        wavelengths = u.Quantity(wavelengths, unit=u.AA)

    # Use built-in astropy equivalencies
    if in_flux_type != 'unknown' and out_flux_type != 'unknown':
        return fluxes.to(
            out_flux_unit, equivalencies=u.spectral_density(wavelengths))

    # Convert input unit to PHOTLAM
    if fluxes.unit == PHOTLAM:
        flux_photlam = fluxes
    elif in_flux_type != 'unknown':
        flux_photlam = fluxes.to(
            PHOTLAM, equivalencies=u.spectral_density(wavelengths))
    else:
        flux_photlam = _convert_flux(wavelengths, fluxes, PHOTLAM, **kwargs)

    # Convert PHOTLAM to output unit
    if out_flux_unit == PHOTLAM:
        out_flux = flux_photlam
    elif out_flux_type != 'unknown':
        out_flux = flux_photlam.to(
            out_flux_unit, equivalencies=u.spectral_density(wavelengths))
    else:
        out_flux = _convert_flux(
            wavelengths, flux_photlam, out_flux_unit, **kwargs)

    return out_flux


def _convert_flux(wavelengths, fluxes, out_flux_unit, area=None, vegaspec=None):
    """Flux conversion for PHOTLAM <-> X."""
    flux_unit_names = (fluxes.unit.to_string(), out_flux_unit.to_string())

    if PHOTLAM.to_string() not in flux_unit_names:
        raise exceptions.SynphotError(
            'PHOTLAM must be one of the conversion units but get '
            '{0}.'.format(flux_unit_names))

    # VEGAMAG
    if VEGAMAG.to_string() in flux_unit_names:
        from .spectrum import SourceSpectrum

        if not isinstance(vegaspec, SourceSpectrum):
            raise exceptions.SynphotError('Vega spectrum is missing.')

        flux_vega = vegaspec.resample(wavelengths)
        out_flux = fluxes.to(
            out_flux_unit,
            equivalencies=spectral_density_vega(wavelengths, flux_vega))

    # OBMAG or count
    elif (u.count.to_string() in flux_unit_names or
          OBMAG.to_string() in flux_unit_names):
        if area is None:
            raise exceptions.SynphotError(
                'Area is compulsory for conversion involving count or OBMAG.')
        elif not isinstance(area, u.Quantity):
            area = u.Quantity(area, unit=AREA)

        out_flux = fluxes.to(
            out_flux_unit,
            equivalencies=spectral_density_count(wavelengths, area))

    # STMAG
    elif STMAG.to_string() in flux_unit_names:
        out_flux = fluxes.to(
            out_flux_unit,
            equivalencies=spectral_density_mag(wavelengths, 'stmag'))

    # ABMAG
    elif ABMAG.to_string() in flux_unit_names:
        out_flux = fluxes.to(
            out_flux_unit,
            equivalencies=spectral_density_mag(wavelengths, 'abmag'))

    else:
        raise u.UnitsError('{0} and {1} are not convertible'.format(
                fluxes.unit, out_flux_unit))

    return u.Quantity(out_flux, unit=out_flux_unit)


#--------------------#
# Utility functions  #
#--------------------#

def validate_unit(input_unit):
    """Validate unit.

    To be compatible with existing SYNPHOT data files:

        * 'angstroms' and 'inversemicrons' are accepted although
          unrecognized by astropy units
        * 'transmission', 'extinction', and 'emissivity' are
          converted to astropy dimensionless unit

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
        elif input_unit_lowcase in ('transmission', 'extinction', 'emissivity'):
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
        (see :func:`convert_flux`).

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
