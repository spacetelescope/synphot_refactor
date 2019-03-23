.. doctest-skip-all

.. _astropy_synphot:

******************************
Synthetic Photometry (synphot)
******************************

Introduction
============

**synphot** simulates photometric data and spectra, observed or otherwise.
You can incorporate your own filters, spectra, and data. You can also use a
pre-defined standard star (Vega), bandpass, or extinction law. Furthermore, it
allows you to:

* Construct complicated composite spectra using different models.
* Simulate observations.
* Compute photometric properties such as count rate, effective wavelength, and
  effective stimulus.
* Manipulate a spectrum; e.g., applying redshift or normalize it to a given
  flux value in a given bandpass.
* Sample a spectrum at given wavelengths.
* Plot a quick-view of a spectrum.
* Perform repetitive operations such as simulating the observations of multiple
  type of sources through multiple bandpasses.

This package covers the general functionalities not related to any particular
observatory. If you use HST (and soon JWST), you might also be interested in
**stsynphot** (https://github.com/spacetelescope/stsynphot_refactor), which
covers synthetic photometry for the telescope(s).

If you use **synphot** in your work, please see
`CITATION <https://github.com/spacetelescope/synphot_refactor/blob/master/CITATION>`_
for details on how to cite it in your publications.

If you have questions or concerns regarding the software, please open an issue
at https://github.com/spacetelescope/synphot_refactor/issues (if not already
reported) or contact `STScI Help Desk <https://hsthelp.stsci.edu>`_.


.. _synphot-installation-setup:

Installation and Setup
======================

**synphot** works under both Python 2 and 3. It requires the following
packages:

* numpy (>= 1.9)
* astropy (>= 1.3)
* scipy (>= 0.14)
* matplotlib (optional for plotting)

You can install **synphot** using one of the following ways:

* From `AstroConda <http://astroconda.readthedocs.io/en/latest/>`_::

    conda install synphot -c http://ssb.stsci.edu/astroconda

* From standalone release::

    pip install git+https://github.com/spacetelescope/synphot_refactor.git@0.1

* From source (example shown is for the ``dev`` version)::

    git clone https://github.com/spacetelescope/synphot_refactor.git
    cd synphot_refactor
    python setup.py install

To use the pre-defined standard star, extinction laws, and bandpasses, it is
recommended that you copy
`synphot.cfg <https://github.com/spacetelescope/synphot_refactor/blob/master/synphot/synphot.cfg>`_
to your ``$HOME/.astropy/config/`` directory.
In doing so, you can avoid connecting directly to STScI HTTP service,
which is slower and might not be available all the time.

If necessary (i.e., if you are not an internal STScI user), replace
``/grp/hst/cdbs`` with your local directory name
(e.g., ``/my/local/dir/cdbs``), where you plan to store the data files.
Then, follow the instructions below to "install" the data files.

.. note::

    **synphot** data files are a minimal subset of those required by
    **stsynphot**. If you plan to use the latter anyway, please also read the
    instructions in its documentation.

To install local data files via HTTP into, say, ``/my/local/dir/cdbs``::

    >>> from synphot.util import download_data
    >>> file_list = download_data('/my/local/dir/cdbs')

If you have your own version of the data files that you wish to use, you can
modify ``synphot.cfg`` to point to your own copies without having to download
using the function above. However, before you do so, make sure that your own
file(s) can be read in successfully with
:func:`~synphot.specio.read_fits_spec`.
For example, if you want to use your own Johnson *V* throughput file, you
can modify this line in your ``$HOME/.astropy/config/synphot.cfg`` file::

    johnson_v_file = /my/other/dir/my_johnson_v.fits

Alternately, you can also take advantage of :ref:`astropy:astropy_config`
to manage **synphot** data files. For example, you can also temporarily use a
different Johnson *V* throughput file::

    >>> from synphot.config import conf
    >>> print(conf.johnson_v_file)
    /my/local/dir/cdbs/comp/nonhst/johnson_v_004_syn.fits
    >>> with conf.set_temp('johnson_v_file', '/my/other/dir/my_johnson_v.fits'):
    ...     print(conf.johnson_v_file)
    /my/other/dir/my_johnson_v.fits
    >>> print(conf.johnson_v_file)
    /my/local/dir/cdbs/comp/nonhst/johnson_v_004_syn.fits


.. _synphot_getting_started:

Getting Started
===============

This section only contains minimal examples showing how to use this package.
For detailed documentation, see :ref:`synphot_using`.

In the examples below, you will notice that most models are from
`synphot.models`, not ``astropy.modeling.models``, because the models in
``synphot`` have extra things like ``sampleset`` that are not (yet) available
in Astropy. Despite this, some models like
`~astropy.modeling.functional_models.Const1D` does not need the extra things to
work, so they can be used directly. When in doubt, see if a model is in
`synphot.models` first before using Astropy's.

