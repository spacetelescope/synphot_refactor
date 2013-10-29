# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test analytic.py module."""
from __future__ import division, print_function

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import modeling
from astropy import units as u
from astropy.tests.helper import pytest

# LOCAL
from .. import analytic, exceptions, spectrum, units
from ..utils import generate_wavelengths


def test_factory_exceptions():
    """The rest of the factory is indirectly tested below."""
    # Wrong mixin class
    with pytest.raises(exceptions.SynphotError):
        cls = analytic.class_factory(
            spectrum.SourceSpectrum, modeling.models.Const1DModel)

    # Wrong modeling class
    with pytest.raises(exceptions.SynphotError):
        cls = analytic.class_factory(
            analytic.MixinAnalyticSource, spectrum.SourceSpectrum)


class TestMixinAnalytic(object):
    """Test MixinAnalytic classes without modeling component."""
    def setup_class(self):
        """Since BaseMixinAnalytic cannot be used directly,
        we test base class methods using one of the subclasses.

        """
        self.source = analytic.MixinAnalyticSource(
            flux_unit=units.PHOTLAM, wave_unit=u.micron, area=10.0)
        self.source_flam = analytic.MixinAnalyticFlamSource()
        self.passband = analytic.MixinAnalyticPassband()

    def test_init(self):
        assert (self.source._spec_cls == self.source_flam._spec_cls ==
                spectrum.SourceSpectrum)
        assert self.passband._spec_cls == spectrum.SpectralElement

        assert self.source.flux_unit == units.PHOTLAM
        assert self.source_flam.flux_unit == units.FLAM
        assert self.passband.flux_unit == units.THROUGHPUT

        assert self.source.wave_unit == u.micron
        assert self.source_flam.wave_unit == self.passband.wave_unit == u.AA

        assert self.source.primary_area == 10
        assert self.source_flam.primary_area is None
        assert self.passband.primary_area is None

    def test_flux_setter(self):
        self.source.flux_unit = 'Jy'
        assert self.source.flux_unit == u.Jy

        with pytest.raises(exceptions.SynphotError):
            self.source.flux_unit = u.AA

        with pytest.raises(AttributeError):
            self.source_flam.flux_unit = u.Jy

        with pytest.raises(AttributeError):
            self.passband.flux_unit = u.Jy

    def test_wave_setter(self):
        with pytest.raises(AttributeError):
            self.source.wave_unit = u.Hz

    def test_area_setter(self):
        self.source.primary_area = u.Quantity(42.0, units.AREA)
        assert self.source.primary_area.value == 42
        assert self.source.primary_area.unit == units.AREA


class TextBox(object):
    """Test Box1DSpectrum class."""
    def setup_class(self):
        self.box = analytic.Box1DSpectrum(1, 5000, 100)

    def test_data_points(self):
        assert self.box.flux_unut == units.THROUGHPUT
        assert self.box.wave_unit == u.AA

        # Box: Outside, boundary, inside
        thru = self.box.sample([4000, 4949.95, 5000])
        np.testing.assert_array_equal(thru.value, [0, 0, 1])

    def test_metadata(self):
        sp = self.box.to_spectrum(
            [4949.95, 4950.0, 4950.1, 5049.9, 5050.0, 5050.1])

        assert 'Box' in self.bp.metadata['expr']

    def test_conversion(self):
        box = analytic.Box1DSpectrum(1, 500, 10, wave_unit=u.nm)
        assert box.wave_unit == u.nm

        wave = generate_wavelengths(
            minwave=4949, maxwave=5052, delta=1.0, log=False)[0]
        thru1 = self.box.sample(wave)
        thru2 = box.sample(wave)
        np.testing.assert_array_equal(thru1.value, thru2.value)

    def test_multi_param_sets(self):
        box = analytic.Box1DSpectrum([1, 0.5], [5000, 6000], [100, 50])
        specs = box.to_spectrum([4940, 5000, 6000, 6030])
        np.testing.assert_array_equal(specs[0].flux.value, [0, 1, 0, 0])
        np.testing.assert_array_equal(specs[1].flux.value, [0, 0, 0.5, 1])


