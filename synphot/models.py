# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Spectrum models not in `astropy.modeling`."""
from __future__ import absolute_import, division, print_function
from .extern.six.moves import map, zip

# STDLIB
import warnings
from collections import defaultdict
from copy import deepcopy
from functools import partial

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import units as u
from astropy.analytic_functions.blackbody import blackbody_nu
from astropy.modeling import Fittable1DModel, Model, Parameter
from astropy.modeling import models as _models
from astropy.modeling.core import _CompoundModel
from astropy.stats.funcs import gaussian_fwhm_to_sigma, gaussian_sigma_to_fwhm
from astropy.utils import metadata
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from . import units
from .exceptions import SynphotError
from .utils import merge_wavelengths

__all__ = ['BlackBody1D', 'BlackBodyNorm1D', 'Box1D', 'ConstFlux1D',
           'Empirical1D', 'Gaussian1D', 'GaussianAbsorption1D',
           'GaussianFlux1D', 'Lorentz1D', 'MexicanHat1D', 'PowerLawFlux1D',
           'Trapezoid1D', 'get_waveset', 'get_metadata']


class BlackBody1D(Fittable1DModel):
    """Create a :ref:`blackbody spectrum <synphot-planck-law>`
    model with given temperature.

    Parameters
    ----------
    temperature : float
        Blackbody temperature in Kelvin.

    """
    temperature = Parameter(default=5000)

    def __init__(self, *args, **kwargs):
        super(BlackBody1D, self).__init__(*args, **kwargs)
        self.meta['expr'] = 'bb({0})'.format(self.temperature)

    @property
    def lambda_max(self):
        """Peak wavelength in Angstrom when the curve is expressed as
        power density."""
        return u.Quantity(const.b_wien.value / self.temperature, u.m).to(
            u.AA).value

    def bounding_box(self, factor=10.0):
        """Tuple defining the default ``bounding_box`` limits,
        ``(x_low, x_high)``.

        .. math::

            x_{\\textnormal{low}} = 0

            x_{\\textnormal{high}} = \\log(\\lambda_{\\textnormal{max}} \\;\
            (1 + \\textnormal{factor}))

        Parameters
        ----------
        factor : float
            Used to calculate ``x_high``.

        """
        w0 = self.lambda_max
        return (w0 * 0, np.log10(w0 + factor * w0))

    @staticmethod
    def _calc_sampleset(w1, w2, num):
        """Calculate sampleset for each model."""
        return np.logspace(w1, w2, num=num)

    def sampleset(self, factor_bbox=10.0, num=1000):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        factor_bbox : float
            Factor for ``bounding_box`` calculations.

        num : int
            Number of points to generate.

        """
        w1, w2 = self.bounding_box(factor=factor_bbox)

        if self._n_models == 1:
            w = self._calc_sampleset(w1, w2, num)
        else:
            f = partial(self._calc_sampleset, num=num)
            w = list(map(f, w1, w2))

        return np.asarray(w)

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


class BlackBodyNorm1D(BlackBody1D):
    """Create a normalized :ref:`blackbody spectrum <synphot-planck-law>`
    with given temperature.

    It is normalized by multiplying `BlackBody1D` result with a solid angle,
    :math:`\\Omega`, as defined below, where :math:`d` is 1 kpc:

    .. math::

        \\Omega = \\frac{\\pi R_{\\textnormal{Sun}}^{2}}{d^{2}}

    Parameters
    ----------
    temperature : float
        Blackbody temperature in Kelvin.

    """
    def __init__(self, *args, **kwargs):
        super(BlackBodyNorm1D, self).__init__(*args, **kwargs)
        self._omega = np.pi * (const.R_sun / const.kpc).value ** 2  # steradian

    def evaluate(self, x, temperature):
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
            Blackbody radiation in PHOTLAM.

        """
        bbflux = super(BlackBodyNorm1D, self).evaluate(x, temperature)
        return bbflux * self._omega


class Box1D(_models.Box1D):
    """Same as `astropy.modeling.models.Box1D`, except with
    ``sampleset`` defined.

    """
    @staticmethod
    def _calc_sampleset(w1, w2, step, minimal):
        """Calculate sampleset for each model."""
        if minimal:
            arr = [w1 - step, w1, w2, w2 + step]
        else:
            arr = np.arange(w1 - step, w2 + step, step)

        return arr

    def sampleset(self, step=0.01, minimal=False):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        step : float
            Distance of first and last points w.r.t. bounding box.

        minimal : bool
            Only return the minimal points needed to define the box;
            i.e., box edges and a point outside on each side.

        """
        w1, w2 = self.bounding_box

        if self._n_models == 1:
            w = self._calc_sampleset(w1, w2, step, minimal)
        else:
            f = partial(self._calc_sampleset, step=step, minimal=minimal)
            w = list(map(f, w1, w2))

        return np.asarray(w)


class ConstFlux1D(_models.Const1D):
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

        if in_unit_name == u.STmag.to_string():
            a = units.convert_flux(1, amplitude, units.FLAM)
        elif in_unit_name == u.ABmag.to_string():
            a = units.convert_flux(1, amplitude, units.FNU)
        elif (amplitude.unit.physical_type in
              ('spectral flux density', 'spectral flux density wav',
               'photon flux density', 'photon flux density wav')):
            a = amplitude
        else:
            raise NotImplementedError(
                '{0} not supported.'.format(in_unit_name))

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


# TODO: Subclass from LookupTable (spacetelescope/gwcs#28)
class Empirical1D(Fittable1DModel):
    """Empirical (sampled) spectrum or bandpass model.

    .. note::

        This model requires `SciPy <http://www.scipy.org>`_ 0.17
        or later to be installed.

    Parameters
    ----------
    x : ndarray
        Wavelengths.

    y : ndarray
        Flux or throughput.

    keep_neg : bool
        Convert negative ``y`` values to zeroes?
        This is to be consistent with ASTROLIB PYSYNPHOT.

    kwargs : dict
        Optional keywords for model creation or
        :func:`~scipy.interpolate.interp1d`.

    """
    standard_broadcasting = False
    x = Parameter(default=[0, 0])
    y = Parameter(default=[0, 0])

    def __init__(self, x, y, **kwargs):
        n_models = kwargs.get('n_models', 1)
        if n_models > 1:
            raise NotImplementedError('Only n_models=1 is supported')

        # Manually insert user metadata here to accomodate any warning
        # from self._process_neg_flux()
        meta = kwargs.pop('meta', {})
        self.meta = meta
        if 'warnings' not in self.meta:
            self.meta['warnings'] = {}

        keep_neg = kwargs.pop('keep_neg', False)
        self._keep_neg = keep_neg
        y = self._process_neg_flux(y)

        # Set interpolation default values
        self._kind = 'linear'
        self._axis = -1
        self._copy = True
        self._bounds_error = False
        self._fill_value = 0
        self._assume_sorted = False

        # Filter out keywords that do not go into model init
        kwargs = self._process_interp1d_options(x, y, **kwargs)

        super(Empirical1D, self).__init__(x=x, y=y, **kwargs)

    def _process_neg_flux(self, y):
        """Remove negative flux."""
        y = np.asarray(y)

        if not self._keep_neg:
            i = np.where(y < 0)
            n_neg = len(i[0])
            if n_neg > 0:
                y[i] = 0
                warn_str = ('{0} bin(s) contained negative flux or throughput'
                            '; it/they will be set to zero.'.format(n_neg))
                self.meta['warnings'].update({'NegativeFlux': warn_str})
                warnings.warn(warn_str, AstropyUserWarning)

        return y

    def _process_interp1d_options(self, x, y, **kwargs):
        """Override default interpolation options and return unused
        keywords."""
        from scipy.interpolate import interp1d

        self._kind = kwargs.pop('kind', self._kind)
        self._axis = kwargs.pop('axis', self._axis)
        self._copy = kwargs.pop('copy', self._copy)
        self._bounds_error = kwargs.pop('bounds_error', self._bounds_error)
        self._fill_value = kwargs.pop('fill_value', self._fill_value)
        self._assume_sorted = kwargs.pop('assume_sorted', self._assume_sorted)
        self._f = interp1d(
            x, y, kind=self._kind, axis=self._axis, copy=self._copy,
            bounds_error=self._bounds_error, fill_value=self._fill_value,
            assume_sorted=self._assume_sorted)

        return kwargs

    def set_interp1d(self, **kwargs):
        """Use given keywords with :func:`~scipy.interpolate.interp1d` to
        evaluate model. Otherwise, use previously set values."""
        self._process_interp1d_options(self.x.value, self.y.value, **kwargs)

    # NOTE: It is forced to be property by core Model. The decorator
    #       here is just to make this obvious.
    @property
    def bounding_box(self):
        """Tuple defining the default ``bounding_box`` limits,
        ``(x_low, x_high)``."""
        x = self.x.value
        return (min(x), max(x))

    def sampleset(self):
        """Return ``x`` array that samples the feature."""
        return self.x.value

    def evaluate(self, x, *args):
        """Evaluate the model.

        Parameters
        ----------
        x : number or ndarray
            Wavelengths in same unit as parameter ``x``.

        Returns
        -------
        y : number or ndarray
            Flux or throughput in same unit as parameter ``y``.

        """
        return self._process_neg_flux(self._f(x))


class GaussianSampleset1DMixin(object):
    """Mixin class to define ``sampleset`` for Gaussian models.
    Also used for Lorentz and MexicanHat due to similarities.

    """
    @staticmethod
    def _calc_sampleset(w1, w2, dw):
        """Calculate sampleset for each model."""
        return np.arange(w1, w2, dw)

    def sampleset(self, factor_step=0.1, **kwargs):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        factor_step : float
            Factor for sample step calculation. The step is calculated
            using ``factor_step * self.stddev``.

        kwargs : dict
            Keyword(s) for ``bounding_box`` calculation.

        """
        w1, w2 = self.bounding_box(**kwargs)
        dw = factor_step * self.stddev

        if self._n_models == 1:
            w = self._calc_sampleset(w1, w2, dw)
        else:
            w = list(map(self._calc_sampleset, w1, w2, dw))

        return np.asarray(w)


