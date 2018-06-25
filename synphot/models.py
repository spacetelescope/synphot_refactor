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
from astropy.modeling import Fittable1DModel, Model, Parameter
from astropy.modeling import models as _models
from astropy.modeling.core import _CompoundModel
from astropy.modeling.models import Tabular1D
from astropy.stats.funcs import gaussian_fwhm_to_sigma, gaussian_sigma_to_fwhm
from astropy.utils import metadata
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from . import units
from .compat import ASTROPY_LT_2_0
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
        self.meta['expr'] = 'bb({0})'.format(self.temperature.value)

    @property
    def lambda_max(self):
        """Peak wavelength in Angstrom when the curve is expressed as
        power density."""
        return ((const.b_wien.value / self.temperature) * u.m).to(u.AA).value

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
            w = np.logspace(w1, w2, num)
        else:
            w = list(map(partial(np.logspace, num=num), w1, w2))

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
        if ASTROPY_LT_2_0:
            from astropy.analytic_functions.blackbody import blackbody_nu
        else:
            from astropy.modeling.blackbody import blackbody_nu

        # Silence Numpy
        old_np_err_cfg = np.seterr(all='ignore')

        wave = np.ascontiguousarray(x) * u.AA
        bbnu_flux = blackbody_nu(wave, temperature)
        bbflux = (bbnu_flux * u.sr).to(
            units.PHOTLAM, u.spectral_density(wave)) / u.sr  # PHOTLAM/sr

        # Restore Numpy settings
        np.seterr(**old_np_err_cfg)

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
    """Same as `astropy.modeling.functional_models.Box1D`, except with
    ``sampleset`` defined.

    """
    @staticmethod
    def _calc_sampleset(w1, w2, step, minimal):
        """Calculate sampleset for each model."""
        if minimal:
            arr = [w1 - step, w1, w2, w2 + step]
        else:
            arr = np.arange(w1 - step, w2 + step + step, step)

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
            w = list(map(partial(
                self._calc_sampleset, step=step, minimal=minimal), w1, w2))

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
            amplitude = amplitude * units.PHOTLAM

        if amplitude.unit == u.STmag:
            a = units.convert_flux(1, amplitude, units.FLAM)
        elif amplitude.unit == u.ABmag:
            a = units.convert_flux(1, amplitude, units.FNU)
        elif (amplitude.unit.physical_type in
              ('spectral flux density', 'spectral flux density wav',
               'photon flux density', 'photon flux density wav')):
            a = amplitude
        else:
            raise NotImplementedError(
                '{0} not supported.'.format(amplitude.unit))

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
        a = (self.amplitude * np.ones_like(x)) * self._flux_unit
        y = units.convert_flux(x, a, units.PHOTLAM)
        return y.value