.. plot::
    :include-source:

    from astropy import units as u
    from synphot import units, SourceSpectrum
    from synphot.models import (BlackBodyNorm1D, GaussianAbsorption1D,
                                GaussianFlux1D)
    from synphot.spectrum import BaseUnitlessSpectrum
    # Create a Gaussian absorption profile that absorps 80% of the flux at
    # 4000 Angstrom with a sigma of 20 Angstrom
    g_abs = BaseUnitlessSpectrum(GaussianAbsorption1D, amplitude=0.8,
                                 mean=4000, stddev=20)
    # Create a Gaussian emission line with the given total flux
    # centered at 3000 Angstrom with FWHM of 100 Angstrom
    g_em = SourceSpectrum(GaussianFlux1D,
                          total_flux=3.5e-13*u.erg/(u.cm**2 * u.s),
                          mean=3000, fwhm=100)
    # Create a blackbody source spectrum with a temperature of 6000 K
    bb = SourceSpectrum(BlackBodyNorm1D, temperature=6000)
    # Combine the above components to create a source spectrum that is twice
    # the original blackbody flux with the Gaussian emission and absorption
    # lines
    sp = g_abs * (g_em + 2 * bb)
    # Plot the spectrum, zooming in on the line features
    sp.plot(left=1, right=7000)

Sample the spectrum at 0.3 micron::

    >>> sp(0.3 * u.micron)
    <Quantity 0.0012685 PHOTLAM>

Or sample the same thing but in a different flux unit::

    >>> sp(0.3 * u.micron, flux_unit=units.FLAM)
    <Quantity 8.57716634e-15 FLAM>

Sample the spectrum at its native wavelength set::

    >>> sp(sp.waveset)
    <Quantity [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, ...,
               4.47483287e-05, 4.34264666e-05, 4.21423394e-05] PHOTLAM>

Models that built the spectrum::

    >>> print(sp)
    SourceSpectrum at z=0.0
    Model: CompoundModel2
    Inputs: ('x',)
    Outputs: ('y',)
    Model set size: 1
    Expression: ([0] + ([1] | [2])) * [3]
    Components:
        [0]: <GaussianFlux1D(amplitude=...>

        [1]: <BlackBodyNorm1D(temperature=6000.0)>

        [2]: <Scale(factor=2.0)>

        [3]: <GaussianAbsorption1D(amplitude=0.8, mean=4000.0, stddev=20.0)>
    Parameters:
        ...

Redshift the source spectrum by :math:`z = 0.2`::

   >>> sp.z = 0.2

Create a box-shaped bandpass centered at 4000 Angstrom with a width of
2000 Angstrom::

    >>> from synphot import SpectralElement
    >>> from synphot.models import Box1D
    >>> bp = SpectralElement(Box1D, amplitude=1, x_0=4000, width=2000)

Normalize the source spectrum to 1 Jy in a given box bandpass and
integrate it::

    >>> sp_rn = sp.normalize(1 * u.Jy, band=bp)
    >>> sp_rn.integrate()
    <Quantity 12901.13466265 ph / (cm2 s)>

Create an observation by passing the redshifted and normalized source spectrum
through the box bandpass::

    >>> from synphot import Observation
    >>> obs = Observation(sp_rn, bp)

Calculate the count rate of the observation above for an 2-meter telescope:

    >>> import numpy as np
    >>> area = np.pi * (1 * u.m) ** 2
    >>> area
    <Quantity 3.14159265 m2>
    >>> obs.countrate(area=area)
    <Quantity 24219651.1854991 ct / s>


.. _synphot_using:

Using **synphot**
=================

.. toctree::
   :maxdepth: 1

   synphot/overview
   synphot/from_pysyn_iraf
   synphot/bandpass
   synphot/spectrum
   synphot/observation
   synphot/formulae
   synphot/units
   synphot/tutorials

.. _synphot_history:

A Brief History
===============

A brief history: First, there was
`STSDAS SYNPHOT <http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?synphot.sys>`_.
Then, there was
ASTROLIB PYSYNPHOT (:ref:`Lim et al. 2015 <synphot-ref-lim2015>`), which
aimed at replacing STSDAS SYNPHOT using Python. In order to take advantage of
:ref:`astropy:astropy-modeling` and :ref:`astropy:astropy-units` and to
repurpose the functionality for a wider audience (other than HST users),
it was refactored again and separated into **synphot** and
**stsynphot** (see :ref:`astropy_synphot`).

.. _synphot_api:

API
===

.. automodapi:: synphot.binning
   :no-inheritance-diagram:

Also imports this C-extension to local namespace:

.. toctree::
   :maxdepth: 1

   synphot/c_ext

.. automodapi:: synphot.config
   :no-inheritance-diagram:

.. automodapi:: synphot.exceptions

.. automodapi:: synphot.models

.. automodapi:: synphot.observation

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


.. _synphot_biblio:

References
==========

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

.. _synphot-ref-lim2015:

Lim, P. L., Diaz, R. I., & Laidler, V. 2015, PySynphot User's Guide (Baltimore, MD: STScI), https://pysynphot.readthedocs.io/en/latest/

.. _synphot-ref-madau1995:

Madau, P., et al. 1995, ApJ, 441, 18

.. _synphot-ref-oke1974:

Oke, J. B., 1974, ApJS, 27, 21

.. _synphot-ref-rybicki1979:

Rybicki, G. B., & Lightman, A. P. 1979, Radiative Processes in Astrophysics (New York, NY: Wiley)

.. _synphot-ref-schneider1983:

Schneider, D. P., Gunn, J. E., & Hoessel J. G. 1983, ApJ, 264, 337
