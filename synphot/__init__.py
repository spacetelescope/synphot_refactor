# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This is an Astropy affiliated package.
"""
try:
    from .version import version as __version__
except ImportError:
    __version__ = ''

# SYNPHOT UI
from .config import conf  # noqa
from .utils import generate_wavelengths  # noqa
from .models import *  # noqa
from .observation import *  # noqa
from .reddening import *  # noqa
from .thermal import *  # noqa
from .spectrum import SourceSpectrum, SpectralElement, BaseUnitlessSpectrum  # noqa
