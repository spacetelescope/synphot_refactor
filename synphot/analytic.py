# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines the analytic spectrum classes for source spectrum
or passband.

"""
from __future__ import division, print_function

# STDLIB
import abc

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import constants as const
from astropy import modeling
from astropy import units as u
from astropy.extern import six

# LOCAL
from . import exceptions, planck, spectrum, units, utils


__all__ = ['BaseMixinAnalytic', 'MixinAnalyticPassband',
           'MixinAnalyticFlamSource', 'MixinAnalyticSource',
           'BlackBody1D', 'class_factory', 'Box1DSpectrum',
           'Const1DSpectrum', 'Gaussian1DSpectrum', 'PowerLaw1DSpectrum',
           'BlackBody1DSpectrum', 'flat_spectrum', 'gaussian_spectrum']


@six.add_metaclass(abc.ABCMeta)
class BaseMixinAnalytic(object):
    """Abstract base mixin class to handle analytic spectrum or passband.
    Do not use directly.

    .. note::

        Math operators will be inherited from `astropy.modeling`
        for use to create composite model.

    Parameters
    ----------
    args : tuple
        Arguments for modeling, not used here.

    kwargs : dict
        Keywords for modeling, except:
            * ``flux_unit``
            * ``wave_unit``
            * ``area``

    """
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Subclasses should implement this.')

    @property
    def flux_unit(self):
        """Flux/throughput unit of the spectrum/passband."""
        return self._flux_unit

    @property
    def wave_unit(self):
        """Wavelength unit of the spectrum/passband."""
        return self._wave_unit

    def _set_wave_unit(self, new_unit):
        """Set the wavelength unit once in init.

        When `astropy.modeling` support Quantity, this can be a
        property setter.

        """
        wave = u.Quantity(1.0, unit=new_unit)
        utils.validate_wavelengths(wave)
        self._wave_unit = new_unit

    @property
    def primary_area(self):
        """Area that flux/throughput covers in cm^2. Can be `None`."""
        return self._primary_area

    @primary_area.setter
    def primary_area(self, area):
        """Change the area attribute.

        No check is done until :func:`to_spectrum` is called.

        Parameters
        ----------
        area : `None`, float, or `astropy.units.quantity.Quantity`
            New area.

        """
        self._primary_area = area

    def sample(self, wavelengths):
        """Sample flux or throughput to match the given wavelengths.

        Given wavelengths are converted to ``self.wave_unit`` and
        must satisfy :func:`synphot.utils.validate_wavelengths`.

        Parameters
        ----------
        wavelengths : array_like or `astropy.units.quantity.Quantity`
            Wavelength values for sampling. If not a Quantity,
            assumed to be in ``self.wave_unit``.

        Returns
        -------
        sampled_result : `astropy.units.quantity.Quantity`
            Sampled flux or throughput that is in-sync with
            given wavelengths. Might have negative values.

        """
        if not isinstance(wavelengths, u.Quantity):
            wavelengths = u.Quantity(wavelengths, unit=self.wave_unit)
        else:
            wavelengths = wavelengths.to(
                self.wave_unit, equivalencies=u.spectral())

        utils.validate_wavelengths(wavelengths)
        resampled_result = self(wavelengths.value)
        return u.Quantity(resampled_result, unit=self.flux_unit)

    def _get_expr(self, i_pset=0):
        """A hack on :func:`astropy.modeling.core.Model.__repr__`
        to return string for individual parameter set for use
        by :func:`to_spectrum`.

        Only works when param_dim > 1. For single param set, use
        regular :func:`repr`.

        Parameters
        ----------
        i_pset : int
            Parameter set index.

        Returns
        -------
        expr : str

        """
        n_par = len(self.param_names)
        fmt = '{0}('.format(self.__class__.__name__)
        for i in xrange(n_par):
            fmt += '{0}={1}'.format(
                self.param_names[i], getattr(self, self.param_names[i])[i_pset])
            if i < n_par - 1:
                fmt += ','
        fmt += ')'
        return fmt

    def to_spectrum(self, wavelengths):
        """Generate spectrum object(s).

        `astropy.modeling` supports defining a single model with
        multiple parameter sets. As a result, the number of spectrum
        object(s) returned will be equal to the ``param_dim`` attribute
        of the model.

        Parameters
        ----------
        wavelengths
            See :func:`sample`.

        Returns
        -------
        newspec : `~synphot.spectrum.SourceSpectrum` or `~synphot.spectrum.SpectralElement` or tuple
            Sampled spectrum/spectra from analytic model.

        """
        flux = self.sample(wavelengths)

        if self.param_dim > 1:
            flux = flux.T
            specs = tuple(
                [self._spec_cls(wavelengths, flux[i], area=self.primary_area,
                                header={'expr': self._get_expr(i_pset=i)})
                 for i in xrange(self.param_dim)])
        else:
            specs = self._spec_cls(
                wavelengths, flux, area=self.primary_area,
                header={'expr': repr(self)})

        return specs


class MixinAnalyticPassband(BaseMixinAnalytic):
    """Mixin class to handle analytic passband.
    Do not use directly.

    Ignores following keyword:

        * ``flux_unit`` - Set to THROUGHPUT.

    Uses following keyword:

        * ``wave_unit`` - Defaults to Angstrom.
        * ``area`` - Defaults to `None`.

    """
    def __init__(self, *args, **kwargs):
        self._spec_cls = spectrum.SpectralElement
        self._flux_unit = units.THROUGHPUT
        self._set_wave_unit(kwargs.get('wave_unit', u.AA))
        self.primary_area = kwargs.get('area', None)


class MixinAnalyticFlamSource(BaseMixinAnalytic):
    """Like `MixinAnalyticPassband` but for source spectrum
    with fixed flux unit set to FLAM.

    """
    def __init__(self, *args, **kwargs):
        self._spec_cls = spectrum.SourceSpectrum
        self._flux_unit = units.FLAM
        self._set_wave_unit(kwargs.get('wave_unit', u.AA))
        self.primary_area = kwargs.get('area', None)


class MixinAnalyticSource(BaseMixinAnalytic):
    """Mixin class to handle analytic source spectrum.
    Do not use directly.

    Uses following keywords:

        * ``flux_unit`` - Defaults to FLAM.
        * ``wave_unit`` - Defaults to Angstrom.
        * ``area`` - Defaults to `None`.

    """
    def __init__(self, *args, **kwargs):
        self._spec_cls = spectrum.SourceSpectrum
        self.flux_unit = kwargs.get('flux_unit', units.FLAM)
        self._set_wave_unit(kwargs.get('wave_unit', u.AA))
        self.primary_area = kwargs.get('area', None)

    # Need to put this here so setter will work
    @property
    def flux_unit(self):
        """Flux unit of the spectrum."""
        return self._flux_unit

    @flux_unit.setter
    def flux_unit(self, new_unit):
        """Change the flux unit attribute.

        Does not change computed flux values, just the unit.

        Parameters
        ----------
        new_unit : str or `astropy.units.core.Unit`
            New flux unit.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid unit.

        """
        self._spec_cls._validate_flux_unit(new_unit)
        self._flux_unit = new_unit


class BlackBody1D(modeling.Parametric1DModel):
    """Create a :ref:`blackbody spectrum <synphot-planck-law>`
    model with given temperature.

    Parameters
    ----------
    temperature : float
        Blackbody temperature in Kelvin.

    """
    temperature = modeling.Parameter('temperature')

    def __init__(self, temperature, **constraints):
        super(BlackBody1D, self).__init__(
            temperature=temperature, **constraints)

    def eval(self, x, temperature):
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
            Blackbody radiation in FLAM.

        """
        wave = u.Quantity(np.ascontiguousarray(x), unit=u.AA)
        t = u.Quantity(temperature, unit=u.K)
        bbflux = planck.bb_photlam(wave, t)
        fluxes = bbflux.to(units.FLAM, equivalencies=u.spectral_density(wave))
        return fluxes.value

    def deriv(self, x, temperature):
        raise NotImplementedError(
            'deriv undefined for {0}.'.format(self.__class__.__name__))


