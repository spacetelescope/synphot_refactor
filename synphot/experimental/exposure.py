# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module is a wrapper for synphot's most commonly used functions.

"""

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import units as u
from astropy.modeling.models import Const1D

# LOCAL
from synphot.models import Empirical1D
from synphot.spectrum import SpectralElement
from .observation import Observation, ccd_snr, exptime_from_ccd_snr
from synphot.experimental.skymodel import atmospheric_transmittance
from synphot import exceptions

__all__ = ['Exposure']


AD_ERR_DEFAULT = np.sqrt(0.289) * (u.adu / u.pixel)


class Exposure(object):
    """
    Parameters
    ----------
    source_spec : `~synphot.spectrum.SourceSpectrum`
        The spectrum of the target object scaled by distance (i.e. the
        target spectrum just before interacting with the instrument).
    diameter : `~astropy.units.quantity.Quantity`
        Diameter of the telescope aperture.
    bandpass : str, list with dimension 2 x n containing
        `~astropy.units.quantity.Quantity` values, or
        `~synphot.spectrum.SpectralElement`
        The bandpass(es) of this observation. Can either be specified by a
        string or a list with dimensions 2 x n, where one row is the
        list of wavelengths associated with the bandpass, and the other
        row contains the fractional values of the bandpass.
        Default is a constant model with amplitude = 1, i.e. as if a
        bandpass with perfect throughput were in effect.
    quantum_efficiency : bool or list with dimension 2 x n containing
        `~astropy.units.quantity.Quantity` values
        A model for the quantum efficiency of the instrument's CCD.
        Default is False. If set to True, quantum_efficiency assumes
        a generic silicon CCD response function.
    atmospheric_transmission : bool or list with dimension 2 x n containing
        `~astropy.units.quantity.Quantity` values
        A model for the atmopsheric transmission. Default is False.
        If set to True, atmospheric_transmission queries from SkyCalc
        with default parameters. For more information on SkyCalc, see:
        (http://www.eso.org/observing/etc/bin/gen/form?INS.MODE=
        swspectr+INS.NAME=SKYCALC)
        For more information on the default parameters, see:
        (https://www.eso.org/observing/etc/doc/skycalc/helpskycalccli.
        html#skycalc-input-parameters)
    force : {None, ‘none’, ‘extrap’, ‘taper’}
        Force the creation of an observation even when source spectrum
        and bandpass do not fully overlap:

            * `None` or 'none' - Source must encompass bandpass (default)
            * 'extrap' - Extrapolate source spectrum (this changes the
              underlying model of ``spec`` to always extrapolate,
              if applicable)
            * 'taper' - Taper source spectrum to zero
    """
    @u.quantity_input(diameter=u.m, exptime=u.s)
    def __init__(self, source_spec, diameter, exptime,
                 bandpass=SpectralElement(Const1D, amplitude=1),
                 quantum_efficiency=False, atmospheric_transmission=False,
                 force=None):
        self.source_spec = source_spec
        self.diameter = diameter
        self.exptime = exptime
        self._bandpass = bandpass
        self._qe = quantum_efficiency
        self._atmo = atmospheric_transmission

        # turn spectrum elements into synphot objects
        self._set_bandpass()

        if type(self._qe) == list:
            self._custom_qe()
        elif self._qe is True:
            self._generic_ccd()

        if type(self._atmo) == list:
            self._custom_atmosphere()
        elif self._atmo is True:
            self.atmospheric_transmission = atmospheric_transmittance()

        self.observation = Observation(self.source_spec, self.throughput,
                                       force=force)

    @property
    def aperture_area(self):
        """ Area of the telescope aperture. """
        return np.pi * (self.diameter / 2) ** 2

    @property
    def countrate(self):
        """ Countrate of the observation in ct / s."""
        return self.observation.countrate(area=self.aperture_area)

    def _set_lists(self, _list, _list_str):
        """
        Turns user-provided models into SpectralElements.
        Written such that the order in which the waveset and corresponding
        values are given in the list does not matter.
        """
        if len(_list) != 2:
            raise exceptions.BandpassError(_list_str + " should be "
                                           "a list with 2 x n "
                                           "dimensions.")
        try:
            __list = _call_SpecElement_4list(_list[0], _list[1])
        except u.UnitsError:
            try:
                __list = _call_SpecElement_4list(_list[1], _list[0])
            except u.UnitsError:
                print("rows of " + _list_str + " list must be of type "
                      "astropy.units.quantity.Quantity")
        return __list

    def _set_bandpass(self):
        """
        Sets the SpectralElement for the bandpass, which can be one of the
        given synphot bandpasses, a custom user-provided model, or one already
        set as a SpectralElement.
        """
        if type(self._bandpass) == list:
            self.bandpass = self._set_lists(self._bandpass, 'bandpass')

        elif type(self._bandpass) == str:
            self.bandpass = SpectralElement.from_filter(self._bandpass)

        elif type(self._bandpass) == SpectralElement:
            self.bandpass = self._bandpass

        else:
            raise exceptions.BandpassError("bandpass must be of type str, "
                                           "`~synphot.spectrum."
                                           "SpectralElement`, or list of "
                                           "shape(2, n) containing `~astropy"
                                           ".units.quantity.Quantity` values"
                                           )

        self.throughput = self.bandpass

    def _custom_qe(self):
        """
        Sets the SpectralElement for a given quantum efficiency and convolves
        it with the total throughput.
        """
        self.quantum_efficiency = self._set_lists(self._qe,
                                                  'quantum_efficiency')
        self.throughput *= self.quantum_efficiency

    def _generic_ccd(self):
        """
        Sets the SpectralElement for a generic throughput function of
        a silicon detector and convolves it with the total throughput.
        """
        wl = [100., 309.45600215, 319.53901519, 329.99173871,
              339.70504127, 349.78805431, 379.53294279, 390.00376402,
              399.57293121, 409.3114413, 419.5961146, 429.14136695,
              439.52687038, 449.9795939, 459.69289647, 469.60785929,
              479.85892255, 489.5638226, 499.59835962, 509.99161922,
              519.5607864, 529.30446727, 539.85285015, 549.59976275,
              559.51472558, 569.94676599, 579.68075166, 589.59571448,
              599.9631202, 609.56008031, 619.65269622, 630.09581687,
              639.67467926, 649.50561697, 659.84070534, 669.7685951,
              679.50258077, 689.9637068, 699.78494931, 709.53555533,
              719.83463294, 729.72858948, 739.88431656, 749.9673296,
              759.66253445, 769.59042422, 780.37854306, 789.59647942,
              799.60677842, 810.07759966, 819.65646205, 829.52341053,
              839.82248813, 849.68943661, 859.77244965, 870.07152726,
              879.71760973, 889.81096433, 899.94245339, 909.73137855,
              919.69435573, 930.06545485, 939.64431724, 949.72733028,
              959.95862293, 969.6772918, 979.76030484, 990.05938245,
              1100.]
        response = [0., 70.30747425, 73.11442327, 75.26541144, 76.58538173,
                    74.70200949, 77.10351031, 81.79762371, 84.528972,
                    87.18136276, 89.0405892, 91.16038906, 92.49142617,
                    93.66048522, 94.87582372, 95.64295585, 96.56602958,
                    97.20551595, 98.01709918, 98.32588679, 98.26189462,
                    98.79719419, 99.10133838, 99.09379281, 99.35788748,
                    99.30100555, 99.14661175, 98.81209184, 98.74843825,
                    98.30855134, 98.04495971, 97.98459522, 97.24513015,
                    96.85779131, 96.40002722, 96.03435769, 95.87183789,
                    95.09275863, 94.89671913, 94.49854563, 94.12126754,
                    93.52139537, 92.57268607, 91.77633908, 90.30410094,
                    88.68846298, 86.74856762, 84.85909033, 82.85400237,
                    80.76562301, 78.18504085, 75.90628116, 72.63150731,
                    68.93418199, 65.34249453, 61.79608045, 58.13799205,
                    54.49429826, 49.87975185, 45.18326838, 41.57397462,
                    36.82027063, 32.80603172, 28.7917928, 25.09446748,
                    21.39714216, 18.4392819, 14.89286782, 0.]

        self.quantum_efficiency = self._set_lists([wl, response],
                                                  'quantum_efficiency')
        self.throughput *= self.quantum_efficiency

    def _custom_atmosphere(self):
        """
        Sets the SpectralElement for a user-provided atmospheric
        transmission function and convolves it with the total throughput.
        """
        self.atmospheric_transmission = self._set_lists(self._atmo,
                                                        'atmospheric_'
                                                        'transmission')
        self.throughput *= self.atmospheric_transmission

    def snr(self, npix=1 * u.pixel,
            n_background=np.inf * u.pixel,
            background=0 * (u.ct / u.pixel),
            darkcurrent=0 * (u.ct / u.pixel),
            readnoise=0 * (u.ct / u.pixel),
            gain=0 * (u.ct / u.adu),
            ad_err=AD_ERR_DEFAULT):
        """
        A method to return the signal to noise ratio of the observation.
        For a complete list of parameters and their default values,
        see :func: `synphot.observe.ccd_snr`.

        Returns
        -------
        snr : `~astropy.units.quantity.Quantity`
        """
        return ccd_snr(self.countrate * self.exptime, npix=npix,
                       n_background=n_background, background=background,
                       darkcurrent=darkcurrent, readnoise=readnoise,
                       gain=gain, ad_err=ad_err)

    def required_exptime(self, desired_snr, npix=1 * u.pixel,
                         n_background=np.inf * u.pixel,
                         background_rate=0 * (u.ct / u.pixel / u.s),
                         darkcurrent_rate=0 * (u.ct / u.pixel / u.s),
                         readnoise=0 * (u.ct / u.pixel),
                         gain=1 * (u.ct / u.adu),
                         ad_err=AD_ERR_DEFAULT):
        """
        A method to return the exposure time needed to obtain a
        desired signal to noise ratio for this observation. For a complete
        list of parameters and their default values, see
        :func: `synphot.observe.exptime_from_ccd_snr`.

        Parameters
        ----------
        desired_snr : int or float

        Returns
        -------
        required_exptime : `~astropy.units.quantity.Quantity`
        """
        return exptime_from_ccd_snr(desired_snr, self.countrate,
                                    npix=npix, n_background=n_background,
                                    background_rate=background_rate,
                                    darkcurrent_rate=darkcurrent_rate,
                                    readnoise=readnoise, gain=gain,
                                    ad_err=AD_ERR_DEFAULT)


@u.quantity_input(waves=u.angstrom, frac=u.Unit(''))
def _call_SpecElement_4list(waves, frac):
    """ Returns a SpectralElement for the given points and values. """
    return SpectralElement(Empirical1D, points=waves, lookup_table=frac)
