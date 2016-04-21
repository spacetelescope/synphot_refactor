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

__all__ = ['BlackBody1D', 'ConstFlux1D', 'Empirical1D', 'GaussianAbsorption1D',
           'PowerLawFlux1D', 'Redshift']


# TODO: Use https://github.com/astropy/astropy/pull/1480 instead
class BlackBody1D(modeling.Fittable1DModel):
    """Create a :ref:`blackbody spectrum <synphot-planck-law>`
    model with given temperature.

    Parameters
    ----------
    temperature : float
        Blackbody temperature in Kelvin.

    """
    temperature = modeling.Parameter('temperature')

    def __init__(self, temperature, **kwargs):
        try:
            n_models = len(temperature)
        except TypeError:
            n_models = 1
        super(BlackBody1D, self).__init__(
            n_models=n_models, temperature=temperature, **kwargs)

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
                          for i in range(self._n_models)]).T

        return w

    @staticmethod
    def eval(x, temperature):
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
        wave = u.Quantity(np.ascontiguousarray(x), unit=u.AA)
        bbnu_flux = blackbody_nu(wave, temperature)

        # UNTIL HERE -- convert to bbfunc unit

        return bbflux.value


class ConstFlux1D(modeling.Parametric1DModel):
    """One dimensional constant flux model.

    Flux that is constant in a given unit might not be constant in
    another unit. During evaluation, flux is always converted to PHOTLAM.

    For multiple ``param_dim``, this model only accepts amplitudes of the
    same flux unit; e.g., ``[1, 2]`` or ``Quantity([1, 2], 'photlam')``.

    Parameters
    ----------
    amplitude : number or `~astropy.units.quantity.Quantity`
        Value and unit of the constant function.
        If not Quantity, assume the unit of PHOTLAM.

    """
    amplitude = modeling.Parameter('amplitude')

    def __init__(self, amplitude, **constraints):
        try:
            param_dim = len(amplitude)
        except TypeError:
            param_dim = 1

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
        super(ConstFlux1D, self).__init__(
            param_dim=param_dim, amplitude=a.value, **constraints)

    def eval(self, x, *args):
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

    @staticmethod
    def fit_deriv(x, amplitude):
        """One dimensional constant flux model derivative."""
        raise NotImplementedError('fit_deriv undefined ConstFlux1D.')


