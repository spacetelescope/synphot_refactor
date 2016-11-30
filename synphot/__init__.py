# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This is an Astropy affiliated package.
"""
from __future__ import absolute_import

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    # SYNPHOT UI
    from .config import conf
    from .utils import generate_wavelengths
    from .models import *
    from .observation import *
    from .reddening import *
    from .thermal import *
    from .spectrum import SourceSpectrum, SpectralElement, BaseUnitlessSpectrum
