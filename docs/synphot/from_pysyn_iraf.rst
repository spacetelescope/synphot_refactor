.. doctest-skip-all

.. _synphot-switcher:

Switching from Legacy Software
==============================

This section provides basic switcher's guide for those who are familar with
ASTROLIB PYSYNPHOT or IRAF SYNPHOT. This guide is not meant to be
all-inclusive; Therefore, not all legacy commands are listed here.
This is because a legacy command can be reproduced in several different ways
using **synphot** or has no equivalent implementation.
Naming convention used is the same as :ref:`synphot-quick-guide`
Please contact `STScI Help Desk <https://hsthelp.stsci.edu>`_ if you have
any questions.


.. _synphot-pysyn-switcher:

ASTROLIB Switcher Guide
-----------------------

Bandpass
^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |ASTROLIB PYSYNPHOT                    |
+======================================+======================================+
|SpectralElement.from_file(filename)   |FileBandpass(filename)                |
+--------------------------------------+--------------------------------------+
|SpectralElement.from_filter(filter)   |ObsBandpass(filter)                   |
+--------------------------------------+--------------------------------------+
|SpectralElement(Empirical1D,          |ArrayBandpass(wavelength=wave,        |
|points=wave, lookup_table=thru)       |throughput=thru)                      |
+--------------------------------------+--------------------------------------+
|SpectralElement(Box1D, amplitude=1,   |Box(mu, width)                        |
|x_0=mu, width=width)                  |                                      |
+--------------------------------------+--------------------------------------+
|bp.waveset                            |bp.wave                               |
+--------------------------------------+--------------------------------------+
|bp(bp.waveset)                        |bp.throughput                         |
+--------------------------------------+--------------------------------------+
|bp.taper()                            |bp.taper()                            |
+--------------------------------------+--------------------------------------+
|bp.avgwave()                          |bp.avgwave()                          |
+--------------------------------------+--------------------------------------+
|bp.tlambda()                          |bp(bp.avgwave())                      |
+--------------------------------------+--------------------------------------+
|bp.tpeak()                            |bp.throughput.max()                   |
+--------------------------------------+--------------------------------------+
|bp.wpeak()                            |bp.wave[bp.throughput ==              |
|                                      |bp.throughput.max()]                  |
+--------------------------------------+--------------------------------------+
|bp.efficiency()                       |bp.efficiency()                       |
+--------------------------------------+--------------------------------------+
|bp.equivwidth()                       |bp.equivwidth()                       |
+--------------------------------------+--------------------------------------+
|bp.rectwidth()                        |bp.rectwidth()                        |
+--------------------------------------+--------------------------------------+
|bp.rmswidth()                         |bp.rmswidth()                         |
+--------------------------------------+--------------------------------------+
|bp.photbw()                           |bp.photbw()                           |
+--------------------------------------+--------------------------------------+
|bp.pivot()                            |bp.pivot()                            |
+--------------------------------------+--------------------------------------+
|bp.unit_response(area)                |bp.unit_response()                    |
+--------------------------------------+--------------------------------------+
|bp.emflx(area)                        |bp.unit_response() * bp.equivwidth() /|
|                                      |bp(bp.avgwave())                      |
+--------------------------------------+--------------------------------------+
|bp.check_overlap(sp)                  |bp.check_overlap(sp)                  |
+--------------------------------------+--------------------------------------+
|bp.to_fits(filename)                  |bp.writefits(filename)                |
+--------------------------------------+--------------------------------------+
|bp.plot()                             |matplotlib.pyplot.plot(bp.wave,       |
|                                      |bp.throughput)                        |
+--------------------------------------+--------------------------------------+

