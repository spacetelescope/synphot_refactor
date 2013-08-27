# Licensed under a 3-clause BSD style license - see LICENSE.rst

# A quickstart tutorial containing further examples and other documentation
# can be found at U{http://stsdas.stsci.edu/pysynphot/

from __future__ import division, print_function

import pysynphot as pysyn


def test_blackbody():
    bb = pysyn.spectrum.BlackBody(40000)
    # BB(T=40000)
    assert bb


# >>> pl=S.PowerLaw(10000,-2)
# >>> print pl
# Power law: refwave 10000 angstrom, index -2
#
#
# >>> g1=S.GaussianSource(18.3,18000,2000,fluxunits='abmag')
# >>> print g1
# Gaussian: mu=18000 angstrom,fwhm=2000 angstrom, total flux=18.3 abmag
#
# >>> unitflux=S.FlatSpectrum(18,fluxunits='abmag')
# >>> print unitflux
# Flat spectrum of 18 abmag
#
# >>> bp1=S.ObsBandpass('acs,hrc,f555w')
# >>> print bp1
# acs,hrc,f555w
# >>> print bp1.wave
# [   500.   1000.   1010. ...,  11999.  30000.  30010.]
# >>> print bp1.throughput
# [ 0.  0.  0. ...,  0.  0.  0.]
#
# >>> len(bp1)
# 6
#
# >>> print bp1.waveunits
# angstrom
#
# >>> obs1=S.Observation(vega,bp1)
#
# >>> print obs1.waveunits
# angstrom
# >>> print obs1.fluxunits
# flam

# Read a spectrum from a file
# vega=S.FileSpectrum(S.locations.VegaFile)

