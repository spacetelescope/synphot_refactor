"""
:Package:  Astrolib Pysynphot

Purpose
========

Object-oriented replacement for STSDAS synphot package.

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
0.9.4dev
>>> #Read a spectrum from a file
>>> vega=S.FileSpectrum(S.locations.VegaFile)



..  ##>>> print vega
    ##/user/laidler/pyinstall/pysynphot/data/alpha_lyr_stis_003.fits
    ## >>> vega.wave
    ## array([  9.00452026e+02,   9.01354004e+02,   9.02257996e+02, ...,
    ##          2.99353200e+06,   2.99653275e+06,   2.99953700e+06], dtype=float32)
    ## >>> vega.flux
    ## array([  1.23810534e-17,   1.67559564e-17,   1.78002369e-17, ...,
    ##          1.40140738e-19,   1.38734357e-19,   1.26490663e-19])


>>> bb=S.BlackBody(40000)
>>> print bb
BB(T=40000)

..  ## >>> print bb.wave
    ## [   500.            500.19760122    500.39528054 ...,  25969.1985582
    ##   25979.46164894  25989.72879567]
    ## >>> print bb.flux
    ## [ 1.1523018   1.15375884  1.15521644 ...,  0.00141824  0.0014166
    ##   0.00141496]


>>> pl=S.PowerLaw(10000,-2)
>>> print pl
Power law: refwave 10000 angstrom, index -2

..  ## >>> print pl.wave
    ## [   500.            500.19760122    500.39528054 ...,  25969.1985582
    ##   25979.46164894  25989.72879567]
    ## >>> print pl.flux
    ## [  4.00000000e+02   3.99684025e+02   3.99368300e+02 ...,   1.48280112e-01
    ##    1.48162980e-01   1.48045941e-01]

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

..  ## >>> bp1.showfiles()
    ## /grp/hst/cdbs/comp/ota/hst_ota_007_syn.fits
    ## /grp/hst/cdbs/comp/acs/acs_hrc_m12_005_syn.fits
    ## /grp/hst/cdbs/comp/acs/acs_hrc_m3_005_syn.fits
    ## /grp/hst/cdbs/comp/acs/acs_f555w_003_syn.fits
    ## /grp/hst/cdbs/comp/acs/acs_hrc_win_005_syn.fits
    ## /grp/hst/cdbs/comp/acs/acs_hrc_ccd_013_syn.fits

>>> len(bp1)
6

..  ## >>> sp1=S.FileSpectrum('/grp/hst/cdbs/calspec/feige66_002.fits')

>>> print bp1.waveunits
angstrom

.. ##>>> obs1=S.Observation(sp1,bp1)

>>> obs1=S.Observation(vega,bp1)

..  ## >>> print obs1
    ## /grp/hst/cdbs/calspec/feige66_002.fits * acs,hrc,f555w


    ##>>> print obs1.wave
    ##[   500.   1000.   1010. ...,  11999.  30000.  30010.]

    ## >>> print obs1.flux.max()
    ## 7.51179802362e-14

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
