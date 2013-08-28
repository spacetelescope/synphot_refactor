# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synthetic photometry utility functions."""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u

# LOCAL
from . import synexceptions, units


__all__ = ['overlap_status', 'validate_totalflux', 'validate_wavelengths',
           'to_length', 'generate_wavelengths', 'merge_wavelengths',
           'trapezoid_integration', 'avg_wavelength', 'barlam']


def overlap_status(a, b):
    """Check overlap between two arrays.

    Parameters
    ----------
    a, b : array_like
        Arrays to check. Assumed to be in the same unit.

    Returns
    -------
    result : {'full', 'partial', 'none'}
        * 'full' - ``a`` is within or same as ``b``
        * 'partial' - ``a`` partially overlaps with ``b``
        * 'none' - ``a`` does not overlap ``b``

    """
    # Get the endpoints
    a1, a2 = a.min(), a.max()
    b1, b2 = b.min(), b.max()

    # Do the comparison
    if a1 >= b1 and a2 <= b2:
        result = 'full'
    elif a2 < b1 or b2 < a1:
        result = 'none'
    else:
        result = 'partial'

    return result


def validate_totalflux(totalflux):
    """Check integrated flux for invalid values.

    Parameters
    ----------
    totalflux : float
        Integrated flux.

    Raises
    ------
    synphot.synexceptions.SynphotError
        Input is zero, negative, or not a number.

    """
    if totalflux <= 0.0:
        raise synexceptions.SynphotError('Integrated flux is <= 0')
    elif np.isnan(totalflux):
        raise synexceptions.SynphotError('Integrated flux is NaN')
    elif np.isinf(totalflux):
        raise synexceptions.SynphotError('Integrated flux is infinite')