Source Spectrum
^^^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |ASTROLIB PYSYNPHOT                    |
+======================================+======================================+
|SourceSpectrum.from_file(filename)    |FileSpectrum(filename)                |
+--------------------------------------+--------------------------------------+
|SourceSpectrum.from_vega()            |Vega                                  |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(Empirical1D,           |ArraySpectrum(wave=wave, flux=flux)   |
|points=wave, lookup_table=flux)       |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(BlackBodyNorm1D,       |BlackBody(teff)                       |
|temperature=teff)                     |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(ConstFlux1D,           |FlatSpectrum(val, fluxunits=form)     |
|amplitude=val*form)                   |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(PowerLawFlux1D,        |Powerlaw(refval, expon,               |
|amplitude=1*form, x_0=refval,         |fluxunits=form)                       |
|alpha=expon)                          |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(GaussianFlux1D, mean=mu|GaussianSource(flux, mu, fwhm,        |
|, fwhm=fwhm, total_flux=flux)         |fluxunits=form)                       |
+--------------------------------------+--------------------------------------+
|sp.waveset                            |sp.wave                               |
+--------------------------------------+--------------------------------------+
|sp(sp.waveset)                        |sp.flux                               |
+--------------------------------------+--------------------------------------+
|sp.taper()                            |sp.taper()                            |
+--------------------------------------+--------------------------------------+
|sp.normalize(val*form, band=bp)       |sp.renorm(val, form, bp)              |
+--------------------------------------+--------------------------------------+
|sp * extcurve                         |sp * extcurve                         |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(sp.model, z=z)         |sp.redshift(z)                        |
+--------------------------------------+--------------------------------------+
|sp.to_fits(filename)                  |sp.writefits(filename)                |
+--------------------------------------+--------------------------------------+
|sp.plot()                             |matplotlib.pyplot.plot(sp.wave,       |
|                                      |sp.flux)                              |
+--------------------------------------+--------------------------------------+

Observation
^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |ASTROLIB PYSYNPHOT                    |
+======================================+======================================+
|Observation(sp, bp, binset=binset)    |Observation(sp, bp, binset=binset)    |
+--------------------------------------+--------------------------------------+
|obs.waveset                           |obs.wave                              |
+--------------------------------------+--------------------------------------+
|obs(obs.waveset)                      |obs.flux                              |
+--------------------------------------+--------------------------------------+
|obs.binset                            |obs.binwave                           |
+--------------------------------------+--------------------------------------+
|obs.binflux                           |obs.binflux                           |
+--------------------------------------+--------------------------------------+
|obs(wave)                             |obs.sample(wave, binned=False)        |
+--------------------------------------+--------------------------------------+
|obs.sample_binned(wave)               |obs.sample(wave)                      |
+--------------------------------------+--------------------------------------+
|obs.effective_wavelength()            |obs.efflam()                          |
+--------------------------------------+--------------------------------------+
|obs.effstim(flux_unit=form)           |obs.effstim(form)                     |
+--------------------------------------+--------------------------------------+
|obs.countrate(area)                   |obs.countrate()                       |
+--------------------------------------+--------------------------------------+
|obs.as_spectrum()                     |obs.as_spectrum()                     |
+--------------------------------------+--------------------------------------+
|obs.as_spectrum().to_fits(filename)   |obs.writefits(filename)               |
+--------------------------------------+--------------------------------------+
|obs.plot()                            |matplotlib.pyplot.plot(obs.binwave,   |
|                                      |obs.binflux)                          |
+--------------------------------------+--------------------------------------+
|obs.plot(binned=False)                |matplotlib.pyplot.plot(obs.wave,      |
|                                      |obs.flux)                             |
+--------------------------------------+--------------------------------------+

Miscellaneous
^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |ASTROLIB PYSYNPHOT                    |
+======================================+======================================+
|ReddeningLaw.from_extinction_model(law|Extinction(val, law)                  |
|).extinction_curve(val)               |                                      |
+--------------------------------------+--------------------------------------+
|generate_wavelengths(minwave=w1,      |Waveset(w1, w2, dw)                   |
|maxwave=w2, delta=dw)                 |                                      |
+--------------------------------------+--------------------------------------+

.. _synphot-iraf-switcher:

IRAF Switcher Guide
-------------------

