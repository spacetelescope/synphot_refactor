import os
import sys

try:
    # TODO: If we made the tests dir a package this could be avoided by using
    # package-relative imports
    import conv_base
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    os.pardir)))
    import conv_base


class Test1251(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        cls.fname="C1251_%s.fits"
        cls.setup2()

class Test1252(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        cls.fname="C1252_%s.fits"
        cls.setup2()

class Test1253(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        cls.fname="C1253_%s.fits"
        cls.setup2()

class Test1254(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        cls.fname="C1254_%s.fits"
        cls.setup2()

class Test1255(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1255_%s.fits"
        cls.setup2()

class Test1256(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1256_%s.fits"
        cls.setup2()

class Test1257(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1257_%s.fits"
        cls.setup2()

class Test1258(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1258_%s.fits"
        cls.setup2()

class Test1259(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x01"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1259_%s.fits"
        cls.setup2()

class Test1260(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x2"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1260_%s.fits"
        cls.setup2()

