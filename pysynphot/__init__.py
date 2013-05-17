# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
:Package:  pysynphot

Purpose
========

Replacement for STSDAS synphot package.

This __init__ file is used to expose the desired elements of the user
interface for interactive use.


Dependencies
=============
- numpy 1.5.1 or greater
- pyfits 2.4 or greater


Environment
============
The environment variable PYSYN_CDBS must be set.

Example
========

In the examples below, items which may be installation- or platform-
specific are commented out so as to be excluded from doctest. However
users are still encouraged to try these examples.

A quickstart tutorial containing further examples and other documentation
can be found at U{http://stsdas.stsci.edu/pysynphot/


>>> import pysynphot as S
>>> import os
>>> print S.__version__
2.0.0dev
>>> #Read a spectrum from a file
>>> vega=S.FileSpectrum(S.locations.VegaFile)


>>> bb=S.BlackBody(40000)
>>> print bb
BB(T=40000)


>>> pl=S.PowerLaw(10000,-2)
>>> print pl
Power law: refwave 10000 angstrom, index -2


>>> g1=S.GaussianSource(18.3,18000,2000,fluxunits='abmag')
>>> print g1
Gaussian: mu=18000 angstrom,fwhm=2000 angstrom, total flux=18.3 abmag

>>> unitflux=S.FlatSpectrum(18,fluxunits='abmag')
>>> print unitflux
Flat spectrum of 18 abmag

>>> bp1=S.ObsBandpass('acs,hrc,f555w')
>>> print bp1
acs,hrc,f555w
>>> print bp1.wave
[   500.   1000.   1010. ...,  11999.  30000.  30010.]
>>> print bp1.throughput
[ 0.  0.  0. ...,  0.  0.  0.]

>>> len(bp1)
6

>>> print bp1.waveunits
angstrom

>>> obs1=S.Observation(vega,bp1)

>>> print obs1.waveunits
angstrom
>>> print obs1.fluxunits
flam

"""
from __future__ import division

from pysynphot.version import (__version__, __svn_revision__,
                               __svn_full_info__, __setup_datetime__)

# For backwards compatibility
__svn_version__ = __svn_revision__
__full_svn_info__ = __svn_full_info__


#UI:
#AnalyticSpectra:
from spectrum import BlackBody, GaussianSource, FlatSpectrum
from spectrum import Powerlaw as PowerLaw
#Tabular Spectra
from spectrum import FileSourceSpectrum as FileSpectrum
from spectrum import ArraySourceSpectrum as ArraySpectrum
from catalog import Icat
#Analytic Spectral Elements
from spectrum import Box, UniformTransmission
#Tabular Spectral Elements
from spectrum import FileSpectralElement as FileBandpass
from spectrum import ArraySpectralElement as ArrayBandpass
#Complicated spectral elements
from obsbandpass import ObsBandpass
from reddening import Extinction
#Observations
from observation import Observation
#Other constructs
from observationmode import ObservationMode as Obsmode
from numpy import arange as Waveset
#Get Vega
from spectrum import Vega
#Get cache
import Cache
#Permit resetting refdata
from refs import setref, showref
#
from locations import get_data_filename
import tables

def _test():
    "Runs doctest on the examples in this file"
    import doctest
    nfail,ntest=doctest.testfile('__init__.py')
    return nfail,ntest

if __name__ == '__main__':
    nfail,ntest=_test()
