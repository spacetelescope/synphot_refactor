# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test specio.py module."""
from __future__ import absolute_import, division, print_function

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u
from astropy.io import fits
from astropy.tests.helper import remote_data
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import exceptions, specio, units


@remote_data
def test_read_remote_spec():
    """Test read remote spectrum.

    .. note:: This is just I/O test. No check on data quality.

    """
    from .. import config

    hdr, wave, flux = specio.read_remote_spec(
        config.conf.vega_file, cache=False, show_progress=False)

    assert isinstance(wave, u.Quantity)
    assert isinstance(flux, u.Quantity)
    assert isinstance(hdr, dict)


def test_read_ascii_spec():
    """Test read local ASCII spectrum."""
    specfile = get_pkg_data_filename(
        os.path.join('data', 'qso_fos_001.dat'))
    hdr, wave, flux = specio.read_spec(specfile)

    np.testing.assert_array_equal(
        wave.value[::1000],
        [100.0, 610.8, 910.8, 1210.8, 1510.8, 1810.8, 2110.8, 2410.8, 2710.8,
         3010.8, 3310.8])
    np.testing.assert_array_equal(
        flux.value[::1000],
        [1.5e-13, 2.40258e-13, 2.24e-13, 7.49e-13, 1.97e-13, 1.41e-13,
         1.17e-13, 1.1e-13, 9.07e-14, 8.47173e-14, 8.10268e-14])
    assert wave.unit == u.AA
    assert flux.unit == units.FLAM
    assert hdr == {}


class TestReadWriteFITS(object):
    """Test read/write FITS spectrum."""
    def setup_class(self):
        self.epsilon = 0.00031
        self.outdir = tempfile.mkdtemp()
        self.wave = np.array([1000.0, 2000.0, 2000.0 + self.epsilon, 3000.0,
                              4000.0, 5000.0], dtype=np.float64) * u.AA
        self.flux = np.array([0.1, 100.2, 10.0, 0.0, 6.5, 1.2],
                             dtype=np.float64) * units.PHOTLAM
        self.prihdr = {'PEDIGREE': 'DUMMY'}
        self.scihdr = {'SPEC_SRC': 'RANDOM'}

    def test_array_data(self):
        """Data as Numpy array."""
        outfile = os.path.join(self.outdir, 'outspec1.fits')

        # Write it out
        specio.write_fits_spec(
            outfile, self.wave.value, self.flux.value, pri_header=self.prihdr,
            ext_header=self.scihdr, trim_zero=False, pad_zero_ends=False,
            precision='single', wave_unit=self.wave.unit,
            flux_unit=self.flux.unit)

        # Read it back in and check values (flux_unit should be ignored)
        hdr, wave, flux = specio.read_spec(outfile, flux_unit='foo')

        # Compare data
        np.testing.assert_allclose(
            wave.value,
            [1000.0, 2000.0 + self.epsilon, 3000.0, 4000.0, 5000.0],
            rtol=1e-06)
        np.testing.assert_allclose(flux.value, [0.1, 10.0, 0.0, 6.5, 1.2])
        assert wave.unit == self.wave.unit
        assert flux.unit == self.flux.unit

        # Compare primary header
        assert hdr['PEDIGREE'] == 'DUMMY'

        # Compare science header
        sci_hdr = fits.getheader(outfile, 1)
        assert sci_hdr['SPEC_SRC'] == 'RANDOM'
        assert sci_hdr['TFORM2'].lower() == 'e'

    def test_quantity_data(self):
        """Data as Quantity."""
        outfile = os.path.join(self.outdir, 'outspec2.fits')

        # Write it out (flux_unit should be ignored)
        specio.write_fits_spec(
            outfile, self.wave, self.flux, pri_header=self.prihdr,
            ext_header=self.scihdr, precision='double', flux_unit='foo')

        # Read it back in and check values (flux_unit should be ignored)
        hdr, wave, flux = specio.read_spec(outfile, flux_unit='foo')

        # Compare data (trim_zero=True, pad_zero_ends=True)
        np.testing.assert_allclose(
            wave.value, [500.0, 1000.0, 2000.0, 2000.0 + self.epsilon, 4000.0,
                         5000.0, 6250.0],
            rtol=1e-06)
        np.testing.assert_allclose(
            flux.value, [0.0, 0.1, 100.2, 10.0, 6.5, 1.2, 0.0])
        assert wave.unit == self.wave.unit
        assert flux.unit == self.flux.unit

        # Compare primary header
        assert hdr['PEDIGREE'] == 'DUMMY'

        # Compare science header
        sci_hdr = fits.getheader(outfile, 1)
        assert sci_hdr['SPEC_SRC'] == 'RANDOM'
        assert sci_hdr['TFORM2'].lower() == 'd'

    def test_exceptions(self):
        """Test for appropriate exceptions."""
        outfile = os.path.join(self.outdir, 'outspec3.fits')

        # Shape mismatch
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, self.wave, np.arange(3, dtype=np.float64))

        # Invalid precision keyword
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, self.wave, self.flux, precision='foo', overwrite=True)

        # Invalid wavelength precision
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, np.arange(6), self.flux, overwrite=True)

        # Invalid flux precision
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, self.wave, np.arange(6), overwrite=True)

    def teardown_class(self):
        shutil.rmtree(self.outdir)
