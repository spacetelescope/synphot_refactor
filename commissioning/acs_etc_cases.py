from pytools import testutil
import sys
import basecase
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=True
        self.etcid="ACS.MISC.1.IMAG.029"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.032"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="ACS.MISC.1.IMAG.029"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.035"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.037"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.036"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.038"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.039"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        self.subset=True
        self.etcid="ACS.HRC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        self.subset=True
        self.etcid="ACS.MISC.1.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="ACS.HRC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=True
        self.etcid="ACS.HRC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.SBC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        self.subset=True
        self.etcid="ACS.SBC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.SBC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=True
        self.etcid="ACS.WFC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.WFC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="ACS.WFC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="ACS.WFC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.024"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.019"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.016"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.020"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.subset=True
        self.etcid="ACS.WFC.PT.RAMP.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.023"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.025"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.022"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.021"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.015"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=False
        self.etcid="['ACS.SBC.PT.IMAG.008', 'ACS.SBC.SPEC.007', 'ACS.SBC.SPEC.008', 'ACS.WFC.PT.IMAG.015', 'ACS.WFC.PT.RAMP.024', 'ACS.WFC.SPEC.003', 'ACS.HRC.PT.IMAG.019', 'ACS.HRC.PT.RAMP.013', 'ACS.HRC.SPEC.007', 'ACS.HRC.SPEC.008']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.subset=False
        self.etcid="['ACS.SBC.PT.IMAG.007', 'ACS.SBC.SPEC.005', 'ACS.SBC.SPEC.006', 'ACS.WFC.PT.IMAG.014', 'ACS.WFC.PT.RAMP.025', 'ACS.WFC.SPEC.002', 'ACS.HRC.PT.IMAG.018', 'ACS.HRC.PT.RAMP.014', 'ACS.HRC.SPEC.005', 'ACS.HRC.SPEC.006']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.024"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.019"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.020"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.025"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.029"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.032"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.SBC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=True
        self.etcid="ACS.WFC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.021"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.029"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.EXT.RAMP.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.018"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.EXT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.PT.RAMP.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.006"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.010"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.035"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.037"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.036"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.038"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        self.subset=False
        self.etcid="ACS.MISC.1.IMAG.039"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.011"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.012"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        self.subset=True
        self.etcid="ACS.HRC.SPEC.011"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.010"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.008"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.007"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.007"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.008"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.003"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.009"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.012"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.009"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.010"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=True
        self.etcid="ACS.HRC.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.006"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.006"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.002"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.005"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.006"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.MISC.1.SPEC.009"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="ACS.A1.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.002"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.002"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.003"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.003"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.HRC.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.001"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.SBC.SPEC.004"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.subset=False
        self.etcid="ACS.WFC.SPEC.006"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:40 - 33 dup =7
#thermback:0 - 0 dup =0
#calcphot:190 - 0 dup =190
#countrate:190 - 0 dup =190
#SpecSourcerateSpec:35 - 0 dup =35
