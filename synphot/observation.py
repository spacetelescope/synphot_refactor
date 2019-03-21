# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines an observed spectrum, i.e., a source spectrum
that has gone through a bandpass.

"""
from __future__ import absolute_import, division, print_function

# STDLIB
import math
import warnings

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import log
from astropy import units as u
from astropy.utils.exceptions import (AstropyUserWarning,
                                      AstropyDeprecationWarning)

# LOCAL
from . import binning, exceptions, units, utils
from .models import Empirical1D
from .spectrum import BaseSourceSpectrum, SourceSpectrum, SpectralElement

__all__ = ['Observation']


class Observation(BaseSourceSpectrum):
    """This is an observed spectrum, where a source spectrum
    has gone through a bandpass.

    Usually, this is the end point of a chain of spectral
    manipulation. It has extra attributes that deal with binning,
    which is introduced by the detector.

    Parameters
    ----------
    spec : `~synphot.spectrum.SourceSpectrum`
        Source spectrum.

    band : `~synphot.spectrum.SpectralElement`
        Bandpass.

    binset : array-like, `~astropy.units.quantity.Quantity`, or `None`
        Center of binned wavelengths.
        If not a Quantity, assumed to be in Angstrom.
        If `None`, input ``self.waveset`` values are used.

    force : {`None`, 'none', 'extrap', 'taper'}
        Force creation of an observation even when source spectrum
        and bandpass do not fully overlap:

            * `None` or 'none' - Source must encompass bandpass (default)
            * 'extrap' - Extrapolate source spectrum (this changes the
              underlying model of ``spec`` to always extrapolate,
              if applicable)
            * 'taper' - Taper source spectrum

    Raises
    ------
    synphot.exceptions.DisjointError
        Bandpass does not overlap with source spectrum.

    synphot.exceptions.PartialOverlap
        Bandpass only partially overlaps with source spectrum
        when they must fully overlap.

    synphot.exceptions.SynphotError
        Invalid inputs.

    synphot.exceptions.UndefinedBinset
        Missing binned wavelength set.

    """
    def __init__(self, spec, band, binset=None, force='none'):
        if not isinstance(spec, SourceSpectrum):
            raise exceptions.SynphotError('Invalid source spectrum.')

        if not isinstance(band, SpectralElement):
            raise exceptions.SynphotError('Invalid bandpass.')

        # Inherit input warnings like ASTROLIB PYSYNPHOT
        warn = {}

        # Validate overlap
        if force is None:
            force = 'none'
        else:
            force = force.lower()
        stat = band.check_overlap(spec)

        if stat == 'none':
            raise exceptions.DisjointError(
                'Source spectrum and bandpass are disjoint.')

        elif 'partial' in stat:

            if force == 'none':
                raise exceptions.PartialOverlap(
                    'Source spectrum and bandpass do not fully overlap. '
                    'You may use force=[extrap|taper] to force this '
                    'Observation anyway.')

            elif force == 'taper':
                spec = spec.taper()
                msg = 'Source spectrum is tapered.'
                warnings.warn(msg, AstropyUserWarning)
                warn['PartialOverlap'] = msg

            elif force.startswith('extrap'):
                if spec.force_extrapolation():
                    msg = ('Source spectrum will be extrapolated (at constant '
                           'value for empirical model).')
                else:
                    msg = ('Source spectrum will be evaluated outside '
                           'pre-defined waveset.')

                warnings.warn(msg, AstropyUserWarning)
                warn['PartialOverlap'] = msg

            else:
                raise exceptions.SynphotError(
                    'force={0} is invalid, must be "none", "taper", '
                    'or "extrap"'.format(force))

        elif stat != 'full':  # pragma: no cover
            raise exceptions.SynphotError(
                'Overlap result of {0} is unexpected'.format(stat))

        # Create composite spectrum
        super(Observation, self).__init__(spec * band, clean_meta=True)
        self._spec = spec
        self._band = band
        self._force = force

        # Merge in other warnings
        self.warnings = warn

        # Initialize bins
        self._init_bins(binset)

    def _init_bins(self, binset):
        """Calculated binned wavelength centers, edges, and flux.

        By contrast, the native waveset and flux should be considered
        samples of a continuous function.

        Thus, it makes sense to interpolate ``self.waveset`` and
        ``self(self.waveset)``, but not `binset` and `binflux`.

        """
        if binset is None:
            if self.bandpass.waveset is not None:
                self._binset = self.bandpass.waveset
            elif self.spectrum.waveset is not None:
                self._binset = self.spectrum.waveset
                log.info('Bandpass waveset is undefined; '
                         'Using source spectrum waveset instead.')
            else:
                raise exceptions.UndefinedBinset(
                    'Both source spectrum and bandpass have undefined '
                    'waveset; Provide binset manually.')
        else:
            self._binset = self._validate_wavelengths(binset)

        # binset must be in ascending order for calcbinflux()
        # to work properly.
        if self._binset[0] > self._binset[-1]:
            self._binset = self._binset[::-1]

        self._bin_edges = binning.calculate_bin_edges(self._binset)

        # Merge bin edges and centers in with the natural waveset
        spwave = utils.merge_wavelengths(
            self._bin_edges.value, self._binset.value)
        if self.waveset is not None:
            spwave = utils.merge_wavelengths(spwave, self.waveset.value)

        # Throw out invalid wavelengths after merging.
        spwave = spwave[spwave > 0]

        # Compute indices associated to each endpoint.
        indices = np.searchsorted(spwave, self._bin_edges.value)
        i_beg = indices[:-1]
        i_end = indices[1:]

        # Prepare integration variables.
        flux = self(spwave)
        avflux = (flux.value[1:] + flux.value[:-1]) * 0.5
        deltaw = spwave[1:] - spwave[:-1]

        # Sum over each bin.
        binflux, intwave = binning.calcbinflux(
            self._binset.size, i_beg, i_end, avflux, deltaw)

        self._binflux = binflux * flux.unit

    @property
    def spectrum(self):
        """Source spectrum of the observation."""
        return self._spec

    @property
    def bandpass(self):
        """Bandpass of the observation."""
        return self._band

    @property
    def binset(self):
        """Center of binned wavelengths."""
        return self._binset

    @property
    def bin_edges(self):
        """Edges of binned wavelengths."""
        return self._bin_edges

    @property
    def binflux(self):
        """Binned flux corresponding to `binset`."""
        return self._binflux

    def __mul__(self, other):
        """Multiply self and other."""
        sp = self.spectrum * other
        obs = self.__class__(
            sp, self.bandpass, binset=self.binset, force=self._force)
        return obs

    def taper(self, **kwargs):
        """Tapering is disabled."""
        raise NotImplementedError('Observation cannot be tapered.')

    def _validate_binned_wavelengths(self, wave):
        if wave is None:
            wavelengths = self.binset
        else:
            wavelengths = self._validate_wavelengths(wave)
        return wavelengths

    def sample_binned(self, wavelengths=None, flux_unit=None, **kwargs):
        """Sample binned observation without interpolation.

        To sample unbinned data, use ``__call__``.

        Parameters
        ----------
        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, `binset` is used.

        flux_unit : str or `~astropy.units.core.Unit` or `None`
            Flux is converted to this unit.
            If not given, internal unit is used.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.units.convert_flux`.

        Returns
        -------
        flux : `~astropy.units.quantity.Quantity`
            Binned flux in given unit.

        Raises
        ------
        synphot.exceptions.InterpolationNotAllowed
            Interpolation of binned data is not allowed.

        """
        x = self._validate_binned_wavelengths(wavelengths)
        i = np.searchsorted(self.binset, x)
        if not np.allclose(self.binset[i].value, x.value):
            raise exceptions.InterpolationNotAllowed(
                'Some or all wavelength values are not in binset.')
        y = self.binflux[i]

        if flux_unit is None:
            flux = y
        else:
            flux = units.convert_flux(x, y, flux_unit, **kwargs)

        return flux

    def _get_binned_arrays(self, wavelengths, flux_unit, area=None,
                           vegaspec=None):
        """Get binned observation in user units."""
        x = self._validate_binned_wavelengths(wavelengths)
        y = self.sample_binned(wavelengths=x, flux_unit=flux_unit, area=area,
                               vegaspec=vegaspec)

        if isinstance(wavelengths, u.Quantity):
            w = x.to(wavelengths.unit, u.spectral())
        else:
            w = x

        return w, y

    def binned_waverange(self, cenwave, npix, **kwargs):
        """Calculate the wavelength range covered by the given number
        of pixels centered on the given central wavelengths of
        `binset`.

        Parameters
        ----------
        cenwave : float or `~astropy.units.quantity.Quantity`
            Desired central wavelength.
            If not a Quantity, assumed to be in Angstrom.

        npix : int
            Desired number of pixels, centered on ``cenwave``.

        kwargs : dict
            Keywords accepted by :func:`synphot.binning.wave_range`.

        Returns
        -------
        waverange : `~astropy.units.quantity.Quantity`
            Lower and upper limits of the wavelength range,
            in the unit of ``cenwave``.

        """
        # Calculation is done in the unit of cenwave.
        if not isinstance(cenwave, u.Quantity):
            cenwave = cenwave * self._internal_wave_unit

        bin_wave = units.validate_quantity(
            self.binset, cenwave.unit, equivalencies=u.spectral())

        return binning.wave_range(
            bin_wave.value, cenwave.value, npix, **kwargs) * cenwave.unit

    def binned_pixelrange(self, waverange, **kwargs):
        """Calculate the number of pixels within the given wavelength
        range and `binset`.

        Parameters
        ----------
        waverange : tuple of float or `~astropy.units.quantity.Quantity`
            Lower and upper limits of the desired wavelength range.
            If not a Quantity, assumed to be in Angstrom.

        kwargs : dict
            Keywords accepted by :func:`synphot.binning.pixel_range`.

        Returns
        -------
        npix : int
            Number of pixels.

        """
        x = units.validate_quantity(
            waverange, self._internal_wave_unit, equivalencies=u.spectral())
        return binning.pixel_range(self.binset.value, x.value, **kwargs)

    def effective_wavelength(self, binned=True, wavelengths=None,
                             mode='efflerg'):
        """Calculate :ref:`effective wavelength <synphot-formula-effwave>`.

        Parameters
        ----------
        binned : bool
            Sample data in native wavelengths if `False`.
            Else, sample binned data (default).

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` or `binset` is used, depending
            on ``binned``.

        mode : {'efflerg', 'efflphot'}
            Flux is first converted to the unit below before calculation:

                * 'efflerg' - FLAM
                * 'efflphot' - PHOTLAM (deprecated)

        Returns
        -------
        eff_lam : `~astropy.units.quantity.Quantity`
            Observation effective wavelength.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid mode.

        """
        mode = mode.lower()
        if mode == 'efflerg':
            flux_unit = units.FLAM
        elif mode == 'efflphot':
            warnings.warn(
                'Usage of EFFLPHOT is deprecated.', AstropyDeprecationWarning)
            flux_unit = units.PHOTLAM
        else:
            raise exceptions.SynphotError(
                'mode must be "efflerg" or "efflphot"')

        if binned:
            x = self._validate_binned_wavelengths(wavelengths).value
            y = self.sample_binned(wavelengths=x, flux_unit=flux_unit).value
        else:
            x = self._validate_wavelengths(wavelengths).value
            y = units.convert_flux(x, self(x), flux_unit).value

        num = np.trapz(y * x ** 2, x=x)
        den = np.trapz(y * x, x=x)

        if den == 0.0:  # pragma: no cover
            eff_lam = 0.0
        else:
            eff_lam = abs(num / den)

        return eff_lam * self._internal_wave_unit

    # https://github.com/spacetelescope/synphot_refactor/issues/159
    def effstim(self, flux_unit=None, wavelengths=None, area=None,
                vegaspec=None):
        """Calculate :ref:`effective stimulus <synphot-formula-effstim>`
        for given flux unit.

        Parameters
        ----------
        flux_unit : str or `~astropy.units.core.Unit` or `None`
            The unit of effective stimulus.
            COUNT gives result in count/s (see :meth:`countrate` for more
            options).
            If not given, internal unit is used.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling. This must be given if
            ``self.waveset`` is undefined for the underlying spectrum model(s).
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        Returns
        -------
        eff_stim : `~astropy.units.quantity.Quantity`
            Observation effective stimulus based on given flux unit.

        """
        if flux_unit is None:
            flux_unit = self._internal_flux_unit

        flux_unit = units.validate_unit(flux_unit)
        flux_unit_name = flux_unit.to_string()

        # Special handling of COUNT/OBMAG.
        # This is special case of countrate calculations.
        if flux_unit == u.count or flux_unit_name == units.OBMAG.to_string():
            val = self.countrate(area, binned=False, wavelengths=wavelengths)

            if flux_unit.decompose() == u.mag:
                eff_stim = (-2.5 * np.log10(val.value)) * flux_unit
            else:
                eff_stim = val

            return eff_stim

        # Special handling of VEGAMAG.
        # This is basically effstim(self)/effstim(Vega)
        if flux_unit_name == units.VEGAMAG.to_string():
            num = self.integrate(wavelengths=wavelengths)
            den = (vegaspec * self.bandpass).integrate()
            utils.validate_totalflux(num)
            utils.validate_totalflux(den)
            return (2.5 * (math.log10(den.value) -
                           math.log10(num.value))) * units.VEGAMAG

        # Sample the bandpass
        x_band = self.bandpass._validate_wavelengths(wavelengths).value
        y_band = self.bandpass(x_band).value

        # Sample the observation in FLAM
        inwave = self._validate_wavelengths(wavelengths).value
        influx = units.convert_flux(inwave, self(inwave), units.FLAM).value

        # Integrate
        num = abs(np.trapz(inwave * influx, x=inwave))
        den = abs(np.trapz(x_band * y_band, x=x_band))
        utils.validate_totalflux(num)
        utils.validate_totalflux(den)
        val = (num / den) * units.FLAM

        # Integration should always be done in FLAM and then
        # converted to desired units as follows.
        if flux_unit.physical_type == 'spectral flux density wav':
            if flux_unit == u.STmag:
                eff_stim = val.to(flux_unit)
            else:  # FLAM
                eff_stim = val
        elif flux_unit.physical_type in (
                'spectral flux density', 'photon flux density',
                'photon flux density wav'):
            w_pivot = self.bandpass.pivot()
            eff_stim = units.convert_flux(w_pivot, val, flux_unit)
        else:
            raise exceptions.SynphotError(
                'Flux unit {0} is invalid'.format(flux_unit))

        return eff_stim

    def countrate(self, area, binned=True, wavelengths=None, waverange=None,
                  force=False):
        """Calculate :ref:`effective stimulus <synphot-formula-effstim>`
        in count/s.

        Parameters
        ----------
        area : float or `~astropy.units.quantity.Quantity`
            Area that flux covers. If not a Quantity, assumed to be in
            :math:`cm^{2}`.

        binned : bool
            Sample data in native wavelengths if `False`.
            Else, sample binned data (default).

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling. This must be given if
            ``self.waveset`` is undefined for the underlying spectrum model(s).
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` or `binset` is used, depending
            on ``binned``.

        waverange : tuple of float, Quantity, or `None`
            Lower and upper limits of the desired wavelength range.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, the full range is used.

        force : bool
            If a wavelength range is given, partial overlap raises
            an exception when this is `False` (default). Otherwise,
            it returns calculation for the overlapping region.
            Disjoint wavelength range raises an exception regardless.

        Returns
        -------
        count_rate : `~astropy.units.quantity.Quantity`
            Observation effective stimulus in count/s.

        Raises
        ------
        synphot.exceptions.DisjointError
            Wavelength range does not overlap with observation.

        synphot.exceptions.PartialOverlap
            Wavelength range only partially overlaps with observation.

        synphot.exceptions.SynphotError
            Calculation failed.

        """
        # Sample the observation
        if binned:
            x = self._validate_binned_wavelengths(wavelengths).value
            y = self.sample_binned(wavelengths=x, flux_unit=u.count,
                                   area=area).value
        else:
            x = self._validate_wavelengths(wavelengths).value
            y = units.convert_flux(x, self(x), u.count,
                                   area=area).value

        # Use entire wavelength range
        if waverange is None:
            influx = y

        # Use given wavelength range
        else:
            w = units.validate_quantity(waverange, self._internal_wave_unit,
                                        equivalencies=u.spectral()).value
            stat = utils.overlap_status(w, x)
            w1 = w.min()
            w2 = w.max()

            if stat == 'none':
                raise exceptions.DisjointError(
                    'Observation and wavelength range are disjoint.')
            elif 'partial' in stat:
                if force:
                    warnings.warn(
                        'Count rate calculated only for wavelengths in the '
                        'overlap between observation and given range.',
                        AstropyUserWarning)
                    w1 = max(w1, x.min())
                    w2 = min(w2, x.max())
                else:
                    raise exceptions.PartialOverlap(
                        'Observation and wavelength range do not fully '
                        'overlap. You may use force=True to force this '
                        'calculation anyway.')
            elif stat != 'full':  # pragma: no cover
                raise exceptions.SynphotError(
                    'Overlap result of {0} is unexpected'.format(stat))

            if binned:
                if wavelengths is None:
                    bin_edges = self.bin_edges.value
                else:
                    bin_edges = binning.calculate_bin_edges(x).value
                i1 = np.searchsorted(bin_edges, w1) - 1
                i2 = np.searchsorted(bin_edges, w2)
                influx = y[i1:i2]
            else:
                mask = ((x >= w1) & (x <= w2))
                influx = y[mask]

        val = math.fsum(influx)
        utils.validate_totalflux(val)

        return val * (u.count / u.s)

    def plot(self, binned=True, wavelengths=None, flux_unit=None, area=None,
             vegaspec=None, **kwargs):  # pragma: no cover
        """Plot the observation.

        .. note:: Uses ``matplotlib``.

        Parameters
        ----------
        binned : bool
            Plot data in native wavelengths if `False`.
            Else, plot binned data (default).

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` or `binset` is used, depending
            on ``binned``.

        flux_unit : str or `~astropy.units.core.Unit` or `None`
            Flux is converted to this unit for plotting.
            If not given, internal unit is used.

        area, vegaspec
            See :func:`~synphot.units.convert_flux`.

        kwargs : dict
            See :func:`synphot.spectrum.BaseSpectrum.plot`.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        if binned:
            w, y = self._get_binned_arrays(wavelengths, flux_unit, area=area,
                                           vegaspec=vegaspec)
        else:
            w, y = self._get_arrays(wavelengths, flux_unit=flux_unit,
                                    area=area, vegaspec=vegaspec)
        self._do_plot(w, y, **kwargs)

    def as_spectrum(self, binned=True, wavelengths=None):
        """Reduce the observation to an empirical source spectrum.

        An observation is a complex object with some restrictions
        on its capabilities. At times, it would be useful to work
        with the observation as a simple object that is easier to
        manipulate and takes up less memory.

        This is also useful for writing an observation as sampled
        spectrum out to a FITS file.

        Parameters
        ----------
        binned : bool
            Write out data in native wavelengths if `False`.
            Else, write binned data (default).

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` or `binset` is used, depending
            on ``binned``.

        Returns
        -------
        sp : `~synphot.spectrum.SourceSpectrum`
            Empirical source spectrum.

        """
        if binned:
            w, y = self._get_binned_arrays(
                wavelengths, self._internal_flux_unit)
        else:
            w, y = self._get_arrays(
                wavelengths, flux_unit=self._internal_flux_unit)

        header = {'observation': str(self), 'binned': binned}
        return SourceSpectrum(Empirical1D, points=w, lookup_table=y,
                              meta={'header': header})
