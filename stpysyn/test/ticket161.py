from __future__ import division

import numpy as N

from stpysyn.test import testutil
import pysynphot as S


class ErrcolCase(testutil.FPTestCase):
    def setUp(self):
        self.obsmode='stis,ccd,50ccd,mjd#55000'

    def testfix(self):
        obs=S.ObsBandpass(self.obsmode)
        #It passes if the above statement does not raise an exception,
        #but let's make sure it got some values
        tst=N.all(obs.throughput == 0)
        self.failIf(tst)
