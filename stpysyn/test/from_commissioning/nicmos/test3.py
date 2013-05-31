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


class Test891(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C891_%s.fits"
        cls.setup2()

class Test892(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C892_%s.fits"
        cls.setup2()

class Test893(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C893_%s.fits"
        cls.setup2()

class Test894(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C894_%s.fits"
        cls.setup2()

class Test895(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C895_%s.fits"
        cls.setup2()

class Test896(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C896_%s.fits"
        cls.setup2()

class Test897(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C897_%s.fits"
        cls.setup2()

class Test898(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd153_mod_004.fits)"
        cls.fname="C898_%s.fits"
        cls.setup2()

class Test899(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C899_%s.fits"
        cls.setup2()

class Test900(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C900_%s.fits"
        cls.setup2()

class Test901(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C901_%s.fits"
        cls.setup2()

class Test902(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C902_%s.fits"
        cls.setup2()

class Test903(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C903_%s.fits"
        cls.setup2()

class Test904(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C904_%s.fits"
        cls.setup2()

class Test905(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C905_%s.fits"
        cls.setup2()

class Test906(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C906_%s.fits"
        cls.setup2()

class Test907(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C907_%s.fits"
        cls.setup2()

class Test908(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C908_%s.fits"
        cls.setup2()

class Test909(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C909_%s.fits"
        cls.setup2()

class Test910(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C910_%s.fits"
        cls.setup2()

class Test911(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C911_%s.fits"
        cls.setup2()

class Test912(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C912_%s.fits"
        cls.setup2()

class Test913(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C913_%s.fits"
        cls.setup2()

class Test914(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C914_%s.fits"
        cls.setup2()

class Test915(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C915_%s.fits"
        cls.setup2()

class Test916(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C916_%s.fits"
        cls.setup2()

class Test917(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C917_%s.fits"
        cls.setup2()

class Test918(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C918_%s.fits"
        cls.setup2()

class Test919(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C919_%s.fits"
        cls.setup2()

class Test920(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd153_mod_004.fits)"
        cls.fname="C920_%s.fits"
        cls.setup2()

class Test921(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C921_%s.fits"
        cls.setup2()

class Test922(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C922_%s.fits"
        cls.setup2()

class Test923(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C923_%s.fits"
        cls.setup2()

class Test924(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C924_%s.fits"
        cls.setup2()

class Test925(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C925_%s.fits"
        cls.setup2()

class Test926(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C926_%s.fits"
        cls.setup2()

class Test927(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd153_mod_004.fits)"
        cls.fname="C927_%s.fits"
        cls.setup2()

class Test928(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C928_%s.fits"
        cls.setup2()

class Test929(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C929_%s.fits"
        cls.setup2()

class Test930(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C930_%s.fits"
        cls.setup2()

class Test931(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C931_%s.fits"
        cls.setup2()

class Test932(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C932_%s.fits"
        cls.setup2()

class Test933(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C933_%s.fits"
        cls.setup2()

class Test934(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C934_%s.fits"
        cls.setup2()

class Test935(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C935_%s.fits"
        cls.setup2()

class Test936(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C936_%s.fits"
        cls.setup2()

class Test937(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C937_%s.fits"
        cls.setup2()

class Test938(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C938_%s.fits"
        cls.setup2()

class Test939(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C939_%s.fits"
        cls.setup2()

class Test940(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C940_%s.fits"
        cls.setup2()

