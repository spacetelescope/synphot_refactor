# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test synphot version."""
from __future__ import division, print_function

# LOCAL
from synphot import __version__


__doctest_skip__ = ['*']


def test_version():
    assert '3.0.0.dev' in __version__
