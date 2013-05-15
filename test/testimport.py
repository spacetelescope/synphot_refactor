from __future__ import division
import os
import sys
import warnings
import unittest

class ticket136(unittest.TestCase):
    def setUp(self):
        self.cdbs=os.environ.get('PYSYN_CDBS','/grp/hst/cdbs/')
        del os.environ['PYSYN_CDBS']

    def tearDown(self):
        os.environ['PYSYN_CDBS']=self.cdbs
        warnings.resetwarnings()

    def testWarning(self):
        #Note this test has to come alphabetically before the one
        #that results in a successful import...!
        warnings.simplefilter("error", UserWarning)
        if 'pysynphot.locations' in sys.modules:
            func = reload
            mod = sys.modules['pysynphot.locations']
        else:
            func = __import__
            mod = 'pysynphot.locations'
        self.assertRaises(UserWarning, func, mod)

    def testimport(self):
        import pysynphot as S
        self.assert_(True)


