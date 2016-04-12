# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines reddening laws and extinction curves."""
from __future__ import absolute_import, division, print_function, unicode_literals

# STDLIB
import numbers

# ASTROPY
from astropy import units as u

# LOCAL
from . import exceptions, specio
from .config import Conf
from .models import Empirical1D
from .spectrum import BaseUnitlessSpectrum


__all__ = ['ReddeningLaw', 'ExtinctionCurve']


class ReddeningLaw(BaseUnitlessSpectrum):
    """Class to handle reddening law.

    Parameters
    ----------
    modelclass, metadata, kwargs
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

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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
            'ReddeningLaw': self.metadata.get('expr', 'unknown')}

        return ExtinctionCurve(Empirical1D, x=x, y=y, metadata=header)

    def to_fits(self, filename, wavelengths=None, **kwargs):
        """Write the reddening law to a FITS file.

        :math:`R(V)` column is automatically named 'Av/E(B-V)'.

        Parameters
        ----------
        filename : str
            Output filename.

        wavelengths : array_like, `~astropy.units.quantity.Quantity`, or `None`
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

        if 'expr' in self.metadata:
            bkeys['expr'] = (self.metadata['expr'], 'synphot expression')

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
        return cls(Empirical1D, x=wavelengths, y=rvs, metadata=header)

    @classmethod
    def from_extinction_model(cls, modelname, **kwargs):
        """Load :ref:`pre-defined extinction model <synphot_reddening>`.

        Parameters
        ----------
        modelname : {'lmc30dor', 'lmcavg', 'mwavg', 'mwdense', 'mwrv21', 'mwrv40', 'smcbar', 'xgalsb'}
            Extinction model name.

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
        header['expr'] = modelname
        header['filename'] = filename
        header['descrip'] = cfgitem.description

        return cls(Empirical1D, x=wavelengths, y=rvs, metadata=header)


class ExtinctionCurve(BaseUnitlessSpectrum):
    """Class to handle extinction curve.

    Parameters
    ----------
    modelclass, metadata, kwargs
        See `~synphot.spectrum.BaseSpectrum`.

    """
    pass
