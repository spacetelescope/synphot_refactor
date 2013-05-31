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


class Test472(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C472_%s.fits"
        cls.setup2()

class Test473(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C473_%s.fits"
        cls.setup2()

class Test474(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C474_%s.fits"
        cls.setup2()

class Test475(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        cls.fname="C475_%s.fits"
        cls.setup2()

class Test476(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        cls.fname="C476_%s.fits"
        cls.setup2()

class Test477(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        cls.fname="C477_%s.fits"
        cls.setup2()

class Test478(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        cls.fname="C478_%s.fits"
        cls.setup2()

class Test479(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        cls.fname="C479_%s.fits"
        cls.setup2()

class Test480(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C480_%s.fits"
        cls.setup2()

class Test481(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C481_%s.fits"
        cls.setup2()

class Test482(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C482_%s.fits"
        cls.setup2()

class Test483(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C483_%s.fits"
        cls.setup2()

class Test484(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C484_%s.fits"
        cls.setup2()

class Test485(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C485_%s.fits"
        cls.setup2()

class Test486(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C486_%s.fits"
        cls.setup2()

class Test487(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C487_%s.fits"
        cls.setup2()

class Test488(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C488_%s.fits"
        cls.setup2()

class Test489(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C489_%s.fits"
        cls.setup2()

class Test490(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C490_%s.fits"
        cls.setup2()

class Test491(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C491_%s.fits"
        cls.setup2()

class Test492(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C492_%s.fits"
        cls.setup2()

class Test493(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C493_%s.fits"
        cls.setup2()

class Test494(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C494_%s.fits"
        cls.setup2()

class Test495(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        cls.fname="C495_%s.fits"
        cls.setup2()

class Test496(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C496_%s.fits"
        cls.setup2()

class Test497(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C497_%s.fits"
        cls.setup2()

class Test498(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C498_%s.fits"
        cls.setup2()

class Test499(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C499_%s.fits"
        cls.setup2()

class Test500(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C500_%s.fits"
        cls.setup2()

class Test501(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C501_%s.fits"
        cls.setup2()

class Test502(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C502_%s.fits"
        cls.setup2()

class Test503(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C503_%s.fits"
        cls.setup2()

class Test504(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C504_%s.fits"
        cls.setup2()

class Test505(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C505_%s.fits"
        cls.setup2()

class Test506(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C506_%s.fits"
        cls.setup2()

class Test507(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C507_%s.fits"
        cls.setup2()

class Test508(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C508_%s.fits"
        cls.setup2()

class Test509(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C509_%s.fits"
        cls.setup2()

class Test510(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C510_%s.fits"
        cls.setup2()

class Test511(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C511_%s.fits"
        cls.setup2()

class Test512(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C512_%s.fits"
        cls.setup2()

class Test513(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C513_%s.fits"
        cls.setup2()

class Test514(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C514_%s.fits"
        cls.setup2()

class Test515(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C515_%s.fits"
        cls.setup2()

class Test516(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C516_%s.fits"
        cls.setup2()

class Test517(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C517_%s.fits"
        cls.setup2()

class Test518(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C518_%s.fits"
        cls.setup2()

class Test519(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C519_%s.fits"
        cls.setup2()

class Test520(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C520_%s.fits"
        cls.setup2()

class Test521(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C521_%s.fits"
        cls.setup2()

