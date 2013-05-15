from __future__ import division
import os
import testutil
from pysynphot import locations
from pysynphot.observation import Observation
from pysynphot import refs  # to freeze comptable


cmptb_name = os.path.join('mtab', 'r1j2146sm_tmc.fits')


class ETCTestCase(testutil.FPTestCase):
    """Base class for cases generated from the ETC test listings"""

    def setUp(self):
        self.old_comptable = refs.COMPTABLE
        refs.COMPTABLE = locations._refTable(cmptb_name)
        self.oldpath = os.path.abspath(os.curdir)
        if os.path.isdir(os.path.join(locations.specdir, 'generic')):
            os.chdir(os.path.join(locations.specdir, 'generic'))
        else:
            os.chdir(locations.specdir)
        self.accuracy = 0.00109
        self.setparms()
        if self.sp is not None:  # Skip the base class!!
            self.obs = Observation(self.sp, self.bp)

    def setparms(self):
        self.sp = None
        self.bp = None
        self.ref_rate = None
        self.file = None
        self.cmd = None

    def tearDown(self):
        os.chdir(self.oldpath)
        refs.COMPTABLE = self.old_comptable

    def testrate(self):
        if self.sp is not None:
            self.assertApproxFP(self.obs.countrate(), self.ref_rate,
                                accuracy=self.accuracy)

#    def testfile(self):
#        """Need to figure out where to keep reference files"""
#        pass