def class_factory(mixinclass, modelclass):
    """Generate new analytic spectrum class for a given mixin
    and model classes.

    The class inherits from both the given mixin and model,
    with priority given to the former. For usage of model methods,
    see `astropy.modeling`.

    Only 1D or composite models are allowed.

    Parameters
    ----------
    mixinclass : `MixinAnalyticPassband`, `MixinAnalyticFlamSource` or `MixinAnalyticSource`
        Mixin analytic class.

    modelclass : obj
        Model class from `astropy.modeling`.

    Returns
    -------
    newcls : cls
        Analytic spectrum class.

    Raises
    ------
    synphot.exceptions.SynphotError
        Invalid input class.

    """
    modelname = modelclass.__name__

    if (not issubclass(modelclass, modeling.Model) or
            ('Composite' not in modelname and '1D' not in modelname)):
        raise exceptions.SynphotError(
            '{0} is not supported'.format(modelname))

    if issubclass(mixinclass, MixinAnalyticPassband):
        sp_str = 'passband'
    elif issubclass(mixinclass, BaseMixinAnalytic):
        sp_str = 'source spectrum'
    else:
        raise exceptions.SynphotError(
            '{0} is not supported'.format(mixinclass.__name__))

    class cls(mixinclass, modelclass):
        def __init__(self, *args, **kwargs):
            mixinclass.__init__(self, *args, **kwargs)

            # These are not used by astropy.modeling
            for key in ('flux_unit', 'wave_unit', 'area'):
                if key in kwargs:
                    del kwargs[key]

            #---------------------------------------------------------------
            # Explicitly set param_dim, except for Gaussian1D.
            # Not needed after astropy#1680 merged but not deleted in case
            # it is needed again in a future modeling API change.
            #---------------------------------------------------------------
            #if 'Gaussian1D' not in modelname and 'param_dim' not in kwargs:
            #    a = args[0]
            #    if np.isscalar(a):
            #        n = 1
            #    else:
            #        n = len(a)
            #    kwargs.update({'param_dim': n})
            #---------------------------------------------------------------

            modelclass.__init__(self, *args, **kwargs)

    cls.__name__ = modelname + 'Spectrum'
    cls.__doc__ = 'Class to handle analytic {0} using {1}.'.format(
        sp_str, modelname)

    return cls


