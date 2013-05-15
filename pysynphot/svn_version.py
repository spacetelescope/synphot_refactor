# For backwards compatibility with py_etc
try:
    from .version import *
    __svn_version__ = __svn_revision__
    __full_svn_info__ = __svn_full_info__
except:
    __svn_version__ = ''
    __full_svn_info__ = ''
