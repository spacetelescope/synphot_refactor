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


class Test1041(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1041_%s.fits"
        cls.setup2()

class Test1042(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1042_%s.fits"
        cls.setup2()

class Test1043(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1043_%s.fits"
        cls.setup2()

class Test1044(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1044_%s.fits"
        cls.setup2()

class Test1045(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1045_%s.fits"
        cls.setup2()

class Test1046(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1046_%s.fits"
        cls.setup2()

class Test1047(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1047_%s.fits"
        cls.setup2()

class Test1048(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1048_%s.fits"
        cls.setup2()

class Test1049(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1049_%s.fits"
        cls.setup2()

class Test1050(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1050_%s.fits"
        cls.setup2()

class Test1051(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1051_%s.fits"
        cls.setup2()

class Test1052(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1052_%s.fits"
        cls.setup2()

class Test1053(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1053_%s.fits"
        cls.setup2()

class Test1054(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1054_%s.fits"
        cls.setup2()

class Test1055(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1055_%s.fits"
        cls.setup2()

class Test1056(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1056_%s.fits"
        cls.setup2()

class Test1057(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1057_%s.fits"
        cls.setup2()

class Test1058(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1058_%s.fits"
        cls.setup2()

class Test1059(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1059_%s.fits"
        cls.setup2()

class Test1060(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1060_%s.fits"
        cls.setup2()

class Test1061(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1061_%s.fits"
        cls.setup2()

class Test1062(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1062_%s.fits"
        cls.setup2()

class Test1063(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1063_%s.fits"
        cls.setup2()

class Test1064(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        cls.fname="C1064_%s.fits"
        cls.setup2()

class Test1065(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        cls.fname="C1065_%s.fits"
        cls.setup2()

class Test1066(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        cls.fname="C1066_%s.fits"
        cls.setup2()

class Test1067(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        cls.fname="C1067_%s.fits"
        cls.setup2()

class Test1068(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1068_%s.fits"
        cls.setup2()

class Test1069(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1069_%s.fits"
        cls.setup2()

class Test1070(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1070_%s.fits"
        cls.setup2()

class Test1071(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1071_%s.fits"
        cls.setup2()

class Test1072(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1072_%s.fits"
        cls.setup2()

class Test1073(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1073_%s.fits"
        cls.setup2()

class Test1074(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1074_%s.fits"
        cls.setup2()

class Test1075(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1075_%s.fits"
        cls.setup2()

class Test1076(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1076_%s.fits"
        cls.setup2()

class Test1077(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1077_%s.fits"
        cls.setup2()

class Test1078(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1078_%s.fits"
        cls.setup2()

class Test1079(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1079_%s.fits"
        cls.setup2()

class Test1080(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1080_%s.fits"
        cls.setup2()

class Test1081(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1081_%s.fits"
        cls.setup2()

class Test1082(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1082_%s.fits"
        cls.setup2()

class Test1083(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1083_%s.fits"
        cls.setup2()

class Test1084(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1084_%s.fits"
        cls.setup2()

class Test1085(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1085_%s.fits"
        cls.setup2()

class Test1086(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1086_%s.fits"
        cls.setup2()

class Test1087(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1087_%s.fits"
        cls.setup2()

class Test1088(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1088_%s.fits"
        cls.setup2()

class Test1089(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1089_%s.fits"
        cls.setup2()

class Test1090(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1090_%s.fits"
        cls.setup2()

