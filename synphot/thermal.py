# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module contains thermal spectrum functionalities."""
from __future__ import absolute_import, division, print_function, unicode_literals

# ASTROPY
from astropy import units as u
from astropy.io import fits

# LOCAL
from . import exceptions, planck, specio, spectrum, units


__all__ = ['ThermalSpectralElement']


class ThermalSpectralElement(spectrum.BaseUnitlessSpectrum):
    """Class to handle spectral element with associated thermal
    properties.

    This differs from `~synphot.spectrum.SpectralElements` in the
    sense that it carries thermal parameters such as temperature
    and beam filling factor.

    .. note::

        Use :func:`to_thermal_source` to apply its emissivity to an
        existing beam.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Values for the unitless component (hereafter, known as emissivity)
    must be dimensionless. They are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    emissivity : array_like or `astropy.units.quantity.Quantity`
        Emissivity values. Must be dimensionless.
        If not a Quantity, assumed to be in THROUGHPUT.

    temperature : float or `astropy.units.quantity.Quantity`
        Temperature. If not a Quantity, assumed to be in Kelvin.

    beam_fill_factor : float
        Beam filling factor.

    kwargs : dict
        Keywords accepted by `~synphot.spectrum.BaseSpectrum`,
        except ``flux_unit``.

    Attributes
    ----------
    wave, thru : `astropy.units.quantity.Quantity`
        Wavelength and emissivity of the spectrum.

    temperature : `astropy.units.quantity.Quantity`
        Temperature.

    beam_fill_factor : float
        Beam filling factor.

    primary_area : `astropy.units.quantity.Quantity` or `None`
        Area that flux covers in cm^2.

    metadata : dict
        Metadata. ``self.metadata['expr']`` must contain a descriptive string of the object.

    warnings : dict
        List of warnings related to spectrum object.

    Raises
    ------
    synphot.exceptions.SynphotError
        If wavelengths and emissivity do not match, or if they have
        invalid units.

    synphot.exceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    def __init__(self, wavelengths, emissivity, temperature, beam_fill_factor,
                 **kwargs):
        super(ThermalSpectralElement, self).__init__(
            wavelengths, emissivity, **kwargs)
        self.temperature = units.validate_quantity(temperature, u.K)
        self.beam_fill_factor = float(beam_fill_factor)

    def to_thermal_source(self, wavelengths=None):
        """Apply emissivity to an existing beam to produce a thermal
        source spectrum (without optical counterpart).

        Thermal source spectrum is calculated as follow:

            #. Create a blackbody spectrum in
               :math:`\\textnormal{PHOTLAM} \\textnormal{arcsec^{-2}}`
               with ``self.temperature`` using
               :func:`synphot.planck.bb_photlam_arcsec`.
            #. Multiply the blackbody with ``self.beam_fill_factor``
               and ``self.thru``.

        Parameters
        ----------
        wavelengths : array_like or `astropy.units.quantity.Quantity`, optional
            Wavelength values. If not a Quantity, assumed to be in
            Angstrom. If `None`, ``self.wave`` is used.

        Returns
        -------
        sp : `~synphot.spectrum.SourceSpectrum`
            Thermal source spectrum in PHOTLAM.

        """
        if wavelengths is None:
            wavelengths = self.wave

        bbflux = planck.bb_photlam_arcsec(wavelengths, self.temperature)
        sp_bb = spectrum.SourceSpectrum(
            wavelengths, bbflux.value, flux_unit=units.PHOTLAM,
            area=self.primary_area)

        sp = sp_bb * self.beam_fill_factor * self

        # Clear confusing metadata
        for k in list(sp.metadata.keys()):
            if k != 'expr':
                del sp.metadata[k]

        # Add new metadata
        sp.metadata['temperature'] = self.temperature
        sp.metadata['beam_fill_factor'] = self.beam_fill_factor

        return sp

    @classmethod
    def from_file(cls, filename, temperature_key='DEFT',
                  beamfill_key='BEAMFILL', area=None, **kwargs):
        """Creates a thermal spectrum object from FITS file.

        Parameters
        ----------
        filename : str
            Thermal spectrum filename.

        temperature_key, beamfill_key : str
            Keywords in FITS *table extension* that store temperature
            (in Kelvin) and beam filling factor values.
            Beam filling factor is set to 1 if its keyword is missing.

        area : float or `astropy.units.quantity.Quantity`, optional
            Telescope collecting area.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by :func:`synphot.stio.read_fits_spec`.

        Returns
        -------
        newspec : obj
            New thermal spectrum object.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid file format or missing keyword.

        """
        if not (filename.endswith('fits') or filename.endswith('fit')):
            raise exceptions.SynphotError('Only FITS is supported.')

        # Extra info from table header
        ext = kwargs.get('ext', 1)
        tab_hdr = fits.getheader(filename, ext=ext)

        temperature = tab_hdr.get(temperature_key)
        if temperature is None:
            raise exceptions.SynphotError(
                'Missing {0} keyword.'.format(temperature_key))

        beam_fill_factor = tab_hdr.get('BEAMFILL', 1.0)

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = units.THROUGHPUT

        if 'flux_col' not in kwargs:
            kwargs['flux_col'] = 'EMISSIVITY'

        header, wavelengths, fluxes = specio.read_spec(filename, **kwargs)
        return cls(wavelengths, fluxes, temperature, beam_fill_factor,
                   area=area, header=header)

    def plot(self, **kwargs):  # pragma: no cover
        """Plot the emissivity.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        kwargs : dict
            Keywords accepted by :func:`synphot.spectrum.BaseSpectrum.plot`,
            *except* ``ylabel``.

        """
        if 'ylabel' in kwargs:
            del kwargs[key]

        super(ThermalSpectralElement, self).plot(ylabel='Emissivity', **kwargs)