def validate_wavelengths(wavelengths):
    """Check wavelengths for synphot compatibility.

    Wavelengths must satisfy these conditions:

        * valid unit type
        * no zeroes
        * monotonic ascending or descending
        * no duplicate values

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in Angstrom.

    Raises
    ------
    synphot.synexceptions.SynphotError
        If wavelengths unit type is invalid.

    synphot.synexceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.synexceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.synexceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    if not isinstance(wavelengths, u.Quantity):
        wavelengths = u.Quantity(wavelengths, unit=u.AA)

    unit_type = wavelengths.unit.physical_type
    wave = wavelengths.value

    if unit_type not in ('length', 'wavenumber', 'frequency'):
        raise synexceptions.SynphotError(
            'wavelength physical type is not length, wave number, or '
            'frequency: {0}'.format(unit_type))

    # Check for zeroes
    if np.any(wave <= 0):
        raise synexceptions.ZeroWavelength(
            'Negative or zero wavelength occurs in wavelength array',
            rows=np.where(wave <= 0)[0])

    # Check for monotonicity
    sorted_wave = np.sort(wave)
    if not np.alltrue(sorted_wave == wave):
        if np.alltrue(sorted_wave[::-1] == wave):
            pass  # Monotonic descending is allowed
        else:
            raise synexceptions.UnsortedWavelength(
                'Wavelength array is not monotonic',
                rows=np.where(sorted_wave != wave)[0])

    # Check for duplicate values
    if not np.isscalar(wave):
        dw = sorted_wave[1:] - sorted_wave[:-1]
        if np.any(dw == 0):
            raise synexceptions.DuplicateWavelength(
                'Wavelength array contains duplicate entries',
                rows=np.where(dw == 0)[0])


def to_length(wavelengths, wave_unit=u.AA):
    """Ensure wavelengths are of length type.

    If input is frequency or wave number, it is converted
    to given default unit. Otherwise, no conversion is done.

    Parameters
    ----------
    wavelengths : `astropy.units.quantity.Quantity`
        Wavelength values.

    wave_unit : str or `astropy.units.core.Unit`
        Wavelength unit to convert to if input is not of
        type length. Default is Angstrom.

    Returns
    -------
    outwave : `astropy.units.quantity.Quantity`
        Wavelengths converted to type length.

    """
    if wavelengths.unit.physical_type == 'length':
        outwave = wavelengths
    else:
        wave_unit = units.validate_unit(wave_unit)
        outwave = wavelengths.to(wave_unit, equivalencies=units.wave_conversion)

    return outwave


def generate_wavelengths(minwave=500, maxwave=26000, num=10000, delta=None,
                         log=True, wave_unit=u.AA):
    """Generate wavelengths to be used for some synphot spectral types.

    .. math::

        minwave \\le \\lambda < maxwave

    Parameters
    ----------
    minwave, maxwave : float
        Lower and upper limits of the wavelengths.
        These must be values in linear space regardless of ``log``.

    num : int
        The number of wavelength values.
        This is only used when ``delta=None``.

    delta : float or `None`
        Delta between wavelength values.
        When ``log=True``, this is the spacing in log space.

    log : bool
        If `True`, the wavelength values are evenly spaced in log scale.
        Otherwise, spacing is linear.

    wave_unit : str or `astropy.units.core.Unit`
        Wavelength unit. Default is Angstrom.

    Returns
    -------
    waveset : `astropy.units.quantity.Quantity`
        Generated wavelength set.

    waveset_str : str
        Info string associated with the result.

    """
    wave_unit = units.validate_unit(wave_unit)

    if delta is not None:
        num = None

    waveset_str = 'Min: {0}, Max: {1}, Num: {2}, Delta: {3}, Log: {4}'.format(
        minwave, maxwave, num, delta, log)

    # Log space
    if log:
        logmin = np.log10(minwave)
        logmax = np.log10(maxwave)

        if delta is None:
            waveset = np.logspace(logmin, logmax, num, endpoint=False)
        else:
            waveset = 10 ** np.arange(logmin, logmax, delta)

    # Linear space
    else:
        if delta is None:
            waveset = np.linspace(minwave, maxwave, num, endpoint=False)
        else:
            waveset = np.arange(minwave, maxwave, delta)

    return u.Quantity(waveset, unit=wave_unit, dtype=np.float64), waveset_str


def merge_wavelengths(waveset1, waveset2, threshold=1e-12):
    """Return the union of the two sets of wavelengths using
    :func:`numpy.union1d`.

    The merged wavelengths may sometimes contain numbers which are nearly
    equal but differ at levels as small as 1e-14. Having values this
    close together can cause problems down the line. So, here we test
    whether any such small differences are present, with a small
    difference defined as less than ``threshold``. If a small
    difference is present, the lower of the too-close pair is removed.

    Parameters
    ----------
    waveset1, waveset2 : array_like
        Wavelength values, assumed to be in the same unit already.

    threshold : float, optional
        Merged wavelength values are considered "too close together"
        when the difference is smaller than this number.
        The default is 1e-12.

    Returns
    -------
    out_wavelengths : array_like
        Merged wavelengths.

    """
    out_wavelengths = np.union1d(waveset1, waveset2)
    delta = out_wavelengths[1:] - out_wavelengths[:-1]
    i_good = np.where(delta > threshold)

    # Remove "too close together" duplicates
    if len(i_good[0]) < delta.size:
        out_wavelengths = np.append(out_wavelengths[i_good],
                                    out_wavelengths[-1])

    return out_wavelengths


def trapezoid_integration(x, y):
    """Perform trapezoid integration for spectrum data.

    Parameters
    ----------
    x : array_like
        Wavelength values.

    y : array_like
        Flux or throughput values.

    Returns
    -------
    result : array_like
        Integrated result. It is zero if wavelengths are invalid.

    """
    npoints = x.size

    if npoints > 0:
        result = np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1]))
        if x[-1] < x[0]:
            result *= -1.0
    else:
        result = 0.0

    return result


def avg_wavelength(wave, flux):
    """Calculate the :ref:`average wavelength <synphot-formula-avgwv>`.

    Parameters
    ----------
    wave, flux : array_like
        Wavelength and flux values.

    Returns
    -------
    avg_wave : float
        Passband average wavelength in the unit of ``wave``.

    """
    num = trapezoid_integration(wave, flux * wave)
    den = trapezoid_integration(wave, flux)

    if den == 0:  # pragma: no cover
        avg_wave = 0.0
    else:
        avg_wave = num / den

    return avg_wave


def barlam(wave, flux):
    """Calculate :ref:`mean log wavelength <synphot-formula-barlam>`.

    Parameters
    ----------
    wave, flux : array_like
        Wavelength and flux values.

    Returns
    -------
    bar_lam : float
        Mean log wavelength in the unit of ``wave``.

    """
    num = trapezoid_integration(wave, flux * np.log(wave) / wave)
    den = trapezoid_integration(wave, flux / wave)

    if num == 0 or den == 0:  # pragma: no cover
        bar_lam = 0.0
    else:
        bar_lam = np.exp(num / den)

    return bar_lam
