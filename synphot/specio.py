# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This modules handles synthetic photometry data formats."""
from __future__ import absolute_import, division, print_function
from .extern import six

# STDLIB
import os
import warnings

# THIRD-PARTY
import numpy as np

# ASTROPY
from astropy import log
from astropy import units as u
from astropy.io import ascii, fits
from astropy.utils.data import get_readable_fileobj
from astropy.utils.exceptions import AstropyUserWarning

# LOCAL
from . import exceptions, units
from synphot import __version__

__all__ = ['read_remote_spec', 'read_spec', 'read_ascii_spec',
           'read_fits_spec', 'write_fits_spec']


def read_remote_spec(filename, encoding='binary', cache=True,
                     show_progress=True, **kwargs):
    """Read FITS or ASCII spectrum from a remote location.

    Parameters
    ----------
    filename : str
        Spectrum filename.

    encoding, cache, show_progress
        See :func:`~astropy.utils.data.get_readable_fileobj`.

    kwargs : dict
        Keywords acceptable by :func:`read_fits_spec` (if FITS) or
        :func:`read_ascii_spec` (if ASCII).

    Returns
    -------
    header : dict
        Metadata.

    wavelengths, fluxes : `~astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

    """
    with get_readable_fileobj(filename, encoding=encoding, cache=cache,
                              show_progress=show_progress) as fd:
        header, wavelengths, fluxes = read_spec(fd, fname=filename, **kwargs)

    return header, wavelengths, fluxes


def read_spec(filename, fname='', **kwargs):
    """Read FITS or ASCII spectrum.

    Parameters
    ----------
    filename : str or file pointer
        Spectrum file name or pointer.

    fname : str
        Filename. This is *only* used if ``filename`` is a pointer.

    kwargs : dict
        Keywords acceptable by :func:`read_fits_spec` (if FITS) or
        :func:`read_ascii_spec` (if ASCII).

    Returns
    -------
    header : dict
        Metadata.

    wavelengths, fluxes : `~astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

    Raises
    ------
    synphot.exceptions.SynphotError
        Read failed.

    """
    if isinstance(filename, six.string_types):
        fname = filename
    elif not fname:  # pragma: no cover
        raise exceptions.SynphotError('Cannot determine filename.')

    if fname.endswith('fits') or fname.endswith('fit'):
        read_func = read_fits_spec
    else:
        read_func = read_ascii_spec

    return read_func(filename, **kwargs)


def read_ascii_spec(filename, wave_unit=u.AA, flux_unit=units.FLAM, **kwargs):
    """Read ASCII spectrum.

    ASCII table must have following columns:

        #. Wavelength data
        #. Flux data

    It can have more than 2 columns but the rest is ignored.
    Comments are discarded.

    Parameters
    ----------
    filename : str or file pointer
        Spectrum file name or pointer.

    wave_unit, flux_unit : str or `~astropy.units.core.Unit`
        Wavelength and flux units, which default to Angstrom and FLAM,
        respectively.

    kwargs : dict
        Keywords accepted by :func:`astropy.io.ascii.ui.read`.

    Returns
    -------
    header : dict
        This is just an empty dictionary, so returned values
        are the same as :func:`read_fits_spec`.

    wavelengths, fluxes : `~astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.
        They are set to 'float64' percision.

    """
    header = {}

    dat = ascii.read(filename, **kwargs)

    wave_unit = units.validate_unit(wave_unit)
    flux_unit = units.validate_unit(flux_unit)

    wavelengths = dat.columns[0].data.astype(np.float64) * wave_unit
    fluxes = dat.columns[1].data.astype(np.float64) * flux_unit

    return header, wavelengths, fluxes


