# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synthetic photometry utility functions."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import modeling
from astropy import units as u

# LOCAL
from . import exceptions, units

__all__ = ['get_waveset', 'overlap_status', 'validate_totalflux',
           'validate_wavelengths', 'generate_wavelengths', 'merge_wavelengths']


def get_waveset(model):
    """Get optimal wavelengths for sampling a given model.

    Parameters
    ----------
    model : `~astropy.modeling.Model`
        Model.

    Returns
    -------
    waveset : array_like or `None`
        Optimal wavelengths. `None` if undefined.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid model.

    """
    if not isinstance(model, modeling.Model):
        raise exceptions.SynphotError('{0} is not a model.'.format(model))

    if (isinstance(model, modeling.SerialCompositeModel) and
            model._transforms[0].__class__.__name__ == 'Redshift'):
        z = model._transforms[0].inverse
        w = get_waveset(model._transforms[1])
        if w is None:
            waveset = None
        else:
            waveset = z(w)

    elif isinstance(model, modeling._compound_deprecated._CompositeModel):
        w_list = [get_waveset(m) for m in model._transforms]
        waveset = merge_wavelengths(w_list[0], w_list[1])
        for cur_w in w_list[2:]:
            waveset = merge_wavelengths(waveset, cur_w)

    elif hasattr(model, 'sampleset'):
        waveset = model.sampleset

        # Hack Box1D waveset so its bandpar results are consistent with IRAF
        if model.__class__.__name__ == 'Box1D':
            waveset = np.arange(waveset[0], waveset[-1], 0.01)

    else:
        waveset = None

    return waveset


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
    synphot.exceptions.SynphotError
        Input is zero, negative, or not a number.

    """
    if totalflux <= 0.0:
        raise exceptions.SynphotError('Integrated flux is <= 0')
    elif np.isnan(totalflux):
        raise exceptions.SynphotError('Integrated flux is NaN')
    elif np.isinf(totalflux):
        raise exceptions.SynphotError('Integrated flux is infinite')


def validate_wavelengths(wavelengths):
    """Check wavelengths for ``synphot`` compatibility.

    Wavelengths must satisfy these conditions:

        * valid unit type, if given
        * no zeroes
        * monotonic ascending or descending
        * no duplicate values

    Parameters
    ----------
    wavelengths : array_like or `~astropy.units.quantity.Quantity`
        Wavelength values.

    Raises
    ------
    synphot.exceptions.SynphotError
        Wavelengths unit type is invalid.

    synphot.exceptions.DuplicateWavelength
        Wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        Wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        Negative or zero wavelength occurs in wavelength array.

    """
    if isinstance(wavelengths, u.Quantity):
        units.validate_wave_unit(wavelengths.unit)
        wave = wavelengths.value
    else:
        wave = wavelengths

    if np.isscalar(wave):
        wave = [wave]

    wave = np.asarray(wave)

    # Check for zeroes
    if np.any(wave <= 0):
        raise exceptions.ZeroWavelength(
            'Negative or zero wavelength occurs in wavelength array',
            rows=np.where(wave <= 0)[0])

    # Check for monotonicity
    sorted_wave = np.sort(wave)
    if not np.alltrue(sorted_wave == wave):
        if np.alltrue(sorted_wave[::-1] == wave):
            pass  # Monotonic descending is allowed
        else:
            raise exceptions.UnsortedWavelength(
                'Wavelength array is not monotonic',
                rows=np.where(sorted_wave != wave)[0])

    # Check for duplicate values
    if wave.size > 1:
        dw = sorted_wave[1:] - sorted_wave[:-1]
        if np.any(dw == 0):
            raise exceptions.DuplicateWavelength(
                'Wavelength array contains duplicate entries',
                rows=np.where(dw == 0)[0])


def generate_wavelengths(minwave=500, maxwave=26000, num=10000, delta=None,
                         log=True, wave_unit=u.AA):
    """Generate wavelength array to be used for spectrum sampling.

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

    wave_unit : str or `~astropy.units.core.Unit`
        Wavelength unit. Default is Angstrom.

    Returns
    -------
    waveset : `~astropy.units.quantity.Quantity`
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
    waveset1, waveset2 : array_like or `None`
        Wavelength values, assumed to be in the same unit already.
        Also see :func:`get_waveset`.

    threshold : float, optional
        Merged wavelength values are considered "too close together"
        when the difference is smaller than this number.
        The default is 1e-12.

    Returns
    -------
    out_wavelengths : array_like or `None`
        Merged wavelengths. `None` if undefined.

    """
    if waveset1 is None and waveset2 is None:
        out_wavelengths = None
    elif waveset1 is not None and waveset2 is None:
        out_wavelengths = waveset1
    elif waveset1 is None and waveset2 is not None:
        out_wavelengths = waveset2
    else:
        out_wavelengths = np.union1d(waveset1, waveset2)
        delta = out_wavelengths[1:] - out_wavelengths[:-1]
        i_good = np.where(delta > threshold)

        # Remove "too close together" duplicates
        if len(i_good[0]) < delta.size:
            out_wavelengths = np.append(
                out_wavelengths[i_good], out_wavelengths[-1])

    return out_wavelengths
