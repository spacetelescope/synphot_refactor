# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division
"""This module is a container for IO-intensive items that should be
read in only once, and then re-used from memory.

This is planned to include the reddening laws and some indexes for the
Kurucz and Castelli-Kurucz model atlases."""

from locations import RedLaws

# if PYSYN_CDBS is undefined RedLaws will be an empty dictionary
# so we should check whether these assignments are possible
if 'mwavg' in RedLaws:
    RedLaws[None]=RedLaws['mwavg'] #Establishes default
    RedLaws['gal3']=RedLaws['mwavg'] #Temporary: for syn_pysyn testing

CATALOG_CACHE = {}

def reset_catalog_cache():
    """
    Empty the CATALOG_CACHE global variable.
    """
    global CATALOG_CACHE
    
    CATALOG_CACHE.clear()