class TestBlackBody(object):
    """Test BlackBody1DSpectrum class, that uses BlackBody1DModel."""
    def setup_class(self):
        bb = analytic.BlackBody1DSpectrum(5500)
        refwave = generate_wavelengths(
            minwave=3000, maxwave=3100, delta=10, log=False)[0]
        self.sp = bb.to_spectrum(refwave)
        self.totalflux = self.sp.integrate()  # FLAM
        self.sp.convert_flux(units.PHOTLAM)

    def test_data_points(self):
        np.testing.assert_allclose(
            self.sp.flux.value,
            [0.00019318, 0.00019623, 0.0001993, 0.00020238, 0.00020549,
             0.00020861, 0.00021175, 0.00021491, 0.00021809, 0.00022128],
            rtol=2.5e-3)

    def test_metadata(self):
        assert 'BlackBody' in self.sp.metadata['expr']

    def test_conversion(self):
        self.sp.convert_wave(u.Hz)
        self.sp.convert_flux(units.FNU)
        totalflux = self.sp.integrate()
        np.testing.assert_allclose(
            self.totalflux.value, totalflux.value, rtol=2.5e-5)

    def test_multi_param_sets(self):
        bb = analytic.BlackBody1DSpectrum([5500, 6000])
        specs = bb.to_spectrum([4940, 5000, 6000, 6030])
        np.testing.assert_allclose(
            specs[0].flux.value,
            [3.25640962e-15, 3.26787057e-15, 3.16458162e-15, 3.15522005e-15],
            rtol=1e-6)
        np.testing.assert_allclose(
            specs[1].flux.value,
            [5.07696242e-15, 5.06863567e-15, 4.57696300e-15, 4.55560172e-15],
            rtol=1e-6)


class TestFlatSpectrum(object):
    """Test :func:`flat_spectrum`, which uses Const1DSpectrum."""
    def setup_class(self):
        self.wave = [1000.0, 5000.0, 9000.0]

    @pytest.mark.parametrize(
        ('flux_unit'),
        [units.PHOTLAM, units.PHOTNU, units.FLAM, units.FNU, u.Jy, u.mJy])
    def test_linear_density(self, flux_unit):
        flat = analytic.flat_spectrum(flux_unit)
        sp = flat.to_spectrum(self.wave)
        assert flat.flux_unit == flux_unit
        assert flat.wave_unit == u.AA
        assert np.all(sp.flux.value == 1)
        assert 'Const1D' in sp.metadata['expr']

    def test_stmag(self):
        flat = analytic.flat_spectrum(units.STMAG)
        flux = flat.sample(self.wave)
        assert flat.flux_unit == units.FLAM
        np.testing.assert_allclose(flux.value, 3.63e-9, rtol=2.5e-4)

    def test_abmag(self):
        flat = analytic.flat_spectrum(units.ABMAG)
        flux = flat.sample(self.wave)
        assert flat.flux_unit == units.FNU
        np.testing.assert_allclose(flux.value, 3.63e-20, rtol=2.5e-4)

    @pytest.mark.parametrize(
        ('flux_unit'), [u.count, units.OBMAG, units.VEGAMAG])
    def test_nondensity_vegamag(self, flux_unit):
        """These units are not supported anymore."""
        with pytest.raises(exceptions.SynphotError):
            flat = analytic.flat_spectrum(flux_unit)

    def test_conversion(self):
        """Flat spectrum in FLAM is not flat in FNU."""
        flat = analytic.flat_spectrum(units.FLAM)
        sp = flat.to_spectrum(self.wave)
        sp.convert_flux(units.FNU)
        meanflux = sp.flux.value.mean()
        assert not np.allclose(meanflux, 1, rtol=1e-4)

    def test_multi_param_sets(self):
        """:func:`flat_spectrum` does not support multi params sets,
        but Const1DSpectrum does.

        """
        flat = analytic.Const1DSpectrum([1.0, 0.5])
        specs = flat.to_spectrum(self.wave)
        np.testing.assert_array_equal(specs[0].flux.value, 1)
        np.testing.assert_array_equal(specs[1].flux.value, 0.5)


