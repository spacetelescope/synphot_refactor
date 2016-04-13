# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test reddening.py module."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

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
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import exceptions, units
from ..models import ConstFlux1D, Empirical1D
from ..reddening import ReddeningLaw, ExtinctionCurve
from ..spectrum import SourceSpectrum


class TestExtinction(object):
    """Test ReddeningLaw and ExtinctionCurve classes (most methods)."""
    def setup_class(self):
        rfile = get_pkg_data_filename(
            os.path.join('data', 'milkyway_diffuse_001.fits'))
        self.redlaw = ReddeningLaw.from_file(rfile)
        self.extcurve = self.redlaw.extinction_curve(0.3 * u.mag)

    def test_invalid_ebv(self):
        with pytest.raises(exceptions.SynphotError):
            extcurve = self.redlaw.extinction_curve(1 * units.FLAM)

    def test_redlaw_call(self):
        w = self.redlaw.waveset[48:53]
        np.testing.assert_allclose(
            w.to(u.micron ** -1, u.spectral()).value,
            [5.03399992, 5.12949991, 5.2249999, 5.3204999, 5.41599989])
        np.testing.assert_allclose(
            self.redlaw(w).value,
            [8.69231796, 8.40150452, 8.17892265, 8.01734924, 7.90572977])

    def test_extcurve_call(self):
        w = self.extcurve.waveset
        y = self.extcurve(w)
        np.testing.assert_array_equal(w, self.redlaw.waveset)
        np.testing.assert_allclose(y, 10 ** (-0.4 * self.redlaw(w) * 0.3))

    def test_mul_spec(self):
        """Apply extinction curve in inverse micron to flat spectrum in
        Angstrom.

        """
        sp = SourceSpectrum(ConstFlux1D, amplitude=1)
        sp2 = self.extcurve * sp
        w = u.Quantity(5.03399992, u.micron ** -1)
        ans = self.extcurve(w).value
        np.testing.assert_allclose(sp2(w).value, ans, rtol=1e-6)


@remote_data
@pytest.mark.parametrize(
    'modelname',
    ['lmc30dor', 'lmcavg', 'mwavg', 'mwdense', 'mwrv21', 'mwrv40',
     'smcbar', 'xgalsb'])
def test_redlaw_from_model(modelname):
    """Test ReddeningLaw from remote file.

    .. note:: No check on data quality as it is dependent on data file.

    """
    redlaw = ReddeningLaw.from_extinction_model(modelname, encoding='binary')
    assert modelname in redlaw.metadata['expr']
    assert 'filename' in redlaw.metadata
    assert 'descrip' in redlaw.metadata


def test_redlaw_from_model_exception():
    with pytest.raises(exceptions.SynphotError):
        redlaw = ReddeningLaw.from_extinction_model('foo')


class TestWriteReddeningLaw(object):
    """Test ReddeningLaw ``to_fits()`` method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.x = np.linspace(1000, 5000, 5)
        self.y = np.linspace(1, 5, 5) * 0.1
        self.redlaw = ReddeningLaw(Empirical1D, x=self.x, y=self.y)

    @pytest.mark.parametrize('ext_hdr', [None, {'foo': 'foo'}])
    def test_write(self, ext_hdr):
        outfile = os.path.join(self.outdir, 'outredlaw.fits')

        if ext_hdr is None:
            self.redlaw.to_fits(outfile, clobber=True)
        else:
            self.redlaw.to_fits(outfile, clobber=True, ext_header=ext_hdr)

        # Read it back in and check
        redlaw2 = ReddeningLaw.from_file(outfile)
        np.testing.assert_allclose(redlaw2.waveset.value, self.x)
        np.testing.assert_allclose(redlaw2(self.x).value, self.y)

        if ext_hdr is not None:
            hdr = fits.getheader(outfile, 1)
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
