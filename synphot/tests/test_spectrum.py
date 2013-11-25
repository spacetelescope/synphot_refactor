# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and flux conversion."""
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
from astropy.utils.data import get_pkg_data_filename

# LOCAL
from .. import analytic, spectrum, exceptions, units
from ..observation import Observation
from ..utils import generate_wavelengths


# HST primary mirror
_area = u.Quantity(45238.93416, units.AREA)

# ftp://ftp.stsci.edu/cdbs/supplemental_calspec/grw_70d5824_stisnic_002.ascii
_wave = u.Quantity([4956.8, 4959.55, 4962.3], u.AA)
_flux_photlam = u.Quantity([9.7654e-3, 1.003896e-2, 9.78473e-3], units.PHOTLAM)
_flux_photnu = u.Quantity(
    [8.00335589e-14, 8.23668949e-14, 8.03700310e-14], units.PHOTNU)
_flux_flam = u.Quantity([3.9135e-14, 4.0209e-14, 3.9169e-14], units.FLAM)
_flux_fnu = u.Quantity(
    [3.20735792e-25, 3.29903646e-25, 3.21727226e-25], units.FNU)
_flux_jy = u.Quantity([3.20735792e-2, 3.29903646e-2, 3.21727226e-2], u.Jy)
_flux_count = u.Quantity([1214.88479883, 1248.91795446, 1217.28946691], u.count)
_flux_stmag = u.Quantity([12.41858665, 12.38919182, 12.41764379], units.STMAG)
_flux_abmag = u.Quantity([12.63463143, 12.60403221, 12.63128047], units.ABMAG)
_flux_obmag = u.Quantity([-7.71133775, -7.74133477, -7.71348466], units.OBMAG)
_flux_vegamag = u.Quantity(
    [12.72810665, 12.69861694, 12.72605148], units.VEGAMAG)

# Test data files
_bandfile = get_pkg_data_filename(
    os.path.join('data', 'hst_acs_hrc_f555w.fits'))
_specfile = get_pkg_data_filename(
    os.path.join('data', 'hst_acs_hrc_f555w_x_grw70d5824.fits'))
_vspec = None  # Loaded in test_load_vspec()


@remote_data
def test_load_vspec():
    """Load VEGA spectrum once here to be used later."""
    global _vspec
    _vspec = spectrum.SourceSpectrum.from_vega(
        cache=False, show_progress=False, area=_area, encoding='binary')


@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans'),
    [(_flux_photlam.value, units.PHOTLAM, _flux_photlam),
     (_flux_photlam, u.count, _flux_count),
     (_flux_count, units.PHOTLAM, _flux_photlam),
     (_flux_photlam, units.OBMAG, _flux_obmag),
     (_flux_obmag, units.PHOTLAM, _flux_photlam),
     (_flux_count, units.OBMAG, _flux_obmag),
     (_flux_obmag, u.count, _flux_count),
     (_flux_photlam, units.FLAM, _flux_flam),
     (_flux_flam, units.PHOTLAM, _flux_photlam),
     (_flux_photlam, units.STMAG, _flux_stmag),
     (_flux_stmag, units.PHOTLAM, _flux_photlam),
     (_flux_flam, units.STMAG, _flux_stmag),
     (_flux_stmag, units.FLAM, _flux_flam),
     (_flux_photlam, units.PHOTNU, _flux_photnu),
     (_flux_photnu, units.PHOTLAM, _flux_photlam),
     (_flux_photlam, units.FNU, _flux_fnu),
     (_flux_fnu, units.PHOTLAM, _flux_photlam),
     (_flux_photlam, units.ABMAG, _flux_abmag),
     (_flux_abmag, units.PHOTLAM, _flux_photlam),
     (_flux_fnu, units.ABMAG, _flux_abmag),
     (_flux_abmag, units.FNU, _flux_fnu),
     (_flux_fnu, units.STMAG, _flux_stmag),
     (_flux_fnu, u.mJy, _flux_jy.to(u.mJy)),
     (_flux_photlam, u.Jy, _flux_jy),
     (_flux_jy, units.PHOTLAM, _flux_photlam),
     (_flux_flam, u.Jy, _flux_jy),
     (u.Quantity(np.zeros(3), units.FNU), units.FLAM,
      u.Quantity(np.zeros(3), units.FLAM))])
def test_flux_conversion(in_q, out_u, ans):
    """Test flux conversion, except VEGAMAG."""
    result = units.convert_flux(_wave, in_q, out_u, area=_area)
    np.testing.assert_allclose(result.value, ans.value, rtol=1e-6)
    assert result.unit == ans.unit


@remote_data
@pytest.mark.parametrize(
    ('in_q', 'out_u', 'ans'),
    [(_flux_photlam, units.VEGAMAG, _flux_vegamag),
     (_flux_vegamag, units.PHOTLAM, _flux_photlam),
     (_flux_jy, units.VEGAMAG, _flux_vegamag),
     (_flux_vegamag, u.Jy, _flux_jy)])
def test_flux_conversion_vega(in_q, out_u, ans):
    """Test Vega spectrum object and flux conversion with VEGAMAG.

    .. note:: 0.5% is good enough given Vega gets updated from time to time.

    """
    result = units.convert_flux(_wave, in_q, out_u, area=_area, vegaspec=_vspec)
    np.testing.assert_allclose(result.value, ans.value, rtol=5e-3)
    assert result.unit == ans.unit


