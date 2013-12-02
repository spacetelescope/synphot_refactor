# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module defines reddening laws and extinction curves."""
from __future__ import absolute_import, division, print_function, unicode_literals

# ASTROPY
from astropy import units as u

# LOCAL
from . import spectrum, config, exceptions, specio, units


__all__ = ['ReddeningLaw', 'ExtinctionCurve']


class ReddeningLaw(spectrum.BaseUnitlessSpectrum):
    """Class to handle reddening law.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    R(V) values must be dimensionless.
    They are checked for negative values.
    If found, warning is issued and negative values are set to zeroes.

    Parameters
    ----------
    wavelengths : array_like or `astropy.units.quantity.Quantity`
        Wavelength values. If not a Quantity, assumed to be in
        Angstrom.

    rvs : array_like or `astropy.units.quantity.Quantity`
        R(V) values. Must be dimensionless.
        If not a Quantity, assumed to be in THROUGHPUT.

    kwargs : dict
        Keywords accepted by `~synphot.spectrum.BaseSpectrum`,
        except ``flux_unit``.

    Attributes
    ----------
    wave, thru : `astropy.units.quantity.Quantity`
        Wavelength and R(V) of the reddening law.

    primary_area : `astropy.units.quantity.Quantity` or `None`
        Area that flux covers in cm^2.

    metadata : dict
        Metadata. ``self.metadata['expr']`` must contain a descriptive string of the object.

    warnings : dict
        List of warnings related to spectrum object.

    Raises
    ------
    synphot.exceptions.SynphotError
        If wavelengths and R(V) do not match, or if they have invalid units.

    synphot.exceptions.DuplicateWavelength
        If wavelength array contains duplicate entries.

    synphot.exceptions.UnsortedWavelength
        If wavelength array is not monotonic.

    synphot.exceptions.ZeroWavelength
        If negative or zero wavelength occurs in wavelength array.

    """
    @classmethod
    def from_file(cls, filename, area=None, **kwargs):
        """Create a reddening law from file.

        If filename has 'fits' or 'fit' suffix, it is read as FITS.
        Otherwise, it is read as ASCII.

        Parameters
        ----------
        filename : str
            Reddening law filename.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by
            :func:`synphot.specio.read_fits_spec` (if FITS) or
            :func:`synphot.specio.read_ascii_spec` (if ASCII).

        Returns
        -------
        newspec : obj
            New reddening law.

        """
        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = units.THROUGHPUT

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'Av/E(B-V)'

        header, wavelengths, rvs = specio.read_spec(filename, **kwargs)
        return cls(wavelengths, rvs, area=area, header=header)

    def to_fits(self, filename, **kwargs):
        """Write the reddening law to a FITS file.

        R(V) column is automatically named 'Av/E(B-V)'.

        Parameters
        ----------
        filename : str
            Output filename.

        kwargs : dict
            Keywords accepted by :func:`synphot.specio.write_fits_spec`.

        """
        kwargs['flux_col'] = 'Av/E(B-V)'
        kwargs['flux_unit'] = units.THROUGHPUT

        # No need to trim/pad zeroes, unless user chooses to do so.
        if 'pad_zero_ends' not in kwargs:
            kwargs['pad_zero_ends'] = False
        if 'trim_zero' not in kwargs:
            kwargs['trim_zero'] = False

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = {'expr': (str(self), 'synphot expression'),
                 'tdisp1': 'G15.7',
                 'tdisp2': 'G15.7'}

        if 'ext_header' in kwargs:
            kwargs['ext_header'].update(bkeys)
        else:
            kwargs['ext_header'] = bkeys

        specio.write_fits_spec(filename, self.wave, self.thru, **kwargs)

    @classmethod
    def from_model(cls, modelname, area=None, **kwargs):
        """Load :ref:`pre-defined extinction model <synphot_reddening>`.

        Parameters
        ----------
        modelname : {'lmc30dor', 'lmcavg', 'mwavg', 'mwdense', 'mwrv21', 'mwrv40', 'smcbar', 'xgalsb'}
            Extinction model name.

        area : float or `astropy.units.quantity.Quantity`, optional
            Area that fluxes cover. Usually, this is the area of
            the primary mirror of the observatory of interest.
            If not a Quantity, assumed to be in cm^2.

        kwargs : dict
            Keywords acceptable by :func:`synphot.specio.read_remote_spec`.

        Returns
        -------
        newspec : obj
            Reddening law for the given model.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid model name.

        """
        modelname = modelname.lower()

        # Select filename based on model name
        if modelname == 'lmc30dor':
            cfgitem = config.LMC30DOR_FILE
        elif modelname == 'lmcavg':
            cfgitem = config.LMCAVG_FILE
        elif modelname == 'mwavg':
            cfgitem = config.MWAVG_FILE
        elif modelname == 'mwdense':
            cfgitem = config.MWDENSE_FILE
        elif modelname == 'mwrv21':
            cfgitem = config.MWRV21_FILE
        elif modelname == 'mwrv40':
            cfgitem = config.MWRV40_FILE
        elif modelname == 'smcbar':
            cfgitem = config.SMCBAR_FILE
        elif modelname == 'xgalsb':
            cfgitem = config.XGAL_FILE
        else:
            raise exceptions.SynphotError(
                'Model name {0} is invalid.'.format(modelname))

        filename = cfgitem()

        if 'flux_unit' not in kwargs:
            kwargs['flux_unit'] = units.THROUGHPUT

        if ((filename.endswith('fits') or filename.endswith('fit')) and
                'flux_col' not in kwargs):
            kwargs['flux_col'] = 'Av/E(B-V)'

        header, wavelengths, rvs = specio.read_remote_spec(filename, **kwargs)
        header['expr'] = modelname
        header['filename'] = filename
        header['descrip'] = cfgitem.description

        return cls(wavelengths, rvs, area=area, header=header)

    def plot(self, **kwargs):  # pragma: no cover
        """Plot the reddening law.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        kwargs : dict
            Keywords accepted by :func:`synphot.spectrum.BaseSpectrum.plot`,
            *except* ``ylabel``.

        """
        if 'ylabel' in kwargs:
            del kwargs[key]

        super(ReddeningLaw, self).plot(ylabel='R(V)', **kwargs)


