# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Spectrum models not in `astropy.modeling`."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# STDLIB
import collections
import warnings

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import modeling
from astropy import units as u
from astropy.analytic_functions.blackbody import blackbody_nu
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from . import units

__all__ = ['BlackBody1D', 'Box1D', 'ConstFlux1D', 'Empirical1D', 'Gaussian1D',
           'GaussianAbsorption1D', 'Lorentz1D', 'MexicanHat1D',
           'PowerLawFlux1D', 'Trapezoid1D']


class BlackBody1D(modeling.Fittable1DModel):
    """Create a :ref:`blackbody spectrum <synphot-planck-law>`
    model with given temperature.

    Parameters
    ----------
    temperature : float
        Blackbody temperature in Kelvin.

    """
    temperature = modeling.Parameter(default=5000)

    @property
    def lambda_max(self):
        """Peak wavelength in Angstrom when the curve is expressed as
        power density."""
        return u.Quantity(const.b_wien.value / self.temperature, u.m).to(
            u.AA).value

    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        w0 = self.lambda_max
        w2 = np.log10(w0 + 10 * w0)

        if self._n_models == 1:
            w = np.logspace(0, w2, num=1000)
        else:
            w = np.array([np.logspace(0, w2[i], num=1000)
                          for i in range(self._n_models)])

        return w

    @staticmethod
    def evaluate(x, temperature):
        """Evaluate the model.

        Parameters
        ----------
        x : number or ndarray
            Wavelengths in Angstrom.

        temperature : number
            Temperature in Kelvin.

        Returns
        -------
        y : number or ndarray
            Blackbody radiation in PHOTLAM per steradian.

        """
        # Silence Numpy
        old_np_err_cfg = np.seterr(all='ignore')

        wave = u.Quantity(np.ascontiguousarray(x), unit=u.AA)
        bbnu_flux = blackbody_nu(wave, temperature)
        bbflux = (bbnu_flux * u.sr).to(
            units.PHOTLAM, u.spectral_density(wave)) / u.sr  # PHOTLAM/sr

        # Restore Numpy settings
        dummy = np.seterr(**old_np_err_cfg)

        return bbflux.value


class Box1D(modeling.models.Box1D):
    """Same as `astropy.modeling.models.Box1D`, except with
    ``sampleset`` defined.

    """
    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        step = 0.01
        dw = 0.5 * self.width
        w1 = self.x_0 - dw
        w2 = self.x_0 + dw

        if self._n_models == 1:
            w = np.array([w1 - step, w1, w2, w2 + step])
        else:
            w = np.array([[w1[i] - step[i], w1[i], w2[i], w2[i] + step[i]]
                          for i in range(self._n_models)])

        return w


class ConstFlux1D(modeling.models.Const1D):
    """One dimensional constant flux model.

    Flux that is constant in a given unit might not be constant in
    another unit. During evaluation, flux is always converted to PHOTLAM.

    For multiple ``n_models``, this model only accepts amplitudes of the
    same flux unit; e.g., ``[1, 2]`` or ``Quantity([1, 2], 'photlam')``.

    Parameters
    ----------
    amplitude : number or `~astropy.units.quantity.Quantity`
        Value and unit of the constant function.
        If not Quantity, assume the unit of PHOTLAM.

    """
    def __init__(self, amplitude, **kwargs):
        if not isinstance(amplitude, u.Quantity):
            amplitude = u.Quantity(amplitude, units.PHOTLAM)

        in_unit_name = amplitude.unit.to_string()

        if in_unit_name == units.STMAG.to_string():
            a = units.convert_flux(1, amplitude, units.FLAM)
        elif in_unit_name == units.ABMAG.to_string():
            a = units.convert_flux(1, amplitude, units.FNU)
        elif (amplitude.unit.physical_type in
              ('spectral flux density', 'spectral flux density wav',
               'photon flux density', 'photon flux density wav')):
            a = amplitude
        else:
            raise NotImplementedError('{0} not supported.'.format(in_unit_name))

        self._flux_unit = a.unit
        super(ConstFlux1D, self).__init__(amplitude=a.value, **kwargs)

    def evaluate(self, x, *args):
        """One dimensional constant flux model function.

        Parameters
        ----------
        x : number or ndarray
            Wavelengths in Angstrom.

        Returns
        -------
        y : number or ndarray
            Flux in PHOTLAM.

        """
        a = u.Quantity(self.amplitude * np.ones_like(x), self._flux_unit)
        y = units.convert_flux(x, a, units.PHOTLAM)
        return y.value


