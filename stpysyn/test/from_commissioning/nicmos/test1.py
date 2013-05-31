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


class Test791(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C791_%s.fits"
        cls.setup2()

class Test792(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C792_%s.fits"
        cls.setup2()

class Test793(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C793_%s.fits"
        cls.setup2()

class Test794(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C794_%s.fits"
        cls.setup2()

class Test795(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C795_%s.fits"
        cls.setup2()

class Test796(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C796_%s.fits"
        cls.setup2()

class Test797(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C797_%s.fits"
        cls.setup2()

class Test798(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C798_%s.fits"
        cls.setup2()

class Test799(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C799_%s.fits"
        cls.setup2()

class Test800(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C800_%s.fits"
        cls.setup2()

class Test801(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C801_%s.fits"
        cls.setup2()

class Test802(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C802_%s.fits"
        cls.setup2()

class Test803(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        cls.fname="C803_%s.fits"
        cls.setup2()

class Test804(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C804_%s.fits"
        cls.setup2()

class Test805(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C805_%s.fits"
        cls.setup2()

class Test806(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C806_%s.fits"
        cls.setup2()

class Test807(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C807_%s.fits"
        cls.setup2()

class Test808(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C808_%s.fits"
        cls.setup2()

class Test809(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C809_%s.fits"
        cls.setup2()

class Test810(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C810_%s.fits"
        cls.setup2()

class Test811(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C811_%s.fits"
        cls.setup2()

class Test812(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C812_%s.fits"
        cls.setup2()

class Test813(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C813_%s.fits"
        cls.setup2()

class Test814(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C814_%s.fits"
        cls.setup2()

class Test815(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C815_%s.fits"
        cls.setup2()

class Test816(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C816_%s.fits"
        cls.setup2()

class Test817(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C817_%s.fits"
        cls.setup2()

class Test818(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C818_%s.fits"
        cls.setup2()

class Test819(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C819_%s.fits"
        cls.setup2()

class Test820(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C820_%s.fits"
        cls.setup2()

class Test821(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C821_%s.fits"
        cls.setup2()

class Test822(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C822_%s.fits"
        cls.setup2()

class Test823(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C823_%s.fits"
        cls.setup2()

class Test824(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C824_%s.fits"
        cls.setup2()

class Test825(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C825_%s.fits"
        cls.setup2()

class Test826(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C826_%s.fits"
        cls.setup2()

class Test827(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C827_%s.fits"
        cls.setup2()

class Test828(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C828_%s.fits"
        cls.setup2()

class Test829(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C829_%s.fits"
        cls.setup2()

class Test830(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C830_%s.fits"
        cls.setup2()

class Test831(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C831_%s.fits"
        cls.setup2()

class Test832(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C832_%s.fits"
        cls.setup2()

class Test833(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C833_%s.fits"
        cls.setup2()

class Test834(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C834_%s.fits"
        cls.setup2()

class Test835(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C835_%s.fits"
        cls.setup2()

class Test836(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C836_%s.fits"
        cls.setup2()

class Test837(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C837_%s.fits"
        cls.setup2()

class Test838(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C838_%s.fits"
        cls.setup2()

class Test839(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        cls.fname="C839_%s.fits"
        cls.setup2()

class Test840(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        cls.fname="C840_%s.fits"
        cls.setup2()

