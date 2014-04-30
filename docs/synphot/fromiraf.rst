.. doctest-skip-all

.. synphot-iraf-switcher:

Switching from Legacy SYNPHOT/PYSYNPHOT
=======================================

This section provides basic switcher's guide for those who are familar with
IRAF SYNPHOT or ASTROLIB PYSYNPHOT. This guide is not meant to be all-inclusive.
Therefore, not all legacy commands are listed here. Please contact
``help[at]stsci.edu`` if you have any questions.

In the following examples, for simplicity:

>>> import matplotlib.pyplot as plt
>>> from modeling import models  # Has to support composite model and sampleset
>>> import synphot as S  # This package
>>> import pysynphot as S  # ASTROLIB PYSYNPHOT


Spectra
-------

==================================================================================== =================================================== ===========================
``synphot``                                                                          ASTROLIB PYSYNPHOT                                  IRAF SYNPHOT
==================================================================================== =================================================== ===========================
S.SourceSpectrum.from_file(filename)                                                 S.FileSpectrum(filename)                            spec(filename)
S.SourceSpectrum.from_blackbody(temperature)                                         S.BlackBody(temperature)                            bb(temperature)
S.SourceSpectrum(S.models.ConstFlux1D, amplitude=val*form)                           S.FlatSpectrum(val, fluxunits=form)                 unit(val, form)
S.SourceSpectrum(S.models.PowerLawFlux1D, amplitude=1*form, x_0=refval, alpha=expon) S.Powerlaw(refval, expon, fluxunits=form)           pl(refval, expon, form)
S.SourceSpectrum.from_gaussian(totflux*form, mu, fwhm)                               S.GaussianSource(totflux, mu, fwhm, fluxunits=form) em(mu, fwhm, totflux, form)
S.SourceSpectrum(S.models.Empirical1D, x=ww, y=ff*form)                              S.ArraySpectrum(wave=ww, flux=ff, fluxunits=form)   N/A
sp.normalize(val*form, band=bp)                                                      sp.renorm(val, form, bp)                            rn(sp, bp, val, form)
sp.z = z                                                                             sp.redshift(z)                                      z(sp, z)
sp.to_fits(filename)                                                                 sp.writefits(filename)                              calcspec sp filename
sp.plot()                                                                            plt.plot(sp.wave, sp.flux)                          N/A
==================================================================================== =================================================== ===========================


Bandpasses
----------

================================================================= ================================ ==========================
``synphot``                                                       ASTROLIB PYSYNPHOT               IRAF SYNPHOT
================================================================= ================================ ==========================
S.SpectralElement.from_file(filename)                             S.FileBandpass(filename)         thru(filename)
S.SpectralElement(models.Box1D, amplitude=1, x_0=mu, width=width) S.Box(mu, width)                 box(mu, width)
bp.avgwave()                                                      bp.avgwave()                     bandpar bp photlist=avglam
bp.efficiency()                                                   bp.efficiency()                  bandpar bp photlist=qtlam
bp.equivwidth()                                                   bp.equivwidth()                  bandpar bp photlist=equvw
bp.rectwidth()                                                    bp.rectwidth()                   bandpar bp photlist=rectw
bp.photbw()                                                       bp.photbw()                      bandpar bp photlist=bandw
bp.tpeak()                                                        bp.throughput.max()              bandpar bp photlist=tpeak
bp.to_fits(filename)                                              bp.writefits(filename)           calcband bp filename
bp.plot()                                                         plt.plot(bp.wave, bp.throughput) plband bp
================================================================= ================================ ==========================


Observations
------------

=================================== ================================== ==================================
``synphot``                         ASTROLIB PYSYNPHOT                 IRAF SYNPHOT
=================================== ================================== ==================================
S.Observation(sp, bp)               S.Observation(sp, bp)              N/A
obs.countrate(area)                 obs.countrate()                    calcphot bp sp counts
obs.effstim(flux_unit=form)         obs.effstim(form)                  calcphot bp sp form
obs.effective_wavelength()          obs.efflam()                       calcphot bp sp flam func='efflerg'
obs.as_spectrum().to_fits(filename) obs.writefits(filename)            N/A
obs.plot()                          plt.plot(obs.binwave, obs.binflux) plspec bp sp photlam
=================================== ================================== ==================================


Miscellaneous
-------------

=============================================================== ====================== =========================
``synphot``                                                     ASTROLIB PYSYNPHOT     IRAF SYNPHOT
=============================================================== ====================== =========================
S.ReddeningLaw.from_extinction_model(law).extinction_curve(val) S.Extinction(val, law) ebmvx(val, law)
S.utils.generate_wavelengths(minwave=w1, maxwave=w2, delta=dw)  S.Waveset(w1, w2, dw)  genwave filename w1 w2 dw
=============================================================== ====================== =========================


See Also
--------
`Introduction to Pysynphot for Synphot Users <http://stsdas.stsci.edu/pysynphot/Introduction_to_Pysynphot_for_Synphot_Users.html>`_
