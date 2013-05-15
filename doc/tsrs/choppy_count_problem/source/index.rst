.. TSR 2009-02 documentation master file, created by
   sphinx-quickstart on Mon Oct 26 15:19:38 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TSR 2009-02: Choppy source plot in ETC 18.0
============================================

.. abstract::
   :author: Victoria G. Laidler
   :date: 26 October 2009

   A source spectrum plot in ETC 18.0 was observed to appear strange
   and choppy compared to the corresponding file in CDBS. The choppy
   appearance is an artifact of the uneven wavelength spacing in the
   source spectrum, which is preserved by pysynphot but was not
   preserved by SYNPHOT, together with the fact that a spectrum in
   counts is integrated over the bin width.


.. toctree::
   :maxdepth: 2

   main.rst
   commands.rst

