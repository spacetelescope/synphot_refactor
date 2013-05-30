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


class Test1101(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd"
        cls.spectrum="rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        cls.fname="C1101_%s.fits"
        cls.setup2()

class Test1102(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        cls.fname="C1102_%s.fits"
        cls.setup2()

class Test1103(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1103_%s.fits"
        cls.setup2()

class Test1104(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        cls.fname="C1104_%s.fits"
        cls.setup2()

class Test1105(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1105_%s.fits"
        cls.setup2()

class Test1106(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1106_%s.fits"
        cls.setup2()

class Test1107(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1107_%s.fits"
        cls.setup2()

class Test1108(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1108_%s.fits"
        cls.setup2()

class Test1109(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1109_%s.fits"
        cls.setup2()

class Test1110(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1110_%s.fits"
        cls.setup2()

class Test1111(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1111_%s.fits"
        cls.setup2()

class Test1112(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1112_%s.fits"
        cls.setup2()

class Test1113(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1113_%s.fits"
        cls.setup2()

class Test1114(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1114_%s.fits"
        cls.setup2()

class Test1115(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1115_%s.fits"
        cls.setup2()

class Test1116(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1116_%s.fits"
        cls.setup2()

class Test1117(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1117_%s.fits"
        cls.setup2()

class Test1118(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1118_%s.fits"
        cls.setup2()

class Test1119(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1119_%s.fits"
        cls.setup2()

class Test1120(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1120_%s.fits"
        cls.setup2()

class Test1121(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1121_%s.fits"
        cls.setup2()

class Test1122(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1122_%s.fits"
        cls.setup2()

class Test1123(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1123_%s.fits"
        cls.setup2()

class Test1124(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1124_%s.fits"
        cls.setup2()

class Test1125(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1125_%s.fits"
        cls.setup2()

class Test1126(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1126_%s.fits"
        cls.setup2()

class Test1127(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1127_%s.fits"
        cls.setup2()

class Test1128(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1128_%s.fits"
        cls.setup2()

class Test1129(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1129_%s.fits"
        cls.setup2()

class Test1130(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1130_%s.fits"
        cls.setup2()

class Test1131(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        cls.fname="C1131_%s.fits"
        cls.setup2()

class Test1132(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1132_%s.fits"
        cls.setup2()

class Test1133(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1133_%s.fits"
        cls.setup2()

class Test1134(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1134_%s.fits"
        cls.setup2()

class Test1135(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1135_%s.fits"
        cls.setup2()

class Test1136(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1136_%s.fits"
        cls.setup2()

class Test1137(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1137_%s.fits"
        cls.setup2()

class Test1138(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1138_%s.fits"
        cls.setup2()

class Test1139(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1139_%s.fits"
        cls.setup2()

class Test1140(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1140_%s.fits"
        cls.setup2()

class Test1141(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1141_%s.fits"
        cls.setup2()

class Test1142(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1142_%s.fits"
        cls.setup2()

class Test1143(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1143_%s.fits"
        cls.setup2()

class Test1144(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        cls.fname="C1144_%s.fits"
        cls.setup2()

class Test1145(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        cls.fname="C1145_%s.fits"
        cls.setup2()

class Test1146(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        cls.fname="C1146_%s.fits"
        cls.setup2()

class Test1147(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        cls.fname="C1147_%s.fits"
        cls.setup2()

class Test1148(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        cls.fname="C1148_%s.fits"
        cls.setup2()

class Test1149(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1149_%s.fits"
        cls.setup2()

class Test1150(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1150_%s.fits"
        cls.setup2()

