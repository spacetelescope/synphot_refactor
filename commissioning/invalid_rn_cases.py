import unittest
from pysynphot import etc

class C1(unittest.TestCase):
    def setUp(self):
        self.sp="rn(icat(ck04models,41000,4.5,0),band(ACS,HRC,G800L,F220W),4.5,vegamag)"

    def testinvalid(self):
        self.assertRaises(ValueError,
                           etc.parse_spec,
                           self.sp)

class C2(C1):
    def setUp(self):
        self.sp="rn(icat(ck04models,41000,4.5,0),band(ACS,HRC,G800L,F250W),4.5,vegamag)"

class C3(C1):
    def setUp(self):
        self.sp="rn(icat(ck04models,41000,4.5,0),band(ACS,HRC,G800L,F330W),4.5,vegamag)"
        
