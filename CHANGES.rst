0.3.0 (unreleased)
==================

- ``effstim`` now raises ``SynphotError`` properly when Vega spectrum
  is not given for VEGAMAG calculation. [#228]
- Infrastructure update in accordance to Astropy APE 17. [#229]

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
