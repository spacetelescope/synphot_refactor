from __future__ import division
"""Applies to both #125 and #126.
Test raises an error if the bug has not been fixed."""
import sys
import os
import testutil
import pysynphot as S
import numpy as N
from pysynphot.units import Units
from pysynphot import extinction, spectrum, units, spparser
from pysynphot.obsbandpass import ObsBandpass

class ticket125(testutil.FPTestCase):
    def setUp(self):
        self.spstring="rn(icat(k93models,44500,0.0,5.0),band(nicmos,2,f222m),18,vegamag)"
    def testparse(self):
        self.spstring=spparser.parse_spec(self.spstring)
        
