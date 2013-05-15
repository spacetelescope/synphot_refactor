from pytools import testutil
import sys
import basecase
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISACQ1983b"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISACQ1983b"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="STISACQ1983b"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="STISACQ1983b"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISACQ1908"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISACQ1908"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.subset=True
        self.etcid="STISACQ1908"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.subset=True
        self.etcid="STISACQ1908"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISACQ1943"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISACQ1943"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.subset=False
        self.etcid="STISACQ1943"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.subset=True
        self.etcid="STISACQ1943"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1257"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1257"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISIMAG1257"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISIMAG1257"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1258"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1258"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=True
        self.etcid="STISIMAG1258"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISIMAG1258"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1259"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1259"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISIMAG1259"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISIMAG1259"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1260"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1260"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1260"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1260"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1263"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1263"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1271"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1271"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1271"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1271"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1273"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1273"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1273"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1273"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1275"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1275"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1275"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1275"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1277"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1277"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1277"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1277"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1279"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1279"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1279"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1279"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1281"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1281"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1281"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1281"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1282"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1282"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1282"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1282"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1286"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1286"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1286"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1286"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1288"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1288"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1288"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1288"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1290"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1290"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1290"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1290"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1291"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="STISIMAG1291"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1291"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1291"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1295"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1295"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1295"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1295"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1297"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1297"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1297"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1297"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1302"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG1302"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=True
        self.etcid="STISIMAG1302"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.subset=False
        self.etcid="STISIMAG1302"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="STISIMAG110509"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISIMAG110509"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.subset=True
        self.etcid="STISIMAG110509"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="STISIMAG110509"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['STISSPEC1264', 'STISSPEC1242']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1264"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1266"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1266"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1269"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=True
        self.etcid="STISSPEC1269"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1370"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1370"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['STISSPEC1272', 'STISSPEC1396']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x2"
        self.spectrum="spec(HS20270651.dat)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['STISSPEC1346', 'STISSPEC1274']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1274"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1278"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.subset=True
        self.etcid="STISSPEC1278"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1280"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1280"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1372"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1372"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x01"
        self.spectrum="spec(HS20270651.dat)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1305"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1305"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1307"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1307"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="['STISSPEC1308', 'STISSPEC1319']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1308"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1310"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1310"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1374"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=False
        self.etcid="STISSPEC1374"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1400"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.subset=True
        self.etcid="STISSPEC1400"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1316"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1316"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1319"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase37(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1320"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase38(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1321"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase39(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1376"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase40(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1377"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(50000)"
        self.subset=True
        self.etcid="STISSPEC1378"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase41(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1378"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase42(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1379"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,0.0,flam)"
        self.subset=True
        self.etcid="STISSPEC1380"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase43(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1380"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.subset=True
        self.etcid="STISSPEC1381"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase44(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1381"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase45(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        self.subset=True
        self.etcid="STISSPEC1382"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase46(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1322"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase47(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1322"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase48(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1323"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase49(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1324"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase50(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1325"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase51(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1099"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase52(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1101"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase53(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1239"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase54(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1240"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase55(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1241"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase57(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x01"
        self.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1242"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase58(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['STISSPEC1341', 'STISSPEC1243']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase59(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1243"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase60(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1254"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase61(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1256"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase62(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1292"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase63(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1294"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase64(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1296"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase65(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1296"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase66(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1298"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase67(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1300"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase68(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        self.subset=False
        self.etcid="STISSPEC1300"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase69(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        self.subset=True
        self.etcid="STISSPEC1329"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase70(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1332"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase71(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1333"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase72(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="STISSPEC1336"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase73(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="STISSPEC1337"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase74(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=True
        self.etcid="STISSPEC1338"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase75(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="STISSPEC1339"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase77(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.subset=True
        self.etcid="['STISSPEC1341', 'STISSPEC1343']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase79(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        self.subset=False
        self.etcid="STISSPEC110506"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase80(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="STISSPEC1344"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase81(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.subset=False
        self.etcid="STISSPEC1344"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase82(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="STISSPEC1345"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase83(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.subset=False
        self.etcid="STISSPEC1345"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase85(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        self.subset=False
        self.etcid="STISSPEC1346"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase86(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        self.subset=False
        self.etcid="STISSPEC1347"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase87(basecase.SpecSourcerateSpecOverlapCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.subset=False
        self.etcid="STISSPEC4422"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:61 - 53 dup =8
#thermback:0 - 0 dup =0
#calcphot:63 - 4 dup =59
#countrate:62 - 3 dup =59
#SpecSourcerateSpec:87 - 6 dup =81
