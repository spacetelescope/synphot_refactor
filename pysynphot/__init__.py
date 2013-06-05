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


"""
from __future__ import division, print_function

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
#Get Vega
from spectrum import Vega
#Get cache
import Cache
#Permit resetting refdata
from refs import setref, showref
#
from locations import get_data_filename
import tables

__version__ = "3.0.0.dev"
