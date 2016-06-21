# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""It gets to be really tedious to type long docstrings in ANSI C
syntax (since multi-line string literals are not valid).
Therefore, the docstrings are written here, which are then
converted by setup.py into include/docstrings.h, which is
included by src/synphot_utils.c.

"""
from __future__ import absolute_import, division, print_function


calcbinflux = """
calcbinflux(len_binwave, i_beg, i_end, avflux, deltaw)

Sum over each bin.

Parameters
----------
len_binwave : int
    Number of wavelength bin centers.

i_beg, i_end : array-like
    Locations of bin edges in ``deltaw``.

avflux : array-like
    Average flux associated with ``deltaw``.

deltaw : array-like
    Delta of merge wavelengths (native + centers + edges).
    Values are in ascending order.

Returns
-------
binflux : array-like
    Integrated flux associated with given bins in ascending order.

intwave : array-like
    Integrated delta wavelength associated with ``binflux``.

"""
