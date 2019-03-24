# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test utils.py module."""
from __future__ import absolute_import, division, print_function
from ..extern import six

# STDLIB
import os

# THIRD PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u

# LOCAL
from .. import exceptions, utils


@pytest.mark.parametrize(
    ('a', 'b', 'ans'),
    [(np.arange(5, 8), np.arange(10), 'full'),
     (np.arange(10), np.arange(5, 8), 'partial'),
     (np.arange(3), np.arange(2, 5), 'partial'),
     (np.arange(4, 8), np.arange(2, 5), 'partial'),
     (np.arange(3), np.arange(3, 6), 'none'),
     (np.arange(3, 6), np.arange(3), 'none')])
def test_overlap_status(a, b, ans):
    """Test overlap status validation."""
    assert utils.overlap_status(a, b) == ans


def test_validate_totalflux():
    """Test integrated flux validation."""
    # Valid integrated flux
    utils.validate_totalflux(0.01)

    # Invalid integrated flux
    with pytest.raises(exceptions.SynphotError):
        utils.validate_totalflux(-0.01)
    with pytest.raises(exceptions.SynphotError):
        utils.validate_totalflux(0)
    with pytest.raises(exceptions.SynphotError):
        utils.validate_totalflux(np.inf)
    with pytest.raises(exceptions.SynphotError):
        utils.validate_totalflux(np.nan)


def test_validate_wavelengths():
    """Test wavelengths validation."""
    # Valid wavelengths (ascending)
    a = np.arange(1, 11)
    utils.validate_wavelengths(a)

    # Valid wavelengths (descending)
    a = a[::-1]
    utils.validate_wavelengths(a * u.micron)

    # Invalid wavelengths
    with pytest.raises(exceptions.SynphotError):
        utils.validate_wavelengths(1.0 * u.K)
    with pytest.raises(exceptions.ZeroWavelength):
        utils.validate_wavelengths(np.arange(10))
    with pytest.raises(exceptions.UnsortedWavelength):
        utils.validate_wavelengths([1000, 1002, 1001, 1003, 1004])

    try:
        utils.validate_wavelengths([1000, 1001, 1002, 1003, 1003])
    except exceptions.DuplicateWavelength as e:
        np.testing.assert_array_equal(e.rows, 3)


@pytest.mark.parametrize(
    ('num', 'delta', 'log', 'ans'),
    [(10, None, True, [10.0, 10.71773463, 11.48698355, 12.31144413,
                       13.19507911, 14.14213562, 15.15716567, 16.24504793,
                       17.41101127, 18.66065983]),
     (0, 0.05, True, [10.0, 11.22018454, 12.58925412, 14.12537545, 15.84893192,
                      17.7827941, 19.95262315]),
     (10, None, False, np.arange(10, 20)),
     (0, 1.0, False, np.arange(10, 20))])
def test_genwave(num, delta, log, ans):
    """Test wavelength generation."""
    wave, wave_str = utils.generate_wavelengths(
        minwave=10, maxwave=20, num=num, delta=delta, log=log,
        wave_unit=u.micron)
    np.testing.assert_allclose(wave.value, ans)
    assert wave.unit == u.micron
    assert isinstance(wave_str, six.string_types)


class TestMergeWave(object):
    """Test wavelengths merging."""
    def setup_class(self):
        self.thres = 1e-12
        self.wave = [5000.0, 5000.01, 5000.02, 5000.03, 5000.04, 6000.0]

    def test_merge_none(self):
        assert utils.merge_wavelengths(None, None) is None
        np.testing.assert_array_equal(
            utils.merge_wavelengths(None, self.wave), self.wave)
        np.testing.assert_array_equal(
            utils.merge_wavelengths(self.wave, None), self.wave)

    def test_merge_thres(self):
        w = [5000.005, 5000.02 + self.thres, 5500.0, 6000.0]
        ans = [5000.0, 5000.005, 5000.01, 5000.02, 5000.03, 5000.04, 5500.0,
               6000.0]
        wave = utils.merge_wavelengths(self.wave, w, threshold=self.thres)
        dw = wave[1:] - wave[:-1]
        np.testing.assert_allclose(wave, ans)
        assert np.all(dw > self.thres)

    def test_merge_same(self):
        wave = utils.merge_wavelengths(self.wave, self.wave)
        np.testing.assert_array_equal(wave, self.wave)


def test_download_bad_root(tmpdir):
    """Test data download helper when input dir is invalid."""
    ptr = tmpdir.join('bad_cdbs')
    ptr.write('content')
    cdbs_root = str(ptr)

    with pytest.raises(OSError):
        utils.download_data(cdbs_root, verbose=False)


def test_download_data(tmpdir):
    """Test data download helper in dry run mode."""
    from ..config import conf

    # Use case where user downloads all data into new dir.
    cdbs_root = os.path.join(tmpdir.strpath, 'cdbs')
    file_list_1 = utils.download_data(cdbs_root, verbose=False, dry_run=True)
    filename = file_list_1[0]
    assert len(file_list_1) == 21
    assert filename.startswith(cdbs_root)
    assert os.path.isdir(os.path.join(cdbs_root, 'calspec'))

    # Make dummy files for the next step.
    for fname in file_list_1:
        with open(fname, 'w') as f:
            f.write('\n')

    # Use case where user downloads only some data into existing dir.
    os.remove(filename)
    file_list_2 = utils.download_data(cdbs_root, verbose=False, dry_run=True)
    assert len(file_list_2) == 1 and file_list_2[0] == filename

    # Re-create the deleted dummy file for next step.
    with open(filename, 'w') as f:
        f.write('\n')

    # Use case where user redefined data file to be non-STScI.
    filename = [fname for fname in file_list_1
                if fname.endswith('alpha_lyr_stis_008.fits')][0]
    os.remove(filename)
    with conf.set_temp('vega_file', '/custom/host/my_vega.fits'):
        file_list_2 = utils.download_data(
            cdbs_root, verbose=False, dry_run=True)
    assert len(file_list_2) == 0
