import numpy as np
from nose.tools import raises

from pysynphot import binning


def test_calculate_bin_edges_even():
    """
    Test bin edges calculated for an evenly spaced set of centers.

    """
    centers = np.arange(10, 20, dtype=np.float)
    edges = binning.calculate_bin_edges(centers)

    ref = np.arange(9.5, 20)

    np.testing.assert_array_equal(edges, ref)


def test_calculate_bin_edges_uneven():
    """
    Test bin edges calculated for an unevenly spaced set of centers.

    """
    centers = 2.0 ** np.arange(1, 10)
    edges = binning.calculate_bin_edges(centers)

    ref = [1, 3, 6, 12, 24, 48, 96, 192, 384, 640]

    np.testing.assert_array_equal(edges, ref)


@raises(ValueError)
def test_calculate_bin_edges_raises_not_1d():
    """
    Test we get a ValueError with a non-1D array.

    """
    a = np.arange(20).reshape((4, 5))
    binning.calculate_bin_edges(a)


@raises(ValueError)
def test_calculate_bin_edges_raises_1_val():
    """
    Test we get a ValueError with a single value array.

    """
    a = np.array([5])
    binning.calculate_bin_edges(a)


def test_calculate_bin_widths():
    edges = [1, 2, 4, 10, 20]
    widths = [1, 2, 6, 10]

    np.testing.assert_array_equal(binning.calculate_bin_widths(edges), widths)


def test_calculate_bin_widths_two_val():
    """
    Test the edge case where there is only one bin.

    """
    edges = [1, 2]
    widths = [1]

    np.testing.assert_array_equal(binning.calculate_bin_widths(edges), widths)


@raises(ValueError)
def test_calculate_bin_widths_raises_not_1d():
    """
    Test we get a ValueError with a non-1D array.

    """
    a = np.arange(20).reshape((4, 5))
    binning.calculate_bin_widths(a)


@raises(ValueError)
def test_calculate_bin_widths_raises_1_val():
    """
    Test we get a ValueError with a single value array.

    """
    a = np.array([5])
    binning.calculate_bin_widths(a)


def test_calculate_bin_centers():
    edges = [1, 2, 4, 10, 20]
    centers = [1.5, 2.5, 5.5, 14.5]

    np.testing.assert_array_equal(binning.calculate_bin_centers(edges),
                                  centers)


def test_calculate_bin_centers_two_val():
    """
    Test the edge case where there is only one bin.

    """
    edges = [1, 2]
    centers = [1.5]

    np.testing.assert_array_equal(binning.calculate_bin_centers(edges),
                                  centers)


@raises(ValueError)
def test_calculate_bin_centers_raises_not_1d():
    """
    Test we get a ValueError with a non-1D array.

    """
    a = np.arange(20).reshape((4, 5))
    binning.calculate_bin_centers(a)


@raises(ValueError)
def test_calculate_bin_centers_raises_1_val():
    """
    Test we get a ValueError with a single value array.

    """
    a = np.array([5])
    binning.calculate_bin_centers(a)


def test_center_edge_center_roundtrip():
    """
    Test that we can start with centers and roundtrip to the same centers.

    """
    centers = [1, 2, 4, 10, 20]
    calc_edges = binning.calculate_bin_edges(centers)
    calc_centers = binning.calculate_bin_centers(calc_edges)

    np.testing.assert_array_equal(calc_centers, centers)