Bandpass
^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |IRAF SYNPHOT                          |
+======================================+======================================+
|SpectralElement.from_file(filename)   |thru(filename)                        |
+--------------------------------------+--------------------------------------+
|SpectralElement.from_filter(filter)   |band(filter)                          |
+--------------------------------------+--------------------------------------+
|SpectralElement(Box1D, amplitude=1,   |box(mu, width)                        |
|x_0=mu, width=width)                  |                                      |
+--------------------------------------+--------------------------------------+
|bp.avgwave()                          |bandpar bp photlist=avglam            |
+--------------------------------------+--------------------------------------+
|bp.tlambda()                          |bandpar bp photlist=tlambda           |
+--------------------------------------+--------------------------------------+
|bp.tpeak()                            |bandpar bp photlist=tpeak             |
+--------------------------------------+--------------------------------------+
|bp.wpeak()                            |bandpar bp photlist=wpeak             |
+--------------------------------------+--------------------------------------+
|bp.efficiency()                       |bandpar bp photlist=qtlam             |
+--------------------------------------+--------------------------------------+
|bp.equivwidth()                       |bandpar bp photlist=equvw             |
+--------------------------------------+--------------------------------------+
|bp.rectwidth()                        |bandpar bp photlist=rectw             |
+--------------------------------------+--------------------------------------+
|bp.photbw()                           |bandpar bp photlist=bandw             |
+--------------------------------------+--------------------------------------+
|bp.fwhm()                             |bandpar bp photlist=fwhm              |
+--------------------------------------+--------------------------------------+
|bp.pivot()                            |bandpar bp photlist=pivwv             |
+--------------------------------------+--------------------------------------+
|bp.unit_response(area)                |bandpar bp photlist=uresp             |
+--------------------------------------+--------------------------------------+
|bp.emflx(area)                        |bandpar bp photlist=emflx             |
+--------------------------------------+--------------------------------------+
|bp.to_fits(filename)                  |calcband bp filename                  |
+--------------------------------------+--------------------------------------+
|bp.plot()                             |plband bp                             |
+--------------------------------------+--------------------------------------+

Source Spectrum
^^^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |IRAF SYNPHOT                          |
+======================================+======================================+
|SourceSpectrum.from_file(filename)    |spec(filename)                        |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(BlackBodyNorm1D,       |bb(teff)                              |
|temperature=teff)                     |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(ConstFlux1D,           |unit(val, form)                       |
|amplitude=val*form)                   |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(PowerLawFlux1D,        |pl(refval, expon, form)               |
|amplitude=1*form, x_0=refval,         |                                      |
|alpha=expon)                          |                                      |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(GaussianFlux1D, mean=mu|em(mu, fwhm, flux, form)              |
|, fwhm=fwhm, total_flux=flux)         |                                      |
+--------------------------------------+--------------------------------------+
|sp.normalize(val*form, band=bp)       |rn(sp, bp, val, form)                 |
+--------------------------------------+--------------------------------------+
|SourceSpectrum(sp.model, z=z)         |z(sp, z)                              |
+--------------------------------------+--------------------------------------+
|sp.to_fits(filename)                  |calcspec sp filename                  |
+--------------------------------------+--------------------------------------+

Observation
^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |IRAF SYNPHOT                          |
+======================================+======================================+
|obs.effective_wavelength()            |calcphot bp sp flam func='efflerg'    |
+--------------------------------------+--------------------------------------+
|obs.effstim(flux_unit=form)           |calcphot bp sp form                   |
+--------------------------------------+--------------------------------------+
|obs.countrate(area)                   |calcphot bp sp counts                 |
+--------------------------------------+--------------------------------------+
|obs.plot(flux_unit=form)              |plspec bp sp form                     |
+--------------------------------------+--------------------------------------+

Miscellaneous
^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------+
|**synphot**                           |IRAF SYNPHOT                          |
+======================================+======================================+
|ReddeningLaw.from_extinction_model(law|ebmvx(val, law)                       |
|).extinction_curve(val)               |                                      |
+--------------------------------------+--------------------------------------+
|generate_wavelengths(minwave=w1,      |genwave filename w1 w2 dw             |
|maxwave=w2, delta=dw)                 |                                      |
+--------------------------------------+--------------------------------------+
