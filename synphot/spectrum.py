# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines the different types of spectra."""
from __future__ import absolute_import, division, print_function
from .extern import six

# STDLIB
import numbers
import os
import warnings
from copy import deepcopy

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import log
from astropy import units as u
from astropy.modeling import Model
from astropy.modeling.core import _CompoundModel
from astropy.modeling.models import RedshiftScaleFactor, Scale
from astropy.utils.exceptions import AstropyUserWarning
from astropy.utils import metadata

# LOCAL
from . import exceptions, specio, units, utils
from .config import Conf, conf
from .models import ConstFlux1D, Empirical1D, get_waveset, get_metadata

__all__ = ['BaseSpectrum', 'BaseSourceSpectrum', 'SourceSpectrum',
           'BaseUnitlessSpectrum', 'SpectralElement']


# TODO: Update model logic when astropy.modeling supports Quantity.
class BaseSpectrum(object):
    """Base class to handle spectrum or bandpass.

    .. note::

        Until `astropy.modeling` can handle units, all parameters
        are converted to pre-defined internal units.

    Parameters
    ----------
    modelclass : cls
        Model class from `astropy.modeling.models`.

    clean_meta : bool
        Scrub "expr" and "header" entries from input metadata before merging.
        Set this to `True` when those entries no longer make sense in ``self``.
        This is automatically set to `True` regardless for spectrum arithmetic.

    kwargs : dict
        Model parameters accepted by ``modelclass``. Each parameter can
        be either a Quantity or number. If the latter, assume pre-defined
        internal units.

    Attributes
    ----------
    meta : dict
        Metadata associated with the spectrum or bandpass model \
        (warnings, legacy SYNPHOT expression, FITS header, etc).

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid model.

    """
    _internal_wave_unit = u.AA
    _internal_flux_unit = None

    # For handling of units with models.
    _model_param_dict = {
        'BlackBody1D': {'temperature': u.K},
        'BlackBodyNorm1D': {'temperature': u.K},
        'Box1D': {'amplitude': 'flux', 'x_0': 'wave', 'width': 'wave'},
        'BrokenPowerLaw1D': {
            'amplitude': 'flux', 'x_break': 'wave',
            'alpha_1': u.dimensionless_unscaled,
            'alpha_2': u.dimensionless_unscaled},
        'Const1D': {'amplitude': 'noconv'},
        'ConstFlux1D': {'amplitude': 'noconv'},
        'Empirical1D': {'points': 'wave', 'lookup_table': 'flux'},
        'ExtinctionModel1D': {'points': 'wave', 'lookup_table': 'flux'},
        'ExponentialCutoffPowerLaw1D': {
            'amplitude': 'flux', 'x_0': 'wave', 'x_cutoff': 'wave',
            'alpha': u.dimensionless_unscaled},
        'Gaussian1D': {'amplitude': 'flux', 'mean': 'wave', 'stddev': 'wave'},
        'GaussianAbsorption1D': {
            'amplitude': 'flux', 'mean': 'wave', 'stddev': 'wave'},
        'GaussianFlux1D': {'total_flux': 'noconv', 'amplitude': 'flux',
                           'mean': 'wave', 'stddev': 'wave', 'fwhm': 'wave'},
        'LogParabola1D': {
            'amplitude': 'flux', 'x_0': 'wave',
            'alpha': u.dimensionless_unscaled,
            'beta': u.dimensionless_unscaled},
        'Lorentz1D': {'amplitude': 'flux', 'x_0': 'wave', 'fwhm': 'wave'},
        'MexicanHat1D': {'amplitude': 'flux', 'x_0': 'wave', 'sigma': 'wave'},
        'PowerLaw1D': {
            'amplitude': 'flux', 'x_0': 'wave',
            'alpha': u.dimensionless_unscaled},
        'PowerLawFlux1D': {
            'amplitude': 'noconv', 'x_0': 'noconv',
            'alpha': u.dimensionless_unscaled},
        'Trapezoid1D': {
            'amplitude': 'flux', 'x_0': 'wave', 'width': 'wave',
            'slope': u.dimensionless_unscaled}}

    # Flux conversion will use these wavelengths.
    _model_fconv_wav = {
        'Box1D': 'x_0',
        'BrokenPowerLaw1D': 'x_break',
        'Empirical1D': 'points',
        'ExponentialCutoffPowerLaw1D': 'x_0',
        'Gaussian1D': 'mean',
        'GaussianAbsorption1D': 'mean',
        'GaussianFlux1D': 'mean',
        'LogParabola1D': 'x_0',
        'Lorentz1D': 'x_0',
        'MexicanHat1D': 'x_0',
        'PowerLaw1D': 'x_0',
        'Trapezoid1D': 'x_0'}

    def __init__(self, modelclass, clean_meta=False, **kwargs):

        # Does not handle multiple model sets for now; too complicated.
        n_models = kwargs.pop('n_models', 1)
        if n_models != 1:
            raise exceptions.SynphotError('Model can only have n_models=1')

        other_meta = {}

        # This is needed for internal math operations to build composite model.
        # Handles the model instance, not class. Assume it is already in the
        # correct units and _n_models.
        if isinstance(modelclass, Model):
            self._model = modelclass

            if isinstance(modelclass, _CompoundModel):
                clean_meta = True

        elif isinstance(modelclass, BaseSpectrum):
            other_meta = modelclass.meta  # External metadata
            self._model = modelclass.model

        elif not issubclass(modelclass, Model):
            raise exceptions.SynphotError(
                '{0} is not a valid model class.'.format(modelclass))

        else:
            modelname = modelclass.__name__
            if modelname not in self._model_param_dict:
                raise exceptions.SynphotError(
                    '{0} is not supported.'.format(modelname))

            modargs = {}

            # Process wavelength needed for flux conversion first,
            # if applicable.
            if modelname in self._model_fconv_wav:
                pname_wav = self._model_fconv_wav[modelname]
                pval_wav = self._process_wave_param(kwargs.pop(pname_wav))
                modargs[pname_wav] = pval_wav
            else:
                pname_wav = ''
                pval_wav = None

            # Process the rest of the parameters.
            for pname, kval in six.iteritems(kwargs):
                if pname in self._model_param_dict[modelname]:
                    ptype = self._model_param_dict[modelname][pname]
                    if ptype == 'wave':
                        pval = self._process_wave_param(kval)
                    elif ptype == 'flux':
                        pval = self._process_flux_param(kval, pval_wav)
                    elif ptype == 'noconv':
                        pval = kval
                    else:
                        pval = self._process_generic_param(kval, ptype)
                else:
                    pval = kval

                modargs[pname] = pval

            self._model = modelclass(**modargs)

        # NOTE: This does not pick up any later changes to model metadata!
        # Start with model metadata. Others can be added later as needed
        # without affecting model metadata.
        m_meta = get_metadata(self._model)  # Merge compound model meta
        self.meta = {}
        self._merge_meta(m_meta, other_meta, self, clean=clean_meta)

    @staticmethod
    def _get_meta(obj):
        """Extract metadata, if any, from given object."""
        if hasattr(obj, 'meta'):  # Spectrum or model
            meta = deepcopy(obj.meta)
        elif isinstance(obj, dict):  # Metadata
            meta = deepcopy(obj)
        else:  # Number
            meta = {}
        return meta

    @staticmethod
    def _merge_meta(left, right, result, clean=True):
        """Merge metadata from left and right onto results.

        This is used during class initialization.
        This should also be used by operators to merge metadata after
        creating a new instance but before returning it.
        Result's metadata is modified in-place.

        Parameters
        ----------
        left, right : number, `BaseSpectrum`, or `~astropy.modeling.models`
            Inputs of an operation.

        result : `BaseSpectrum`
            Output spectrum object.

        clean : bool
            Remove ``'header'`` and ``'expr'`` entries from inputs.

        """
        # Copies are returned because they need some clean-up below.
        left = BaseSpectrum._get_meta(left)
        right = BaseSpectrum._get_meta(right)

        # Remove these from going into result to avoid mess.
        #   header = FITS header metadata
        #   expr = ASTROLIB PYSYNPHOT expression
        if clean:
            for key in ('header', 'expr'):
                for d in (left, right):
                    if key in d:
                        del d[key]

        mid = metadata.merge(left, right, metadata_conflicts='silent')
        result.meta = metadata.merge(result.meta, mid,
                                     metadata_conflicts='silent')

    @staticmethod
    def _process_generic_param(pval, def_unit, equivalencies=[]):
        """Process generic model parameter."""
        if isinstance(pval, u.Quantity):
            outval = pval.to(def_unit, equivalencies).value
        else:  # Assume already in desired unit
            outval = pval
        return outval

    def _process_wave_param(self, pval):
        """Process individual model parameter representing wavelength."""
        return self._process_generic_param(
            pval, self._internal_wave_unit, equivalencies=u.spectral())

    def _process_flux_param(self, pval, wave):
        """Process individual model parameter representing flux/throughput.

        Parameters
        ----------
        pval : number, array, or Quantity
            Input to be processed.

        wave : Quantity or `None`
            Wavelength for flux conversion, if applicable.

        Returns
        -------
        outval : number or array
            Input converted to internal unit.

        """
        raise NotImplementedError('To be implemented by subclasses.')

    @staticmethod
    def _validate_flux_unit(new_unit):
        """Make sure flux unit is valid.

        Parameters
        ----------
        new_unit : str or Unit
            Unit to validate.

        Returns
        -------
        new_unit
            Output from :func:`~synphot.units.validate_unit`.

        """
        raise NotImplementedError('To be implemented by subclasses.')

    @property
    def model(self):
        """Model of the spectrum/bandpass."""
        return self._model

    @property
    def warnings(self):
        """Dictionary of warning key-value pairs related to spectrum/bandpass.
        """
        return self.meta.get('warnings', {})

    @warnings.setter
    def warnings(self, val):
        if 'warnings' not in self.meta:
            self.meta['warnings'] = {}
        self.meta['warnings'].update(val)

    @property
    def waveset(self):
        """Optimal wavelengths for sampling the spectrum or bandpass."""
        w = get_waveset(self.model)
        if w is not None:
            utils.validate_wavelengths(w)
            w = w * self._internal_wave_unit
        return w

    @property
    def waverange(self):
        """Range of `waveset`."""
        if self.waveset is None:
            x = [None, None]
        else:
            x = u.Quantity([self.waveset.min(), self.waveset.max()])
        return x

    def __str__(self):
        """Descriptive information of the spectrum or bandpass."""
        return '{0}\n{1}'.format(self.__class__.__name__, str(self.model))

    def _validate_wavelengths(self, wave):
        """Validate wavelengths for sampling."""
        if wave is None:
            if self.waveset is None:
                raise exceptions.SynphotError(
                    'self.waveset is undefined; '
                    'Provide wavelengths for sampling.')
            wavelengths = self.waveset
        else:
            w = self._process_wave_param(wave)
            utils.validate_wavelengths(w)
            wavelengths = w * self._internal_wave_unit

        return wavelengths

    def __call__(self, wavelengths):
        """Sample the spectrum or bandpass.

        Parameters
        ----------
        wavelengths : array-like or `~astropy.units.quantity.Quantity`
            Wavelength values for sampling. If not a Quantity,
            assumed to be in Angstrom.

        Returns
        -------
        sampled_result : `~astropy.units.quantity.Quantity`
            Sampled flux or throughput in pre-defined internal unit.
            Might have negative values.

        """
        w = self._validate_wavelengths(wavelengths)
        return self.model(w.value) * self._internal_flux_unit

    # Operators are to be implemented by subclasses, where applicable.

    def __add__(self, other):  # pragma: no cover
        """Add self and other."""
        raise NotImplementedError('This operation is not supported.')

    def __sub__(self, other):  # pragma: no cover
        """Subtract other from self."""
        raise NotImplementedError('This operation is not supported.')

    @staticmethod
    def _validate_other_mul_div(other):
        """Conditions for other to satisfy before mul/div."""
        if not isinstance(other, (u.Quantity, numbers.Number,
                                  BaseUnitlessSpectrum, SourceSpectrum)):
            raise exceptions.IncompatibleSources(
                'Can only operate on scalar number/Quantity or spectrum')
        elif (isinstance(other, u.Quantity) and
              (other.unit.decompose() != u.dimensionless_unscaled or
               not np.isscalar(other.value) or
               not isinstance(other.value, numbers.Real))):
            raise exceptions.IncompatibleSources(
                'Can only operate on real scalar dimensionless Quantity')
        elif (isinstance(other, numbers.Number) and
              not (np.isscalar(other) and isinstance(other, numbers.Real))):
            raise exceptions.IncompatibleSources(
                'Can only operate on real scalar number')

    def __mul__(self, other):  # pragma: no cover
        """Multiply self and other."""
        raise NotImplementedError('This operation is not supported.')

    def __rmul__(self, other):
        """This is only called if ``other.__mul__`` cannot operate."""
        return self.__mul__(other)

    def __truediv__(self, other):  # pragma: no cover
        """Divide self by other."""
        raise NotImplementedError('This operation is not supported.')

    def __div__(self, other):  # pragma: py2
        """Same as :meth:`__truediv__` for Python 2 compatibility without
        future import.
        """
        return self.__truediv__(other)

    def integrate(self, wavelengths=None, **kwargs):
        """Perform integration.

        This uses any analytical integral that the
        underlying model has (i.e., ``self.model.integral``).
        If unavailable, it uses the default fall-back integrator
        set in the ``default_integrator`` configuration item.

        If wavelengths are provided, flux or throughput is first resampled.
        This is useful when user wants to integrate at specific end points
        or use custom spacing; In that case, user can pass in desired
        sampling array generated with :func:`numpy.linspace`,
        :func:`numpy.logspace`, etc.
        If not provided, then `waveset` is used.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        kwargs : dict
            Optional keywords to ``__call__`` for sampling.

        Returns
        -------
        result : `~astropy.units.quantity.Quantity`
            Integrated result.

        Raises
        ------
        NotImplementedError
            Invalid default integrator.

        synphot.exceptions.SynphotError
            `waveset` is needed but undefined or cannot integrate
            natively in the given ``flux_unit``.

        """
        # Cannot integrate per Hz units natively across wavelength
        # without converting them to per Angstrom unit first, so
        # less misleading to just disallow that option for now.
        if 'flux_unit' in kwargs:
            self._validate_flux_unit(kwargs['flux_unit'], wav_only=True)

        x = self._validate_wavelengths(wavelengths)

        # TODO: When astropy.modeling.models supports this, need to
        #       make sure that this actually works, and gives correct unit.
        # https://github.com/astropy/astropy/issues/5033
        # https://github.com/astropy/astropy/pull/5108
        try:
            m = self.model.integral
        except (AttributeError, NotImplementedError):
            if conf.default_integrator == 'trapezoid':
                y = self(x, **kwargs)
                result = abs(np.trapz(y.value, x=x.value))
                result_unit = y.unit
            else:  # pragma: no cover
                raise NotImplementedError(
                    'Analytic integral not available and default integrator '
                    '{0} is not supported'.format(conf.default_integrator))
        else:  # pragma: no cover
            start = x[0].value
            stop = x[-1].value
            result = (m(stop) - m(start))
            result_unit = self._internal_flux_unit

        # Ensure final unit takes account of integration across wavelength
        if result_unit != units.THROUGHPUT:
            if result_unit == units.PHOTLAM:
                result_unit = u.photon / (u.cm**2 * u.s)
            elif result_unit == units.FLAM:
                result_unit = u.erg / (u.cm**2 * u.s)
            else:  # pragma: no cover
                raise NotImplementedError(
                    'Integration of {0} is not supported'.format(result_unit))
        else:
            # Ideally flux can use this too but unfortunately this
            # operation results in confusing output unit for flux.
            result_unit *= self._internal_wave_unit

        return result * result_unit

    def avgwave(self, wavelengths=None):
        """Calculate the :ref:`average wavelength <synphot-formula-avgwv>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        Returns
        -------
        avg_wave : `~astropy.units.quantity.Quantity`
            Average wavelength.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value
        num = np.trapz(y * x, x=x)
        den = np.trapz(y, x=x)

        if den == 0:  # pragma: no cover
            avg_wave = 0.0
        else:
            avg_wave = abs(num / den)

        return avg_wave * self._internal_wave_unit

    def barlam(self, wavelengths=None):
        """Calculate :ref:`mean log wavelength <synphot-formula-barlam>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        Returns
        -------
        bar_lam : `~astropy.units.quantity.Quantity`
            Mean log wavelength.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value
        num = np.trapz(y * np.log(x) / x, x=x)
        den = np.trapz(y / x, x=x)

        if num == 0 or den == 0:  # pragma: no cover
            bar_lam = 0.0
        else:
            bar_lam = np.exp(abs(num / den))

        return bar_lam * self._internal_wave_unit

    def pivot(self, wavelengths=None):
        """Calculate :ref:`pivot wavelength <synphot-formula-pivwv>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        Returns
        -------
        pivwv : `~astropy.units.quantity.Quantity`
            Pivot wavelength.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value
        num = np.trapz(y * x, x=x)
        den = np.trapz(y / x, x=x)

        if den == 0:  # pragma: no cover
            pivwv = 0.0
        else:
            pivwv = np.sqrt(abs(num / den))

        return pivwv * self._internal_wave_unit

    def force_extrapolation(self):
        """Force the underlying model to extrapolate.

        An example where this is useful: You create a source spectrum
        with non-default extrapolation behavior and you wish to force
        the underlying empirical model to extrapolate based on nearest point.

        .. note::

            This is only applicable to `~synphot.models.Empirical1D` model
            and should still work even if the source spectrum has been
            redshifted.

        Returns
        -------
        is_forced : bool
            `True` if the model is successfully forced to be extrapolated,
            else `False`.

        """
        # We use _model here in case the spectrum is redshifted.
        if isinstance(self._model, Empirical1D):
            self._model.fill_value = np.nan
            is_forced = True
        else:
            is_forced = False

        return is_forced

    def taper(self, wavelengths=None):
        """Taper the spectrum or bandpass.

        The wavelengths to use for the first and last points are
        calculated by using the same ratio as for the 2 interior points.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for tapering.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        Returns
        -------
        sp : `BaseSpectrum`
            Tapered empirical spectrum or bandpass.
            ``self`` is returned if already tapered (e.g., box model).

        """
        x = self._validate_wavelengths(wavelengths)

        # Calculate new end points for tapering
        w1 = x[0] ** 2 / x[1]
        w2 = x[-1] ** 2 / x[-2]

        # Special handling for empirical data.
        # This is to be compatible with ASTROLIB PYSYNPHOT behavior.
        if isinstance(self._model, Empirical1D):
            y1 = self._model.lookup_table[0]
            y2 = self._model.lookup_table[-1]
        # Other models can just evaluate at new end points
        else:
            y1 = self(w1)
            y2 = self(w2)

        # Nothing to do
        if y1 == 0 and y2 == 0:
            return self  # Do we need a deepcopy here?

        y = self(x)

        if y1 != 0:
            x = np.insert(x, 0, w1)
            y = np.insert(y, 0, 0.0)
        if y2 != 0:
            x = np.insert(x, x.size, w2)
            y = np.insert(y, y.size, 0.0)

        return self.__class__(Empirical1D, points=x, lookup_table=y)

    def _get_arrays(self, wavelengths, **kwargs):
        """Get sampled spectrum or bandpass in user units."""
        x = self._validate_wavelengths(wavelengths)
        y = self(x, **kwargs)

        if isinstance(wavelengths, u.Quantity):
            w = x.to(wavelengths.unit, u.spectral())
        else:
            w = x

        return w, y

    @staticmethod
    def _do_plot(x, y, title='', xlog=False, ylog=False,
                 left=None, right=None, bottom=None, top=None,
                 save_as=''):  # pragma: no cover
        """Plot worker.

        Parameters
        ----------
        x, y : `~astropy.units.quantity.Quantity`
            Wavelength and flux/throughput to plot.

        kwargs
            See :func:`plot`.

        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            log.error('No matplotlib installation found; plotting disabled '
                      'as a result.')
            return

        fig, ax = plt.subplots()
        ax.plot(x, y)

        # Custom wavelength limits
        if left is not None:
            ax.set_xlim(left=left)
        if right is not None:
            ax.set_xlim(right=right)

        # Custom flux/throughput limit
        if bottom is not None:
            ax.set_ylim(bottom=bottom)
        if top is not None:
            ax.set_ylim(top=top)

        xu = x.unit
        if xu.physical_type == 'frequency':
            ax.set_xlabel('Frequency ({0})'.format(xu))
        else:
            ax.set_xlabel('Wavelength ({0})'.format(xu))

        yu = y.unit
        if yu is u.dimensionless_unscaled:
            ax.set_ylabel('Unitless')
        else:
            ax.set_ylabel('Flux ({0})'.format(yu))

        if title:
            ax.set_title(title)

        if xlog:
            ax.set_xscale('log')
        if ylog:
            ax.set_yscale('log')

        plt.draw()

        if save_as:
            plt.savefig(save_as)
            log.info('Plot saved as {0}'.format(save_as))

    def plot(self, wavelengths=None, **kwargs):  # pragma: no cover
        """Plot the spectrum.

        .. note:: Uses ``matplotlib``.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        title : str
            Plot title.

        xlog, ylog : bool
            Plot X and Y axes, respectively, in log scale.
            Default is linear scale.

        left, right : `None` or number
            Minimum and maximum wavelengths to plot.
            If `None`, uses the whole range. If a number is given,
            must be in Angstrom.

        bottom, top : `None` or number
            Minimum and maximum flux/throughput to plot.
            If `None`, uses the whole range. If a number is given,
            must be in internal unit.

        save_as : str
            Save the plot to an image file. The file type is
            automatically determined by given file extension.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        w, y = self._get_arrays(wavelengths)
        self._do_plot(w, y, **kwargs)


