# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test different integration methods.
Things not covered here but somewhere else:

* ``conf.set_temp('default_integrator', 'analytical')`` and its default
  covered in ``spectrum.rst``.
* The following integrations are tested in ``test_spectrum.py``:
    * ``BlackBodyNorm1D`` source, and indirectly, ``BlackBody1D``.
    * ``Box1D`` bandpass.
    * ``Empirical1D`` source and bandpass.
    * ``GaussianFlux1D`` source.
    * ``PowerLawFlux1D`` source.
    * Compound source and bandpass.

"""

# THIRD-PARTY
import numpy as np
import pytest
from astropy import units as u
from astropy.modeling.models import Const1D
from astropy.tests.helper import assert_quantity_allclose
from numpy.testing import assert_allclose

# LOCAL
from synphot import models, units
from synphot.exceptions import SynphotError
from synphot.spectrum import SourceSpectrum, SpectralElement


class TestSourceConstFlux1D:
    def setup_class(self):
        self.sp = SourceSpectrum(models.ConstFlux1D, amplitude=1 * units.FLAM)
        self.w = np.arange(5499, 5600) * u.AA
        self.ans_flam = 100 * (u.erg / (u.cm * u.cm * u.s))
        self.ans_photlam = 2.79343128e+13 * (u.ph / (u.cm * u.cm * u.s))

    def test_integrate(self):
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w), self.ans_photlam)
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w, flux_unit='flam'),
            self.ans_flam)
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w, flux_unit='flam',
                              integration_type='analytical'),
            self.ans_flam)

        with pytest.raises(SynphotError, match='cannot operate in Jy'):
            self.sp.integrate(wavelengths=self.w, flux_unit=u.Jy)

    @pytest.mark.xfail(reason='Cannot convert to PHOTLAM')
    def test_integrate_wontfix(self):
        """Constant spectrum in FLAM is not constant in PHOTLAM, so cannot
        apply simple unit conversion to integrated flux.
        """
        assert_quantity_allclose(
            self.sp.integrate(wavelengths=self.w,
                              integration_type='analytical'),
            self.ans_photlam)

    def test_integrate_freq_space(self):
        """When flux is constant in frequency space."""
        sp = SourceSpectrum(models.ConstFlux1D, amplitude=1 * u.Jy)
        nu = self.w.to(u.Hz, u.spectral())

        # Answer in this setup is basically
        # ((max(nu) - min(nu)) * u.Jy).to(u.erg / (u.cm * u.cm * u.s))
        ans_flam = 9.73703017e-11 * (u.erg / (u.cm * u.cm * u.s))

        assert_quantity_allclose(
            sp.integrate(wavelengths=self.w, flux_unit='flam'), ans_flam)
        assert_quantity_allclose(
            sp.integrate(wavelengths=self.w, flux_unit='flam',
                         integration_type='analytical'),
            ans_flam)
        assert_quantity_allclose(
            sp.integrate(wavelengths=nu, flux_unit='flam'), ans_flam)
        assert_quantity_allclose(
            sp.integrate(wavelengths=nu, flux_unit='flam',
                         integration_type='analytical'),
            ans_flam)


def test_bandpass_Const1D():
    """Test Const1D bandpass and a few optional logic routes."""
    bp = SpectralElement(Const1D, amplitude=1)
    w = np.arange(5499, 5600) * u.AA
    ans = 100 * u.AA

    assert_quantity_allclose(bp.integrate(wavelengths=w), ans)

    # Const1D from astropy has no integrate method, so this silently falls
    # back to trapezoid integration anyway.
    assert_quantity_allclose(
        bp.integrate(wavelengths=w, integration_type='analytical'), ans)

    with pytest.raises(SynphotError, match='waveset is undefined'):
        bp.integrate()

    with pytest.raises(SynphotError, match='flux_unit cannot be used'):
        bp.integrate(wavelengths=w, flux_unit='flam')

    with pytest.raises(NotImplementedError,
                       match='not a supported integration type'):
        bp.integrate(wavelengths=w, integration_type='notreal')


def test_bandpass_Gaussian1D():
    bp = SpectralElement(
        models.Gaussian1D, amplitude=0.8, mean=5000, stddev=130)
    ans = 260.68913672 * u.AA
    assert_quantity_allclose(bp.integrate(), ans)
    assert_quantity_allclose(bp.integrate(integration_type='analytical'), ans,
                             rtol=1e-6)

    # Equivalent width is basically the integral.
    assert_quantity_allclose(bp.equivwidth(), ans)
    assert_quantity_allclose(bp.equivwidth(integration_type='analytical'), ans,
                             rtol=1e-6)


def test_bandpass_Lorentz1D():
    bp = SpectralElement(models.Lorentz1D, amplitude=0.8, x_0=5000, fwhm=130)
    ans = 161.28101053 * u.AA
    assert_quantity_allclose(bp.integrate(), ans)
    assert_quantity_allclose(bp.integrate(integration_type='analytical'), ans)


def test_source_Lorentz1D():
    sp = SourceSpectrum(
        models.Lorentz1D, amplitude=1 * units.PHOTLAM, x_0=5000, fwhm=130)
    ans_photlam = 201.60126316 * (u.ph / (u.cm * u.cm * u.s))
    ans_flam = 8.06013348e-10 * (u.erg / (u.cm * u.cm * u.s))

    assert_quantity_allclose(sp.integrate(), ans_photlam)
    assert_quantity_allclose(sp.integrate(flux_unit='flam'), ans_flam)
    assert_quantity_allclose(
        sp.integrate(integration_type='analytical'), ans_photlam)

    # Flux unit conversion is iffy here because we do not have proper
    # LorentzFlux1D model.
    assert_quantity_allclose(
        sp.integrate(flux_unit='flam', integration_type='analytical'),
        ans_flam, rtol=0.01)


def test_bandpass_RickerWavelet1D():
    """Does not make much sense when transmission is negative, so this
    makes more sense as equivalent width calculation, which is also the
    integral.
    """
    bp = SpectralElement(
        models.RickerWavelet1D, amplitude=1, x_0=5000, sigma=100)
    ans = 242.20770777 * u.AA
    assert_quantity_allclose(bp.equivwidth(), ans)
    assert_quantity_allclose(bp.equivwidth(integration_type='analytical'),
                             ans, rtol=5e-3)

    with pytest.raises(NotImplementedError, match='Partial analytic'):
        bp.equivwidth(integration_type='analytical',
                      wavelengths=np.arange(4900, 5200) * u.AA)

    with pytest.raises(NotImplementedError, match='Partial analytic'):
        bp.equivwidth(integration_type='analytical',
                      wavelengths=np.arange(4800, 5100) * u.AA)


def test_source_RickerWavelet1D():
    pytest.xfail(
        'Not sure if this test makes sense as negative flux is unphysical')


def test_bandpass_Trapezoid1D():
    """Trapezoid integration of a trapezoid. How meta!"""
    bp = SpectralElement(
        models.Trapezoid1D, amplitude=0.8, x_0=5000, width=10, slope=0.25)
    ans = 10.56 * u.AA
    assert_quantity_allclose(bp.integrate(), ans)
    assert_quantity_allclose(bp.integrate(integration_type='analytical'), ans)


def test_trapz_box1d():
    """Test the underlying trapezoid integration."""
    m = models.Box1D(amplitude=1, x_0=5000, width=10)

    # Ascending.
    x = m.sampleset()
    assert_allclose(np.trapz(m(x), x=x), 10)

    # Descending.
    x2 = x[::-1]
    assert_allclose(abs(np.trapz(m(x2), x=x2)), 10)
