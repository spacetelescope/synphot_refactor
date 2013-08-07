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


class Test1261(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1261_%s.fits"
        cls.setup2()

class Test1262(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1262_%s.fits"
        cls.setup2()

class Test1263(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1263_%s.fits"
        cls.setup2()

class Test1264(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1264_%s.fits"
        cls.setup2()

class Test1265(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1265_%s.fits"
        cls.setup2()

class Test1266(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C1266_%s.fits"
        cls.setup2()

class Test1267(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C1267_%s.fits"
        cls.setup2()

class Test1268(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C1268_%s.fits"
        cls.setup2()

class Test1269(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1269_%s.fits"
        cls.setup2()

class Test1270(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1270_%s.fits"
        cls.setup2()

class Test1271(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1271_%s.fits"
        cls.setup2()

class Test1272(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1272_%s.fits"
        cls.setup2()

class Test1273(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1273_%s.fits"
        cls.setup2()

class Test1274(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1274_%s.fits"
        cls.setup2()

class Test1275(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1275_%s.fits"
        cls.setup2()

class Test1276(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1276_%s.fits"
        cls.setup2()

class Test1277(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1277_%s.fits"
        cls.setup2()

class Test1278(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1278_%s.fits"
        cls.setup2()

class Test1279(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1279_%s.fits"
        cls.setup2()

class Test1280(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1280_%s.fits"
        cls.setup2()

class Test1281(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1281_%s.fits"
        cls.setup2()

class Test1282(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1282_%s.fits"
        cls.setup2()

class Test1283(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1283_%s.fits"
        cls.setup2()

class Test1284(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1284_%s.fits"
        cls.setup2()

class Test1285(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1285_%s.fits"
        cls.setup2()

class Test1286(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1286_%s.fits"
        cls.setup2()

class Test1287(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1287_%s.fits"
        cls.setup2()

class Test1288(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1288_%s.fits"
        cls.setup2()

class Test1289(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1289_%s.fits"
        cls.setup2()

class Test1290(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1290_%s.fits"
        cls.setup2()

class Test1291(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1291_%s.fits"
        cls.setup2()

class Test1292(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1292_%s.fits"
        cls.setup2()

class Test1293(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1293_%s.fits"
        cls.setup2()

class Test1294(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1294_%s.fits"
        cls.setup2()

class Test1295(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1295_%s.fits"
        cls.setup2()

class Test1296(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1296_%s.fits"
        cls.setup2()

class Test1297(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1297_%s.fits"
        cls.setup2()

class Test1298(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1298_%s.fits"
        cls.setup2()

class Test1299(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1299_%s.fits"
        cls.setup2()

class Test1300(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1300_%s.fits"
        cls.setup2()

class Test1301(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1301_%s.fits"
        cls.setup2()

class Test1302(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1302_%s.fits"
        cls.setup2()

class Test1303(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1303_%s.fits"
        cls.setup2()

class Test1304(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1304_%s.fits"
        cls.setup2()

class Test1305(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1305_%s.fits"
        cls.setup2()

class Test1306(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1306_%s.fits"
        cls.setup2()

class Test1307(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1307_%s.fits"
        cls.setup2()

class Test1308(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1308_%s.fits"
        cls.setup2()

class Test1309(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1309_%s.fits"
        cls.setup2()

class Test1310(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1310_%s.fits"
        cls.setup2()

