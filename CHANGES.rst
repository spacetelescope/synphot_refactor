1.4.0 (2024-04-11)
==================

- ``read_fits_spec()`` now uses ``astropy.table.QTable.read`` for parsing to
  ensure that the correct ``TUNITn`` is read. As a result, ``wave_unit`` and
  ``flux_unit`` keywords are deprecated and no longer used in that function.
  Additionally, if any ``TUNITn`` in the table is invalid, regardless whether
  the column is used or not, an exception will now be raised. [#384]

- ``read_spec()`` now detects whether given filename is FITS more consistently
  w.r.t. ``astropy``. [#384]

- Compatibility with ``numpy`` 2.0 and ``astropy`` 6.1 by building C-extension
  against ``numpy`` 2.x ABI. [#387]

- Bumped minimum supported versions for Python to 3.10,
  ``numpy`` to 1.23, ``astropy`` to 6.0, and ``scipy`` to 1.9. [#387]

1.3.0 (2023-11-28)
==================

- Compatibility with ``numpy`` 2.0. [#363]

- Bumped minimum supported versions for Python to 3.9,
  ``numpy`` to 1.20, ``astropy`` to 5.0, and ``scipy`` to 1.6. [#363]

- Wheels for Python 3.12.

1.2.1 (2023-06-01)
==================

- Compatibility with ``numpy`` 1.25. [#356]

1.2.0 (2023-03-20)
==================

- New ``filter_parameterization`` subpackage to handle filter parameterization,
  adapted from ``tynt`` package written by Brett Morris. [#257]

- OBMAG and VEGAMAG are no longer interchangeable. [#331]

- ``Box1D`` model now takes optional ``step`` input to allow user control
  over the generated sampleset. Default behavior maintains backwards 
  compatibility. [#342]

- Dropped support for Python 3.6 and 3.7. Minimum supported Python
  version is now 3.8. [#330]

- Bumped minimum supported versions for ``numpy`` to 1.18,
  ``astropy`` to 4.3, and ``scipy`` to 1.3. [#341]

- Added wheel for OSX ARM64 architecture. [#352]

1.1.1 (2021-11-18)
==================

- Compatibility with ``astropy`` 5.0. [#321]

1.1.0 (2021-06-23)
==================

- ``synphot.synphot_utils`` C-extension is no longer optional. Your
  installation will fail if it cannot build. [#297]

- ``~/.astropy/config/synphot.cfg`` is no longer updated on import. [#307]

- Compatibility with ``numpy`` 1.20 and ``astropy`` 4.3. [#301, #309, #311]

1.0.1 (2020-08-03)
==================

- Fix for ``conda`` build. Does not affect functionalities. [#279]

1.0.0 (2020-07-31)
==================

- Default Vega is now ``alpha_lyr_stis_010.fits``. [#266]
- CDBS is now TRDS. [#278]

0.3.0 (2020-03-17)
==================

- ``SourceSpectrum`` and ``SpectralElement`` now have ``to_spectrum1d`` and
  ``from_spectrum1d`` to write to and read from ``specutils.Spectrum1D``
  object, respectively. [#243]
- ``Observation`` now accepts ``specutils.Spectrum1D`` as a valid source
  spectrum input. [#246]
- Dropped support for Python 3.5 and ``astropy`` 2.x. This version is only
  compatible with Python 3.6 or later and ``astropy`` 3.x or later. [#243]
- Added support for ``RickerWavelet1D`` model that is the renamed version
  of ``MexicanHat1D`` model to be consistent with ``astropy`` 4.0. [#250]
- Added support for extinction curve from ``dust-extinction``. [#251]
- Added option for ``synphot.utils.download_data()`` to download to the cache
  instead of a specific location. Please note that new option is not fully
  compatible with customization using ``synphot.cfg``. [#211]
- Added option to use analytic integral for some models. However, for backward
  compatibility, the default is still trapezoid integration. [#252]
- Trapezoid integration now provides unsigned area for ``RickerWavelet1D``.
  [#252]

0.2.1 (2019-12-20)
==================

- ``effstim`` now raises ``SynphotError`` properly when Vega spectrum
  is not given for VEGAMAG calculation. [#228]
- Infrastructure update in accordance to Astropy APE 17. [#229, #233]

0.2.0 (2019-11-19)
==================

- Use updated Vega spectrum for VEGAMAG. [#222]
- Compatibility with Numpy 1.17. [#212]
- Compatibility with ``astropy`` 4.0 models. [#201]
- Removed Python 2 support. This version is only compatible with Python 3.5
  or later. [#185]

0.1.3 (2019-03-24)
==================

- Config to use HTTP instead of FTP. [#171]
- New ``synphot.utils.download_data()`` function to help download data from
  STScI HTTP service. [#179]
- Fixed scalar unit conversion for VEGAMAG. [#174]
- Bug fix for ``effstim`` calculations in some flux units. [#159, #166]

0.1.2 (2018-07-19)
==================

Bug fix for GaussianFlux1D ``total_flux`` unit handling. [#154]

0.1.1 (2018-06-05)
==================

Bug fix for integrated unit. [#151]

0.1.0 (2018-01-19)
==================

First release.
