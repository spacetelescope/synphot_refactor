.. doctest-skip-all

.. _synphot_units:

Photometry Units
================

These are the flux units used by ``synphot``:

+-------------------------+------------------------------------------------------+
|Flux representation      | Unit                                                 |
+=========================+======================================================+
|``synphot.units.PHOTLAM``|:math:`photon \; s^{-1} \; cm^{-2} \; \AA^{-1}`       |
+-------------------------+------------------------------------------------------+
|``synphot.units.PHOTNU`` |:math:`photon \; s^{-1} \; cm^{-2} \; Hz^{-1}`        |
+-------------------------+------------------------------------------------------+
|``synphot.units.FLAM``   |:math:`erg \; s^{-1} \; cm^{-2} \; \AA^{-1}`          |
+-------------------------+------------------------------------------------------+
|``synphot.units.FNU``    |:math:`erg \; s^{-1} cm^{-2} Hz^{-1}`                 |
+-------------------------+------------------------------------------------------+
|``synphot.units.STMAG``  |:math:`-2.5 \times log_{10}(FLAM) - 21.10`            |
+-------------------------+------------------------------------------------------+
|``synphot.units.ABMAG``  |:math:`-2.5 \times log_{10}(FNU)  - 48.60`            |
+-------------------------+------------------------------------------------------+
|``synphot.units.OBMAG``  |:math:`-2.5 \times log_{10}(count)`                   |
+-------------------------+------------------------------------------------------+
|``synphot.units.VEGAMAG``|:math:`-2.5 \times log_{10}(\frac{flux}{flux_{Vega}})`|
+-------------------------+------------------------------------------------------+
|``astropy.units.count``  |:math:`photon \; s^{-1}`                              |
+-------------------------+------------------------------------------------------+
|``astropy.units.Jy``     |:math:`10^{-23} \; erg \; s^{-1} \; cm^{-2} Hz^{-1}`  |
+-------------------------+------------------------------------------------------+

``synphot.units.THROUGHPUT`` is a special dimensionless unit used by unitless
spectra like bandpass and extinction curve.

These are the magnitude zeropoints:

+------------------------+-------+-----------+
|Zeropoint               |Used by|Value (mag)|
+========================+=======+===========+
|``synphot.units.STZERO``| STMAG | -21.1     |
+------------------------+-------+-----------+
|``synphot.units.ABZERO``| ABMAG | -48.6     |
+------------------------+-------+-----------+


.. _synphot-wave-conversion:

Wavelength Conversion
---------------------

:func:`~astropy.units.equivalencies.spectral` equivalencies are used for
wavelength conversion between length, wave number, and frequency, as shown in
examples below:

>>> from astropy import units as u
>>> wave = 4000 * u.AA
>>> wave
<Quantity 4000.0 Angstrom>
>>> wave.to(u.micron ** -1, u.spectral())
<Quantity 2.4999999999999996 1 / micron>
>>> wave.to(u.Hz, u.spectral())
<Quantity 749481144999999.9 Hz>


.. _synphot-flux-conversion:

Flux Conversion
---------------

When possible :func:`~astropy.units.equivalencies.spectral_density` is used for
flux conversion. Otherwise, equivalencies in `synphot.units` are used.

Examples:

>>> from astropy import units as u
>>> from synphot import units
>>> wave = [1000, 4000, 10000] * u.AA
>>> flux_photlam = [0.1, 1.0, 100] * units.PHOTLAM
>>> units.convert_flux(wave, flux_photlam, units.FLAM)
<Quantity [  1.98644568e-12,  4.96611421e-12,  1.98644568e-10] FLAM>
>>> units.convert_flux(wave, flux_photlam, u.mJy)
<Quantity [  6.62606957e+01,  2.65042783e+03,  6.62606957e+05] mJy>

Telescope primary area is needed for conversion that involves count or OBMAG.
For example, a 6-meter telescope:

>>> import numpy as np
>>> area = np.pi * (3 * u.m) ** 2
>>> area
<Quantity 28.274333882308138 m2>
>>> units.convert_flux(wave, flux_photlam, u.count, area=area)
<Quantity [  8.48230016e+07,  1.27234502e+09,  1.69646003e+11] ct>

Vega spectrum is needed for conversion that involves VEGAMAG:

>>> from synphot import SourceSpectrum
>>> vegaspec = SourceSpectrum.from_vega(encoding='binary')
Downloading ftp://ftp.stsci.edu/cdbs/calspec/alpha_lyr_stis_007.fits
|===========================================| 241k/241k (100.00%)        01s
>>> units.convert_flux(wave, flux_photlam, units.VEGAMAG, vegaspec=vegaspec)
<Quantity [-1.41263038, 8.05576758, 1.25874345] VEGAMAG>
