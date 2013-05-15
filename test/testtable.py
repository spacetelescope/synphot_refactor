"""Test table format errors. Usually in real life these occur
in file access, but many of them apply to ArraySpectrum objects
as well & can be tested that way.
"""

from pysynphot import exceptions, spectrum

import os
import unittest
import random
import numpy as np

class WaveProblems(unittest.TestCase):
    def setUp(self):
        self.wv=np.array([10, 20, 20, 30, 50, 100])
        self.fx=self.wv

    def testraise(self):
        self.assertRaises(exceptions.DuplicateWavelength,
                          spectrum.ArraySourceSpectrum,
                          self.wv, self.fx)

    def testpass(self):
        self.wv=np.array([10, 20, 30, 40, 50, 100])
        sp=spectrum.ArraySourceSpectrum(self.wv, self.fx)

    def testrows(self):
        try:
            sp=spectrum.ArraySourceSpectrum(self.wv, self.fx)
        except exceptions.DuplicateWavelength, e:
            self.assertEqual(e.rows, 1)

    def testneg(self):
        self.wv[0]=0
        self.assertRaises(exceptions.ZeroWavelength,
                          spectrum.ArraySourceSpectrum,
                          self.wv, self.fx)

    def testsort(self):
        random.shuffle(self.wv)
        self.assertRaises(exceptions.UnsortedWavelength,
                          spectrum.ArraySourceSpectrum,
                          self.wv, self.fx)



class TestFile(unittest.TestCase):
    def setUp(self):
        #Write an ascii file to test the reading of
        self.wv=np.array([10, 20, 'grackle', 30, 50, 100])
        self.fx=self.wv

        self.fname = os.path.abspath('grackle.dat')
        out=open(self.fname,'w')
        for w,f in zip(self.wv, self.fx):
            out.write("%s  %s\n"%(w,f))
        out.close()

    def tearDown(self):
        try:
            os.unlink(self.fname)
        except Exception, e:
            pass #ok, not there

    def testraises(self):
        self.assertRaises(exceptions.BadRow,
                          spectrum.FileSourceSpectrum,
                          self.fname)

    def testrow(self):
        try:
            sp=spectrum.FileSourceSpectrum(self.fname)
        except exceptions.BadRow, e:
            self.assertEqual(e.rows, 3)
