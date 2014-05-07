.. doctest-skip-all

.. _synphot_spectrum:

Spectra Manipulation
====================

Internal Units
--------------

For simplicity and to be consistent with ASTROLIB PYSYNPHOT, a spectrum has
pre-defined internal units. A spectrum object internally stores its wavelength
in Angstrom. Source spectrum stores flux in PHOTLAM, and unitless spectrum
stores throughput etc. in THROUGHPUT (unitless).

Some methods provide options to calculate or display wavelength and
flux/throughput/etc. in other units. Please refer to API documentations.


.. _synphot-io:

I/O
---

These are the supported ``synphot`` file types via `synphot.specio`:

=========  ====  =====
File type  Read  Write
=========  ====  =====
ASCII      Yes   No
FITS       Yes   Yes
=========  ====  =====

Once a spectrum is read in as an object, one may also use the ``astropy.io``
package to write it out to formats not supported here.
When writing a spectrum out to FITS, the default behaviors mimic ASTROLIB
PYSYNPHOT (e.g., padding with zero flux/throughput at both ends, and removing
rows with zero flux/throughput and duplicate wavelengths); See
:func:`~synphot.specio.write_fits_spec` for all the options.

Examples
^^^^^^^^

>>> from synphot import SourceSpectrum, SpectralElement
>>> sp = SourceSpectrum.from_file('/my/path/my_spec.fits')
>>> sp.to_fits('/my/path/my_spec_copy.fits')
>>> bp = SpectralElement.from_file('/my/path/my_filter.txt')
>>> bp.to_fits('/my/path/my_filter_copy.fits')


.. _synphot-source-create:

Creating a Source Spectrum
--------------------------

Load a `~synphot.spectrum.SourceSpectrum` from file:

>>> from synphot import SourceSpectrum
>>> sp = SourceSpectrum.from_file('/my/path/my_spec.fits')

Construct a spectrum from a model. Its ``model`` property exposes the
underlying model. Actual evaluation of its flux value is not done until
``__call__`` is invoked:

>>> from synphot import units
>>> from astropy import units as u
>>> from modeling import models  # Has to support composite model and sampleset
>>> sp = SourceSpectrum(
...     models.PowerLaw1D, amplitude=1*units.FLAM, x_0=0.3*u.micron, alpha=4)
>>> sp.model
PowerLaw1D(amplitude=Parameter(...), ..., param_dim=1)>
>>> sp([3000, 3500])
<Quantity [  1.51023510e+11,  8.15187294e+10] PHOTLAM>

Construct an empirical spectrum, where wavelength and flux values are already
known:

>>> from synphot.models import Empirical1D
>>> sp = SourceSpectrum(Empirical1D, x=[1000, 2000, 3000], y=[0.1, 0.02, 1.3])

Redshift and metadata could be applied at the constructor or after creation.
``warnings`` is a special type of metadata, usually used internally by
``synphot``:

>>> sp = SourceSpectrum(
...     Empirical1D, x=[1000, 2000, 3000], y=[0.1, 0.02, 1.3],
...     z=0.3, metadata={'Description': 'My source at z=0.3',
...                      'warnings': {'DataWarning': 'Fake data!'}})
>>> sp.z = 1.3
>>> sp.metadata['Description'] = 'My source at z=1.3'
>>> sp.warnings
{'DataWarning': 'Fake data!'}

If the model used has a ``sampleset``, it will be propagated into the spectrum
object as ``waveset``. For empirical spectrum, its ``waveset`` is simply the
sampled wavelength values (redshifted if applicable):

>>> sp.waveset
<Quantity [ 2300., 4600., 6900.] Angstrom>
>>> sp.waverange
<Quantity [ 2300., 6900.] Angstrom>

A spectrum can also be tapered, plotted, and integrated, which is a trapezoid
integration that uses ``waveset`` and flux in PHOTLAM by default:

>>> sp2 = sp.taper()
>>> sp2(sp2.waverange)
<Quantity [ 0., 0.] PHOTLAM>
>>> sp2.plot(wavelengths=sp2.waveset.to(u.micron), flux_unit=units.FLAM)

.. image:: images/src_spec_ex2.png
    :width: 600px
    :alt: Plotted spectrum.

>>> sp2.integrate()
<Quantity 3955.999999999998 PHOTLAM>

A source spectrum can be normalized to a given flux value (and optionally,
in a given bandpass):