def read_fits_spec(filename, ext=1, wave_col='WAVELENGTH', flux_col='FLUX',
                   wave_unit=u.AA, flux_unit=units.FLAM):
    """Read FITS spectrum.

    Wavelength and flux units are extracted from ``TUNIT1`` and ``TUNIT2``
    keywords, respectively, from data table (not primary) header.
    If these keywords are not present, units are taken from
    ``wave_unit`` and ``flux_unit`` instead.

    Parameters
    ----------
    filename : str or file pointer
        Spectrum file name or pointer.

    ext: int
        FITS extension with table data. Default is 1.

    wave_col, flux_col : str
        Wavelength and flux column names (case-insensitive).

    wave_unit, flux_unit : str or `~astropy.units.core.Unit`
        Wavelength and flux units, which default to Angstrom and FLAM,
        respectively. These are *only* used if ``TUNIT1`` and ``TUNIT2``
        keywords are not present in table (not primary) header.

    Returns
    -------
    header : dict
        Primary header only. Extension header is discarded.

    wavelengths, fluxes : `~astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

    """
    fs = fits.open(filename)
    header = dict(fs[str('PRIMARY')].header)
    wave_dat = fs[ext].data.field(wave_col).copy()
    flux_dat = fs[ext].data.field(flux_col).copy()
    fits_wave_unit = fs[ext].header.get('TUNIT1')
    fits_flux_unit = fs[ext].header.get('TUNIT2')

    if fits_wave_unit is not None:
        try:
            wave_unit = units.validate_unit(fits_wave_unit)
        except (exceptions.SynphotError, ValueError) as e:  # pragma: no cover
            warnings.warn(
                '{0} from FITS header is not valid wavelength unit, using '
                '{1}: {2}'.format(fits_wave_unit, wave_unit, e),
                AstropyUserWarning)

    if fits_flux_unit is not None:
        try:
            flux_unit = units.validate_unit(fits_flux_unit)
        except (exceptions.SynphotError, ValueError) as e:  # pragma: no cover
            warnings.warn(
                '{0} from FITS header is not valid flux unit, using '
                '{1}: {2}'.format(fits_flux_unit, flux_unit, e),
                AstropyUserWarning)

    wave_unit = units.validate_unit(wave_unit)
    flux_unit = units.validate_unit(flux_unit)

    wavelengths = wave_dat * wave_unit
    fluxes = flux_dat * flux_unit

    if isinstance(filename, six.string_types):
        fs.close()

    return header, wavelengths, fluxes


