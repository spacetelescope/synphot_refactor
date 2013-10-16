# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test planck.py module.

.. note:: ``bb_photlam()`` is tested in test_spectrum.py

"""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u

# LOCAL
from .. import planck, utils, units


__doctest_skip__ = ['*']


def test_bb_photlam_arsec():
    """Test ``bb_photlam_arsec()``.

    .. note:: ``bbfunc()`` is called indirectly.

    """
    wave = utils.generate_wavelengths()[0]
    flux = planck.bb_photlam_arcsec(wave, 1000.0)
    np.testing.assert_allclose(flux.value[5000], 3.89141e-08, rtol=2.5e-3)
    assert flux.unit == units.PHOTLAM / u.arcsec ** 2
