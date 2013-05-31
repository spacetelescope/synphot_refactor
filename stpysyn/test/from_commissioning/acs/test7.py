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


class Test772(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C772_%s.fits"
        cls.setup2()

class Test773(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C773_%s.fits"
        cls.setup2()

class Test774(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C774_%s.fits"
        cls.setup2()

class Test775(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C775_%s.fits"
        cls.setup2()

class Test776(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C776_%s.fits"
        cls.setup2()

class Test777(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C777_%s.fits"
        cls.setup2()

class Test778(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C778_%s.fits"
        cls.setup2()

class Test779(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C779_%s.fits"
        cls.setup2()

class Test780(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C780_%s.fits"
        cls.setup2()

class Test781(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C781_%s.fits"
        cls.setup2()

class Test782(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C782_%s.fits"
        cls.setup2()

class Test783(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C783_%s.fits"
        cls.setup2()

class Test784(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C784_%s.fits"
        cls.setup2()

class Test785(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C785_%s.fits"
        cls.setup2()

class Test786(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C786_%s.fits"
        cls.setup2()

class Test787(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C787_%s.fits"
        cls.setup2()

class Test788(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C788_%s.fits"
        cls.setup2()

class Test789(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C789_%s.fits"
        cls.setup2()

class Test790(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C790_%s.fits"
        cls.setup2()

