# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This is an Astropy affiliated package.
"""
# Set up the version
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = 'unknown'

# SYNPHOT UI
from .config import conf  # noqa
from .utils import generate_wavelengths  # noqa
from .models import *  # noqa
from .observation import *  # noqa
from .reddening import *  # noqa
from .thermal import *  # noqa
from .spectrum import SourceSpectrum, SpectralElement, BaseUnitlessSpectrum  # noqa
