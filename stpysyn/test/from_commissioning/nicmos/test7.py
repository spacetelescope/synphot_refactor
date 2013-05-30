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


class Test1091(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1091_%s.fits"
        cls.setup2()

class Test1092(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1092_%s.fits"
        cls.setup2()

class Test1093(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1093_%s.fits"
        cls.setup2()

class Test1094(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1094_%s.fits"
        cls.setup2()

class Test1095(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1095_%s.fits"
        cls.setup2()

class Test1096(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1096_%s.fits"
        cls.setup2()

class Test1097(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1097_%s.fits"
        cls.setup2()

class Test1098(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1098_%s.fits"
        cls.setup2()

class Test1099(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1099_%s.fits"
        cls.setup2()

class Test1100(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1100_%s.fits"
        cls.setup2()

