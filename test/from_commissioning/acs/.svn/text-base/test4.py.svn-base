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


class Test622(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C622_%s.fits"
        cls.setup2()

class Test623(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C623_%s.fits"
        cls.setup2()

class Test624(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C624_%s.fits"
        cls.setup2()

class Test625(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C625_%s.fits"
        cls.setup2()

class Test626(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C626_%s.fits"
        cls.setup2()

class Test627(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        cls.fname="C627_%s.fits"
        cls.setup2()

class Test628(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C628_%s.fits"
        cls.setup2()

class Test629(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C629_%s.fits"
        cls.setup2()

class Test630(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C630_%s.fits"
        cls.setup2()

class Test631(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C631_%s.fits"
        cls.setup2()

class Test632(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C632_%s.fits"
        cls.setup2()

class Test633(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C633_%s.fits"
        cls.setup2()

class Test634(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C634_%s.fits"
        cls.setup2()

class Test635(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C635_%s.fits"
        cls.setup2()

class Test636(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C636_%s.fits"
        cls.setup2()

class Test637(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C637_%s.fits"
        cls.setup2()

class Test638(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C638_%s.fits"
        cls.setup2()

class Test639(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C639_%s.fits"
        cls.setup2()

class Test640(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C640_%s.fits"
        cls.setup2()

class Test641(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C641_%s.fits"
        cls.setup2()

class Test642(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C642_%s.fits"
        cls.setup2()

class Test643(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C643_%s.fits"
        cls.setup2()

class Test644(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C644_%s.fits"
        cls.setup2()

class Test645(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C645_%s.fits"
        cls.setup2()

class Test646(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C646_%s.fits"
        cls.setup2()

class Test647(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C647_%s.fits"
        cls.setup2()

class Test648(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C648_%s.fits"
        cls.setup2()

class Test649(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C649_%s.fits"
        cls.setup2()

class Test650(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C650_%s.fits"
        cls.setup2()

class Test651(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C651_%s.fits"
        cls.setup2()

class Test652(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C652_%s.fits"
        cls.setup2()

class Test653(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C653_%s.fits"
        cls.setup2()

class Test654(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C654_%s.fits"
        cls.setup2()

class Test655(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C655_%s.fits"
        cls.setup2()

class Test656(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C656_%s.fits"
        cls.setup2()

class Test657(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C657_%s.fits"
        cls.setup2()

class Test658(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C658_%s.fits"
        cls.setup2()

class Test659(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C659_%s.fits"
        cls.setup2()

class Test660(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C660_%s.fits"
        cls.setup2()

class Test661(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C661_%s.fits"
        cls.setup2()

class Test662(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C662_%s.fits"
        cls.setup2()

class Test663(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C663_%s.fits"
        cls.setup2()

class Test664(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C664_%s.fits"
        cls.setup2()

class Test665(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C665_%s.fits"
        cls.setup2()

class Test666(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C666_%s.fits"
        cls.setup2()

class Test667(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C667_%s.fits"
        cls.setup2()

class Test668(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C668_%s.fits"
        cls.setup2()

class Test669(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C669_%s.fits"
        cls.setup2()

class Test670(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C670_%s.fits"
        cls.setup2()

class Test671(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C671_%s.fits"
        cls.setup2()