class Gaussian1D(_models.Gaussian1D, GaussianSampleset1DMixin):
    """Same as `astropy.modeling.models.Gaussian1D`, except with
    ``sampleset`` defined.

    """
    pass


class GaussianAbsorption1D(_models.GaussianAbsorption1D,
                           GaussianSampleset1DMixin):
    """Same as `astropy.modeling.models.GaussianAbsorption1D`, except with
    ``sampleset`` defined.

    """
    pass


class GaussianFlux1D(Gaussian1D):
    """Same as `Gaussian1D` but accepts extra keywords below.

    Parameters
    ----------
    fwhm : float
        Full width at half maximum of the Gaussian in Angstrom.
        If given, this overrides ``stddev``.

    total_flux : float
        Total flux under the Gaussian in PHOTLAM.
        If given, this overrides ``amplitude``.

    """
    def __init__(self, *args, **kwargs):
        fwhm = kwargs.pop('fwhm', None)
        total_flux = kwargs.pop('total_flux', None)

        super(GaussianFlux1D, self).__init__(*args, **kwargs)

        if fwhm is None:
            fwhm = self.stddev * gaussian_sigma_to_fwhm
        else:
            self.stddev = fwhm * gaussian_fwhm_to_sigma

        gaussian_amp_to_totflux = np.sqrt(2.0 * np.pi) * self.stddev

        if total_flux is None:
            total_flux = self.amplitude * gaussian_amp_to_totflux
        else:
            self.amplitude = total_flux / gaussian_amp_to_totflux

        self.meta['expr'] = 'em({0:g}, {1:g}, {2:g}, PHOTLAM)'.format(
            self.mean.value, fwhm, total_flux)


class Lorentz1D(_models.Lorentz1D, GaussianSampleset1DMixin):
    """Same as `astropy.modeling.models.Lorentz1D`, except with
    ``sampleset`` defined.

    """
    # This is needed for sampleset()
    @property
    def stddev(self):
        """Standard deviation based on FWHM."""
        return self.fwhm * 0.5 / np.sqrt(2 * np.log(2))

    def bounding_box(self, factor=25):
        """Tuple defining the default ``bounding_box`` limits,
        ``(x_low, x_high)``.

        Parameters
        ----------
        factor : float
            The multiple of `stddev` used to define the limits.
            Similar to `Gaussian1D`.

        """
        x0 = self.x_0.value
        dx = factor * self.stddev

        return (x0 - dx, x0 + dx)


