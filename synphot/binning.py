# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Utilities related to wavelength bin calculations."""
from __future__ import absolute_import, division, print_function
from .extern import six

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u

# LOCAL
from . import exceptions

__all__ = ['calculate_bin_edges', 'calculate_bin_widths',
           'calculate_bin_centers', 'wave_range', 'pixel_range']


def _slow_calcbinflux(len_binwave, i_beg, i_end, avflux, deltaw):
    """Python implementation of ``calcbinflux``.

    This is only used if ``synphot.synphot_utils`` C-extension
    import fails.

    See docstrings.py

    """
    binflux = np.empty(shape=(len_binwave, ), dtype=np.float64)
    intwave = np.empty(shape=(len_binwave, ), dtype=np.float64)

    # Note that, like all Python striding, the range over which
    # we integrate is [first:last).
    for i in six.moves.range(len(i_beg)):
        first = i_beg[i]
        last = i_end[i]
        cur_dw = deltaw[first:last]
        intwave[i] = cur_dw.sum()
        binflux[i] = np.sum(avflux[first:last] * cur_dw) / intwave[i]

    return binflux, intwave


# Try to import the C version of calcbinflux, otherwise fall back
# to the Python implementation above.
try:
    from . import synphot_utils
except ImportError:
    calcbinflux = _slow_calcbinflux
else:
    calcbinflux = synphot_utils.calcbinflux


def calculate_bin_edges(centers):
    """Calculate the edges of wavelength bins given the centers.

    The algorithm calculates bin edges as the midpoints between bin centers
    and treats the first and last bins as symmetric about their centers.

    Parameters
    ----------
    centers : array-like or `~astropy.units.quantity.Quantity`
        Sequence of bin centers. Must be 1D and have at least two values.
        If not a Quantity, assumed to be in Angstrom.

    Returns
    -------
    edges : `~astropy.units.quantity.Quantity`
        Array of bin edges. Will be 1D, have one more value
        than ``centers``, and also the same unit.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid input.

    """
    if not isinstance(centers, u.Quantity):
        centers = centers * u.AA

    if centers.ndim != 1:
        raise exceptions.SynphotError('Bin centers must be 1D array.')

    if centers.size < 2:
        raise exceptions.SynphotError(
            'Bin centers must have at least two values.')

    edges = np.empty(centers.size + 1, dtype=np.float64)
    edges[1:-1] = (centers.value[1:] + centers.value[:-1]) * 0.5

    # Compute the first and last by making them symmetric
    edges[0] = 2.0 * centers.value[0] - edges[1]
    edges[-1] = 2.0 * centers.value[-1] - edges[-2]

    return edges * centers.unit


def calculate_bin_widths(edges):
    """Calculate the widths of wavelengths bins given their edges.

    Parameters
    ----------
    edges : array-like or `~astropy.units.quantity.Quantity`
        Sequence of bin edges. Must be 1D and have at least two values.
        If not a Quantity, assumed to be in Angstrom.

    Returns
    -------
    widths : `~astropy.units.quantity.Quantity`
        Array of bin widths. Will be 1D, have one less value
        than ``edges``, and also the same unit.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid input.

    """
    if not isinstance(edges, u.Quantity):
        edges = edges * u.AA

    if edges.ndim != 1:
        raise exceptions.SynphotError('Bin edges must be 1D array.')

    if edges.size < 2:
        raise exceptions.SynphotError(
            'Bin edges must have at least two values.')

    return np.abs(edges[1:] - edges[:-1])


def calculate_bin_centers(edges):
    """Calculate the centers of wavelengths bins given their edges.

    Parameters
    ----------
    edges : array-like or `~astropy.units.quantity.Quantity`
        Sequence of bin edges. Must be 1D and have at least two values.
        If not a Quantity, assumed to be in Angstrom.

    Returns
    -------
    centers : `~astropy.units.quantity.Quantity`
        Array of bin centers. Will be 1D, have one less value
        than ``edges``, and also the same unit.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid input.

    """
    if not isinstance(edges, u.Quantity):
        edges = edges * u.AA

    if edges.ndim != 1:
        raise exceptions.SynphotError('Bin edges must be 1D array.')

    if edges.size < 2:
        raise exceptions.SynphotError(
            'Bin edges must have at least two values.')

    centers = np.empty(edges.size - 1, dtype=np.float64)
    centers[0] = edges.value[:2].mean()

    for i in six.moves.range(1, centers.size):
        centers[i] = 2.0 * edges.value[i] - centers[i - 1]

    return centers * edges.unit


