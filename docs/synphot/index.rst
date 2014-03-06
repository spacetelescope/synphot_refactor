.. doctest-skip-all

.. _astropy_synphot:

**********************************
Synthetic Photometry (``synphot``)
**********************************

Introduction
============

This is a package for manipulating spectra. It is intended to be used for
synthetic photometry, i.e., constructing source spectra and spectral element
throughputs.

This package started out as
`IRAF SYNPHOT <http://www.stsci.edu/institute/software_hardware/stsdas/synphot>`_
and eventually `ASTROLIB PYSYNPHOT <http://stsdas.stsci.edu/pysynphot/>`_
used by `Hubble Space Telescope (HST) <http://www.stsci.edu/hst>`_ calibrations.
They are maintained by
`Space Telescope Science Institute (STScI) <http://www.stsci.edu>`_.


Getting Started
===============

This section only contains minimal examples showing how to use this package.

>>> from astropy import units as u
>>> from synphot import units
>>> from synphot import BaseUnitlessSpectrum, SourceSpectrum
>>> from synphot.models import GaussianAbsorption1D

Create a Gaussian absorption profile that absorps 80% of the flux at
4000 Angstrom with :math:`\sigma` of 20 Angstrom:

>>> g_abs = BaseUnitlessSpectrum(
...     GaussianAbsorption1D, amplitude=0.8, mean=4000, stddev=20)

Create a Gaussian emission line with a total flux of 0.05 PHOTLAM centered at
3000 Angstrom with FWHM of 100 Angstrom:

>>> g_em = SourceSpectrum.from_gaussian(0.05 * units.PHOTLAM, 3000, 100)

Create a blackbody source spectrum with a temperature of 6000 K:

>>> bb =  SourceSpectrum.from_blackbody(6000)

Combine the above components to create a source spectrum that is twice the
original blackbody flux with the Gaussian emission and absorption lines:

>>> sp = g_abs * (g_em + 2 * bb)

Plot the spectrum, zooming in on the line features:

>>> sp.plot(left=1, right=7000)

.. image:: images/src_spec_ex1.png
    :width: 600px
    :alt: Plotted spectrum.

Sample the spectrum at 0.3 micron:

>>> sp(0.3 * u.micron)
<Quantity 0.001268063356632316 PHOTLAM>

Models that built the spectrum:

>>> print(sp)
SourceSpectrum at z=0.0
            Model:  MultipliedModel
            Model:  SummedModel
             Model: Gaussian1D
n_inputs:   1
Degree: N/A
Parameter sets: 1
Parameters:
           amplitude: Parameter('amplitude', value=0.00046971863935)
           mean: Parameter('mean', value=3000.0)
           stddev: Parameter('stddev', value=42.4660900144)
            Model:  MultipliedModel
            Model:  MultipliedModel
             Model: BlackBody1D
n_inputs:   1
Degree: N/A
Parameter sets: 1
Parameters:
           temperature: Parameter('temperature', value=6000.0)
   Model: _Const
n_inputs:   1
Degree: N/A
Parameter sets: 1
Parameters:
           amplitude: Parameter('amplitude', value=1.59607406911e-21)
     Model: _Const
n_inputs:   1
Degree: N/A
Parameter sets: 1
Parameters:
           amplitude: Parameter('amplitude', value=2.0)
       Model: GaussianAbsorption1D
n_inputs:   1
Degree: N/A
Parameter sets: 1
Parameters:
           amplitude: Parameter('amplitude', value=0.8)
           mean: Parameter('mean', value=4000.0)
           stddev: Parameter('stddev', value=20.0)

Redshift the source spectrum by :math:`z = 0.2`:

>>> sp.z = 0.2

Normalize the source spectrum to 1 Jy and integrate it:

>>> sp_rn = sp.normalize(1 * u.Jy)
>>> sp_rn.integrate()
<Quantity 16420.940685022673 PHOTLAM>

Create a box-shaped bandpass centered at 4000 Angstrom with a width of
2000 Angstrom:

>>> from synphot import SpectralElement
>>> from modeling import models  # Has to support composite model and sampleset
>>> bp = SpectralElement(models.Box1D, amplitude=1, x_0=4000, width=2000)

Create an observation by passing the redshifted and normalized source spectrum
through the bandpass:

>>> from synphot import Observation
>>> obs = Observation(sp_rn, bp)

Calculate the count rate of the observation above for an 2-meter telescope:

>>> import numpy as np
>>> area = np.pi * (1 * u.m) ** 2
>>> area
<Quantity 3.141592653589793 m2>
>>> obs.countrate(area=area)
<Quantity 277451343.66660804 ct / s>


Using ``synphot``
=================

.. toctree::
   :maxdepth: 1

   units
   formulae
   spectrum
   observation
   reddening
   thermal
   fromiraf
   accuracy


See Also
========

.. _synphot-ref-extinction-calzetti2000:

Calzetti, D., Armus, L., Bohlin, R. C., Kinney, A. L., Koornneef, J., & Storchi-Bergmann, T. 2000, ApJ, 533, 682

.. _synphot-ref-extinction-cardelli1989:

Cardelli, J. A., Clayton, G. C., & Mathis, J. S. 1989, ApJ, 345, 245

.. _synphot-ref-extinction-gordon2003:

Gordon, K. D., Clayton, G. C., Misselt, K. A., Landolt, A. U., & Wolff, M. J. 2003, ApJ, 594, 279

.. _synphot-ref-horne1988:

Horne, K. 1988, in New Directions in Spectophotometry: A Meeting Held in Las Vegas, NV, March 28-30, Application of Synthetic Photometry Techniques to Space Telescope Calibration, ed. A. G. Davis Philip, D. S. Hayes, & S. J. Adelman (Schenectady, NY: L. Davis Press), 145

.. _synphot-ref-koornneef1986:

Koornneef, J., Bohlin, R., Buser, R., Horne, K., & Turnshek, D. 1986, Highlights Astron., 7, 833

.. _synphot-ref-laidler2008:

Laidler, V., et al. 2008, Synphot Data User's Guide, Version 1.2 (Baltimore, MD: STScI)

.. _synphot-ref-rybicki1979:

Rybicki, G. B., & Lightman, A. P. 1979, Radiative Processes in Astrophysics (New York, NY: Wiley)


Reference/API
=============

.. automodapi:: synphot.binning
   :no-inheritance-diagram:

Also imports this C-extension to local namespace:

.. toctree::
   :maxdepth: 1

   c_ext

.. automodapi:: synphot.exceptions

.. automodapi:: synphot.integrator

.. automodapi:: synphot.models

.. automodapi:: synphot.observation

.. automodapi:: synphot.planck
   :no-inheritance-diagram:

.. automodapi:: synphot.reddening

.. automodapi:: synphot.specio
   :no-inheritance-diagram:

.. automodapi:: synphot.spectrum
   :no-inheritance-diagram:

.. automodapi:: synphot.thermal

.. automodapi:: synphot.units
   :no-inheritance-diagram:

.. automodapi:: synphot.utils
   :no-inheritance-diagram:
