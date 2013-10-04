# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test reddening.py module.

Inherited methods from BaseUnitlessSpectrum are already tested in
test_spectrum.py under SpectralElement, so not tested here.

"""
from __future__ import division, print_function

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
from .. import spectrum, synexceptions, units
from ..reddening import ReddeningLaw, ExtinctionCurve


__doctest_skip__ = ['*']

# HST primary mirror
_area = u.Quantity(45238.93416, units.AREA)


class TestExtinction(object):
    """Test ReddeningLaw and ExtinctionCurve classes (most methods)."""
    def setup_class(self):
        self.redlaw = ReddeningLaw.from_file(get_pkg_data_filename(
                os.path.join('data', 'milkyway_diffuse_001.fits')), area=_area)
        self.ebv = u.Quantity(0.3, u.mag)
        self.extcurve = ExtinctionCurve.from_reddening_law(
            self.redlaw, self.ebv)

    def test_instance(self):
        assert isinstance(self.redlaw, ReddeningLaw)
        assert isinstance(self.redlaw, spectrum.BaseUnitlessSpectrum)

        assert isinstance(self.extcurve, ExtinctionCurve)
        assert isinstance(self.extcurve, spectrum.BaseUnitlessSpectrum)

    def test_redlaw_attributes(self):
        np.testing.assert_allclose(
            self.redlaw.wave.value[48:53],
            [5.03399992, 5.12949991, 5.2249999, 5.3204999, 5.41599989])
        np.testing.assert_allclose(
            self.redlaw.thru.value[48:53],
            [8.69231796, 8.40150452, 8.17892265, 8.01734924, 7.90572977])
        assert self.redlaw.wave.unit == units.INVERSE_MICRON
        assert self.redlaw.thru.unit == units.THROUGHPUT
        assert self.redlaw.thru is self.redlaw.flux
        assert self.redlaw.metadata['SHORTNM'] == 'MWAvg'

    def test_extcurve_attributes(self):
        np.testing.assert_array_equal(
            self.extcurve.wave.value, self.redlaw.wave.value)
        np.testing.assert_allclose(
            self.extcurve.thru.value,
            10 ** (-0.4 * self.redlaw.thru.value * self.ebv.value))
        assert self.extcurve.wave.unit == self.redlaw.wave.unit
        assert self.extcurve.thru.unit == units.THROUGHPUT
        assert self.extcurve.thru is self.extcurve.flux
        assert self.extcurve.primary_area.value == _area.value
        assert 'ExtinctionCurve' in self.extcurve.metadata['expr']

        # E(B-V) as float instead of Quantity
        extcurve = ExtinctionCurve.from_reddening_law(
            self.redlaw, self.ebv.value)
        np.testing.assert_allclose(
            self.extcurve.thru.value, extcurve.thru.value)

    @pytest.mark.parametrize(('op_type'), ['*', '/'])
    def test_muldiv_sp(self, op_type):
        """Apply extinction curve in inverse micron to flat spectrum in
        Angstrom.

        """
        sp = spectrum.SourceSpectrum.from_flat_spectrum(units.FLAM, area=_area)
        ans = self.extcurve.resample(5.03399992)

        if op_type == '*':
            ex_sp = self.extcurve * sp
        elif op_type == '/':
            ex_sp = sp / self.extcurve
            ans = 1 / ans

        np.testing.assert_allclose(
            ex_sp.resample(1986.491886952592).value, ans, rtol=1e-6)

    def test_redlaw_exceptions(self):
        # Invalid R(V)
        with pytest.raises(synexceptions.SynphotError):
            redlaw = ReddeningLaw([1000, 2000], u.Quantity([1, 1], units.FLAM))

        # Invalid reddening law model
        with pytest.raises(synexceptions.SynphotError):
            redlaw = ReddeningLaw.from_model('foo')

    def test_extcurve_exceptions(self):
        # Invalid reddening law
        with pytest.raises(synexceptions.SynphotError):
            extcurve = ExtinctionCurve.from_reddening_law(np.ones(10), self.ebv)

        # Invalid E(B-V)
        with pytest.raises(synexceptions.SynphotError):
            extcurve = ExtinctionCurve.from_reddening_law(self.redlaw, [1,2])
        with pytest.raises(synexceptions.SynphotError):
            extcurve = ExtinctionCurve.from_reddening_law(
                self.redlaw, u.Quantity(1, units.FLAM))


@remote_data
@pytest.mark.parametrize(
    ('modelname'),
    ['lmc30dor', 'lmcavg', 'mwavg', 'mwdense', 'mwrv21', 'mwrv40',
     'smcbar', 'xgalsb'])
def test_redlaw_from_model(modelname):
    """Test ReddeningLaw.from_model() method.

    .. note:: No check on data quality as it is dependent on remote file.

    """
    redlaw = ReddeningLaw.from_model(modelname, encoding='binary')
    wave = redlaw.wave.to(u.AA, equivalencies=units.wave_conversion)
    assert redlaw.thru.unit == units.THROUGHPUT
    assert modelname in redlaw.metadata['expr']
    assert 'filename' in redlaw.metadata
    assert 'descrip' in redlaw.metadata


class TestWriteReddeningLaw(object):
    """Test ReddeningLaw.to_fits() method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.wave = np.arange(1000, 5001, 1000, dtype=np.float64)
        self.thru = np.arange(0.1, 0.51, 0.1)
        self.redlaw = ReddeningLaw(self.wave, self.thru)

    @pytest.mark.parametrize(('ext_hdr'), [None, {'foo': 'foo'}])
    def test_write(self, ext_hdr):
        outfile = os.path.join(self.outdir, 'outredlaw.fits')

        if ext_hdr is None:
            self.redlaw.to_fits(outfile, clobber=True)
        else:
            self.redlaw.to_fits(outfile, clobber=True, ext_header=ext_hdr)

        # Read it back in and check
        redlaw2 = ReddeningLaw.from_file(outfile)
        np.testing.assert_allclose(redlaw2.wave.value, self.wave)
        np.testing.assert_allclose(redlaw2.thru.value, self.thru)
        assert redlaw2.thru is redlaw2.flux
        assert redlaw2.wave.unit == u.AA
        assert redlaw2.thru.unit == units.THROUGHPUT

        hdr = fits.getheader(outfile, 1)
        assert 'expr' in hdr
        if ext_hdr is not None:
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
