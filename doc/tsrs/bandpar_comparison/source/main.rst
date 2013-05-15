Comparison of Synphot and Pysynphot Bandpar Functionality
=========================================================

.. abstract::
   :author: Matt Davis (SSB)
   :date: 15 November 2011
   
   Pysynphot attempts to replicate much of the functionality of the Synphot
   `bandpar utility
   <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_ 
   but sometimes uses different formulae and algorithms.
   This TSR collects the calculations used in Pysynphot, Synphot, the
   formulae described in the `Synphot Manual`_ in Section 5.1 on page 42,
   and the formulae in the Synphot help files.
   
.. _Synphot Manual: http://stsdas.stsci.edu/stsci_python_epydoc/SynphotManual.pdf
   
RMS Width - BANDW - PHOTBW
==========================

Summary
-------

RMS width is added to image headers in the PHOTBW keyword.

**Pysynphot**

* *Function name*: `SpectralElement.rmswidth
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1083>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*: :ref:`3: page 836 <ref3>`

**Synphot**

* *Bandpar name*: `BANDW
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `rmslam`_ called by `comppar`_ called by `bandpar`_.
* *Source code*: `rmslam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/rmslam.x>`_
* *References*: :ref:`1: sections 5.1,7.1 <ref1>`, :ref:`2 <ref2>`,
  :ref:`4: page 46 <ref4>`

.. _comppar: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/bandpar/comppar.x
.. _bandpar: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/bandpar/bandpar.x


Synphot Equations
-----------------

The `Synphot Manual`_ section 5.1 gives the equation for RMS bandwidth as

.. math::

   \lambda_{rms}^2 = \bar{\lambda}^2 \frac{\int P_{\lambda} \ln(\lambda/\bar{\lambda})^2
   \,d\lambda/\lambda}{\int P_{\lambda} \,d\lambda/\lambda}
  
where

.. math::

   \bar{\lambda} = \exp \left[ \frac{\int P_{\lambda} \ln(\lambda) \,d\lambda/\lambda}
   {\int P_{\lambda} \,d\lambda/\lambda} \right].

The Synphot function `rmslam`_ does appear to implement this procedure for
calculating the RMS width of the bandpass. The source code references the 
`WF/PC-1 Instrument Handbook <http://www.stsci.edu/hst/wfpc/documents/HST_WFPC_Instrument_Handbook.pdf>`_
as the source of the equation for RMS width and references
Schneider, Gunn and Hoessel (1983 ApJ 264,337) as the source for the equation
for mean wavelength.

The
`bandpar help file
<https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
gives the same equations as above for the RMS width but the `Synphot Manual`_
in section 7.1 gives different equations when describing bandpar. The equations
in section 7.1 are the same as used by Pysynphot, shown below.

.. _rmslam: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/rmslam.x

Pysynphot Equations
-------------------

The Pysynphot `rmswidth`_ source code references Koornneef et al 1987, page 836
as the source for its RMS width calculation, which is

.. math::

   \lambda_{rms}^2 = \frac{\int P_{\lambda} (\lambda - \bar{\lambda})^2 \,d\lambda}
   {\int P_{\lambda} \,d\lambda}
  
where

.. math::

   \bar{\lambda} = \frac{\int \lambda P_{\lambda} \,d\lambda}
   {\int P_{\lambda} \,d\lambda}.
   
.. _rmswidth: https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1106

Full Width Half-Max - FWHM
==========================

Summary
-------

**Pysynphot**

* *Function name*: `SpectralElement.fwhm
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1462>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `FWHM
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `fwhmlam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/fwhmlam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `fwhmlam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/fwhmlam.x>`_
* *References*: :ref:`1: section 5.1 <ref1>`

Synphot Equations
-----------------

The FWHM is simply defined relative to the RMS width above:

.. math::

   fwhm = \sqrt{8\ln 2}\cdot rmswidth

Pysynphot Equations
-------------------

Pysynphot does not currently implement a FWHM calculation.
See https://trac.assembla.com/astrolib/ticket/139.

Equivalent Width - EQUVW
========================

Summary
-------

**Pysynphot**

* *Function name*: `SpectralElement.equvwidth 
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1126>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `EQUVW 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `widthlam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/widthlam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `widthlam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/widthlam.x>`_
* *References*: :ref:`1: section 5.1 <ref1>`

Synphot Equations
-----------------

The equivalent width is simply the integral of the throughput:

.. math::

   equvw = \int P_{\lambda}\,d\lambda

Pysynphot Equations
-------------------

Pysynphot calculates the equivalent width in the same manner as Synphot.

Rectangular Width - RECTW
=========================

Summary
-------

**Pysynphot**

* *Function name*: `SpectralElement.rectwidth 
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1109>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `RECTW 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `widthlam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/widthlam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `widthlam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/widthlam.x>`_
* *References*: :ref:`1: section 5.1 <ref1>`

Synphot Equations
-----------------

Synphot calculates the rectangular width at the same time it calculates the
equivalent width by simply dividing the equivalent width by the maximum
throughput of the passband:

.. math::

   rectw = \frac{equvw}{\max(P_{\lambda})}

This is equivalent to the formula given in section 5.1 of the `Synphot Manual`_:

.. math::

    rectw = \frac{\int P_{\lambda}\,d\lambda}{\max(P_{\lambda})}

Pysynphot Equations
-------------------

Pysynphot calculates the rectangular width in functionally the same way as
Synphot but does not defer any calculation to the equivalent width method.
Instead, Pysynphot directly calculates the integral of the throughput and
divides by the maximum within the `rectwidth method
<https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1109>`_.

Unit Response - URESP - PHOTFLAM
================================

Summary
-------

Unit response is added to image headers in the PHOTFLAM keyword.

**Pysynphot**

