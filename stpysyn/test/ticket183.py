from __future__ import division

import unittest

#Code under test
from pysynphot.obsbandpass import ObsBandpass


class TestDiscoveryCase(unittest.TestCase):
    def setUp(self):
        self.bp = ObsBandpass('acs,sbc,f150lp')

    def testraise(self):
        self.assertRaises(NotImplementedError,
                          self.bp.thermback)

        
