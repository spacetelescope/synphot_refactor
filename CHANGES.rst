0.3.0 (unreleased)
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