class Empirical1D(modeling.Model):
    """Empirical (sampled) spectrum or bandpass model.

    .. note::

        Only supports ``param_dim=1``.

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
    x = modeling.Parameter('x')
    y = modeling.Parameter('y')

    def __init__(self, x, y, keep_neg=False):
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
        self._x = x
        self._y = y
        super(Empirical1D, self).__init__(param_dim=1)

    @property
    def warnings(self):
        """Dictionary of warning key-value pairs."""
        return self._warnings

    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        return self._x

    @modeling.core.format_input
    def __call__(self, x):
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
        new_wave = np.ascontiguousarray(x)

        # Check whether given wavelengths are in descending order
        if np.isscalar(new_wave) or new_wave[0] < new_wave[-1]:
            newasc = True
        else:
            new_wave = new_wave[::-1]
            newasc = False

        # Interpolation flux/throughput
        if self._x[0] < self._x[-1]:
            oldasc = True
            resampled_result = np.interp(new_wave, self._x, self._y)
        else:
            oldasc = False
            rev = np.interp(new_wave, self._x[::-1], self._y[::-1])
            resampled_result = rev[::-1]

        # If the new and old wavelengths do not have the same parity,
        # the answer has to be flipped again.
        if newasc != oldasc:
            resampled_result = resampled_result[::-1]

        return resampled_result


# TODO: Use https://github.com/astropy/astropy/pull/2215 instead
class GaussianAbsorption1D(modeling.Parametric1DModel):
    """Gaussian absorption line model.

    .. math::

        f(x) = 1 - A e^{- \\frac{\\left(x - x_{0}\\right)^{2}}{2 \\sigma^{2}}}

    Parameters
    ----------
    amplitude : float
        Amplitude of the gaussian absorption.

    mean : float
        Mean of the gaussian.

    stddev : float
        Standard deviation of the gaussian.

    """
    amplitude = modeling.Parameter('amplitude')
    mean = modeling.Parameter('mean')
    stddev = modeling.Parameter('stddev')

    def __init__(self, amplitude, mean, stddev, **constraints):
        try:
            param_dim = len(amplitude)
        except TypeError:
            param_dim = 1
        super(GaussianAbsorption1D, self).__init__(
            param_dim=param_dim, amplitude=amplitude, mean=mean, stddev=stddev,
            **constraints)

    @property
    def sampleset(self):
        """``x`` array that samples the feature."""
        n = 50
        dw = 0.1 * self.stddev
        w1 = self.mean - n * dw
        w2 = self.mean + n * dw

        if self.param_dim == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = np.array([np.arange(w1[i], w2[i], dw[i])
                          for i in range(self.param_dim)]).T

        return w

    @staticmethod
    def eval(x, amplitude, mean, stddev):
        """GaussianAbsorption1D model function."""
        return 1.0 - modeling.models.Gaussian1D.eval(x, amplitude, mean, stddev)

    @staticmethod
    def fit_deriv(x, amplitude, mean, stddev):
        """GaussianAbsorption1D model function derivatives."""
        import operator
        return map(
            operator.neg,
            modeling.models.Gaussian1D.fit_deriv(x, amplitude, mean, stddev))


class PowerLawFlux1D(modeling.Parametric1DModel):
    """One dimensional power law model with proper flux handling.

    For multiple ``param_dim``, this model only accepts parameters of the
    same unit; e.g., ``amplitude=[1, 2]`` or
    ``amplitude=Quantity([1, 2], 'photlam')``.

    .. math::

        f(x) = A (x / x_0) ^ {-\\alpha}

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
    amplitude = modeling.Parameter('amplitude')
    x_0 = modeling.Parameter('x_0')
    alpha = modeling.Parameter('alpha')

    def __init__(self, amplitude, x_0, alpha, **constraints):
        try:
            param_dim = len(amplitude)
        except TypeError:
            param_dim = 1

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
            param_dim=param_dim, amplitude=amplitude.value, x_0=x_0,
            alpha=alpha, **constraints)

    def eval(self, x, *args):
        """Return flux in PHOTLAM."""
        xx = x / self.x_0
        y = u.Quantity(self.amplitude * xx ** (-self.alpha), self._flux_unit)
        flux = units.convert_flux(x, y, units.PHOTLAM)
        return flux.value

    @staticmethod
    def fit_deriv(x, amplitude, x_0, alpha):
        """One dimensional power law derivative with respect to parameters."""
        raise NotImplementedError('fit_deriv undefined PowerLawFlux1D.')


# TODO: Use https://github.com/astropy/astropy/pull/2176 instead
class Redshift(modeling.Parametric1DModel):
    """Apply redshift to wavelength.

    .. math::

        \\lambda_{obs} = (1 + z) \\lambda_{rest}

    Parameters
    ----------
    z : float or a list of floats
        Redshift value(s).

    """
    z = modeling.Parameter('z')

    def __init__(self, z, **constraints):
        if not isinstance(z, collections.Sequence):
            param_dim = 1
        else:
            param_dim = len(z)
        super(Redshift, self).__init__(param_dim=param_dim, z=z, **constraints)

    @staticmethod
    def eval(x, z):
        """One dimensional Redshift model function."""
        return (1 + z) * x

    @staticmethod
    def fit_deriv(x, z):
        """One dimensional Redshift model derivative."""
        d_z = x
        return [d_z]

    def inverse(self):
        """Inverse Redshift model."""
        if self.param_dim == 1:
            return Redshift(z=1.0 / (1.0 + self.z) - 1.0)
        else:
            return Redshift(z=[1.0 / (1.0 + z) - 1.0 for z in self.z])
