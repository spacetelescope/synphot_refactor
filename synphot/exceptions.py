# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Exceptions specific to synthetic photometry."""

__all__ = [
    "DisjointError",
    "DuplicateWavelength",
    "ExtrapolationNotAllowed",
    "IncompatibleSources",
    "InterpolationNotAllowed",
    "OverlapError",
    "PartialOverlap",
    "SynphotError",
    "TableFormatError",
    "UndefinedBinset",
    "UnsortedWavelength",
    "ZeroWavelength",
]


class SynphotError(Exception):
    """Base class for synphot exceptions."""


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
        super().__init__(msg)

        # Save rows with wrong values as an attribute so calling code
        # can access it directly
        self.rows = rows

        # Also make this info go into the visibly displayed message in
        # Python 2.7 (self.args) and Python 2.5/6 (self.message)
        args = list(self.args)
        args.append(f"Invalid entries at or about row: {rows}")

        self.args = tuple(args)
        self.message = self.args


class DuplicateWavelength(TableFormatError):
    """Duplicate wavelengths are not allowed in table."""


class ZeroWavelength(TableFormatError):
    """Zero wavelengths are not allowed in table."""


class UnsortedWavelength(TableFormatError):
    """Unsorted wavelengths are not allowed in table."""


class OverlapError(SynphotError):
    """Exceptions to do with overlap checking."""


class PartialOverlap(OverlapError):
    """Partial overlap is not allowed."""


class DisjointError(OverlapError):
    """Disjoint data is not allowed."""


class UndefinedBinset(SynphotError):
    """Exceptions for undefined bin set."""


class IncompatibleSources(SynphotError):
    """Two sources in composite spectrum are not compatible."""


class InterpolationNotAllowed(SynphotError):
    """Exceptions for interpolation."""


class ExtrapolationNotAllowed(SynphotError):
    """Exceptions for extrapolation."""
