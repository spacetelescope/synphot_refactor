from __future__ import division
import os, sys
import math

import numpy as N
import pyfits
import testutil 
import pysynphot as S
from pysynphot import units, locations

## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()


class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
        self.sp = S.FileSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)

    def testsubtract(self):
        "ui_test.FileTestCase('testsub'): Subtract two spectra, #23"
        sp2=self.sp + self.sp
        sp3=sp2-self.sp
        self.assertEqualNumpy(sp3.flux,self.sp.flux)

    def tearDown(self):
        self.openfits.close()

class TicketXX(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.FlatSpectrum(1)
        self.z=2.5
        self.wavecheck=N.array([550])

                    
    def testfluxpt(self):
        tst=self.sp.redshift(self.z)
        tstpt=tst(self.wavecheck)[0]
        self.assert_(tst.flux.max() == tstpt,"tstpt=%f"%tstpt)

class FileSpecIRAF(testutil.FPTestCase):
    def setUp(self):
        self.opener = S.FileSpectrum
        self.fname='crcalspec$hz2_005.fits'
        self.ref=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                             'calspec',
                                             'hz2_005.fits'))
    def test1(self):
        self.tst = self.opener(self.fname)
        self.assertEqual(os.path.normpath(self.ref.name),
                         os.path.normpath(self.tst.name))

class FileSpecEnv(FileSpecIRAF):
    def setUp(self):
        self.opener = S.FileSpectrum
        self.fname='$PYSYN_CDBS/calspec/hz2_005.fits'
        self.ref=S.FileSpectrum(os.path.join(os.environ['PYSYN_CDBS'],
                                             'calspec',
                                             'hz2_005.fits'))

class FileBandIRAF(FileSpecIRAF):
    def setUp(self):
        self.opener = S.FileBandpass
        self.fname = 'crotacomp$hst_ota_007_syn.fits'
        self.ref = S.FileBandpass(os.path.join(os.environ['PYSYN_CDBS'],
                                               'comp','ota',
                                               'hst_ota_007_syn.fits'))

class FileBandEnv(FileSpecIRAF):
    def setUp(self):
        self.opener = S.FileBandpass
        self.fname = '$PYSYN_CDBS/comp/ota/hst_ota_007_syn.fits'
        self.ref = S.FileBandpass(os.path.join(os.environ['PYSYN_CDBS'],
                                               'comp','ota',
                                               'hst_ota_007_syn.fits'))
    
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)
