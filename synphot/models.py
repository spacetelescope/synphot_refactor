# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Spectrum models not in `astropy.modeling`."""

# STDLIB
import warnings
from copy import deepcopy
from functools import partial

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import units as u
from astropy.modeling import Fittable1DModel, Model, Parameter
from astropy.modeling import models as _models
from astropy.modeling.functional_models import FLOAT_EPSILON
from astropy.modeling.models import Tabular1D
from astropy.stats.funcs import gaussian_fwhm_to_sigma, gaussian_sigma_to_fwhm
from astropy.utils import metadata
from astropy.utils.decorators import deprecated
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from . import units
from .compat import ASTROPY_LT_4_0
from .exceptions import SynphotError
from .utils import merge_wavelengths

if ASTROPY_LT_4_0:
    from astropy.modeling.blackbody import blackbody_nu
    from astropy.modeling.core import _CompoundModel as CompoundModel
    from astropy.modeling.models import MexicanHat1D as _RickerWavelet1D

    class BlackBody1D(Fittable1DModel):
        """Create a :ref:`blackbody spectrum <synphot-planck-law>`
        model with given temperature.

        Parameters
        ----------
        temperature : `~astropy.units.quantity.Quantity`
            Blackbody temperature.

        """
        temperature = Parameter(default=5000, min=0, unit=u.K)
        _input_units_allow_dimensionless = True
        input_units_equivalencies = {'x': u.spectral()}

        def __init__(self, *args, **kwargs):
            super(BlackBody1D, self).__init__(*args, **kwargs)
            self.meta['expr'] = 'bb({0})'.format(self.temperature.value)

        @property
        def lambda_max(self):
            """Peak wavelength in Angstrom when the curve is expressed as
            power density."""
            return ((const.b_wien.value / self.temperature) * u.m).to(u.AA)

        def bounding_box(self, factor=10.0):
            """Tuple defining the default ``bounding_box`` limits,
            ``(x_low, x_high)``.

            .. math::

                x_{\\mathrm{low}} = 0

                x_{\\mathrm{high}} = \\log(\\lambda_{\\mathrm{max}} \\;\
                (1 + \\mathrm{factor}))

            Parameters
            ----------
            factor : float
                Used to calculate ``x_high``.

            """
            w0 = self.lambda_max.value
            return [w0 * 0, np.log10(w0 + factor * w0)]

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

            return np.asarray(w) * self.lambda_max.value

        @property
        def input_units(self):
            return {'x': u.AA}

        def _parameter_units_for_data_units(self, inputs_unit, outputs_unit):
            return {'temperature': u.K}

        @staticmethod
        def evaluate(x, temperature):
            # Silence Numpy
            old_np_err_cfg = np.seterr(all='ignore')

            if not isinstance(x, u.Quantity):
                wave = np.ascontiguousarray(x) * u.AA
            else:
                wave = x

            bbnu_flux = blackbody_nu(wave, temperature)
            bbflux = (bbnu_flux * u.sr).to(
                units.PHOTLAM, u.spectral_density(wave)) / u.sr  # PHOTLAM/sr

            # Restore Numpy settings
            np.seterr(**old_np_err_cfg)

            # If the temperature parameter has no unit, we should return a
            # unitless value. This occurs for instance during fitting,
            # since we drop the units temporarily.
            if hasattr(temperature, 'unit'):
                return bbflux
            else:
                return bbflux.value