class ExtinctionCurve(spectrum.BaseUnitlessSpectrum):
    """Class to handle extinction curve.

    Wavelengths must be monotonic ascending/descending without zeroes
    or duplicate values.

    Throughput (:math:`A(V)` in linear scale) values must be dimensionless.
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
        Keywords accepted by `~synphot.spectrum.BaseSpectrum`,
        except ``flux_unit``.

    Attributes
    ----------
    wave, thru : `astropy.units.quantity.Quantity`
        Wavelength and throughput of the extinction curve.

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
    @classmethod
    def from_reddening_law(cls, redlaw, ebv):
        """Calculate A(V) in linear scale for the given
        reddening law and E(B-V).

        .. math::

            A(V) = R(V) * E(B-V)

            thru = 10^{-0.4 * A(V)}

        Parameters
        ----------
        redlaw : `ReddeningLaw`
            Reddening law.

        ebv : float or `astropy.units.quantity.Quantity`
            E(B-V) value in magnitude.

        Returns
        -------
        newspec : obj
            New extinction curve.

        Raises
        ------
        synphot.exceptions.SynphotError
            Invalid inputs.

        """
        if not isinstance(redlaw, ReddeningLaw):
            raise exceptions.SynphotError(
                '{0} is not a ReddeningLaw'.format(redlaw))

        if isinstance(ebv, u.Quantity) and ebv.unit.decompose() == u.mag:
            ebv = ebv.value
        elif not isinstance(ebv, (int, long, float)):
            raise exceptions.SynphotError(
                'E(B-V)={0} is invalid.'.format(ebv))

        thru = 10**(-0.4 * redlaw.thru.value * ebv)
        hdr = {'expr': '{0} from {1} with E(B-V)={2}'.format(
                cls.__name__, str(redlaw), ebv)}

        return cls(redlaw.wave, thru, area=redlaw.primary_area, header=hdr)

    def plot(self, **kwargs):  # pragma: no cover
        """Plot the extinction curve.

        .. note:: Uses :mod:`matplotlib`.

        Parameters
        ----------
        kwargs : dict
            Keywords accepted by :func:`synphot.spectrum.BaseSpectrum.plot`,
            *except* ``ylabel``.

        """
        if 'ylabel' in kwargs:
            del kwargs[key]

        super(ExtinctionCurve, self).plot(ylabel='10^(-0.4 * A(V))', **kwargs)