# Generate analytic passband with modeling behavior
Box1DSpectrum = class_factory(MixinAnalyticPassband, modeling.models.Box1D)
Box1DSpectrum.__doc__ += 'See :ref:`box-shaped passband <synphot-box-passband>`.'

# Generate analytic source spectrum with modeling behavior
BlackBody1DSpectrum = class_factory(MixinAnalyticFlamSource, BlackBody1D)
BlackBody1DSpectrum.__doc__ += 'See :ref:`blackbody spectrum <synphot-planck-law>`.'
Const1DSpectrum = class_factory(MixinAnalyticSource, modeling.models.Const1D)
Const1DSpectrum.__doc__ += 'Also see :func:`flat_spectrum`.'
Gaussian1DSpectrum = class_factory(
    MixinAnalyticSource, modeling.models.Gaussian1D)
Gaussian1DSpectrum.__doc__ += 'Also see :func:`gaussian_spectrum`.'
PowerLaw1DSpectrum = class_factory(
    MixinAnalyticSource, modeling.models.PowerLaw1D)
PowerLaw1DSpectrum.__doc__ += 'See :ref:`power-law spectrum <synphot-powerlaw>`.'

#-----------------------------------------------------------------------------#
# Generate analytic composite source spectrum with modeling behavior.         #
#                                                                             #
# These are not exactly what synphot wants. They do x + model1(x) + model2(x) #
# and not model1(x) + model2(x). Nadia will implement something else.         #
#-----------------------------------------------------------------------------#
#SummedCompositeSpectrum = class_factory(MixinAnalyticSource, modeling.SummedCompositeModel)
#SerialCompositeSpectrum = class_factory(MixinAnalyticSource, modeling.SerialCompositeModel)


