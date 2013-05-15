import basecase
class nicmosC1(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),23,abmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC2(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),23,abmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC3(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),18,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC4(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),18,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC5(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),5,obmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC6(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),5,obmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC7(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,k),5,obmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC8(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),1.0e-27,fnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC9(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.e-27,fnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC10(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-26,fnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC11(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),1.0e-14,photnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC12(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-14,photnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC13(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-14,photnu)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC14(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),1.0e-4,photlam)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC15(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-4,photlam)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC16(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),1.0e-4,photlam)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC17(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),5000,counts)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC18(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(nicmos,2,f237m),25000,counts)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC19(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),10000,counts)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC20(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,1.5),band(nicmos,2,f237m),100000,counts)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC21(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),2.0e-7,jy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC22(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),0.5,jy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC23(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),0.5,jy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC24(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(bessell,h),10,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC25(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5000),band(nicmos,3,f108n),30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC26(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,2.5),band(nicmos,3,f215n),20,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class nicmosC27(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(z(crgridkc96$sb_template.fits,1.0),band(nicmos,2,f205w),20,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

