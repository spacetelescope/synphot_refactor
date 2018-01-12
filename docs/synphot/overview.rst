.. doctest-skip-all

.. _synphot_overview:

Overview
========

There are two basic kinds of spectra in **synphot**, those with and without
flux units. The former is used to construct :ref:`source-spectrum-main` and
:ref:`synphot_observation`, while the latter for :ref:`bandpass-main`,
:ref:`extinction curve <synphot_reddening>`, and :ref:`synphot_thermal`.
In the center of them all are :ref:`Astropy models <astropy:astropy-modeling>`,
which are used to represent the data, to create composite spectra, and to
evaluate the results.

For simplicity and to be consistent with ASTROLIB PYSYNPHOT, a spectrum object
stores its wavelength internally in Angstrom. A source spectrum stores flux in
PHOTLAM, while a unitless spectrum stores throughput as
:ref:`dimensionless_unscaled <astropy:doc_dimensionless_unit>`. Despite this,
most of the functionalities in **synphot** are unit-aware; i.e., you can pass
in :ref:`astropy:quantity` and specify the desired output units via optional
keywords (see relevant :ref:`API documentation <synphot_api>`).

File I/O in **synphot** is handled by its `~synphot.specio` module, which
uses :ref:`Astropy FITS <astropy:astropy-io-fits>` and
:ref:`Astropy ASCII <astropy:io-ascii>`, but read (both FITS and ASCII) and
write (FITS only) spectrum data in a way that is backward-compatible with
ASTROLIB PYSYNPHOT. In most cases, this module does not need to be accessed
directly, but rather via ``from_file()`` and ``to_fits()`` methods of a
spectrum object.


.. _synphot_models_overview:

**synphot** and Astropy Models
------------------------------

.. note::

    The interactions between **synphot** and ``astropy.models`` might change
    in the future as the latter support more features, such as ``Quantity``.
    When that happens, the existing API will issue deprecation warnings,
    where appropriate.

**synphot** takes advantage of the analytical nature of
:ref:`Astropy models <astropy:astropy-modeling>`, except for
`~astropy.modeling.tabular` data, which are interpolated using Scipy.
This is very different from ASTROLIB PYSYNPHOT that relied heavily on
interpolation of internal lookup tables. But similar to ASTROLIB PYSYNPHOT,
each individual model that goes into a
:ref:`compound (composite) model <astropy:compound-models>` is stored
separately and the final result is only calculated on evaluation.
For simplicity, only 1D models and single
:ref:`model set <astropy:modeling-getting-started-model-sets>`
(``n_models=1``) are supported.

At the time that this package was developed, some features needed for
spectra manipulation were not (yet) available in Astropy models
(e.g., `~astropy.units.Quantity` parameters and ``sampleset`` that provides an
array of values that best samples the model). In addition,
some models (e.g., `~synphot.models.Empirical1D`) are simply too specialized
for our use case to be in Astropy. For those reasons, `~synphot.models` exists
to bridge that gap. For instance, a `synphot.models.Gaussian1D` is just like
`astropy.modeling.functional_models.Gaussian1D` but with the extra
``sampleset``. Still, some models can be used straight from Astropy
(e.g., `~astropy.modeling.powerlaws.PowerLaw1D` where ``sampleset`` is
infinite, thus does not apply).

The following table lists the models allowed to be used for spectrum
construction (with flux unit or unitless), where they reside,
and special notes:

