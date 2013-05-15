from __future__ import division
"""Test that exceptions really are raised when they should be."""
import unittest,sys,os
import testutil
from pysynphot import observationmode, locations, refs
import pysynphot as S

class TMCmismatch(unittest.TestCase):
    """Can arise with mismatched graph & component tables"""

    def setUp(self):
        tmcname = os.path.join('mtab','r1j2146sm_tmc.fits')
        self.oldrefs = refs.getref()
        refs.COMPTABLE = locations._refTable(tmcname)
        tmgname = os.path.join('mtab','rbg2236im_tmg.fits')
        refs.GRAPHTABLE = locations._refTable(tmgname)
        self.omstring='acs,hrc,f555w,mjd#54000'

    def tearDown(self):
        refs.COMPTABLE = self.oldrefs['comptable']
        refs.GRAPHTABLE = self.oldrefs['graphtable']

    def test1(self):
        "compname not found in tmc"
        self.assertRaises(IndexError, observationmode.ObservationMode,
                          self.omstring)

class RenormNonsense(unittest.TestCase):
    """Can arise with zero, negative, or nan spectra"""
    def setUp(self):
        self.sp=S.FlatSpectrum(1)
        self.bp=S.ObsBandpass('johnson,v')

    def testneg(self):
        sp2=self.sp*(-10)
        self.assertRaises(ValueError,
                          sp2.renorm,
                          15, 'vegamag', self.bp)




if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)

