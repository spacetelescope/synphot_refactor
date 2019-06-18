# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Module to handle backward-compatibility."""

import astropy
from astropy.utils.introspection import minversion

__all__ = ['ASTROPY_LT_2_0', 'ASTROPY_LT_4_0']

ASTROPY_LT_2_0 = not minversion(astropy, '2.0')
ASTROPY_LT_4_0 = not minversion(astropy, '4.0')
