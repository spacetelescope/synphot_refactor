# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Model and functions related to blackbody radiation.

.. note::

    This was ``astropy.modeling.blackbody`` module that was
    deprecated in ``astropy`` 4.0. The content is copied here
    so we can still use it without deprecation warning.
    Eventually, when we can fully pass in unit handling directly
    to Astropy models, we can remove this module. See
    https://github.com/astropy/astropy/pull/9282 and
    https://github.com/spacetelescope/synphot_refactor/pull/224 .

"""
import warnings

import numpy as np

from astropy import constants as const
from astropy import units as u
from astropy.modeling.core import Fittable1DModel
from astropy.modeling.parameters import Parameter
from astropy.utils.exceptions import AstropyUserWarning

from synphot.units import FNU, FLAM

__all__ = ['BlackBody1D', 'blackbody_nu', 'blackbody_lambda']

with warnings.catch_warnings():
    warnings.simplefilter('ignore', RuntimeWarning)
    _has_buggy_expm1 = np.isnan(np.expm1(1000)) or np.isnan(np.expm1(1e10))


class BlackBody1D(Fittable1DModel):
    """
    One dimensional blackbody model.

    Parameters
    ----------
    temperature : :class:`~astropy.units.Quantity`
        Blackbody temperature.
    bolometric_flux : :class:`~astropy.units.Quantity`
        The bolometric flux of the blackbody (i.e., the integral over the
        spectral axis).

    Notes
    -----

    Model formula:

        .. math:: f(x) = \\pi B_{\\nu} f_{\\text{bolometric}} / (\\sigma  T^{4})

    Examples
    --------
    >>> from astropy import units as u
    >>> from synphot.blackbody import BlackBody1D
    >>> bb = BlackBody1D()
    >>> bb(6000 * u.AA)  # doctest: +FLOAT_CMP
    <Quantity 1.35853828e-15 erg / (Hz s cm2)>

    .. plot::
        :include-source:

        import numpy as np
        import matplotlib.pyplot as plt
        from astropy import units as u
        from astropy.visualization import quantity_support
        from synphot.blackbody import BlackBody1D
        from synphot.units import FLAM

        bb = BlackBody1D(temperature=5778*u.K)
        wav = np.arange(1000, 110000) * u.AA
        flux = bb(wav).to(FLAM, u.spectral_density(wav))

        with quantity_support():
            plt.figure()
            plt.semilogx(wav, flux)
            plt.axvline(bb.lambda_max.to_value(u.AA), ls='--')
            plt.show()

    """  # noqa

    # We parametrize this model with a temperature and a bolometric flux. The
    # bolometric flux is the integral of the model over the spectral axis. This
    # is more useful than simply having an amplitude parameter.
    temperature = Parameter(default=5000, min=0, unit=u.K)
    bolometric_flux = Parameter(default=1, min=0, unit=u.erg / u.cm ** 2 / u.s)

    # We allow values without units to be passed when evaluating the model, and
    # in this case the input x values are assumed to be frequencies in Hz.
    _input_units_allow_dimensionless = True

    # We enable the spectral equivalency by default for the spectral axis
    input_units_equivalencies = {'x': u.spectral()}

    def evaluate(self, x, temperature, bolometric_flux):
        """Evaluate the model.

        Parameters
        ----------
        x : float, `~numpy.ndarray`, or `~astropy.units.Quantity`
            Frequency at which to compute the blackbody. If no units are given,
            this defaults to Hz.

        temperature : float, `~numpy.ndarray`, or `~astropy.units.Quantity`
            Temperature of the blackbody. If no units are given, this defaults
            to Kelvin.

        bolometric_flux : float, `~numpy.ndarray`, or `~astropy.units.Quantity`
            Desired integral for the blackbody.

        Returns
        -------
        y : number or ndarray
            Blackbody spectrum. The units are determined from the units of
            ``bolometric_flux``.
        """

        # We need to make sure that we attach units to the temperature if it
        # doesn't have any units. We do this because even though blackbody_nu
        # can take temperature values without units, the / temperature ** 4
        # factor needs units to be defined.
        if isinstance(temperature, u.Quantity):
            temperature = temperature.to(u.K, equivalencies=u.temperature())
        else:
            temperature = u.Quantity(temperature, u.K)

        # We normalize the returned blackbody so that the integral would be
        # unity, and we then multiply by the bolometric flux. A normalized
        # blackbody has f_nu = pi * B_nu / (sigma * T^4), which is what we
        # calculate here. We convert to 1/Hz to make sure the units are
        # simplified as much as possible, then we multiply by the bolometric
        # flux to get the normalization right.
        fnu = ((np.pi * u.sr * blackbody_nu(x, temperature) /
                const.sigma_sb / temperature ** 4).to(1 / u.Hz) *
               bolometric_flux)

        # If the bolometric_flux parameter has no unit, we should drop the /Hz
        # and return a unitless value. This occurs for instance during fitting,
        # since we drop the units temporarily.
        if hasattr(bolometric_flux, 'unit'):
            return fnu
        else:
            return fnu.value

    @property
    def input_units(self):
        # The input units are those of the 'x' value, which should always be
        # Hz. Because we do this, and because input_units_allow_dimensionless
        # is set to True, dimensionless values are assumed to be in Hz.
        return {'x': u.Hz}

    def _parameter_units_for_data_units(self, inputs_unit, outputs_unit):
        return {'temperature': u.K,
                'bolometric_flux': outputs_unit['y'] * u.Hz}

    @property
    def lambda_max(self):
        """Peak wavelength when the curve is expressed as power density."""
        return const.b_wien / self.temperature


def blackbody_nu(in_x, temperature):
    """Calculate blackbody flux per steradian, :math:`B_{\\nu}(T)`.

    .. note::

        Use `numpy.errstate` to suppress Numpy warnings, if desired.

    .. warning::

        Output values might contain ``nan`` and ``inf``.

    Parameters
    ----------
    in_x : number, array_like, or `~astropy.units.Quantity`
        Frequency, wavelength, or wave number.
        If not a Quantity, it is assumed to be in Hz.

    temperature : number, array_like, or `~astropy.units.Quantity`
        Blackbody temperature.
        If not a Quantity, it is assumed to be in Kelvin.

    Returns
    -------
    flux : `~astropy.units.Quantity`
        Blackbody monochromatic flux in
        :math:`erg \\; cm^{-2} s^{-1} Hz^{-1} sr^{-1}`.

    Raises
    ------
    ValueError
        Invalid temperature.

    ZeroDivisionError
        Wavelength is zero (when converting to frequency).

    """
    # Convert to units for calculations, also force double precision
    with u.add_enabled_equivalencies(u.spectral() + u.temperature()):
        freq = u.Quantity(in_x, u.Hz, dtype=np.float64)
        temp = u.Quantity(temperature, u.K, dtype=np.float64)

    # Check if input values are physically possible
    if np.any(temp < 0):
        raise ValueError(f'Temperature should be positive: {temp}')
    if not np.all(np.isfinite(freq)) or np.any(freq <= 0):
        warnings.warn('Input contains invalid wavelength/frequency value(s)',
                      AstropyUserWarning)

    log_boltz = const.h * freq / (const.k_B * temp)
    boltzm1 = np.expm1(log_boltz)

    if _has_buggy_expm1:
        # Replace incorrect nan results with infs--any result of 'nan' is
        # incorrect unless the input (in log_boltz) happened to be nan to begin
        # with.  (As noted in #4393 ideally this would be replaced by a version
        # of expm1 that doesn't have this bug, rather than fixing incorrect
        # results after the fact...)
        boltzm1_nans = np.isnan(boltzm1)
        if np.any(boltzm1_nans):
            if boltzm1.isscalar and not np.isnan(log_boltz):
                boltzm1 = np.inf
            else:
                boltzm1[np.where(~np.isnan(log_boltz) & boltzm1_nans)] = np.inf

    # Calculate blackbody flux
    bb_nu = (2.0 * const.h * freq ** 3 / (const.c ** 2 * boltzm1))
    flux = bb_nu.to(FNU, u.spectral_density(freq))

    return flux / u.sr  # Add per steradian to output flux unit


def blackbody_lambda(in_x, temperature):
    """Like :func:`blackbody_nu` but for :math:`B_{\\lambda}(T)`.

    Parameters
    ----------
    in_x : number, array_like, or `~astropy.units.Quantity`
        Frequency, wavelength, or wave number.
        If not a Quantity, it is assumed to be in Angstrom.

    temperature : number, array_like, or `~astropy.units.Quantity`
        Blackbody temperature.
        If not a Quantity, it is assumed to be in Kelvin.

    Returns
    -------
    flux : `~astropy.units.Quantity`
        Blackbody monochromatic flux in
        :math:`erg \\; cm^{-2} s^{-1} \\mathring{A}^{-1} sr^{-1}`.

    """
    if getattr(in_x, 'unit', None) is None:
        in_x = u.Quantity(in_x, u.AA)

    bb_nu = blackbody_nu(in_x, temperature) * u.sr  # Remove sr for conversion
    flux = bb_nu.to(FLAM, u.spectral_density(in_x))

    return flux / u.sr  # Add per steradian to output flux unit
