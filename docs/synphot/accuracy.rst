.. doctest-skip-all

.. _synphot_accuracy:

Accuracy of Results
===================

``synphot`` is not a straight port from ASTROLIB PYSYNPHOT nor IRAF SYNPHOT.
It is a re-implementation designed to use `astropy.modeling`. Therefore, you
should expect that some calculations will give different results.

An extensive commissioning process will be performed to verify that the results
produced by ``synphot`` are either as good as, or better than, the results
obtained using ASTROLIB PYSYNPHOT for the same calculations.