def write_fits_spec(filename, wavelengths, fluxes, pri_header={},
                    ext_header={}, overwrite=False, trim_zero=True,
                    pad_zero_ends=True, precision=None, epsilon=0.00032,
                    wave_col='WAVELENGTH', flux_col='FLUX',
                    wave_unit=u.AA, flux_unit=units.FLAM):
    """Write FITS spectrum.

    .. warning::

        If data is being written out as single-precision but wavelengths
        are in double-precision, some rows may be omitted.

    Parameters
    ----------
    filename : str
        Output spectrum filename.

    wavelengths, fluxes : array-like or `~astropy.units.quantity.Quantity`
        Wavelength and flux of the spectrum.

    pri_header, ext_header : dict
        Metadata to be added to primary and given extension FITS header,
        respectively. Do *not* use this to define column names and units.

    overwrite : bool
        Overwrite existing file. Defaults to `False`.

    trim_zero : bool
        Remove rows with zero-flux. Default is `True`.

    pad_zero_ends : bool
        Pad each end of the spectrum with a row of zero flux
        like :func:`synphot.spectrum.BaseSpectrum.taper`.
        This is unnecessary if input is already tapered.

    precision : {`None`, 'single', 'double'}
        Precision of values in output file.
        Use native flux precision by default.

    epsilon : float
        Single-precision :math:`\\epsilon` value, taken from IRAF SYNPHOT FAQ.
        This is the minimum separation in wavelengths necessary for SYNPHOT
        to read the entries as distinct single-precision numbers.
        This is *only* used if ``precision='single'`` but data are in
        double-precision. Default from the FAQ is 0.00032.

    wave_col, flux_col : str
        Wavelength and flux column names (case-insensitive).

    wave_unit, flux_unit : str or `~astropy.units.core.Unit`
        Wavelength and flux units, which default to Angstrom and FLAM,
        respectively. These are *only* used if wavelengths and fluxes
        are not in astropy quantities.

    Raises
    ------
    synphot.exceptions.SynphotError
        Wavelengths and fluxes have difference shapes or value precision
        is not supported.

    """
    if isinstance(wavelengths, u.Quantity):
        wave_unit = wavelengths.unit
        wave_value = wavelengths.value
    else:
        wave_value = wavelengths

    if isinstance(fluxes, u.Quantity):
        flux_unit = fluxes.unit
        flux_value = fluxes.value
    else:
        flux_value = fluxes

    wave_unit = units.validate_unit(wave_unit).to_string().upper()
    flux_unit = units.validate_unit(flux_unit).to_string().upper()

    if wave_value.shape != flux_value.shape:
        raise exceptions.SynphotError(
            'Wavelengths have shape {0} but fluxes have shape {1}'.format(
                wave_value.shape, flux_value.shape))

    # Remove rows with zero flux. Putting this before precision logic to avoid
    # keeping duplicate wavelengths with zero flux.
    if trim_zero:
        idx = np.where(flux_value != 0)
        wave_value = wave_value[idx]
        flux_value = flux_value[idx]

        n_thrown = wave_value.size - len(idx[0])
        if n_thrown != 0:
            log.info('{0} zero-flux rows are thrown out'.format(n_thrown))

    # Only these Numpy types are supported
    #    'f'   np.float32
    #    'd'   np.float64
    pcodes = {'d': 'D', 'f': 'E'}  # Numpy to FITS conversion

    # Use native flux precision
    if precision is None:
        precision = flux_value.dtype.char
        if precision not in pcodes:
            raise exceptions.SynphotError('flux is not float32 or float64')

    # Use user specified precision
    else:
        precision = precision.lower()
        if precision == 'single':
            precision = 'f'
        elif precision == 'double':
            precision = 'd'
        else:
            raise exceptions.SynphotError(
                'precision must be single or double')

    # Now check wavelength precision
    wave_precision = wave_value.dtype.char
    if wave_precision not in pcodes:
        raise exceptions.SynphotError(
            'wavelength is not float32 or float64')

    # If wavelength is double-precision but data is written out as
    # single-precision, wavelength values have to be recalculated
    # so that they will still be sorted with no duplicates.
    if wave_precision == 'd' and precision == 'f':
        orig_size = wave_value.size
        idx = np.where(np.abs(wave_value[1:] - wave_value[:-1]) > epsilon)
        wave_value = np.append(wave_value[idx], wave_value[-1])
        flux_value = np.append(flux_value[idx], flux_value[-1])
        n_thrown = orig_size - wave_value.size
        if n_thrown != 0:
            warnings.warn(
                '{0} rows are thrown out in converting wavelengths from '
                'double- to single-precision'.format(n_thrown),
                AstropyUserWarning)

    # Keep one zero at each end
    if pad_zero_ends:
        w1 = wave_value[0] ** 2 / wave_value[1]
        w2 = wave_value[-1] ** 2 / wave_value[-2]
        wave_value = np.insert(wave_value, [0, wave_value.size], [w1, w2])
        flux_value = np.insert(flux_value, [0, flux_value.size], [0.0, 0.0])

    # Construct the columns
    cw = fits.Column(name=wave_col, array=wave_value, unit=wave_unit,
                     format=pcodes[precision])
    cf = fits.Column(name=flux_col, array=flux_value, unit=flux_unit,
                     format=pcodes[precision])

    # These are written to the primary header:
    #   1. Filename
    #   2. Origin
    #   3. User dictionary (can overwrite defaults)
    hdr_hdu = fits.PrimaryHDU()
    hdr_hdu.header['filename'] = (os.path.basename(filename), 'name of file')
    hdr_hdu.header['origin'] = ('synphot', 'Version {0}'.format(__version__))
    for key, val in pri_header.items():
        hdr_hdu.header[key] = val

    # Make the extension HDU and include user dictionary in extension header.
    tab_hdu = fits.BinTableHDU.from_columns(fits.ColDefs([cw, cf]))
    for key, val in ext_header.items():
        tab_hdu.header[key] = val

    # Write to file
    hdulist = fits.HDUList([hdr_hdu])
    hdulist.append(tab_hdu)
    hdulist.writeto(filename, overwrite=overwrite)
