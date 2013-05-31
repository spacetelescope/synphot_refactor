import unittest
import os
from pysynphot.locations import irafconvert
from pysynphot.spparser import parse_spec

class Ticket52(unittest.TestCase):

    def setUp(self):
        self.ref = os.path.join(os.environ['PYSYN_CDBS'],
                                'calspec',
                                'gd50_004.fits')

    def testiraf(self):
        fname = 'crcalspec$gd50_004.fits'
        tst = irafconvert(fname)
        self.assert_(self.ref == tst, msg="Expected %s, got %s"%(self.ref,tst))

    def testshell(self):
        fname = '$PYSYN_CDBS/calspec/gd50_004.fits'
        tst = irafconvert(fname)
        self.assert_(self.ref == tst, msg="Expected %s, got %s"%(self.ref,tst))

    def testplain(self):
        fname = 'gd50_004.fits'
        tst = irafconvert(fname)
        self.assert_(fname == tst,  msg="Expected %s, got %s"%(fname,tst))

    def testparse_iraf(self):
        sp = parse_spec('crcalspec$gd50_004.fits')
        self.assert_(self.ref == str(sp))

    def testparse_shell(self):
        sp = parse_spec('$PYSYN_CDBS/calspec/gd50_004.fits')
        self.assert_(self.ref == str(sp))
