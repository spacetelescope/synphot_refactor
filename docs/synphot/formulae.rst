.. doctest-skip-all

.. _synphot_formulae:

Photometric Properties
======================

In here, we describe bandpass and spectral photometric properties that can be
calculated using **synphot**, along with their respective formulae.
More information can also be found in
:ref:`Koornneef et al. (1986) <synphot-ref-koornneef1986>`,
:ref:`bandpass-main`, and :ref:`synphot_observation`.

These are some common variables mentioned in the formulae in this section:

=================== =================================
Variable            Description
=================== =================================
:math:`F_{\lambda}` Source flux distribution
:math:`P_{\lambda}` Dimensionless bandpass throughput
*a*                 Telescope collecting area
*h*                 The Planck constant
*c*                 The speed of light
=================== =================================

The examples in this section uses bandpass from ACS/HRC F555W (from package
test data) with some given bins and observation from that bandpass convolved
with a blackbody::

    >>> import os
    >>> from astropy.utils.data import get_pkg_data_filename
    >>> from synphot import Observation, SourceSpectrum, SpectralElement, units
    >>> from synphot.models import BlackBodyNorm1D
    >>> area = 45238.93416 * units.AREA  # HST
    >>> sp = SourceSpectrum(BlackBodyNorm1D, temperature=5000)
    >>> bp = SpectralElement.from_file(get_pkg_data_filename(
    ...     os.path.join('data', 'hst_acs_hrc_f555w.fits'),
    ...     package='synphot.tests'))
    >>> binset = range(1000, 11001)
    >>> obs = Observation(sp, bp, binset=binset)


.. _synphot-formula-avgwv:

Bandpass Average Wavelength
---------------------------

For a bandpass, :meth:`~synphot.spectrum.BaseSpectrum.avgwave` implements
the equation for :math:`\lambda_{0}` as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836). It is
equivalent to IRAF SYNPHOT ``bandpar`` results for ``avglam``,
``avgmw``, or ``refwave``; The throughput at this wavelength is
:meth:`~synphot.spectrum.SpectralElement.tlambda`.

.. math::

    \lambda_{0} = \frac{\int \; P_{\lambda} \; \lambda \; d\lambda }{\int \; P_{\lambda} \; d\lambda}

Example::

    >>> bp.avgwave()
    <Quantity 5367.903565874441 Angstrom>
    >>> bp.tlambda()
    <Quantity 0.22807748889452203>


.. _synphot-formula-tpeak:

Bandpass Peak Throughput
------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.tpeak` implements the
bandpass peak throughput. It is equivalent to IRAF SYNPHOT ``bandpar`` result
for ``tpeak``; The wavelength at this throughput is
:meth:`~synphot.spectrum.SpectralElement.wpeak` (only first match is returned
if peak value is not unique).

Example::

    >>> bp.tpeak()
    <Quantity 0.24144500494003296>
    >>> bp.wpeak()
    <Quantity 5059.8212890625 Angstrom>


.. _synphot-formula-qtlam:

Bandpass Dimensionless Efficiency
---------------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.efficiency` implements
the dimensionless efficiency. It is equivalent to IRAF SYNPHOT ``bandpar``
result for ``qtlam``.

.. math::

    \text{qtlam} = \int \frac{P_{\lambda}}{\lambda} d\lambda

Example::

    >>> bp.efficiency()
    <Quantity 0.05090165033079963>


.. _synphot-formula-equvw:

Bandpass Equivalent Width
-------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.equivwidth` implements
the equivalent width. It gives the same value as
:meth:`~synphot.spectrum.BaseSpectrum.integrate` and is equivalent to
IRAF SYNPHOT ``bandpar`` result for ``equvw``.

.. math::

    \text{equvw} = \int P_{\lambda} d\lambda

Example::

    >>> bp.equivwidth()
    <Quantity 272.0108162945954 Angstrom>
    >>> bp.integrate()
    <Quantity 272.0108162945954 Angstrom>


.. _synphot-formula-rectw:

Bandpass Rectangular Width
--------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.rectwidth` implements
the rectangular width. It is equivalent to IRAF SYNPHOT ``bandpar`` result for
``rectw``. The ``equvw`` in the formula below is :ref:`synphot-formula-equvw`.

.. math::

    \text{rectw} = \frac{\text{equvw}}{\text{MAX}(P_{\lambda})}

Example::

    >>> bp.rectwidth()
    <Quantity 1126.5953352903448 Angstrom>


.. _synphot-formula-rmswidth:

Bandpass RMS Band Width (Koornneef)
-----------------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.rmswidth` implements
the bandpass RMS width as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836), where
:math:`\lambda_{0}` is the :ref:`synphot-formula-avgwv`.

.. math::

    \lambda_{\text{rms}} = \sqrt{\frac{\int \; P_{\lambda} \; (\lambda - \lambda_{0})^{2} \; d\lambda}{\int \; P_{\lambda} \: d\lambda}}

Example::

    >>> bp.rmswidth()
    <Quantity 359.56457676412236 Angstrom>


.. _synphot-formula-bandw:

Bandpass RMS Band Width (IRAF)
------------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.photbw` implements the
equivalent for ``bandw`` from IRAF SYNPHOT ``bandpar`` task, where
:math:`\bar{\lambda}` is :ref:`synphot-formula-barlam`. This is not the same
as :ref:`synphot-formula-rmswidth`.

.. math::

    \text{bandw} = \bar{\lambda} \; \sqrt{\frac{\int \; (P_{\lambda} / \lambda) \; \ln(\lambda \; / \; \bar{\lambda})^{2} \; d\lambda}{\int \; (P_{\lambda} / \lambda) \; d\lambda}}

Example::

    >>> bp.photbw()
    <Quantity 357.17951791474843 Angstrom>


.. _synphot-formula-fwhm:

FWHM
----

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.fwhm` implements the
equivalent for ``fwhm`` from IRAF SYNPHOT ``bandpar`` task, where ``bandw``
is :ref:`synphot-formula-bandw`.

.. math::

    \text{fwhm} = \text{bandw} \; \sqrt{8 \; \log 2}

Example::

    >>> bp.fwhm()
    <Quantity 841.0934884601406 Angstrom>


.. _synphot-formula-barlam:

Bandpass Mean Log Wavelength
----------------------------

For a bandpass, :meth:`~synphot.spectrum.BaseSpectrum.barlam` implements the
mean wavelength as defined in
:ref:`Schneider, Gunn, and Hoessel (1983) <synphot-ref-schneider1983>`.
This rather unusual definition is such that the corresponding mean frequency is
:math:`c / \bar{\lambda}`.
It is equivalent to IRAF SYNPHOT ``bandpar`` results for ``barlam``.

.. math::

    \bar{\lambda} = \exp\Bigg[\frac{\int \; (P_{\lambda} / \lambda) \; \ln(\lambda) \; d\lambda}{\int (P_{\lambda} / \lambda) \; d\lambda}\Bigg]

Example::

    >>> bp.barlam()
    <Quantity 5331.8648495386 Angstrom>


.. _synphot-formula-uresp:

Bandpass Unit Response
----------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.unit_response`
implements the computation of the flux of a star that produces a response of
one count per second in that bandpass for a given telescope collecting area.
It is equivalent to IRAF SYNPHOT ``bandpar`` result for ``uresp``.

.. math::

    \text{uresp} = \frac{hc}{a \int P_{\lambda}\; \lambda\; d\lambda}

Example::

    >>> bp.unit_response(area)
    <Quantity 3.007277127274156e-19 FLAM>


.. _synphot-formula-emflx:

Bandpass Equivalent Monochromatic Flux
--------------------------------------

For a bandpass, :meth:`~synphot.spectrum.SpectralElement.emflx` implements the
equivalent monochromatic flux for a given telescope collecting area.
It is equivalent to IRAF SYNPHOT ``bandpar`` result for ``emflx``.
In the formula below, ``uresp``, ``equvw``, and :math:`\lambda_{0}` are
:ref:`synphot-formula-uresp`, :ref:`synphot-formula-equvw`, and
:ref:`synphot-formula-avgwv`, respectively.

.. math::

    \text{emflx} = \frac{\text{uresp} \times \text{equvw}}{P(\lambda_{0})}

Example::

    >>> bp.emflx(area)
    <Quantity 3.586552579909415e-16 FLAM>

.. _synphot-formula-effstim:

Effective Stimulus
------------------

For an observation, :meth:`~synphot.observation.Observation.effstim` calculates
the predicted effective stimulus in given flux unit.
:meth:`~synphot.observation.Observation.countrate` is a special form of
effective stimulus in the unit of count/s given a telescope collecting area.
It is equivalent to IRAF SYNPHOT ``calcphot`` result for ``effstim``.
The default binning behavior is to be consistent with ASTROLIB PYSYNPHOT.

.. math::

    \text{effstim} = \frac{\int\; F_{\lambda}\; P_{\lambda}\; \lambda\; d\lambda}{\int\; P_{\lambda}\; \lambda\; d\lambda}

Example::

    >>> obs.effstim()
    <Quantity 0.00053744 PHOTLAM>
    >>> obs.effstim('flam')
    <Quantity 1.99333435e-15 FLAM>
    >>> obs.effstim('count', area=area)  # Not binned
    <Quantity 6628.36886854 ct / s>
    >>> obs.countrate(area=area, binned=False)
    <Quantity 6628.36886854 ct / s>
    >>> obs.countrate(area=area)  # Binned
    <Quantity 6628.36888121 ct / s>


.. _synphot-formula-effwave:

Effective Wavelength
--------------------

For an observation,
:meth:`~synphot.observation.Observation.effective_wavelength`
implements the effective wavelength, as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836), where flux
unit is converted to FLAM prior to calculations.
It is equivalent to IRAF SYNPHOT ``calcphot`` result for ``efflerg``.
For backward compatibility, there is also an option (``mode='efflphot'``) to
calculate this using flux in PHOTLAM, which is equivalent to IRAF SYNPHOT
``calcphot`` result for ``efflphot``.
The default binning behavior is to be consistent with ASTROLIB PYSYNPHOT.

.. math::

    \lambda_{\text{eff}} = \frac{\int \; F_{\lambda} \; P_{\lambda} \; \lambda^2 \; d\lambda}{\int \; F_{\lambda} \; P_{\lambda} \; \lambda \; d\lambda}

Example::

    >>> obs.effective_wavelength()  # Binned
    <Quantity 5401.267857308841 Angstrom>
    >>> obs.effective_wavelength(mode='efflphot')  # Deprecated
    WARNING: AstropyDeprecationWarning: Usage of EFFLPHOT is deprecated. [...]
    <Quantity 5424.929868234263 Angstrom>


.. _synphot-formula-pivwv:

Pivot Wavelength
----------------

For a bandpass or a source spectrum,
:meth:`~synphot.spectrum.BaseSpectrum.pivot` calculates the pivot wavelength.
It is equivalent to IRAF SYNPHOT result for ``pivwv`` and ``pivot``.
The formula shown applies to a bandpass. For a source, replace
:math:`P_{\lambda}` with :math:`F_{\lambda}` below.

.. math::

    \lambda_{\text{pivot}} = \sqrt{\frac{\int \: P_{\lambda} \; \lambda \; d\lambda}{\int(P_{\lambda} \; / \; \lambda) \; d\lambda}}

Example::

    >>> bp.pivot()
    <Quantity 5355.863596422958 Angstrom>
    >>> obs.pivot()  # Not binned
    <Quantity 5389.368734064575 Angstrom>