else:
    from astropy.modeling.core import CompoundModel
    from astropy.modeling.physical_models import BlackBody
    from astropy.modeling.models import RickerWavelet1D as _RickerWavelet1D

    class BlackBody1D(BlackBody):
        """Create a :ref:`blackbody spectrum <synphot-planck-law>`
        model with given temperature.

        See :class:`astropy.modeling.physical_models.BlackBody`.

        """
        def __init__(self, *args, **kwargs):
            super(BlackBody1D, self).__init__(*args, **kwargs)
            self.meta['expr'] = 'bb({0})'.format(self.temperature.value)

        def bounding_box(self, factor=10.0):
            """Tuple defining the default ``bounding_box`` limits,
            ``(x_low, x_high)`` in Angstrom.

            .. math::

                x_{\\mathrm{low}} = 0

                x_{\\mathrm{high}} = \\log(\\lambda_{\\mathrm{max}} \\;\
                (1 + \\mathrm{factor}))

            Parameters
            ----------
            factor : float
                Used to calculate ``x_high``.

            """
            w0 = self.lambda_max.to(u.AA).value
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

            return np.asarray(w) * u.AA

        @property
        def input_units(self):
            return {'x': u.AA}

        def evaluate(self, x, temperature, scale):
            """Evaluate the model.

            This is similar to
            :meth:`astropy.modeling.physical_models.BlackBody.evaluate`,
            except that Numpy warnings are suppressed already and
            evaluated flux is not Quantity but is always in the unit of
            PHOTLAM per steradian. This is for backward compatibility.

            """
            # Silence Numpy
            old_np_err_cfg = np.seterr(all='ignore')

            if isinstance(x, u.Quantity):
                wave = x
            else:
                wave = np.ascontiguousarray(x) * u.AA

            bbnu_flux = super(BlackBody1D, self).evaluate(
                wave, temperature, scale)
            bbflux = (bbnu_flux).to(
                units.PHOTLAM / u.sr, u.spectral_density(wave))

            # Restore Numpy settings
            np.seterr(**old_np_err_cfg)

            # If the temperature parameter has no unit, we should return a
            # unitless value. This occurs for instance during fitting,
            # since we drop the units temporarily.
            if hasattr(temperature, 'unit'):
                return bbflux
            else:
                return bbflux.value


__all__ = ['BlackBody1D', 'BlackBodyNorm1D', 'Box1D', 'ConstFlux1D',
           'Empirical1D', 'Gaussian1D', 'GaussianAbsorption1D',
           'GaussianFlux1D', 'Lorentz1D', 'RickerWavelet1D', 'PowerLawFlux1D',
           'Trapezoid1D', 'get_waveset', 'get_metadata']


class BlackBodyNorm1D(BlackBody1D):
    """Create a normalized :ref:`blackbody spectrum <synphot-planck-law>`
    with given temperature.

    It is normalized by multiplying `BlackBody1D` result with a solid angle,
    :math:`\\Omega`, as defined below, where :math:`d` is 1 kpc:

    .. math::

        \\Omega = \\frac{\\pi R_{\\mathrm{Sun}}^{2}}{d^{2}}

    Parameters
    ----------
    temperature : `~astropy.units.quantity.Quantity`
        Blackbody temperature.

    """
    def __init__(self, *args, **kwargs):
        super(BlackBodyNorm1D, self).__init__(*args, **kwargs)
        self._omega = np.pi * (const.R_sun / const.kpc).value ** 2 * u.sr

    def evaluate(self, x, temperature, *args):
        """Evaluate the model."""
        bbflux = super(BlackBodyNorm1D, self).evaluate(*args)
        y = bbflux * self._omega

        # If the temperature parameter has no unit, we should return a
        # unitless value. This occurs for instance during fitting,
        # since we drop the units temporarily.
        if hasattr(temperature, 'unit'):
            return y
        else:
            return y.value


class Box1D(_models.Box1D):
    """Same as `astropy.modeling.functional_models.Box1D`, except with
    ``sampleset`` defined.

    """
    x_0 = Parameter(default=0, unit=u.AA)
    width = Parameter(default=1, unit=u.AA)
    _input_units_allow_dimensionless = True
    input_units_equivalencies = {'x': u.spectral()}

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
            w = self._calc_sampleset(w1.value, w2.value, step, minimal)
        else:
            w = list(map(partial(
                self._calc_sampleset, step=step, minimal=minimal),
                w1.value, w2.value))

        return w * w1.unit


