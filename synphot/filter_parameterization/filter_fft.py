"""Handle Fast Fourier Transform (FFT) for filter parameterization."""

import numpy as np
from astropy import units as u
from astropy.modeling.models import custom_model, Sine1D
from astropy.table import Table

from synphot.models import Empirical1D
from synphot.spectrum import SpectralElement
from synphot.units import validate_quantity

__all__ = ['filter_to_fft', 'filter_from_fft', 'analytical_model_from_fft',
           'filters_to_fft_table']


def _simplified_wavelength(n_lambda, lambda_0, delta_lambda):
    # tynt assumed everything was in Angstrom, which coincides with
    # synphot internal wavelength unit.
    wave_unit = SpectralElement._internal_wave_unit

    lambda_0 = validate_quantity(
        lambda_0, wave_unit, equivalencies=u.spectral())
    delta_lambda = validate_quantity(
        delta_lambda, wave_unit, equivalencies=u.spectral())
    lambda_max = (n_lambda + 1) * delta_lambda + lambda_0

    return np.arange(lambda_0.value, lambda_max.value,
                     delta_lambda.value) * wave_unit


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

    lambda_0 : `~astropy.units.quantity.Quantity`
        Minimum value of ``wl``.

    delta_lambda : `~astropy.units.quantity.Quantity`
        Median delta wavelength.

    tr_max : `~astropy.units.quantity.Quantity`
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

    if isinstance(fft, u.Quantity):
        fft_parameters = fft.value.tolist()
    else:  # Older Numpy does not return Quantity
        fft_parameters = fft.tolist()

    return n_lambda, lambda_0, delta_lambda, tr_max, fft_parameters


def filter_from_fft(n_lambda, lambda_0, delta_lambda, tr_max, fft_parameters):
    """Reconstruct a filter from given FFT parameters.
    The inputs for this function can be obtained from :func:`filter_to_fft`.

    Parameters
    ----------
    n_lambda : int
        Number of elements in original wavelength array.

    lambda_0 : float or `~astropy.units.quantity.Quantity`
        Minimum value of original wavelength array.
        If not a Quantity, assumed to be in Angstrom.

    delta_lambda : float or `~astropy.units.quantity.Quantity`
        Median delta wavelength of original wavelength array.
        If not a Quantity, assumed to be in Angstrom.

    tr_max : float or `~astropy.units.quantity.Quantity`
        Maximum value of transmittance curve.
        If a Quantity, must be unitless.

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
    ifft = np.fft.ifft(fft_parameters, n=n_wave)
    transmittance = ((ifft.real - ifft.real.min()) * tr_max / np.ptp(ifft.real))  # noqa
    return SpectralElement(
        Empirical1D, points=wavelength, lookup_table=transmittance)


def analytical_model_from_fft(n_lambda, lambda_0, delta_lambda, tr_max,
                              fft_parameters):
    """Similar to :func:`filter_from_fft` except that this returns
    an analytical model.

    .. note::

        This model needs to be sampled using the full range of
        wavelength. See https://github.com/bmorris3/tynt/issues/9 .

    Returns
    -------
    astropy_model : `~astropy.modeling.CompoundModel`
        A compound model that consists of
        `~astropy.modeling.functional_models.Sine1D` models.

    """
    wavelength = _simplified_wavelength(n_lambda, lambda_0, delta_lambda)
    n_wave = len(wavelength)
    n_fft_pars = len(fft_parameters)

    m = (np.sum([Sine1D(amplitude=fft_parameters[i].real / n_wave,
                        frequency=i / n_wave, phase=0.25)
                 for i in range(n_fft_pars)]) -
         np.sum([Sine1D(amplitude=fft_parameters[i].imag / n_wave,
                        frequency=i / n_wave)
                 for i in range(n_fft_pars)]))

    @custom_model
    def fft_model(x):
        """Approximate Fourier reconstruction of an astronomical filter.

        Parameters
        ----------
        x : `~astropy.units.quantity.Quantity`
            Full wavelength range that samples the filter.

        Returns
        -------
        transmittance : array-like or `~astropy.units.quantity.Quantity`
            Transmittance curve. If ``tr_max`` is a Quantity, this will
            be a Quantity as well.

        """
        wave_unit = SpectralElement._internal_wave_unit
        x = validate_quantity(x, wave_unit, equivalencies=u.spectral())

        mo = m((x - wavelength.min()) / (wavelength[1] - wavelength[0]))
        return (mo - mo.min()) * tr_max / np.ptp(mo)

    return fft_model()


def filters_to_fft_table(filters_mapping, n_terms=10):
    """Run :func:`filter_to_fft` on a list of filters
    and store results in a table.

    Parameters
    ----------
    filters_mapping : dict
        Dictionary mapping human-readable filter name to its
        `~synphot.spectrum.SpectralElement` and wavelengths, if applicable.
        If the filter object has a valid ``waveset``, just provide `None`
        for wavelengths; otherwise provide a Quantity array for sampling.
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
    wave_unit = SpectralElement._internal_wave_unit
    colnames = ['filter', 'n_lambda', 'lambda_0', 'delta_lambda',
                'tr_max'] + [f'fft_{i}' for i in range(n_terms)]
    rows = []

    for key, (bp, wavelengths) in filters_mapping.items():
        n_lambda, lambda_0, delta_lambda, tr_max, fft_pars = filter_to_fft(
            bp, wavelengths=wavelengths, n_terms=n_terms)
        rows.append(tuple(
            [key, n_lambda, lambda_0, delta_lambda, tr_max] + fft_pars))

    fft_table = Table(rows=rows, names=colnames)
    fft_table['lambda_0'].unit = wave_unit
    fft_table['delta_lambda'].unit = wave_unit

    return fft_table
