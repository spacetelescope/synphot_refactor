import os
import re
import unittest

#Code under test
from pysynphot.locations import irafconvert


class VarString(unittest.TestCase):
    def setUp(self):
        self.old_cdbs = os.environ['PYSYN_CDBS']
        os.environ['PYSYN_CDBS'] = os.path.abspath(os.path.dirname(__file__))
        self.fstring = '$PYSYN_CDBS/etc/background/Zodi.fits'
        self.ref = os.path.join(os.environ['PYSYN_CDBS'],
                                'etc/background/Zodi.fits')
        self.tda=dict(pysyn_cdbs = os.path.dirname(__file__),
                      sep = os.path.sep,
                      fstring=self.fstring,
                      ref=self.ref)

    def tearDown(self):
        os.environ['PYSYN_CDBS'] = self.old_cdbs

    def test1(self):
        ans = irafconvert(self.fstring)

        ans = os.path.normpath(ans)
        ref = os.path.normpath(self.ref)

        ans = os.path.normcase(ans)
        ref = os.path.normcase(ref)

        self.tra=dict(ans=ans, ref=ref)
        self.assertEqual(ref, ans)
