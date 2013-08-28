.. _astropy_synphot:

**********************************
Synthetic Photometry (``synphot``)
**********************************

Introduction
============

This is a module for manipulating spectra. It is intended to be used for
synthetic photometry, i.e., constructing source spectra and spectral element
throughputs.

This package started out as IRAF SYNPHOT used by Hubble Space Telescope
calibrations.


Getting Started
===============

This section only contains minimal examples.


Using ``synphot``
=================

.. toctree::
   :maxdepth: 1

   units
   formulae
   spectrum
   reddening
   fromiraf
   accuracy


See Also
========

.. synphot-ref-extinction-calzetti2000: Calzetti, D., Armus, L., Bohlin, R. C., Kinney, A. L., Koornneef, J., & Storchi-Bergmann, T. 2000, ApJ, 533, 682

.. synphot-ref-extinction-cardelli1989: Cardelli, J. A., Clayton, G. C., & Mathis, J. S. 1989, ApJ, 345, 245

.. synphot-ref-extinction-gordon2003: Gordon, K. D., Clayton, G. C., Misselt, K. A., Landolt, A. U., & Wolff, M. J. 2003, ApJ, 594, 279

.. synphot-ref-horne1988: Horne, K. 1988, in New Directions in Spectophotometry: A Meeting Held in Las Vegas, NV, March 28-30, Application of Synthetic Photometry Techniques to Space Telescope Calibration, ed. A. G. Davis Philip, D. S. Hayes, & S. J. Adelman (Schenectady, NY: L. Davis Press), 145

.. synphot-ref-koornneef1986: Koornneef, J., Bohlin, R., Buser, R., Horne, K., & Turnshek, D. 1986, Highlights Astron., 7, 833

.. synphot-ref-laidler2008: Laidler, V., et al. 2008, Synphot Data User's Guide, Version 1.2 (Baltimore, MD: STScI)

.. synphot-ref-rybicki1979: Rybicki, G. B., & Lightman, A. P. 1979, Radiative Processes in Astrophysics (New York, NY: Wiley)


Reference/API
=============

.. automodapi:: synphot.units
   :no-inheritance-diagram:

.. automodapi:: synphot.spectrum
   :no-inheritance-diagram:

.. automodapi:: synphot.observation
   :no-inheritance-diagram:

.. automodapi:: synphot.planck
   :no-inheritance-diagram:

.. automodapi:: synphot.reddening
   :no-inheritance-diagram:

.. automodapi:: synphot.binning
   :no-inheritance-diagram:
   :hidden-members:

.. automodapi:: synphot.synutils
   :no-inheritance-diagram:

.. automodapi:: synphot.synio
   :no-inheritance-diagram:

.. automodapi:: synphot.synexceptions
   :no-inheritance-diagram:

.. automodapi:: synphot.synconfig
   :no-inheritance-diagram:


Version
=======

.. autodata:: synphot.ver.__version__
.. autodata:: synphot.ver.__vdate__
