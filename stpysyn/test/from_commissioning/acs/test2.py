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


class Test522(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C522_%s.fits"
        cls.setup2()

class Test523(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C523_%s.fits"
        cls.setup2()

class Test524(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C524_%s.fits"
        cls.setup2()

class Test525(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C525_%s.fits"
        cls.setup2()

class Test526(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C526_%s.fits"
        cls.setup2()

class Test527(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C527_%s.fits"
        cls.setup2()

class Test528(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C528_%s.fits"
        cls.setup2()

class Test529(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C529_%s.fits"
        cls.setup2()

class Test530(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C530_%s.fits"
        cls.setup2()

class Test531(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C531_%s.fits"
        cls.setup2()

class Test532(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C532_%s.fits"
        cls.setup2()

class Test533(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C533_%s.fits"
        cls.setup2()

class Test534(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C534_%s.fits"
        cls.setup2()

class Test535(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        cls.fname="C535_%s.fits"
        cls.setup2()

class Test536(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        cls.fname="C536_%s.fits"
        cls.setup2()

class Test537(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C537_%s.fits"
        cls.setup2()

class Test538(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C538_%s.fits"
        cls.setup2()

class Test539(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C539_%s.fits"
        cls.setup2()

class Test540(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C540_%s.fits"
        cls.setup2()

class Test541(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C541_%s.fits"
        cls.setup2()

class Test542(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C542_%s.fits"
        cls.setup2()

class Test543(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C543_%s.fits"
        cls.setup2()

class Test544(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C544_%s.fits"
        cls.setup2()

class Test545(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C545_%s.fits"
        cls.setup2()

class Test546(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C546_%s.fits"
        cls.setup2()

class Test547(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C547_%s.fits"
        cls.setup2()

class Test548(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C548_%s.fits"
        cls.setup2()

class Test549(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C549_%s.fits"
        cls.setup2()

class Test550(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C550_%s.fits"
        cls.setup2()

class Test551(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C551_%s.fits"
        cls.setup2()

class Test552(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C552_%s.fits"
        cls.setup2()

class Test553(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C553_%s.fits"
        cls.setup2()

class Test554(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C554_%s.fits"
        cls.setup2()

class Test555(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C555_%s.fits"
        cls.setup2()

class Test556(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C556_%s.fits"
        cls.setup2()

class Test557(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C557_%s.fits"
        cls.setup2()

class Test558(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C558_%s.fits"
        cls.setup2()

class Test559(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C559_%s.fits"
        cls.setup2()

class Test560(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C560_%s.fits"
        cls.setup2()

class Test561(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C561_%s.fits"
        cls.setup2()

class Test562(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C562_%s.fits"
        cls.setup2()

class Test563(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C563_%s.fits"
        cls.setup2()

class Test564(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C564_%s.fits"
        cls.setup2()

class Test565(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C565_%s.fits"
        cls.setup2()

class Test566(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C566_%s.fits"
        cls.setup2()

class Test567(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C567_%s.fits"
        cls.setup2()

class Test568(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C568_%s.fits"
        cls.setup2()

class Test569(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C569_%s.fits"
        cls.setup2()

class Test570(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C570_%s.fits"
        cls.setup2()

class Test571(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C571_%s.fits"
        cls.setup2()

