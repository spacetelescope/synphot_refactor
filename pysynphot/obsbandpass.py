# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
The ObsBandpass user interface needs to support either the usual
(acs,hrc,f555w) obsmode style that produce a set of chained throughput
files; or something like (johnson,v) that has a single throughput file.
Thus ObsBandpass must be a factory function, returning either an
ObsModeBandpass (ack, terrible name) or a TabularSpectralElement.

"""

from __future__ import division, print_function
import numpy as np

from . import observationmode
from . import spectrum
from . import units
from . import pysynexcept


def ObsBandpass(obstring, graphtable=None, comptable=None, component_dict={}):
    """
    Generate an ObsModeBandPass or TabularSpectralElement instance

    obsband = ObsBandpass(string specifying obsmode; for details
    see the Synphot Data User's Guide at
    http://www.stsci.edu/hst/HST_overview/documents/synphot/hst_synphotTOC.html

    """

    # Temporarily create an Obsmode to determine whether an
    # ObsModeBandpass or a TabularSpectralElement will be returned.
    ob = observationmode.ObservationMode(obstring,
                                         graphtable=graphtable,
                                         comptable=comptable,
                                         component_dict=component_dict)
    if len(ob) > 1:
        return ObsModeBandpass(ob)
    else:
        return spectrum.TabularSpectralElement(ob.components[0].throughput_name)


class ObsModeBandpass(spectrum.CompositeSpectralElement):
    """
    Bandpass instantiated from an obsmode string

    """

    def __init__(self, ob):
        """
        Instantiate a COmpositeSpectralElement by means of an
        ObservationMode (which the caller must have already created from
        an  obstring

        """

        #Chain the individual components
        chain = ob.components[0].throughput*ob.components[1].throughput

        for i in range(2, len(ob)-1):
            chain = chain*ob.components[i].throughput

        spectrum.CompositeSpectralElement.__init__(self,
                                                   chain,
                                                   ob.components[-1].throughput)

        self.obsmode = ob
        self.name = self.obsmode._obsmode  # str(self.obsmode)
        self.primary_area = ob.primary_area

        #Check for valid bounds
        self._checkbounds()

        try:
            self.binset = self.obsmode.bandWave()
        except AttributeError:
            # this is to catch an error raised when the self.obsmode
            # object does not have a binset attribute because of some
            # problem with the obsmode used to instatiate it.
            pass

    def __str__(self):
        """
        Defer to ObservationMode component

        """
        return self.name  # self.obsmode._obsmode

    def __len__(self):
        """
        Defer to ObservationMode component

        """
        return len(self.obsmode)

    def showfiles(self):
        """
        Defer to ObservationMode component

        """
        return self.obsmode.showfiles()

    def _checkbounds(self):
        thru = self.throughput
        if thru[0] != 0 or thru[-1] != 0:
            print("Warning: throughput for this obsmode is not bounded by "
                  "zeros. Endpoints: thru[0]=", thru[0], " thru[-1]=", thru[-1])

    def thermback(self):
        """
        Expose the thermal background calculation presently hidden
        in the obsmode class.
        Only bandpasses for which thermal information has been supplied
        in the graph table supports this method; all others will raise a
        NotImplementedError.

        """

        # The obsmode.ThermalSpectrum method will raise an exception if there is
        # no thermal information, and that will just propagate up.
        sp = self.obsmode.ThermalSpectrum()

        #Thermback is always provided in this non-standard set of units.
        #This code was copied from etc.py.
        ans = sp.integrate() * (self.obsmode.pixscale**2 *
                                self.obsmode.primary_area)
        return ans

    def pixel_range(self, waverange, waveunits=None, round='round'):
        """
        Returns the number of wavelength bins within `waverange`.

        .. note::

           This calls the `pixel_range` function with
           `self.binset` as the first argument. See
           `pixel_range` for full documentation.

        Parameters
        ----------
        waveunits: str, optional
            The units of the wavelengths given in `waverange`. Defaults to None.
            If None, the wavelengths are assumed to be in the units of the
            `waveunits` attribute.

        Raises
        ------
        pysynphot.pysynexcept.UndefinedBinset
            If the `binset` attribute is None.

        See Also
        --------
        pixel_range, pysynphot.pysynexcept.UndefinedBinset

        """
        # make sure we have a binset to work with
        if self.binset is None:
            raise pysynexcept.UndefinedBinset(
                'No binset specified for this bandpass.')

        # start by converting waverange to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)

            if not isinstance(waverange, np.ndarray):
                waverange = np.array(waverange)

            # convert to angstroms and then whatever self.waveunits is
            waverange = waveunits.ToAngstrom(waverange)

            waverange = units.Angstrom().Convert(waverange, self.waveunits.name)

        return pixel_range(self.binset, waverange, round=round)

    def wave_range(self, cenwave, npix, waveunits=None, round='round'):
        """
        Get the wavelength range covered by a number of pixels, `npix`, centered
        on wavelength `cenwave`.

        .. note::

           This calls the `wave_range` function with
           `self.binset` as the first argument. See
           `wave_range` for full documentation.

        Parameters
        ----------
        waveunits: str, optional
            Wavelength units of `cenwave` and the returned wavelength range.
            Defaults to None. If None, the wavelengths are assumed to be in
            the units of the `waveunits` attribute.

        Raises
        ------
        pysynexcept.UndefinedBinset
            If the `binset` attribute is None.

        See Also
        --------
        wave_range, pysynphot.pysynexcept.UndefinedBinset

        """
        # make sure we have a binset to work with
        if self.binset is None:
            raise pysynexcept.UndefinedBinset(
                'No binset specified for this bandpass.')

        # convert cenwave from waveunits to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)

            # convert to angstroms and then whatever self.waveunits is
            cenwave = waveunits.ToAngstrom(cenwave)
            cenwave = units.Angstrom().Convert(cenwave, self.waveunits.name)

        wave1, wave2 = wave_range(self.binset, cenwave, npix, round=round)

        # translate ends to waveunits, if necessary
        if waveunits is not None:
            # convert to angstroms
            wave1 = self.waveunits.ToAngstrom(wave1)
            wave2 = self.waveunits.ToAngstrom(wave2)

            # then to waveunits
            wave1 = units.Angstrom().Convert(wave1, waveunits.name)
            wave2 = units.Angstrom().Convert(wave2, waveunits.name)

        return wave1, wave2


def pixel_range(bins, waverange, round='round'):
    """
    Returns the number of wavelength bins within `waverange`.

    Parameters
    ----------
    bins: ndarray
        Wavelengths of pixel centers. Must be in the same units as `waverange`.

    waverange: array_like
        A sequence containing the wavelength range of interest. Only the
        first and last elements are used. Assumed to be in increasing order.
        Must be in the same units as `bins`.

    round: {'round','min','max',None}, optional
        How to deal with pixels at the edges of the wavelength range. All
        of the options, except None, will return an integer number of pixels.
        Defaults to 'round'.

        When set to 'round' wavelength ends that fall in the middle of a
        pixel are counted if more than half of the pixel is within `waverange`.
        Ends that fall in the center of a pixel are rounded up to the
        nearest pixel edge.

        When set to 'min' only pixels wholly within `waverange` are counted.

        When set to 'max' end pixels that are within `waverange` by any
        margin are counted.

        When set to None the exact number of encompassed pixels, including
        fractional pixels, is returned.

    Returns
    -------
    num: int or float
        Number of wavelength bins within `waverange`.

    Raises
    ------
    ValueError
        If `round` is not an allowed value.

    pysynphot.pysynexcept.OverlapError
        If `waverange` exceeds the bounds of `bins`.

    """
    # make sure that the round keyword is valid
    if round not in ('round', 'min', 'max', None):
        raise ValueError(
            "round keyword must be one of ('round','ciel','floor',None)")

    wave1 = waverange[0]
    wave2 = waverange[-1]

    # make sure the specified waverange is within our .binset
    minwave = bins[0] - (bins[0:2].mean() - bins[0])
    if wave1 < minwave:
        raise pysynexcept.OverlapError(
            "Lower bound of waverange is outside of binset. Min = %f" % minwave)

    maxwave = bins[-1] + (bins[-1] - bins[-2:].mean())
    if wave2 > maxwave:
        raise pysynexcept.OverlapError(
            "Upper bound of waverange is outside of binset. Max = %f" % maxwave)

    # if the wavelength ends are the same return 0
    if wave1 == wave2:
        return 0

    # find where the wavelength endpoints fall.
    if round == 'round':
        ind1 = bins.searchsorted(wave1, side='right')
        ind2 = bins.searchsorted(wave2, side='right')

        num = ind2 - ind1

    elif round == 'min':
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # for ind1, figure out if pixel ind1 is wholly included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (bins[ind1] - wave1) / (bins[ind1] - bins[ind1-1])

        if frac < 0.5:
            # ind1 is only partially included
            ind1 += 1

        # similar but reversed procedure for ind2
        frac = (wave2 - bins[ind2-1]) / (bins[ind2] - bins[ind2-1])

        if frac < 0.5:
            # ind2 is only partially included
            ind2 -= 1

        num = ind2 - ind1

    elif round == 'max':
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # for ind1, figure out if pixel ind1-1 is partially included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (wave1 - bins[ind1-1]) / (bins[ind1] - bins[ind1-1])

        if frac < 0.5:
            # ind1 is partially included
            ind1 -= 1

        # similar but reversed procedure for ind2
        frac = (bins[ind2] - wave2) / (bins[ind2] - bins[ind2-1])

        if frac < 0.5:
            # ind2 is partially included
            ind2 += 1

        num = ind2 - ind1

    elif round is None:
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # calculate fractional indices
        frac1 = ind1 - (bins[ind1] - wave1) / (bins[ind1] - bins[ind1-1])
        frac2 = ind2 - (bins[ind2] - wave2) / (bins[ind2] - bins[ind2-1])

        num = frac2 - frac1

    return num


def wave_range(bins, cenwave, npix, round='round'):
    """
    Get the wavelength range covered by a number of pixels, `npix`, centered
    on wavelength `cenwave`.

    Parameters
    ----------
    bins: ndarray
        Wavelengths of pixel centers. Must be in the same units as
        `cenwave`.

    cenwave: float
        Central wavelength of range. Must be in the same units as `bins`.

    npix: int
        Number of pixels in range, centered on `cenwave`.

    round: {'round','min','max',None}, optional
        How to deal with pixels at the edges of the wavelength range. All
        of the options, except None, will return wavelength ends that
        correpsonds to pixel edges.
        Defaults to 'round'.

        When set to None an exact wavelength range is returned. The
        wavelength ends returned may not correspond to pixel edges, but
        will cover exactly `npix` pixels.

        When set to 'round' a wavelength range is returned such that the
        ends are pixel edges and the range spans exactly `npix` pixels.
        Ends that fall in the center of bins are rounded up to the nearest
        pixel edge.

        When set to 'min' the returned wavelength range is shrunk so that
        it includes an integer number of pixels and the ends fall on pixel
        edges. May not span exactly `npix` pixels.

        When set to 'max' the returned wavelength range is expanded so that
        it includes an integer number of pixels and the ends fall on pixel
        edges. May not span exactly `npix` pixels.

    Returns
    -------
    waverange: tuple of floats
        The range of wavelengths spanned by `npix` centered on `cenwave`.

    Raises
    ------
    ValueError
        If `round` is not an allowed value.

    pysynphot.pysynexcept.OverlapError
        If `cenwave` is not within the `binset` attribute,
        or the returned `waverange` would
        exceed the limits of the `binset` attribute.

    """
    # make sure that the round keyword is valid
    if round not in (None, 'round', 'min', 'max'):
        raise ValueError(
            "round keyword must be one of (None, 'round', 'min', 'max')")

    # make sure cenwave is within binset
    if cenwave < bins[0]:
        raise pysynexcept.OverlapError("cenwave is not within binset. Min = %f"
                                       % bins[0])
    elif cenwave > bins[-1]:
        raise pysynexcept.OverlapError("cenwave is not within binset. Max = %f"
                                       % bins[-1])

    # first figure out what index the central wavelength falls at
    diff = cenwave - bins
    ind = np.where(np.abs(diff) == np.abs(diff).min())[0][0]

    # now figure out the fractional index
    if diff[ind] < 0:
        frac_ind = float(ind) + diff[ind] / (bins[ind] - bins[ind-1])
    elif diff[ind] > 0:
        frac_ind = float(ind) + diff[ind] / (bins[ind+1] - bins[ind])
    else:
        frac_ind = float(ind)

    # then figure out the fractional indices of the ends
    frac_ind1 = frac_ind - npix/2.
    frac_ind2 = frac_ind + npix/2.

    # check ends
    if frac_ind1 < -0.5:
        raise pysynexcept.OverlapError(
            "Lower wavelength range is below allowed binset.")

    if frac_ind2 > bins.shape[0] - 0.5:
        raise pysynexcept.OverlapError(
            "Upper wavelength range is above allowed binset.")

    frac1, int1 = np.modf(frac_ind1)
    frac2, int2 = np.modf(frac_ind2)

    # translate ends to wavelength
    if round is None:
        # translate ends directly to wavelength without regard to bin edges
        f, i = frac1, int1

        wave1 = bins[i] + frac1 * (bins[i+1] - bins[i])

        f, i = frac2, int2

        wave2 = bins[i] + frac2 * (bins[i+1] - bins[i])

    elif round == 'round':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f >= 0:
            # end is somewhere greater than binset[0] so we can just
            # interpolate between two neighboring values going with upper edge
            wave1 = bins[i:i+2].mean()
        else:
            # end is below the lowest binset value, but not by enough to
            # trigger an exception
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if i < bins.shape[0] - 1:
            # end is somewhere below binset[-1] so we can just interpolate
            # between two neighboring values, going with the upper edge.
            wave2 = bins[i:i+2].mean()
        else:
            # end is above highest binset value but not by enough to
            # trigger an exception
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    elif round == 'min':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f <= 0.5 and i < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[i:i+2].mean()
        elif f > 0.5 and i < bins.shape[0] - 2:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[i+1:i+3].mean()
        elif f == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if f >= 0.5 and i < bins.shape[0] - 1:
            # not out at the end and pixel i included
            wave2 = bins[i:i+2].mean()
        elif f < 0.5 and i < bins.shape[0]:
            # not out at end and pixel i not included
            wave2 = bins[i-1:i+1].mean()
        elif f == 0.5 and i == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    elif round == 'max':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f < 0.5 and i < bins.shape[0]:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[i-1:i+1].mean()
        elif f >= 0.5 and i < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[i:i+2].mean()
        elif f == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if f > 0.5 and i < bins.shape[0] - 2:
            # not out at the end and pixel i included
            wave2 = bins[i+1:i+3].mean()
        elif f <= 0.5 and i < bins.shape[0] - 1:
            # not out at end and pixel i not included
            wave2 = bins[i:i+2].mean()
        elif f == 0.5 and i == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    return wave1, wave2
