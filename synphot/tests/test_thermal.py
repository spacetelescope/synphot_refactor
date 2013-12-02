# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test thermal.py module."""
from __future__ import absolute_import, division, print_function, unicode_literals

# STDLIB
import os

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.tests.helper import pytest
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import exceptions, spectrum, thermal, units


class TestThermalSpectralElement(object):
    """Test ThermalSpectralElement."""
    def setup_class(self):
        thfile = get_pkg_data_filename(
            os.path.join('data', 'wfc3_ir_g141_src_003_th.fits'))
        self.th = thermal.ThermalSpectralElement.from_file(thfile)

    def test_attributes(self):
        assert isinstance(self.th, spectrum.BaseUnitlessSpectrum)
        assert self.th.metadata['expr'] == 'ThermalSpectralElement'
        assert self.th.temperature.unit == u.K
        assert self.th.temperature.value == 237.3
        assert self.th.beam_fill_factor == 1

    def test_thermal_source(self):
        sp = self.th.to_thermal_source()
        assert isinstance(sp, spectrum.SourceSpectrum)
        assert sp.metadata['temperature'] == self.th.temperature
        assert sp.metadata['beam_fill_factor'] == self.th.beam_fill_factor
        assert sp.wave.unit == u.AA
        assert sp.flux.unit == units.PHOTLAM
        np.testing.assert_allclose(
            sp.wave.value[5000::1000], [6800, 7800, 8800, 17920, 18920, 19920])
        np.testing.assert_allclose(
            sp.flux.value[5000::1000],
            [0, 6.63655885e-26, 2.80933935e-22, 2.76427032e-08, 1.33011769e-07,
             5.40857951e-07])

    def test_exceptions(self):
        # Non-FITS file
        with pytest.raises(exceptions.SynphotError):
            th = thermal.ThermalSpectralElement.from_file('dummy.txt')

        # Missing DEFT keyword
        with pytest.raises(exceptions.SynphotError):
            th = thermal.ThermalSpectralElement.from_file(
                get_pkg_data_filename(
                    os.path.join('data', 'hst_acs_hrc_f555w.fits')),
                flux_col='THROUGHPUT')
