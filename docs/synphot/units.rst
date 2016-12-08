.. doctest-skip-all

.. _synphot_units:

Units and Constants
===================

**synphot** understands
:ref:`Astropy Units and Quantities <astropy:astropy-units>`.
Its `~synphot.units` module expands on that by providing:

* "Shortcuts" (proper names) for some constants and composite units that are
  frequently used in this package.
* A convenience function, :func:`~synphot.units.convert_flux`, to convert
  between different flux units.
* Support for non-standard unit names for backward compatibility with
  ASTROLIB PYSYNPHOT data files.


.. _synphot-constants:

Constants
---------

These are the constants provided by `~synphot.units`. They can be computed
from existing constants in Astropy but are pre-calculated here for convenience:

=============== ================================
Constant        Description
=============== ================================
C               Speed of light in Angstrom/s
H               Planck's constant in CGS
HC              :math:`H \times C`
SR_PER_ARCSEC2  Steradian per squared arcseconds
=============== ================================


.. _synphot-flux-units:

Flux Units
----------

In addition to flux units already supported by Astropy, such as Jy (and its
prefixes), count, ABmag, and STmag, `~synphot.units` adds direct support to
the following as well. In **synphot**, the easiest way to specify the desired
flux unit is by passing in a ``flux_unit`` keyword into a function or class
method and assigning it the unit name (as string) or direct variable name:

+-------+-------------------------+--------------+
|Name   |Variable                 |Unit          |
+=======+=========================+==============+
|photlam|``synphot.units.PHOTLAM``||photlam_math||
+-------+-------------------------+--------------+
|photnu |``synphot.units.PHOTNU`` ||photnu_math| |
+-------+-------------------------+--------------+
|flam   |``synphot.units.FLAM``   ||flam_math|   |
+-------+-------------------------+--------------+
|fnu    |``synphot.units.FNU``    ||fnu_math|    |
+-------+-------------------------+--------------+
|obmag  |``synphot.units.OBMAG``  ||obmag_math|  |
+-------+-------------------------+--------------+
|vegamag|``synphot.units.VEGAMAG``||vegamag_math||
+-------+-------------------------+--------------+

.. |photlam_math| replace:: :math:`\text{photon} \; \text{s}^{-1} \; \text{cm}^{-2} \; \mathring{A}^{-1}`
.. |photnu_math| replace:: :math:`\text{photon} \; \text{s}^{-1} \; \text{cm}^{-2} \; \text{Hz}^{-1}`
.. |flam_math| replace:: :math:`\text{erg} \; \text{s}^{-1} \; \text{cm}^{-2} \; \mathring{A}^{-1}`
.. |fnu_math| replace:: :math:`\text{erg} \; \text{s}^{-1} \text{cm}^{-2} \text{Hz}^{-1}`
.. |obmag_math| replace:: :math:`-2.5 \; \log(\text{count})`
.. |vegamag_math| replace:: :math:`-2.5 \; \log(\frac{f}{f_{\text{Vega}}})`

The function :func:`~synphot.units.convert_flux` provides an easy way to
convert between all the supported flux units, including count/OBMAG (needs an
extra input specifying telescope collecting area) and VEGAMAG (needs an extra
input specifying the Vega spectrum to use), by taking account all the
necessary unit equivalencies. You may also use
:meth:`~astropy.units.quantity.Quantity.to` directly, as supported by Astropy,
but you would need to provide the equivalencies on your own.

Somewhat related are ``synphot.units.AREA``, which is a shortcut for the unit
:math:`\text{cm}^{2}` often used for conversion to/from count or OBMAG, and
``synphot.units.THROUGHPUT``, which is identical to dimensionless unscaled unit
in Astropy for unitless transmission curves.

For backward compatibility with ASTROLIB PYSYNPHOT data files, the following
non-standard flux unit *names* (case-insensitive) are also supported:

+------------+-----------------------+
|Name        |Resolves to            |
+============+=======================+
|transmission|Dimensionless unscaled |
|            |                       |
|extinction  |                       |
|            |                       |
|emissivity  |                       |
+------------+-----------------------+
|jy          |``astropy.units.Jy``   |
+------------+-----------------------+
|stmag       |``astropy.units.STmag``|
|            |                       |
|mag(st)     |                       |
+------------+-----------------------+
|abmag       |``astropy.units.ABmag``|
|            |                       |
|mag(ab)     |                       |
+------------+-----------------------+


.. _synphot-units-counts-mags:

Counts and Magnitudes
^^^^^^^^^^^^^^^^^^^^^

.. |ab_nu| replace:: :math:`\text{AB}_{\nu}`
.. |st_lam| replace:: :math:`\text{ST}_{\lambda}`

**synphot** supports count and the following magnitude systems:

* VEGAMAG, which is defined by setting the magnitude of Vega to zero in all
  bands. The :ref:`adopted Vega spectrum <synphot-vega-spec>` is defined over a
  wavelength range of 900 Angstrom to 300 micron.
