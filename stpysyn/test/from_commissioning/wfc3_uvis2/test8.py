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


class Test2212(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C2212_%s.fits"
        cls.setup2()

class Test2213(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C2213_%s.fits"
        cls.setup2()

class Test2214(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C2214_%s.fits"
        cls.setup2()

class Test2215(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2215_%s.fits"
        cls.setup2()

class Test2216(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2216_%s.fits"
        cls.setup2()

class Test2217(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2217_%s.fits"
        cls.setup2()

class Test2218(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2218_%s.fits"
        cls.setup2()

class Test2219(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2219_%s.fits"
        cls.setup2()

class Test2220(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2220_%s.fits"
        cls.setup2()

class Test2221(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2221_%s.fits"
        cls.setup2()

class Test2222(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2222_%s.fits"
        cls.setup2()

class Test2223(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2223_%s.fits"
        cls.setup2()

class Test2224(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2224_%s.fits"
        cls.setup2()

class Test2225(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2225_%s.fits"
        cls.setup2()

class Test2226(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2226_%s.fits"
        cls.setup2()

class Test2227(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2227_%s.fits"
        cls.setup2()

class Test2228(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2228_%s.fits"
        cls.setup2()

class Test2229(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C2229_%s.fits"
        cls.setup2()

class Test2230(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2230_%s.fits"
        cls.setup2()

class Test2231(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C2231_%s.fits"
        cls.setup2()

class Test2232(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2232_%s.fits"
        cls.setup2()

class Test2233(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2233_%s.fits"
        cls.setup2()

class Test2234(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2234_%s.fits"
        cls.setup2()

class Test2235(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2235_%s.fits"
        cls.setup2()

class Test2236(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2236_%s.fits"
        cls.setup2()

class Test2237(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2237_%s.fits"
        cls.setup2()

class Test2238(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2238_%s.fits"
        cls.setup2()

class Test2239(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2239_%s.fits"
        cls.setup2()

class Test2240(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2240_%s.fits"
        cls.setup2()