* *Function name*: `SpectralElement.unit_response
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1429>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `URESP 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `funit
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/funit.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `funit.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/funit.x>`_
* *References*: :ref:`1: sections 5.1, 7.1 <ref1>`

Synphot Equations
-----------------

.. math::

   U_{\lambda} = \frac{hc/A}{\int \lambda P_{\lambda}\,d\lambda}

where :math:`h` and :math:`c` are the usual fundamental constants and
:math:`A` is the area of the telescope primary mirror.

Pysynphot Equations
-------------------

Pysynphot calculates the unit response in the same way as Synphot.

Pivot Wavelength - PIVWV - PHOTPLAM
===================================

Summary
-------

Pivot wavelength is added to image headers in the PHOTPLAM keyword.

**Pysynphot**

* *Function name*: `SpectralElement.pivot
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1060>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `PIVWV 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `pivlam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/pivlam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `pivlam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/pivlam.x>`_
* *References*: :ref:`1: sections 5.1, 7.1 <ref1>`

Synphot Equations
-----------------

The pivot wavelength equation is recorded in sections 5.1 and 7.1 of the
`Synphot Manual`_ and matches in both places.

.. math::

   \lambda_p = \sqrt{\frac{\int \lambda P_{\lambda}\,d\lambda}
                    {\int P_{\lambda}\,d\lambda/\lambda}}

Pysynphot Equations
-------------------

Pysynphot calculates the pivot wavelength in the same way as Synphot.

Wavelength at Peak Throughput - WPEAK
=====================================

Summary
-------

**Pysynphot**

* *Function name*:
* *Source code*:
* *References*:

**Synphot**

* *Bandpar name*: `WPEAK 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `peaklam2 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/peaklam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `peaklam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/peaklam.x>`_
* *References*: :ref:`1: sections 5.1 <ref1>`

Synphot Equations
-----------------

Like the name implies, this is simply the wavelength at the point of peak
throughput. Synphot finds it by looping over the throughput.

Pysynphot Equations
-------------------

Pysynphot does not currently implement a peak wavelength calculation.
See https://trac.assembla.com/astrolib/ticket/139.

Peak Throughput - TPEAK
=======================

Summary
-------

**Pysynphot**

* *Function name*:
* *Source code*:
* *References*:

**Synphot**

* *Bandpar name*: `TPEAK 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `peaklam2 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/peaklam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `peaklam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/peaklam.x>`_
* *References*: :ref:`1: sections 5.1 <ref1>`

Synphot Equations
-----------------

This is simply the maximum throughput of the passband. Synphot finds it by
looping over the throughput.

Pysynphot Equations
-------------------

Pysynphot does not currently implement a peak throughput calculation.
See https://trac.assembla.com/astrolib/ticket/139.

Average Wavelength - AVGWV
==========================

Summary
-------

**Pysynphot**

* *Function name*: `SpectralElement.avgwave
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1039>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*: :ref:`3: page 836 <ref3>`

**Synphot**

* *Bandpar name*: `AVGWV
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `avglam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/avglam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `avglam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/avglam.x>`_
* *References*: :ref:`1: sections 5.1, 7.1 <ref1>`

Synphot Equations
-----------------

.. math::

   \lambda_0 = \frac{\int \lambda P_{\lambda}\,d\lambda}
                {\int P_{\lambda}\,d\lambda}

Pysynphot Equations
-------------------

Pysynphot calculates the average wavelength in the same way as Synphot.

Dimensionless Efficiency - QTLAM
================================

Summary
-------

**Pysynphot**

* *Function name*: `SpectralElement.efficiency
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1131>`_
* *Source code*: `spectrum.py
  <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*:

**Synphot**

* *Bandpar name*: `QTLAM
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `qtlam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/qtlam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `qtlam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/qtlam.x>`_
* *References*: :ref:`1: section 5.1 <ref1>`, :ref:`5: page 152 <ref5>`

Synphot Equations
-----------------

.. math::

   qtlam = \int P_{\lambda}\,d\lambda/\lambda

Pysynphot Equations
-------------------

Pysynphot calculates the efficiency in the same way as Synphot.

Throughput at Reference Wavelength - TLAMBDA
============================================

Summary
-------

**Pysynphot**

* *Function name*:
* *Source code*:
* *References*:

**Synphot**

* *Bandpar name*: `TLAMBDA
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `monolam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/monolam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `monolam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/monolam.x>`_
* *References*: :ref:`1: sections 5.1 <ref1>`

Synphot Equations
-----------------

This is simply the bandpass throughput at a reference wavelength. By default
the reference wavelength is the average wavelength as defined above.

Pysynphot Equations
-------------------

The throughput of a Pysynphot SpectralElement object can be sampled at any
wavelength using the `sample() method
<https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1251>`_.
There is no function specifically for retrieving the throughput at the
average wavelength.

Equivalent Monochromatic Flux - EMFLX
=====================================

Summary
-------

**Pysynphot**

* *Function name*:
* *Source code*:
* *References*:

**Synphot**

* *Bandpar name*: `EMFLX
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `monolam 
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/monolam.x>`_
  called by `comppar`_ called by `bandpar`_.
* *Source code*: `monolam.x
  <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/newlib/monolam.x>`_
* *References*: :ref:`1: sections 5.1 <ref1>`

Synphot Equations
-----------------

The equivalent monochromatic flux is a combination of unit response,
rectangular width, peak throughput and throughput at the average wavelength:

.. math::

   emflx = uresp \cdot rectw \cdot \frac{tpeak}{tlambda}

Pysynphot Equations
-------------------

Pysynphot does not currently implement an equivalent monochromatic flux
calculation. See https://trac.assembla.com/astrolib/ticket/139.

Reference Wavelength - REFWAVE
==============================

See the section on average wavelength above.
                