* |ab_nu| magnitude from :ref:`Oke (1974) <synphot-ref-oke1974>`, which is
  based on a constant flux density per unit frequency.
* |st_lam| or Space Telescope magnitude, which is based on a constant flux
  density per unit wavelength.
* Instrumental magnitude (OBMAG) that is the logarithmic form of counts.
  Conversion involving counts and OBMAG requires telescope collecting area to
  be provided.

VEGAMAG offers a reasonable approximation to many of the conventional
photometric systems that use the spectrum of Vega to define magnitude zero in
one or more bandpasses. In broadband photometry, the relevant bandpass integral
is calculated first for the source spectrum and then again for the spectrum of
Vega, and the ratio of the two results is converted to a magnitude. This would
not be a scientifically meaningful option for spectrophotometry.

Meanwhile, |ab_nu| and |st_lam| are appropriate for either spectrophotometry
or photometry. Their zero point values of 48.60 and 21.10 mag, respectively,
are chosen for convenience so that Vega has |ab_nu| and |st_lam| magnitudes
close to 0 in the Johnson *V* bandpass, as shown in the following figure:

.. figure:: images/VegaPhotomSys.png
    :width: 600px
    :alt: Standard photometric system

    Standard photometric systems generally use the spectrum of Vega to
    define magnitude zero. The spectrophotometric magnitudes
    |ab_nu| and |st_lam| refer instead to spectra of constant :math:`f_{\nu}`
    and :math:`f_{\lambda}`, respectively. Magnitude zero in both systems is
    defined to be the mean flux density of Vega in the Johnson *V* bandpass.
    Thus all three of the spectra shown here produce the same count rate in
    the Johnson *V* bandpass. The pivot wavelength of Johnson *V* is defined to
    be the crossing point of the |ab_nu|:math:`= 0` and |st_lam|:math:`= 0`
    spectra.

Because the |ab_nu| and |st_lam| systems are defined such that they result in
constant magnitudes for spectra having constant flux per unit frequency and
wavelength, respectively, they will not provide magnitudes on a conventional
system, such as *UBVRI*, without first deriving an appropriate transformation
onto the desired standard system.

OBMAG and counts are used to predict detected count rates. For instance,
:meth:`~synphot.observation.Observation.countrate` calculates the predicted
number of detected counts per second integrated over the bandpass.
There are two important things to remember concerning this unit:

#. The number of counts per channel depends on the width (in wavelength space)
   of the channel in the wavelength grid that is used. Flux calculations are
   done internally in the unit of PHOTLAM (unless stated otherwise), so when
   the output unit of counts or OBMAG is requested, the PHOTLAM values are
   multiplied by the collecting area of the telescope and by the width
   (in Angstrom) of each channel in the wavelength grid. Therefore, in order to
   accurately predict the number of counts per channel for a spectroscopic
   instrument, it is necessary to use a wavelength grid that provides a good
   match to the dispersion properties of the selected instrument mode.
   For supported HST instruments, the appropriate wavelength grid will be
   automatically selected in **stsynphot**.
#. The unit count may refer to different physical units for different
   instruments. For instance, in HST, it refers to the actual detector counts
   for the FOC, FOS, HRS, and HSP instruments. While for the WF/PC-1, WFPC2,
   NICMOS, WFC3, COS, ACS, and STIS instruments, it refers to electrons.


.. _synphot-wave-units:

Wavelength Units
----------------

**synphot** supports all wavelength, frequency, and spectroscopic wavenumber
(inverse wavelength) that are supported by Astropy. Conversion between those
units can be easily done using :meth:`~astropy.units.quantity.Quantity.to` and
passing in :func:`~astropy.units.equivalencies.spectral` as equivalency.

For backward compatibility with ASTROLIB PYSYNPHOT data files, the following
non-standard wavelength unit *names* (case-insensitive) are also supported:

* angstroms
* inversemicrons
* jy


.. _synphot-units-examples:

Examples
--------

Create a blackbody source spectrum::

    >>> from astropy import units as u
    >>> from synphot import SourceSpectrum
    >>> from synphot.models import BlackBodyNorm1D
    >>> sp = SourceSpectrum(BlackBodyNorm1D, temperature=5000*u.K)

Sample the source at some wavelengths given in nm and obtain flux in count
for HST::

    >>> from synphot import units
    >>> area = 45238.93416 * units.AREA
    >>> sp([499, 500, 501, 502] * u.nm, flux_unit='count', area=area)
    <Quantity [ 219.25781807, 220.04014043, 220.81868137, 221.59342806] ct>

Sample the source at 5E+15 Hz and obtain flux in FLAM::

    >>> sp([5E+15] * u.Hz, flux_unit=units.FLAM)
    <Quantity [  3.52271822e-29] FLAM>

Sample the source in internal units (Angstrom and PHOTLAM)::

    >>> sp(6000)
    <Quantity 0.0006152610208167509 PHOTLAM>
