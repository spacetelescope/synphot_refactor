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
- astropy 0.2 or greater


Environment
============
The environment variable PYSYN_CDBS must be set.


"""
from __future__ import division, print_function

#UI:
import spectrum
import catalog
import obsbandpass
import reddening
import observation
import observationmode
import Cache
import refs
import locations
import tables

__version__ = "3.0.0.dev"
