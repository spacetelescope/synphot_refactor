"""Handle Fast Fourier Transform (FFT) for filter parameterization."""

import numpy as np
from astropy.modeling import models
from astropy.modeling.models import Sine1D
from astropy.table import Table

from synphot.spectrum import SpectralElement

__all__ = ['filter_to_fft', 'filter_from_fft']


def _simplified_wavelength(n_lambda, lambda_0, delta_lambda):
    return np.arange(lambda_0, (n_lambda + 1) * delta_lambda + lambda_0,
                     delta_lambda)


def filter_to_fft(bp, wavelengths=None, n_terms=10):
    """Calculate filter parameters using FFT.

    Parameters
    ----------
    bp : `~synphot.spectrum.SpectralElement`
        Filter to parameterize.

    wavelengths : array-like or `~astropy.units.quantity.Quantity`
        Wavelength values for sampling.
        If not a Quantity, assumed to be in Angstrom.
        If `None`, ``waveset`` is used.

    n_terms : int
        Number of FFT parameters to keep.

    Returns
    -------
    n_lambda : int
        Number of elements in ``wl``.

    lambda_0 : float
        Minimum value of ``wl``.

    delta_lambda : float
        Median delta wavelength.

    tr_max : float
        Maximum value of ``tr``.

    fft_parameters : list of complex
        List of complex values that are FFT parameters to keep.

    """
    wl = bp._validate_wavelengths(wavelengths)
    tr = bp(wl)

    diff_wl = np.diff(wl)

    delta_lambda = np.nanmedian(diff_wl[diff_wl != 0])
    lambda_0 = wl.min()
    n_lambda = len(wl)

    # Create a simplified wavelength grid
    simplified_wavelength = _simplified_wavelength(
        n_lambda, lambda_0, delta_lambda)

    tr_max = tr.max()

    # Interpolate transmittance onto simplified wavelength grid
    tr_interp = np.interp(simplified_wavelength, wl, tr)

    # Take the DFT of the interpolated transmittance curve
    fft = np.fft.fft(tr_interp)[:n_terms]

    return n_lambda, lambda_0, delta_lambda, tr_max, fft.tolist()


def filter_from_fft(n_lambda, lambda_0, delta_lambda, tr_max, fft_parameters):
    """Reconstruct a filter from given FFT parameters.
    The inputs for this function can be obtained from :func:`filter_to_fft`.

    Parameters
    ----------
    n_lambda : int
        Number of elements in original wavelength array.

    lambda_0 : float
        Minimum value of original wavelength array.

    delta_lambda : float
        Median delta wavelength of original wavelength array.

    tr_max : float
        Maximum value of transmittance curve.

    fft_parameters : list of complex
        List of complex values that are FFT parameters representing the
        filter transmittance curve.

    Returns
    -------
    bp : `~synphot.spectrum.SpectralElement`
       Reconstructed filter.

    """
    wavelength = _simplified_wavelength(n_lambda, lambda_0, delta_lambda)
    n_wave = len(wavelength)

    # NOTE: This is not used when astropy model is returned. But the formula
    # is kept here in case we need sampled data instead of model in the future.
    # To calculate sampled transmittance:
    # ifft = np.fft.ifft(fft_parameters, n=n_wave)
    # transmittance = ((ifft.real - ifft.real.min()) * tr_max / ifft.real.ptp())  # noqa

    n_fft_pars = len(fft_parameters)

    m = (np.sum([Sine1D(amplitude=fft_parameters[i].real / n_wave,
                        frequency=i / n_wave, phase=0.25)
                 for i in range(n_fft_pars)]) -
         np.sum([Sine1D(amplitude=fft_parameters[i].imag / n_wave,
                        frequency=i / n_wave)
                 for i in range(n_fft_pars)]))

    @models.custom_model
    def fft_model(x):
        """
        Approximate Fourier reconstruction of an astronomical filter

        Parameters
        ----------
        x : array-like
            Wavelength in Angstroms.

        Returns
        -------
        transmittance : array-like
            Transmittance curve.
        """
        mo = m((x - wavelength.min()) / (wavelength[1] - wavelength[0]))
        return (mo - mo.min()) * tr_max / mo.ptp()

    return SpectralElement(fft_model())


def filters_to_fft_table(filters_mapping, n_terms=10):
    """Run :func:`filter_to_fft` on a list of filters
    and store results in a table.

    Parameters
    ----------
    filters_mapping : dict
        Dictionary mapping human-readable filter name to its
        `~synphot.spectrum.SpectralElement` and wavelengths, if applicable.
        For example::

            {'JOHNSON/V': (<SpectralElement ...>, None),
             'Flat': (<SpectralElement ...>, <Quantity [1000., ..., 9999.] Angstrom>)}

    n_terms : int
        Number of FFT parameters to keep.

    Returns
    -------
    fft_table : `~astropy.table.Table`
        Table storing FFT parameterization for the given filters.
        Use its ``write`` method to save it to file.

    """  # noqa
    fft_table = Table(names=['filter', 'n_lambda', 'lambda_0', 'delta_lambda',
                             'tr_max'] + [f'fft_{i}' for i in range(n_terms)],
                      dtype=[np.str, np.int, np.float, np.float, np.float] +
                      [np.complex] * n_terms)

    for key, (bp, wavelengths) in filters_mapping.items():
        n_lambda, lambda_0, delta_lambda, tr_max, fft_pars = filter_to_fft(
            bp, wavelengths=wavelengths, n_terms=n_terms)
        fft_table.add_row(tuple(
            [key, n_lambda, lambda_0, delta_lambda, tr_max] + fft_pars))

    return fft_table