class BaseSourceSpectrum(BaseSpectrum):
    """Base class to handle spectrum with flux unit like source spectrum
    and observation. Do not use directly.

    """
    _internal_flux_unit = units.PHOTLAM

    @staticmethod
    def _validate_flux_unit(new_unit, wav_only=False):
        """Make sure flux unit is valid."""
        new_unit = units.validate_unit(new_unit)
        acceptable_types = ['spectral flux density wav',
                            'photon flux density wav']
        acceptable_names = ['PHOTLAM', 'FLAM']

        if not wav_only:  # Include per Hz units
            acceptable_types += ['spectral flux density',
                                 'photon flux density']
            acceptable_names += ['PHOTNU', 'FNU', 'Jy']

        if new_unit.physical_type not in acceptable_types:
            raise exceptions.SynphotError(
                'Source spectrum cannot operate in {0}. Acceptable units: '
                '{1}'.format(new_unit, ','.join(acceptable_names)))

        return new_unit

    def __call__(self, wavelengths, flux_unit=None, **kwargs):
        """Sample the spectrum.

        Parameters
        ----------
        wavelengths : array-like or `~astropy.units.quantity.Quantity`
            Wavelength values for sampling. If not a Quantity,
            assumed to be in Angstrom.

        flux_unit : str or `~astropy.units.core.Unit` or `None`
            Flux is converted to this unit.
            If not given, internal unit is used.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.units.convert_flux`.

        Returns
        -------
        sampled_result : `~astropy.units.quantity.Quantity`
            Sampled flux in the given unit.
            Might have negative values.

        """
        w = self._validate_wavelengths(wavelengths)
        y = self.model(w.value) * self._internal_flux_unit

        if flux_unit is None:
            sampled_result = y
        else:
            sampled_result = units.convert_flux(w, y, flux_unit, **kwargs)

        return sampled_result

    def normalize(self, renorm_val, band=None, wavelengths=None, force=False,
                  area=None, vegaspec=None):
        """Renormalize the spectrum to the given Quantity and band.

        .. warning::

            Redshift attribute (``z``) is reset to 0 in the normalized
            spectrum even if ``self.z`` is non-zero.
            This is because the normalization simply adds a scale
            factor to the existing composite model.
            This is confusing but should not affect the flux sampling.

        Parameters
        ----------
        renorm_val : number or `~astropy.units.quantity.Quantity`
            Value to renormalize the spectrum to. If not a Quantity,
            assumed to be in internal unit.

        band : `SpectralElement`
           Bandpass to use in renormalization.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for renormalization.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        force : bool
            By default (`False`), renormalization is only done
            when band wavelength limits are within ``self``
            or at least 99% of the flux is within the overlap.
            Set to `True` to force renormalization for partial overlap
            (this changes the underlying model of ``self`` to always
            extrapolate, if applicable).
            Disjoint bandpass raises an exception regardless.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        Returns
        -------
        sp : obj
            Renormalized spectrum.

        Raises
        ------
        synphot.exceptions.DisjointError
            Renormalization band does not overlap with ``self``.

        synphot.exceptions.PartialOverlap
            Renormalization band only partially overlaps with ``self``
            and significant amount of flux falls outside the overlap.

        synphot.exceptions.SynphotError
            Invalid inputs or calculation failed.

        """
        warndict = {}

        if band is None:
            sp = self

        else:
            if not isinstance(band, SpectralElement):
                raise exceptions.SynphotError('Invalid bandpass.')

            stat = band.check_overlap(self, wavelengths=wavelengths)

            if stat == 'none':
                raise exceptions.DisjointError(
                    'Spectrum and renormalization band are disjoint.')

            elif 'partial' in stat:
                if stat == 'partial_most':
                    warn_str = 'At least'
                elif stat == 'partial_notmost' and force:
                    warn_str = 'Less than'
                else:
                    raise exceptions.PartialOverlap(
                        'Spectrum and renormalization band do not fully '
                        'overlap. You may use force=True to force the '
                        'renormalization to proceed.')

                warn_str = (
                    'Spectrum is not defined everywhere in renormalization '
                    'bandpass. {0} 99% of the band throughput has '
                    'data. Spectrum will be').format(warn_str)

                if self.force_extrapolation():
                    warn_str = ('{0} extrapolated at constant '
                                'value.').format(warn_str)
                else:
                    warn_str = ('{0} evaluated outside pre-defined '
                                'waveset.').format(warn_str)

                warnings.warn(warn_str, AstropyUserWarning)
                warndict['PartialRenorm'] = warn_str

            elif stat != 'full':  # pragma: no cover
                raise exceptions.SynphotError(
                    'Overlap result of {0} is unexpected.'.format(stat))

            sp = self.__mul__(band)

        if not isinstance(renorm_val, u.Quantity):
            renorm_val = renorm_val * self._internal_flux_unit

        renorm_unit_name = renorm_val.unit.to_string()
        w = sp._validate_wavelengths(wavelengths)

        if (renorm_val.unit == u.count or
                renorm_unit_name == units.OBMAG.to_string()):
            # Special handling for non-density units
            flux_tmp = sp(w, flux_unit=u.count, area=area)
            totalflux = flux_tmp.sum().value
            stdflux = 1.0
        else:
            totalflux = sp.integrate(wavelengths=wavelengths).value

            # VEGAMAG
            if renorm_unit_name == units.VEGAMAG.to_string():
                if not isinstance(vegaspec, SourceSpectrum):
                    raise exceptions.SynphotError(
                        'Vega spectrum is missing.')
                stdspec = vegaspec

            # Magnitude flux-density units
            elif renorm_val.unit in (u.STmag, u.ABmag):
                stdspec = SourceSpectrum(
                    ConstFlux1D, amplitude=(0 * renorm_val.unit))

            # Linear flux-density units
            else:
                stdspec = SourceSpectrum(
                    ConstFlux1D, amplitude=(1 * renorm_val.unit))

            if band is None:
                # TODO: Cannot get this to agree with results
                # from using a very large box bandpass.
                # stdflux = stdspec.integrate(wavelengths=w).value
                raise NotImplementedError('Must provide a bandpass')
            else:
                up = stdspec * band
                stdflux = up.integrate(wavelengths=wavelengths).value

        utils.validate_totalflux(totalflux)

        # Renormalize in magnitudes
        if (renorm_val.unit.decompose() == u.mag or
                isinstance(renorm_val.unit, u.LogUnit)):
            const = renorm_val.value + (2.5 *
                                        np.log10(totalflux / stdflux))
            newsp = self.__mul__(10**(-0.4 * const))
        # Renormalize in linear flux units
        else:
            const = renorm_val.value * (stdflux / totalflux)
            newsp = self.__mul__(const)

        newsp.warnings = warndict
        return newsp


