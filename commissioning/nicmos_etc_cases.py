from pytools import testutil
import sys
import basecase
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NIC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:ImagingA:00001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:ImagingA:00001"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits)"
        self.subset=False
        self.etcid="['ImagingA:00012', 'ImagingB:95']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00012', 'ImagingA:00021', 'ImagingA:00028']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00012', 'ImagingA:00021', 'ImagingA:00028']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits)"
        self.subset=False
        self.etcid="['ImagingA:00013', 'ImagingB:96']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00013"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits)"
        self.subset=False
        self.etcid="['ImagingA:00014', 'ImagingB:97']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00014', 'ImagingA:00022', 'ImagingA:00029']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00014', 'ImagingA:00022', 'ImagingA:00029']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits)"
        self.subset=False
        self.etcid="['ImagingA:00015', 'ImagingB:98']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00015', 'ImagingA:00023', 'ImagingA:00030']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00015', 'ImagingA:00023', 'ImagingA:00030']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits)"
        self.subset=False
        self.etcid="['ImagingA:00016', 'ImagingB:99']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="['ImagingA:00016', 'ImagingA:00031']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="['ImagingA:00016', 'ImagingA:00031']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,6250,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00017"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,15000,0.0,3.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00018"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,7750,0.0,2.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00019"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,4750,0.0,1.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00020"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00024"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00025"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00025"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00026"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00026"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00027"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00027"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00032"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00032"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00033"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00033"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00034"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00034"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00035"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00035"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00036"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00036"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00037"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00037"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00038"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00038"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(7700)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00039"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00039"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(6200)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00040"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00040"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00041"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00041"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase41(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-0.5,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00042"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00042"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00043"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00043"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase43(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.5,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00044"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00044"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00045"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00045"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00046"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00046"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00047"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00047"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00048"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00048"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        self.subset=False
        self.etcid="ImagingA:00049"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        self.subset=False
        self.etcid="ImagingA:00049"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00052"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00052"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        self.subset=False
        self.etcid="ImagingA:00053"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        self.subset=False
        self.etcid="ImagingA:00053"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00054"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00054"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        self.subset=False
        self.etcid="ImagingA:00055"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        self.subset=True
        self.etcid="ImagingA:00055"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00056"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00056"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00057"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00057"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00058"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.subset=True
        self.etcid="ImagingA:00058"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00059"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00059"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00060"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00060"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00061"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00061"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00062"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00062"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00063"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00063"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00064"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00064"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00065"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00065"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00066"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00066"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00067"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00067"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00068"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00068"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00069"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00069"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00070"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        self.subset=False
        self.etcid="ImagingA:00070"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00071"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00071"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00072"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00072"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00073"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="ImagingA:00073"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase44(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.subset=False
        self.etcid="['ImagingB:158', 'ImagingA:00074']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.subset=False
        self.etcid="ImagingA:00074"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.subset=True
        self.etcid="ImagingA:00074"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00076"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00076"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00077"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00077"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00078"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00078"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00079"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00079"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00080"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00080"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00081"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00081"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00082"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00082"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00085"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00085"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00086"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00086"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00087"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00087"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00088"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00088"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00089"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00089"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00090"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00090"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.subset=False
        self.etcid="ImagingA:00091"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.subset=False
        self.etcid="ImagingA:00091"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        self.subset=True
        self.etcid="ImagingA:00092"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        self.subset=False
        self.etcid="ImagingA:00092"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00093"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00093"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00094"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00094"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00095"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00095"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="ImagingA:00096"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00096"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00097"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00097"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00098"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingA:00098"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00100"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00100"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00101"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00101"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00102"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00102"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00103"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00103"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00104"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=True
        self.etcid="ImagingA:00104"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00105"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00105"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00106"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00106"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00107"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00107"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00108"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00108"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00109"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=True
        self.etcid="ImagingA:00109"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00110"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00110"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00111"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00111"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ImagingA:00113"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=True
        self.etcid="ImagingA:00113"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00115"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00115"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00117"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ImagingA:00117"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S001"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.subset=True
        self.etcid="SpecA:S001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S002"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.subset=False
        self.etcid="SpecA:S002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="SpecA:S003"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.subset=False
        self.etcid="SpecA:S003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S007"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.subset=False
        self.etcid="SpecA:S007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S008"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.subset=False
        self.etcid="SpecA:S008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S009"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.subset=False
        self.etcid="SpecA:S009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S010"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.subset=False
        self.etcid="SpecA:S010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S011"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.subset=False
        self.etcid="SpecA:S011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S012"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.subset=False
        self.etcid="SpecA:S012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=True
        self.etcid="SpecA:S018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S019"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S020"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="SpecA:S021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="SpecA:S024"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.subset=False
        self.etcid="SpecA:S025"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.subset=False
        self.etcid="SpecA:S026"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.subset=False
        self.etcid="SpecA:S027"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.subset=False
        self.etcid="SpecA:S028"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.subset=True
        self.etcid="SpecA:S029"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.subset=False
        self.etcid="SpecA:S030"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.subset=False
        self.etcid="SpecA:S031"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.subset=False
        self.etcid="SpecA:S032"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.subset=False
        self.etcid="SpecA:S033"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.subset=False
        self.etcid="SpecA:S034"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.subset=False
        self.etcid="SpecA:S035"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.subset=True
        self.etcid="SpecA:S036"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase37(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.subset=False
        self.etcid="SpecA:S037"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase38(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.subset=False
        self.etcid="SpecA:S038"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase39(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.subset=False
        self.etcid="SpecA:S039"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase49(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S049"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase45(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.subset=False
        self.etcid="['ImagingB:118', 'SpecA:S050', 'SpecA:S051', 'SpecA:S053', 'SpecA:S054', 'SpecA:S055', 'SpecA:S056', 'SpecA:S057', 'SpecA:S058', 'SpecA:S059', 'SpecA:S060']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase50(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S050"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase51(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase52(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.subset=False
        self.etcid="SpecA:S052"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase53(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.subset=False
        self.etcid="SpecA:S053"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase54(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase55(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,45000,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase61(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.subset=True
        self.etcid="SpecA:S061"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase62(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S062"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase63(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S063"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase64(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S064"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase58(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase65(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S065"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase66(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S066"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase59(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase67(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        self.subset=True
        self.etcid="SpecA:S067"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase68(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.subset=True
        self.etcid="SpecA:S068"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase69(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.subset=True
        self.etcid="SpecA:S069"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase70(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S070"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase71(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S071"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase72(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S072"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase73(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.subset=True
        self.etcid="SpecA:S073"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase74(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.subset=False
        self.etcid="SpecA:S074"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase75(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        self.subset=False
        self.etcid="SpecA:S075"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase76(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        self.subset=False
        self.etcid="SpecA:S076"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase77(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        self.subset=False
        self.etcid="SpecA:S077"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase78(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        self.subset=True
        self.etcid="SpecA:S078"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="ImagingB:37"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ImagingB:37"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase191(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase191(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase192(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase192(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase193(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase193(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase194(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase194(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase195(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase195(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase196(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase196(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase197(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase197(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase198(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase198(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase199(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase199(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase200(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase200(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase201(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase201(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase202(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class countrateCase202(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class countrateCase203(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase203(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase204(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class countrateCase204(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class countrateCase205(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.028"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase205(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.028"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase206(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.028"
        self.setglobal(__file__)
        self.runpy()
class countrateCase206(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.028"
        self.setglobal(__file__)
        self.runpy()
class countrateCase207(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.030"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase207(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.030"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase208(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.030"
        self.setglobal(__file__)
        self.runpy()
class countrateCase208(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.030"
        self.setglobal(__file__)
        self.runpy()
class countrateCase209(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.031"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase209(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.031"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase210(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.031"
        self.setglobal(__file__)
        self.runpy()
class countrateCase210(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.031"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase211(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.032"
        self.setglobal(__file__)
        self.runpy()
class countrateCase211(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.032"
        self.setglobal(__file__)
        self.runpy()
class countrateCase212(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.033"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase212(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.033"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase213(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.033"
        self.setglobal(__file__)
        self.runpy()
class countrateCase213(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.033"
        self.setglobal(__file__)
        self.runpy()
class countrateCase214(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.034"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase214(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.034"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase215(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NIC.PT.IMAG.034"
        self.setglobal(__file__)
        self.runpy()
class countrateCase215(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NIC.PT.IMAG.034"
        self.setglobal(__file__)
        self.runpy()
class countrateCase216(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase216(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase217(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase217(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase218(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase218(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase219(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase219(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase220(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase220(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase221(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase221(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase222(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase222(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase223(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase223(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase224(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase224(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase225(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase225(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase226(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase226(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase227(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase227(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase228(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase228(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase229(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase229(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase230(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase230(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase231(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase231(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase232(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase232(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase233(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase233(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase234(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase234(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase235(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase235(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase236(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase236(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase237(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase237(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase238(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase238(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase239(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase239(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase240(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase240(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase241(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase241(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase242(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase242(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase243(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase243(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase244(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1458"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase244(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1458"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase245(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1458"
        self.setglobal(__file__)
        self.runpy()
class countrateCase245(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1458"
        self.setglobal(__file__)
        self.runpy()
class countrateCase246(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1459"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase246(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1459"
        self.setglobal(__file__)
        self.runpy()
class countrateCase247(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1460"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase247(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1460"
        self.setglobal(__file__)
        self.runpy()
class countrateCase248(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1461"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase248(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1461"
        self.setglobal(__file__)
        self.runpy()
class countrateCase249(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1463"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase249(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1463"
        self.setglobal(__file__)
        self.runpy()
class countrateCase250(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1464"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase250(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1464"
        self.setglobal(__file__)
        self.runpy()
class countrateCase251(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1465"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase251(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1465"
        self.setglobal(__file__)
        self.runpy()
class countrateCase252(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1466"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase252(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1466"
        self.setglobal(__file__)
        self.runpy()
class countrateCase253(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1467"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase253(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1467"
        self.setglobal(__file__)
        self.runpy()
class countrateCase254(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1468"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase254(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1468"
        self.setglobal(__file__)
        self.runpy()
class countrateCase255(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1470"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase255(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1470"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase145(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase256(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1471"
        self.setglobal(__file__)
        self.runpy()
class countrateCase256(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1471"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase257(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1472"
        self.setglobal(__file__)
        self.runpy()
class countrateCase257(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1472"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase258(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1473"
        self.setglobal(__file__)
        self.runpy()
class countrateCase258(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1473"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase259(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1474"
        self.setglobal(__file__)
        self.runpy()
class countrateCase259(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1474"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase260(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1479"
        self.setglobal(__file__)
        self.runpy()
class countrateCase260(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1479"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase261(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1480"
        self.setglobal(__file__)
        self.runpy()
class countrateCase261(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1480"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase262(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1481"
        self.setglobal(__file__)
        self.runpy()
class countrateCase262(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1481"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase263(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1482"
        self.setglobal(__file__)
        self.runpy()
class countrateCase263(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1482"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase264(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        self.subset=False
        self.etcid="NICIMAG1483"
        self.setglobal(__file__)
        self.runpy()
class countrateCase264(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        self.subset=True
        self.etcid="NICIMAG1483"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase265(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.01"
        self.setglobal(__file__)
        self.runpy()
class countrateCase265(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.01"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase79(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.01"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase266(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.02"
        self.setglobal(__file__)
        self.runpy()
class countrateCase266(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.02"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase80(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=True
        self.etcid="NIC.SPEC.CTS.02"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase267(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.03"
        self.setglobal(__file__)
        self.runpy()
class countrateCase267(basecase.countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.03"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase81(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="NIC.SPEC.CTS.03"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:148 - 122 dup =26
#thermback:0 - 0 dup =0
#calcphot:267 - 8 dup =259
#countrate:267 - 8 dup =259
#SpecSourcerateSpec:81 - 30 dup =51