class TestGaussian(object):
    """Test :func:`gaussian_spectrum` function, which uses
    Gaussian1DSpectrum.

    """
    def setup_class(self):
        self.gauss = analytic.gaussian_spectrum(
            u.Quantity(1, units.PHOTLAM), 4000, 100)
        self.refwave = u.Quantity(np.arange(3800.0, 4200.0), unit=u.AA)
        self.sp = self.gauss.to_spectrum(self.refwave)

    def test_data_points(self):
        flux = self.gauss.sample([3900, 4000, 4060])
        assert self.gauss.flux_unit == units.PHOTLAM
        assert self.gauss.wave_unit == u.AA
        np.testing.assert_allclose(
            flux.value, [0.00058715, 0.00939437, 0.00346246], rtol=1e-5)

    def test_metadata(self):
        assert 'Gaussian' in self.sp.metadata['expr']

    def test_totalflux(self):
        np.testing.assert_allclose(self.sp.integrate(), 1, rtol=1e-5)

        gauss = analytic.gaussian_spectrum(1, 4000, 100)
        sp = gauss.to_spectrum(self.refwave)
        assert gauss.flux_unit == units.FLAM
        np.testing.assert_allclose(sp.integrate(), 1, rtol=1e-5)

    def test_symmetry(self):
        flux = self.gauss.sample(u.Quantity([3950, 4050], u.AA))
        np.testing.assert_allclose(flux.value[0], flux.value[1])

    def test_conversion(self):
        gauss = analytic.gaussian_spectrum(
            u.Quantity(1, units.PHOTLAM), u.Quantity(400, u.nm), 10)
        flux = gauss.sample(self.refwave)
        assert gauss.wave_unit == u.nm
        np.testing.assert_allclose(flux.value, self.sp.flux.value * 10)

    def test_multi_param_sets(self):
        gauss = analytic.gaussian_spectrum(
            [1.0, 0.5], [4000.0, 4050.0], [100.0, 25.0])
        specs = gauss.to_spectrum([3900, 4000, 4050, 4150])
        np.testing.assert_allclose(
            specs[0].flux.value,
            [5.87148299e-04, 9.39437279e-03, 4.69718639e-03, 1.83483843e-05],
            rtol=1e-6)
        np.testing.assert_allclose(
            specs[1].flux.value,
            [0, 2.86693505e-07, 1.87887456e-02, 0],
            rtol=1e-6, atol=1e-20)


class TestPowerLaw(object):
    """Test PowerLaw1DSpectrum class."""
    def setup_class(self):
        self.powlaw = analytic.PowerLaw1DSpectrum(
            1, 6000, 4, flux_unit=units.PHOTLAM)
        self.refwave = generate_wavelengths(
            minwave=3000, maxwave=3100, delta=10, log=False)[0]
        self.sp = self.powlaw.to_spectrum(self.refwave)

    def test_data_points(self):
        assert self.powlaw.flux_unit == units.PHOTLAM
        assert self.powlaw.wave_unit == u.AA
        np.testing.assert_allclose(
            self.sp.flux.value,
            [16, 15.78843266, 15.58035072, 15.37568551, 15.17436992,
             14.97633838, 14.78152682, 14.5898726, 14.40131453, 14.21579277],
            rtol=1e-6)

    def test_metadata(self):
        assert 'PowerLaw' in self.sp.metadata['expr']

    def test_normalization(self):
        flux = self.powlaw.sample(6000)
        np.testing.assert_allclose(flux.value, 1, rtol=1e-6)

    def test_conversion(self):
        wave = self.refwave.to(u.nm)
        flux = self.powlaw.sample(wave)
        np.testing.assert_allclose(flux.value, self.sp.flux.value)

    def test_multi_param_sets(self):
        powlaw = analytic.PowerLaw1DSpectrum([1, 1], [3000, 3050], [4, 1])
        specs = powlaw.to_spectrum(self.refwave)
        np.testing.assert_allclose(
            specs[0].flux.value,
            [1, 0.98677704, 0.97377192, 0.96098034, 0.94839812,
             0.93602115, 0.92384543, 0.91186704, 0.90008216, 0.88848705],
            rtol=1e-6)
        np.testing.assert_allclose(
            specs[1].flux.value,
            [1.01666667, 1.01328904, 1.00993377, 1.00660066, 1.00328947,
             1, 0.99673203, 0.99348534, 0.99025974, 0.98705502],
            rtol=1e-6)
