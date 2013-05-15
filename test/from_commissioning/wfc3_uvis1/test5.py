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


class Test1683(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1683_%s.fits"
        cls.setup2()

class Test1684(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1684_%s.fits"
        cls.setup2()

class Test1685(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1685_%s.fits"
        cls.setup2()

class Test1686(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1686_%s.fits"
        cls.setup2()

class Test1687(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1687_%s.fits"
        cls.setup2()

class Test1688(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1688_%s.fits"
        cls.setup2()

class Test1689(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1689_%s.fits"
        cls.setup2()

class Test1690(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1690_%s.fits"
        cls.setup2()

class Test1691(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1691_%s.fits"
        cls.setup2()

class Test1692(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1692_%s.fits"
        cls.setup2()

class Test1693(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1693_%s.fits"
        cls.setup2()

class Test1694(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1694_%s.fits"
        cls.setup2()

class Test1695(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1695_%s.fits"
        cls.setup2()

class Test1696(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1696_%s.fits"
        cls.setup2()

class Test1697(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1697_%s.fits"
        cls.setup2()

class Test1698(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1698_%s.fits"
        cls.setup2()

class Test1699(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1699_%s.fits"
        cls.setup2()

class Test1700(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1700_%s.fits"
        cls.setup2()

class Test1701(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1701_%s.fits"
        cls.setup2()

class Test1702(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1702_%s.fits"
        cls.setup2()

class Test1703(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1703_%s.fits"
        cls.setup2()

class Test1704(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1704_%s.fits"
        cls.setup2()

class Test1705(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1705_%s.fits"
        cls.setup2()

class Test1706(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1706_%s.fits"
        cls.setup2()

class Test1707(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1707_%s.fits"
        cls.setup2()

class Test1708(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1708_%s.fits"
        cls.setup2()

class Test1709(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1709_%s.fits"
        cls.setup2()

class Test1710(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1710_%s.fits"
        cls.setup2()

class Test1711(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1711_%s.fits"
        cls.setup2()

class Test1712(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1712_%s.fits"
        cls.setup2()

class Test1713(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1713_%s.fits"
        cls.setup2()

class Test1714(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1714_%s.fits"
        cls.setup2()

class Test1715(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1715_%s.fits"
        cls.setup2()

class Test1716(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1716_%s.fits"
        cls.setup2()

class Test1717(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1717_%s.fits"
        cls.setup2()

class Test1718(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1718_%s.fits"
        cls.setup2()

class Test1719(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1719_%s.fits"
        cls.setup2()

class Test1720(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1720_%s.fits"
        cls.setup2()

class Test1721(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1721_%s.fits"
        cls.setup2()

class Test1722(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1722_%s.fits"
        cls.setup2()

class Test1723(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1723_%s.fits"
        cls.setup2()

class Test1724(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1724_%s.fits"
        cls.setup2()

class Test1725(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1725_%s.fits"
        cls.setup2()

class Test1726(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1726_%s.fits"
        cls.setup2()

class Test1727(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1727_%s.fits"
        cls.setup2()

class Test1728(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1728_%s.fits"
        cls.setup2()

class Test1729(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1729_%s.fits"
        cls.setup2()

class Test1730(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1730_%s.fits"
        cls.setup2()

class Test1731(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1731_%s.fits"
        cls.setup2()

class Test1732(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1732_%s.fits"
        cls.setup2()

