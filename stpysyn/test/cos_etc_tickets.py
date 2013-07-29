from __future__ import division
import os
import sys

import numpy as N

from stpysyn.test import testutil
import pysynphot as S
from pysynphot import pysynexcept


class EnforceWave(testutil.FPTestCase):
    """Ticket #85: enforce monotonic ascending wavesets
    for ArraySourceSpectrum objects.
    **Already moved to cos_etc_test.**"""
    def setUp(self):
        self.gendata()
        #make some bad wavesets here
        self.constructor=S.ArraySpectrum
        self.args=[self.wave,self.flux]
        #first do unit test: test the Integrator method explicitly
        #then test for ascii & fits file spectra (ETC case)
        # then test for file bandpasses.. then other cases.

    def gendata(self):
        self.zeros=N.arange(10)
        self.neg=N.arange(-3,7)
        self.valid=N.arange(1000,1010)
        self.descending=self.valid[::-1]
        self.mixed=N.array([3,8,2,12,15,18,11,10,20,18])
        self.wave=self.zeros
        self.flux=N.ones(len(self.wave))

        self.argdict={'zero':(self.zeros,self.flux),
                      'neg':(self.neg,self.flux),
                      'valid':(self.valid,self.flux),
                      'desc':(self.descending,self.flux),
                      'mixed':(self.mixed,self.flux)}
    def test(self):
        self.args=self.argdict['valid']
        sp=self.constructor(*self.args)
        self.assertEqualNumpy(sp.wave,self.valid)


    def testzero(self):
        self.args=self.argdict['zero']
        self.assertRaises(pysynexcept.ZeroWavelength,
                          self.constructor,
                          *self.args)

    def testneg(self):
        self.args=self.argdict['neg']
        self.assertRaises(pysynexcept.ZeroWavelength,
                          self.constructor,
                          *self.args)

    def testmixed(self):
        self.args=self.argdict['mixed']
        self.assertRaises(pysynexcept.UnsortedWavelength,
                          self.constructor,
                          *self.args)



class EnforceWaveFile(EnforceWave):
    """Ticket *85: enforce monotonic ascending wavesets
        for FileSourceSpectrum objects
        **already moved to cos_etc_test"""
    def setUp(self):
        self.gendata()
        self.writedata()
        self.constructor=S.FileSpectrum
        self.args=(self.fname,)

    def writeone(self, fname, wave):
        f=open(fname,'w')
        for k in range(len(wave)):
            f.write("%f    %f\n"%(wave[k],self.flux[k]))
        f.close()

    def writedata(self):
        self.cases={'valid':'valid.txt',
                    'neg':'neg.txt',
                    'zero':'zero.txt',
                    'mixed':'mixed.txt',
                    'desc':'desc.txt'}
        self.waves={'valid':self.valid,
                    'neg':self.neg,
                   'zero':self.zeros,
                   'mixed':self.mixed,
                   'desc':self.descending}
        self.fname=self.cases['zero']
        self.argdict={}
        for k in self.cases:
            self.writeone(self.cases[k], self.waves[k])
            self.argdict[k]=(self.cases[k],)
    def tearDown(self):
        for k in self.cases:
            os.remove(self.cases[k])



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)
