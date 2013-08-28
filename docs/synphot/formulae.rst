.. _synphot_formulae:


``synphot`` Formulae
====================

This section contains the formulae for different spectrum properties.
Some are used for both observation (source spectrum convolved with passband)
and passband, while some are just for one of them, as specified below.

*INT* is the integral with respect to wavelengths, *EXP* is exponent,
*LN* is the natural logarithm, *LOG* is base 10 logarithm,
*flux* is spectrum flux array, *thru* is passband throughput,
and *wave* is the array of wavelengths corresponding to flux or throughput.


For Both Observation and Passband
---------------------------------

In this case, *flux* in the formulae can also be replaced by *thru*.


.. _synphot-formula-avgwv:

Average Wavelength
^^^^^^^^^^^^^^^^^^

This implements the equation for :math:`\\lambda_{0}` as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`, page 836.

Equivalent to IRAF SYNPHOT BANDPAR results for
``AVGLAM``, ``AVGWV``, or ``REFWAVE``. For a passband, the throughput at this
wavelength is ``TLAMBDA``.

.. math::

    \lambda_{0} = \frac{INT(flux * wave)}{INT(flux)}


.. _synphot-formula-barlam:

Mean Log Wavelength
^^^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT result for ``BARLAM``.

.. math::

    \bar{\lambda} = EXP(INT(flux * LN(wave) / wave) / INT(flux / wave))


For Passband Only
-----------------

.. _synphot-formula-uresp:

Unit Response
^^^^^^^^^^^^^

This is the flux (in FLAM) of a star that produces a response of one photon
per second in the passband.

Equivalent to IRAF SYNPHOT BANDPAR result for ``URESP``, where H and C are
astronomical constants, and *AREA* is the telescope collecting area.

.. math::

    URESP = \\frac{H * C}{AREA * INT(thru * wave)}


.. _synphot-formula-pivwv:

Pivot Wavelength
^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``PIVWV``.

.. math::

    \lambda_{pivot} = \sqrt{\frac{INT(thru * wave)}{INT(thru / wave)}}


.. _synphot-formula-bandw:

Passband RMS Width (IRAF)
^^^^^^^^^^^^^^^^^^^^^^^^^

This is not the same as passband RMS width in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`.

Equivalent to IRAF SYNPHOT BANDPAR result for ``BANDW``, where
:math:`\bar{\lambda}` is :ref:`synphot-formula-barlam`.

.. math::

    BANDW = \bar{\lambda} * \sqrt{INT(thru * LN(wave / \bar{\lambda})^{2} / wave) / INT(thru / wave)}


.. _synphot-formula-fwhm:

FWHM
^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``FWHM``, where ``BANDW`` is
:ref:`synphot-formula-bandw`.

.. math::

    FWHM = \sqrt{8 * LOG(2)} * BANDW


.. _synphot-formula-tpeak:

Peak Throughput
^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``TPEAK``, which corresponds
to the wavelength at ``WPEAK``.

.. math::

    TPEAK = MAX(thru)


.. _synphot-formula-equvw:

Equivalent Width
^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``EQUVW``.

.. math::

    EQUVW = INT(thru)


.. _synphot-formula-rectw:

Rectangular Width
^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``RECTW``, where ``EQUVW``
is :ref:`synphot-formula-equvw` and ``TPEAK`` is :ref:`synphot-formula-tpeak`.

.. math::

    rectw = EQUVW / TPEAK


.. _synphot-formula-qtlam:

Dimensionless Efficiency
^^^^^^^^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``QTLAM``.

.. math::

    QTLAM = INT(thru / wave)


.. _synphot-formula-emflx:

Equivalent Monochromatic Flux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT BANDPAR result for ``EMFLX``, where ``URESP`` is
:ref:`synphot-formula-uresp`, ``RECTW`` is :ref:`synphot-formula-rectw`,
``TPEAK`` is :ref:`synphot-formula-tpeak`, and ``TLAMBDA`` is throughput at
:ref:`synphot-formula-avgwv`.

.. math::

    EMFLX = URESP * RECTW * (TPEAK / TLAMBDA)


For Observation Only
--------------------

.. _synphot-formula-effwave:

Effective Wavelength
^^^^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT CALCPHOT result for:

    * ``EFFLERG`` if :math:`flux_{obs}` is in FLAM (this is the correct
      version, as defined in
      :ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`, page 836).
    * ``EFFLPHOT`` or ``EFFLAM`` if :math:`flux_{obs}` is in PHOTLAM (this
      is depreciated in IRAF SYNPHOT but kept for backward compatibility).

.. math::

    \lambda_{eff} = \frac{INT(flux_{obs} * wave^{2})}{INT(flux_{obs} * wave)}


.. _synphot-formula-effstim:

Effective Stimulus
^^^^^^^^^^^^^^^^^^

Equivalent to IRAF SYNPHOT CALCPHOT result for ``EFFSTIM``.

.. math::

    EFFSTIM = \frac{INT(flux_{source} * thru_{passband} * wave)}{INT(thru_{passband} * wave)}
