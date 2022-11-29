# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Module to handle backward-compatibility."""
import importlib

import astropy
from astropy.utils.introspection import minversion

_optional_deps = ['specutils', 'dust_extinction']
_deps = {k.upper(): k for k in _optional_deps}

ASTROPY_LT_5_0 = not minversion(astropy, '5.0')

__all__ = ['ASTROPY_LT_5_0'] + [f"HAS_{pkg}" for pkg in _deps]


def __getattr__(name):
    if name in __all__:
        module_name = name[4:]

        try:
            importlib.import_module(_deps[module_name])
        except (ImportError, ModuleNotFoundError):
            return False
        return True

    raise AttributeError(f"Module {__name__!r} has no attribute {name!r}.")
