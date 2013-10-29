.. _synphot_reddening:

Extinction
==========

Extinction in ``synphot`` is defined by R(V) across some wavelength values.

.. math::

    R(V) = \frac{A(V)}{E(B-V)}

Below are the pre-defined extinction models. By default, they are downloaded
from a remote location as defined in `synphot.config`. They can be accessed
via :func:`synphot.reddening.ExtinctionCurve.from_model` by providing the
class method with the corresponding model name:

==========  ================  ===========================  ====  =================================================================
Model name  Config Item       Description                  R(V)  Reference
==========  ================  ===========================  ====  =================================================================
'lmc30dor'  ``LMC30DORFILE``  LMC2 Supershell              2.76  :ref:`Gordon et al. 2003 <synphot-ref-extinction-gordon2003>`
'lmcavg'    ``LMCAVGFILE``    LMC Average                  3.41  :ref:`Gordon et al. 2003 <synphot-ref-extinction-gordon2003>`
'mwavg'     ``MWAVGFILE``     Milky Way Diffuse            3.1   :ref:`Cardelli et al. 1989 <synphot-ref-extinction-cardelli1989>`
'mwdense'   ``MWDENSEFILE``   Milky Way Dense              5.0   :ref:`Cardelli et al. 1989 <synphot-ref-extinction-cardelli1989>`
'mwrv21'    ``MWRV21FILE``    Milky Way CCM                2.1   :ref:`Cardelli et al. 1989 <synphot-ref-extinction-cardelli1989>`
'mwrv40'    ``MWRV40FILE``    Milky Way CCM                4.0   :ref:`Cardelli et al. 1989 <synphot-ref-extinction-cardelli1989>`
'smcbar'    ``SMCBARFILE``    SMC Bar                      2.74  :ref:`Gordon et al. 2003 <synphot-ref-extinction-gordon2003>`
'xgalsb'    ``XGALFILE``      Starburst (attenuation law)  4.0   :ref:`Calzetti et al. 2000 <synphot-ref-extinction-calzetti2000>`
==========  ================  ===========================  ====  =================================================================


Examples
--------

>>> TODO