def test_flux_conversion_exceptions():
    """Test for appropriate exceptions."""
    # Invalid flux unit
    with pytest.raises(u.UnitsError):
        x = units.convert_flux(_wave, _wave, units.PHOTLAM)
    with pytest.raises(u.UnitsError):
        x = units.convert_flux(_wave, _flux_photlam, u.AA)

    # Missing Vega spectrum
    with pytest.raises(exceptions.SynphotError):
        x = units.convert_flux(_wave, _flux_fnu, units.VEGAMAG, vegaspec=None)

    # Missing area
    with pytest.raises(exceptions.SynphotError):
        x = units.convert_flux(_wave, _flux_photlam, u.count, area=None)
    with pytest.raises(exceptions.SynphotError):
        x = units.convert_flux(_wave, _flux_obmag, units.PHOTLAM, area=None)


class TestSourceSpectrum(object):
    """Test SourceSpectrum object (most methods)."""
    def setup_class(self):
        self.sp = spectrum.SourceSpectrum.from_file(_specfile, area=_area)

    def test_attributes(self):
        np.testing.assert_allclose(
            self.sp.wave.value[5000:5004],
            [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            self.sp.flux.value[5000:5004],
            [1.87284130e-15, 1.85656811e-15, 1.84030867e-15, 1.82404183e-15])
        np.testing.assert_allclose(self.sp.primary_area.value, _area.value)
        assert self.sp.wave.unit == u.AA
        assert self.sp.flux.unit == units.FLAM
        assert self.sp.primary_area.unit == _area.unit
        assert self.sp.metadata['expr'] == str(self.sp)
        assert self.sp.metadata['SIMPLE']  # From FITS header
        assert self.sp.warnings == {}

    def test_init(self):
        # Direct initialization with flipped arrays
        sp = spectrum.SourceSpectrum(
            self.sp.wave.value[::-1], self.sp.flux.value[::-1],
            flux_unit=self.sp.flux.unit, header={'FOO': 'foo'})
        np.testing.assert_array_equal(sp.wave.value, self.sp.wave.value[::-1])
        np.testing.assert_array_equal(sp.flux.value, self.sp.flux.value[::-1])
        assert sp.wave.unit == self.sp.wave.unit
        assert sp.flux.unit == self.sp.flux.unit
        assert sp.primary_area is None
        assert sp.metadata['FOO'] == 'foo'

        # Negative flux warning
        sp = spectrum.SourceSpectrum(_wave, [100.0, -45, 5e-17])
        assert 'NegativeFlux' in sp.warnings

        # Invalid flux unit
        with pytest.raises(exceptions.SynphotError):
            sp = spectrum.SourceSpectrum(_wave, _flux_obmag)

        # Shape mismatch
        with pytest.raises(exceptions.SynphotError):
            sp = spectrum.SourceSpectrum(self.sp.wave, np.arange(10))

    def test_merge_wave(self):
        sp = spectrum.SourceSpectrum(_wave.to(u.micron), _flux_flam)
        wave = self.sp.merge_wave(sp)
        np.testing.assert_allclose(
            wave.value[3202:3218],
            [4956.39111328, 4956.8, 4956.93847656, 4957.48583984,
             4958.03320312, 4958.58105469, 4959.12890625, 4959.55,
             4959.67626953, 4960.22412109, 4960.77197266, 4961.3203125,
             4961.86816406, 4962.3, 4962.41601562, 4962.96435547])
        assert wave.unit == self.sp.wave.unit

    def test_resample(self):
        # Sample at existing wavelength (no interpolation)
        flux = self.sp.resample(self.sp.wave[5000])
        np.testing.assert_array_equal(flux.value, self.sp.flux.value[5000])
        assert flux.unit == self.sp.flux.unit

        # Sampling with interpolation
        flux = self.sp.resample(_wave.value)
        np.testing.assert_allclose(
            flux.value, [8.57166622e-15, 8.86174843e-15, 8.68707743e-15])

        # Descending order
        flux = self.sp.resample(_wave.value[::-1])
        np.testing.assert_allclose(
            flux.value, [8.68707743e-15, 8.86174843e-15, 8.57166622e-15])

        # Spectrum with descending order
        sp = spectrum.SourceSpectrum(
            self.sp.wave.value[::-1], self.sp.flux.value[::-1])
        flux = sp.resample(_wave)
        np.testing.assert_allclose(
            flux.value, [8.57166622e-15, 8.86174843e-15, 8.68707743e-15])

    def test_conversion(self):
        old_wave = self.sp.wave.copy()
        old_flux = self.sp.flux.copy()

        self.sp.convert_wave(u.micron ** -1)
        self.sp.convert_flux(units.FNU)
        np.testing.assert_allclose(self.sp.wave.value[5000], 1.6542148230571696)
        np.testing.assert_allclose(
            self.sp.flux.value[5000], 2.282950185743497e-26)
        assert self.sp.wave.unit == u.micron ** -1
        assert self.sp.flux.unit == units.FNU

        with pytest.raises(u.UnitsError):
            self.sp.convert_wave(u.Jy)
        with pytest.raises(exceptions.SynphotError):
            self.sp.convert_flux(u.AA)

        # Convert back to original units
        self.sp.convert_wave(old_wave.unit)
        self.sp.convert_flux(old_flux.unit)
        np.testing.assert_allclose(
            self.sp.wave.value, old_wave.value, rtol=1e-6)
        np.testing.assert_allclose(
            self.sp.flux.value, old_flux.value, rtol=1e-6)

    def test_integrate(self):
        # Whole range
        totalflux = self.sp.integrate()
        np.testing.assert_allclose(
            totalflux.value, 8.460125829057308e-12, rtol=1e-6)
        assert totalflux.unit == self.sp.flux.unit

        # Given range
        totalflux = self.sp.integrate(wavelengths=_wave)
        totalflux2 = self.sp.integrate(wavelengths=_wave.value)
        np.testing.assert_allclose(
            totalflux.value, 4.810058069909525e-14, rtol=2.5e-6)
        np.testing.assert_allclose(totalflux2.value, totalflux.value)

    def test_trim(self):
        sp = self.sp.trim_spectrum(6045.15, 6047.84)
        np.testing.assert_array_equal(
            sp.wave.value, self.sp.wave.value[5000:5005])
        np.testing.assert_array_equal(
            sp.flux.value, self.sp.flux.value[5000:5005])
        assert sp.wave.unit == self.sp.wave.unit
        assert sp.flux.unit == self.sp.flux.unit

        with pytest.raises(ValueError):
            sp = self.sp.trim_spectrum(6045.15, 6045.15)

        with pytest.raises(ValueError):
            sp = self.sp.trim_spectrum(6047.84, 6045.15)

    def test_taper(self):
        # Original spectrum already tapered -- nothing done
        old_wave = self.sp.wave.copy()
        old_flux = self.sp.flux.copy()
        self.sp.taper()
        np.testing.assert_array_equal(self.sp.wave.value, old_wave.value)
        np.testing.assert_array_equal(self.sp.flux.value, old_flux.value)

        # Tapering is done
        sp = spectrum.SourceSpectrum(_wave, _flux_flam)
        sp.taper()
        np.testing.assert_allclose(
            sp.wave.value,
            [4954.05152484, 4956.8, 4959.55, 4962.3, 4965.05152484])
        np.testing.assert_allclose(
            sp.flux.value, [0, 3.9135e-14, 4.0209e-14, 3.9169e-14, 0])
        assert sp.wave.unit == _wave.unit
        assert sp.flux.unit == _flux_flam.unit

    def test_redshift(self):
        """Test SourceSpectrum apply_redshift() method."""
        # Zero redshift should return the same spectrum.
        sp_z0 = self.sp.apply_redshift(0)
        np.testing.assert_array_equal(sp_z0.wave.value, self.sp.wave.value)
        np.testing.assert_array_equal(sp_z0.flux.value, self.sp.flux.value)
        assert sp_z0.wave.unit == self.sp.wave.unit
        assert sp_z0.flux.unit == self.sp.flux.unit
        assert sp_z0.metadata['expr'] != self.sp.metadata['expr']
        assert sp_z0.metadata['FILENAME'] == self.sp.metadata['FILENAME']

        # Non-zero redshift (length)
        sp_zlen = sp_z0.apply_redshift(1.65)
        np.testing.assert_array_equal(
            sp_zlen.wave.value, sp_z0.wave.value * 2.65)
        np.testing.assert_array_equal(sp_zlen.flux.value, sp_z0.flux.value)

        # Non-zero redshift (frequency).
        # Should give same result as length after conversion.
        sp_z0.convert_wave(u.Hz)
        sp_zfrq = sp_z0.apply_redshift(1.65)
        np.testing.assert_array_equal(sp_zfrq.flux.value, sp_z0.flux.value)
        sp_zfrq.convert_wave(sp_zlen.wave.unit)
        np.testing.assert_allclose(
            sp_zfrq.wave.value, sp_zlen.wave.value, rtol=1e-6)
        assert sp_zfrq.metadata['expr'] == sp_zlen.metadata['expr']

        # Exceptions
        with pytest.raises(exceptions.SynphotError):
            sp_zlen = sp_z0.apply_redshift([1, 2, 3])
        with pytest.raises(exceptions.SynphotError):
            sp_zlen = sp_z0.apply_redshift(u.Quantity(2))


class TestAddMag(object):
    """Test SourceSpectrum add_mag() method."""
    def setup_class(self):
        self.bright = spectrum.SourceSpectrum(_wave, units.convert_flux(
                _wave, u.Quantity([18.0] * 3, units.ABMAG), units.PHOTLAM))
        self.faint = spectrum.SourceSpectrum(_wave, units.convert_flux(
                _wave, u.Quantity([21.0] * 3, units.ABMAG), units.PHOTLAM))
        self.dmag = u.Quantity(3.0, u.mag)

    def test_add(self):
        sp = self.bright.add_mag(self.dmag)
        np.testing.assert_allclose(sp.flux.value, self.faint.flux.value)

    def test_subtract(self):
        sp = self.faint.add_mag(self.dmag.value * -1)
        np.testing.assert_allclose(sp.flux.value, self.bright.flux.value)

    def test_exceptions(self):
        with pytest.raises(exceptions.SynphotError):
            sp = self.bright.add_mag('s')
        with pytest.raises(exceptions.SynphotError):
            sp = self.bright.add_mag(self.faint.flux.value)
        with pytest.raises(exceptions.SynphotError):
            sp = self.bright.add_mag(self.faint.flux)
        with pytest.raises(exceptions.SynphotError):
            sp = self.bright.add_mag(u.Quantity(1.0, units.FLAM))


class TestSpectralElement(object):
    """Test SpectralElement object (most methods)."""
    def setup_class(self):
        self.bp = spectrum.SpectralElement.from_file(_bandfile, area=_area)
        self.exthdr = fits.getheader(_bandfile, 1)

    def test_attributes(self):
        np.testing.assert_allclose(
            self.bp.wave.value[5000:5004],
            [6045.1640625, 6045.83203125, 6046.49951172, 6047.16748047])
        np.testing.assert_allclose(
            self.bp.thru.value[5000:5004],
            [0.0920415, 0.09125588, 0.09047068, 0.08968487])
        np.testing.assert_allclose(self.bp.primary_area.value, _area.value)
        assert self.bp.wave.unit == u.AA
        assert self.bp.thru.unit == units.THROUGHPUT
        assert self.bp.thru is self.bp.flux
        assert self.bp.primary_area.unit == _area.unit
        assert self.bp.metadata['expr'] == str(self.bp)
        assert self.bp.metadata['SIMPLE']  # From FITS header
        assert self.bp.warnings == {}

    def test_init(self):
        # Direct initialization with flipped arrays
        bp = spectrum.SpectralElement(
            self.bp.wave.value[::-1], self.bp.thru.value[::-1],
            header={'FOO': 'foo'})
        np.testing.assert_array_equal(bp.wave.value, self.bp.wave.value[::-1])
        np.testing.assert_array_equal(bp.thru.value, self.bp.thru.value[::-1])
        assert bp.wave.unit == self.bp.wave.unit
        assert bp.thru.unit == self.bp.thru.unit
        assert bp.primary_area is None
        assert bp.metadata['FOO'] == 'foo'

        # Negative throughput warning
        bp = spectrum.SpectralElement(_wave, [100.0, -45, 5e-17])
        assert 'NegativeFlux' in bp.warnings

        # Invalid throughput unit
        with pytest.raises(exceptions.SynphotError):
            bp = spectrum.SpectralElement(_wave, _flux_flam)

        # Shape mismatch
        with pytest.raises(exceptions.SynphotError):
            bp = spectrum.SpectralElement(self.bp.wave, np.arange(10))

    def test_merge_wave(self):
        bp = spectrum.SpectralElement(_wave.to(u.micron), _flux_flam.value)
        wave = self.bp.merge_wave(bp)
        np.testing.assert_allclose(
            wave.value[3202:3218],
            [4956.39111328, 4956.8, 4956.93847656, 4957.48583984,
             4958.03320312, 4958.58105469, 4959.12890625, 4959.55,
             4959.67626953, 4960.22412109, 4960.77197266, 4961.3203125,
             4961.86816406, 4962.3, 4962.41601562, 4962.96435547])
        assert wave.unit == self.bp.wave.unit

    def test_resample(self):
        # Sample at existing wavelength (no interpolation)
        thru = self.bp.resample(self.bp.wave[5000])
        np.testing.assert_array_equal(thru.value, self.bp.thru.value[5000])
        assert thru.unit == self.bp.thru.unit

        # Sampling with interpolation
        thru = self.bp.resample(_wave.value)
        np.testing.assert_allclose(
            thru.value, [0.21766723, 0.21963299, 0.22037384])

        # Descending order
        thru = self.bp.resample(_wave.value[::-1])
        np.testing.assert_allclose(
            thru.value, [0.22037384, 0.21963299, 0.21766723])

        # Passband with descending order
        bp = spectrum.SpectralElement(
            self.bp.wave.value[::-1], self.bp.thru.value[::-1])
        thru = bp.resample(_wave)
        np.testing.assert_allclose(
            thru.value, [0.21766723, 0.21963299, 0.22037384])

    def test_conversion(self):
        old_wave = self.bp.wave.copy()
        self.bp.convert_wave(u.micron ** -1)
        np.testing.assert_allclose(self.bp.wave.value[5000], 1.6542149)
        assert self.bp.wave.unit == u.micron ** -1

        with pytest.raises(u.UnitsError):
            self.bp.convert_wave(u.Jy)

        # Throughput cannot be converted, so convert_flux() does nothing
        thru = self.bp.convert_flux(units.FNU)
        assert thru is self.bp.thru
        assert thru is self.bp.flux

        with pytest.raises(AttributeError):
            self.bp.convert_thru(units.FNU)

        # Convert back to original units
        self.bp.convert_wave(old_wave.unit)
        np.testing.assert_allclose(
            self.bp.wave.value, old_wave.value, rtol=1e-6)

    def test_integrate(self):
        """For passband, value=EQUVW when all wavelengths are used."""
        # Whole range (EQUVW)
        totalthru = self.bp.integrate()
        equvw = self.bp.equivwidth()
        np.testing.assert_allclose(equvw.value, self.exthdr['EQUVW'], rtol=1e-5)
        np.testing.assert_equal(totalthru.value, equvw.value)
        assert totalthru.unit == self.bp.thru.unit
        assert equvw.unit == self.bp.wave.unit

        # Given range
        totalthru = self.bp.integrate(wavelengths=_wave)
        totalthru2 = self.bp.integrate(wavelengths=_wave.value)
        np.testing.assert_allclose(
            totalthru.value, 1.2062975715374322, rtol=2.5e-6)
        np.testing.assert_allclose(totalthru2.value, totalthru.value)

    def test_trim(self):
        bp = self.bp.trim_spectrum(6045.15, 6047.84)
        np.testing.assert_array_equal(
            bp.wave.value, self.bp.wave.value[5000:5005])
        np.testing.assert_array_equal(
            bp.thru.value, self.bp.thru.value[5000:5005])
        assert bp.wave.unit == self.bp.wave.unit
        assert bp.thru.unit == self.bp.thru.unit

        with pytest.raises(ValueError):
            bp = self.bp.trim_spectrum(6045.15, 6045.15)

        with pytest.raises(ValueError):
            bp = self.bp.trim_spectrum(6047.84, 6045.15)

    def test_taper(self):
        # Original spectrum already tapered -- nothing done
        old_wave = self.bp.wave.copy()
        old_thru = self.bp.thru.copy()
        self.bp.taper()
        np.testing.assert_array_equal(self.bp.wave.value, old_wave.value)
        np.testing.assert_array_equal(self.bp.thru.value, old_thru.value)

        # Tapering is done
        bp = spectrum.SpectralElement(_wave, _flux_flam.value)
        bp.taper()
        np.testing.assert_allclose(
            bp.wave.value,
            [4954.05152484, 4956.8, 4959.55, 4962.3, 4965.05152484])
        np.testing.assert_allclose(
            bp.thru.value, [0, 3.9135e-14, 4.0209e-14, 3.9169e-14, 0])
        assert bp.wave.unit == _wave.unit
        assert bp.thru.unit == self.bp.thru.unit
        assert bp.thru is bp.flux

    def test_uresp(self):
        uresp = self.bp.unit_response()
        np.testing.assert_allclose(
            uresp.value, self.exthdr['URESP'], rtol=2.5e-5)
        assert uresp.unit == units.FLAM

        # Undefined area must raise exception
        bp = spectrum.SpectralElement(_wave, _flux_flam.value)
        with pytest.raises(exceptions.SynphotError):
            bp.unit_response()

    def test_pivot(self):
        pivwv = self.bp.pivot()
        np.testing.assert_allclose(pivwv.value, self.exthdr['PIVWV'], rtol=1e-6)
        assert pivwv.unit == u.AA

    def test_rmswidth(self):
        rmsw = self.bp.rmswidth()
        np.testing.assert_allclose(rmsw.value, 359.55954282883687, rtol=1e-6)
        assert rmsw.unit == u.AA

        rmsw = self.bp.rmswidth(threshold=0.01)
        np.testing.assert_allclose(rmsw.value, 357.43298216917754, rtol=1e-6)

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            rmsw = self.bp.rmswidth(threshold=u.Quantity(0.01))
        with pytest.raises(exceptions.SynphotError):
            rmsw = self.bp.rmswidth(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            rmsw = self.bp.rmswidth(threshold='foo')

    def test_fwhm(self):
        """This also calls PHOTBW."""
        fwhmval = self.bp.fwhm()
        np.testing.assert_allclose(fwhmval.value, 841.09, rtol=2.5e-5)
        assert fwhmval.unit == u.AA

        fwhmval = self.bp.fwhm(threshold=0.01)
        np.testing.assert_allclose(
            fwhmval.value, 836.2879507505378, rtol=2.5e-5)

        # Invalid threshold must raise exception
        with pytest.raises(exceptions.SynphotError):
            fwhmval = self.bp.fwhm(threshold=u.Quantity(0.01))
        with pytest.raises(exceptions.SynphotError):
            fwhmval = self.bp.fwhm(threshold=[0.01, 0.02])
        with pytest.raises(exceptions.SynphotError):
            fwhmval = self.bp.fwhm(threshold='foo')

    def test_avgwave_tlambda(self):
        avgwv = self.bp.avgwave()
        np.testing.assert_allclose(avgwv.value, 5367.9, rtol=1e-5)
        assert avgwv.unit == u.AA

        tlam = self.bp.tlambda()
        np.testing.assert_allclose(tlam.value, 0.22808, rtol=1e-5)
        assert tlam.unit == u.dimensionless_unscaled

    def test_wpeak_tpeak(self):
        tpk = self.bp.tpeak()
        np.testing.assert_allclose(tpk.value, self.exthdr['TPEAK'])
        assert tpk.unit == u.dimensionless_unscaled

        wpk = self.bp.wpeak()
        np.testing.assert_allclose(wpk.value, 5059.8, rtol=1e-5)
        assert wpk.unit == u.AA

    def test_rectw(self):
        rectw = self.bp.rectwidth()
        np.testing.assert_allclose(rectw.value, self.exthdr['RECTW'], rtol=1e-6)
        assert rectw.unit == u.AA

    def test_qtlam(self):
        qtlam = self.bp.efficiency()
        np.testing.assert_allclose(qtlam.value, 0.050901, rtol=1e-5)
        assert qtlam.unit == u.dimensionless_unscaled

    def test_emflx(self):
        flx = self.bp.emflx()
        np.testing.assert_allclose(flx.value, self.exthdr['EMFLX'], rtol=2.5e-5)
        assert flx.unit == units.FLAM


@remote_data
@pytest.mark.parametrize(
    ('filtername'),
    ['bessel_j', 'bessel_h', 'bessel_k', 'cousins_r', 'cousins_i',
     'johnson_u', 'johnson_b', 'johnson_v', 'johnson_r', 'johnson_i',
     'johnson_j', 'johnson_k'])
def test_filter(filtername):
    """Test SpectralElement from_filter() class method.

    .. note::

        Filter data quality is not checked as it depends on the remote file.

    """
    bp = spectrum.SpectralElement.from_filter(filtername, encoding='binary')
    assert bp.thru is bp.flux
    assert filtername in bp.metadata['expr']


def test_filter_exception():
    """Test SpectralElement from_filter() exception."""
    with pytest.raises(exceptions.SynphotError):
        sp = spectrum.SpectralElement.from_filter('foo')


class TestMathOperators(object):
    """Test spectrum math operators."""
    def setup_class(self):
        self.sp_1 = spectrum.SourceSpectrum(
            [3999.9, 4000.0, 5000.0, 6000.0, 6000.1],
            [0, 3.5e-14, 4e-14, 4.5e-14, 0], area=_area)

        # FLAM: 3.9135e-14, 4.0209e-14, 3.9169e-14
        self.sp_2 = spectrum.SourceSpectrum(_wave, _flux_jy, area=_area)

        self.bp_1 = spectrum.SpectralElement(
            u.Quantity([399.99, 400.01, 500.0, 590.0, 600.1], u.nm),
            [0, 0.1, 0.2, 0.3, 0], area=_area)

    def _check_sp(self, sp, ans_wave, ans_flux):
        np.testing.assert_allclose(sp.wave.value, ans_wave)
        np.testing.assert_allclose(sp.flux.value, ans_flux)
        assert sp.wave.unit == u.AA
        assert sp.flux.unit == units.FLAM
        assert isinstance(sp, spectrum.SourceSpectrum)

    def _check_bp(self, bp, ans_flux):
        np.testing.assert_array_equal(bp.wave.value, self.bp_1.wave.value)
        np.testing.assert_allclose(bp.thru.value, ans_flux)
        assert bp.thru is bp.flux
        assert bp.wave.unit == u.nm
        assert bp.thru.unit == u.dimensionless_unscaled
        assert isinstance(bp, spectrum.SpectralElement)

    @pytest.mark.parametrize(
        ('op_type', 'other_scalar', 'ans_flux'),
        [('+', False, [3.9135e-14, 7.4135e-14, 7.8919e-14, 8.000675e-14,
                       7.89805001e-14, 7.9169e-14, 8.4169e-14, 3.9169e-14]),
         ('-', False, [0, 0, 6.49e-16, 0, 6.425e-16, 8.31e-16, 5.831e-15, 0]),
         ('+', True, [5e-15, 4e-14, 4.5e-14, 5e-14, 5e-15]),
         ('-', True, [0, 3e-14, 3.5e-14, 4e-14, 0])])
    def test_add_sub_sp(self, op_type, other_scalar, ans_flux):
        if other_scalar:
            other = 5e-15
            ans_wave = self.sp_1.wave.value
        else:
            other = self.sp_2
            ans_wave = [3999.9, 4000, 4956.8, 4959.55, 4962.3, 5000,
                        6000, 6000.1]

        if op_type == '+':
            sp = self.sp_1 + other
        elif op_type == '-':
            sp = self.sp_1 - other

        self._check_sp(sp, ans_wave, ans_flux)
        if not other_scalar:
            assert self.sp_2.flux.unit == u.Jy

    @pytest.mark.parametrize(
        ('op_type', 'other_scalar', 'ans_flux'),
        [('+', False, [0, 0.2, 0.4, 0.6, 0]),
         ('-', False, 0),
         ('+', True, [0.1, 0.2, 0.3, 0.4, 0.1]),
         ('-', True, [0, 0, 0.1, 0.2, 0])])
    def test_add_sub_bp(self, op_type, other_scalar, ans_flux):
        if other_scalar:
            other = 0.1
        else:
            other = self.bp_1

        if op_type == '+':
            bp1 = self.bp_1 + other
        elif op_type == '-':
            bp1 = self.bp_1 - other

        self._check_bp(bp1, ans_flux)

    @pytest.mark.parametrize(
        ('op_type', 'sp_first'),
        [('+', True),
         ('+', False),
         ('-', True),
         ('-', False)])
    def test_add_sub_sp_bp(self, op_type, sp_first):
        """Cannot add/subtract SourceSpectrum and SpectralElement."""
        if sp_first:
            obj1 = self.sp_1
            obj2 = self.bp_1
        else:
            obj1 = self.bp_1
            obj2 = self.sp_1

        with pytest.raises(exceptions.IncompatibleSources):
            if op_type == '+':
                sp = obj1 + obj2
            elif op_type == '-':
                sp = obj1 - obj2

    @pytest.mark.parametrize(('op_type'), ['*', '/'])
    def test_mul_div_sp_sp(self, op_type):
        """Multiplication can only be between spectrum and dimensionless."""
        with pytest.raises(exceptions.IncompatibleSources):
            if op_type == '*':
                sp = self.sp_1 * self.sp_1
            elif op_type == '/':
                sp = self.sp_1 / self.sp_1

    @pytest.mark.parametrize(
        ('op_type', 'is_rmul', 'ans_flux'),
        [('*', False, [0, 7e-14, 8e-14, 9e-14, 0]),
         ('*', True, [0, 7e-14, 8e-14, 9e-14, 0]),
         ('/', False, [0, 1.75e-14, 2e-14, 2.25e-14, 0])])
    def test_mul_div_sp_scalar(self, op_type, is_rmul, ans_flux):
        if is_rmul:
            obj1 = 2
            obj2 = self.sp_1
        else:
            obj1 = self.sp_1
            obj2 = 2

        if op_type == '*':
            sp = obj1 * obj2
        elif op_type == '/':
            sp = obj1 / obj2

        self._check_sp(sp, self.sp_1.wave.value, ans_flux)

    @pytest.mark.parametrize(
        ('op_type', 'is_scalar', 'is_rmul', 'ans_flux'),
        [('*', True, False, [0, 0.2, 0.4, 0.6, 0]),
         ('*', True, True, [0, 0.2, 0.4, 0.6, 0]),
         ('*', False, False, [0, 0.01, 0.04, 0.09, 0]),
         ('/', True, False, [0, 0.05, 0.1, 0.15, 0]),
         ('/', False, False, [np.nan, 1, 1, 1, np.nan])])
    def test_mul_div_bp(self, op_type, is_scalar, is_rmul, ans_flux):
        if is_scalar:
            other = 2
        else:
            other = self.bp_1

        if is_rmul:
            obj1 = other
            obj2 = self.bp_1
        else:
            obj1 = self.bp_1
            obj2 = other

        if op_type == '*':
            bp = obj1 * obj2
        elif op_type == '/':
            bp = obj1 / obj2

        self._check_bp(bp, ans_flux)

    @pytest.mark.parametrize(('is_rmul'), [False, True])
    def test_mul_sp_bp(self, is_rmul):
        """SpectralElement * SourceSpectrum = SourceSpectrum"""
        if is_rmul:
            sp = self.bp_1 * self.sp_1
        else:
            sp = self.sp_1 * self.bp_1

        self._check_sp(
            sp, [3999.9, 4000, 4000.1, 5000, 5900, 6000, 6000.1, 6001],
            [0, 1.75e-15, 3.50005e-15, 8e-15, 1.335e-14, 1.33663366e-16, 0, 0])

    def test_div_sp_bp(self):
        sp = self.sp_1 / self.bp_1
        self._check_sp(
            sp, [3999.9, 4000, 4000.1, 5000, 5900, 6000, 6000.1, 6001],
            [0, 7e-13, 3.50005e-13, 2e-13, 1.483333333333e-13,
             1.5149999998e-11, 0, np.nan])

        # Spectrum can only divided by dimensionless value
        with pytest.raises(exceptions.IncompatibleSources):
            sp = self.bp_1 / self.sp_1

    def test_misc_exceptions(self):
        """Unsupported operations raise TypeError but are not tested."""
        # other is of wrong data type.
        # Works for all operators but only * tested.
        with pytest.raises(exceptions.IncompatibleSources):
            sp = self.sp_1 * [1, 2, 3]
        with pytest.raises(exceptions.IncompatibleSources):
            sp = self.sp_1 * u.Quantity(1)

        # Primary area mismatch.
        # Works for all operators but only + tested.
        with pytest.raises(exceptions.IncompatibleSources):
            sp = self.sp_1 + spectrum.SourceSpectrum(_wave, _flux_jy)


class TestCheckOverlap(object):
    """Test spectrum overlap check."""
    def setup_class(self):
        self.sp = spectrum.SourceSpectrum(
            [2999.9, 3000.0, 6000.0, 6000.1], [0, 1.0, 1.0, 0])

    def test_full(self):
        bp = spectrum.SpectralElement(
            [999.9, 1000.0, 9000.0, 9000.1], [0, 1.0, 1.0, 0])
        assert self.sp.check_overlap(bp) == 'full'

    def test_partial_most(self):
        bp = spectrum.SpectralElement(
            [3000.0, 3001.0, 6000.1, 6000.2], [0, 1.0, 1.0, 0])
        assert self.sp.check_overlap(bp) == 'partial_most'

    def test_partial_notmost(self):
        bp = spectrum.SpectralElement(
            [3999.9, 4000.0, 4500.0, 4500.1], [0, 1.0, 1.0, 0])
        assert self.sp.check_overlap(bp) == 'partial_notmost'

        # Ensure zeroes in passband are not taken into account
        bp2 = spectrum.SpectralElement(
            [3000.0, 3001.0, 6000.1, 6000.2], [0, 1.0, 1.0, 0])
        bp3 = bp2 * bp
        assert self.sp.check_overlap(bp2) == 'partial_most'
        assert self.sp.check_overlap(bp3) == 'partial_notmost'

    def test_none(self):
        bp = spectrum.SpectralElement(
            [99.9, 100.0, 2999.9, 3000.0], [0, 1.0, 1.0, 0])
        assert self.sp.check_overlap(bp) == 'none'


class TestRenorm(object):
    """Test SourceSpectrum renorm() method."""
    def setup_class(self):
        """``expr`` stores the equivalent IRAF SYNPHOT command."""
        # Blackbody
        wave = generate_wavelengths(wave_unit=u.AA)[0]
        tmp = analytic.BlackBody1DSpectrum(5000, area=_area)
        self.bb = tmp.to_spectrum(wave)
        self.bb.metadata['expr'] = 'bb(5000)'

        # Gaussian emission line
        wave = np.arange(4900, 6100, 0.1)
        tmp = analytic.gaussian_spectrum(1e-13, 5500, 250, area=_area)
        self.em = tmp.to_spectrum(wave)
        self.em.metadata['expr'] = 'em(5500, 250, 1e-13, flam)'

        # Passbands
        self.acs = spectrum.SpectralElement.from_file(_bandfile, area=_area)
        self.acs.metadata['expr'] = 'band(acs,hrc,f555w)'
        self.abox = spectrum.SpectralElement(
            [5499.4, 5499.5, 5500.5, 5500.6], [0, 1.0, 1.0, 0], area=_area)
        self.abox.metadata['expr'] = 'box(5500,1)'

    def _select_sp(self, sp_type):
        if sp_type == 'bb':
            sp = self.bb
        elif sp_type == 'em':
            sp = self.em
        else:
            sp = None
        return sp

    def _compare_countrate(self, rn_sp, ans_countrate):
        # Observation is needed to compare with expected count rate
        # although it is tested in test_observation.py
        obs = Observation.from_spec_band(rn_sp, self.acs, force='extrap')
        ct_rate = obs.countrate()

        # 0.025% agreement with IRAF SYNPHOT COUNTRATE
        np.testing.assert_allclose(ct_rate.value, ans_countrate, rtol=2.5e-4)
        assert ct_rate.unit == u.count

    @pytest.mark.parametrize(
        ('sp_type', 'rn_val', 'ans_countrate'),
        [('bb', u.Quantity(1e-5, units.PHOTLAM), 117.9167),
         ('bb', u.Quantity(1e-16, units.PHOTNU), 116.8613),
         ('bb', 1e-16, 326.4773),
         ('bb', u.Quantity(20, units.STMAG), 118.5366),
         ('bb', u.Quantity(1e-27, units.FNU), 323.5549),
         ('bb', u.Quantity(20, units.ABMAG), 117.4757),
         ('bb', u.Quantity(1e-4, u.Jy), 323.5547),
         ('bb', u.Quantity(0.1, u.mJy), 323.5548),
         ('em', u.Quantity(1e-4, units.PHOTLAM), 277.4368),
         ('em', u.Quantity(1e-15, units.PHOTNU), 274.9537),
         ('em', 1e-16, 76.81425),
         ('em', u.Quantity(18, units.STMAG), 175.9712),
         ('em', u.Quantity(1e-27, units.FNU), 76.12671),
         ('em', u.Quantity(18, units.ABMAG), 174.3967),
         ('em', u.Quantity(1e-3, u.Jy), 761.2667),
         ('em', u.Quantity(1, u.mJy), 761.2666)])
    def test_renorm_density(self, sp_type, rn_val, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.renorm(rn_val, self.abox)
        self._compare_countrate(rn_sp, ans_countrate)

    @pytest.mark.parametrize(
        ('sp_type', 'rn_val', 'ans_countrate'),
        [('bb', u.Quantity(2, u.count), 2),
         ('bb', u.Quantity(-1, units.OBMAG), 2.511886),
         ('em', u.Quantity(2, u.count), 2),
         ('em', u.Quantity(-1, units.OBMAG), 2.511888)])
    def test_renorm_nondensity(self, sp_type, rn_val, ans_countrate):
        """This also tests force=True for 'partial_notmost' overlap."""
        sp = self._select_sp(sp_type)
        rn_sp = sp.renorm(rn_val, self.acs, force=True)
        self._compare_countrate(rn_sp, ans_countrate)

        if sp_type == 'em':
            assert 'PartialRenorm' in rn_sp.warnings
            assert 'PartialRenorm' not in sp.warnings

    @remote_data
    @pytest.mark.parametrize(
        ('sp_type', 'ans_countrate'),
        [('bb', 116.4746),
         ('em', 27.40439)])
    def test_renorm_vegamag(self, sp_type, ans_countrate):
        sp = self._select_sp(sp_type)
        rn_sp = sp.renorm(
            u.Quantity(20, unit=units.VEGAMAG), self.abox, vegaspec=_vspec)
        self._compare_countrate(rn_sp, ans_countrate)

    def test_exceptions(self):
        # Invalid passband
        with pytest.raises(exceptions.SynphotError):
            self.bb.renorm(10, np.ones(10))

        # Disjoint passband
        with pytest.raises(exceptions.DisjointError):
            self.bb.renorm(
                10, spectrum.SpectralElement(
                    [29999.9, 30000, 30001, 30001.1],
                    [0, 1.0, 1.0, 0], area=_area))

        # Partial overlap without force
        with pytest.raises(exceptions.PartialOverlap):
            rn_sp = self.em.renorm(1, self.acs)

        # Missing Vega spectrum
        with pytest.raises(exceptions.SynphotError):
            rn_sp = self.bb.renorm(u.Quantity(10, units.VEGAMAG), self.abox)

        # Zero flux
        with pytest.raises(ValueError):
            sp = self.em * 0.0
            rn_sp = sp.renorm(u.Quantity(10, units.VEGAMAG), self.abox)


class TestWriteSpec(object):
    """Test spectrum to_fits() method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()

    @pytest.mark.parametrize(
        ('is_sp', 'ext_hdr'),
        [(True, None),
         (True, {'foo': 'foo'}),
         (False, None),
         (False, {'foo': 'foo'})])
    def test_write(self, is_sp, ext_hdr):
        outfile = os.path.join(self.outdir, 'outspec.fits')

        if is_sp:
            sp1 = spectrum.SourceSpectrum(_wave, _flux_flam)
        else:
            sp1 = spectrum.SpectralElement(_wave, np.ones(_wave.shape))

        if ext_hdr is None:
            sp1.to_fits(outfile, clobber=True, trim_zero=False,
                        pad_zero_ends=False)
        else:
            sp1.to_fits(outfile, clobber=True, trim_zero=False,
                        pad_zero_ends=False, ext_header=ext_hdr)

        # Read it back in and check
        if is_sp:
            sp2 = spectrum.SourceSpectrum.from_file(outfile)
        else:
            sp2 = spectrum.SpectralElement.from_file(outfile)
            assert sp2.flux is sp2.thru

        np.testing.assert_allclose(sp2.wave.value, sp1.wave.value)
        np.testing.assert_allclose(sp2.flux.value, sp1.flux.value)
        assert sp2.wave.unit == sp1.wave.unit
        assert sp2.flux.unit == sp1.flux.unit

        hdr = fits.getheader(outfile, 1)
        assert 'expr' in hdr
        if ext_hdr is not None:
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
