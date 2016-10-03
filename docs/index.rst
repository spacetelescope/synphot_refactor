.. doctest-skip-all

.. _astropy_synphot:

******************************
Synthetic Photometry (synphot)
******************************

Introduction
============

A brief history: First, there was
`STSDAS SYNPHOT <http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?synphot.sys>`_.
Then, there was
ASTROLIB PYSYNPHOT (:ref:`Lim et al. 2015 <synphot-ref-lim2015>`), which
aimed at replacing STSDAS SYNPHOT using Python. In order to take advantage of
:ref:`astropy:astropy-modeling` and :ref:`astropy:astropy-units` and to
repurpose the functionality for a wider audience (other than HST users),
it was refactored again and separated into:

* **synphot** (this package), which covers the general functionalities not
  related to any particular observatory; and
* :ref:`stsynphot:stsynphot_index`.

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

If you use **synphot** in your work, please cite it as,
"*Lim, P. L. 2016, synphot User's Guide
(Baltimore, MD: STScI), http://synphot.readthedocs.io/en/latest/*"

If you have questions or concerns regarding the software, please open an issue
at https://github.com/spacetelescope/synphot_refactor/issues (if not already
reported) or contact STScI Help Desk via ``help[at]stsci.edu``.


.. _synphot-installation-setup:

Installation and Setup
======================

**synphot** works under both Python 2 and 3. It requires the following
packages:

* numpy (>= 1.9)
* astropy (>= 1.3)
* scipy (>= 0.14)
* matplotlib (optional for plotting)

You can install **synphot** using one of the following ways
(`AstroConda <http://astroconda.readthedocs.io/en/latest/>`_ support is planned
for a future release):

* From standalone release::

    pip install git+https://github.com/spacetelescope/synphot_refactor.git@0.1b1

* From source (example shown is for the ``dev`` version)::

    git clone https://github.com/spacetelescope/synphot_refactor.git
    cd synphot_refactor
    python setup.py install

To use the pre-defined standard star, extinction laws, and bandpasses, it is
recommended that you copy
`synphot.cfg <https://github.com/spacetelescope/synphot_refactor/blob/master/synphot/synphot.cfg>`_
to your ``$HOME/.astropy/config/`` directory.
In doing so, you can avoid connecting directly to STScI anonymous FTP service,
which is slower and might not be available all the time.

If necessary (i.e., if you are not an internal STScI user), replace
``/grp/hst/cdbs`` with your local directory name
(e.g., ``/my/local/dir/cdbs``), where you plan to store the data files.
Then, follow the instructions below to "install" the data files.

.. note::

    **synphot** data files are a minimal subset of those required by
    **stsynphot**. If you plan to use the latter anyway, please also read the
    instructions in :ref:`stsynphot:stsynphot-installation-setup`.

To install local data files via anonymous FTP::

    $ cd /my/local/dir/cdbs
    $ mkdir calspec extinction comp comp/nonhst
    $ ftp ftp.stsci.edu
    Name: anonymous
    Password: (Enter your email address)
    ftp> lcd calspec
    ftp> cd cdbs/calspec
    ftp> get alpha_lyr_stis_008.fits
    ftp> lcd ../extinction
    ftp> cd ../extinction
    ftp> mget *.fits
    (Press "y" to accept transfer)
    ftp> lcd ../comp/nonhst
    ftp> cd ../comp/nonhst
    ftp> get bessell_h_004_syn.fits
    ftp> get bessell_j_003_syn.fits
    ftp> get bessell_k_003_syn.fits
    ftp> get cousins_i_004_syn.fits
    ftp> get cousins_r_004_syn.fits
    ftp> get johnson_b_004_syn.fits
    ftp> get johnson_i_003_syn.fits
    ftp> get johnson_j_003_syn.fits
    ftp> get johnson_k_003_syn.fits
    ftp> get johnson_r_003_syn.fits
    ftp> get johnson_u_004_syn.fits
    ftp> get johnson_v_004_syn.fits
    ftp> quit

If you have your own version of the data files that you wish to use, you can
modify ``synphot.cfg`` to point to your own copies without having to download
from the FTP server above. However, before you do so, make sure that your own
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
`synphot.models`, not `astropy.modeling.models`, because the models in
``synphot`` have extra things like ``sampleset`` that are not (yet) available
in Astropy. Despite this, some models like `~astropy.modeling.models.Const1D`
does not need the extra things to work, so they can be used directly.
When in doubt, see if a model is in `synphot.models` first before using
Astropy's.

.. plot::
    :include-source:

    from synphot import units, SourceSpectrum
    from synphot.models import (BlackBodyNorm1D, GaussianAbsorption1D,
                                GaussianFlux1D)
    from synphot.spectrum import BaseUnitlessSpectrum
    # Create a Gaussian absorption profile that absorps 80% of the flux at
    # 4000 Angstrom with a sigma of 20 Angstrom
    g_abs = BaseUnitlessSpectrum(GaussianAbsorption1D, amplitude=0.8,
                                 mean=4000, stddev=20)
    # Create a Gaussian emission line with a total flux of 0.05 PHOTLAM
    # centered at 3000 Angstrom with FWHM of 100 Angstrom
    g_em = SourceSpectrum(GaussianFlux1D, total_flux=0.05*units.PHOTLAM,
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

    >>> from astropy import units as u
    >>> sp(0.3 * u.micron)
    <Quantity 0.001268063356632316 PHOTLAM>

Models that built the spectrum::

    >>> print(sp)
    SourceSpectrum at z=0.0
    Model: CompoundModel5
    Inputs: ('x',)
    Outputs: ('y',)
    Model set size: 1
    Expression: ([0] + ([1] | [2])) * [3]
    Components:
        [0]: <GaussianFlux1D(amplitude=0.0004697186393498257, mean=3000.0, ...>

        [1]: <BlackBodyNorm1D(temperature=6000.0)>

        [2]: <Scale(factor=2.0)>

        [3]: <GaussianAbsorption1D(amplitude=0.8, mean=4000.0, stddev=20.0)>
    Parameters:
          amplitude_0    mean_0    stddev_0   ... amplitude_3 mean_3 stddev_3
        ---------------- ------ ------------- ... ----------- ------ --------
        0.00046971863935 3000.0 42.4660900144 ...         0.8 4000.0     20.0

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
    <Quantity 12900.947986966807 PHOTLAM>

Create an observation by passing the redshifted and normalized source spectrum
through the box bandpass::

    >>> from synphot import Observation
    >>> obs = Observation(sp_rn, bp)

Calculate the count rate of the observation above for an 2-meter telescope:

    >>> import numpy as np
    >>> area = np.pi * (1 * u.m) ** 2
    >>> area
    <Quantity 3.141592653589793 m2>
    >>> obs.countrate(area=area)
    <Quantity 24219652.902789623 ct / s>


.. _synphot_using:

Using **synphot**
=================

# UNTIL HERE -- reorganize?

.. toctree::
   :maxdepth: 1

   synphot/overview
   synphot/from_pysyn_iraf
   synphot/bandpass
##   synphot/units
##   synphot/formulae
##   synphot/spectrum
##   synphot/observation
##   synphot/reddening
##   synphot/thermal
   synphot/ref_api
   synphot/biblio
