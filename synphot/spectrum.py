# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines the different types of spectra."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from astropy.extern import six

# STDLIB
import numbers
import os
import warnings

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import log
#from astropy import modeling
from astropy import units as u
from astropy.utils.exceptions import AstropyUserWarning

# STSCI
from jwst_lib import modeling

# LOCAL
from . import exceptions, specio, units, utils
from .config import Conf, conf
from .integrator import TrapezoidIntegrator, TrapezoidFluxIntegrator
from .models import BlackBody1D, ConstFlux1D, Empirical1D, Redshift

__all__ = ['BaseSpectrum', 'BaseSourceSpectrum', 'SourceSpectrum',
           'BaseUnitlessSpectrum', 'SpectralElement']


# TODO: Update model logic when astropy.modeling supports
#       Quantity or metadata.
class BaseSpectrum(object):
    """Base class to handle spectrum or bandpass.

    .. note::

        Until `astropy.modeling` can handle units, all parameters
        are converted to pre-defined internal units.

    Parameters
    ----------
    modelclass : cls
        Model class from `astropy.modeling`.

    metadata : dict
        Metadata associated with the spectrum or bandpass
        (warnings, legacy SYNPHOT expression, FITS header, etc).

    kwargs : dict
        Model parameters accepted by ``modelclass``. Each parameter can
        be either a Quantity or number. If the latter, assume pre-defined
        internal units.

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
        'Box1D': {'amplitude': 'flux', 'x_0': 'wave', 'width': 'wave'},
        'BrokenPowerLaw1D': {
            'amplitude': 'flux', 'x_break': 'wave',
            'alpha_1': u.dimensionless_unscaled,
            'alpha_2': u.dimensionless_unscaled},
        'Const1D': {'amplitude': 'noconv'},
        'ConstFlux1D': {'amplitude': 'noconv'},
        'Empirical1D': {'x': 'wave', 'y': 'flux', 'keep_neg': 'noconv'},
        'ExponentialCutoffPowerLaw1D': {
            'amplitude': 'flux', 'x_0': 'wave', 'x_cutoff': 'wave',
            'alpha': u.dimensionless_unscaled},
        'Gaussian1D': {'amplitude': 'flux', 'mean': 'wave', 'stddev': 'wave'},
        'GaussianAbsorption1D': {
            'amplitude': 'flux', 'mean': 'wave', 'stddev': 'wave'},
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
            'alpha': u.dimensionless_unscaled}}

    # Flux conversion will use these wavelengths.
    _model_fconv_wav = {
        'Box1D': 'x_0',
        'BrokenPowerLaw1D': 'x_break',
        'Empirical1D': 'x',
        'ExponentialCutoffPowerLaw1D': 'x_0',
        'Gaussian1D': 'mean',
        'GaussianAbsorption1D': 'mean',
        'LogParabola1D': 'x_0',
        'Lorentz1D': 'x_0',
        'MexicanHat1D': 'x_0',
        'PowerLaw1D': 'x_0'}

    def __init__(self, modelclass, metadata={}, **kwargs):
        self._build_model(modelclass, **kwargs)

        self.metadata = metadata
        if 'warnings' not in self.metadata:
            self.metadata['warnings'] = {}
        if hasattr(self.model, 'warnings'):
            self.metadata['warnings'].update(self.model.warnings)

    def _build_model(self, modelclass, **kwargs):
        """Build the model."""

        # This is needed for internal math operations to build composite model.
        # Handles the model instance, not class. Assume it is already in the
        # correct units and param_dim.
        if isinstance(modelclass, modeling.core.Model):
            self._model = modelclass
            return
        if isinstance(modelclass, BaseSpectrum):
            self._model = modelclass.model
            return

        if not issubclass(modelclass, modeling.core.Model):
            raise exceptions.SynphotError(
                '{0} is not a valid model class.'.format(modelclass))

        modelname = modelclass.__name__
        if modelname not in self._model_param_dict:
            raise exceptions.SynphotError(
                '{0} is not supported.'.format(modelname))

        modargs = {}

        # Process wavelength needed for flux conversion first, if applicable.
        if modelname in self._model_fconv_wav:
            pname_wav = self._model_fconv_wav[modelname]
            pval_wav = self._process_wave_param(kwargs[pname_wav])
            modargs[pname_wav] = pval_wav
        else:
            pname_wav = ''
            pval_wav = None

        # Process the rest of the parameters.
        for pname, ptype in six.iteritems(self._model_param_dict[modelname]):
            if pname not in kwargs:
                continue
            if pname == pname_wav:
                continue
            kval = kwargs[pname]
            if ptype == 'wave':
                pval = self._process_wave_param(kval)
            elif ptype == 'flux':
                pval = self._process_flux_param(kval, pval_wav)
            elif ptype == 'noconv':
                pval = kval
            else:
                pval = self._process_generic_param(kval, ptype)
            modargs[pname] = pval

        model = modelclass(**modargs)
        if model.param_dim != 1:
            raise exceptions.SynphotError('Model can only have param_dim=1')

        self._model = model

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
        return self.metadata['warnings']

    @property
    def waveset(self):
        """Optimal wavelengths for sampling the spectrum or bandpass."""
        w = utils.get_waveset(self.model)
        if w is not None:
            utils.validate_wavelengths(w)
            w = u.Quantity(w, self._internal_wave_unit)
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
            wavelengths = u.Quantity(w, self._internal_wave_unit)

        return wavelengths

    def __call__(self, wavelengths):
        """Sample the spectrum or bandpass.

        Parameters
        ----------
        wavelengths : array_like or `~astropy.units.quantity.Quantity`
            Wavelength values for sampling. If not a Quantity,
            assumed to be in Angstrom.

        Returns
        -------
        sampled_result : `~astropy.units.quantity.Quantity`
            Sampled flux or throughput in pre-defined internal unit
            that is in-sync with given wavelengths.
            Might have negative values.

        """
        w = self._validate_wavelengths(wavelengths)
        return u.Quantity(self.model(w.value), unit=self._internal_flux_unit)

    def __mul__(self, other):
        """Multiply self and other."""
        raise NotImplementedError('To be implemented by subclasses.')

    def __rmul__(self, other):
        """This is only called if ``other.__mul__`` cannot operate."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide self by other."""
        raise NotImplementedError('To be implemented by subclasses.')

    def __div__(self, other):
        """Same as :func:`__truediv__`."""
        return self.__truediv__(other)

    def integrate(self, wavelengths=None):
        """Perform trapezoid integration.

        If wavelengths are provided, flux is first resampled.
        Otherwise, `waveset` is used.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `waveset` is used.

        Returns
        -------
        result : `~astropy.units.quantity.Quantity`
            Integrated result in pre-defined internal unit.

        Raises
        ------
        synphot.exceptions.SynphotError
            `waveset` is needed but undefined.

        """
        x = self._validate_wavelengths(wavelengths)
        return TrapezoidIntegrator()(self, x.value)

    def avgwave(self, wavelengths=None):
        """Calculate the :ref:`average wavelength <synphot-formula-avgwv>`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        t = TrapezoidIntegrator()
        num = t._raw_math(x, y * x)
        den = t._raw_math(x, y)

        if den == 0:  # pragma: no cover
            avg_wave = 0.0
        else:
            avg_wave = num / den

        return u.Quantity(avg_wave, unit=self._internal_wave_unit)

    def barlam(self, wavelengths=None):
        """Calculate :ref:`mean log wavelength <synphot-formula-barlam>`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        t = TrapezoidIntegrator()
        num = t._raw_math(x, y * np.log(x) / x)
        den = t._raw_math(x, y / x)

        if num == 0 or den == 0:  # pragma: no cover
            bar_lam = 0.0
        else:
            bar_lam = np.exp(num / den)

        return u.Quantity(bar_lam, unit=self._internal_wave_unit)

    def pivot(self, wavelengths=None):
        """Calculate :ref:`pivot wavelength <synphot-formula-pivwv>`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        t = TrapezoidIntegrator()
        num = t._raw_math(x, y * x)
        den = t._raw_math(x, y / x)

        if den == 0:  # pragma: no cover
            pivwv = 0.0
        else:
            val = num / den
            if val < 0:  # pragma: no cover
                pivwv = 0.0
            else:
                pivwv = np.sqrt(val)

        return u.Quantity(pivwv, self._internal_wave_unit)

    def check_overlap(self, other, wavelengths=None, threshold=0.01):
        """Check for wavelength overlap between two spectra.

        Only wavelengths where the flux or throughput is non-zero
        are considered.

        Parameters
        ----------
        other : `BaseSpectrum`

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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

        x2 = other._validate_wavelengths(wavelengths)
        y2 = other(x2)
        b = x2[y2 > 0].value

        result = utils.overlap_status(a, b)

        if result == 'partial':
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

    def taper(self, wavelengths=None):
        """Taper the spectrum or bandpass.

        The wavelengths to use for the first and last points are
        calculated by using the same ratio as for the 2 interior points.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        w1 = x[0] ** 2 / x[1]
        y1 = self(w1)
        w2 = x[-1] ** 2 / x[-2]
        y2 = self(w2)

        # Nothing to do
        if y1 == 0 and y2 == 0:
            return self  # deepcopy?

        y = self(x)

        if y1 != 0:
            x = np.insert(x, 0, w1)
            y = np.insert(y, 0, 0.0)
        if y2 != 0:
            x = np.insert(x, x.size, w2)
            y = np.insert(y, y.size, 0.0)

        return self.__class__(Empirical1D, x=x, y=y)

    def _get_arrays(self, wavelengths):
        """Get sampled spectrum or bandpass in user units."""
        x = self._validate_wavelengths(wavelengths)
        y = self(x)

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
        ax.plot(x.value, y.value)

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

        ax.set_xlabel('{0}'.format(x.unit))
        ax.set_ylabel('{0}'.format(y.unit))

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
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
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
    def _validate_flux_unit(new_unit):
        """Make sure flux unit is valid."""
        new_unit = units.validate_unit(new_unit)
        acceptable_types = [
            'spectral flux density', 'spectral flux density wav',
            'photon flux density', 'photon flux density wav']

        if new_unit.physical_type not in acceptable_types:
            raise exceptions.SynphotError(
                'Source spectrum cannot operate in {0}. Acceptable units are '
                'PHOTLAM, PHOTNU, FLAM, FNU, or Jy.'.format(new_unit))

        return new_unit

    def integrate(self, wavelengths=None, flux_unit=units.PHOTLAM, **kwargs):
        """Perform trapezoid integration.

        If wavelengths are provided, flux is first resampled.
        Otherwise, ``self.waveset`` is used.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        flux_unit : str or `~astropy.units.core.Unit`
            Flux is converted to this unit first prior to integration.

        kwargs : dict
            Keywords accepted by :func:`~synphot.units.convert_flux`.

        Returns
        -------
        result : `~astropy.units.quantity.Quantity`
            Integrated result in the given flux unit.
            It is zero if calculations failed.

        Raises
        ------
        synphot.exceptions.SynphotError
            ``self.waveset`` is needed but undefined.

        """
        x = self._validate_wavelengths(wavelengths)
        result = TrapezoidFluxIntegrator()(
            self, x.value, flux_unit=flux_unit, **kwargs)
        return u.Quantity(result, unit=flux_unit)

    def _get_arrays(self, wavelengths, flux_unit, area=None, vegaspec=None):
        """Get sampled spectrum or bandpass in user units."""
        x = self._validate_wavelengths(wavelengths)
        y = units.convert_flux(x, self(x), flux_unit,
                               area=area, vegaspec=vegaspec)

        if isinstance(wavelengths, u.Quantity):
            w = x.to(wavelengths.unit, u.spectral())
        else:
            w = x

        return w, y

    def normalize(self, renorm_val, band=None, wavelengths=None, force=False,
                  area=None, vegaspec=None):
        """Renormalize the spectrum to the given Quantity and band.

        Parameters
        ----------
        renorm_val : number or `~astropy.units.quantity.Quantity`
            Value to renormalize the spectrum to. If not a Quantity,
            assumed to be in internal unit.

        band : `SpectralElement`
           Bandpass to use in renormalization.

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for renormalization.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        force : bool
            By default (`False`), renormalization is only done
            when band wavelength limits are within ``self``
            or at least 99% of the flux is within the overlap.
            Set to `True` to force renormalization for partial overlap.
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

            elif stat == 'partial_most':
                warn_str = (
                    'Spectrum is not defined everywhere in renormalization' +
                    'bandpass. At least 99% of the band throughput has' +
                    'data. Spectrum will be extrapolated at constant value.')
                warndict['PartialRenorm'] = warn_str
                warnings.warn(warn_str, AstropyUserWarning)

            elif stat == 'partial_notmost':
                if force:
                    warn_str = (
                        'Spectrum is not defined everywhere in '
                        'renormalization bandpass. Less than 99% of the ' +
                        'band throughput has data. Spectrum will be ' +
                        'extrapolated at constant value.')
                    warndict['PartialRenorm'] = warn_str
                    warnings.warn(warn_str, AstropyUserWarning)
                else:
                    raise exceptions.PartialOverlap(
                        'Spectrum and renormalization band do not fully '
                        'overlap. You may use force=True to force the '
                        'renormalization to proceed.')

            elif stat != 'full':  # pragma: no cover
                raise exceptions.SynphotError(
                    'Overlap result of {0} is unexpected.'.format(stat))

            sp = self.__mul__(band)

        if not isinstance(renorm_val, u.Quantity):
            renorm_val = u.Quantity(renorm_val, unit=self._internal_flux_unit)

        renorm_unit_name = renorm_val.unit.to_string()
        w = sp._validate_wavelengths(wavelengths)

        if renorm_unit_name in (u.count.to_string(), units.OBMAG.to_string()):
            # Special handling for non-density units
            flux_tmp = units.convert_flux(w, sp(w), u.count, area=area)
            totalflux = flux_tmp.sum()
            stdflux = 1.0
        else:
            totalflux = sp.integrate(wavelengths=wavelengths)
            # VEGAMAG
            if renorm_unit_name == units.VEGAMAG.to_string():
                if not isinstance(vegaspec, SourceSpectrum):
                    raise exceptions.SynphotError(
                        'Vega spectrum is missing.')
                stdspec = vegaspec
            # Magnitude flux-density units
            elif renorm_unit_name == units.STMAG.to_string():
                stdspec = SourceSpectrum(
                    ConstFlux1D, amplitude=u.Quantity(0, units.STMAG))
            elif renorm_unit_name == units.ABMAG.to_string():
                stdspec = SourceSpectrum(
                    ConstFlux1D, amplitude=u.Quantity(0, units.ABMAG))
            # Linear flux-density units
            else:
                stdspec = SourceSpectrum(
                    ConstFlux1D, amplitude=u.Quantity(1, renorm_val.unit))

            if band is None:
                stdflux = stdspec.integrate(wavelengths=w).value
            else:
                up = stdspec * band
                stdflux = up.integrate(wavelengths=wavelengths).value

        utils.validate_totalflux(totalflux.value)

        # Renormalize in magnitudes
        if renorm_val.unit.decompose() == u.mag:
            const = renorm_val.value + 2.5 * np.log10(totalflux.value / stdflux)
            newsp = self.__mul__(10**(-0.4 * const))
        # Renormalize in linear flux units
        else:
            const = renorm_val.value * (stdflux / totalflux.value)
            newsp = self.__mul__(const)

        newsp.metadata['warnings'].update(warndict)
        return newsp