class Empirical1D(Tabular1D):
    """Empirical (sampled) spectrum or bandpass model.

    .. note::

        This model requires `SciPy <http://www.scipy.org>`_ 0.14
        or later to be installed.

    Parameters
    ----------
    keep_neg : bool
        Convert negative ``lookup_table`` values to zeroes?
        This is to be consistent with ASTROLIB PYSYNPHOT.

    kwargs : dict
        Keywords for `~astropy.modeling.tabular.Tabular1D` model
        creation or :func:`~scipy.interpolate.interpn`.
        When ``fill_value=np.nan`` is given, extrapolation is done
        based on nearest end points on each end; This is the default
        behavior.

    """
    def __init__(self, **kwargs):

        # Manually insert user metadata here to accomodate any warning
        # from self._process_neg_flux()
        meta = kwargs.pop('meta', {})
        self.meta = meta
        if 'warnings' not in self.meta:
            self.meta['warnings'] = {}

        x = kwargs['points']
        y = kwargs['lookup_table']

        # Points can only be ascending for interpn()
        if x[-1] < x[0]:
            x = x[::-1]
            y = y[::-1]
            kwargs['points'] = x

        # Handle negative flux
        keep_neg = kwargs.pop('keep_neg', False)
        self._keep_neg = keep_neg
        y = self._process_neg_flux(x, y)

        kwargs['lookup_table'] = y
        super(Empirical1D, self).__init__(**kwargs)

        # Set non-default interpolation default values.
        # For tapered model, just fill with zero;
        # Otherwise, extrapolate like ASTROLIB PYSYNPHOT.
        self.bounds_error = kwargs.get('bounds_error', False)
        if self.is_tapered():
            self.fill_value = kwargs.get('fill_value', 0)
        else:
            self.fill_value = kwargs.get('fill_value', np.nan)

    def _process_neg_flux(self, x, y):
        """Remove negative flux."""

        if self._keep_neg:  # Nothing to do
            return y

        old_y = None

        if np.isscalar(y):  # pragma: no cover
            if y < 0:
                n_neg = 1
                old_x = x
                old_y = y
                y = 0
        else:
            x = np.asarray(x)  # In case input is just pure list
            y = np.asarray(y)
            i = np.where(y < 0)
            n_neg = len(i[0])
            if n_neg > 0:
                old_x = x[i]
                old_y = y[i]
                y[i] = 0

        if old_y is not None:
            warn_str = ('{0} bin(s) contained negative flux or throughput'
                        '; it/they will be set to zero.'.format(n_neg))
            warn_str += '\n  points: {0}\n  lookup_table: {1}'.format(
                old_x, old_y)  # Extra info
            self.meta['warnings'].update({'NegativeFlux': warn_str})
            warnings.warn(warn_str, AstropyUserWarning)

        return y

    def is_tapered(self):
        return np.array_equal(
            self.lookup_table[::self.lookup_table.size - 1], [0, 0])

    def sampleset(self):
        """Return array that samples the feature."""
        return np.squeeze(self.points)

    def evaluate(self, inputs):
        """Evaluate the model.

        Parameters
        ----------
        inputs : number or ndarray
            Wavelengths in same unit as ``points``.

        Returns
        -------
        y : number or ndarray
            Flux or throughput in same unit as ``lookup_table``.

        """
        y = super(Empirical1D, self).evaluate(inputs)

        # Assume NaN at both ends need to be extrapolated based on
        # nearest end point.
        if self.fill_value is np.nan:
            # Cannot use sampleset() due to ExtinctionModel1D
            x = np.squeeze(self.points)

            if np.isscalar(y):  # pragma: no cover
                if inputs < x[0]:
                    y = self.lookup_table[0]
                elif inputs > x[-1]:
                    y = self.lookup_table[-1]
            else:
                y[inputs < x[0]] = self.lookup_table[0]
                y[inputs > x[-1]] = self.lookup_table[-1]

        return self._process_neg_flux(inputs, y)


