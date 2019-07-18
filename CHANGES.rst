0.2.0 (unreleased)
==================

- Removed Python 2 support. This version is only compatible with Python 3.5
  or later. [#185]
- New ``synphot.observation.howell_snr()`` function to calculate the signal
  to noise ratio given a count rate and exposure time.
- New ``synphot.observation.exptime_from_howell_snr()`` function to
  determine the exposure time needed to achieve a given signal to noise
  ratio.

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
