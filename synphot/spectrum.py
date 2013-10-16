# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines the different type of synphot spectra.

Here are the two main classes:

    * `SourceSpectrum` - For a spectrum with wavelengths and fluxes.
    * `SpectralElement` - For observatory passband (e.g., filters) with
      wavelengths and throughput, which is unitless.

"""
from __future__ import division, print_function

# STDLIB
import os
from copy import deepcopy

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import log
from astropy import units as u

# LOCAL
from . import binning, planck, exceptions, config, io, utils, units


__all__ = ['convert_fluxes', 'BaseSpectrum', 'BaseUnitlessSpectrum',
           'SourceSpectrum', 'SpectralElement']


#-------------------------------------------------------------------------#
# Flux conversion function.                                               #
# It is here instead of units.py because it relies on source spectrum.    #
# Having this in units.py would cause circular import.                    #
#-------------------------------------------------------------------------#

def convert_fluxes(wavelengths, fluxes, out_flux_unit, **kwargs):
    """Perform :ref:`flux conversion <synphot-flux-conversion>`.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    fluxes : array_like or `astropy.units.quantity.Quantity`
        Flux values. If not a Quantity, assumed to be in PHOTLAM.

    out_flux_unit : str or `astropy.units.core.Unit`
        Output flux unit.

    area : float or `astropy.units.quantity.Quantity`
        Area that fluxes cover. If not a Quantity, assumed to be in cm^2.
        This value *must* be provided for conversions involving
        OBMAG and count, otherwise it is not needed.

    vegaspec : `synphot.spectrum.SourceSpectrum`
        Vega spectrum from :func:`SourceSpectrum.from_vega`.
        This is *only* used for conversions involving VEGAMAG.

    Returns
    -------
    out_flux : `astropy.units.quantity.Quantity`
        Converted flux values.

    Raises
    ------
    astropy.units.core.UnitsError
        Conversion failed.

    synphot.exceptions.SynphotError
        Area or Vega spectrum is not given when needed.

    """
    if not isinstance(fluxes, u.Quantity):
        fluxes = u.Quantity(fluxes, unit=units.PHOTLAM)

    out_flux_unit = units.validate_unit(out_flux_unit)
    out_flux_unit_name = out_flux_unit.to_string()
    in_flux_unit_name = fluxes.unit.to_string()

    # No conversion necessary
    if in_flux_unit_name == out_flux_unit_name:
        return fluxes

    # Use built-in astropy.units conversion
    if (fluxes.unit.physical_type != 'unknown' and
            fluxes.unit.physical_type == out_flux_unit.physical_type):
        return fluxes.to(out_flux_unit)

    # Wavelengths must be in Angstrom
    wavelengths = units.validate_quantity(
        wavelengths, u.AA, equivalencies=units.wave_conversion)

    # Convert input unit to PHOTLAM
    if in_flux_unit_name == units.PHOTLAM.to_string():
        flux_photlam = fluxes
    else:
        # Handles different prefixes of Jy by converting it to FNU
        # so the equivalencies can understand.
        if (fluxes.unit.physical_type == 'spectral flux density' and
                in_flux_unit_name != units.FNU.to_string()):
            flux_tmp = fluxes.to(units.FNU)
        else:
            flux_tmp = fluxes

        flux_photlam = _convert_fluxes(
            wavelengths, flux_tmp, units.PHOTLAM, **kwargs)

    # Convert PHOTLAM to output unit
    if out_flux_unit_name == units.PHOTLAM.to_string():
        out_flux = flux_photlam
    elif (out_flux_unit.physical_type == 'spectral flux density' and
          out_flux_unit_name != units.FNU.to_string()):  # xJy
        flux_tmp = _convert_fluxes(
            wavelengths, flux_photlam, units.FNU, **kwargs)
        out_flux = flux_tmp.to(out_flux_unit)
    else:
        out_flux = _convert_fluxes(
            wavelengths, flux_photlam, out_flux_unit, **kwargs)

    return out_flux


def _convert_fluxes(wavelengths, fluxes, out_flux_unit, area=None,
                    vegaspec=None):
    """Flux conversion worker."""
    flux_unit_names = (fluxes.unit.to_string(), out_flux_unit.to_string())

    # VEGAMAG
    if units.VEGAMAG.to_string() in flux_unit_names:
        if not isinstance(vegaspec, SourceSpectrum):
            raise exceptions.SynphotError('Vega spectrum is missing.')

        flux_vega = convert_fluxes(
            wavelengths, vegaspec.resample(wavelengths), units.PHOTLAM,
            area=area, vegaspec=None)
        out_flux = fluxes.unit.to(
            out_flux_unit, (fluxes.value, flux_vega.value),
            equivalencies=units.flux_conversion_vegamag)

    # OBMAG or count
    elif (u.count.to_string() in flux_unit_names or
          units.OBMAG.to_string() in flux_unit_names):
        if area is None:
            raise exceptions.SynphotError(
                'Area must be provided for conversion involving count or OBMAG.')

        area = units.validate_quantity(area, units.AREA)
        area_arr = np.empty(fluxes.shape, dtype=fluxes.dtype)
        area_arr.fill(area.value)
        bin_widths = binning.calculate_bin_widths(
            binning.calculate_bin_edges(wavelengths))
        out_flux = fluxes.unit.to(
            out_flux_unit, (fluxes.value, bin_widths.value, area_arr),
            equivalencies=units.flux_conversion_nondensity)

    # FLAM or STMAG
    elif (units.FLAM.to_string() in flux_unit_names or
          units.STMAG.to_string() in flux_unit_names):
        out_flux = fluxes.unit.to(
            out_flux_unit, (wavelengths.value, fluxes.value),
            equivalencies=units.flux_conversion_wav)

    # PHOTNU, FNU, or ABMAG
    elif (units.PHOTNU.to_string() in flux_unit_names or
          units.FNU.to_string() in flux_unit_names or
          units.ABMAG.to_string() in flux_unit_names):
        out_flux = fluxes.unit.to(
            out_flux_unit, (wavelengths.value, fluxes.value),
            equivalencies=units.flux_conversion_freq)

    else:
        raise u.UnitsError('{0} and {1} are not convertible'.format(
                fluxes.unit, out_flux_unit))

    return u.Quantity(out_flux, unit=out_flux_unit)


#-------------------------------------------------------------------------#
# Spectrum classes.                                                       #
#-------------------------------------------------------------------------#

class BaseSpectrum(object):
    """Base class for generic spectrum that should not be used directly.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Fluxes, if not magnitudes, are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    fluxes : array_like or `astropy.units.quantity.Quantity`
        Flux values. If not a Quantity, assumed to be in ``flux_unit``.

    flux_unit : str or `astropy.units.core.Unit`
        Flux unit, which defaults to FLAM. This is *only* used if
        ``fluxes`` is not Quantity.

    area : float or `astropy.units.quantity.Quantity`, optional
        Area that fluxes cover. Usually, this is the area of
        the primary mirror of the observatory of interest.
        If not a Quantity, assumed to be in cm^2.

    header : dict, optional
        Metadata.

    Attributes
    ----------
    wave, flux : `astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

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
    def __init__(self, wavelengths, fluxes, flux_unit=units.FLAM, area=None,
                 header={}):
        self.warnings = {}

        if not isinstance(fluxes, u.Quantity):
            self.flux = u.Quantity(fluxes, unit=flux_unit)
        else:
            self.flux = fluxes.copy()

        self._validate_flux_unit(self.flux.unit)
        self._validate_flux_value()

        if not isinstance(wavelengths, u.Quantity):
            self.wave = u.Quantity(wavelengths, unit=u.AA)
        else:
            self.wave = wavelengths.copy()

        utils.validate_wavelengths(self.wave)

        if self.wave.value.shape != self.flux.value.shape:
            raise exceptions.SynphotError(
                'Fluxes expected to have shape of {0} but has shape of '
                '{1}'.format(self.wave.value.shape, self.flux.value.shape))

        if area is None:
            self.primary_area = None
        else:
            self.primary_area = units.validate_quantity(area, units.AREA)

        self.metadata = header
        if 'expr' not in self.metadata:
            self.metadata['expr'] = self.__class__.__name__

    def _validate_flux_unit(self, new_unit):
        """Check flux unit before conversion."""
        pass  # To be implemented by child classes

    def _validate_flux_value(self):
        """Enforce non-negative fluxes if they are not in magnitudes."""

        if self.flux.unit.decompose() != u.mag and self.flux.value.min() < 0:
            idx = np.where(self.flux.value < 0)
            self.flux.value[idx] = 0.0

            warn_str = '{0:d} of {1:d} bins contained negative flux or throughput; they have been set to zero.'.format(len(idx[0]), self.flux.size)
            self.warnings['NegativeFlux'] = warn_str
            log.warn(warn_str)

    def __str__(self):
        """Descriptive info of the object."""
        return self.metadata['expr']

    def merge_wave(self, other, **kwargs):
        """Return the union of the two sets of wavelengths.

        The result is returned as a separate variable instead of
        overwriting attribute because this method is called by
        other method that deals with merging both wavelength and
        flux/throughput. Relevant ``self`` attribute should be updated
        in the calling method to avoid confusion.

        Parameters
        ----------
        other : obj
            Another spectrum object.

        kwargs : dict
            Keywords accepted by :func:`synphot.utils.merge_wavelengths`.

        Returns
        -------
        out_wavelengths : `astropy.units.quantity.Quantity`
            Merged wavelengths in the unit of ``self.wave``.

        """
        # Convert to self.wave unit
        other_wave = units.validate_quantity(
            other.wave, self.wave.unit, equivalencies=units.wave_conversion)

        out_wavelengths = utils.merge_wavelengths(
            self.wave.value, other_wave.value, **kwargs)

        return u.Quantity(out_wavelengths, unit=self.wave.unit)

    def resample(self, wavelengths):
        """Resample flux or throughput to match the given
        wavelengths, using :func:`numpy.interp`.

        Given wavelengths must satisfy
        :func:`synphot.utils.validate_wavelengths`.

        The result is returned as a separate variable instead of
        overwriting attribute because this method is called by
        other method that deals with merging both wavelength and
        flux/throughput. Relevant ``self`` attribute should be updated
        in the calling method to avoid confusion.

        .. warning::

            If given wavelengths fall outside ``self.wave``,
            extrapolation is done. This may compromise the
            quality of the spectrum.

        Parameters
        ----------
        wavelengths : array_like or `astropy.units.quantity.Quantity`
            Wavelength values for resampling. If not a Quantity,
            assumed to be the unit of ``self.wave``.

        Returns
        -------
        resampled_result : `astropy.units.quantity.Quantity`
            Resampled flux or throughput that is in-sync with
            given wavelengths. Might have negative values.

        """
        if not isinstance(wavelengths, u.Quantity):
            wavelengths = u.Quantity(wavelengths, unit=self.wave.unit)

        utils.validate_wavelengths(wavelengths)

        # Interpolation will be done in given wavelength unit, not self
        self_wave = units.validate_quantity(
            self.wave, wavelengths.unit, equivalencies=units.wave_conversion)
        old_wave = self_wave.value
        new_wave = wavelengths.value

        # Check whether given wavelengths are in descending order
        if np.isscalar(new_wave) or new_wave[0] < new_wave[-1]:
            newasc = True
        else:
            new_wave = new_wave[::-1]
            newasc = False

        # Interpolation flux/throughput
        if old_wave[0] < old_wave[-1]:
            oldasc = True
            resampled_result = np.interp(new_wave, old_wave, self.flux.value)
        else:
            oldasc = False
            rev = np.interp(new_wave, old_wave[::-1], self.flux.value[::-1])
            resampled_result = rev[::-1]

        # If the new and old wavelengths do not have the same parity,
        # the answer has to be flipped again.
        if newasc != oldasc:
            resampled_result = resampled_result[::-1]

        return u.Quantity(resampled_result, unit=self.flux.unit)

    def _operate_on(self, other, op_type):
        """Perform given operation between self and other
        spectra/scalar value.

        Addition and subtraction are done in the units of
        ``self``. Multiplication is only allowed if either
        self or other is unitless or scalar. Division is
        only allowed if other is unitless or scalar.
        Operation between mag and linear flux is not allowed.

        New spectrum object:

            #. has same units as ``self``
            #. inherits metadata from both, with ``self`` having
               higher priority
            #. does *not* inherit old warnings (they are thrown away)

        Parameters
        ----------
        other : obj or number
            The other spectrum or scalar value to operate on.

        op_type : {'+', '-', '*', '/'}
            Allowed operations:
                * '+' - :math:`self + other`
                * '-' - :math:`self - other`
                * '*' - :math:`self * other`
                * '/' - :math:`self / other`

        Returns
        -------
        newspec : obj
            Resultant spectrum, same class and units as ``self``.

        Raises
        ------
        synphot.exceptions.SynphotError
            If operation type not supported.

        synphot.exceptions.IncompatibleSources
            If self and other are not compatible.

        """
        # Scalar operation
        if isinstance(other, (int, long, float)):
            is_scalar_op = True
            new_wave = self.wave
            resamp_flux_1 = self.flux

            # So Astropy Quantity will not crash
            if op_type in ('+', '-'):
                resamp_flux_2 = u.Quantity(other, unit=self.flux.unit)
            else:
                resamp_flux_2 = other

        # Spectra operation
        elif isinstance(other, BaseSpectrum):
            is_scalar_op = False

            if self.primary_area != other.primary_area:
                raise exceptions.IncompatibleSources(
                    'Areas covered by flux are not the same: {0}, {1}'.format(
                        self.primary_area, other.primary_area))

            # Spectrum can only divided by dimensionless value
            if op_type == '/' and other.flux.unit != u.dimensionless_unscaled:
                raise exceptions.IncompatibleSources(
                    'The other spectrum must be dimensionless in / op')

            # Multiplication can only be between spectrum and dimensionless
            if (op_type == '*' and
                  self.flux.unit != u.dimensionless_unscaled and
                  other.flux.unit != u.dimensionless_unscaled):
                raise exceptions.IncompatibleSources(
                    'One of the spectra must be dimensionless in * op')

            # Addition and subtraction cannot mix SourceSpectrum and
            # SpectralElement
            if op_type in ('+', '-') and not isinstance(other, self.__class__):
                raise exceptions.IncompatibleSources(
                    'Cannot perform {0} between {1} and {2}'.format(
                        op_type, self.__class__.__name__,
                        other.__class__.__name__))

            # Operation between mag and linear flux is not allowed
            if ((self.flux.unit.decompose() == u.mag and
                   other.flux.unit.decompose() not in
                   (u.dimensionless_unscaled, u.mag)) or
                  (self.flux.unit.decompose() != u.mag and
                   other.flux.unit.decompose() == u.mag)):  # pragma: no cover
                raise exceptions.IncompatibleSources(
                    'Operation between mag and linear flux is not allowed')

            # Merged wavelengths in self.wave.unit
            new_wave = self.merge_wave(other)

            # Resampled self.flux in self.flux.unit
            resamp_flux_1 = self.resample(new_wave)

            if op_type in ('+', '-'):
                # Convert to self.flux.unit
                other2 = deepcopy(other)
                other2.convert_flux(self.flux.unit)
                resamp_flux_2 = other2.resample(new_wave)
            else:
                # Retain other.flux.unit
                resamp_flux_2 = other.resample(new_wave)

        else:
            raise exceptions.IncompatibleSources(
                'other is not a number or a spectrum object')

        # Perform operation on the flux quantities
        if op_type == '+':
            result = resamp_flux_1 + resamp_flux_2
        elif op_type == '-':
            result = resamp_flux_1 - resamp_flux_2
        elif op_type == '*':
            result = resamp_flux_1 * resamp_flux_2
        elif op_type == '/':
            result = resamp_flux_1 / resamp_flux_2
        else:  # pragma: no cover
            raise exceptions.SynphotError(
                'Operation type {0} not supported'.format(op_type))

        # Merge metadata (self overwrites other if duplicate exists)
        if is_scalar_op:
            new_metadata = {}
        else:
            new_metadata = deepcopy(other.metadata)

        new_metadata.update(self.metadata)
        del new_metadata['expr']  # Let init re-assign this

        return self.__class__(new_wave, result, area=self.primary_area,
                              header=new_metadata)

    def __add__(self, other):
        """Add self with other."""
        return self._operate_on(other, '+')

    def __sub__(self, other):
        """Subtract other from self."""
        return self._operate_on(other, '-')

    def __mul__(self, other):
        """Multiply self and other."""
        return self._operate_on(other, '*')

    def __rmul__(self, other):
        """This is only called if ``other.__mul__`` cannot operate."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide self by other."""
        return self._operate_on(other, '/')

    def convert_wave(self, out_wave_unit):
        """Convert ``self.wave`` to a different unit.
        The attribute is updated in-place.

        Parameters
        ----------
        out_wave_unit : str or `astropy.units.core.Unit`
            Output wavelength unit.

        """
        self.wave = units.validate_quantity(
            self.wave, out_wave_unit, equivalencies=units.wave_conversion)

    def integrate(self, wavelengths=None):
        """Perform trapezoid integration.

        If a wavelength range is provided, flux is first resampled
        with :func:`resample` and then integrated. Otherwise,
        the entire range is used.

        Parameters
        ----------
        wavelengths : array_like, `astropy.units.quantity.Quantity`, or `None`
            Wavelength values for integration. If not a Quantity,
            assumed to be the unit of ``self.wave``. If `None`,
            ``self.wave`` is used.

        Returns
        -------
        result : `astropy.units.quantity.Quantity`
            Integrated result in ``self.flux`` unit.
            It is zero if wavelengths are invalid.

        """
        if wavelengths is None:
            x = self.wave.value
            y = self.flux.value
        else:
            y = self.resample(wavelengths).value
            if isinstance(wavelengths, u.Quantity):
                x = wavelengths.value
            else:
                x = wavelengths

        result = utils.trapezoid_integration(x, y)

        return u.Quantity(result, unit=self.flux.unit)

    def check_overlap(self, other, threshold=0.01):
        """Check for wavelength overlap between two spectra.

        For `synphot.spectrum.SpectralElement` objects, only
        wavelengths where the throughput is non-zero are
        considered.

        Parameters
        ----------
        other : obj
            Another spectrum object.

        threshold : float
            If less than this fraction of flux or throughput falls
            outside wavelength overlap, the *lack* of overlap is
            *insignificant*. This is only used when partial overlap
            is detected. Default is 1%.

        Returns
        -------
        result : {'full', 'partial_most', 'partial_notmost', 'none'}
            * 'full' - ``self.wave`` is within or same as ``other.wave``
            * 'partial_most' - Less than ``threshold`` fraction of
                  ``self`` flux is outside the overlapping wavelength
                  region, i.e., the *lack* of overlap is *insignificant*
            * 'partial_notmost' - ``self.wave`` partially overlaps with
                  ``other.wave`` but does not qualify for 'partial_most'
            * 'none' - ``self.wave`` does not overlap ``other.wave``

        """
        # Get the wavelength arrays
        waves = [x.wave[x.thru.value != 0] if isinstance(x, SpectralElement)
                 else x.wave for x in (self, other)]

        # Convert other wave unit to self wave unit, and extract values
        a = waves[0].value
        b = units.validate_quantity(
            waves[1], waves[0].unit, equivalencies=units.wave_conversion).value

        # Do the comparison
        result = utils.overlap_status(a, b)

        if result == 'partial':
            lorange = sorted([a.min(), b.min()])
            hirange = sorted([a.max(), b.max()])

            # Get the full throughput
            totalflux = self.integrate().value
            utils.validate_totalflux(totalflux)

            # Now get the other two pieces
            idxs = [np.searchsorted(self.wave.value, lorange, 'left'),
                    np.searchsorted(self.wave.value, hirange, 'left')]
            excluded = 0.0
            for idx in idxs:
                wave = self.wave[slice(*idx)]
                if wave.size > 0:
                    excluded += self.integrate(wavelengths=wave).value

            if excluded / totalflux < threshold:
                result = 'partial_most'
            else:
                result = 'partial_notmost'

        return result

    def trim_spectrum(self, min_wave, max_wave):
        """Create a trimmed spectrum with given wavelength limits.

        Parameters
        ----------
        min_wave, max_wave : number or `astropy.units.quantity.Quantity`
            Wavelength limits, inclusive.
            If not a Quantity, assumed to be in ``self.wave.unit``.

        Returns
        -------
        newspec : obj
            Trimmed spectrum in same units as ``self``.

        """
        wave_limits = [units.validate_quantity(
                w, self.wave.unit, equivalencies=units.wave_conversion)
                       for w in (min_wave, max_wave)]
        minw = wave_limits[0].value
        maxw = wave_limits[1].value

        mask = (self.wave.value >= minw) & (self.wave.value <= maxw)
        new_wave = self.wave[mask]
        new_flux = self.flux[mask]

        return self.__class__(new_wave, new_flux, area=self.primary_area,
                              header=deepcopy(self.metadata))

    def taper(self):
        """Taper the spectrum by adding zero flux or throughput
        to each end.

        The wavelengths to use for the first and last points are
        calculated by using the same ratio as for the 2 interior points.

        Skipped if ends are already zeros. Attributes are updated in-place.

        """
        wave_value = self.wave.value
        flux_value = self.flux.value
        has_insertion = False

        if flux_value[0] != 0:
            has_insertion = True
            wave_value = np.insert(wave_value, 0,
                                   wave_value[0] ** 2 / wave_value[1])
            flux_value = np.insert(flux_value, 0, 0.0)

        if flux_value[-1] != 0:
            has_insertion = True
            wave_value = np.insert(wave_value, wave_value.size,
                                   wave_value[-1] ** 2 / wave_value[-2])
            flux_value = np.insert(flux_value, flux_value.size, 0.0)

        if has_insertion:
            self.wave = u.Quantity(wave_value, unit=self.wave.unit)
            self.flux = u.Quantity(flux_value, unit=self.flux.unit)

    def plot(self, overplot_data=None, xlog=False, ylog=False,
             left=None, right=None, bottom=None, top=None,
             show_legend=True, data_labels=('Spectrum data', 'User data'),
             xlabel='', ylabel='', title='', save_as=''):  # pragma: no cover
        """Plot the spectrum.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        overplot_data : tuple of array_like
            Another ``(wave, flux)`` pair to overplot.
            Assumed to be in ``self`` units.

        xlog, ylog : bool
            Plot X and Y axes, respectively, in log scale.
            Default is linear scale.

        left, right : `None` or number
            Minimum and maximum wavelengths to plot.
            If `None`, uses the whole range. If a number is given,
            must be in ``self`` wavelength unit.

        bottom, top : `None` or number
            Minimum and maximum flux/throughput to plot.
            If `None`, uses the whole range. If a number is given,
            must be in ``self`` flux/throughput unit.

        show_legend : bool
            Display legend (automatically positioned).

        data_labels : tuple of str
            Data labels for legend. Only used if ``show_legend=True``.

        xlabel, ylabel : str
            Labels for X and Y axes. By default, they are based on
            data units.

        title : str
            Custom plot title. By default, 'expr' from metadata
            is displayed.

        save_as : str
            Save the plot to an image file. The file type is
            automatically determined by given file extension.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        import matplotlib.pyplot as plt

        if overplot_data is not None:
            other_wave = overplot_data[0]
            other_flux = overplot_data[1]

        # Lower wavelength limit
        if left is None:
            left = self.wave.value.min()
        elif not isinstance(left, (int, long, float)):
            raise exceptions.SynphotError(
                '{0} must be a number'.format(left))

        # Upper wavelength limit
        if right is None:
            right = self.wave.value.max()
        elif not isinstance(right, (int, long, float)):
            raise exceptions.SynphotError(
                '{0} must be a number'.format(right))

        # Lower flux/throughput limit
        if bottom is None:
            bottom = self.flux.value.min()
        elif not isinstance(bottom, (int, long, float)):
            raise exceptions.SynphotError(
                '{0} must be a number'.format(bottom))

        # Upper flux/throughput limit
        if top is None:
            top = self.flux.value.max()
        elif not isinstance(top, (int, long, float)):
            raise exceptions.SynphotError(
                '{0} must be a number'.format(top))

        fig, ax = plt.subplots()

        if not xlabel:
            if self.wave.unit.physical_type == 'frequency':
                xlabel = 'Frequency ({0})'.format(self.wave.unit)
            elif self.wave.unit.physical_type == 'wavenumber':
                xlabel = 'Wave number ({0})'.format(self.wave.unit)
            else:  # length
                xlabel = 'Wavelength ({0})'.format(self.wave.unit)
        if not ylabel:
            if self.flux.unit == u.dimensionless_unscaled:
                ylabel = 'Throughput'
            else:
                ylabel = 'Flux ({0})'.format(self.flux.unit)
        if not title:
            title = self.metadata['expr']

        ax.plot(self.wave.value, self.flux.value, label=data_labels[0])
        if overplot_data is not None:
            ax.plot(other_wave, other_flux, label=data_labels[1])
        ax.set_xlim(left, right)
        ax.set_ylim(bottom, top)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        if xlog:
            ax.set_xscale('log')
        if ylog:
            ax.set_yscale('log')

        if show_legend:
            ax.legend(loc='best')

        plt.draw()

        if save_as:
            plt.savefig(save_as)
            log.info('Plot saved as {0}'.format(save_as))


class BaseUnitlessSpectrum(BaseSpectrum):
    """Base class for unitless spectrum that should not be used directly.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Values for the unitless component (hereafter, known as throughput)
    must be dimensionless. They are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    throughput : array_like or `astropy.units.quantity.Quantity`
        Throughput values. Must be dimensionless.
        If not a Quantity, assumed to be in THROUGHPUT.

    kwargs : dict
        Keywords accepted by `BaseSpectrum`, except ``flux_unit``.

    Attributes
    ----------
    wave, thru : `astropy.units.quantity.Quantity`
        Wavelength and throughput of the spectrum.

    primary_area : `astropy.units.quantity.Quantity` or `None`
        Area that flux covers in cm^2.

    metadata : dict
        Metadata. ``self.metadata['expr']`` must contain a descriptive string of the object.

    warnings : dict
        List of warnings related to spectrum object.

    Raises
    ------
    synphot.exceptions.SynphotError
        If wavelengths and throughput do not match, or if they have
        invalid units.

    synphot.exceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    def __init__(self, wavelengths, throughput, **kwargs):
        kwargs['flux_unit'] = units.THROUGHPUT
        BaseSpectrum.__init__(self, wavelengths, throughput, **kwargs)

        # Rename attribute to avoid confusion. They are interchangable.
        self.thru = self.flux

    def _validate_flux_unit(self, new_unit):
        """Check throughput unit, which must be dimensionless."""
        new_unit = units.validate_unit(new_unit)
        if new_unit.decompose() != u.dimensionless_unscaled:
            raise exceptions.SynphotError(
                'Throughput unit {0} is not dimensionless'.format(new_unit))

    def __mul__(self, other):
        """If other is a SourceSpectrum, result is a SourceSpectrum,
        not a BaseUnitlessSpectrum.

        """
        if isinstance(other, SourceSpectrum):
            return other.__mul__(self)
        else:
            return BaseSpectrum.__mul__(self, other)

    def convert_flux(self, out_flux_unit):
        """This merely returns ``self.thru``."""
        return self.thru

    def taper(self):
        """Taper the spectrum by adding zero flux or throughput
        to each end.

        The wavelengths to use for the first and last points are
        calculated by using the same ratio as for the 2 interior points.

        Skipped if ends are already zeros. Attributes are updated in-place.

        """
        BaseSpectrum.taper(self)
        self.thru = self.flux


class SourceSpectrum(BaseSpectrum):
    """Class to handle a source spectrum.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Fluxes, if not magnitudes, are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    fluxes : array_like or `astropy.units.quantity.Quantity`
        Flux values. If not a Quantity, assumed to be in FLAM.

    kwargs : dict
        Keywords accepted by `BaseSpectrum`.

    Attributes
    ----------
    wave, flux : `astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

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
    def __init__(self, wavelengths, fluxes, **kwargs):
        BaseSpectrum.__init__(self, wavelengths, fluxes, **kwargs)

    def _validate_flux_unit(self, new_unit):
        """Check flux unit before conversion."""
        new_unit = units.validate_unit(new_unit)
        unit_name = new_unit.to_string()
        unit_type = new_unit.physical_type

        # These have 'unknown' physical type.
        # Only linear flux density is supported in the calculations.
        acceptable_unknown_units = (
            units.PHOTLAM.to_string(), units.PHOTNU.to_string(),
            units.FLAM.to_string())

        if (unit_name not in acceptable_unknown_units and
                unit_type != 'spectral flux density'):
            raise exceptions.SynphotError(
                '{0} cannot operate in {1}, use '
                'synphot.spectrum.convert_fluxes() to convert flux to '
                'PHOTLAM, PHOTNU, FLAM, FNU, or Jy first.'.format(
                    self.__class__.__name__, unit_name))

    def add_mag(self, mag):
        """Add a scalar magnitude to flux.

        .. math::

            result = flux_{linear} * 10^{-0.4 * mag}

            result = flux_{mag} + mag

        Parameters
        ----------
        mag : number or `astropy.units.quantity.Quantity`
            Scalar magnitude to add.

        Returns
        -------
        newspec : obj
            Resultant spectrum, same class and units as ``self``.

        Raises
        ------
        synphot.exceptions.SynphotError
            Magnitude is invalid.

        """
        if isinstance(mag, u.Quantity):
            magval = mag.value
            is_mag = mag.unit.decompose() == u.mag
        else:
            magval = mag
            is_mag = True

        if not isinstance(magval, (int, long, float)) or not is_mag:
            raise exceptions.SynphotError(
                '{0} cannot be added to spectrum'.format(mag))

        if self.flux.unit.decompose() == u.mag:  # pragma: no cover
            newspec = self.__add__(magval)
        else:
            newspec = self.__mul__(10**(-0.4 * magval))

        return newspec

    def convert_flux(self, out_flux_unit):
        """Convert ``self.flux`` to a different unit.
        The attribute is updated in-place.

        See :func:`convert_fluxes` for more details.

        Parameters
        ----------
        out_flux_unit : str or `astropy.units.core.Unit`
            Output flux unit.

        """
        self._validate_flux_unit(out_flux_unit)
        self.flux = convert_fluxes(self.wave, self.flux, out_flux_unit,
                                   area=self.primary_area, vegaspec=None)

    def apply_redshift(self, z):
        """Return a new spectrum with redshifted wavelengths.

        .. math::

            \\lambda_{obs} = (1 + z) * \\lambda_{rest}

            \\nu_{obs} = \\frac{\\nu_{rest}}{1 + z}

        .. note::

            Wave number has the same formula as :math:`\\nu`.

        Parameters
        ----------
        z : float
            Redshift to apply.

        Returns
        -------
        newspec : obj
            Spectrum with redshifted wavelengths, same class and
            units as ``self``.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid redshift value.

        """
        if not isinstance(z, (int, long, float)):
            raise exceptions.SynphotError('Redshift must be a number.')

        wave_type = self.wave.unit.physical_type
        fac = 1.0 + z

        if wave_type == 'length':
            new_wave = self.wave * fac
        else:  # frequency or wavenumber
            new_wave = self.wave / fac

        new_metadata = deepcopy(self.metadata)
        new_metadata['expr'] = '{0} at z={1}'.format(str(self), z)

        return self.__class__(new_wave, self.flux, area=self.primary_area,
                              header=new_metadata)

    @classmethod
    def from_file(cls, filename, area=None, **kwargs):
        """Creates a spectrum object from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Spectrum filename.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by
            :func:`synphot.io.read_fits_spec` (if FITS) or
            :func:`synphot.io.read_ascii_spec` (if ASCII).

        Returns
        -------
        newspec : obj
            New spectrum object.

        """
        header, wavelengths, fluxes = io.read_spec(filename, **kwargs)
        return cls(wavelengths, fluxes, area=area, header=header)

    def to_fits(self, filename, **kwargs):
        """Write the spectrum to a FITS file.

        Parameters
        ----------
        filename : str
            Output filename.

        kwargs : dict
            Keywords accepted by :func:`synphot.io.write_fits_spec`.

        """
        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {
            'expr': (str(self), 'synphot expression'),
            'tdisp1': 'G15.7',
            'tdisp2': 'G15.7' }

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        io.write_fits_spec(filename, self.wave, self.flux, **kwargs)

    @classmethod
    def from_vega(cls, area=None, **kwargs):
        """Load :ref:`Vega spectrum <synphot-vega-spec>`.

        Parameters
        ----------
        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by :func:`synphot.io.read_remote_spec`.

        Returns
        -------
        vegaspec : obj
            Vega spectrum.

        """
        filename = config.VEGA_FILE()
        header, wavelengths, fluxes = io.read_remote_spec(filename, **kwargs)
        header['expr'] = 'Vega from {0}'.format(os.path.basename(filename))
        header['filename'] = filename
        return cls(wavelengths, fluxes, area=area, header=header)

    @classmethod
    def from_flat_spectrum(cls, flux_unit, area=None):
        """Create a :ref:`flat spectrum <synphot-flat-spec>`.

        Wavelengths are automatically generated by
        :func:`synphot.utils.generate_wavelengths` and
        converted to Angstrom.

        Parameters
        ----------
        flux_unit : str or `astropy.units.core.Unit`
            Flux unit of flat spectrum.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        Returns
        -------
        flatspec : obj
            Flat spectrum in given flux unit.

        Raises
        ------
        synphot.exceptions.SynphotError
            Flat spectrum is not defined for given flux unit.

        """
        flux_unit = units.validate_unit(flux_unit)
        flux_unit_name = flux_unit.to_string()
        wavelengths = utils.generate_wavelengths(wave_unit=u.AA)[0]
        flux_value = np.empty(wavelengths.size)

        # Magnitude flux-density units
        if flux_unit_name == units.STMAG.to_string():
            x = convert_fluxes(1, u.Quantity(0, units.STMAG), units.FLAM)
            flux_value.fill(x.value)
            fluxes = u.Quantity(flux_value, unit=x.unit)

        elif flux_unit_name == units.ABMAG.to_string():
            x = convert_fluxes(1, u.Quantity(0, units.ABMAG), units.FNU)
            flux_value.fill(x.value)
            fluxes = u.Quantity(flux_value, unit=x.unit)

        # Linear flux-density units
        elif (flux_unit.physical_type == 'spectral flux density' or
              flux_unit_name in (
                units.PHOTLAM.to_string(), units.PHOTNU.to_string(),
                units.FLAM.to_string())):
            flux_value.fill(1.0)
            fluxes = u.Quantity(flux_value, unit=flux_unit)

        else:
            raise exceptions.SynphotError(
                'No standard spectrum available for {0}'.format(flux_unit_name))

        header = {
            'expr': 'Flat spectrum for {0}'.format(flux_unit_name)}

        return cls(wavelengths, fluxes, area=area, header=header)

    def renorm(self, renorm_val, band, force=False, vegaspec=None):
        """Renormalize the spectrum to the given Quantity and band.

        Parameters
        ----------
        renorm_val : number or `astropy.units.quantity.Quantity`
            Value to renormalize the spectrum to. If not a Quantity,
            assumed to be in ``self.flux.unit``.

        band : `synphot.spectrum.SpectralElement`
            Spectrum of the passband to use in renormalization.

        force : bool
            By default (`False`), renormalization is only done
            when band wavelength limits are within ``self``
            or at least 99% of the flux is within the overlap.
            Set to `True` to force renormalization for partial overlap.
            Disjoint passband raises an exception regardless.

        vegaspec : `synphot.spectrum.SourceSpectrum`
            Vega spectrum from :func:`SourceSpectrum.from_vega`.
            This is *only* used if flux is renormalized to VEGAMAG.

        Returns
        -------
        newsp : obj
            Renormalized spectrum in units of ``self``.

        Raises
        ------
        synphot.exceptions.DisjointError
            Renormalization band does not overlap with ``self``.

        synphot.exceptions.OverlapError
            Renormalization band only partially overlaps with ``self``
            and significant amount of flux falls outside the overlap.

        synphot.exceptions.SynphotError
            Invalid inputs or calculation failed.

        """
        if not isinstance(band, SpectralElement):
            raise exceptions.SynphotError(
                'Renormalization passband must be a SpectralElement.')

        # Validate the overlap.
        stat = band.check_overlap(self)
        warnings = {}

        if stat == 'none':
            raise exceptions.DisjointError(
                'Spectrum and renormalization band are disjoint.')

        elif stat == 'partial_most':
            warn_str = (
                'Spectrum is not defined everywhere in renormalization' +
                'passband. At least 99% of the band throughput has' +
                'data. Spectrum will be extrapolated at constant value.')
            warnings['PartialRenorm'] = warn_str
            log.warn(warn_str)

        elif stat == 'partial_notmost':
            if force:
                warn_str = (
                    'Spectrum is not defined everywhere in renormalization' +
                    'passband. Less than 99% of the band throughput has' +
                    'data. Spectrum will be extrapolated at constant value.')
                warnings['PartialRenorm'] = warn_str
                log.warn(warn_str)
            else:
                raise exceptions.OverlapError(
                    'Spectrum and renormalization band do not fully overlap.'
                    'You may use force=True to force the renormalization to '
                    'proceed.')

        elif stat != 'full':  # pragma: no cover
            raise exceptions.SynphotError(
                'Overlap result of {0} is unexpected'.format(stat))

        if not isinstance(renorm_val, u.Quantity):
            renorm_val = u.Quantity(renorm_val, unit=self.flux.unit)

        renorm_unit_name = renorm_val.unit.to_string()

        # Compute the flux of the spectrum through the passband
        sp = self.__mul__(band)

        # Special handling for non-density units
        if renorm_unit_name in (u.count.to_string(), units.OBMAG.to_string()):
            stdflux = 1.0
            flux_tmp = convert_fluxes(
                sp.wave, sp.flux, u.count, area=sp.primary_area)
            totalflux = flux_tmp.sum()

        # Flux density units and VEGAMAG
        else:
            totalflux = sp.integrate()

            # Get the standard unit spectrum in the renormalization units.
            if renorm_unit_name == units.VEGAMAG.to_string():
                if not isinstance(vegaspec, SourceSpectrum):
                    raise exceptions.SynphotError(
                        'Vega spectrum is missing.')
                stdspec = vegaspec
            else:
                stdspec = SourceSpectrum.from_flat_spectrum(
                    renorm_val.unit, area=self.primary_area)

            up = stdspec * band
            up.convert_flux(totalflux.unit)
            stdflux = up.integrate().value

        utils.validate_totalflux(totalflux.value)

        # Renormalize in magnitudes
        if renorm_val.unit.decompose() == u.mag:
            const = renorm_val.value + 2.5 * np.log10(totalflux.value / stdflux)
            newsp = self.add_mag(const)

        # Renormalize in linear flux units
        else:
            const = renorm_val.value * (stdflux / totalflux.value)
            newsp = self.__mul__(const)

        newsp.warnings.update(warnings)
        return newsp

    @classmethod
    def from_gaussian(cls, total_flux, center, fwhm, area=None):
        """Create spectrum from :ref:`Gaussian source <synphot-gaussian>`.

        Wavelength increment is :math:`0.1 * \\sigma`, with limits
        set at 50 times the increment from center. Therefore, the
        wavelength array has 100 values.

        .. warning::

            Behaviors in frequency and wave number space are untested.

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
        newspec : obj
            Spectrum from Gaussian source.

        """
        if not isinstance(total_flux, u.Quantity):
            total_flux = u.Quantity(total_flux, unit=units.FLAM)
        if not isinstance(center, u.Quantity):
            center = u.Quantity(center, unit=u.AA)

        fwhm = units.validate_quantity(
            fwhm, center.unit, equivalencies=units.wave_conversion)
        sigma = fwhm / np.sqrt(8.0 * np.log(2.0))
        factor = total_flux / (np.sqrt(2.0 * np.pi) * sigma.value)

        # Calculate wavelength
        dw = 0.1 * sigma
        first = center - 50.0 * dw
        last = center + 50.0 * dw
        wavelengths = u.Quantity(np.arange(first.value, last.value, dw.value),
                                 unit=center.unit)

        # Calculate flux
        fluxes = factor * np.exp(-0.5 * ((wavelengths - center) / sigma)**2)

        header = {
            'expr': 'Gaussian: mu={0}, fwhm={1}, total_flux={2}'.format(
                center, fwhm, total_flux),
            'center' : center,
            'fwhm' : fwhm,
            'sigma' : sigma,
            'factor' : factor,
            'total_flux' : total_flux }

        return cls(wavelengths, fluxes, area=area, header=header)

    @classmethod
    def from_powerlaw(cls, refwave, index, flux_unit=units.FLAM, area=None):
        """Create a :ref:`power-law spectrum <synphot-powerlaw>`.

        Flux is normalized to 1 in ``flux_units`` at ``refwave``.

        Wavelengths are generated using
        :func:`synphot.utils.generate_wavelengths` in the unit
        of ``refwave``.

        Parameters
        ----------
        refwave : float or `astropy.units.quantity.Quantity`
            Reference wavelength. If not a Quantity, assumed
            to be in Angstrom.

        index : number
            Index of the power law.

        flux_unit : str or `astropy.units.core.Unit`, optional
            Flux unit of the spectrum. Default is FLAM.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        Returns
        -------
        newspec : obj
            Power-law spectrum.

        Raises
        ------
        synphot.exceptions.SynphotError
            Index is invalid.

        """
        flux_unit = units.validate_unit(flux_unit)

        if not isinstance(index, (int, long, float)):
            raise exceptions.SynphotError(
                'Index {0} must be a number.'.format(index))

        if not isinstance(refwave, u.Quantity):
            refwave = u.Quantity(refwave, unit=u.AA)

        # Generate wavelengths
        tmp_wave = utils.generate_wavelengths(wave_unit=u.AA)[0]
        wavelengths = tmp_wave.to(
            refwave.unit, equivalencies=units.wave_conversion)

        # Calculate flux
        fluxes = ((wavelengths / refwave) ** index) * flux_unit

        header = {
            'expr': 'Power law: refwave {0}, index {1}'.format(refwave, index),
            'refwave': refwave,
            'index': index }

        return cls(wavelengths, fluxes, area=area, header=header)

    @classmethod
    def from_blackbody(cls, temperature, flux_unit=units.FLAM, area=None):
        """Create a :ref:`blackbody spectrum <synphot-planck-law>`
        with given temperature.

        Flux is normalized to a star of solar radius at a
        distance of 1 kpc.

        Wavelengths are generated using
        :func:`synphot.utils.generate_wavelengths` in Angstrom.

        Parameters
        ----------
        temperature : float or `astropy.units.quantity.Quantity`
            Blackbody temperature. If not a Quantity, assumed
            to be in Kelvin.

        flux_unit : str or `astropy.units.core.Unit`, optional
            Flux unit of the spectrum. Default is FLAM.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        """
        flux_unit = units.validate_unit(flux_unit)

        if not isinstance(temperature, u.Quantity):
            temperature = u.Quantity(temperature, unit=u.K)

        # Generate wavelengths
        wavelengths = utils.generate_wavelengths(wave_unit=u.AA)[0]

        # Calculate flux and renormalize to 1 R_sun at 1 kpc
        bbflux = planck.bb_photlam(wavelengths, temperature)
        fluxes = convert_fluxes(wavelengths, bbflux, flux_unit, area=area)

        header = {
            'expr': 'BB(T = {0})'.format(temperature),
            'temperature': temperature }

        return cls(wavelengths, fluxes, area=area, header=header)


