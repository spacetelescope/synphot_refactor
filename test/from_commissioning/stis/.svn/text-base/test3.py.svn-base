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


class Test1201(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el2471a.fits"
        cls.fname="C1201_%s.fits"
        cls.setup2()

class Test1202(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C1202_%s.fits"
        cls.setup2()

class Test1203(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C1203_%s.fits"
        cls.setup2()

class Test1204(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C1204_%s.fits"
        cls.setup2()

class Test1205(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C1205_%s.fits"
        cls.setup2()

class Test1206(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C1206_%s.fits"
        cls.setup2()

class Test1207(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C1207_%s.fits"
        cls.setup2()

class Test1208(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C1208_%s.fits"
        cls.setup2()

class Test1209(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C1209_%s.fits"
        cls.setup2()

class Test1210(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C1210_%s.fits"
        cls.setup2()

class Test1211(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C1211_%s.fits"
        cls.setup2()

class Test1212(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C1212_%s.fits"
        cls.setup2()

class Test1213(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C1213_%s.fits"
        cls.setup2()

class Test1214(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1214_%s.fits"
        cls.setup2()

class Test1215(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1215_%s.fits"
        cls.setup2()

class Test1216(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1216_%s.fits"
        cls.setup2()

class Test1217(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1217_%s.fits"
        cls.setup2()

class Test1218(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        cls.fname="C1218_%s.fits"
        cls.setup2()

class Test1219(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        cls.fname="C1219_%s.fits"
        cls.setup2()

class Test1220(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1220_%s.fits"
        cls.setup2()

class Test1221(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1221_%s.fits"
        cls.setup2()

class Test1222(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1222_%s.fits"
        cls.setup2()

class Test1223(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        cls.fname="C1223_%s.fits"
        cls.setup2()

class Test1224(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1224_%s.fits"
        cls.setup2()

class Test1225(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1225_%s.fits"
        cls.setup2()

class Test1226(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1226_%s.fits"
        cls.setup2()

class Test1227(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1227_%s.fits"
        cls.setup2()

class Test1228(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1228_%s.fits"
        cls.setup2()

class Test1229(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1229_%s.fits"
        cls.setup2()

class Test1230(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1230_%s.fits"
        cls.setup2()

class Test1231(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1231_%s.fits"
        cls.setup2()

class Test1232(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1232_%s.fits"
        cls.setup2()

class Test1233(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1233_%s.fits"
        cls.setup2()

class Test1234(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1234_%s.fits"
        cls.setup2()

class Test1235(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1235_%s.fits"
        cls.setup2()

class Test1236(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1236_%s.fits"
        cls.setup2()

class Test1237(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1237_%s.fits"
        cls.setup2()

class Test1238(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1238_%s.fits"
        cls.setup2()

class Test1239(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1239_%s.fits"
        cls.setup2()

class Test1240(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1240_%s.fits"
        cls.setup2()

class Test1241(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1241_%s.fits"
        cls.setup2()

class Test1242(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1242_%s.fits"
        cls.setup2()

class Test1243(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1243_%s.fits"
        cls.setup2()

class Test1244(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1244_%s.fits"
        cls.setup2()

class Test1245(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1245_%s.fits"
        cls.setup2()

class Test1246(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1246_%s.fits"
        cls.setup2()

class Test1247(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1247_%s.fits"
        cls.setup2()

class Test1248(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1248_%s.fits"
        cls.setup2()

class Test1249(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1249_%s.fits"
        cls.setup2()

class Test1250(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        cls.fname="C1250_%s.fits"
        cls.setup2()

