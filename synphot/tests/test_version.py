# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test ver.py module."""
from __future__ import division, print_function

# LOCAL
from .. import ver


__doctest_skip__ = ['*']


def test_version():
    assert ver.__version__ == '3.0.0.dev'
    assert ver.__vdate__ == '2013-08-28'
