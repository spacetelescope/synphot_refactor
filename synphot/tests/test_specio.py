# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test specio.py module."""
from __future__ import absolute_import, division, print_function, unicode_literals

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.io import fits
from astropy.tests.helper import pytest, remote_data
from astropy.utils.data import get_pkg_data_filename, _find_pkg_data_path

# LOCAL
from .. import exceptions, specio, units


class TestGetLatestFile(object):
    """Test getting latest file."""
    def setup_class(self):
        self.datadir = _find_pkg_data_path('data')

    @remote_data
    def test_ftp(self):
        """Remote FTP path."""
        template = 'ftp://ftp.stsci.edu/cdbs/mtab/n*tmg.fits'
        ans = 'ftp://ftp.stsci.edu/cdbs/mtab/n9i1408hm_tmg.fits'
        filename = specio.get_latest_file(template, raise_error=True)
        assert filename == ans

    def test_local(self):
        """Local data path."""
        template = os.path.join(self.datadir, 'hst_acs_hrc_*.fits')
        ans = os.path.join(self.datadir, 'hst_acs_hrc_f555w_x_grw70d5824.fits')
        filename = specio.get_latest_file(template, raise_error=True)
        assert filename == ans

    def test_bogus(self):
        """Bogus data path."""
        filename = specio.get_latest_file(
            os.path.join('foo', 'foo', 'hst_acs_hrc_*.fits'))
        assert filename == ''

    def test_no_files(self):
        """Real path with no files."""
        template = os.path.join(self.datadir, '*dummy')

        # Warning only
        filename = specio.get_latest_file(template)
        assert filename == ''

        # Raise error
        with pytest.raises(IOError):
            filename = specio.get_latest_file(template, raise_error=True)


@remote_data
def test_read_remote_spec():
    """Test read remote spectrum.

    .. note:: This is just I/O test. No check on data quality.

    """
    from .. import config

    specfile = config.VEGA_FILE()
    hdr, wave, flux = specio.read_remote_spec(
        specfile, cache=False, show_progress=False, encoding='binary')

    assert isinstance(wave, u.Quantity)
    assert isinstance(flux, u.Quantity)
    assert isinstance(hdr, dict)


def test_read_ascii_spec():
    """Test read local ASCII spectrum."""
    specfile = get_pkg_data_filename(
        os.path.join('data', 'dummy_ascii_spec.txt'))
    hdr, wave, flux = specio.read_spec(specfile)

    np.testing.assert_array_equal(
        wave.value, [999.9, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 7000.1])
    np.testing.assert_array_equal(
        flux.value, [0.0, 0.5, 1.1, 2.3, 4.5, 3.2, 1.6, 0.4, 0.0])
    assert wave.unit == u.AA
    assert flux.unit == units.FLAM
    assert hdr == {}


class TestReadWriteFITS(object):
    """Test read/write FITS spectrum."""
    def setup_class(self):
        self.epsilon = 0.00031
        self.outdir = tempfile.mkdtemp()
        self.wave = u.Quantity(
            [1000.0, 2000.0, 2000.0 + self.epsilon, 3000.0, 4000.0, 5000.0],
            unit=u.AA, dtype=np.float64)
        self.flux = u.Quantity(
            [0.1, 100.2, 10.0, 0.0, 6.5, 1.2],
            unit=units.PHOTLAM, dtype=np.float64)
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
            wave.value, [1000.0, 2000.0 + self.epsilon, 3000.0, 4000.0, 5000.0],
            rtol=1e-06)
        np.testing.assert_allclose(flux.value, [0.1, 10.0, 0.0, 6.5, 1.2])
        assert wave.unit == self.wave.unit
        assert flux.unit == self.flux.unit

        # Compare primary header
        assert hdr['PEDIGREE'] == 'DUMMY'

        # Compare science header
        assert fits.getval(outfile, 'SPEC_SRC', ext=1) == 'RANDOM'

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
        assert fits.getval(outfile, 'SPEC_SRC', ext=1) == 'RANDOM'

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
                outfile, self.wave, self.flux, precision='foo', clobber=True)

        # Invalid wavelength precision
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, np.arange(6), self.flux, clobber=True)

        # Invalid flux precision
        with pytest.raises(exceptions.SynphotError):
            specio.write_fits_spec(
                outfile, self.wave, np.arange(6), clobber=True)

    def teardown_class(self):
        shutil.rmtree(self.outdir)
