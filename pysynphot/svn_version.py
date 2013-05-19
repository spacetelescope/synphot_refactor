# Licensed under a 3-clause BSD style license - see LICENSE.rst

# For backwards compatibility with py_etc
try:
    from .version import *
    __svn_version__ = __svn_revision__
    __full_svn_info__ = __svn_full_info__
except ImportError as e:
    __svn_version__ = ''
    __full_svn_info__ = ''
