# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines an observed spectrum, i.e., a source spectrum
that has gone through a passband.

"""
from __future__ import division, print_function

# STDLIB
from copy import deepcopy

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import log
from astropy import units as u

# LOCAL
from . import binning, spectrum, exceptions, io, utils, units


__all__ = ['Observation']


class Observation(spectrum.SourceSpectrum):
    """This is an observed spectrum, where a source spectrum
    has gone through a passband.

    While it mostly inherits from `~synphot.spectrum.SourceSpectrum`,
    it has additional methods and attributes. It also disables some
    existing methods from parent class. This is such that its
    behavior is consistent with an observed spectrum that it
    represents.

    Most notably, this class has extra attributes that deal
    with binning, which is introduced by the detector.

    Usually, this is the end point of a chain of spectral
    manipulation.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    fluxes : array_like or `astropy.units.quantity.Quantity`
        Flux values. If not a Quantity, assumed to be in FLAM.

    binwave : `None`, array_like, or `astropy.units.quantity.Quantity`
        Center of binned wavelengths. If not a Quantity, assumed
        to have the same unit as ``wavelengths``.
        If `None`, not binned data is stored.

    kwargs : dict
        Keywords accepted by `~synphot.spectrum.BaseSpectrum`.

    Attributes
    ----------
    wave, flux : `astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

    binwave : `None` or `astropy.units.quantity.Quantity`
        Center of binned wavelengths.

    binflux : `None` or `astropy.units.quantity.Quantity`
        Binned flux corresponding to ``self.binwave``.

    bin_edges : `None` or `astropy.units.quantity.Quantity`
        Edges of the binned wavelengths.

    primary_area : `astropy.units.quantity.Quantity` or `None`
        Area that flux covers in cm^2.

    metadata : dict
        Metadata. ``self.metadata['expr']`` must contain a descriptive string of the object.

    warnings : dict
        Dictionary of warning key-value pairs related to spectrum object.

    Raises
    ------
    synphot.exceptions.SynphotError
        If wavelengths and fluxes do not match, or if they have invalid units.

    synphot.exceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    def __init__(self, wavelengths, fluxes, binwave=None, **kwargs):
        spectrum.SourceSpectrum.__init__(self, wavelengths, fluxes, **kwargs)

        if binwave is None:
            self.binwave = None
            self.binflux = None
            self.bin_edges = None
        else:
            self.binspec(binwave)

        # This is set internally before calculations, as needed
        self._set_data(False)

    def binspec(self, binwave):
        """Set binning attributes based on given binned wavelength
        centers.

        By contrast, the native wave and flux should be considered
        samples of a continuous function.

        Thus, it makes sense to interpolate ``self.wave`` and
        ``self.flux``, but not ``self.binwave`` and ``self.binflux``.

        Parameters
        ----------
        binwave : array_like or `astropy.units.quantity.Quantity`
            Center of binned wavelengths. If not a Quantity, assumed
            to have the same unit as ``self.wave``.

        """
        # Convert binwave to native wavelength unit and validate.
        self.binwave = units.validate_quantity(
            binwave, self.wave.unit, equivalencies=units.wave_conversion)
        utils.validate_wavelengths(self.binwave)

        # binwave must be in ascending order for calcbinflux()
        # to work properly.
        if self.binwave[0] > self.binwave[-1]:
            self.binwave = u.Quantity(
                self.binwave.value[::-1], unit=self.binwave.unit)

        self.bin_edges = binning.calculate_bin_edges(self.binwave)

        # Merge bin edges and centers in with the natural waveset
        spwave = utils.merge_wavelengths(utils.merge_wavelengths(
                self.wave.value, self.bin_edges.value), self.binwave.value)

        # Compute indices associated to each endpoint.
        indices = np.searchsorted(spwave, self.bin_edges.value)
        i_beg = indices[:-1]
        i_end = indices[1:]

        # Prepare integration variables.
        flux = self.resample(spwave)
        avflux = (flux.value[1:] + flux.value[:-1]) * 0.5
        deltaw = spwave[1:] - spwave[:-1]

        # Sum over each bin.
        binflux, intwave = binning.calcbinflux(
            self.binwave.size, i_beg, i_end, avflux, deltaw)

        self.binflux = u.Quantity(binflux, unit=self.flux.unit)

    def _set_data(self, binned):
        """Set the data for calculations, either native or binned."""
        if binned:
            if (self.binwave is None or self.binflux is None or
                    self.bin_edges is None):
                raise exceptions.UndefinedBinset('No binned data.')
            self._wave = self.binwave
            self._flux = self.binflux
        else:
            self._wave = self.wave
            self._flux = self.flux

    def __add__(self, other):
        raise NotImplementedError('Observations cannot be added.')

    def __sub__(self, other):
        raise NotImplementedError('Observations cannot be subtracted.')

    def __mul__(self, other):
        """Extends base class mul to handle binned data."""
        new_obs = spectrum.BaseSpectrum.__mul__(self, other)
        new_obs.binspec(self.binwave)
        return new_obs

    def __truediv__(self, other):
        """Extends base class truediv to handle binned data."""
        new_obs = spectrum.BaseSpectrum.__truediv__(self, other)
        new_obs.binspec(self.binwave)
        return new_obs

    def apply_redshift(self, z):
        raise NotImplementedError('Observations cannot be redshifted.')

    def convert_flux(self, out_flux_unit):
        """Convert ``self.flux`` and ``self.binflux`` to a different unit.
        The attribute is updated in-place.

        See :func:`synphot.spectrum.convert_fluxes` for more details.

        Parameters
        ----------
        out_flux_unit : str or `astropy.units.core.Unit`
            Output flux unit.

        """
        self._validate_flux_unit(out_flux_unit)
        self.flux = spectrum.convert_fluxes(
            self.wave, self.flux, out_flux_unit, area=self.primary_area,
            vegaspec=None)

        if self.binwave is not None and self.binflux is not None:
            self.binflux = spectrum.convert_fluxes(
                self.binwave, self.binflux, out_flux_unit,
                area=self.primary_area, vegaspec=None)

        # Also update hidden attributes, just in case
        self._set_data(False)

    def sample_binned(self, wavelengths):
        """Sample binned observation at the given wavelengths,
        without interpolation.

        To sample unbinned data, use the ``resample()`` method.

        Parameters
        ----------
        wavelengths : array_like or `astropy.units.quantity.Quantity`
            Wavelength values for sampling. If not a Quantity,
            assumed to be the unit of ``self.binwave``.

        Returns
        -------
        sampled_result : `astropy.units.quantity.Quantity`
            Sampled binned flux that is in-sync with given wavelengths.

        Raises
        ------
        synphot.exceptions.InterpolationNotAllowed
            Interpolation of binned data is not allowed.

        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(True)  # Use binned data

        # Convert wavelengths to self.binwave unit, and do validation
        wavelengths = units.validate_quantity(
            wavelengths, self._wave.unit, equivalencies=units.wave_conversion)
        utils.validate_wavelengths(wavelengths)

        if not np.all(np.in1d(wavelengths, self._wave)):
            raise exceptions.InterpolationNotAllowed(
                'Given wavelengths are not in binwave attribute')

        return self._flux[np.searchsorted(self._wave, wavelengths)]

    def wave_range(self, cenwave, npix, **kwargs):
        """Calculate the wavelength range covered by the given number
        of pixels centered on the given central wavelengths of
        ``self.binwave``.

        Parameters
        ----------
        cenwave : float or `astropy.units.quantity.Quantity`
            Desired central wavelength. If not a Quantity,
            assumed to be in the unit of ``self.binwave``.

        npix : int
            Desired number of pixels, centered on ``cenwave``.

        kwargs : dict
            Keywords accepted by :func:`synphot.binning.wave_range`.

        Returns
        -------
        wave1, wave2 : `astropy.units.quantity.Quantity`
            Lower and upper limits of the wavelength range,
            in the unit of ``cenwave``.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(True)  # Use binned data

        if isinstance(cenwave, u.Quantity):
            bin_wave = units.validate_quantity(
                self._wave, cenwave.unit, equivalencies=units.wave_conversion)
        else:
            cenwave = u.Quantity(cenwave, unit=self._wave.unit)
            bin_wave = self._wave

        w1, w2 = binning.wave_range(
            bin_wave.value, cenwave.value, npix, **kwargs)
        wave1 = u.Quantity(w1, unit=cenwave.unit)
        wave2 = u.Quantity(w2, unit=cenwave.unit)

        return wave1, wave2

    def pixel_range(self, waverange, **kwargs):
        """Calculate the number of pixels within the given wavelength
        range and ``self.binwave``.

        Parameters
        ----------
        waverange : tuple of float or `astropy.units.quantity.Quantity`
            Lower and upper limits of the desired wavelength range.
            If not a Quantity, assumed to be in the same unit as
            ``self.binwave``.

        kwargs : dict
            Keywords accepted by :func:`synphot.binning.pixel_range`.

        Returns
        -------
        npix : number
            Number of pixels.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(True)  # Use binned data

        w1 = units.validate_quantity(
            waverange[0], self._wave.unit, equivalencies=units.wave_conversion)
        w2 = units.validate_quantity(
            waverange[-1], self._wave.unit, equivalencies=units.wave_conversion)

        return binning.pixel_range(
            self._wave.value, (w1.value, w2.value), **kwargs)

    def avgwave(self, binned=False):
        """Calculate the observation average wavelength using
        :func:`synphot.utils.avg_wavelength`.

        Parameters
        ----------
        binned : bool
            Use native (default) or binned data.

        Returns
        -------
        avg_wave : `astropy.units.quantity.Quantity`
            Observation average wavelength.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(binned)
        wave = utils.to_length(self._wave)
        avg_wave = utils.avg_wavelength(wave.value, self._flux.value)
        return u.Quantity(avg_wave, unit=wave.unit)

    def barlam(self, binned=False):
        """Calculate the observation mean log wavelength using
        :func:`synphot.utils.barlam`.

        Parameters
        ----------
        binned : bool
            Use native (default) or binned data.

        Returns
        -------
        bar_lam : `astropy.units.quantity.Quantity`
            Observation mean log wavelength.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(binned)
        wave = utils.to_length(self._wave)
        bar_lam = utils.barlam(wave.value, self._flux.value)
        return u.Quantity(bar_lam, unit=wave.unit)

    def effective_wavelength(self, binned=False, mode='efflerg'):
        """Calculate :ref:`effective wavelength <synphot-formula-effwave>`.

        Parameters
        ----------
        binned : bool
            Use native (default) or binned data.

        mode : {'efflerg', 'efflphot'}
            Flux is first converted to the unit below before calculation:

                * 'efflerg' - FLAM
                * 'efflphot' - PHOTLAM (depreciated)

        Returns
        -------
        eff_lam : `astropy.units.quantity.Quantity`
            Observation effective wavelength.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        synphot.exceptions.SynphotError
            Invalid mode.

        """
        self._set_data(binned)

        # Convert flux to appropriate unit
        mode = mode.lower()
        if mode == 'efflerg':
            flux = spectrum.convert_fluxes(self._wave, self._flux, units.FLAM,
                                           area=self.primary_area)
        elif mode == 'efflphot':
            flux = spectrum.convert_fluxes(self._wave, self._flux, units.PHOTLAM,
                                           area=self.primary_area)
        else:
            raise exceptions.SynphotError(
                'mode={0} is invalid, must be "efflerg" or "efflphot"'.format(
                    mode))

        wave = utils.to_length(self._wave)
        num = utils.trapezoid_integration(
            wave.value, flux.value * wave.value ** 2)
        den = utils.trapezoid_integration(
            wave.value, flux.value * wave.value)

        if den == 0.0:  # pragma: no cover
            eff_lam = 0.0
        else:
            eff_lam = num / den

        return u.Quantity(eff_lam, unit=wave.unit)

    def effstim(self, binned=False, flux_unit=None, band=None,
                vegaspec=None, wave_range=None, force=False):
        """Calculate :ref:`effective stimulus <synphot-formula-effstim>`.

        Calculations are done with flux in given unit, and wavelengths
        in Angstrom.

        Parameters
        ----------
        binned : bool
            Use native (default) or binned data.

        flux_unit : `None`, str, or `astropy.units.core.Unit`
            The unit of effective stimulus. If `None`, uses ``self`` flux unit.

        band : `~synphot.spectrum.SpectralElement`
            Passband that went into the observation. This is needed
            unless flux unit is count or OBMAG.

        vegaspec : `synphot.spectrum.SourceSpectrum`
            Vega spectrum from :func:`SourceSpectrum.from_vega`.
            This is *only* used if given flux unit is VEGAMAG.

        wave_range : tuple of float or `astropy.units.quantity.Quantity`, or `None`
            Wavelength range (inclusive) for calculations in the
            form of ``(low, high)``. If not Quantity, assumed to be
            in the wavelength unit of ``self``. If `None`, the full
            range is used.

        force : bool
            If a wavelength range is given, partial overlap raises
            an exception when this is `False` (default). Otherwise,
            it returns calculation for the overlapping region.
            Disjoint wavelength range raises an exception regardless.

        Returns
        -------
        eff_stim : `astropy.units.quantity.Quantity`
            Observation effective stimulus in given flux unit.

        Raises
        ------
        synphot.exceptions.DisjointError
            Passband or wavelength range does not overlap with observation.

        synphot.exceptions.OverlapError
            Passband or wavelength range only partially overlaps with
            observation.

        synphot.exceptions.UndefinedBinset
            Missing binned data.

        synphot.exceptions.SynphotError
            Missing passband, invalid inputs, or calculation failed.

        """
        self._set_data(binned)

        if flux_unit is None:
            flux_unit = self._flux.unit
        else:
            flux_unit = units.validate_unit(flux_unit)

        # Use entire wavelength range
        if wave_range is None:
            inwave = self._wave
            influx = self._flux

        # Use given wavelength range
        else:
            w1 = units.validate_quantity(wave_range[0], self._wave.unit,
                                         equivalencies=units.wave_conversion)
            w2 = units.validate_quantity(wave_range[-1], self._wave.unit,
                                         equivalencies=units.wave_conversion)
            if w1 >= w2:
                raise exceptions.SynphotError('Invalid wavelength range.')

            stat = utils.overlap_status(
                np.array([w1.value, w2.value]), self._wave.value)

            if stat == 'none':
                raise exceptions.DisjointError(
                    'Observation and wavelength range are disjoint.')
            elif 'partial' in stat:
                if force:
                    log.warn('EFFSTIM calculated only for wavelengths in the '
                             'overlap between observation and given range.')
                    w1 = max(w1, self._wave.min())
                    w2 = min(w2, self._wave.max())
                else:
                    raise exceptions.OverlapError(
                        'Observation and wavelength range do not fully '
                        'overlap. You may use force=True to force this '
                        'calculation anyway.')
            elif stat != 'full':  # pragma: no cover
                raise exceptions.SynphotError(
                    'Overlap result of {0} is unexpected'.format(stat))

            if binned:
                i1 = np.searchsorted(self.bin_edges, w1) - 1
                i2 = np.searchsorted(self.bin_edges, w2)
                inwave = self._wave[i1:i2]
                influx = self.sample_binned(inwave)
            else:
                mask = ((self._wave >= w1) & (self._wave <= w2))
                inwave = u.Quantity(utils.merge_wavelengths(
                        self._wave[mask].value,
                        np.array([w1.value, w2.value])), unit=self._wave.unit)
                utils.validate_wavelengths(inwave)
                influx = self.resample(inwave)

        flux_unit_name = flux_unit.to_string()

        # Special handling for non-density units
        if flux_unit_name in (u.count.to_string(), units.OBMAG.to_string()):
            self_flux = spectrum.convert_fluxes(
                inwave, influx, u.count, area=self.primary_area)
            val = self_flux.sum()
            utils.validate_totalflux(val.value)

            if flux_unit.decompose() == u.mag:
                eff_stim = u.Quantity(
                    -2.5 * np.log10(val.value), unit=flux_unit)
            else:
                eff_stim = val

        # Density flux units and VEGAMAG
        else:
            # Passband is required and must overlap
            if isinstance(band, spectrum.SpectralElement):
                stat = band.check_overlap(self)
                if stat == 'none':
                    raise exceptions.DisjointError(
                        'Observation and passband are disjoint.')
                elif 'partial' in stat:
                    raise exceptions.OverlapError(
                        'Observation and passband do not fully overlap.')
                elif stat != 'full':  # pragma: no cover
                    raise exceptions.SynphotError(
                        'Overlap result of {0} is unexpected'.format(stat))
            else:
                raise exceptions.SynphotError('Missing passband data.')

            # Convert wavelengths to Angstrom
            band_wave = band.wave.to(u.AA, equivalencies=units.wave_conversion)
            self_wave = inwave.to(u.AA, equivalencies=units.wave_conversion)

            # Convert observation to given flux unit.
            # For mag, convert to corresponding linear flux unit.
            if flux_unit_name in (units.STMAG.to_string(),
                                  units.VEGAMAG.to_string()):
                tmp_unit = units.FLAM
            elif flux_unit_name == units.ABMAG.to_string():
                tmp_unit = units.FNU
            elif flux_unit.decompose() != u.mag:
                tmp_unit = flux_unit
            else:
                raise exceptions.SynphotError(
                    'Flux unit {0} is invalid'.format(flux_unit))

            self_flux = spectrum.convert_fluxes(
                self_wave, influx, tmp_unit, area=self.primary_area)

            if flux_unit_name == units.VEGAMAG.to_string():
                if not isinstance(vegaspec, spectrum.SourceSpectrum):
                    raise exceptions.SynphotError(
                        'Vega spectrum is missing.')
                vega_flux = spectrum.convert_fluxes(
                    self_wave, vegaspec.resample(self_wave), tmp_unit,
                    area=self.primary_area, vegaspec=None)
                flux = self_flux.value / vega_flux.value
            else:
                flux = self_flux.value

            # Integrate
            num = utils.trapezoid_integration(
                self_wave.value, self_wave.value * flux)
            den = utils.trapezoid_integration(
                band_wave.value, band_wave.value * band.thru.value)
            utils.validate_totalflux(num)
            utils.validate_totalflux(den)
            val = num / den

            # Convert back to mag, if needed
            if flux_unit_name in (units.STMAG.to_string(),
                                  units.ABMAG.to_string()):
                eff_stim = spectrum.convert_fluxes(
                    1, u.Quantity(val, unit=tmp_unit), flux_unit)
            elif flux_unit_name == units.VEGAMAG.to_string():
                eff_stim = u.Quantity(-2.5 * np.log10(val), unit=flux_unit)
            else:
                eff_stim = u.Quantity(val, unit=flux_unit)

        return eff_stim

    def countrate(self, binned=True, wave_range=None, force=False):
        """Calculate :ref:`effective stimulus <synphot-formula-effstim>`
        in counts.

        Parameters
        ----------
        binned, wave_range, force
            See :func:`effstim`.

        Returns
        -------
        eff_stim : `astropy.units.quantity.Quantity`
            Effective stimulus in counts.

        """
        return self.effstim(binned=binned, flux_unit=u.count, band=None,
                            vegaspec=None, wave_range=wave_range, force=force)

    def to_fits(self, filename, binned=True, **kwargs):
        """Write the spectrum to a FITS file.

        Parameters
        ----------
        filename : str
            Output filename.

        binned : bool
            Write out data in native wavelengths if `False`.
            Else, write binned data (default).

        kwargs : dict
            Keywords accepted by :func:`synphot.io.write_fits_spec`.

        Raises
        ------
        synphot.exceptions.UndefinedBinset
            Missing binned data.

        """
        self._set_data(binned)

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {
            'expr': (str(self), 'synphot expression'),
            'binned': binned,
            'tdisp1': 'G15.7',
            'tdisp2': 'G15.7' }

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        io.write_fits_spec(filename, self._wave, self._flux, **kwargs)

    @classmethod
    def from_spec_band(cls, spec, band, binwave=None, force='none', area=None):
        """Create an Observation from given source spectrum and passband.

        By default, it is required that the spectrum and passband fully
        overlap. Partial overlap will raise an error in the absence of the
        ``force`` keyword. If they do not overlap at all, an error
        is raised regardless.

        Parameters
        ----------
        spec : `~synphot.spectrum.SourceSpectrum`
            Source spectrum.

        band : `~synphot.spectrum.SpectralElement`
            Passband.

        binwave : `None`, array_like, or `astropy.units.quantity.Quantity`
            Center of binned wavelengths. If array is given but not
            a Quantity, assumed to have the same unit as ``spec.wave``.
            If `None`, ``spec.wave`` is used.

        force : {'none', 'extrap', 'taper'}
            Force creation of an Observation even when source spectrum
            and passband do not fully overlap:

                * 'none' - Source must encompass passband (default)
                * 'extrap' - Extrapolate source spectrum
                * 'taper' - Taper source spectrum

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        Returns
        -------
        obspec : obj
            Observation spectrum.

        Raises
        ------
        synphot.exceptions.DisjointError
            Passband does not overlap with source spectrum.

        synphot.exceptions.OverlapError
            Passband only partially overlaps with source spectrum
            when they must fully overlap.

        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        if not isinstance(spec, spectrum.SourceSpectrum):
            raise exceptions.SynphotError('Invalid source spectrum')

        if not isinstance(band, spectrum.SpectralElement):
            raise exceptions.SynphotError('Invalid passband')

        if binwave is None:
            binwave = spec.wave
            log.info('Observation binned wavelength centers will be '
                     'taken from source spectrum wavelengths.')

        # Inherit warnings, with source spectrum having higher priority
        warn = deepcopy(band.warnings)
        warn.update(spec.warnings)

        # Validate overlap
        force = force.lower()
        stat = band.check_overlap(spec)

        if stat == 'none':
            raise exceptions.DisjointError(
                'Source spectrum and passband are disjoint.')
        elif 'partial' in stat:
            if force == 'none':
                raise exceptions.OverlapError(
                    'Source spectrum and passband do not fully overlap. '
                    'You may use force=[extrap|taper] to force this '
                    'Observation anyway.')
            elif force == 'taper':
                spec = deepcopy(spec)  # Avoid modifying input
                spec.taper()
                msg = 'Source spectrum is tapered.'
                log.warn(msg)
                warn['PartialOverlap'] = msg
            elif force.startswith('extrap'):
                msg = 'Source spectrum will be extrapolated at constant value.'
                log.warn(msg)
                warn['PartialOverlap'] = msg
            else:
                raise exceptions.SynphotError(
                    'force={0} is invalid, must be "none", "taper", '
                    'or "extrap"'.format(force))
        elif stat != 'full':  # pragma: no cover
            raise exceptions.SynphotError(
                'Overlap result of {0} is unexpected'.format(stat))

        mulspec = spec * band
        header = {'expr': '{0} * {1}'.format(str(spec), str(band))}

        # Inherit primary area and set warning
        obspec = cls(mulspec.wave, mulspec.flux, binwave=binwave, area=area,
                     header=header)
        obspec.primary_area = spec.primary_area
        obspec.warnings.update(warn)

        return obspec

    def plot(self, **kwargs):  # pragma: no cover
        """Plot the observation.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        kwargs : dict
            Keywords accepted by :func:`synphot.spectrum.BaseSpectrum.plot`,
            *except* ``overplot_data`` and ``data_labels``.

        """
        for key in ('overplot_data', 'data_labels'):
            if key in kwargs:
                del kwargs[key]

        spectrum.BaseSpectrum.plot(
            self, overplot_data=(self.binwave.value, self.binflux.value),
            data_labels=('Native dataset', 'Binned dataset'), **kwargs)
