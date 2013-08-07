import unittest
from nose.exc import SkipTest
import pysynphot.spparser as parser
from pysynphot.pysynexcept import DisjointError, OverlapError

def test_double_slash():
    sp = parser.parse_spec("spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)")
    assert True

def test_pound():
    sp = parser.parse_spec("rn(unit(1.,flam),band(acs,wfc1,fr388n#3881.0),10.000000,abmag)")
    assert True

def test_x_decimal():
    raise SkipTest('does not work')
    sp = parser.parse_spec("rn(unit(1.,flam),band(stis,ccd,g430m,c4451,52X0.2),10.000000,abmag)")
    assert True

def test_50CCD():
    raise SkipTest('does not work')
    sp = parser.parse_spec("rn(unit(1.,flam),band(stis,ccd,mirror,50CCD),10.000000,abmag)")
    assert True

class TestParsing(unittest.TestCase):
    def setUp(self):
        self.disjoint_str = "rn($PYSYN_CDBS/etc/source/qso_fos_001.dat,band(johnson,v),15,abmag)"
        self.partial_str = "rn($PYSYN_CDBS/etc/source/qso_fos_001.dat,band(johnson,u),15,abmag)"

    def test_disjoint(self):
        self.assertRaises(DisjointError,
                          parser.parse_spec,
                          self.disjoint_str
                          )

    def test_partial(self):
        #This should work with a warning
        sp = parser.parse_spec(self.partial_str)
        assert 'force_renorm' in sp.warnings