class Empirical1D(modeling.Fittable1DModel):
    """Empirical (sampled) spectrum or bandpass model.

    .. note::

        This model requires `SciPy <http://www.scipy.org>`_ to be installed.

    Parameters
    ----------
    x : ndarray
        Wavelengths.

    y : ndarray
        Flux or throughput.

    keep_neg : bool
        Convert negative ``y`` values to zeroes?
        This is to be consistent with ASTROLIB PYSYNPHOT.

    """
    x = modeling.Parameter(default=0)
    y = modeling.Parameter(default=0)

    def __init__(self, x, y, keep_neg=False, **kwargs):
        from scipy.interpolate import interp1d

        y = np.asarray(y)

        if not keep_neg:
            i = np.where(y < 0)
            n_neg = len(i[0])
            if n_neg > 0:
                y[i] = 0
                warn_str = ('{0} bin(s) contained negative flux or throughput; '
                            'it/they will be set to zero.'.format(n_neg))
                self._warnings = {'NegativeFlux': warn_str}
                warnings.warn(warn_str, AstropyUserWarning)

        # Need this to work around the output shape guessing based on model
        # parameters. In this model, the shape is determined by input into
        # evaluate(), not parameters.
        self._f = interp1d(x, y)

        # Do not pass in parameters here (see comment above).
        super(Empirical1D, self).__init__(**kwargs)

    @property
    def warnings(self):
        """Dictionary of warning key-value pairs."""
        return self._warnings

    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        return self._f.x

    def evaluate(self, x, *args):
        """Evaluate the model.

        Parameters
        ----------
        x : number or ndarray
            Wavelengths in same unit as parameter ``x``.

        Returns
        -------
        resampled_result : number or ndarray
            Flux or throughput in same unit as parameter ``y``.

        """
        return self._f(x)


class GaussianSamplesetMixin(object):
    """Mixin class to define ``sampleset`` for Gaussian models."""
    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        n = 50
        dw = 0.1 * self.stddev
        w1 = self.mean - n * dw
        w2 = self.mean + n * dw

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = np.array([np.arange(w1[i], w2[i], dw[i])
                          for i in range(self._n_models)])

        return w


class Gaussian1D(modeling.models.Gaussian1D, GaussianSamplesetMixin):
    """Same as `astropy.modeling.models.Gaussian1D`, except with
    ``sampleset`` defined.

    """
    pass


class GaussianAbsorption1D(modeling.models.GaussianAbsorption1D,
                           GaussianSamplesetMixin):
    """Same as `astropy.modeling.models.GaussianAbsorption1D`, except with
    ``sampleset`` defined.

    """
    pass


class Lorentz1D(modeling.models.Lorentz1D):
    """Same as `astropy.modeling.models.Lorentz1D`, except with
    ``sampleset`` defined.

    """
    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        n = 50
        dw = 0.1 * 2.355 * self.fwhm
        w1 = self.x_0 - n * dw
        w2 = self.x_0 + n * dw

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = np.array([np.arange(w1[i], w2[i], dw[i])
                          for i in range(self._n_models)])

        return w


class MexicanHat1D(modeling.models.MexicanHat1D):
    """Same as `astropy.modeling.models.MexicanHat1D`, except with
    ``sampleset`` defined.

    """
    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        n = 50
        dw = 0.1 * self.sigma
        w1 = self.x_0 - n * dw
        w2 = self.x_0 + n * dw

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = np.array([np.arange(w1[i], w2[i], dw[i])
                          for i in range(self._n_models)])


class PowerLawFlux1D(modeling.models.PowerLaw1D):
    """One dimensional power law model with proper flux handling.

    For multiple ``n_models``, this model only accepts parameters of the
    same unit; e.g., ``amplitude=[1, 2]`` or
    ``amplitude=Quantity([1, 2], 'photlam')``.

    Also see `~astropy.modeling.models.powerlaws.PowerLaw1D`.

    Parameters
    ----------
    amplitude : number or `~astropy.units.quantity.Quantity`
        Model amplitude at the reference point.
        If not Quantity, assume the unit of PHOTLAM.

    x_0 : number or `~astropy.units.quantity.Quantity`
        Reference point.
        If not Quantity, assume the unit of Angstrom.

    alpha : float
        Power law index.

    """
    def __init__(self, amplitude, x_0, alpha, **kwargs):
        if not isinstance(amplitude, u.Quantity):
            amplitude = u.Quantity(amplitude, units.PHOTLAM)

        if ((amplitude.unit.to_string() in
             (units.STMAG.to_string(), units.ABMAG.to_string())) or
            (amplitude.unit.physical_type in
             ('spectral flux density', 'spectral flux density wav',
              'photon flux density', 'photon flux density wav'))):
            self._flux_unit = amplitude.unit
        else:
            raise NotImplementedError(
                '{0} not supported.'.format(amplitude.unit))

        if isinstance(x_0, u.Quantity):
            x_0 = x_0.to(u.AA, u.spectral()).value

        super(PowerLawFlux1D, self).__init__(
            amplitude=amplitude.value, x_0=x_0, alpha=alpha, **kwargs)

    def evaluate(self, x, *args):
        """Return flux in PHOTLAM. Assume input wavelength is in Angstrom."""
        xx = x / self.x_0
        y = u.Quantity(self.amplitude * xx ** (-self.alpha), self._flux_unit)
        flux = units.convert_flux(x, y, units.PHOTLAM)
        return flux.value


class Trapezoid1D(modeling.models.Trapezoid1D):
    """Same as `astropy.modeling.models.Trapezoid1D`, except with
    ``sampleset`` defined.

    """
    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        x2 = self.x_0 - self.width * 0.5
        x3 = self.x_0 + self.width * 0.5
        x1 = x2 - self.amplitude / self.slope
        x4 = x3 + self.amplitude / self.slope

        if self._n_models == 1:
            w = [x1[0], x2, x3, x4[0]]
        else:
            w = np.array([[x1[i], x2[i], x3[i], x4[i]]
                          for i in range(self._n_models)])

        return w
