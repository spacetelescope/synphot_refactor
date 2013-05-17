# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division
"""
Utilities related to wavelength bin calculations.

"""

import numpy as np


def calculate_bin_edges(centers):
    """
    Calculate the edges of wavelength bins given the centers.

    The algorithm calculates bin edges as the midpoints between bin centers
    and treats the first and last bins as symmetric about their centers.

    Parameters
    ----------
    centers : array_like
        Sequence of bin centers. Must be 1D and have at least two values.

    Returns
    -------
    edges : ndarray
        Array of bin edges. Will be 1D and have one more value
        than `centers`.

    """
    centers = np.asanyarray(centers)

    if centers.ndim != 1:
        raise ValueError('centers input array must be 1D.')

    if centers.size < 2:
        raise ValueError('centers input must have at least two values.')

    edges = np.empty(centers.size + 1)

    edges[1:-1] = (centers[1:] + centers[:-1]) / 2.

    #compute the first and last by making them symmetric
    edges[0] = centers[0] - (edges[1] - centers[0])
    edges[-1] = centers[-1] + (centers[-1] - edges[-2])

    return edges


def calculate_bin_widths(edges):
    """
    Calculate the widths of wavelengths bins given their edges.

    Parameters
    ----------
    edges : array_like
        Sequence of bin edges. Must be 1D and have at least two values.

    Returns
    -------
    widths : ndarray
        Array of bin widths. Will be 1D and have one less value than `edges`.

    """
    edges = np.asanyarray(edges)

    if edges.ndim != 1:
        raise ValueError('edges input array must be 1D.')

    if edges.size < 2:
        raise ValueError('edges input must have at least two values.')

    return edges[1:] - edges[:-1]


def calculate_bin_centers(edges):
    """
    Calculate the centers of wavelengths bins given their edges.

    Parameters
    ----------
    edges : array_like
        Sequence of bin edges. Must be 1D and have at least two values.

    Returns
    -------
    centers : ndarray
        Array of bin centers. Will be 1D and have one less value than `edges`.

    """
    edges = np.asanyarray(edges, dtype=np.float)

    if edges.ndim != 1:
        raise ValueError('edges input array must be 1D.')

    if edges.size < 2:
        raise ValueError('edges input must have at least two values.')

    centers = np.empty(edges.size - 1, dtype=np.float)

    centers[0] = edges[:2].mean()

    for i in xrange(1, centers.size):
        centers[i] = 2. * edges[i] - centers[i - 1]

    return centers