class BaseGaussian1D(_models.Gaussian1D):
    """Same as `astropy.modeling.functional_models.BaseGaussian1D`, except with
    ``sampleset`` defined.

    """
    def sampleset(self, factor_step=0.1, **kwargs):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        factor_step : float
            Factor for sample step calculation. The step is calculated
            using ``factor_step * self.stddev``.

        kwargs : dict
            Keyword(s) for ``bounding_box`` calculation.
            Default ``factor`` is set to 5 to be compatible with
            ASTROLIB PYSYNPHOT.

        """
        if 'factor' not in kwargs:
            kwargs['factor'] = 5.0

        w1, w2 = self.bounding_box(**kwargs)
        dw = factor_step * self.stddev

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = list(map(np.arange, w1, w2, dw))

        return np.asarray(w)


class Gaussian1D(BaseGaussian1D):
    """Same as `astropy.modeling.functional_models.Gaussian1D`, except with
    ``sampleset`` defined.

    """
    pass


class GaussianAbsorption1D(BaseGaussian1D):
    """Same as ``astropy.modeling.functional_models.GaussianAbsorption1D``,
    except with ``sampleset`` defined.

    """
    @staticmethod
    def evaluate(x, amplitude, mean, stddev):
        """
        GaussianAbsorption1D model function.
        """
        return 1.0 - Gaussian1D.evaluate(x, amplitude, mean, stddev)

    @staticmethod
    def fit_deriv(x, amplitude, mean, stddev):
        """
        GaussianAbsorption1D model function derivatives.
        """
        import operator
        return list(map(
            operator.neg, Gaussian1D.fit_deriv(x, amplitude, mean, stddev)))


class GaussianFlux1D(Gaussian1D):
    """Same as `Gaussian1D` but accepts extra keywords below.

    Parameters
    ----------
    amplitude : float
        Amplitude of the Gaussian in PHOTLAM.
        Also see ``total_flux``.

    mean : float
        Mean of the Gaussian in Angstrom.

    stddev : float
        Standard deviation of the Gaussian in Angstrom.
        Also see ``fwhm``.

    fwhm : float
        Full width at half maximum of the Gaussian in Angstrom.
        If given, this overrides ``stddev``.

    total_flux : float
        Total flux under the Gaussian in ``erg/s/cm^2``.
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
            u_str = 'PHOTLAM'
            total_flux = self.amplitude * gaussian_amp_to_totflux
        else:
            u_str = 'FLAM'
            # total_flux is passed in unaltered, any conversion error would
            # happen here.
            tf_unit = u.erg / (u.cm * u.cm * u.s)
            if isinstance(total_flux, u.Quantity):
                total_flux = total_flux.to(tf_unit)
            else:
                total_flux = total_flux * tf_unit
            self.amplitude = (total_flux / (gaussian_amp_to_totflux * u.AA)).to(units.PHOTLAM, u.spectral_density(self.mean.value * u.AA)).value  # noqa
            total_flux = total_flux.value

        self.meta['expr'] = 'em({0:g}, {1:g}, {2:g}, {3})'.format(
            self.mean.value, fwhm, total_flux, u_str)


class Lorentz1D(_models.Lorentz1D):
    """Same as `astropy.modeling.functional_models.Lorentz1D`, except with
    ``sampleset`` defined.

    """
    def sampleset(self, factor_step=0.05, **kwargs):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        factor_step : float
            Factor for sample step calculation. The step is calculated
            using ``factor_step * self.fwhm``.

        kwargs : dict
            Keyword(s) for ``bounding_box`` calculation.

        """
        w1, w2 = self.bounding_box(**kwargs)
        dw = factor_step * self.fwhm

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = list(map(np.arange, w1, w2, dw))

        return np.asarray(w)


class MexicanHat1D(_models.MexicanHat1D):
    """Same as `astropy.modeling.models.MexicanHat1D`, except with
    ``sampleset`` defined.

    """
    def sampleset(self, factor_step=0.1, **kwargs):
        """Return ``x`` array that samples the feature.

        Parameters
        ----------
        factor_step : float
            Factor for sample step calculation. The step is calculated
            using ``factor_step * self.sigma``.

        kwargs : dict
            Keyword(s) for ``bounding_box`` calculation.

        """
        w1, w2 = self.bounding_box(**kwargs)
        dw = factor_step * self.sigma

        if self._n_models == 1:
            w = np.arange(w1, w2, dw)
        else:
            w = list(map(np.arange, w1, w2, dw))

        return np.asarray(w)


class PowerLawFlux1D(_models.PowerLaw1D):
    """One dimensional power law model with proper flux handling.

    For multiple ``n_models``, this model only accepts parameters of the
    same unit; e.g., ``amplitude=[1, 2]`` or
    ``amplitude=Quantity([1, 2], 'photlam')``.

    Also see `~astropy.modeling.powerlaws.PowerLaw1D`.

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
            amplitude = amplitude * units.PHOTLAM

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
        y = (self.amplitude * xx ** (-self.alpha)) * self._flux_unit
        flux = units.convert_flux(x, y, units.PHOTLAM)
        return flux.value


class Trapezoid1D(_models.Trapezoid1D):
    """Same as `astropy.modeling.functional_models.Trapezoid1D`, except with
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
    waveset : array-like or `None`
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
