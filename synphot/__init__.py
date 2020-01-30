# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This is an Astropy affiliated package.
"""

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *  # noqa
# ----------------------------------------------------------------------------

# SYNPHOT UI
from .config import conf  # noqa
from .utils import generate_wavelengths  # noqa
from .models import *  # noqa
from .observation import *  # noqa
from .reddening import *  # noqa
from .thermal import *  # noqa
from .spectrum import SourceSpectrum, SpectralElement, BaseUnitlessSpectrum  # noqa
