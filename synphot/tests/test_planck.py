# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test planck.py module.

.. note:: Mostly tested in test_spectrum.py

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# THIRD-PARTY
import numpy as np

# LOCAL
from ..planck import bbfunc


def test_overflow():
    flux = bbfunc([0, 1000.0, 100000.0, 1e55], 10000.0)
    np.testing.assert_allclose(
        flux.value, [0, 3.38131732e+16, 3.87451317e+15, 0], rtol=1e-3)
