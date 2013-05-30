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


class Test1912(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1912_%s.fits"
        cls.setup2()

class Test1913(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1913_%s.fits"
        cls.setup2()

class Test1914(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1914_%s.fits"
        cls.setup2()

class Test1915(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1915_%s.fits"
        cls.setup2()

class Test1916(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1916_%s.fits"
        cls.setup2()

class Test1917(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1917_%s.fits"
        cls.setup2()

class Test1918(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1918_%s.fits"
        cls.setup2()

class Test1919(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1919_%s.fits"
        cls.setup2()

class Test1920(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1920_%s.fits"
        cls.setup2()

class Test1921(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1921_%s.fits"
        cls.setup2()

class Test1922(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1922_%s.fits"
        cls.setup2()

class Test1923(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1923_%s.fits"
        cls.setup2()

class Test1924(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1924_%s.fits"
        cls.setup2()

class Test1925(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1925_%s.fits"
        cls.setup2()

class Test1926(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1926_%s.fits"
        cls.setup2()

class Test1927(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1927_%s.fits"
        cls.setup2()

class Test1928(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1928_%s.fits"
        cls.setup2()

class Test1929(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1929_%s.fits"
        cls.setup2()

class Test1930(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1930_%s.fits"
        cls.setup2()

class Test1931(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1931_%s.fits"
        cls.setup2()

class Test1932(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1932_%s.fits"
        cls.setup2()

class Test1933(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1933_%s.fits"
        cls.setup2()

class Test1934(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1934_%s.fits"
        cls.setup2()

class Test1935(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1935_%s.fits"
        cls.setup2()

class Test1936(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1936_%s.fits"
        cls.setup2()

class Test1937(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1937_%s.fits"
        cls.setup2()

class Test1938(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1938_%s.fits"
        cls.setup2()

class Test1939(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1939_%s.fits"
        cls.setup2()

class Test1940(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1940_%s.fits"
        cls.setup2()

class Test1941(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1941_%s.fits"
        cls.setup2()

class Test1942(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        cls.fname="C1942_%s.fits"
        cls.setup2()

class Test1943(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1943_%s.fits"
        cls.setup2()

class Test1944(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1944_%s.fits"
        cls.setup2()

class Test1945(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1945_%s.fits"
        cls.setup2()

class Test1946(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1946_%s.fits"
        cls.setup2()

class Test1947(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1947_%s.fits"
        cls.setup2()

class Test1948(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1948_%s.fits"
        cls.setup2()

class Test1949(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1949_%s.fits"
        cls.setup2()

class Test1950(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1950_%s.fits"
        cls.setup2()

class Test1951(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1951_%s.fits"
        cls.setup2()

class Test1952(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1952_%s.fits"
        cls.setup2()

class Test1953(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1953_%s.fits"
        cls.setup2()

class Test1954(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1954_%s.fits"
        cls.setup2()

class Test1955(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1955_%s.fits"
        cls.setup2()

class Test1956(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1956_%s.fits"
        cls.setup2()

class Test1957(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1957_%s.fits"
        cls.setup2()

class Test1958(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1958_%s.fits"
        cls.setup2()

class Test1959(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1959_%s.fits"
        cls.setup2()

class Test1960(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1960_%s.fits"
        cls.setup2()

class Test1961(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1961_%s.fits"
        cls.setup2()

