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


class Test572(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C572_%s.fits"
        cls.setup2()

class Test573(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C573_%s.fits"
        cls.setup2()

class Test574(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C574_%s.fits"
        cls.setup2()

class Test575(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C575_%s.fits"
        cls.setup2()

class Test576(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C576_%s.fits"
        cls.setup2()

class Test577(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C577_%s.fits"
        cls.setup2()

class Test578(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C578_%s.fits"
        cls.setup2()

class Test579(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C579_%s.fits"
        cls.setup2()

class Test580(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C580_%s.fits"
        cls.setup2()

class Test581(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C581_%s.fits"
        cls.setup2()

class Test582(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C582_%s.fits"
        cls.setup2()

class Test583(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C583_%s.fits"
        cls.setup2()

class Test584(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C584_%s.fits"
        cls.setup2()

class Test585(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C585_%s.fits"
        cls.setup2()

class Test586(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C586_%s.fits"
        cls.setup2()

class Test587(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C587_%s.fits"
        cls.setup2()

class Test588(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C588_%s.fits"
        cls.setup2()

class Test589(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C589_%s.fits"
        cls.setup2()

class Test590(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C590_%s.fits"
        cls.setup2()

class Test591(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C591_%s.fits"
        cls.setup2()

class Test592(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C592_%s.fits"
        cls.setup2()

class Test593(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C593_%s.fits"
        cls.setup2()

class Test594(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C594_%s.fits"
        cls.setup2()

class Test595(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C595_%s.fits"
        cls.setup2()

class Test596(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C596_%s.fits"
        cls.setup2()

class Test597(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C597_%s.fits"
        cls.setup2()

class Test598(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C598_%s.fits"
        cls.setup2()

class Test599(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C599_%s.fits"
        cls.setup2()

class Test600(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C600_%s.fits"
        cls.setup2()

class Test601(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C601_%s.fits"
        cls.setup2()

class Test602(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C602_%s.fits"
        cls.setup2()

class Test603(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C603_%s.fits"
        cls.setup2()

class Test604(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C604_%s.fits"
        cls.setup2()

class Test605(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C605_%s.fits"
        cls.setup2()

class Test606(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C606_%s.fits"
        cls.setup2()

class Test607(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C607_%s.fits"
        cls.setup2()

class Test608(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C608_%s.fits"
        cls.setup2()

class Test609(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C609_%s.fits"
        cls.setup2()

class Test610(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        cls.fname="C610_%s.fits"
        cls.setup2()

class Test611(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C611_%s.fits"
        cls.setup2()

class Test612(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C612_%s.fits"
        cls.setup2()

class Test613(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C613_%s.fits"
        cls.setup2()

class Test614(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C614_%s.fits"
        cls.setup2()

class Test615(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C615_%s.fits"
        cls.setup2()

class Test616(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C616_%s.fits"
        cls.setup2()

class Test617(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C617_%s.fits"
        cls.setup2()

class Test618(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C618_%s.fits"
        cls.setup2()

class Test619(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C619_%s.fits"
        cls.setup2()

class Test620(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C620_%s.fits"
        cls.setup2()

class Test621(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C621_%s.fits"
        cls.setup2()