class SourceSpectrum(BaseSourceSpectrum):
    """Class to handle source spectrum.

    Parameters
    ----------
    modelclass, kwargs
        See `BaseSpectrum`.

    z : number
        Redshift to apply to model.

    z_type : {'wavelength_only', 'conserve_flux'}
        Redshift can be done in one of the following ways:

        * ``'wavelength_only'`` only shifts the wavelength
          without adjusting the flux. This is the default behavior
          to be backward compatible with ASTROLIB PYSYNPHOT.
        * ``'conserve_flux'`` also scales the flux to conserve it.

    """
    def __init__(self, modelclass, z=0, z_type='wavelength_only', **kwargs):
        self._valid_z_types = ('wavelength_only', 'conserve_flux')
        self.z_type = z_type
        self.z = z
        super(SourceSpectrum, self).__init__(modelclass, **kwargs)

    def _process_flux_param(self, pval, wave):
        """Process individual model parameter representing flux."""
        if isinstance(pval, u.Quantity):
            self._validate_flux_unit(pval.unit)
            outval = units.convert_flux(self._redshift_model(wave), pval,
                                        self._internal_flux_unit).value
        else:  # Assume already in internal unit
            outval = pval
        return outval

    @property
    def model(self):
        """Model of the spectrum with given redshift."""
        if self.z == 0:
            m = self._model
        else:
            # wavelength
            if self._internal_wave_unit.physical_type == 'length':
                rs = self._redshift_model.inverse
            # frequency or wavenumber
            # NOTE: This will never execute as long as internal wavelength
            #       unit remains Angstrom.
            else:  # pragma: no cover
                rs = self._redshift_model

            if self.z_type == 'wavelength_only':
                m = rs | self._model
            else:  # conserve_flux
                m = rs | self._model | self._redshift_flux_model

        return m

    @property
    def z(self):
        """Redshift of the source spectrum."""
        return self._z

    @z.setter
    def z(self, what):
        """Change redshift."""
        if not isinstance(what, numbers.Real):
            raise exceptions.SynphotError(
                'Redshift must be a real scalar number.')
        self._z = float(what)
        self._redshift_model = RedshiftScaleFactor(self._z)
        if self.z_type == 'wavelength_only':
            self._redshift_flux_model = None
        else:  # conserve_flux
            self._redshift_flux_model = Scale(1 / (1 + self._z))

    @property
    def z_type(self):
        """Redshift behavior."""
        return self._z_type

    @z_type.setter
    def z_type(self, what):
        if what not in self._valid_z_types:
            raise exceptions.SynphotError(
                '{0} is not a valid redshift behavior, choose '
                'from {1}'.format(what, self._valid_z_types))
        self._z_type = what

    def __str__(self):
        """Descriptive information of the spectrum."""
        return '{0} at z={1}\n{2}'.format(
            self.__class__.__name__, self.z, str(self.model))

    def _validate_other_add_sub(self, other):
        """Conditions for other to satisfy before add/sub."""
        if not isinstance(other, self.__class__):
            raise exceptions.IncompatibleSources(
                'Can only operate on {0}.'.format(self.__class__.__name__))

    def __add__(self, other):
        """Add ``self`` with ``other``."""
        self._validate_other_add_sub(other)
        result = self.__class__(self.model + other.model)
        self._merge_meta(self, other, result)
        return result

    def __sub__(self, other):
        """Subtract other from self."""
        self._validate_other_add_sub(other)
        result = self.__class__(self.model - other.model)
        self._merge_meta(self, other, result)
        return result

    def __mul__(self, other):
        """Multiply self and other."""
        self._validate_other_mul_div(other)

        if isinstance(other, (u.Quantity, numbers.Number)):
            newcls = self.__class__(self.model | Scale(other))
        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model * other.model)
        else:  # Source spectrum
            raise exceptions.IncompatibleSources(
                'Cannot multiply two source spectra together')

        self._merge_meta(self, other, newcls)
        return newcls

    def __truediv__(self, other):
        """Divide self by other."""
        self._validate_other_mul_div(other)

        if isinstance(other, (u.Quantity, numbers.Number)):
            newcls = self.__class__(self.model | Scale(1 / other))
        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model / other.model)
        else:  # Source spectrum
            newcls = BaseUnitlessSpectrum(self.model / other.model)

        self._merge_meta(self, other, newcls)
        return newcls

    def plot(self, wavelengths=None, flux_unit=None, area=None, vegaspec=None,
             **kwargs):  # pragma: no cover
        """Plot the spectrum.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        flux_unit : str or `~astropy.units.core.Unit` or `None`
            Flux is converted to this unit for plotting.
            If not given, internal unit is used.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        kwargs : dict
            See :func:`BaseSpectrum.plot`.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        w, y = self._get_arrays(wavelengths, flux_unit=flux_unit, area=area,
                                vegaspec=vegaspec)
        self._do_plot(w, y, **kwargs)

    def to_fits(self, filename, wavelengths=None, flux_unit=None, area=None,
                vegaspec=None, **kwargs):
        """Write the spectrum to a FITS file.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        flux_unit : str or `~astropy.units.core.Unit` or `None`
            Flux is converted to this unit before written out.
            If not given, internal unit is used.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        kwargs : dict
            Keywords accepted by :func:`~synphot.specio.write_fits_spec`.

        """
        w, y = self._get_arrays(wavelengths, flux_unit=flux_unit, area=area,
                                vegaspec=vegaspec)

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'tdisp1': 'G15.7', 'tdisp2': 'G15.7'}

        if 'expr' in self.meta:
            bkeys['expr'] = (self.meta['expr'], 'synphot expression')

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        specio.write_fits_spec(filename, w, y, **kwargs)

    @classmethod
    def from_file(cls, filename, keep_neg=False, **kwargs):
        """Create a spectrum from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Spectrum filename.

        keep_neg : bool
            See `~synphot.models.Empirical1D`.

        kwargs : dict
            Keywords acceptable by
            :func:`~synphot.specio.read_fits_spec` (if FITS) or
            :func:`~synphot.specio.read_ascii_spec` (if ASCII).

        Returns
        -------
        sp : `SourceSpectrum`
            Empirical spectrum.

        """
        header, wavelengths, fluxes = specio.read_spec(filename, **kwargs)
        return cls(Empirical1D, points=wavelengths, lookup_table=fluxes,
                   keep_neg=keep_neg, meta={'header': header})

    @classmethod
    def from_vega(cls, **kwargs):
        """Load :ref:`Vega spectrum <synphot-vega-spec>`.

        Parameters
        ----------
        kwargs : dict
            Keywords acceptable by :func:`~synphot.specio.read_remote_spec`.

        Returns
        -------
        vegaspec : `SourceSpectrum`
            Empirical Vega spectrum.

        """
        filename = conf.vega_file
        header, wavelengths, fluxes = specio.read_remote_spec(
            filename, **kwargs)
        header['filename'] = filename
        meta = {'header': header,
                'expr': 'Vega from {0}'.format(os.path.basename(filename))}
        return cls(Empirical1D, points=wavelengths, lookup_table=fluxes,
                   meta=meta)


class BaseUnitlessSpectrum(BaseSpectrum):
    """Base class to handle unitless spectrum like bandpass, reddening, etc."""
    _internal_flux_unit = units.THROUGHPUT

    def _process_flux_param(self, pval, wave):
        """Process individual model parameter representing throughput."""
        return self._process_generic_param(pval, self._internal_flux_unit)

    @staticmethod
    def _validate_flux_unit(new_unit):  # pragma: no cover
        """Make sure flux unit is valid."""
        new_unit = units.validate_unit(new_unit)

        if new_unit.decompose() != u.dimensionless_unscaled:
            raise exceptions.SynphotError(
                'Unit {0} is not dimensionless'.format(new_unit))

        return new_unit

    def __mul__(self, other):
        """Multiply self and other."""
        do_meta_merge = True
        self._validate_other_mul_div(other)

        if isinstance(other, (u.Quantity, numbers.Number)):
            newcls = self.__class__(self.model | Scale(other))
        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model * other.model)
        else:  # SourceSpectrum
            do_meta_merge = False
            newcls = other.__mul__(self)

        if do_meta_merge:
            self._merge_meta(self, other, newcls)

        return newcls

    def __truediv__(self, other):
        """Divide self by other."""
        self._validate_other_mul_div(other)

        if isinstance(other, (u.Quantity, numbers.Number)):
            newcls = self.__class__(self.model | Scale(1 / other))
        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model / other.model)
        else:  # SourceSpectrum
            raise exceptions.IncompatibleSources(
                'Cannot divide by source spectrum')

        self._merge_meta(self, other, newcls)
        return newcls


class SpectralElement(BaseUnitlessSpectrum):
    """Class to handle instrument filter bandpass.

    Parameters
    ----------
    modelclass, kwargs
        See `BaseSpectrum`.

    """
    def check_overlap(self, other, wavelengths=None, threshold=0.01):
        """Check for wavelength overlap between two spectra.

        Only wavelengths where ``self`` throughput is non-zero
        are considered.

        Example of full overlap::

            |---------- other ----------|
               |------ self ------|

        Examples of partial overlap::

            |---------- self ----------|
               |------ other ------|

            |---- other ----|
               |---- self ----|

            |---- self ----|
               |---- other ----|

        Examples of no overlap::

            |---- self ----|  |---- other ----|

            |---- other ----|  |---- self ----|

        Parameters
        ----------
        other : `BaseSpectrum`

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        threshold : float
            If less than this fraction of flux or throughput falls
            outside wavelength overlap, the *lack* of overlap is
            *insignificant*. This is only used when partial overlap
            is detected. Default is 1%.

        Returns
        -------
        result : {'full', 'partial_most', 'partial_notmost', 'none'}
            * 'full' - ``self`` coverage is within or same as ``other``
            * 'partial_most' - Less than ``threshold`` fraction of
              ``self`` flux is outside the overlapping wavelength
              region, i.e., the *lack* of overlap is *insignificant*
            * 'partial_notmost' - ``self`` partially overlaps with
              ``other`` but does not qualify for 'partial_most'
            * 'none' - ``self`` does not overlap ``other``

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        if not isinstance(other, BaseSpectrum):
            raise exceptions.SynphotError(
                'other must be spectrum or bandpass.')

        # Special cases where no sampling wavelengths given and
        # one of the inputs is continuous.
        if wavelengths is None:
            if other.waveset is None:
                return 'full'
            if self.waveset is None:
                return 'partial_notmost'

        x1 = self._validate_wavelengths(wavelengths)
        y1 = self(x1)
        a = x1[y1 > 0].value

        b = other._validate_wavelengths(wavelengths).value

        result = utils.overlap_status(a, b)

        if result == 'partial':
            # If there is no need to extrapolate or taper other
            # (i.e., other is zero at self's wave limits),
            # then we consider it as a full coverage.
            # This logic assumes __call__ never returns mag or count!
            if ((isinstance(other.model, Empirical1D) and
                 other.model.is_tapered() or
                 not isinstance(other.model,
                                (Empirical1D, _CompoundModel))) and
                    np.allclose(other(x1[::x1.size - 1]).value, 0)):
                result = 'full'

            # Check if the lack of overlap is significant.
            else:
                # Get all the flux
                totalflux = self.integrate(wavelengths=wavelengths).value
                utils.validate_totalflux(totalflux)

                a_min, a_max = a.min(), a.max()
                b_min, b_max = b.min(), b.max()

                # Now get the other two pieces
                excluded = 0.0
                if a_min < b_min:
                    excluded += self.integrate(
                        wavelengths=np.array([a_min, b_min])).value
                if a_max > b_max:
                    excluded += self.integrate(
                        wavelengths=np.array([b_max, a_max])).value

                if excluded / totalflux < threshold:
                    result = 'partial_most'
                else:
                    result = 'partial_notmost'

        return result

    def unit_response(self, area, wavelengths=None):
        """Calculate :ref:`unit response <synphot-formula-uresp>`
        of this bandpass.

        Parameters
        ----------
        area : float or `~astropy.units.quantity.Quantity`
            Area that flux covers. If not a Quantity, assumed to be in
            :math:`cm^{2}`.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        uresp : `~astropy.units.quantity.Quantity`
            Flux (in FLAM) of a star that produces a response of
            one photon per second in this bandpass.

        """
        a = units.validate_quantity(area, units.AREA)

        # Only correct if wavelengths are in Angstrom.
        x = self._validate_wavelengths(wavelengths).value

        y = self(x).value * x
        int_val = abs(np.trapz(y, x=x))
        uresp = units.HC / (a.cgs * int_val)

        return uresp.value * units.FLAM

    def rmswidth(self, wavelengths=None, threshold=None):
        """Calculate the :ref:`bandpass RMS width <synphot-formula-rmswidth>`.
        Not to be confused with :func:`photbw`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        threshold : float or `~astropy.units.quantity.Quantity`, optional
            Data points with throughput below this value are not
            included in the calculation. By default, all data points
            are included.

        Returns
        -------
        rms_width : `~astropy.units.quantity.Quantity`
            RMS width of the bandpass.

        Raises
        ------
        synphot.exceptions.SynphotError
            Threshold is invalid.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value

        if threshold is None:
            wave = x
            thru = y
        else:
            if (isinstance(threshold, numbers.Real) or
                (isinstance(threshold, u.Quantity) and
                 threshold.unit == self._internal_flux_unit)):
                mask = y >= threshold
            else:
                raise exceptions.SynphotError(
                    '{0} is not a valid threshold'.format(threshold))
            wave = x[mask]
            thru = y[mask]

        a = self.avgwave(wavelengths=wavelengths).value
        num = np.trapz((wave - a) ** 2 * thru, x=wave)
        den = np.trapz(thru, x=wave)

        if den == 0:  # pragma: no cover
            rms_width = 0.0
        else:
            rms_width = np.sqrt(abs(num / den))

        return rms_width * self._internal_wave_unit

    def photbw(self, wavelengths=None, threshold=None):
        """Calculate the
        :ref:`bandpass RMS width as in IRAF SYNPHOT <synphot-formula-bandw>`.

        This is a compatibility function. To calculate the actual
        bandpass RMS width, use :func:`rmswidth`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        threshold : float or `~astropy.units.quantity.Quantity`, optional
            Data points with throughput below this value are not
            included in the calculation. By default, all data points
            are included.

        Returns
        -------
        bandw : `~astropy.units.quantity.Quantity`
            IRAF SYNPHOT RMS width of the bandpass.

        Raises
        ------
        synphot.exceptions.SynphotError
            Threshold is invalid.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value

        if threshold is None:
            wave = x
            thru = y
        else:
            if (isinstance(threshold, numbers.Real) or
                (isinstance(threshold, u.Quantity) and
                 threshold.unit == self._internal_flux_unit)):
                mask = y >= threshold
            else:
                raise exceptions.SynphotError(
                    '{0} is not a valid threshold'.format(threshold))
            wave = x[mask]
            thru = y[mask]

        a = self.barlam(wavelengths=wavelengths).value

        if a == 0:
            bandw = 0.0
        else:
            num = np.trapz(thru * np.log(wave / a) ** 2 / wave, x=wave)
            den = np.trapz(thru / wave, x=wave)

            if den == 0:  # pragma: no cover
                bandw = 0.0
            else:
                bandw = a * np.sqrt(abs(num / den))

        return bandw * self._internal_wave_unit

    def fwhm(self, **kwargs):
        """Calculate :ref:`synphot-formula-fwhm` of equivalent gaussian.

        Parameters
        ----------
        kwargs : dict
            See :func:`photbw`.

        Returns
        -------
        fwhm_val : `~astropy.units.quantity.Quantity`
            FWHM of equivalent gaussian.

        """
        return np.sqrt(8 * np.log(2)) * self.photbw(**kwargs)

    def tlambda(self, **kwargs):
        """Calculate throughput at
        :ref:`bandpass average wavelength <synphot-formula-avgwv>`.

        Parameters
        ----------
        kwargs : dict
            See :func:`~BaseSpectrum.avgwave`.

        Returns
        -------
        t_lambda : `~astropy.units.quantity.Quantity`
            Throughput at bandpass average wavelength.

        """
        return self(self.avgwave(**kwargs))

    def tpeak(self, wavelengths=None):
        """Calculate :ref:`peak bandpass throughput <synphot-formula-tpeak>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        tpeak : `~astropy.units.quantity.Quantity`
            Peak bandpass throughput.

        """
        x = self._validate_wavelengths(wavelengths).value
        return self(x).max()

    def wpeak(self, wavelengths=None):
        """Calculate
        :ref:`wavelength at peak throughput <synphot-formula-tpeak>`.

        If there are multiple data points with peak throughput
        value, only the first match is returned.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        wpeak : `~astropy.units.quantity.Quantity`
            Wavelength at peak throughput.

        """
        x = self._validate_wavelengths(wavelengths)
        return x[self(x) == self.tpeak(wavelengths=wavelengths)][0]

    def equivwidth(self, wavelengths=None):
        """Calculate :ref:`bandpass equivalent width <synphot-formula-equvw>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        equvw : `~astropy.units.quantity.Quantity`
            Bandpass equivalent width.

        """
        return self.integrate(wavelengths=wavelengths)

    def rectwidth(self, wavelengths=None):
        """Calculate :ref:`bandpass rectangular width <synphot-formula-rectw>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        rectw : `~astropy.units.quantity.Quantity`
            Bandpass rectangular width.

        """
        equvw = self.equivwidth(wavelengths=wavelengths)
        tpeak = self.tpeak(wavelengths=wavelengths)

        if tpeak.value == 0:  # pragma: no cover
            rectw = 0.0 * self._internal_wave_unit
        else:
            rectw = equvw / tpeak

        return rectw

    def efficiency(self, wavelengths=None):
        """Calculate :ref:`dimensionless efficiency <synphot-formula-qtlam>`.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        qtlam : `~astropy.units.quantity.Quantity`
            Dimensionless efficiency.

        """
        x = self._validate_wavelengths(wavelengths).value
        y = self(x).value
        qtlam = abs(np.trapz(y / x, x=x))
        return qtlam * u.dimensionless_unscaled

    def emflx(self, area, wavelengths=None):
        """Calculate
        :ref:`equivalent monochromatic flux <synphot-formula-emflx>`.

        Parameters
        ----------
        area, wavelengths
            See :func:`unit_response`.

        Returns
        -------
        em_flux : `~astropy.units.quantity.Quantity`
            Equivalent monochromatic flux.

        """
        t_lambda = self.tlambda(wavelengths=wavelengths)

        if t_lambda == 0:  # pragma: no cover
            em_flux = 0.0 * units.FLAM
        else:
            uresp = self.unit_response(area, wavelengths=wavelengths)
            equvw = self.equivwidth(wavelengths=wavelengths).value
            em_flux = uresp * equvw / t_lambda

        return em_flux

    def to_fits(self, filename, wavelengths=None, **kwargs):
        """Write the bandpass to a FITS file.

        Throughput column is automatically named 'THROUGHPUT'.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        kwargs : dict
            Keywords accepted by :func:`~synphot.specio.write_fits_spec`.

        """
        w, y = self._get_arrays(wavelengths)

        kwargs['flux_col'] = 'THROUGHPUT'
        kwargs['flux_unit'] = self._internal_flux_unit

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'tdisp1': 'G15.7', 'tdisp2': 'G15.7'}

        if 'expr' in self.meta:
            bkeys['expr'] = (self.meta['expr'], 'synphot expression')

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        specio.write_fits_spec(filename, w, y, **kwargs)

    @classmethod
    def from_file(cls, filename, **kwargs):
        """Creates a bandpass from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Bandpass filename.

        kwargs : dict
            Keywords acceptable by
            :func:`~synphot.specio.read_fits_spec` (if FITS) or
            :func:`~synphot.specio.read_ascii_spec` (if ASCII).

        Returns
        -------
        bp : `SpectralElement`
            Empirical bandpass.

        """
        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = cls._internal_flux_unit

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'THROUGHPUT'

        header, wavelengths, throughput = specio.read_spec(filename, **kwargs)
        return cls(Empirical1D, points=wavelengths, lookup_table=throughput,
                   keep_neg=True, meta={'header': header})

    @classmethod
    def from_filter(cls, filtername, **kwargs):
        """Load :ref:`pre-defined filter bandpass <synphot-predefined-filter>`.

        Parameters
        ----------
        filtername : str
            Filter name. Choose from 'bessel_j', 'bessel_h', 'bessel_k',
            'cousins_r', 'cousins_i', 'johnson_u', 'johnson_b', 'johnson_v',
            'johnson_r', 'johnson_i', 'johnson_j', or 'johnson_k'.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.specio.read_remote_spec`.

        Returns
        -------
        bp : `SpectralElement`
            Empirical bandpass.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid filter name.

        """
        filtername = filtername.lower()

        # Select filename based on filter name
        if filtername == 'bessel_j':
            cfgitem = Conf.bessel_j_file
        elif filtername == 'bessel_h':
            cfgitem = Conf.bessel_h_file
        elif filtername == 'bessel_k':
            cfgitem = Conf.bessel_k_file
        elif filtername == 'cousins_r':
            cfgitem = Conf.cousins_r_file
        elif filtername == 'cousins_i':
            cfgitem = Conf.cousins_i_file
        elif filtername == 'johnson_u':
            cfgitem = Conf.johnson_u_file
        elif filtername == 'johnson_b':
            cfgitem = Conf.johnson_b_file
        elif filtername == 'johnson_v':
            cfgitem = Conf.johnson_v_file
        elif filtername == 'johnson_r':
            cfgitem = Conf.johnson_r_file
        elif filtername == 'johnson_i':
            cfgitem = Conf.johnson_i_file
        elif filtername == 'johnson_j':
            cfgitem = Conf.johnson_j_file
        elif filtername == 'johnson_k':
            cfgitem = Conf.johnson_k_file
        else:
            raise exceptions.SynphotError(
                'Filter name {0} is invalid.'.format(filtername))

        filename = cfgitem()

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = cls._internal_flux_unit

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'THROUGHPUT'

        header, wavelengths, throughput = specio.read_remote_spec(
            filename, **kwargs)
        header['filename'] = filename
        header['descrip'] = cfgitem.description
        meta = {'header': header, 'expr': filtername}
        return cls(Empirical1D, points=wavelengths, lookup_table=throughput,
                   meta=meta)
