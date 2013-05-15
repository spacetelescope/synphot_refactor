import basecase
class wfc3C1(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f105w),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C2(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f105w),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C3(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f160w),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C4(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f160w),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C5(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f128n),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C6(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f128n),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C7(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f139m),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C8(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f139m),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C9(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f167n),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C10(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f167n),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C11(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,g102),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C12(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,g102),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C13(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f105w),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C14(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f105w),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C15(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f160w),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C16(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f160w),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C17(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f128n),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C18(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f128n),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C19(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f139m),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C20(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f139m),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C21(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,f167n),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C22(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,f167n),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C23(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(2000),band(wfc3,ir,g102),0.30,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C24(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(bb(5500),band(wfc3,ir,g102),0.003,mjy)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C25(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(wfc3,ir,f105w),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C26(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(wfc3,ir,f105w),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C27(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_57.fits),band(wfc3,ir,f160w),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C28(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_61.fits),band(wfc3,ir,f160w),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C29(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_77.fits),band(wfc3,ir,f128n),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C30(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(wfc3,ir,f128n),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C31(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(wfc3,ir,f139m),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C32(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_57.fits),band(wfc3,ir,f139m),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C33(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_61.fits),band(wfc3,ir,f167n),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C34(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_77.fits),band(wfc3,ir,f167n),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C35(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(wfc3,ir,g102),20.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C36(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(wfc3,ir,g102),25.0,stmag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C37(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(bessell,j),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C38(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(bessell,j),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C39(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_57.fits),band(bessell,h),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C40(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_61.fits),band(bessell,h),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C41(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_77.fits),band(bessell,j),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C42(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(bessell,j),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C43(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(bessell,h),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C44(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_57.fits),band(bessell,h),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C45(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_61.fits),band(bessell,j),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C46(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_77.fits),band(bessell,j),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C47(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_35.fits),band(bessell,h),17.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

class wfc3C48(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='rn(spec(/grp/hst/cdbs/grid/bz77/bz_48.fits),band(bessell,h),23.0,vegamag)'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()

