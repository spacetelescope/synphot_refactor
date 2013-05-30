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


class Test991(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C991_%s.fits"
        cls.setup2()

class Test992(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C992_%s.fits"
        cls.setup2()

class Test993(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C993_%s.fits"
        cls.setup2()

class Test994(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C994_%s.fits"
        cls.setup2()

class Test995(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C995_%s.fits"
        cls.setup2()

class Test996(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C996_%s.fits"
        cls.setup2()

class Test997(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd153_mod_004.fits)"
        cls.fname="C997_%s.fits"
        cls.setup2()

class Test998(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C998_%s.fits"
        cls.setup2()

class Test999(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C999_%s.fits"
        cls.setup2()

class Test1000(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1000_%s.fits"
        cls.setup2()

class Test1001(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1001_%s.fits"
        cls.setup2()

class Test1002(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1002_%s.fits"
        cls.setup2()

class Test1003(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1003_%s.fits"
        cls.setup2()

class Test1004(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1004_%s.fits"
        cls.setup2()

class Test1005(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1005_%s.fits"
        cls.setup2()

class Test1006(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1006_%s.fits"
        cls.setup2()

class Test1007(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1007_%s.fits"
        cls.setup2()

class Test1008(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1008_%s.fits"
        cls.setup2()

class Test1009(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1009_%s.fits"
        cls.setup2()

class Test1010(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1010_%s.fits"
        cls.setup2()

class Test1011(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1011_%s.fits"
        cls.setup2()

class Test1012(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1012_%s.fits"
        cls.setup2()

class Test1013(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1013_%s.fits"
        cls.setup2()

class Test1014(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1014_%s.fits"
        cls.setup2()

class Test1015(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1015_%s.fits"
        cls.setup2()

class Test1016(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1016_%s.fits"
        cls.setup2()

class Test1017(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1017_%s.fits"
        cls.setup2()

class Test1018(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1018_%s.fits"
        cls.setup2()

class Test1019(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1019_%s.fits"
        cls.setup2()

class Test1020(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1020_%s.fits"
        cls.setup2()

class Test1021(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1021_%s.fits"
        cls.setup2()

class Test1022(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1022_%s.fits"
        cls.setup2()

class Test1023(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1023_%s.fits"
        cls.setup2()

class Test1024(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1024_%s.fits"
        cls.setup2()

class Test1025(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1025_%s.fits"
        cls.setup2()

class Test1026(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1026_%s.fits"
        cls.setup2()

class Test1027(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1027_%s.fits"
        cls.setup2()

class Test1028(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1028_%s.fits"
        cls.setup2()

class Test1029(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1029_%s.fits"
        cls.setup2()

class Test1030(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1030_%s.fits"
        cls.setup2()

class Test1031(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1031_%s.fits"
        cls.setup2()

class Test1032(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1032_%s.fits"
        cls.setup2()

class Test1033(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1033_%s.fits"
        cls.setup2()

class Test1034(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1034_%s.fits"
        cls.setup2()

class Test1035(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1035_%s.fits"
        cls.setup2()

class Test1036(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1036_%s.fits"
        cls.setup2()

class Test1037(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1037_%s.fits"
        cls.setup2()

class Test1038(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1038_%s.fits"
        cls.setup2()

class Test1039(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1039_%s.fits"
        cls.setup2()

class Test1040(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_9.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1040_%s.fits"
        cls.setup2()