def wave_range(bins, cenwave, npix, mode='round'):
    """Calculate the wavelength range covered by the given number of pixels
    centered on the given central wavelength of the given bins.

    Parameters
    ----------
    bins : array-like
        Wavelengths at bin centers, each centered on a pixel.
        Must be 1D array.

    cenwave : float
        Desired central wavelength, in the same unit as ``bins``.

    npix : int
        Desired number of pixels, centered on ``cenwave``.

    mode : {'round', 'min', 'max', 'none'}
        Determines how the pixels at the edges of the wavelength range
        are handled. All the options, except 'none', will return
        wavelength range edges that correspond to pixel edges:

            * 'round' - Wavelength range edges are the pixel edges
              and the range spans exactly ``npix`` pixels. An edge
              that falls in the center of a bin is rounded to the
              nearest pixel edge. This is the default.

            * 'min' - Wavelength range is shrunk such that it includes
              an integer number of pixels and its edges fall on pixel
              edges. It may not span exactly ``npix`` pixels.

            * 'max' - Wavelength range is expanded such that it
              includes an integer number of pixels and its edges fall
              on pixel edges. It may not span exactly ``npix`` pixels.

            * 'none' - Exact wavelength range is returned. The edges
              may not correspond to pixel edges, but it covers exactly
              ``npix`` pixels.

    Returns
    -------
    wave1, wave2 : float
        Lower and upper limits of the wavelength range.

    Raises
    ------
    synphot.exceptions.OverlapError
        Given central wavelength is not within the given bins
        or the wavelength range would exceed the bin limits.

    synphot.exceptions.SynphotError
        Invalid inputs or calculation failed.

    """
    mode = mode.lower()

    if mode not in ('round', 'min', 'max', 'none'):
        raise exceptions.SynphotError(
            'mode={0} is invalid, must be "round", "min", "max", '
            'or "none".'.format(mode))

    if not isinstance(npix, six.integer_types):
        raise exceptions.SynphotError('npix={0} is invalid.'.format(npix))

    # Bin values must be in ascending order.
    if bins[0] > bins[-1]:
        bins = bins[::-1]

    # Central wavelength must be within given bins.
    if cenwave < bins[0] or cenwave > bins[-1]:
        raise exceptions.OverlapError(
            'cenwave={0} is not within binset (min={1}, max={2}).'.format(
                cenwave, bins[0], bins[-1]))

    # Find the index the central wavelength among bins
    diff = cenwave - bins
    ind = np.argmin(np.abs(diff))

    # Calculate fractional index
    frac_ind = float(ind)
    if diff[ind] < 0:
        frac_ind += diff[ind] / (bins[ind] - bins[ind - 1])
    elif diff[ind] > 0:
        frac_ind += diff[ind] / (bins[ind + 1] - bins[ind])

    # Calculate fractional indices of the edges
    half_npix = npix / 2.0
    frac_ind1 = frac_ind - half_npix
    frac_ind2 = frac_ind + half_npix

    # Calculated edges must not exceed bin edges
    if frac_ind1 < -0.5:
        raise exceptions.OverlapError(
            'Lower limit of wavelength range is out of bounds.')
    if frac_ind2 > (bins.size - 0.5):
        raise exceptions.OverlapError(
            'Upper limit of wavelength range is out of bounds.')

    frac1, int1 = np.modf(frac_ind1)
    frac2, int2 = np.modf(frac_ind2)
    int1 = int(int1)
    int2 = int(int2)

    if mode == 'round':
        # Lower end of wavelength range
        if frac1 >= 0:
            # end is somewhere greater than binset[0] so we can just
            # interpolate between two neighboring values going with upper edge
            wave1 = bins[int1:int1 + 2].mean()
        else:
            # end is below the lowest binset value, but not by enough to
            # trigger an exception
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # Upper end of wavelength range
        if int2 < bins.shape[0] - 1:
            # end is somewhere below binset[-1] so we can just interpolate
            # between two neighboring values, going with the upper edge.
            wave2 = bins[int2:int2 + 2].mean()
        else:
            # end is above highest binset value but not by enough to
            # trigger an exception
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    elif mode == 'min':
        # Lower end of wavelength range
        if frac1 <= 0.5 and int1 < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[int1:int1 + 2].mean()
        elif frac1 > 0.5 and int1 < bins.shape[0] - 2:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[int1 + 1:int1 + 3].mean()
        elif frac1 == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])
        else:  # pragma: no cover
            raise exceptions.SynphotError(
                'mode={0} gets unexpected frac1={1}, int1={2}'.format(
                    mode, frac1, int1))

        # Upper end of wavelength range
        if frac2 >= 0.5 and int2 < bins.shape[0] - 1:
            # not out at the end and pixel i included
            wave2 = bins[int2:int2 + 2].mean()
        elif frac2 < 0.5 and int2 < bins.shape[0]:
            # not out at end and pixel i not included
            wave2 = bins[int2 - 1:int2 + 1].mean()
        elif frac2 == 0.5 and int2 == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())
        else:  # pragma: no cover
            raise exceptions.SynphotError(
                'mode={0} gets unexpected frac2={1}, int2={2}'.format(
                    mode, frac2, int2))

    elif mode == 'max':
        # Lower end of wavelength range
        if frac1 < 0.5 and int1 < bins.shape[0]:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[int1 - 1:int1 + 1].mean()
        elif frac1 >= 0.5 and int1 < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[int1:int1 + 2].mean()
        elif frac1 == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])
        else:  # pragma: no cover
            raise exceptions.SynphotError(
                'mode={0} gets unexpected frac1={1}, int1={2}'.format(
                    mode, frac1, int1))

        # Upper end of wavelength range
        if frac2 > 0.5 and int2 < bins.shape[0] - 2:
            # not out at the end and pixel i included
            wave2 = bins[int2 + 1:int2 + 3].mean()
        elif frac2 <= 0.5 and int2 < bins.shape[0] - 1:
            # not out at end and pixel i not included
            wave2 = bins[int2:int2 + 2].mean()
        elif frac2 == 0.5 and int2 == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())
        else:  # pragma: no cover
            raise exceptions.SynphotError(
                'mode={0} gets unexpected frac2={1}, int2={2}'.format(
                    mode, frac2, int2))

    else:  # mode == 'none'
        wave1 = bins[int1] + frac1 * (bins[int1 + 1] - bins[int1])
        wave2 = bins[int2] + frac2 * (bins[int2 + 1] - bins[int2])

    return wave1, wave2


