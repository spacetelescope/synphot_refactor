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


class Test672(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C672_%s.fits"
        cls.setup2()

class Test673(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C673_%s.fits"
        cls.setup2()

class Test674(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C674_%s.fits"
        cls.setup2()

class Test675(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C675_%s.fits"
        cls.setup2()

class Test676(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C676_%s.fits"
        cls.setup2()

class Test677(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C677_%s.fits"
        cls.setup2()

class Test678(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C678_%s.fits"
        cls.setup2()

class Test679(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C679_%s.fits"
        cls.setup2()

class Test680(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C680_%s.fits"
        cls.setup2()

class Test681(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C681_%s.fits"
        cls.setup2()

class Test682(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C682_%s.fits"
        cls.setup2()

class Test683(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C683_%s.fits"
        cls.setup2()

class Test684(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C684_%s.fits"
        cls.setup2()

class Test685(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C685_%s.fits"
        cls.setup2()

class Test686(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C686_%s.fits"
        cls.setup2()

class Test687(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C687_%s.fits"
        cls.setup2()

class Test688(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C688_%s.fits"
        cls.setup2()

class Test689(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C689_%s.fits"
        cls.setup2()

class Test690(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C690_%s.fits"
        cls.setup2()

class Test691(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C691_%s.fits"
        cls.setup2()

class Test692(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C692_%s.fits"
        cls.setup2()

class Test693(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C693_%s.fits"
        cls.setup2()

class Test694(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C694_%s.fits"
        cls.setup2()

class Test695(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C695_%s.fits"
        cls.setup2()

class Test696(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C696_%s.fits"
        cls.setup2()

class Test697(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C697_%s.fits"
        cls.setup2()

class Test698(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C698_%s.fits"
        cls.setup2()

class Test699(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C699_%s.fits"
        cls.setup2()

class Test700(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C700_%s.fits"
        cls.setup2()

class Test701(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C701_%s.fits"
        cls.setup2()

class Test702(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C702_%s.fits"
        cls.setup2()

class Test703(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C703_%s.fits"
        cls.setup2()

class Test704(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C704_%s.fits"
        cls.setup2()

class Test705(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C705_%s.fits"
        cls.setup2()

class Test706(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C706_%s.fits"
        cls.setup2()

class Test707(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C707_%s.fits"
        cls.setup2()

class Test708(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C708_%s.fits"
        cls.setup2()

class Test709(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C709_%s.fits"
        cls.setup2()

class Test710(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C710_%s.fits"
        cls.setup2()

class Test711(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C711_%s.fits"
        cls.setup2()

class Test712(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C712_%s.fits"
        cls.setup2()

class Test713(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C713_%s.fits"
        cls.setup2()

class Test714(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C714_%s.fits"
        cls.setup2()

class Test715(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C715_%s.fits"
        cls.setup2()

class Test716(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C716_%s.fits"
        cls.setup2()

class Test717(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C717_%s.fits"
        cls.setup2()

class Test718(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C718_%s.fits"
        cls.setup2()

class Test719(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C719_%s.fits"
        cls.setup2()

class Test720(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C720_%s.fits"
        cls.setup2()

class Test721(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C721_%s.fits"
        cls.setup2()