class ConstFlux1D(_models.Const1D):
    """One dimensional constant flux model.

    Flux that is constant in a given unit might not be constant in
    another unit.

    For multiple ``n_models``, this model only accepts amplitudes of the
    same flux unit; e.g., ``Quantity([1, 2], 'photlam')``.

    Parameters
    ----------
    amplitude : `~astropy.units.quantity.Quantity`
        Value and unit of the constant function.

    """
    amplitude = Parameter(default=1, unit=units.PHOTLAM)
    _input_units_allow_dimensionless = True
    input_units_equivalencies = {'x': u.spectral()}

    def __init__(self, amplitude=amplitude.default * amplitude.unit, **kwargs):
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

        super(ConstFlux1D, self).__init__(amplitude=a, **kwargs)

    @property
    def input_units(self):
        return {'x': u.AA}

    def _parameter_units_for_data_units(self, inputs_unit, outputs_unit):
        return {'amplitude': outputs_unit['y']}

    def evaluate(self, x, *args):
        if hasattr(x, "unit"):
            y = self.amplitude * np.ones_like(x.value)
        else:
            y = self.amplitude.value * np.ones_like(x)
        return y


class Empirical1D(Tabular1D):
    """Empirical (sampled) spectrum or bandpass model.

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
            # In case input is just pure list
            if not isinstance(x, u.Quantity):
                x = np.asarray(x)
            if not isinstance(y, u.Quantity):
                y = np.asarray(y)

            i = y < 0
            n_neg = np.count_nonzero(i)
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
        y = self.lookup_table[::self.lookup_table.size - 1]
        if isinstance(y, u.Quantity):
            y = y.value
        return np.array_equal(y, [0, 0])

    def sampleset(self):
        """Return array that samples the feature."""
        return np.squeeze(self.points)

    def evaluate(self, inputs):
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


class Gaussian1D(_models.Gaussian1D):
    """Same as `astropy.modeling.functional_models.Gaussian1D`, except with
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
        if isinstance(w1, u.Quantity):
            dw = (factor_step * self.stddev).to(w1.unit, u.spectral())
            if self._n_models == 1:
                w = np.arange(w1.value, w2.value, dw.value) * w1.unit
            else:
                w = list(map(
                    np.arange, w1.value, w2.value, dw.value)) * w1.unit
        else:
            dw = factor_step * self.stddev
            if self._n_models == 1:
                w = np.arange(w1, w2, dw)
            else:
                w = np.asarray(list(map(np.arange, w1, w2, dw)))

        return w