class SpectralElement(BaseUnitlessSpectrum):
    """Class to handle a spectral element.
    That is, throughput for filter, detector, et cetera.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Throughput values must be dimensionless.
    They are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    throughput : array_like or `astropy.units.quantity.Quantity`
        Throughput values. Must be dimensionless.
        If not a Quantity, assumed to be in THROUGHPUT.

    kwargs : dict
        Keywords accepted by `BaseSpectrum`, except ``flux_unit``.

    Attributes
    ----------
    wave, thru : `astropy.units.quantity.Quantity`
        Wavelength and throughput of the spectrum.

    primary_area : `astropy.units.quantity.Quantity` or `None`
        Area that flux covers in cm^2.

    metadata : dict
        Metadata. ``self.metadata['expr']`` must contain a descriptive string of the object.

    warnings : dict
        List of warnings related to spectrum object.

    Raises
    ------
    synphot.exceptions.SynphotError
        If wavelengths and throughput do not match, or if they have
        invalid units.

    synphot.exceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    def unit_response(self):
        """Calculate :ref:`unit response <synphot-formula-uresp>`
        of this passband.

        Returns
        -------
        uresp : `astropy.units.quantity.Quantity`
            Flux (in FLAM) of a star that produces a response of
            one photon per second in this passband.

        Raises
        ------
        synphot.exceptions.SynphotError
            If ``self.primary_area``, which is compulsory for this
            calculation, is undefined.

        """
        if self.primary_area is None:
            raise exceptions.SynphotError('Area is undefined.')

        # Only correct if wavelengths are in Angstrom.
        wave = self.wave.to(u.AA, equivalencies=units.wave_conversion)

        int_val = utils.trapezoid_integration(
            wave.value, (self.thru * wave).value)
        uresp = units.HC / (self.primary_area.cgs * int_val)

        return u.Quantity(uresp.value, unit=units.FLAM)

    def pivot(self):
        """Calculate :ref:`passband pivot wavelength <synphot-formula-pivwv>`.

        Returns
        -------
        pivwv : `astropy.units.quantity.Quantity`
            Passband pivot wavelength.

        """
        wave = utils.to_length(self.wave)
        num = utils.trapezoid_integration(
            wave.value, self.thru.value * wave.value)
        den = utils.trapezoid_integration(
            wave.value, self.thru.value / wave.value)

        if den == 0:  # pragma: no cover
            pivwv = 0.0
        else:
            val = num / den
            if val < 0:  # pragma: no cover
                pivwv = 0.0
            else:
                pivwv = np.sqrt(val)

        return u.Quantity(pivwv, unit=wave.unit)

    def rmswidth(self, threshold=None):
        """Calculate the passband RMS width as in
        :ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`, page 836.

        Not to be confused with :func:`photbw`.

        Parameters
        ----------
        threshold : float, optional
            Data points with throughput below this value are not
            included in the calculation. By default, all data points
            are included.

        Returns
        -------
        rms_width : `astropy.units.quantity.Quantity`
            RMS width of the passband.

        Raises
        ------
        synphot.exceptions.SynphotError
            Threshold is invalid.

        """
        wave = utils.to_length(self.wave)

        if threshold is None:
            wave = wave
            thru = self.thru
        elif isinstance(threshold, (int, long, float)):
            mask = self.thru.value >= threshold
            wave = wave[mask]
            thru = self.thru[mask]
        else:
            raise exceptions.SynphotError(
                '{0} is not a valid threshold'.format(threshold))

        num = utils.trapezoid_integration(
            wave.value, ((wave - self.avgwave())**2 * thru).value)
        den = self.integrate(wavelengths=wave).value

        if den == 0:  # pragma: no cover
            rms_width = 0.0
        else:
            val = num / den
            if val < 0:  # pragma: no cover
                rms_width = 0.0
            else:
                rms_width = np.sqrt(val)

        return u.Quantity(rms_width, unit=wave.unit)

    def photbw(self, threshold=None):
        """Calculate the
        :ref:`passband RMS width as in IRAF SYNPHOT <synphot-formula-bandw>`.

        This is a compatibility function. To calculate the actual
        passband RMS width, use :func:`rmswidth`.

        Parameters
        ----------
        threshold : float, optional
            Data points with throughput below this value are not
            included in the calculation. By default, all data points
            are included.

        Returns
        -------
        bandw : `astropy.units.quantity.Quantity`
            IRAF SYNPHOT RMS width of the passband.

        Raises
        ------
        synphot.exceptions.SynphotError
            Threshold is invalid.

        """
        wv = utils.to_length(self.wave)
        avg_wave = utils.barlam(wv.value, self.thru.value)

        if threshold is None:
            wave = wv.value
            thru = self.thru.value
        elif isinstance(threshold, (int, long, float)):
            mask = self.thru.value >= threshold
            wave = wv[mask].value
            thru = self.thru[mask].value
        else:
            raise exceptions.SynphotError(
                '{0} is not a valid threshold'.format(threshold))

        # calculate the rms width
        num = utils.trapezoid_integration(
            wave, thru * np.log(wave / avg_wave) ** 2 / wave)
        den = utils.trapezoid_integration(wave, thru / wave)

        if den == 0:  # pragma: no cover
            bandw = 0.0
        else:
            val = num / den
            if val < 0:  # pragma: no cover
                bandw = 0.0
            else:
                bandw = avg_wave * np.sqrt(val)

        return u.Quantity(bandw, unit=wv.unit)

    def fwhm(self, threshold=None):
        """Calculate :ref:`synphot-formula-fwhm` of equivalent gaussian.

        Parameters
        ----------
        threshold : float, optional
            Data points with throughput below this value are not
            included in the calculation. By default, all data points
            are included.

        Returns
        -------
        fwhm_val : `astropy.units.quantity.Quantity`
            FWHM of equivalent gaussian.

        """
        return np.sqrt(8 * np.log(2)) * self.photbw(threshold=threshold)

    def avgwave(self):
        """Calculate the passband average wavelength using
        :func:`synphot.utils.avg_wavelength`.

        Returns
        -------
        avg_wave : `astropy.units.quantity.Quantity`
            Passband average wavelength.

        """
        wave = utils.to_length(self.wave)
        avg_wave = utils.avg_wavelength(wave.value, self.thru.value)
        return u.Quantity(avg_wave, unit=wave.unit)

    def tlambda(self):
        """Calculate throughput at
        :ref:`passband average wavelength <synphot-formula-avgwv>`.

        Returns
        -------
        t_lambda : `astropy.units.quantity.Quantity`
            Throughput at passband average wavelength.

        """
        return self.resample(self.avgwave())

    def tpeak(self):
        """Calculate :ref:`peak bandpass throughput <synphot-formula-tpeak>`.

        Returns
        -------
        tpeak : `astropy.units.quantity.Quantity`
            Peak bandpass throughput.

        """
        return self.thru.max()

    def wpeak(self):
        """Calculate
        :ref:`wavelength at peak throughput <synphot-formula-tpeak>`.

        If there are multiple data points with peak throughput
        value, only the first match is returned.

        Returns
        -------
        wpeak : `astropy.units.quantity.Quantity`
            Wavelength at peak throughput.

        """
        wave = utils.to_length(self.wave)
        return wave[self.thru == self.tpeak()][0]

    def equivwidth(self):
        """Calculate :ref:`passband equivalent width <synphot-formula-equvw>`.

        Returns
        -------
        equvw : `astropy.units.quantity.Quantity`
            Passband equivalent width.

        """
        wave = utils.to_length(self.wave)
        equvw = utils.trapezoid_integration(wave.value, self.thru.value)
        return u.Quantity(equvw, unit=wave.unit)

    def rectwidth(self):
        """Calculate :ref:`passband rectangular width <synphot-formula-rectw>`.

        Returns
        -------
        rectw : `astropy.units.quantity.Quantity`
            Passband rectangular width.

        """
        equvw = self.equivwidth()
        tpeak = self.tpeak()

        if tpeak.value == 0:  # pragma: no cover
            rectw = u.Quantity(0.0, unit=equvw.unit)
        else:
            rectw = equvw / tpeak

        return rectw

    def efficiency(self):
        """Calculate :ref:`dimensionless efficiency <synphot-formula-qtlam>`.

        Returns
        -------
        qtlam : `astropy.units.quantity.Quantity`
            Dimensionless efficiency.

        """
        wave = utils.to_length(self.wave)
        qtlam = utils.trapezoid_integration(
            wave.value, self.thru.value / wave.value)
        return u.Quantity(qtlam, unit=u.dimensionless_unscaled)

    def emflx(self):
        """Calculate
        :ref:`equivalent monochromatic flux <synphot-formula-emflx>`.

        Returns
        -------
        em_flux : `astropy.units.quantity.Quantity`
            Equivalent monochromatic flux in FLAM.

        """
        t_lambda = self.tlambda()

        if t_lambda == 0:  # pragma: no cover
            em_flux = u.Quantity(0.0, unit=units.FLAM)
        else:
            fac = self.tpeak() / t_lambda
            em_flux = self.unit_response() * self.rectwidth().value * fac

        return em_flux

    @classmethod
    def from_file(cls, filename, area=None, **kwargs):
        """Creates a throughput object from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Throughput filename.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by
            :func:`synphot.io.read_fits_spec` (if FITS) or
            :func:`synphot.io.read_ascii_spec` (if ASCII).

        Returns
        -------
        newspec : obj
            New throughput object.

        """
        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = units.THROUGHPUT

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'THROUGHPUT'

        header, wavelengths, throughput = io.read_spec(filename, **kwargs)
        return cls(wavelengths, throughput, area=area, header=header)

    def to_fits(self, filename, **kwargs):
        """Write the spectrum to a FITS file.

        Throughput column is automatically named 'THROUGHPUT'.

        Parameters
        ----------
        filename : str
            Output filename.

        kwargs : dict
            Keywords accepted by :func:`synphot.io.write_fits_spec`.

        """
        kwargs['flux_col'] = 'THROUGHPUT'
        kwargs['flux_unit'] = units.THROUGHPUT

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'expr': (str(self), 'synphot expression'),
                 'tdisp1': 'G15.7',
                 'tdisp2': 'G15.7'}

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        io.write_fits_spec(filename, self.wave, self.thru, **kwargs)

    @classmethod
    def from_box(cls, center, width, step=0.05, area=None):
        """Create a box passband with given central wavelength and width.

        Parameters
        ----------
        center : float or `astropy.units.quantity.Quantity`
            Central wavelength of the passband. If not a Quantity,
            assumed to be in Angstrom.

        width : float or `astropy.units.quantity.Quantity`
            Width of the passband. If not a Quantity, assumed to be
            in the unit of ``center``.

        step : float or `astropy.units.quantity.Quantity`
            Linear wavelength spacing. If not a Quantity, assumed
            to be in the unit of ``center``.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        Returns
        -------
        newspec : obj
            Box-shaped passband.

        """
        if not isinstance(center, u.Quantity):
            center = u.Quantity(center, unit=u.AA)

        width = units.validate_quantity(
            width, center.unit, equivalencies=units.wave_conversion)
        step = units.validate_quantity(
            step, center.unit, equivalencies=units.wave_conversion)

        # Generate wavelengths
        half_width = width / 2.0
        lower = center - half_width - step
        upper = center + half_width + step
        wave_value = np.arange(
            lower.value, upper.value, step.value, dtype=np.float64)
        wavelengths = u.Quantity(wave_value, unit=center.unit)

        # Generate throughput
        thru_value = np.ones(wavelengths.shape, dtype=np.float64)
        thru_value[0] = 0.0
        thru_value[-1] = 0.0
        throughput = u.Quantity(thru_value, unit=units.THROUGHPUT)

        header = {
            'expr': 'Box at {0} ({1} wide)'.format(center, width),
            'box_center': center,
            'box_width': width }

        return cls(wavelengths, throughput, area=area, header=header)

    @classmethod
    def from_filter(cls, filtername, area=None, **kwargs):
        """Load :ref:`pre-defined filter passband <synphot-passband-create>`.

        Parameters
        ----------
        filtername : {'bessel_j', 'bessel_h', 'bessel_k', 'cousins_r', 'cousins_i', 'johnson_u', 'johnson_b', 'johnson_v', 'johnson_r', 'johnson_i', 'johnson_j', 'johnson_k'}
            Filter name.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by :func:`synphot.io.read_remote_spec`.

        Returns
        -------
        newspec : obj
            Passband object for the given filter.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid filter name.

        """
        filtername = filtername.lower()

        # Select filename based on filter name
        if filtername == 'bessel_j':
            cfgitem = config.BESSEL_J_FILE
        elif filtername == 'bessel_h':
            cfgitem = config.BESSEL_H_FILE
        elif filtername == 'bessel_k':
            cfgitem = config.BESSEL_K_FILE
        elif filtername == 'cousins_r':
            cfgitem = config.COUSINS_R_FILE
        elif filtername == 'cousins_i':
            cfgitem = config.COUSINS_I_FILE
        elif filtername == 'johnson_u':
            cfgitem = config.JOHNSON_U_FILE
        elif filtername == 'johnson_b':
            cfgitem = config.JOHNSON_B_FILE
        elif filtername == 'johnson_v':
            cfgitem = config.JOHNSON_V_FILE
        elif filtername == 'johnson_r':
            cfgitem = config.JOHNSON_R_FILE
        elif filtername == 'johnson_i':
            cfgitem = config.JOHNSON_I_FILE
        elif filtername == 'johnson_j':
            cfgitem = config.JOHNSON_J_FILE
        elif filtername == 'johnson_k':
            cfgitem = config.JOHNSON_K_FILE
        else:
            raise exceptions.SynphotError(
                'Filter name {0} is invalid.'.format(filtername))

        filename = cfgitem()

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = units.THROUGHPUT

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'THROUGHPUT'

        header, wavelengths, throughput = io.read_remote_spec(filename,
                                                                  **kwargs)
        header['expr'] = filtername
        header['filename'] = filename
        header['descrip'] = cfgitem.description

        return cls(wavelengths, throughput, area=area, header=header)
