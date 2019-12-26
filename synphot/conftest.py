try:
    from pytest_astropy_header.display import PYTEST_HEADER_MODULES
except ImportError:
    PYTEST_HEADER_MODULES = {}

# Uncomment the following line to treat all DeprecationWarnings as
# exceptions
from astropy.tests.helper import enable_deprecations_as_exceptions
enable_deprecations_as_exceptions()

# Uncomment and customize the following lines to add/remove entries
# from the list of packages for which version numbers are displayed
# when running the tests.
PYTEST_HEADER_MODULES['Astropy'] = 'astropy'
PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'
if 'h5py' in PYTEST_HEADER_MODULES:
    del PYTEST_HEADER_MODULES['h5py']