def flat_spectrum(flux_unit, wave_unit=u.AA, area=None):
    """Generate an instance of `Const1DSpectrum` with value
    determined from given flux unit. See
    :ref:`flat spectrum <synphot-flat-spec>`.

    Parameters
    ----------
    flux_unit : str or `astropy.units.core.Unit`
        Flux unit of flat spectrum.

    wave_unit : str or `astropy.units.core.Unit`, optional
        Wavelength unit of flat spectrum. Default is Angstrom.

    area : float or `astropy.units.quantity.Quantity`, optional
        Area that fluxes cover. Usually, this is the area of
        the primary mirror of the observatory of interest.
        If not a Quantity, assumed to be in cm^2.

    Returns
    -------
    flatspec : `Const1DSpectrum`
        Flat spectrum in given flux unit.

    Raises
    ------
    synphot.exceptions.SynphotError
        Flat spectrum is not defined for given flux unit.

    """
    flux_unit = units.validate_unit(flux_unit)
    flux_unit_name = flux_unit.to_string()

    # Magnitude flux-density units
    if flux_unit_name == units.STMAG.to_string():
        x = units.convert_flux(1, u.Quantity(0, units.STMAG), units.FLAM)

    elif flux_unit_name == units.ABMAG.to_string():
        x = units.convert_flux(1, u.Quantity(0, units.ABMAG), units.FNU)

    # Linear flux-density units
    elif (flux_unit.physical_type == 'spectral flux density' or
          flux_unit_name in (
            units.PHOTLAM.to_string(), units.PHOTNU.to_string(),
            units.FLAM.to_string())):
        x = u.Quantity(1.0, unit=flux_unit)

    else:
        raise exceptions.SynphotError(
            'No standard spectrum available for {0}'.format(flux_unit_name))

    return Const1DSpectrum(
        x.value, flux_unit=x.unit, wave_unit=wave_unit, area=area)


def gaussian_spectrum(total_flux, center, fwhm, area=None):
    """Generate an instance of `Gaussian1DSpectrum` using
    parameters from a :ref:`Gaussian source <synphot-gaussian>`.

    If central wavelength is given in frequency or wave number,
    it is converted to wavelength using :func:`synphot.utils.to_length`.
    FWHM is then converted to the final unit of central wavelength.

    Parameters
    ----------
    total_flux : float or `astropy.units.quantity.Quantity`
        Total flux under gaussian. If not a Quantity, assumed
        to be in FLAM.

    center : float or `astropy.units.quantity.Quantity`
        Central wavelength of gaussian.
        If not a Quantity, assumed to be in Angstrom.

    fwhm : float or `astropy.units.quantity.Quantity`
        Full-width-at-half-maximum (FWHM) of gaussian.
        If not a Quantity, assumed to be in the same unit
        as ``center``.

    area : float or `astropy.units.quantity.Quantity`, optional
        Area that fluxes cover. Usually, this is the area of
        the primary mirror of the observatory of interest.
        If not a Quantity, assumed to be in cm^2.

    Returns
    -------
    gspec : `Gaussian1DSpectrum`
        Spectrum from Gaussian source.

    """
    if not isinstance(total_flux, u.Quantity):
        total_flux = u.Quantity(total_flux, unit=units.FLAM)

    if not isinstance(center, u.Quantity):
        center = u.Quantity(center, unit=u.AA)

    if not isinstance(fwhm, u.Quantity):
        fwhm = u.Quantity(fwhm, unit=center.unit)

    center = utils.to_length(center)  # Convert to length
    fwhm = fwhm.to(center.unit, equivalencies=u.spectral())
    sigma = fwhm.value / np.sqrt(8.0 * np.log(2.0))
    factor = total_flux.value / (np.sqrt(2.0 * np.pi) * sigma)

    return Gaussian1DSpectrum(
        factor, center.value, sigma, flux_unit=total_flux.unit,
        wave_unit=center.unit, area=area)
