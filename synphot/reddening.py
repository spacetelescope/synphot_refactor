# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines reddening laws and extinction curves."""
from __future__ import absolute_import, division, print_function

# STDLIB
import numbers

# THIRD-PARTY
import numpy as np
from astropy import units as u

# LOCAL
from . import exceptions, specio, units
from .config import Conf
from .models import Empirical1D
from .spectrum import BaseUnitlessSpectrum

__all__ = ['ExtinctionModel1D', 'ReddeningLaw', 'ExtinctionCurve',
           'etau_madau']


class ExtinctionModel1D(Empirical1D):
    """Model to handle extinction curve.
    This is like :class:`~synphot.models.Empirical1D` except that
    its ``sampleset`` will not be propagated to composite spectrum.
    """
    def sampleset(self):
        """This simply returns `None`. Use ``numpy.squeeze(self.points)``
        instead for array (in Angstrom) that samples the model.
        """
        return None


class ReddeningLaw(BaseUnitlessSpectrum):
    """Class to handle reddening law.

    Parameters
    ----------
    modelclass, kwargs
        See `~synphot.spectrum.BaseSpectrum`.

    """
    def extinction_curve(self, ebv, wavelengths=None):
        """Generate extinction curve.

        .. math::

            A(V) = R(V) \\; \\times \\; E(B-V)

            THRU = 10^{-0.4 \\; A(V)}

        Parameters
        ----------
        ebv : float or `~astropy.units.quantity.Quantity`
            :math:`E(B-V)` value in magnitude.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        Returns
        -------
        extcurve : `ExtinctionCurve`
            Empirical extinction curve.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid input.

        """
        if isinstance(ebv, u.Quantity) and ebv.unit.decompose() == u.mag:
            ebv = ebv.value
        elif not isinstance(ebv, numbers.Real):
            raise exceptions.SynphotError('E(B-V)={0} is invalid.'.format(ebv))

        x = self._validate_wavelengths(wavelengths).value
        y = 10 ** (-0.4 * self(x).value * ebv)
        header = {
            'E(B-V)': ebv,
            'ReddeningLaw': self.meta.get('expr', 'unknown')}

        return ExtinctionCurve(ExtinctionModel1D, points=x, lookup_table=y,
                               meta={'header': header})

    def to_fits(self, filename, wavelengths=None, **kwargs):
        """Write the reddening law to a FITS file.

        :math:`R(V)` column is automatically named 'Av/E(B-V)'.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array-like, `~astropy.units.quantity.Quantity`, or `None`
            Wavelength values for sampling.
            If not a Quantity, assumed to be in Angstrom.
            If `None`, ``self.waveset`` is used.

        kwargs : dict
            Keywords accepted by :func:`~synphot.specio.write_fits_spec`.

        """
        w, y = self._get_arrays(wavelengths)

        kwargs['flux_col'] = 'Av/E(B-V)'
        kwargs['flux_unit'] = self._internal_flux_unit

        # No need to trim/pad zeroes, unless user chooses to do so.
        if 'pad_zero_ends' not in kwargs:
            kwargs['pad_zero_ends'] = False
        if 'trim_zero' not in kwargs:
            kwargs['trim_zero'] = False

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'tdisp1': 'G15.7', 'tdisp2': 'G15.7'}

        if 'expr' in self.meta:
            bkeys['expr'] = (self.meta['expr'], 'synphot expression')

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        specio.write_fits_spec(filename, w, y, **kwargs)

    @classmethod
    def from_file(cls, filename, **kwargs):
        """Create a reddening law from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Reddening law filename.

        kwargs : dict
            Keywords acceptable by
            :func:`~synphot.specio.read_fits_spec` (if FITS) or
            :func:`~synphot.specio.read_ascii_spec` (if ASCII).

        Returns
        -------
        redlaw : `ReddeningLaw`
            Empirical reddening law.

        """
        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = cls._internal_flux_unit

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'Av/E(B-V)'

        header, wavelengths, rvs = specio.read_spec(filename, **kwargs)

        return cls(Empirical1D, points=wavelengths, lookup_table=rvs,
                   meta={'header': header})

    @classmethod
    def from_extinction_model(cls, modelname, **kwargs):
        """Load :ref:`pre-defined extinction model <synphot_reddening>`.

        Parameters
        ----------
        modelname : str
            Extinction model name. Choose from 'lmc30dor', 'lmcavg', 'mwavg',
            'mwdense', 'mwrv21', 'mwrv40', 'smcbar', or 'xgalsb'.

        kwargs : dict
            Keywords acceptable by :func:`~synphot.specio.read_remote_spec`.

        Returns
        -------
        redlaw : `ReddeningLaw`
            Empirical reddening law.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid extinction model name.

        """
        modelname = modelname.lower()

        # Select filename based on model name
        if modelname == 'lmc30dor':
            cfgitem = Conf.lmc30dor_file
        elif modelname == 'lmcavg':
            cfgitem = Conf.lmcavg_file
        elif modelname == 'mwavg':
            cfgitem = Conf.mwavg_file
        elif modelname == 'mwdense':
            cfgitem = Conf.mwdense_file
        elif modelname == 'mwrv21':
            cfgitem = Conf.mwrv21_file
        elif modelname == 'mwrv40':
            cfgitem = Conf.mwrv40_file
        elif modelname == 'smcbar':
            cfgitem = Conf.smcbar_file
        elif modelname == 'xgalsb':
            cfgitem = Conf.xgal_file
        else:
            raise exceptions.SynphotError(
                'Extinction model {0} is invalid.'.format(modelname))

        filename = cfgitem()

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = cls._internal_flux_unit

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'Av/E(B-V)'

        header, wavelengths, rvs = specio.read_remote_spec(filename, **kwargs)
        header['filename'] = filename
        header['descrip'] = cfgitem.description
        meta = {'header': header, 'expr': modelname}

        return cls(Empirical1D, points=wavelengths, lookup_table=rvs,
                   meta=meta)


