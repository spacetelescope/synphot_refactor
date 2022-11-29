.. _synphot_par_filters:

Parameterized Filters
=====================

.. note::

    The algorithm for parameterized filters here was originally developed by
    Brett Morris for the `tynt <https://github.com/bmorris3/tynt/>`_ package.

Filter responses can be approximated using Fast Fourier Transform (FFT).
If a filter is approximated this way, one only needs to store its FFT
parameters instead of all the sampled data points. This reduces the
storage size and increases performance, at the cost of reduced accuracy.
If you decide to use the parameterization functions provided here,
it is up to you to decide whether the results are good enough for your
use cases or not.

.. _filter_fft_generation:

Generating FFT
--------------

.. testsetup::

    >>> import os
    >>> from astropy.utils.data import get_pkg_data_filename
    >>> filename = get_pkg_data_filename(
    ...     os.path.join('data', 'hst_acs_hrc_f555w.fits'),
    ...     package='synphot.tests')

You could parameterize a given filter using
:func:`~synphot.filter_parameterization.filter_to_fft` as follows.
By default, 10 FFT parameters are returned as complex numbers::

    >>> from synphot import SpectralElement
    >>> from synphot.filter_parameterization import filter_to_fft
    >>> filename = 'hst_acs_hrc_f555w.fits'  # doctest: +SKIP
    >>> bp = SpectralElement.from_file(filename)
    >>> n_lambda, lambda_0, delta_lambda, tr_max, fft_pars = filter_to_fft(bp)
    >>> n_lambda  # Number of elements in wavelengths
    10000
    >>> lambda_0  # Starting value of wavelengths  # doctest: +FLOAT_CMP
    <Quantity 3479.999 Angstrom>
    >>> delta_lambda  # Median wavelength separation  # doctest: +FLOAT_CMP
    <Quantity 0.66748047 Angstrom>
    >>> tr_max  # Peak value of throughput  # doctest: +FLOAT_CMP
    <Quantity 0.241445>
    >>> fft_pars  # FFT parameters  # doctest: +FLOAT_CMP
    [(407.5180314841658+7.494005416219807e-16j),
     (-78.52240189503877-376.53990235136575j),
     (-294.86589196496584+127.25464850352665j),
     (130.20273803287864+190.84263652863257j),
     (96.62299079012317-91.70087676328245j),
     (-32.572468348727654-34.227696019221035j),
     (-8.051741476066471-21.354793540998294j),
     (-51.708676896903725+6.883836090870033j),
     (13.08719675518801+54.48177212720124j),
     (38.635087381362396-13.02803811279449j)]

It is up to you to decide how to store this data, though storing it in a
table format is recommended. In fact, if you have many filters to parameterize,
:func:`~synphot.filter_parameterization.filters_to_fft_table`
will store the results in a table for you::

    >>> from synphot.filter_parameterization import filters_to_fft_table
    >>> mapping = {'HST/ACS/HRC/F555W': (bp, None)}
    >>> filter_pars_table = filters_to_fft_table(mapping)
    >>> filter_pars_table  # doctest: +FLOAT_CMP +ELLIPSIS
    <Table length=1>
          filter      n_lambda ...                  fft_9
                               ...
          str17        int...  ...                complex128
    ----------------- -------- ... ---------------------------------------
    HST/ACS/HRC/F555W    10000 ... (38.635087381362396-13.02803811279449j)
    >>> filter_pars_table.write('my_filter_pars.fits')  # doctest: +SKIP

.. _filter_fft_construction:

Reconstructing Filter from FFT
------------------------------

Once you have a parameterized filter (see :ref:`filter_fft_generation`),
you can reconstruct it for use using
:func:`~synphot.filter_parameterization.filter_from_fft`.
Following from the example above::

    >>> from synphot.filter_parameterization import filter_from_fft
    >>> reconstructed_bp = filter_from_fft(
    ...     n_lambda, lambda_0, delta_lambda, tr_max, fft_pars)

For this particular example using HST ACS/HRC F555W filter, perhaps 10
parameters are not quite sufficient. Therefore, caution needs to be exercised
if you opt to parameterize your filters using this method.

.. plot::

    import os
    import matplotlib.pyplot as plt
    from astropy.utils.data import get_pkg_data_filename
    from synphot import SpectralElement
    from synphot.filter_parameterization import filter_to_fft, filter_from_fft
    filename = get_pkg_data_filename(
        os.path.join('data', 'hst_acs_hrc_f555w.fits'),
        package='synphot.tests')
    bp = SpectralElement.from_file(filename)
    fit_result = filter_to_fft(bp)
    reconstructed_bp = filter_from_fft(*fit_result)
    w = bp.waveset
    plt.plot(w, bp(w), 'b-', label='Original')
    plt.plot(w, reconstructed_bp(w), 'r--', label='Reconstructed')
    plt.xlim(3500, 8000)
    plt.xlabel('Wavelength (Angstrom)')
    plt.ylabel('Throughput')
    plt.title('HST ACS/HRC F555W')
    plt.legend(loc='upper right', numpoints=1)
