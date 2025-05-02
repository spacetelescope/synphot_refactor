"""Module to handle backward-compatibility for ``specutils``.

Since ``specutils`` is an optional, dependency, this module
should only be imported under the condition where ``specutils``
is already installed separately; otherwise, you will encounter
``ImportError``.

This module should no longer be necessary once this package
requires ``specutils`` 2.0 or later.

"""
import specutils
from astropy.utils import minversion

__all__ = []

SPECUTILS_LT_2 = not minversion(specutils, "2.0.dev")

if SPECUTILS_LT_2:
    from specutils import Spectrum1D as Spectrum
else:
    from specutils import Spectrum  # noqa: F401
