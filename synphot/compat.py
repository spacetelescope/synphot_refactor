# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Module to handle backward-compatibility."""

import astropy
from astropy.utils.introspection import minversion

try:
    import specutils  # noqa
except ImportError:
    HAS_SPECUTILS = False
else:
    HAS_SPECUTILS = True

__all__ = ['ASTROPY_LT_4_0', 'HAS_SPECUTILS']

ASTROPY_LT_4_0 = not minversion(astropy, '4.0')
