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


class Test1151(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1151_%s.fits"
        cls.setup2()

class Test1152(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1152_%s.fits"
        cls.setup2()

class Test1153(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1153_%s.fits"
        cls.setup2()

class Test1154(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1154_%s.fits"
        cls.setup2()

class Test1155(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1155_%s.fits"
        cls.setup2()

class Test1156(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1156_%s.fits"
        cls.setup2()

class Test1157(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1157_%s.fits"
        cls.setup2()

class Test1158(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1158_%s.fits"
        cls.setup2()

class Test1159(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1159_%s.fits"
        cls.setup2()

class Test1160(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1160_%s.fits"
        cls.setup2()

class Test1161(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1161_%s.fits"
        cls.setup2()

class Test1162(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1162_%s.fits"
        cls.setup2()

class Test1163(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1163_%s.fits"
        cls.setup2()

class Test1164(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        cls.fname="C1164_%s.fits"
        cls.setup2()

class Test1165(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        cls.fname="C1165_%s.fits"
        cls.setup2()

class Test1166(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        cls.fname="C1166_%s.fits"
        cls.setup2()

class Test1167(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        cls.fname="C1167_%s.fits"
        cls.setup2()

class Test1168(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        cls.fname="C1168_%s.fits"
        cls.setup2()

class Test1169(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1169_%s.fits"
        cls.setup2()

class Test1170(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1170_%s.fits"
        cls.setup2()

class Test1171(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1171_%s.fits"
        cls.setup2()

class Test1172(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1172_%s.fits"
        cls.setup2()

class Test1173(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1173_%s.fits"
        cls.setup2()

class Test1174(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1174_%s.fits"
        cls.setup2()

class Test1175(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1175_%s.fits"
        cls.setup2()

class Test1176(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1176_%s.fits"
        cls.setup2()

class Test1177(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1177_%s.fits"
        cls.setup2()

class Test1178(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1178_%s.fits"
        cls.setup2()

class Test1179(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1179_%s.fits"
        cls.setup2()

class Test1180(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1180_%s.fits"
        cls.setup2()

class Test1181(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1181_%s.fits"
        cls.setup2()

class Test1182(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1182_%s.fits"
        cls.setup2()

class Test1183(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1183_%s.fits"
        cls.setup2()

class Test1184(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1184_%s.fits"
        cls.setup2()

class Test1185(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x01"
        cls.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        cls.fname="C1185_%s.fits"
        cls.setup2()

class Test1186(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        cls.fname="C1186_%s.fits"
        cls.setup2()

class Test1187(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        cls.fname="C1187_%s.fits"
        cls.setup2()

class Test1188(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        cls.fname="C1188_%s.fits"
        cls.setup2()

class Test1189(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        cls.fname="C1189_%s.fits"
        cls.setup2()

class Test1190(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        cls.fname="C1190_%s.fits"
        cls.setup2()

class Test1191(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1191_%s.fits"
        cls.setup2()

class Test1192(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1192_%s.fits"
        cls.setup2()

class Test1193(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1193_%s.fits"
        cls.setup2()

class Test1194(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1194_%s.fits"
        cls.setup2()

class Test1195(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C1195_%s.fits"
        cls.setup2()

class Test1196(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C1196_%s.fits"
        cls.setup2()

class Test1197(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C1197_%s.fits"
        cls.setup2()

class Test1198(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1215a.fits"
        cls.fname="C1198_%s.fits"
        cls.setup2()

class Test1199(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1302a.fits"
        cls.fname="C1199_%s.fits"
        cls.setup2()

class Test1200(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1356a.fits"
        cls.fname="C1200_%s.fits"
        cls.setup2()