class MexicanHat1D(_models.MexicanHat1D, GaussianSampleset1DMixin):
    """Same as `astropy.modeling.models.MexicanHat1D`, except with
    ``sampleset`` defined.

    """
    # This is needed for sampletset()
    @property
    def stddev(self):
        """Alias for ``sigma``."""
        return self.sigma

    def bounding_box(self, factor=5.5):
        """Tuple defining the default ``bounding_box`` limits,
        ``(x_low, x_high)``.

        Parameters
        ----------
        factor : float
            The multiple of ``sigma`` used to define the limits.
            Similar to `Gaussian1D`.

        """
        x0 = self.x_0.value
        dx = factor * self.sigma

        return (x0 - dx, x0 + dx)


class PowerLawFlux1D(_models.PowerLaw1D):
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

        if (amplitude.unit.physical_type in
                ('spectral flux density', 'spectral flux density wav',
                 'photon flux density', 'photon flux density wav')):
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


class Trapezoid1D(_models.Trapezoid1D):
    """Same as `astropy.modeling.models.Trapezoid1D`, except with
    ``sampleset`` defined.

    """
    def sampleset(self):
        """Return ``x`` array that samples the feature."""
        x1, x4 = self.bounding_box
        dw = self.width * 0.5
        x2 = self.x_0 - dw
        x3 = self.x_0 + dw

        if self._n_models == 1:
            w = [x1, x2, x3, x4]
        else:
            w = list(zip(x1, x2, x3, x4))

        return np.asarray(w)


# Functions below are for sampleset magic.

def _get_sampleset(model):
    """Return sampleset of a model or `None` if undefined.
    Model could be a real model or evaluated sampleset."""
    if isinstance(model, Model):
        if hasattr(model, 'sampleset'):
            w = model.sampleset()
        else:
            w = None
    else:
        w = model  # Already a sampleset
    return w


def _merge_sampleset(model1, model2):
    """Simple merge of samplesets."""
    w1 = _get_sampleset(model1)
    w2 = _get_sampleset(model2)
    return merge_wavelengths(w1, w2)


def _shift_wavelengths(model1, model2):
    """One of the models is either ``RedshiftScaleFactor`` or ``Scale``.

    Possible combos::

        RedshiftScaleFactor | Model
        Scale | Model
        Model | Scale

    """
    if isinstance(model1, _models.RedshiftScaleFactor):
        val = _get_sampleset(model2)
        if val is None:
            w = val
        else:
            w = model1.inverse(val)
    elif isinstance(model1, _models.Scale):
        w = _get_sampleset(model2)
    else:
        w = _get_sampleset(model1)
    return w


WAVESET_OPERATORS = {
    '+': _merge_sampleset,
    '-': _merge_sampleset,
    '*': _merge_sampleset,
    '/': _merge_sampleset,
    '**': _merge_sampleset,
    '|': _shift_wavelengths,
    '&': _merge_sampleset
}


def get_waveset(model):
    """Get optimal wavelengths for sampling a given model.

    Parameters
    ----------
    model : `~astropy.modeling.Model`
        Model.

    Returns
    -------
    waveset : array_like or `None`
        Optimal wavelengths. `None` if undefined.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid model.

    """
    if not isinstance(model, Model):
        raise SynphotError('{0} is not a model.'.format(model))

    if isinstance(model, _CompoundModel):
        waveset = model._tree.evaluate(WAVESET_OPERATORS, getter=None)
    else:
        waveset = _get_sampleset(model)

    return waveset


# Functions below are for meta magic.

# This is for joining metadata in a compound model.
METADATA_OPERATORS = defaultdict(lambda: _merge_meta)


def _get_meta(model):
    """Return metadata of a model.
    Model could be a real model or evaluated metadata."""
    if isinstance(model, Model):
        w = model.meta
    else:
        w = model  # Already metadata
    return w


def _merge_meta(model1, model2):
    """Simple merge of samplesets."""
    w1 = _get_meta(model1)
    w2 = _get_meta(model2)
    return metadata.merge(w1, w2, metadata_conflicts='silent')


def get_metadata(model):
    """Get metadata for a given model.

    Parameters
    ----------
    model : `~astropy.modeling.Model`
        Model.

    Returns
    -------
    metadata : dict
        Metadata for the model.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid model.

    """
    if not isinstance(model, Model):
        raise SynphotError('{0} is not a model.'.format(model))

    if isinstance(model, _CompoundModel):
        metadata = model._tree.evaluate(METADATA_OPERATORS, getter=None)
    else:
        metadata = deepcopy(model.meta)

    return metadata
