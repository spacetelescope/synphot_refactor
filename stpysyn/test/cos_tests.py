"""Container for tests of newly added cos functionality such
as new obsmodes.
In general, these tests simply test for file integrity -- ie, if there
are no errors, the tests pass -- rather than comparison resultz.
"""

from __future__ import division

import unittest

import pysynphot as S

class TestCosObsmodes(unittest.TestCase):
    def setUp(self):
        self.tda=dict()
        
    def test_c1055(self):
        self.obsmode='cos,fuv,g130m,c1055'
        self.tda['obsmode']=self.obsmode
        bp = S.ObsBandpass(self.obsmode)
        obs = S.Observation(S.BlackBody(5500), bp)

        
    def test_c1096(self):
        self.obsmode='cos,fuv,g130m,c1096'
        self.tda['obsmode']=self.obsmode
        bp = S.ObsBandpass(self.obsmode)
        obs = S.Observation(S.BlackBody(5500), bp)
        
    def test_c1280(self):
        self.obsmode='cos,fuv,g140l,c1280'
        self.tda['obsmode']=self.obsmode
        bp = S.ObsBandpass(self.obsmode)
        obs = S.Observation(S.BlackBody(5500), bp)        
