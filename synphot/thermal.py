# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines thermal spectra."""
from __future__ import absolute_import, division, print_function

# ASTROPY
from astropy import units as u
from astropy.io import fits

# LOCAL
from . import exceptions, specio, units
from .models import BlackBody1D, Empirical1D
from .spectrum import BaseUnitlessSpectrum, SourceSpectrum

__all__ = ['ThermalSpectralElement']


class ThermalSpectralElement(BaseUnitlessSpectrum):
    """Class to handle spectral element with associated thermal
    properties.

    This differs from `~synphot.spectrum.SpectralElement` in the
    sense that it carries thermal parameters, i.e., temperature
    and beam filling factor.

    .. note::

        Use :func:`thermal_source` to apply its emissivity to an
        existing beam.

    Parameters
    ----------
    modelclass, kwargs
        See `~synphot.spectrum.BaseSpectrum`.

    temperature : float or `~astropy.units.quantity.Quantity`
        Temperature. If not a Quantity, assumed to be in Kelvin.

    beam_fill_factor : float or `~astropy.units.quantity.Quantity`
        Beam filling factor. If a Quantity, must be unitless.
        Defaults to 1.

    """
    def __init__(self, modelclass, temperature, beam_fill_factor=1, **kwargs):
        super(ThermalSpectralElement, self).__init__(modelclass, **kwargs)
        self.temperature = temperature
        self.beam_fill_factor = beam_fill_factor

    @property
    def temperature(self):
        """Temperature."""
        return self._temperature

    @temperature.setter
    def temperature(self, what):
        """Set temperature."""
        self._temperature = units.validate_quantity(what, u.K)

    @property
    def beam_fill_factor(self):
        """Beam filling factor."""
        return self._beam_fill_factor

    @beam_fill_factor.setter
    def beam_fill_factor(self, what):
        """Set beam filling factor."""
        self._beam_fill_factor = units.validate_quantity(what, '').value

    def taper(self, **kwargs):
        """Tapering is disabled."""
        raise NotImplementedError(
            'Thermal spectral element cannot be tapered.')

    def thermal_source(self):
        """Apply emissivity to an existing beam to produce a thermal
        source spectrum (without optical counterpart).

        Thermal source spectrum is calculated as follow:

            #. Create a blackbody spectrum in PHOTLAM per square arcsec
               with `temperature`.
            #. Multiply the blackbody with `beam_fill_factor` and ``self``.

        Returns
        -------
        sp : `~synphot.spectrum.SourceSpectrum`
            Thermal source spectrum.

        """
        sp = (SourceSpectrum(BlackBody1D, temperature=self.temperature) *
              units.SR_PER_ARCSEC2 * self.beam_fill_factor * self)
        sp.meta['temperature'] = self.temperature
        sp.meta['beam_fill_factor'] = self.beam_fill_factor
        return sp

    @classmethod
    def from_file(cls, filename, temperature_key='DEFT',
                  beamfill_key='BEAMFILL', **kwargs):
        """Creates a thermal spectral element from file.

        .. note::

            Only FITS format is supported.

        Parameters
        ----------
        filename : str
            Thermal spectral element filename.

        temperature_key, beamfill_key : str
            Keywords in FITS *table extension* that store temperature
            (in Kelvin) and beam filling factor values.
            Beam filling factor is set to 1 if its keyword is missing.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.specio.read_fits_spec`.

        Returns
        -------
        th : `ThermalSpectralElement`
            Empirical thermal spectral element.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        if not (filename.endswith('fits') or filename.endswith('fit')):
            raise exceptions.SynphotError('Only FITS format is supported.')

        # Extra info from table header
        ext = kwargs.get('ext', 1)
        tab_hdr = fits.getheader(filename, ext=ext)

        temperature = tab_hdr.get(temperature_key)
        if temperature is None:
            raise exceptions.SynphotError(
                'Missing {0} keyword.'.format(temperature_key))

        beam_fill_factor = tab_hdr.get('BEAMFILL', 1)

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = cls._internal_flux_unit

        if 'flux_col' not in kwargs:
            kwargs['flux_col'] = 'EMISSIVITY'

        header, wavelengths, em = specio.read_spec(filename, **kwargs)
        return cls(
            Empirical1D, temperature, beam_fill_factor=beam_fill_factor,
            points=wavelengths, lookup_table=em, meta={'header': header})