# TODO: Deprecate this?
class GaussianAbsorption1D(Gaussian1D):
    """Model to calculate ``1 - Gaussian1D``."""
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
    """Same as `Gaussian1D` but accepts ``fwhm`` and ``total_flux`` also.

    Parameters
    ----------
    amplitude : `~astropy.units.quantity.Quantity`
        Amplitude of the Gaussian.
        Also see ``total_flux``.

    mean : `~astropy.units.quantity.Quantity`
        Mean of the Gaussian.

    stddev : `~astropy.units.quantity.Quantity`
        Standard deviation of the Gaussian.
        Also see ``fwhm``.

    fwhm : float or `~astropy.units.quantity.Quantity`
        Full width at half maximum of the Gaussian.
        Assume Angstrom if no unit given.
        If given, this overrides ``stddev``.

    total_flux : float or `~astropy.units.quantity.Quantity`
        Total flux under the Gaussian.
        Assume ``erg/s/cm^2`` if no unit given.
        If given, this overrides ``amplitude``.

    """
    amplitude = Parameter(default=1, unit=units.PHOTLAM)
    mean = Parameter(default=0, unit=u.AA)

    # Ensure stddev makes sense if its bounds are not explicitly set.
    # stddev must be non-zero and positive.
    stddev = Parameter(default=1, bounds=(FLOAT_EPSILON, None), unit=u.AA)

    def __init__(self, amplitude=amplitude.default * amplitude.unit,
                 mean=mean.default * mean.unit,
                 stddev=stddev.default * stddev.unit,
                 fwhm=None, total_flux=None, **kwargs):
        if fwhm is None:
            fwhm = stddev * gaussian_sigma_to_fwhm
        else:
            if not isinstance(fwhm, u.Quantity):
                fwhm = fwhm * u.AA
            stddev = fwhm * gaussian_fwhm_to_sigma

        # Taken from PySynphot
        gaussian_amp_to_totflux = np.sqrt(2.0 * np.pi) * stddev.to(
            u.AA, u.spectral())

        if total_flux is None:
            u_str = 'PHOTLAM'
            total_flux = ((amplitude.to(u.AA, u.spectral()).value *
                           gaussian_amp_to_totflux.value) *
                          (u.ph / (u.cm * u.cm * u.s)))
        else:
            u_str = 'FLAM'
            tf_unit = u.erg / (u.cm * u.cm * u.s)
            if not isinstance(total_flux, u.Quantity):
                total_flux = total_flux * tf_unit
            amplitude = (total_flux / gaussian_amp_to_totflux).to(
                units.PHOTLAM, u.spectral_density(mean)).value * u.AA

        super(GaussianFlux1D, self).__init__(
            amplitude=amplitude, mean=mean, stddev=stddev, **kwargs)

        # TODO: Allow FWHM and total flux to be property
        self.fwhm = fwhm
        self.total_flux = total_flux
        self.meta['expr'] = 'em({0:g}, {1:g}, {2:g}, {3})'.format(
            mean.to(u.AA, u.spectral()).value,
            fwhm.to(u.AA, u.spectral()).value, total_flux.value, u_str)


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

        if isinstance(w1, u.Quantity):
            dw = (factor_step * self.fwhm).to(w1.unit, u.spectral())
            if self._n_models == 1:
                w = np.arange(w1.value, w2.value, dw.value) * w1.unit
            else:
                w = np.asarray(list(map(
                    np.arange, w1.value, w2.value, dw.value))) * w1.unit
        else:
            dw = factor_step * self.fwhm
            if self._n_models == 1:
                w = np.arange(w1, w2, dw)
            else:
                w = np.asarray(list(map(np.arange, w1, w2, dw)))

        return w


