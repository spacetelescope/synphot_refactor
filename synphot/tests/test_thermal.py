# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test thermal.py module."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
import astropy
from astropy import units as u
from astropy.utils import minversion
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import exceptions
from ..thermal import ThermalSpectralElement

try:
    import scipy
except ImportError:
    HAS_SCIPY = False
else:
    HAS_SCIPY = True

HAS_SCIPY = HAS_SCIPY and minversion(scipy, '0.14')
ASTROPY_LT_20 = not minversion(astropy, '2.0')


def setup_module(module):
    # https://github.com/astropy/astropy/issues/6383
    if not ASTROPY_LT_20:
        import astropy.constants as const
        from astropy.constants import si, astropyconst13

        const.sigma_sb = si.sigma_sb = astropyconst13.sigma_sb
        const.h = si.h = astropyconst13.h
        const.k_B = si.k_B = astropyconst13.k_B


def teardown_module(module):
    # https://github.com/astropy/astropy/issues/6383
    if not ASTROPY_LT_20:
        import astropy.constants as const
        from astropy.constants import si, astropyconst20
        const.sigma_sb = si.sigma_sb = astropyconst20.sigma_sb
        const.h = si.h = astropyconst20.h
        const.k_B = si.k_B = astropyconst20.k_B


@pytest.mark.skipif('not HAS_SCIPY')
class TestThermalSpectralElement(object):
    """Test ``ThermalSpectralElement``."""
    def setup_class(self):
        thfile = get_pkg_data_filename(
            os.path.join('data', 'wfc3_ir_g141_src_003_th.fits'))
        self.th = ThermalSpectralElement.from_file(thfile)

    def test_taper(self):
        with pytest.raises(NotImplementedError):
            self.th.taper()

    def test_properties(self):
        assert self.th.temperature == 237.3 * u.K
        assert self.th.beam_fill_factor == 1

    def test_thermal_source(self):
        sp = self.th.thermal_source()
        assert sp.meta['temperature'] == self.th.temperature
        assert sp.meta['beam_fill_factor'] == self.th.beam_fill_factor
        np.testing.assert_allclose(
            sp([6800, 7800, 8800, 17920, 18920, 19920]).value,
            [1.246735e-30, 6.63655885e-26, 2.80933935e-22, 2.76427032e-08,
             1.33011769e-07, 5.40857951e-07], rtol=1e-5)

    def test_from_file_exceptions(self):
        # Non-FITS file
        with pytest.raises(exceptions.SynphotError):
            ThermalSpectralElement.from_file('dummy.txt')

        # Missing DEFT keyword
        thfile = get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f555w.fits'))
        with pytest.raises(exceptions.SynphotError):
            ThermalSpectralElement.from_file(thfile, flux_col='THROUGHPUT')