+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|Model                                                    |Package    |Notes                                                         |
+=========================================================+===========+==============================================================+
|`~synphot.models.BlackBody1D`                            |**synphot**|Calculate flux in PHOTLAM per                                 |
|                                                         |           |steradian.                                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.BlackBodyNorm1D`                        |**synphot**|Calculate flux in PHOTLAM.                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.Box1D`                                  |**synphot**|Like `astropy.modeling.functional_models.Box1D`               |
|                                                         |           |but with ``sampleset``.                                       |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~astropy.modeling.powerlaws.BrokenPowerLaw1D`           |Astropy    ||note_flux_conv_incorrect|                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~astropy.modeling.functional_models.Const1D`            |Astropy    ||note_flux_conv_incorrect|                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.ConstFlux1D`                            |**synphot**|Constant flux in a given unit might                           |
|                                                         |           |not be constant in other flux units.                          |
|                                                         |           |This handles flux unit conversion                             |
|                                                         |           |properly.                                                     |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.Empirical1D`                            |**synphot**|Like `~astropy.modeling.tabular.Tabular1D`                    |
|                                                         |           |but with extra features specific to                           |
|                                                         |           |spectrum (e.g., option to keep negative flux) and             |
|                                                         |           |different default values.                                     |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~astropy.modeling.powerlaws.ExponentialCutoffPowerLaw1D`|Astropy    ||note_flux_conv_incorrect|                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.Gaussian1D`                             |**synphot**|Like `astropy.modeling.functional_models.Gaussian1D`          |
|                                                         |           |but with ``sampleset``.                                       |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.GaussianAbsorption1D`                   |**synphot**|Like `astropy.modeling.functional_models.GaussianAbsorption1D`|
|                                                         |           |but with ``sampleset``.                                       |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.GaussianFlux1D`                         |**synphot**|Like `~synphot.models.Gaussian1D` but allows                  |
|                                                         |           |backward-compatible parameters like total flux and            |
|                                                         |           |FWHM.                                                         |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~astropy.modeling.powerlaws.LogParabola1D`              |Astropy    ||note_flux_conv_incorrect|                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.Lorentz1D`                              |**synphot**|Like `astropy.modeling.functional_models.Lorentz1D`           |
|                                                         |           |but with ``sampleset`` and ``bounding_box``.                  |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.MexicanHat1D`                           |**synphot**|Like `astropy.modeling.functional_models.MexicanHat1D`        |
|                                                         |           |but with ``sampleset`` and ``bounding_box``.                  |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~astropy.modeling.powerlaws.PowerLaw1D`                 |Astropy    ||note_flux_conv_incorrect|                                    |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.PowerLawFlux1D`                         |**synphot**|Like `~astropy.modeling.powerlaws.PowerLaw1D`                 |
|                                                         |           |but handles flux unit conversion properly by                  |
|                                                         |           |evaluating in user flux unit instead of internal              |
|                                                         |           |unit of PHOTLAM.                                              |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+
|`~synphot.models.Trapezoid1D`                            |**synphot**|Like `astropy.modeling.functional_models.Trapezoid1D`         |
|                                                         |           |but with ``sampleset``.                                       |
+---------------------------------------------------------+-----------+--------------------------------------------------------------+

.. |note_flux_conv_incorrect| replace:: Flux handling might be incorrect unless amplitude is in PHOTLAM when creating a source spectrum using this model.


.. _synphot-spec-math-op:

Spectrum Arithmetic
-------------------

When spectrum objects are added to, subtracted from, multiplied with, or
divided by each other, the resultant spectrum contains a compound model derived
from the operands. If the operands themselves also contain compound models,
then the final compound model is a compound of the input compound models.

Operations that do not make sense (e.g., multiplying two source spectra or
adding a bandpass to a source spectrum) are prohibited. The type of output
spectrum depends on the operation. In the table below, unitless spectrum can
be a bandpass or extinction curve:

================= ============== ================= ================= ===========
Operand 1         Operation      Operand 2         Result            Commutative
================= ============== ================= ================= ===========
Source Spectrum   :math:`+`      Source Spectrum   Source Spectrum   Yes
Source Spectrum   :math:`-`      Source Spectrum   Source Spectrum   No
Source Spectrum   :math:`\times` Unitless Spectrum Source Spectrum   Yes
Source Spectrum   :math:`\times` Scalar number     Source Spectrum   Yes
Source Spectrum   :math:`\times` Unitless Quantity Source Spectrum   No
Source Spectrum   :math:`/`      Source Spectrum   Unitless Spectrum No
Source Spectrum   :math:`/`      Unitless Spectrum Source Spectrum   No
Source Spectrum   :math:`/`      Scalar number     Source Spectrum   No
Source Spectrum   :math:`/`      Unitless Quantity Source Spectrum   No
Unitless Spectrum :math:`\times` Unitless Spectrum Unitless Spectrum Yes
Unitless Spectrum :math:`\times` Scalar number     Unitless Spectrum Yes
Unitless Spectrum :math:`\times` Unitless Quantity Unitless Spectrum No
Unitless Spectrum :math:`/`      Unitless Spectrum Unitless Spectrum No
Unitless Spectrum :math:`/`      Scalar number     Unitless Spectrum No
Unitless Spectrum :math:`/`      Unitless Quantity Unitless Spectrum No
================= ============== ================= ================= ===========


.. _synphot-quick-guide:

Quick Guide
-----------

The tables below summarize some main functionality of **synphot**.
The variables, where appropriate, can be numbers (assumed to be in certain
units) or Quantity. These are only for quick reference. Detailed explanations
are available in their respective sections in the other parts of this document.

.. _synphot-quick-create-bandpass:

Create Bandpass
^^^^^^^^^^^^^^^

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Load from file.            |bp = SpectralElement.from_file(filename)        |
+---------------------------+------------------------------------------------+
|Load pre-defined bandpass. |bp = SpectralElement.from_filter(filtername)    |
+---------------------------+------------------------------------------------+
|Create from wavelength and |bp = SpectralElement(Empirical1D,               |
|throughput arrays.         |points=wavelength, lookup_table=throughput)     |
+---------------------------+------------------------------------------------+
|Box centered at ``mu`` with|bp = SpectralElement(Box1D, x_0=mu, width=width)|
|given width.               |                                                |
+---------------------------+------------------------------------------------+
|Create from tapering       |bp2 = bp.taper()                                |
|existing bandpass.         |                                                |
+---------------------------+------------------------------------------------+

.. _synphot-quick-bandpass-params:

Calculate Bandpass Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Average wavelength and     |bp.avgwave()                                    |
|associated throughput.     |                                                |
|                           |bp.tlambda()                                    |
+---------------------------+------------------------------------------------+
|Peak throughput and        |bp.tpeak()                                      |
|associated wavelength.     |                                                |
|                           |bp.wpeak()                                      |
+---------------------------+------------------------------------------------+
|Dimensionless efficiency.  |bp.efficiency()                                 |
+---------------------------+------------------------------------------------+
|Equivalent width.          |bp.equivwidth()                                 |
+---------------------------+------------------------------------------------+
|Rectangular width.         |bp.rectwidth()                                  |
+---------------------------+------------------------------------------------+
|RMS band width as in       |bp.rmswidth()                                   |
||koornneef1986page836|.    |                                                |
+---------------------------+------------------------------------------------+
|RMS band width as in       |bp.photbw()                                     |
|IRAF SYNPHOT.              |                                                |
+---------------------------+------------------------------------------------+
|FWHM of equiv. Gaussian.   |bp.fwhm()                                       |
+---------------------------+------------------------------------------------+
|Pivot wavelength.          |bp.pivot()                                      |
+---------------------------+------------------------------------------------+
|Mean log wavelength.       |bp.barlam()                                     |
+---------------------------+------------------------------------------------+
|Unit response; |uresp1cts|,|bp.unit_response(area)                          |
|for given telescope area.  |                                                |
+---------------------------+------------------------------------------------+
|Equiv. monochromatic flux. |bp.emflx(area)                                  |
+---------------------------+------------------------------------------------+
|Check if bandpass fully    |bp.check_overlap(sp)                            |
|overlaps a source spectrum.|                                                |
+---------------------------+------------------------------------------------+

.. |koornneef1986page836| replace:: :ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836)
.. |uresp1cts| replace:: flux that produces 1 count/s in the bandpass

.. _synphot-quick-create-unitless:

Create Other Unitless Spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Reddening law from         |redlaw = ReddeningLaw.from_extinction_model(    |
|extinction model. |rlloads||extinction_model_name)                          |
+---------------------------+------------------------------------------------+
|Extinction curve from      |extcurve = redlaw.extinction_curve(ebv)         |
|reddening law at given     |                                                |
|:math:`E(B-V)`             |                                                |
+---------------------------+------------------------------------------------+
|Extinction for Lyman-alpha |extcurve = etau_madau(wave, z)                  |
+---------------------------+------------------------------------------------+
|Bandpass with thermal      |thbp = ThermalSpectralElement(modelclass,       |
|properties (from model).   |temperature, \*\*kwargs)                        |
+---------------------------+------------------------------------------------+
|Bandpass with thermal      |thbp = ThermalSpectralElement.from_file(        |
|properties (from file).    |filename)                                       |
+---------------------------+------------------------------------------------+

.. |rlloads| replace:: Creation using Astropy model and from file also possible but not shown.

.. _synphot-quick-create-source:

Create Source Spectrum
^^^^^^^^^^^^^^^^^^^^^^

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Load from file.            |sp = SourceSpectrum.from_file(filename)         |
+---------------------------+------------------------------------------------+
|Load Vega from file.       |sp = SourceSpectrum.from_vega()                 |
+---------------------------+------------------------------------------------+
|Create from wavelength and |sp = SourceSpectrum(Empirical1D,                |
|flux arrays.               |points=wavelength, lookup_table=flux)           |
+---------------------------+------------------------------------------------+
|Blackbody with temperature,|sp = SourceSpectrum(BlackBodyNorm1D,            |
|``teff``, and |bbnormflux|.|temperature=teff)                               |
+---------------------------+------------------------------------------------+
|Flat spectrum with constant|sp = SourceSpectrum(ConstFlux1D, amplitude=flux)|
|flux.                      |                                                |
+---------------------------+------------------------------------------------+
|Powerlaw spectrum with flux|sp = SourceSpectrum(PowerLawFlux1D,             |
|of 1 in given unit at      |amplitude=1*unit, x_0=x, alpha=a)               |
|``x`` and power of ``-a``. |                                                |
+---------------------------+------------------------------------------------+
|Gaussian emission line     |sp = SourceSpectrum(GaussianFlux1D, mean=mu,    |
|centered on ``mu`` with    |fwhm=fwhm, total_flux=total_flux)               |
|given FWHM and total flux. |                                                |
+---------------------------+------------------------------------------------+
|Thermal source spectrum    |sp = thbp.thermal_source()                      |
|from thermal bandpass.     |                                                |
+---------------------------+------------------------------------------------+

.. |bbnormflux| replace:: flux normalized to a star of solar radius at a distance of 1 kpc

.. _synphot-quick-modify-source:

Modify Source Spectrum
^^^^^^^^^^^^^^^^^^^^^^

New source spectrum is created as a result unless stated otherwise.

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Taper flux to zero on ends.|sp2 = sp.taper()                                |
+---------------------------+------------------------------------------------+
|Normalize to given value   |sp2 = sp.normalize(value, band=bp)              |
|over given bandpass.       |                                                |
|Count and VEGAMAG unit     |sp2 = sp.normalize(value_count, band=bp,        |
|requires extra inputs.     |area=area)                                      |
|                           |                                                |
|                           |sp2 = sp.normalize(value_vegamag, band=bp,      |
|                           |vegaspec=SourceSpectrum.from_vega())            |
+---------------------------+------------------------------------------------+
|Apply extinction curve.    |sp2 = sp * extcurve                             |
+---------------------------+------------------------------------------------+
|Apply redshift (models     |sp.z = z                                        |
|modified in-place).        |                                                |
|                           |sp.z_type = ...                                 |
+---------------------------+------------------------------------------------+
|Apply redshift (new source |sp2 = SourceSpectrum(sp.model, z=z, z_type=...) |
|spectrum).                 |                                                |
|                           |sp = SourceSpectrum(modelclass, z=z, z_type=...,|
|                           |\*\*kwargs)                                     |
+---------------------------+------------------------------------------------+

.. _synphot-quick-obs:

Create Observation and Calculate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Observation has binned and unbinned components. Most methods accept an optional
``binned`` keyword to indicate which component you want to calculate for.
Only the default binning option is listed below.

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Observe a source spectrum  |obs = Observation(sp, bp)                       |
|through given bandpass.    |                                                |
+---------------------------+------------------------------------------------+
|Sample observed flux.      |flux = obs(wavelength)  # Unbinned              |
|                           |                                                |
|                           |flux = obs.sample_binned(wavelength)            |
+---------------------------+------------------------------------------------+
|Effective wavelength.      |obs.effective_wavelength()  # Binned            |
+---------------------------+------------------------------------------------+
|Effective stimulus in given|obs.effstim(flux_unit=unit)  # Unbinned         |
|unit.                      |                                                |
+---------------------------+------------------------------------------------+
|Count rate for given area. |obs.countrate(area)  # Binned                   |
+---------------------------+------------------------------------------------+
|Convert into simple source |sp = obs.as_spectrum()  # Binned                |
|spectrum.                  |                                                |
+---------------------------+------------------------------------------------+

.. _synphot-quick-misc:

Miscellaneous
^^^^^^^^^^^^^

+---------------------------+------------------------------------------------+
|Description                |Command                                         |
+===========================+================================================+
|Generate wavelength array. |wavelength = generate_wavelengths()             |
+---------------------------+------------------------------------------------+
|Quick-look plot.           |obj.plot()  # Any spectrum object               |
+---------------------------+------------------------------------------------+
|Write to FITS table.       |bp.to_fits(filename); redlaw.to_fits();         |
|                           |sp.to_fits(filename)                            |
+---------------------------+------------------------------------------------+


.. _synphot-fits-format-overview:

FITS Table Format
-----------------

The FITS table format supported here is the same as that in
ASTROLIB PYSYNPHOT for backward compatibility with existing data files.
Data is extracted from Extension 1, where the first column
contains wavelength values, and the second flux (for source spectrum) or
throughput (for bandpass). The extension header must contain the following
keywords (unless you overwrite them with non-default values in
:func:`~synphot.specio.read_fits_spec`):

* ``TUNIT1`` set to :ref:`supported wavelength unit name <synphot_units>`.
* ``TUNIT2`` set to :ref:`supported flux unit name <synphot_units>`
  (source spectrum only).
* ``TTYPE1`` set to "WAVELENGTH".
* ``TTYPE2`` set to "FLUX" (for source spectrum) or "THROUGHPUT"
  (for bandpass).

For writing out FITS table, many options can be set to non-default as
acceptable by :func:`~synphot.specio.write_fits_spec`.


.. _synphot-ascii-format-overview:

ASCII Table Format
------------------

The ASCII table format supported here is the same as that in
ASTROLIB PYSYNPHOT for backward compatibility with existing data files.
Wavelength and flux/throughput values must be in the first and the second
columns, respectively. By default, wavelength is assumed to be in Angstrom;
For source spectrum, flux is assumed to be in FLAM. All values will be read in
as double-precision floating points. The file may contain blank or comment
lines (any lines starting with ``"#"``), which are ignored.

By default, :ref:`Astropy's ASCII reader <astropy:io_ascii_read_parameters>`
will attempt to guess the format of your file (e.g., space- or tab-delimited).
If guessing fails, you can pass in additional keywords to the reader, as well
as specifying non-default wavelength and flux units, via
:func:`synphot.specio.read_ascii_spec`.


.. _synphot-accuracy:

Result Accuracy
---------------

This is indirectly discussed in a similar section within **stsynphot**
documentation as it is heavily built upon **synphot** machinery.
