.. doctest-skip-all

.. _synphot-tutorials:

Tutorials
=========

This page contains tutorials of specific **synphot** functionality not
explicitly covered in other sections.


.. _tutorial_em_line:

Emission Line
-------------

This tutorial is adapted from
`Exposure Time Calculator User's Guide on a similar topic <http://etc.stsci.edu/etcstatic/users_guide/1_ref_8.5_emlines.html#using-synphot-to-modify-emission-lines>`_.
In this tutorial, you will learn how to manipulate and superimpose
an emission line to a continuum spectrum.

.. plot::
    :include-source:

    from synphot import SourceSpectrum, ReddeningLaw, units
    from synphot.models import BlackBodyNorm1D, GaussianFlux1D
    # Create a continuum spectrum of a 5500 K blackbody with z=0.6
    bb = SourceSpectrum(BlackBodyNorm1D, temperature=5500, z=0.6)
    # Create a Gaussian emission line with 8E-14 FLAM total flux,
    # FWHM of 100 Angstrom, and centered at 7000 Angstrom
    em = SourceSpectrum(
        GaussianFlux1D, total_flux=8e-14*units.FLAM, fwhm=100, mean=7000)
    # Add emission line to continuum spectrum
    sp = bb + em
    # Apply extinction curve for LMC (average) with E(B-V)=1.3
    # to the composite spectrum
    ext = ReddeningLaw.from_extinction_model('lmcavg').extinction_curve(1.3)
    my_spec = sp * ext
    # Plot the result
    my_spec.plot(right=45000)


.. _tutorial_continuum_norm:

Continuum-Normalized Spectrum
-----------------------------

In this tutorial, you will learn how to create a composite spectrum with a
noisy blackbody continuum, an emission line, and an absorption line.
Then, you will divide it by a smooth continuum and plot the resultant
continuum-normalized spectrum.

.. plot::
    :include-source:

    import matplotlib.pyplot as plt
    import numpy as np
    from synphot import SourceSpectrum, BaseUnitlessSpectrum
    from synphot.models import BlackBodyNorm1D, Empirical1D, GaussianFlux1D
    np.random.seed(1234)  # For reproducibility
    # Create the smooth continuum that is a 5000 K blackbody.
    bb = SourceSpectrum(BlackBodyNorm1D, temperature=5000)
    # Then, add random noise to it. Since synphot spectrum object cannot
    # be multiplied with scalar array, this has to be done indirectly by
    # applying the noise as a unitless spectrum.
    wave = np.arange(100, 30001, 10)
    nse = 1 + np.random.normal(size=wave.size, scale=0.02)
    sp_nse = BaseUnitlessSpectrum(Empirical1D, points=wave, lookup_table=nse)
    bb_noisy = bb * sp_nse
    # Apply emission and absorption lines to the noisy continuum.
    g_em = SourceSpectrum(
        GaussianFlux1D, total_flux=0.02, mean=15000, fwhm=500)
    g_ab = SourceSpectrum(
        GaussianFlux1D, total_flux=0.015, mean=4500, fwhm=100)
    sp = bb_noisy + g_em - g_ab
    # Divide the noisy spectrum with lines with the original smooth continuum
    # to obtain the continuum-normalized spectrum.
    ratio = sp / bb
    with np.errstate(invalid='ignore'):
        ratio.plot(left=2500, right=17000,
                   title='Continuum-normalized spectrum')
    plt.axhline(1, ls='--', color='k')