class RickerWavelet1D(_RickerWavelet1D):
    """Same as ``astropy`` ``MexicanHat1D`` or ``RickerWavelet1D``, except with
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

        if isinstance(w1, u.Quantity):
            dw = (factor_step * self.sigma).to(w1.unit, u.spectral())
            if self._n_models == 1:
                w = np.arange(w1.value, w2.value, dw.value) * w1.unit
            else:
                w = np.asarray(list(map(
                    np.arange, w1.value, w2.value, dw.value))) * w1.unit
        else:
            dw = factor_step * self.sigma
            if self._n_models == 1:
                w = np.arange(w1, w2, dw)
            else:
                w = np.asarray(list(map(np.arange, w1, w2, dw)))

        return w


@deprecated('2.0', alternative='synphot.models.RickerWavelet1D')
class MexicanHat1D(RickerWavelet1D):
    """This model is deprecated. Use `RickerWavelet1D`."""
    pass


class PowerLawFlux1D(_models.PowerLaw1D):
    """One dimensional power law model with proper flux handling.

    For multiple ``n_models``, this model only accepts parameters of the
    same unit; e.g., ``amplitude=Quantity([1, 2], 'photlam')``.

    Also see `~astropy.modeling.powerlaws.PowerLaw1D`.

    Parameters
    ----------
    amplitude : `~astropy.units.quantity.Quantity`
        Model amplitude at the reference point.

    x_0 : `~astropy.units.quantity.Quantity`
        Reference point.

    alpha : float
        Power law index.

    """
    amplitude = Parameter(default=1, unit=units.PHOTLAM)
    x_0 = Parameter(default=1, unit=u.AA)
    alpha = Parameter(default=1)

    _input_units_allow_dimensionless = True
    input_units_equivalencies = {'x': u.spectral()}

    def __init__(self, amplitude=amplitude.default * amplitude.unit,
                 x_0=x_0.default * x_0.unit, alpha=alpha.default, **kwargs):
        if (amplitude.unit.physical_type not in
                ('spectral flux density', 'spectral flux density wav',
                 'photon flux density', 'photon flux density wav')):
            raise NotImplementedError(
                '{0} not supported.'.format(amplitude.unit))

        super(PowerLawFlux1D, self).__init__(
            amplitude=amplitude, x_0=x_0, alpha=alpha, **kwargs)

    @property
    def input_units(self):
        return {'x': u.AA}

    def _parameter_units_for_data_units(self, inputs_unit, outputs_unit):
        return {'x_0', inputs_unit['x'],
                'amplitude', outputs_unit['y']}

    def evaluate(self, x, *args):
        if hasattr(x, 'unit'):
            y = self.amplitude * (x / self.x_0) ** (-self.alpha)
        else:
            y = self.amplitude.value * (x / self.x_0.value) ** (-self.alpha)
        return y


class Trapezoid1D(_models.Trapezoid1D):
    """Same as `astropy.modeling.functional_models.Trapezoid1D`, except with
    ``sampleset`` defined.

    """
    def sampleset(self):
        """Return ``x`` array that samples the feature."""
        x1, x4 = self.bounding_box

        if isinstance(x1, u.Quantity):
            dw = self.width.to(x1.unit, u.spectral()) * 0.5
            x0 = self.x_0.to(x1.unit, u.spectral())
            x2 = x0 - dw
            x3 = x0 + dw
            if self._n_models == 1:
                w = [x1.value, x2.value, x3.value, x4.value] * x1.unit
            else:
                w = list(zip(x1.value, x2.value, x3.value, x4.value)) * x1.unit
        else:
            dw = self.width * 0.5
            x2 = self.x_0 - dw
            x3 = self.x_0 + dw
            if self._n_models == 1:
                w = np.asarray([x1, x2, x3, x4])
            else:
                w = np.asarray(list(zip(x1, x2, x3, x4)))

        return w


# Functions below are for sampleset magic.

def _get_sampleset(model):
    """Return sampleset of a model or `None` if undefined."""
    w = None
    if isinstance(model, Model) and hasattr(model, 'sampleset'):
        w = model.sampleset()
    return w


def _model_tree_evaluate_sampleset(root):
    # Not a CompoundModel, grab sampleset and be done.
    if not hasattr(root, 'op'):
        return _get_sampleset(root)

    model1 = root.left
    model2 = root.right

    # model2 is redshifted, apply the redshift if applicable.
    if isinstance(model1, _models.RedshiftScaleFactor):
        val = _model_tree_evaluate_sampleset(model2)
        if val is None:
            w = val
        else:
            w = model1.inverse(val)

    # This should not ever happen, so ignore the redshift.
    elif isinstance(model2, _models.RedshiftScaleFactor):
        w = _model_tree_evaluate_sampleset(model1)

    # One of the models is scaled. Non-redshift scaling does
    # not affect sampleset of the model.
    elif isinstance(model1, _models.Scale):
        w = _model_tree_evaluate_sampleset(model2)
    elif isinstance(model2, _models.Scale):
        w = _model_tree_evaluate_sampleset(model1)

    # Combine sampleset from both models.
    else:
        w1 = _model_tree_evaluate_sampleset(model1)
        w2 = _model_tree_evaluate_sampleset(model2)
        w = merge_wavelengths(w1, w2)

    return w


def _model_tree_evaluate_sampleset_compat(model):
    """_model_tree_evaluate_sampleset for astropy<4"""

    def _get_sampleset_compat(model):
        # Return sampleset of a model or `None` if undefined.
        # Model could be a real model or evaluated sampleset.
        if isinstance(model, Model):
            if hasattr(model, 'sampleset'):
                w = model.sampleset()
            else:
                w = None
        else:
            w = model  # Already a sampleset
        return w

    def _merge_sampleset_compat(model1, model2):
        # Simple merge of samplesets.
        w1 = _get_sampleset_compat(model1)
        w2 = _get_sampleset_compat(model2)
        return merge_wavelengths(w1, w2)

    def _shift_wavelengths_compat(model1, model2):
        # One of the models is either ``RedshiftScaleFactor`` or ``Scale``.
        # Possible combos::
        #    RedshiftScaleFactor | Model
        #    Scale | Model
        #    Model | Scale
        if isinstance(model1, _models.RedshiftScaleFactor):
            val = _get_sampleset_compat(model2)
            if val is None:
                w = val
            else:
                w = model1.inverse(val)
        elif isinstance(model1, _models.Scale):
            w = _get_sampleset_compat(model2)
        else:
            w = _get_sampleset_compat(model1)
        return w

    WAVESET_OPERATORS = {
        '+': _merge_sampleset_compat,
        '-': _merge_sampleset_compat,
        '*': _merge_sampleset_compat,
        '/': _merge_sampleset_compat,
        '**': _merge_sampleset_compat,
        '|': _shift_wavelengths_compat,
        '&': _merge_sampleset_compat}

    if isinstance(model, CompoundModel):
        waveset = model._tree.evaluate(WAVESET_OPERATORS, getter=None)
    else:
        waveset = _get_sampleset_compat(model)
    return waveset


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

    if ASTROPY_LT_4_0:
        waveset = _model_tree_evaluate_sampleset_compat(model)
    else:
        waveset = _model_tree_evaluate_sampleset(model)

    return waveset


# Functions below are for meta magic.

def _get_meta(model):
    """Return metadata of a model."""
    w = {}
    if isinstance(model, Model):
        w = model.meta
    return w


def _model_tree_evaluate_metadata(root):
    # Not a CompoundModel, grab metadata and be done.
    if not hasattr(root, 'op'):
        return _get_meta(root)

    m1 = _model_tree_evaluate_metadata(root.left)
    m2 = _model_tree_evaluate_metadata(root.right)
    return metadata.merge(m1, m2, metadata_conflicts='silent')


def _model_tree_evaluate_metadata_compat(model):
    """_model_tree_evaluate_sampleset for astropy<4"""
    from collections import defaultdict

    def _get_meta_compat(model):
        # Return metadata of a model.
        # Model could be a real model or evaluated metadata.
        if isinstance(model, Model):
            w = model.meta
        else:
            w = model  # Already metadata
        return w

    def _merge_meta_compat(model1, model2):
        # Simple merge of samplesets.
        m1 = _get_meta_compat(model1)
        m2 = _get_meta_compat(model2)
        return metadata.merge(m1, m2, metadata_conflicts='silent')

    if isinstance(model, CompoundModel):
        meta = model._tree.evaluate(
            defaultdict(lambda: _merge_meta_compat), getter=None)
    else:
        meta = deepcopy(model.meta)

    return meta


def get_metadata(model):
    """Get metadata for a given model.

    Parameters
    ----------
    model : `~astropy.modeling.Model`
        Model.

    Returns
    -------
    meta : dict
        Metadata for the model.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid model.

    """
    if not isinstance(model, Model):
        raise SynphotError('{0} is not a model.'.format(model))

    if ASTROPY_LT_4_0:
        meta = _model_tree_evaluate_metadata_compat(model)
    else:
        # Deep copy to make sure modiyfing returned metadata
        # does not modify input model metadata, especially
        # if input model is not a compound model.
        meta = deepcopy(_model_tree_evaluate_metadata(model))

    return meta