def pixel_range(bins, waverange, mode='round'):
    """Calculate the number of pixels within the given wavelength range
    and the given bins.

    Parameters
    ----------
    bins : array-like
        Wavelengths at bin centers, each centered on a pixel.
        Must be 1D array.

    waverange : tuple of float
        Lower and upper limits of the desired wavelength range,
        in the same unit as ``bins``.

    mode : {'round', 'min', 'max', 'none'}
        Determines how the pixels at the edges of the wavelength range
        are handled. All the options, except 'none', will return
        an integer number of pixels:

            * 'round' - Wavelength range edges that fall in the middle
              of a pixel are counted if more than half of the pixel is
              within the given wavelength range. Edges that fall in
              the center of a pixel are rounded to the nearest pixel
              edge. This is the default.

            * 'min' - Only pixels wholly within the given wavelength
              range are counted.

            * 'max' - Pixels that are within the given wavelength range
              by any margin are counted.

            * 'none' - The exact number of encompassed pixels,
              including fractional pixels, is returned.

    Returns
    -------
    npix : number
        Number of pixels.

    Raises
    ------
    synphot.exceptions.OverlapError
        Given wavelength range exceeds the bounds of given bins.

    synphot.exceptions.SynphotError
        Invalid mode.

    """
    mode = mode.lower()

    if mode not in ('round', 'min', 'max', 'none'):
        raise exceptions.SynphotError(
            'mode={0} is invalid, must be "round", "min", "max", '
            'or "none".'.format(mode))

    if waverange[0] < waverange[-1]:
        wave1 = waverange[0]
        wave2 = waverange[-1]
    else:
        wave1 = waverange[-1]
        wave2 = waverange[0]

    # Bin values must be in ascending order.
    if bins[0] > bins[-1]:
        bins = bins[::-1]

    # Wavelength range must be within bins
    minwave = bins[0] - (bins[0:2].mean() - bins[0])
    maxwave = bins[-1] + (bins[-1] - bins[-2:].mean())
    if wave1 < minwave or wave2 > maxwave:
        raise exceptions.OverlapError(
            'Wavelength range ({0}, {1}) is out of bounds of bins '
            '(min={2}, max={3}).'.format(wave1, wave2, minwave, maxwave))

    if wave1 == wave2:
        return 0

    if mode == 'round':
        ind1 = bins.searchsorted(wave1, side='right')
        ind2 = bins.searchsorted(wave2, side='right')
    else:
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

    if mode == 'round':
        npix = ind2 - ind1

    elif mode == 'min':
        # for ind1, figure out if pixel ind1 is wholly included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (bins[ind1] - wave1) / (bins[ind1] - bins[ind1 - 1])
        if frac < 0.5:
            # ind1 is only partially included
            ind1 += 1

        # similar but reversed procedure for ind2
        frac = (wave2 - bins[ind2 - 1]) / (bins[ind2] - bins[ind2 - 1])
        if frac < 0.5:
            # ind2 is only partially included
            ind2 -= 1

        npix = ind2 - ind1

    elif mode == 'max':
        # for ind1, figure out if pixel ind1-1 is partially included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (wave1 - bins[ind1 - 1]) / (bins[ind1] - bins[ind1 - 1])
        if frac < 0.5:
            # ind1 is partially included
            ind1 -= 1

        # similar but reversed procedure for ind2
        frac = (bins[ind2] - wave2) / (bins[ind2] - bins[ind2 - 1])
        if frac < 0.5:
            # ind2 is partially included
            ind2 += 1

        npix = ind2 - ind1

    else:  # mode == 'none'
        # calculate fractional indices
        frac1 = ind1 - (bins[ind1] - wave1) / (bins[ind1] - bins[ind1 - 1])
        frac2 = ind2 - (bins[ind2] - wave2) / (bins[ind2] - bins[ind2 - 1])
        npix = frac2 - frac1

    return npix
