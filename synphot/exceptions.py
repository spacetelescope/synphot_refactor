# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Exceptions specific to synthetic photometry."""
from __future__ import absolute_import, division, print_function

__all__ = ['SynphotError', 'TableFormatError', 'DuplicateWavelength',
           'ZeroWavelength', 'UnsortedWavelength', 'OverlapError',
           'PartialOverlap', 'DisjointError', 'UndefinedBinset',
           'IncompatibleSources', 'InterpolationNotAllowed',
           'ExtrapolationNotAllowed']


class SynphotError(Exception):
    """Base class for synphot exceptions."""
    pass


class TableFormatError(SynphotError):
    """Exceptions to do with table access.

    Parameters
    ----------
    msg : str
        Error message.

    rows : list of int, optional
        Row numbers where exception occured.

    """
    def __init__(self, msg, rows=None):
        super(TableFormatError, self).__init__(msg)

        # Save rows with wrong values as an attribute so calling code
        # can access it directly
        self.rows = rows

        # Also make this info go into the visibly displayed message in
        # Python 2.7 (self.args) and Python 2.5/6 (self.message)
        args = list(self.args)
        args.append('Invalid entries at or about row: {0}'.format(rows))

        self.args = tuple(args)
        self.message = self.args


class DuplicateWavelength(TableFormatError):
    """Duplicate wavelengths are not allowed in table."""
    pass


class ZeroWavelength(TableFormatError):
    """Zero wavelengths are not allowed in table."""
    pass


class UnsortedWavelength(TableFormatError):
    """Unsorted wavelengths are not allowed in table."""
    pass


class OverlapError(SynphotError):
    """Exceptions to do with overlap checking."""
    pass


class PartialOverlap(OverlapError):
    """Partial overlap is not allowed."""
    pass


class DisjointError(OverlapError):
    """Disjoint data is not allowed."""
    pass


class UndefinedBinset(SynphotError):
    """Exceptions for undefined bin set."""
    pass


class IncompatibleSources(SynphotError):
    """Two sources in composite spectrum are not compatible."""
    pass


class InterpolationNotAllowed(SynphotError):
    """Exceptions for interpolation."""
    pass


class ExtrapolationNotAllowed(SynphotError):
    """Exceptions for extrapolation."""
    pass