class ExtinctionCurve(BaseUnitlessSpectrum):
    """Class to handle extinction curve.

    Parameters
    ----------
    modelclass, kwargs
        See `~synphot.spectrum.BaseSpectrum`.

    """
    pass


# TODO: Find a better way to handle so many magic numbers.
# See https://github.com/spacetelescope/synphot_refactor/issues/77
def etau_madau(wave, z, **kwargs):
    """Madau 1995 extinction for a galaxy at given redshift.
    This is the Lyman-alpha prescription from the photo-z code BPZ.

    The Lyman-alpha forest approximately has an effective
    "throughput" which is a function of redshift and
    rest-frame wavelength.
    One would multiply the SEDs by this factor before
    passing it through an instrument filter.

    This approximation is from Footnote 3 of
    :ref:`Madau et al. (1995) <synphot-ref-madau1995>`.
    This is claimed accurate to 5%.
    The scatter in this factor (due to different lines of sight)
    is huge, as shown in Madau's Fig. 3 (top panel);
    The figure's bottom panel shows a redshifted version of the
    "exact" prescription.

    Parameters
    ----------
    wave : array-like or `~astropy.units.quantity.Quantity`
        Redshifted wavelength values.
        Non-redshifted wavelength is ``wave / (1 + z)``.

    z : number
        Redshift.

    kwargs : dict
        Equivalencies for unit conversion, see
        :func:`~synphot.units.validate_quantity`.

    Returns
    -------
    extcurve : `ExtinctionCurve`
        Extinction curve to apply to the redshifted spectrum.

    """
    if not isinstance(z, numbers.Real):
        raise exceptions.SynphotError(
            'Redshift must be a real scalar number.')

    if np.isscalar(wave) or len(wave) <= 1:
        raise exceptions.SynphotError('Wavelength has too few data points')

    wave = units.validate_quantity(wave, u.AA, **kwargs).value

    ll = 912.0
    c = np.array([3.6e-3, 1.7e-3, 1.2e-3, 9.3e-4])
    el = np.array([1216, 1026, 973, 950], dtype=np.float)  # noqa
    tau = np.zeros_like(wave, dtype=np.float)
    xe = 1.0 + z

    # Lyman series
    for i in range(len(el)):
        tau = np.where(wave <= el[i] * xe,
                       tau + c[i] * (wave / el[i]) ** 3.46,
                       tau)

    # Photoelectric absorption
    xc = wave / ll
    xc3 = xc ** 3
    tau = np.where(wave <= ll * xe,
                   (tau + 0.25 * xc3 * (xe ** 0.46 - xc ** 0.46) +
                    9.4 * xc ** 1.5 * (xe ** 0.18 - xc ** 0.18) -
                    0.7 * xc3 * (xc ** (-1.32) - xe ** (-1.32)) -
                    0.023 * (xe ** 1.68 - xc ** 1.68)),
                   tau)

    thru = np.where(tau > 700., 0., np.exp(-tau))
    meta = {'descrip': 'Madau 1995 extinction for z={0}'.format(z)}
    return ExtinctionCurve(ExtinctionModel1D, points=wave, lookup_table=thru,
                           meta=meta)
