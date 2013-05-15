import unittest

from pysynphot.units import Angstrom

# Code under test
from pysynphot.spectrum import Box

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.bp = Box(5000,100)

    def testinside(self):
        ref = 1.0
        tst = self.bp.sample(5000)
        self.assertEqual(ref,tst,msg="expected %g, got %g"%(ref,tst))

    def testoutside(self):
        ref = 0.0
        tst = self.bp.sample(4000)
        self.assertEqual(ref,tst)

    def testbound(self):
        ref = 0.0
        tst = self.bp.sample(4949)
        self.assertEqual(ref,tst)

    def testunits(self):
        self.assert_(isinstance(self.bp.waveunits, Angstrom))

class Ticket114(unittest.TestCase):
    def setUp(self):
        self.bp = Box(500,10,waveunits='nm')

    def testunits(self):
        self.assertEquals(str(self.bp.waveunits), 'nm')

    def testinside(self):
        ref = 1.0
        tst = self.bp.sample(500)
        self.assertEquals(ref,tst)
        

        
