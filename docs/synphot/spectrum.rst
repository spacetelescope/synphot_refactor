.. _synphot_spectrum:

Spectra Manipulation
====================

.. _synphot-io:

I/O
---

These are the supported ``synphot`` file types via `synphot.synio`:

    =========  ====  =====
    File type  Read  Write
    =========  ====  =====
    ASCII      Yes   No
    FITS       Yes   Yes
    =========  ====  =====

Once a spectrum is read in as an object, one may also use the general
`astropy.io` utilities to write it out to formats not supported here.


Create a Source Spectrum
------------------------

Load a source spectrum from file:

>>> Insert examples here

General constructor if wavelength and flux arrays are already known:

>>> Insert examples here

A source spectrum can also be created from these pre-defined sources below.


.. _synphot-planck-law:

Blackbody Radiation
^^^^^^^^^^^^^^^^^^^

Blackbody spectrum is generated with Planck law
(:ref:`Rybicki & Lightman 1979 <synphot-ref-rybicki1979>`).

.. math::

    B_{\nu}(T) = \frac{2 h \nu^{3} / c^{2}}{exp(h \nu / k T) - 1}

    B_{\lambda}(T) = \frac{2 h c^{2} / \lambda^{5}}{exp(h c / \lambda k T) - 1}

where the unit of :math:`B_{\nu}(T)` is
:math:`erg s^{-1} cm^{-2} Hz^{-1} sr^{-1}` (i.e., FNU per steradian)
and the  unit of :math:`B_{\lambda}(T)` is
:math:`erg s^{-1} cm^{-2} \AA^{-1} sr^{-1}` (i.e., FLAM per steradian)

Examples:

>>> Insert examples here


.. _synphot-gaussian:

Gaussian
^^^^^^^^

.. math::

    \sigma = \frac{FWHM}{2 \sqrt{2 * ln 2}}

    a = \frac{flux_{total}}{\sqrt{2 \pi} \sigma}

    flux = a * e^{- \frac{(\lambda - \lambda_{center})^{2}}{2 \sigma^{2}}}

Examples:

>>> Insert examples here


.. synphot-powerlaw:

Power-Law
^^^^^^^^^

.. math::

    flux = {\frac{\lambda}{\lambda_{ref}}}^{index}

Examples:

>>> Insert examples here


.. synphot-flat-spec:

Flat
^^^^

A flat spectrum in a given flux unit is defined as follows:

    * PHOTLAM - Constant value of 1 PHOTLAM.
    * PHOTNU - Constant value of 1 PHOTNU.
    * FLAM - Constant value of 1 FLAM.
    * STMAG - Constant value of 0 STMAG in the unit of FLAM.
    * FNU - Constant value of 1 FNU.
    * ABMAG - Constant value of 0 ABMAG in the unit of FNU.
    * count - Constant value of \frac{1}{N_{\lambda}} counts.
    * OBMAG - Same as count.
    * Other spectral flux density units (e.g., Jy) - Constant value of 1
      in the unit.

Examples:

>>> Insert examples here


.. synphot-vega-spec:

Vega
^^^^

By default, Vega spectrum is downloaded from STScI via configurable item
``synphot.synconfig.VEGAFILE``, which requires internet connection, unless
a local cached copy exists and ``cache=True``. One can use any desired Vega
spectrum as long as it is a valid file format, remote or local, by changing
the ``VEGAFILE`` configuration item.

Examples:

>>> Insert examples here


Source Spectrum Functionalities
-------------------------------

TODO


Write a Source Spectrum
-----------------------

>>> Insert examples here


.. synphot-passband-create:

Create a Passband
-----------------

Below are the pre-defined passbands for common filters. By default, they are
downloaded from a remote location as defined in `synphot.synconfig`. They can
be accessed via :func:`synphot.spectrum.SpectralElement.from_filter` by
providing the class method with the corresponding filter name:

    ===========  ==================  ===========
    Filter name  Config Item         Description
    ===========  ==================  ===========
    'bessel_j'   ``BESSEL_J_FILE``   Bessel J
    'bessel_h'   ``BESSEL_H_FILE``   Bessel H
    'bessel_k'   ``BESSEL_K_FILE``   Bessel K
    'cousins_r'  ``COUSINS_R_FILE``  Cousins R
    'cousins_i'  ``COUSINS_I_FILE``  Cousins I
    'johnson_u'  ``JOHNSON_U_FILE``  Johnson U
    'johnson_b'  ``JOHNSON_B_FILE``  Johnson B
    'johnson_v'  ``JOHNSON_V_FILE``  Johnson V
    'johnson_r'  ``JOHNSON_R_FILE``  Johnson R
    'johnson_i'  ``JOHNSON_I_FILE``  Johnson I
    'johnson_j'  ``JOHNSON_J_FILE``  Johnson J
    'johnson_k'  ``JOHNSON_K_FILE``  Johnson K
    ===========  ==================  ===========

>>> Insert examples here

Create a box-shaped passband:

>>> Insert examples here

Load a passband from file:

>>> Insert examples here

General constructor if wavelength and throughput arrays are already known:

>>> Insert examples here


Passband Functionalities
------------------------

TODO


Write a Passband
----------------

TODO


Create an Observation
---------------------

General constructor if wavelength and flux arrays are already known:

>>> Insert examples here

Create an observation from existing source spectrum and passband:

>>> Insert examples here


Observation Functionalities
---------------------------

TODO


Write an Observation
--------------------

TODO
