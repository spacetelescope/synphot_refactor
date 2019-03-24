# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synthetic photometry utility functions."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os
from shutil import copyfile

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.config import ConfigItem
from astropy.utils.data import download_file

# LOCAL
from . import exceptions, units

__all__ = ['overlap_status', 'validate_totalflux', 'validate_wavelengths',
           'generate_wavelengths', 'merge_wavelengths', 'download_data']


def overlap_status(a, b):
    """Check overlap between two arrays.

    Parameters
    ----------
    a, b : array-like
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
    wavelengths : array-like or `~astropy.units.quantity.Quantity`
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

    return waveset.astype(np.float64) * wave_unit, waveset_str


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
    waveset1, waveset2 : array-like or `None`
        Wavelength values, assumed to be in the same unit already.
        Also see :func:`~synphot.models.get_waveset`.

    threshold : float, optional
        Merged wavelength values are considered "too close together"
        when the difference is smaller than this number.
        The default is 1e-12.

    Returns
    -------
    out_wavelengths : array-like or `None`
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


def download_data(cdbs_root, verbose=True, dry_run=False):
    """Download CDBS data files to given root directory.
    Download is skipped if a data file already exists.

    Parameters
    ----------
    cdbs_root : str
        Root directory for CDBS data files.

    verbose : bool
        Print extra information to screen.

    dry_run : bool
        Go through the logic but skip the actual download.
        This would return a list of files that *would have been*
        downloaded without network calls.
        Use this option for debugging or testing.

    Raises
    ------
    OSError
        Problem with directory.

    Returns
    -------
    file_list : list of str
        A list of downloaded files.

    """
    from .config import conf  # Avoid potential circular import

    if not os.path.exists(cdbs_root):
        os.makedirs(cdbs_root)
        if verbose:  # pragma: no cover
            print('Created {}'.format(cdbs_root))
    elif not os.path.isdir(cdbs_root):
        raise OSError('{} must be a directory'.format(cdbs_root))

    host = 'http://ssb.stsci.edu/cdbs/'
    file_list = []

    if not cdbs_root.endswith(os.sep):
        cdbs_root += os.sep

    # See https://github.com/astropy/astropy/issues/8524
    for cfgitem in conf.__class__.__dict__.values():
        if (not isinstance(cfgitem, ConfigItem) or
                not cfgitem.name.endswith('file')):
            continue

        url = cfgitem()

        if not url.startswith(host):
            if verbose:  # pragma: no cover
                print('{} is not from {}, skipping download'.format(
                    url, host))
            continue

        dst = url.replace(host, cdbs_root).replace('/', os.sep)

        if os.path.exists(dst):
            if verbose:  # pragma: no cover
                print('{} already exists, skipping download'.format(dst))
            continue

        # Create sub-directories, if needed.
        subdirs = os.path.dirname(dst)
        if not os.path.exists(subdirs):
            os.makedirs(subdirs)

        if not dry_run:  # pragma: no cover
            try:
                src = download_file(url)
                copyfile(src, dst)
            except Exception as exc:
                print('Download failed - {}'.format(str(exc)))
                continue

        file_list.append(dst)
        if verbose:  # pragma: no cover
            print('{} downloaded to {}'.format(url, dst))

    return file_list
