# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test reddening.py module."""

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
from astropy.tests.helper import assert_quantity_allclose
from astropy.units import add_enabled_equivalencies
from astropy.utils.data import get_pkg_data_filename
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from synphot import exceptions, units
from synphot.compat import HAS_DUST_EXTINCTION  # noqa
from synphot.models import ConstFlux1D, Empirical1D
from synphot.observation import Observation
from synphot.reddening import ReddeningLaw, etau_madau
from synphot.spectrum import SourceSpectrum, SpectralElement


class TestExtinction:
    """Test ReddeningLaw and ExtinctionCurve classes (most methods)."""
    def setup_class(self):
        rfile = get_pkg_data_filename(
            os.path.join('data', 'milkyway_diffuse_001.fits'),
            package='synphot.tests')
        self.redlaw = ReddeningLaw.from_file(rfile)
        self.extcurve = self.redlaw.extinction_curve(0.3 * u.mag)

    def test_invalid_ebv(self):
        with pytest.raises(exceptions.SynphotError):
            self.redlaw.extinction_curve(1 * units.FLAM)

    def test_redlaw_call(self):
        w = self.redlaw.waveset[48:53]
        with add_enabled_equivalencies(u.spectral()):
            assert_quantity_allclose(
                w, [5.41599989, 5.3204999, 5.2249999, 5.12949991,
                    5.03399992] * (u.micron ** -1))
        assert_quantity_allclose(
            self.redlaw(w),
            [7.90572977, 8.01734924, 8.17892265, 8.40150452, 8.69231796])

    def test_extcurve_call(self):
        # Cannot use waveset.
        # See https://github.com/spacetelescope/synphot_refactor/issues/129
        w = np.squeeze(self.extcurve.model.points) * u.AA

        y = self.extcurve(w)
        np.testing.assert_array_equal(w, self.redlaw.waveset)
        np.testing.assert_allclose(y, 10 ** (-0.4 * self.redlaw(w) * 0.3))

    @pytest.mark.skipif('not HAS_DUST_EXTINCTION')
    def test_extcurve_call_2(self):
        from dust_extinction.parameter_averages import CCM89

        Av = 2
        wav = np.arange(0.1, 3, 0.001) * u.micron
        ext = CCM89(Rv=3.1)
        ans = ext.extinguish(wav, Av)

        ebv = Av / ext.Rv
        redlaw = ReddeningLaw(ext)
        extcurve = redlaw.extinction_curve(ebv, wavelengths=wav)

        assert_quantity_allclose(extcurve(wav), ans)
        assert extcurve.meta['header']['ReddeningLaw'] == '<CCM89(Rv=3.1)>'

    def test_mul_spec(self):
        """Apply extinction curve in inverse micron to flat spectrum in
        Angstrom.

        """
        sp = SourceSpectrum(ConstFlux1D, amplitude=1)
        sp2 = self.extcurve * sp
        w = 5.03399992 * (u.micron ** -1)
        ans = self.extcurve(w).value
        np.testing.assert_allclose(sp2(w).value, ans, rtol=1e-6)

    def test_qso_countrate(self):
        """Ensure extinction curve waveset is not propagated to spectrum.
        https://github.com/spacetelescope/synphot_refactor/issues/129
        """
        bp = SpectralElement.from_file(get_pkg_data_filename(
            os.path.join('data', 'hst_acs_hrc_f850lp.fits'),
            package='synphot.tests'))
        qso = SourceSpectrum.from_file(get_pkg_data_filename(
            os.path.join('data', 'qso_template_001.dat'),
            package='synphot.tests'))
        extcurve = self.redlaw.extinction_curve(1.0 * u.mag)
        spext = qso * extcurve
        with pytest.warns(AstropyUserWarning):
            sp = spext.normalize(25 * u.STmag, bp)
            obs = Observation(sp, bp, force='taper')
        area = 45238.93416  # HST cm^2
        c = obs.countrate(area)
        ans = 1.104404103799421e-07  # From similar setup in Astrolib PySynphot
        np.testing.assert_allclose(c.value, ans, rtol=1e-3)  # 0.1% agreement


# See https://github.com/spacetelescope/synphot_refactor/issues/77
@pytest.mark.parametrize(
    ('z', 'ans'),
    ([0, [0.99514224, 0.99572959, 0.99630696, 0.99640647, 1]],
     [2, [0.80417561, 0.82569455, 0.84739614, 0.85119226, 1]],
     [4, [0.27908754, 0.32576126, 0.37920904, 0.38926572, 1]],
     [8, [5.80763088e-05, 1.89352199e-04, 6.04679639e-04, 7.38588957e-04, 1]]))
def test_etau_madau(z, ans):
    """Test Madau 1995 extinction curve."""
    w_rest = np.array([950, 973, 1026, 1216, 1300])
    w_z = w_rest * (1 + z)
    extcurve = etau_madau(w_z, z)
    np.testing.assert_allclose(extcurve(w_z), ans)


def test_etau_madau_exceptions():
    # Invalid z
    with pytest.raises(exceptions.SynphotError):
        etau_madau([500, 1000], [1, 2])

    # Too few wave
    with pytest.raises(exceptions.SynphotError):
        etau_madau(500, 0)
    with pytest.raises(exceptions.SynphotError):
        etau_madau([500], 0)


@pytest.mark.remote_data
@pytest.mark.parametrize(
    'modelname',
    ['lmc30dor', 'lmcavg', 'mwavg', 'mwdense', 'mwrv21', 'mwrv40',
     'smcbar', 'xgalsb'])
def test_redlaw_from_model(modelname):
    """Test ReddeningLaw from remote file.

    .. note:: No check on data quality as it is dependent on data file.

    """
    redlaw = ReddeningLaw.from_extinction_model(modelname)
    assert modelname in redlaw.meta['expr']
    assert 'filename' in redlaw.meta['header']
    assert 'descrip' in redlaw.meta['header']


def test_redlaw_from_model_exception():
    with pytest.raises(exceptions.SynphotError):
        ReddeningLaw.from_extinction_model('foo')


class TestWriteReddeningLaw:
    """Test ReddeningLaw ``to_fits()`` method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.x = np.linspace(1000, 5000, 5)
        self.y = np.linspace(1, 5, 5) * 0.1
        self.redlaw = ReddeningLaw(
            Empirical1D, points=self.x, lookup_table=self.y)

    @pytest.mark.parametrize('ext_hdr', [None, {'foo': 'foo'}])
    def test_write(self, ext_hdr):
        outfile = os.path.join(self.outdir, 'outredlaw.fits')

        if ext_hdr is None:
            self.redlaw.to_fits(outfile, overwrite=True)
        else:
            self.redlaw.to_fits(outfile, overwrite=True, ext_header=ext_hdr)

        # Read it back in and check
        redlaw2 = ReddeningLaw.from_file(outfile)
        np.testing.assert_allclose(redlaw2.waveset.value, self.x)
        np.testing.assert_allclose(redlaw2(self.x).value, self.y)

        if ext_hdr is not None:
            hdr = fits.getheader(outfile, 1)
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