>>> sp2_norm = sp2.normalize(1 * u.mJy)
>>> sp2_norm.integrate()
<Quantity 3.5214440607410253 PHOTLAM>

A source spectrum can also be created from these pre-defined sources below.

.. _synphot-planck-law:

Blackbody Radiation
^^^^^^^^^^^^^^^^^^^

Blackbody spectrum is generated with Planck law
(:ref:`Rybicki & Lightman 1979 <synphot-ref-rybicki1979>`).

.. math::

    B_{\lambda}(T) = \frac{2 h c^{2} / \lambda^{5}}{exp(h c / \lambda k T) - 1}

where the unit of :math:`B_{\lambda}(T)` is
:math:`erg s^{-1} cm^{-2} \AA^{-1} sr^{-1}` (i.e., FLAM per steradian).

:func:`~synphot.spectrum.SourceSpectrum.from_blackbody` generates a blackbody
spectrum in PHOTLAM for a given temperature, normalized to a star of 1 solar
radius at a distance of 1 kpc. This is to be consistent with ASTROLIB PYSYNPHOT.
Its ``expr`` metadata has IRAF SYNPHOT equivalent command.

>>> bb_sun = SourceSpectrum.from_blackbody(5777)
>>> bb_sun.metadata['expr']
u'bb(5777)'
>>> bb_sun.plot(title='Sun-like blackbody')

.. image:: images/sun_blackbody.png
    :width: 600px
    :alt: Blackbody spectrum.

.. _synphot-gaussian:

Gaussian Emission
^^^^^^^^^^^^^^^^^

.. math::

    \sigma = \frac{FWHM}{2 \; \sqrt{2 \times ln \; 2}}

    A = \frac{flux_{total}}{\sqrt{2 \; \pi} \; \sigma}

    flux = A \; e^{- \frac{(x - x_{0})^{2}}{2 \; \sigma^{2}}}

where :math:`x` is in the unit of :math:`x_{0}` and flux is in the unit of
the given total flux.

:func:`~synphot.spectrum.SourceSpectrum.from_gaussian` generates a Gaussian
emission spectrum as defined in ASTROLIB PYSYNPHOT, which assumes total flux
to be in FLAM (not PHOTLAM) if no unit is given. Its ``expr`` metadata has
IRAF SYNPHOT equivalent command.

>>> g_em = SourceSpectrum.from_gaussian(1 * units.PHOTLAM, 6000, 100)
>>> g_em.metadata['expr']
u'em(6000, 100, 1, PHOTLAM)'
>>> g_em.plot(title='Gaussian with total flux of 1 PHOTLAM')

.. image:: images/gaussian_em.png
    :width: 600px
    :alt: Gaussian emission spectrum.

Gaussian Absorption
^^^^^^^^^^^^^^^^^^^

Unlike the other source spectrum components, Gaussian absorption line should be
unitless (`~synphot.spectrum.BaseUnitlessSpectrum`) because it is to be
*multiplied* (see :ref:`synphot-spec-math-op`) to the source spectrum. Its
formula is given in `~synphot.models.GaussianAbsorption1D`.

>>> from synphot import BaseUnitlessSpectrum
>>> from synphot.models import GaussianAbsorption1D
>>> g_abs = BaseUnitlessSpectrum(
...     GaussianAbsorption1D, amplitude=0.8, mean=6000, stddev=10)
>>> g_abs.plot(title='Gaussian absorption line')

.. image:: images/gaussian_abs.png
    :width: 600px
    :alt: Gaussian absorption line.

.. _synphot-powerlaw:

Power-Law
^^^^^^^^^

.. math::

    flux = A \; (x \; / \; x_{0})^{-\alpha}

where

    * :math:`A =` Amplitude, usually 1
    * :math:`x =` Wavelength array in the unit of :math:`x_{0}`
    * :math:`x_{0} =` Reference wavelength
    * :math:`\alpha =` Power-law index

It is recommended to use `~synphot.models.PowerLawFlux1D` model that correctly
handles flux conversion instead of ``PowerLaw1D``, although the latter could
still be used if you only work in PHOTLAM. It does not have pre-defined
``waveset``, so wavelength values have to be explicitly given when sampling.

>>> from synphot.models import PowerLawFlux1D
>>> import numpy as np
>>> plaw = SourceSpectrum(
...     PowerLawFlux1D, amplitude=1*u.mJy, x_0=0.5*u.micron, alpha=1.5)
>>> plaw.plot(
...     wavelengths=np.arange(0.2, 0.7, 0.005)*u.micron, flux_unit=u.mJy,
...     title='Powerlaw spectrum with 1 mJy at 0.5 micron')

