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


class Test722(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C722_%s.fits"
        cls.setup2()

class Test723(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C723_%s.fits"
        cls.setup2()

class Test724(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C724_%s.fits"
        cls.setup2()

class Test725(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C725_%s.fits"
        cls.setup2()

class Test726(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C726_%s.fits"
        cls.setup2()

class Test727(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C727_%s.fits"
        cls.setup2()

class Test728(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C728_%s.fits"
        cls.setup2()

class Test729(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C729_%s.fits"
        cls.setup2()

class Test730(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C730_%s.fits"
        cls.setup2()

class Test731(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C731_%s.fits"
        cls.setup2()

class Test732(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C732_%s.fits"
        cls.setup2()

class Test733(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C733_%s.fits"
        cls.setup2()

class Test734(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C734_%s.fits"
        cls.setup2()

class Test735(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C735_%s.fits"
        cls.setup2()

class Test736(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        cls.fname="C736_%s.fits"
        cls.setup2()

class Test737(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C737_%s.fits"
        cls.setup2()

class Test738(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C738_%s.fits"
        cls.setup2()

class Test739(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C739_%s.fits"
        cls.setup2()

class Test740(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C740_%s.fits"
        cls.setup2()

class Test741(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C741_%s.fits"
        cls.setup2()

class Test742(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C742_%s.fits"
        cls.setup2()

class Test743(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C743_%s.fits"
        cls.setup2()

class Test744(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C744_%s.fits"
        cls.setup2()

class Test745(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C745_%s.fits"
        cls.setup2()

class Test746(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C746_%s.fits"
        cls.setup2()

class Test747(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C747_%s.fits"
        cls.setup2()

class Test748(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C748_%s.fits"
        cls.setup2()

class Test749(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C749_%s.fits"
        cls.setup2()

class Test750(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C750_%s.fits"
        cls.setup2()

class Test751(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C751_%s.fits"
        cls.setup2()

class Test752(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C752_%s.fits"
        cls.setup2()

class Test753(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C753_%s.fits"
        cls.setup2()

class Test754(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C754_%s.fits"
        cls.setup2()

class Test755(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C755_%s.fits"
        cls.setup2()

class Test756(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C756_%s.fits"
        cls.setup2()

class Test757(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C757_%s.fits"
        cls.setup2()

class Test758(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C758_%s.fits"
        cls.setup2()

class Test759(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C759_%s.fits"
        cls.setup2()

class Test760(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C760_%s.fits"
        cls.setup2()

class Test761(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C761_%s.fits"
        cls.setup2()

class Test762(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C762_%s.fits"
        cls.setup2()

class Test763(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C763_%s.fits"
        cls.setup2()

class Test764(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C764_%s.fits"
        cls.setup2()

class Test765(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C765_%s.fits"
        cls.setup2()

class Test766(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C766_%s.fits"
        cls.setup2()

class Test767(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C767_%s.fits"
        cls.setup2()

class Test768(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C768_%s.fits"
        cls.setup2()

class Test769(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C769_%s.fits"
        cls.setup2()

class Test770(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C770_%s.fits"
        cls.setup2()

class Test771(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C771_%s.fits"
        cls.setup2()

