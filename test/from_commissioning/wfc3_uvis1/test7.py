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


class Test1783(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1783_%s.fits"
        cls.setup2()

class Test1784(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1784_%s.fits"
        cls.setup2()

class Test1785(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1785_%s.fits"
        cls.setup2()

class Test1786(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1786_%s.fits"
        cls.setup2()

class Test1787(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1787_%s.fits"
        cls.setup2()

class Test1788(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1788_%s.fits"
        cls.setup2()

class Test1789(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1789_%s.fits"
        cls.setup2()

class Test1790(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1790_%s.fits"
        cls.setup2()

class Test1791(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1791_%s.fits"
        cls.setup2()

class Test1792(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1792_%s.fits"
        cls.setup2()

class Test1793(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1793_%s.fits"
        cls.setup2()

class Test1794(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1794_%s.fits"
        cls.setup2()

class Test1795(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1795_%s.fits"
        cls.setup2()

class Test1796(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1796_%s.fits"
        cls.setup2()

class Test1797(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1797_%s.fits"
        cls.setup2()

class Test1798(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1798_%s.fits"
        cls.setup2()

class Test1799(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1799_%s.fits"
        cls.setup2()

class Test1800(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1800_%s.fits"
        cls.setup2()

class Test1801(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1801_%s.fits"
        cls.setup2()

class Test1802(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1802_%s.fits"
        cls.setup2()

class Test1803(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1803_%s.fits"
        cls.setup2()

class Test1804(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1804_%s.fits"
        cls.setup2()

class Test1805(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1805_%s.fits"
        cls.setup2()

class Test1806(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1806_%s.fits"
        cls.setup2()

class Test1807(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1807_%s.fits"
        cls.setup2()

class Test1808(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1808_%s.fits"
        cls.setup2()

class Test1809(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1809_%s.fits"
        cls.setup2()

class Test1810(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1810_%s.fits"
        cls.setup2()

class Test1811(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1811_%s.fits"
        cls.setup2()

class Test1812(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1812_%s.fits"
        cls.setup2()

class Test1813(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1813_%s.fits"
        cls.setup2()

class Test1814(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1814_%s.fits"
        cls.setup2()

class Test1815(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1815_%s.fits"
        cls.setup2()

class Test1816(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1816_%s.fits"
        cls.setup2()

class Test1817(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1817_%s.fits"
        cls.setup2()

class Test1818(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C1818_%s.fits"
        cls.setup2()

class Test1819(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C1819_%s.fits"
        cls.setup2()

class Test1820(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C1820_%s.fits"
        cls.setup2()

class Test1821(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C1821_%s.fits"
        cls.setup2()

class Test1822(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C1822_%s.fits"
        cls.setup2()

class Test1823(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C1823_%s.fits"
        cls.setup2()

class Test1824(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1824_%s.fits"
        cls.setup2()

class Test1825(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1825_%s.fits"
        cls.setup2()

class Test1826(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C1826_%s.fits"
        cls.setup2()

class Test1827(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1827_%s.fits"
        cls.setup2()

class Test1828(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1828_%s.fits"
        cls.setup2()

class Test1829(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C1829_%s.fits"
        cls.setup2()

class Test1830(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1830_%s.fits"
        cls.setup2()

class Test1831(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1831_%s.fits"
        cls.setup2()

class Test1832(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1832_%s.fits"
        cls.setup2()