.. image:: images/powerlaw_spec.png
    :width: 600px
    :alt: Powerlaw spectrum.

.. _synphot-flat-spec:

Flat (Constant Flux)
^^^^^^^^^^^^^^^^^^^^

A flat spectrum has a constant flux value in the given flux unit, except the
following, as per ASTROLIB PYSYNPHOT:

    * STMAG - Constant value in the unit of FLAM.
    * ABMAG - Constant value in the unit of FNU.

Because flux that is constant in a given unit might not be constant in PHOTLAM,
it is recommended to use `~synphot.models.ConstFlux1D` model that correctly
handles flux conversion instead of ``Const1D``, although the latter could still
be used if you only work in PHOTLAM. It does not have pre-defined ``waveset``,
so wavelength values have to be explicitly given when sampling.

>>> from synphot.models import ConstFlux1D
>>> flat_abmag = SourceSpectrum(ConstFlux1D, amplitude=0*units.ABMAG)
>>> flat_abmag.plot(
...     wavelengths=[1, 1e4], flux_unit=units.FNU,
...     title='Flat spectrum in 0 ABMAG')

.. image:: images/flat_abmag.png
    :width: 600px
    :alt: Flat spectrum.

.. _synphot-vega-spec:

Vega
^^^^

By default, Vega spectrum is downloaded from STScI via configurable item
``synphot.config.conf.vega_file``, which requires internet connection, unless
a local or cached copy is used. One can use any desired Vega spectrum as long as
it is a valid file format, remote or local, by changing the ``vega_file`` value.

>>> from synphot.config import conf
>>> with conf.set_temp('vega_file', '/my/path/alpha_lyr_stis_007.fits'):
...     vegaspec = SourceSpectrum.from_vega(encoding='binary')
>>> vegaspec.plot(right=20000, flux_unit=units.FLAM, title='Vega spectrum')

.. image:: images/vega_spec.png
    :width: 600px
    :alt: Vega spectrum.

.. _synphot-bandpass-create:

Creating a Bandpass
-------------------

A bandpass (`~synphot.spectrum.SpectralElement`) has similar basic properties
and methods as a source spectrum (see :ref:`synphot-source-create`), except that
a bandpass throughput is always unitless. Not all source spectrum
functionalities are available for bandpass, and vice versa, so check the API
documentations.

Below are the pre-defined bandpass for common filters. By default, they are
downloaded from STScI as defined in ``synphot.config``. They can be accessed via
:func:`~synphot.spectrum.SpectralElement.from_filter` by providing the following
filter names:

===========  ======================================  ===========
Filter name  Config Item                             Description
===========  ======================================  ===========
'bessel_j'   ``synphot.config.conf.bessel_j_file``   Bessel J
'bessel_h'   ``synphot.config.conf.bessel_h_file``   Bessel H
'bessel_k'   ``synphot.config.conf.bessel_k_file``   Bessel K
'cousins_r'  ``synphot.config.conf.cousins_r_file``  Cousins R
'cousins_i'  ``synphot.config.conf.cousins_i_file``  Cousins I
'johnson_u'  ``synphot.config.conf.johnson_u_file``  Johnson U
'johnson_b'  ``synphot.config.conf.johnson_b_file``  Johnson B
'johnson_v'  ``synphot.config.conf.johnson_v_file``  Johnson V
'johnson_r'  ``synphot.config.conf.johnson_r_file``  Johnson R
'johnson_i'  ``synphot.config.conf.johnson_i_file``  Johnson I
'johnson_j'  ``synphot.config.conf.johnson_j_file``  Johnson J
'johnson_k'  ``synphot.config.conf.johnson_k_file``  Johnson K
===========  ======================================  ===========

>>> from synphot import SpectralElement
>>> johnson_b = SpectralElement.from_filter('johnson_b', encoding='binary')
Downloading ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_b_004_syn.fits
|===========================================| 8.6k/8.6k (100.00%)        00s
>>> johnson_b.plot(title=johnson_b.metadata['descrip'])

.. image:: images/johnson_b.png
    :width: 600px
    :alt: Johnson B bandpass.

Bandpass also has access to photometric parameter calculations akin to
IRAF SYNPHOT BANDPAR task (see :ref:`synphot_formulae` and respective API
documentations). Some of these need the information of telescope collecting
area, which will be set to HST value in the examples below:

>>> from astropy import units as u
>>> area = 45238.93416 * (u.cm * u.cm)
>>> johnson_b.avgwave()
<Quantity 4385.924405300897 Angstrom>
>>> johnson_b.barlam()
<Quantity 4345.239426511072 Angstrom>
>>> johnson_b.pivot()
<Quantity 4372.226931731961 Angstrom>
>>> johnson_b.unit_response(area)
<Quantity 1.0968603705608007e-19 FLAM>
>>> johnson_b.rmswidth()
<Quantity 352.319136703647 Angstrom>
>>> johnson_b.photbw()
<Quantity 338.25063150252436 Angstrom>
>>> johnson_b.fwhm()
<Quantity 796.5193673065214 Angstrom>
>>> johnson_b.tlambda()
<Quantity 0.8972899017977345>
>>> johnson_b.tpeak()
<Quantity 1.0>
>>> johnson_b.wpeak()
<Quantity 4050.0 Angstrom>
>>> johnson_b.equivwidth()
<Quantity 912.7500013855752 Angstrom>
>>> johnson_b.rectwidth()
<Quantity 912.7500013855752 Angstrom>
>>> johnson_b.efficiency()
<Quantity 0.20941490743836771>
>>> johnson_b.emflx(area)
<Quantity 1.1157590236369704e-16 FLAM>

.. _synphot-box-bandpass:

Box
^^^

Like a source spectrum, a bandpass can also be constructed from a model.
A box model is one of the most commonly used.

.. math::

    throughput = \left \{
            \begin{array}{ll}
                A   & : x_0 - w/2 \geq x \geq x_0 + w/2 \\
                0   & : \textnormal{else}
            \end{array}
        \right.

where

    * :math:`A =` Amplitude, usually 1
    * :math:`x =` Wavelength array in the unit of :math:`x_{0}`
    * :math:`x_{0} =` Central wavelength
    * :math:`w =` Width of the box in the unit of :math:`x_{0}`

>>> from modeling import models  # Has to support composite model and sampleset
>>> bp = SpectralElement(models.Box1D, amplitude=1, x_0=5000, width=100)
>>> bp.plot(top=1.1, title='Box-shaped bandpass')

.. image:: images/box_bandpass.png
    :width: 600px
    :alt: Box bandpass.


.. _synphot-spec-math-op:

Math Operations
---------------

The following operations are available for ``synphot`` spectra
(`~synphot.spectrum.BaseUnitlessSpectrum` also includes `~synphot.spectrum.SpectralElement`):

======================================== ============== ============================================= ===========
Operand 1                                Operation      Operand 2                                     Commutative
======================================== ============== ============================================= ===========
`~synphot.spectrum.SourceSpectrum`       :math:`+`      `~synphot.spectrum.SourceSpectrum`            Yes
`~synphot.spectrum.SourceSpectrum`       :math:`-`      `~synphot.spectrum.SourceSpectrum`            No
`~synphot.spectrum.SourceSpectrum`       :math:`\times` `~synphot.spectrum.BaseUnitlessSpectrum`      Yes
`~synphot.spectrum.SourceSpectrum`       :math:`\times` Scalar number                                 Yes
`~synphot.spectrum.SourceSpectrum`       :math:`\times` `~astropy.units.quantity.Quantity` (unitless) No
`~synphot.spectrum.BaseUnitlessSpectrum` :math:`\times` `~synphot.spectrum.BaseUnitlessSpectrum`      Yes
`~synphot.spectrum.BaseUnitlessSpectrum` :math:`\times` Scalar number                                 Yes
`~synphot.spectrum.BaseUnitlessSpectrum` :math:`\times` `~astropy.units.quantity.Quantity` (unitless) No
======================================== ============== ============================================= ===========

Examples
^^^^^^^^

>>> from synphot import SourceSpectrum, SpectralElement
>>> from modeling import models  # Has to support composite model and sampleset
>>> bb = SourceSpectrum.from_blackbody(6000)
>>> g1 = SourceSpectrum.from_gaussian(5e-13, 3000, 100)
>>> g2 = SourceSpectrum.from_gaussian(1e-13, 4000, 50)
>>> bp = SpectralElement(models.Box1D, amplitude=1, x_0=4000, width=3500)
>>> sp = (bb + g1 - g2) * 2 * (bp * u.Quantity(0.8))
>>> sp.plot(left=2000, right=6000)

.. image:: images/spec_math_ex1.png
    :width: 600px
    :alt: Spectrum math example.