class SourceSpectrum(BaseSourceSpectrum):
    """Class to handle source spectrum.

    Parameters
    ----------
    modelclass, metadata, kwargs
        See `BaseSpectrum`.

    z : number
        Redshift to apply to model.

    """
    def __init__(self, modelclass, z=0, **kwargs):
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
                rs = self._redshift_model.inverse()
            # frequency or wavenumber
            else:  # pragma: no cover
                rs = self._redshift_model
            m = modeling.core.SerialCompositeModel([rs, self._model])
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
        self._redshift_model = Redshift(self._z)

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
        return self.__class__(self.model + other.model)

    def __sub__(self, other):
        """Subtract other from self."""
        self._validate_other_add_sub(other)
        return self.__class__(self.model - other.model)

    def __mul__(self, other):
        """Multiply self and other."""
        if isinstance(other, (u.Quantity, numbers.Number)):
            if isinstance(other, u.Quantity):
                if other.unit.decompose() != u.dimensionless_unscaled:
                    raise exceptions.IncompatibleSources(
                        'Can only operate on dimensionless Quantity.')
                val = other.value
            else:
                val = other

            if not np.isscalar(val) or not isinstance(val, numbers.Real):
                raise exceptions.IncompatibleSources(
                    'Can only operate on real scalar number.')

            newcls = self.__class__(self.model * val)

        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model * other.model)

        else:
            raise exceptions.IncompatibleSources(
                'Can only operate on scalar number/Quantity or '
                'unitless spectrum.')

        return newcls

    def __truediv__(self, other):
        """Divide self by other (unavailable in ASTROLIB PYSYNPHOT)."""
        raise NotImplementedError('Currently unsupported.')

    def plot(self, wavelengths=None, flux_unit=units.PHOTLAM, area=None,
             vegaspec=None, **kwargs):  # pragma: no cover
        """Plot the spectrum.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        flux_unit : str or `~astropy.units.core.Unit`
            Flux is converted to this unit for plotting.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        kwargs : dict
            See :func:`BaseSpectrum.plot`.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        w, y = self._get_arrays(wavelengths, flux_unit, area=area,
                                vegaspec=vegaspec)
        self._do_plot(w, y, **kwargs)

    def to_fits(self, filename, wavelengths=None, flux_unit=units.PHOTLAM,
                area=None, vegaspec=None, **kwargs):
        """Write the spectrum to a FITS file.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        flux_unit : str or `~astropy.units.core.Unit`
            Flux is converted to this unit before written out.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        kwargs : dict
            Keywords accepted by :func:`~synphot.specio.write_fits_spec`.

        """
        w, y = self._get_arrays(wavelengths, flux_unit, area=area,
                                vegaspec=vegaspec)

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'tdisp1': 'G15.7', 'tdisp2': 'G15.7'}

        if 'expr' in self.metadata:
            bkeys['expr'] = (self.metadata['expr'], 'synphot expression')

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
        return cls(Empirical1D, x=wavelengths, y=fluxes, keep_neg=keep_neg,
                   metadata=header)

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
        header['expr'] = 'Vega from {0}'.format(os.path.basename(filename))
        header['filename'] = filename
        return cls(Empirical1D, x=wavelengths, y=fluxes, metadata=header)

    @classmethod
    def from_gaussian(cls, total_flux, center, fwhm, z=0, **kwargs):
        """Create a spectrum from a :ref:`Gaussian source <synphot-gaussian>`.

        Parameters
        ----------
        total_flux : float or `~astropy.units.quantity.Quantity`
            Total flux under Gaussian. If not a Quantity, assumed
            to be in FLAM.

        center : float or `~astropy.units.quantity.Quantity`
            Central wavelength of Gaussian.
            If not a Quantity, assumed to be in Angstrom.

        fwhm : float or `~astropy.units.quantity.Quantity`
            Full-width-at-half-maximum (FWHM) of Gaussian.
            If not a Quantity, assumed to be in Angstrom.

        z : number
            Redshift to apply to model.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.units.convert_flux`.

        Returns
        -------
        gspec : `SourceSpectrum`
            ``Gaussian1D`` spectrum.

        """
        if isinstance(center, u.Quantity):
            x0 = center.to(cls._internal_wave_unit, u.spectral()).value
        else:
            x0 = center

        if isinstance(fwhm, u.Quantity):
            fh = fwhm.to(cls._internal_wave_unit, u.spectral()).value
        else:
            fh = fwhm

        if not isinstance(total_flux, u.Quantity):
            total_flux = u.Quantity(total_flux, units.FLAM)

        tf = units.convert_flux(
            x0, total_flux, cls._internal_flux_unit, **kwargs).value
        sigma = fh / np.sqrt(8.0 * np.log(2.0))
        amplitude = tf / (np.sqrt(2.0 * np.pi) * sigma)
        header = {
            'expr': 'em({0:g}, {1:g}, {2:g}, {3})'.format(
                x0, fh, tf, cls._internal_flux_unit)}

        return cls(modeling.models.Gaussian1D, amplitude=amplitude, mean=x0,
                   stddev=sigma, z=z, metadata=header)

    @classmethod
    def from_blackbody(cls, temperature, r=const.R_sun, d=const.kpc, z=0):
        """Create a :ref:`blackbody spectrum <synphot-planck-law>`
        with given temperature and solid angle (:math:`\\Omega`).

        .. math::

            \\Omega = \\frac{\\pi r^{2}}{d^{2}}

        Parameters
        ----------
        temperature : float or `~astropy.units.quantity.Quantity`
            Blackbody temperature. If not a Quantity, assumed to be in Kelvin.

        r : float or `~astropy.units.quantity.Quantity`
            Radius of the star. If not a Quantity, assumed to be in meter.
            Default is a solar radius.

        d : float or `~astropy.units.quantity.Quantity`
            Distance to the star. If not a Quantity, assumed to be in the
            same unit as ``r``. Default is 1 kpc.

        z : number
            Redshift to apply to model.

        Returns
        -------
        bbspec : `SourceSpectrum`
            Normalized ``BlackBody1D`` spectrum.

        """
        if not isinstance(r, u.Quantity):  # pragma: no cover
            r = u.Quantity(r, u.m)

        d = units.validate_quantity(d, r.unit)
        fac = np.pi * (r.value / d.value) ** 2  # steradian
        bbmodel = cls(BlackBody1D, temperature=temperature, z=z) * fac
        bbmodel.metadata['expr'] = 'bb({0})'.format(temperature)

        return bbmodel


class BaseUnitlessSpectrum(BaseSpectrum):
    """Base class to handle unitless spectrum like bandpass, reddening, etc."""
    _internal_flux_unit = units.THROUGHPUT

    def _process_flux_param(self, pval, wave):
        """Process individual model parameter representing throughput."""
        return self._process_generic_param(pval, self._internal_flux_unit)

    @staticmethod
    def _validate_flux_unit(new_unit):
        """Make sure flux unit is valid."""
        new_unit = units.validate_unit(new_unit)

        if new_unit.decompose() != u.dimensionless_unscaled:
            raise exceptions.SynphotError(
                'Unit {0} is not dimensionless'.format(new_unit))

        return new_unit

    def __mul__(self, other):
        """Multiply self and other."""
        if isinstance(other, (u.Quantity, numbers.Number)):
            if isinstance(other, u.Quantity):
                if other.unit.decompose() != u.dimensionless_unscaled:
                    raise exceptions.IncompatibleSources(
                        'Can only operate on dimensionless Quantity.')
                val = other.value
            else:
                val = other

            if not np.isscalar(val) or not isinstance(val, numbers.Real):
                raise exceptions.IncompatibleSources(
                    'Can only operate on real scalar number.')

            newcls = self.__class__(self.model * val)

        elif isinstance(other, BaseUnitlessSpectrum):
            newcls = self.__class__(self.model * other.model)

        elif isinstance(other, SourceSpectrum):
            newcls = other.__mul__(self)

        else:
            raise exceptions.IncompatibleSources(
                'Can only operate on scalar number/Quantity or spectrum.')

        return newcls

    def __truediv__(self, other):
        """Divide self by other (unavailable in ASTROLIB PYSYNPHOT)."""
        raise NotImplementedError('Currently unsupported.')


class SpectralElement(BaseUnitlessSpectrum):
    """Class to handle instrument filter bandpass.

    Parameters
    ----------
    modelclass, metadata, kwargs
        See `BaseSpectrum`.

    """
    def unit_response(self, area, wavelengths=None):
        """Calculate :ref:`unit response <synphot-formula-uresp>`
        of this bandpass.

        Parameters
        ----------
        area : float or `~astropy.units.quantity.Quantity`
            Area that flux covers. If not a Quantity, assumed to be in
            :math:`cm^{2}`.

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        int_val = TrapezoidIntegrator()._raw_math(x, y)
        uresp = units.HC / (a.cgs * int_val)

        return u.Quantity(uresp.value, unit=units.FLAM)

    def rmswidth(self, wavelengths=None, threshold=None):
        """Calculate the bandpass RMS width.

        As defined in
        :ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`, page 836.
        Not to be confused with :func:`photbw`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        t = TrapezoidIntegrator()
        num = t._raw_math(wave, (wave - a) ** 2 * thru)
        den = t._raw_math(wave, thru)

        if den == 0:  # pragma: no cover
            rms_width = 0.0
        else:
            val = num / den
            if val < 0:  # pragma: no cover
                rms_width = 0.0
            else:
                rms_width = np.sqrt(val)

        return u.Quantity(rms_width, self._internal_wave_unit)

    def photbw(self, wavelengths=None, threshold=None):
        """Calculate the
        :ref:`bandpass RMS width as in IRAF SYNPHOT <synphot-formula-bandw>`.

        This is a compatibility function. To calculate the actual
        bandpass RMS width, use :func:`rmswidth`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
            t = TrapezoidIntegrator()
            num = t._raw_math(wave, thru * np.log(wave / a) ** 2 / wave)
            den = t._raw_math(wave, thru / wave)

            if den == 0:  # pragma: no cover
                bandw = 0.0
            else:
                val = num / den
                if val < 0:  # pragma: no cover
                    bandw = 0.0
                else:
                    bandw = a * np.sqrt(val)

        return u.Quantity(bandw, self._internal_wave_unit)

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
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        equvw : `~astropy.units.quantity.Quantity`
            Bandpass equivalent width.

        """
        return u.Quantity(self.integrate(wavelengths=wavelengths).value,
                          self._internal_wave_unit)

    def rectwidth(self, wavelengths=None):
        """Calculate :ref:`bandpass rectangular width <synphot-formula-rectw>`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
            rectw = u.Quantity(0.0, self._internal_wave_unit)
        else:
            rectw = equvw / tpeak

        return rectw

    def efficiency(self, wavelengths=None):
        """Calculate :ref:`dimensionless efficiency <synphot-formula-qtlam>`.

        Parameters
        ----------
        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
        qtlam = TrapezoidIntegrator()._raw_math(x, y / x)
        return u.Quantity(qtlam, u.dimensionless_unscaled)

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
            Equivalent monochromatic flux in FLAM.

        """
        t_lambda = self.tlambda(wavelengths=wavelengths)

        if t_lambda == 0:  # pragma: no cover
            em_flux = u.Quantity(0.0, units.FLAM)
        else:
            uresp = self.unit_response(area, wavelengths=wavelengths)
            rectw = self.rectwidth(wavelengths=wavelengths).value
            fac = self.tpeak(wavelengths=wavelengths) / t_lambda
            em_flux = uresp * rectw * fac

        return em_flux

    def to_fits(self, filename, wavelengths=None, **kwargs):
        """Write the bandpass to a FITS file.

        Throughput column is automatically named 'THROUGHPUT'.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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

        if 'expr' in self.metadata:
            bkeys['expr'] = (self.metadata['expr'], 'synphot expression')

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
        return cls(Empirical1D, x=wavelengths, y=throughput, metadata=header)

    @classmethod
    def from_filter(cls, filtername, **kwargs):
        """Load :ref:`pre-defined filter bandpass <synphot-bandpass-create>`.

        Parameters
        ----------
        filtername : {'bessel_j', 'bessel_h', 'bessel_k', 'cousins_r', 'cousins_i', 'johnson_u', 'johnson_b', 'johnson_v', 'johnson_r', 'johnson_i', 'johnson_j', 'johnson_k'}
            Filter name.

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
        header['expr'] = filtername
        header['filename'] = filename
        header['descrip'] = cfgitem.description

        return cls(Empirical1D, x=wavelengths, y=throughput, metadata=header)
