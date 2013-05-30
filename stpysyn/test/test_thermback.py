import unittest

from pysynphot.observationmode import _ThermalObservationMode
from pysynphot.obsbandpass import ObsBandpass

class TestException(unittest.TestCase):
    #Making a ThermalObservationMode for an obsmode that
    #has no support for thermal calculations should raise
    #an exception.
    def setUp(self):
        self.ostring='acs,hrc,f555w'
        self.tda = dict(obsmode=self.ostring)

    def test1(self):
        self.assertRaises(NotImplementedError,
                          _ThermalObservationMode,
                          self.ostring)

class TestThermal(unittest.TestCase):
    def setUp(self):
        self.ostring='nicmos,3,f222m'
        self.tda = dict(obsmode=self.ostring)
    

    def test1(self):
        try:
            self.omode = _ThermalObservationMode(self.ostring)
        except Exception, e:
            self.fail(str(e))


class TestThermback(unittest.TestCase):
    def setUp(self):
        self.ostring='nicmos,3,f222m'
        self.tda = dict(obsmode=self.ostring)
        self.bp=ObsBandpass(self.ostring)
        
        
    def testruns(self):
        try:
            ans=self.bp.thermback()
        except Exception, e:
            self.fail(str(type(e))+str(e))

class TestThermbackException(unittest.TestCase):
    def setUp(self):
        self.ostring='acs,hrc,f555w'
        self.tda = dict(obsmode=self.ostring)
        self.bp=ObsBandpass(self.ostring)

    def testexc(self):
        self.assertRaises(NotImplementedError,
                          self.bp.thermback)
