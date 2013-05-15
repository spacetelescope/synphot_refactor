from pytools import testutil
import sys
import basecase
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['uvsp1006.tab:5000', 'uvsp1006.tab:5001', 'uvsp1006.tab:5002', 'uvsp1006.tab:5003', 'uvsp1006.tab:5004', 'uvsp1006.tab:5005', 'uvsp1006.tab:5006', 'uvsp1006.tab:5007', 'uvsp1006.tab:5008', 'uvsp1006.tab:5009', 'uvsp1006.tab:5010', 'uvsp1006.tab:5011', 'uvsp1006.tab:5012', 'uvsp1006.tab:5013', 'uvsp1006.tab:5014', 'uvsp1006.tab:5015', 'uvsp1006.tab:5016', 'uvsp1006.tab:5017', 'uvsp1006.tab:5018', 'uvsp1006.tab:5019', 'uvsp1006.tab:5020', 'uvsp1006.tab:5021', 'uvsp1006.tab:5022', 'uvsp1006.tab:5023', 'uvsp1006.tab:5024', 'uvsp1006.tab:5025', 'uvsp1006.tab:5026', 'uvsp1006.tab:5027', 'uvsp1006.tab:5028', 'uvsp1006.tab:5029', 'uvsp1006.tab:5030', 'uvsp1006.tab:5031', 'uvsp1006.tab:5032', 'uvsp1006.tab:5033', 'uvsp1006.tab:5034', 'uvsp1006.tab:5035', 'uvsp1006.tab:5036', 'uvsp1006.tab:5037', 'uvsp1006.tab:5038', 'uvsp1006.tab:5039', 'uvsp1006.tab:5040', 'uvsp1006.tab:5041', 'uvsp1006.tab:5042', 'uvsp1006.tab:5043', 'uvsp1006.tab:5044', 'uvsp1006.tab:5045', 'uvsp1006.tab:5046', 'uvsp1006.tab:5047', 'uvsp1006.tab:5048', 'uvsp1006.tab:5049', 'uvsp1006.tab:5050', 'uvsp1006.tab:5051', 'uvsp1006.tab:5052', 'uvsp1006.tab:5053', 'uvsp1006.tab:5054', 'uvsp1006.tab:5055', 'uvsp1006.tab:5056', 'uvsp1006.tab:5057', 'uvsp1006.tab:5058', 'uvsp1006.tab:5059', 'uvsp1006.tab:5060', 'uvsp1006.tab:5061', 'uvsp1006.tab:5062', 'uvsp1006.tab:5063', 'uvsp1006.tab:5064', 'uvsp1006.tab:5065', 'uvsp1006.tab:5066', 'uvsp1006.tab:5067', 'uvsp1006.tab:5068', 'uvsp1006.tab:5069', 'uvsp1006.tab:5070', 'uvsp1006.tab:5071', 'uvsp1006.tab:5072', 'uvsp1006.tab:5073', 'uvsp1006.tab:5074', 'uvsp1006.tab:5075', 'uvsp1006.tab:5076', 'uvsp1006.tab:5077', 'uvsp1006.tab:5078', 'uvsp1006.tab:5079', 'uvsp1006.tab:5080', 'uvsp1006.tab:5081', 'uvsp1006.tab:5082', 'uvsp1006.tab:5083', 'uvsp1006.tab:5084', 'uvsp1006.tab:5085', 'uvsp1006.tab:5086', 'uvsp1006.tab:5087', 'uvsp1006.tab:5088', 'uvsp1006.tab:5089', 'uvsp1006.tab:5090', 'uvsp1006.tab:5091', 'uvsp1006.tab:5092', 'uvsp1006.tab:5093', 'uvsp1006.tab:5094', 'uvsp1006.tab:5095', 'uvsp1006.tab:5096', 'uvsp1006.tab:5097', 'uvsp1006.tab:5098', 'uvsp1006.tab:5099', 'uvsp1006.tab:5100', 'uvsp1006.tab:5101', 'uvsp1006.tab:5102', 'uvsp1006.tab:5103', 'uvsp1006.tab:5104', 'uvsp1006.tab:5105', 'uvsp1006.tab:5106', 'uvsp1006.tab:5107', 'uvsp1006.tab:5108', 'uvsp1006.tab:5109', 'uvsp1006.tab:5110', 'uvsp1006.tab:5111', 'uvsp1006.tab:5112', 'uvsp1006.tab:5113', 'uvsp1006.tab:5114', 'uvsp1006.tab:5115', 'uvsp1006.tab:5116', 'uvsp1006.tab:5117', 'uvsp1006.tab:5118', 'uvsp1006.tab:5119', 'uvsp1006.tab:5120', 'uvsp1006.tab:5121', 'uvsp1006.tab:5122', 'uvsp1006.tab:5123', 'uvsp1006.tab:5124', 'uvsp1006.tab:5125', 'uvsp1006.tab:5126', 'uvsp1006.tab:5127', 'uvsp1006.tab:5128', 'uvsp1006.tab:5129', 'uvsp1006.tab:5130', 'uvsp1006.tab:5131', 'uvsp1006.tab:5132', 'uvsp1006.tab:5133', 'uvsp1006.tab:5134', 'uvsp1006.tab:5135', 'uvsp1006.tab:5136', 'uvsp1006.tab:5137', 'uvsp1006.tab:5138', 'uvsp1006.tab:5139', 'uvsp1006.tab:5140', 'uvsp1006.tab:5141', 'uvsp1006.tab:5142', 'uvsp1006.tab:5143', 'uvsp1006.tab:5144', 'uvsp1006.tab:5145', 'uvsp1006.tab:5146', 'uvsp1006.tab:5147', 'uvsp1006.tab:5148', 'uvsp1006.tab:5149']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['uvsp1006.tab:5000', 'uvsp1006.tab:5001', 'uvsp1006.tab:5002', 'uvsp1006.tab:5003', 'uvsp1006.tab:5004', 'uvsp1006.tab:5005', 'uvsp1006.tab:5006', 'uvsp1006.tab:5007', 'uvsp1006.tab:5008', 'uvsp1006.tab:5009', 'uvsp1006.tab:5010', 'uvsp1006.tab:5011', 'uvsp1006.tab:5012', 'uvsp1006.tab:5013', 'uvsp1006.tab:5014', 'uvsp1006.tab:5015', 'uvsp1006.tab:5016', 'uvsp1006.tab:5017', 'uvsp1006.tab:5018', 'uvsp1006.tab:5019', 'uvsp1006.tab:5020', 'uvsp1006.tab:5021', 'uvsp1006.tab:5022', 'uvsp1006.tab:5023', 'uvsp1006.tab:5024', 'uvsp1006.tab:5025', 'uvsp1006.tab:5026', 'uvsp1006.tab:5027', 'uvsp1006.tab:5028', 'uvsp1006.tab:5029', 'uvsp1006.tab:5030', 'uvsp1006.tab:5031', 'uvsp1006.tab:5032', 'uvsp1006.tab:5033', 'uvsp1006.tab:5034', 'uvsp1006.tab:5035', 'uvsp1006.tab:5036', 'uvsp1006.tab:5037', 'uvsp1006.tab:5038', 'uvsp1006.tab:5039', 'uvsp1006.tab:5040', 'uvsp1006.tab:5041', 'uvsp1006.tab:5042', 'uvsp1006.tab:5043', 'uvsp1006.tab:5044', 'uvsp1006.tab:5045', 'uvsp1006.tab:5046', 'uvsp1006.tab:5047', 'uvsp1006.tab:5048', 'uvsp1006.tab:5049', 'uvsp1006.tab:5050', 'uvsp1006.tab:5051', 'uvsp1006.tab:5052', 'uvsp1006.tab:5053', 'uvsp1006.tab:5054', 'uvsp1006.tab:5055', 'uvsp1006.tab:5056', 'uvsp1006.tab:5057', 'uvsp1006.tab:5058', 'uvsp1006.tab:5059', 'uvsp1006.tab:5060', 'uvsp1006.tab:5061', 'uvsp1006.tab:5062', 'uvsp1006.tab:5063', 'uvsp1006.tab:5064', 'uvsp1006.tab:5065', 'uvsp1006.tab:5066', 'uvsp1006.tab:5067', 'uvsp1006.tab:5068', 'uvsp1006.tab:5069', 'uvsp1006.tab:5070', 'uvsp1006.tab:5071', 'uvsp1006.tab:5072', 'uvsp1006.tab:5073', 'uvsp1006.tab:5074', 'uvsp1006.tab:5075', 'uvsp1006.tab:5076', 'uvsp1006.tab:5077', 'uvsp1006.tab:5078', 'uvsp1006.tab:5079', 'uvsp1006.tab:5080', 'uvsp1006.tab:5081', 'uvsp1006.tab:5082', 'uvsp1006.tab:5083', 'uvsp1006.tab:5084', 'uvsp1006.tab:5085', 'uvsp1006.tab:5086', 'uvsp1006.tab:5087', 'uvsp1006.tab:5088', 'uvsp1006.tab:5089', 'uvsp1006.tab:5090', 'uvsp1006.tab:5091', 'uvsp1006.tab:5092', 'uvsp1006.tab:5093', 'uvsp1006.tab:5094', 'uvsp1006.tab:5095', 'uvsp1006.tab:5096', 'uvsp1006.tab:5097', 'uvsp1006.tab:5098', 'uvsp1006.tab:5099', 'uvsp1006.tab:5100', 'uvsp1006.tab:5101', 'uvsp1006.tab:5102', 'uvsp1006.tab:5103', 'uvsp1006.tab:5104', 'uvsp1006.tab:5105', 'uvsp1006.tab:5106', 'uvsp1006.tab:5107', 'uvsp1006.tab:5108', 'uvsp1006.tab:5109', 'uvsp1006.tab:5110', 'uvsp1006.tab:5111', 'uvsp1006.tab:5112', 'uvsp1006.tab:5113', 'uvsp1006.tab:5114', 'uvsp1006.tab:5115', 'uvsp1006.tab:5116', 'uvsp1006.tab:5117', 'uvsp1006.tab:5118', 'uvsp1006.tab:5119', 'uvsp1006.tab:5120', 'uvsp1006.tab:5121', 'uvsp1006.tab:5122', 'uvsp1006.tab:5123', 'uvsp1006.tab:5124', 'uvsp1006.tab:5125', 'uvsp1006.tab:5126', 'uvsp1006.tab:5127', 'uvsp1006.tab:5128', 'uvsp1006.tab:5129', 'uvsp1006.tab:5130', 'uvsp1006.tab:5131', 'uvsp1006.tab:5132', 'uvsp1006.tab:5133', 'uvsp1006.tab:5134', 'uvsp1006.tab:5135', 'uvsp1006.tab:5136', 'uvsp1006.tab:5137', 'uvsp1006.tab:5138', 'uvsp1006.tab:5139', 'uvsp1006.tab:5140', 'uvsp1006.tab:5141', 'uvsp1006.tab:5142', 'uvsp1006.tab:5143', 'uvsp1006.tab:5144', 'uvsp1006.tab:5145', 'uvsp1006.tab:5146', 'uvsp1006.tab:5147', 'uvsp1006.tab:5148', 'uvsp1006.tab:5149']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.subset=True
        self.etcid="['uvsp1006.tab:5000', 'uvsp1006.tab:5002', 'uvsp1006.tab:5003', 'uvsp1006.tab:5004', 'uvsp1006.tab:5005', 'uvsp1006.tab:5007', 'uvsp1006.tab:5008', 'uvsp1006.tab:5009', 'uvsp1006.tab:5010', 'uvsp1006.tab:5012', 'uvsp1006.tab:5013', 'uvsp1006.tab:5014', 'uvsp1006.tab:5015', 'uvsp1006.tab:5017', 'uvsp1006.tab:5018', 'uvsp1006.tab:5019', 'uvsp1006.tab:5020', 'uvsp1006.tab:5022', 'uvsp1006.tab:5023', 'uvsp1006.tab:5024', 'uvsp1006.tab:5025', 'uvsp1006.tab:5027', 'uvsp1006.tab:5028', 'uvsp1006.tab:5029', 'uvsp1006.tab:5030', 'uvsp1006.tab:5031', 'uvsp1006.tab:5032', 'uvsp1006.tab:5033', 'uvsp1006.tab:5034', 'uvsp1006.tab:5035', 'uvsp1006.tab:5036', 'uvsp1006.tab:5037', 'uvsp1006.tab:5038', 'uvsp1006.tab:5039', 'uvsp1006.tab:5040', 'uvsp1006.tab:5041', 'uvsp1006.tab:5042', 'uvsp1006.tab:5043', 'uvsp1006.tab:5044', 'uvsp1006.tab:5045', 'uvsp1006.tab:5046', 'uvsp1006.tab:5047', 'uvsp1006.tab:5048', 'uvsp1006.tab:5049', 'uvsp1006.tab:5050', 'uvsp1006.tab:5051', 'uvsp1006.tab:5052', 'uvsp1006.tab:5053', 'uvsp1006.tab:5054', 'uvsp1006.tab:5055', 'uvsp1006.tab:5056', 'uvsp1006.tab:5057', 'uvsp1006.tab:5058', 'uvsp1006.tab:5059', 'uvsp1006.tab:5060', 'uvsp1006.tab:5061', 'uvsp1006.tab:5062', 'uvsp1006.tab:5063', 'uvsp1006.tab:5064', 'uvsp1006.tab:5065', 'uvsp1006.tab:5066', 'uvsp1006.tab:5067', 'uvsp1006.tab:5068', 'uvsp1006.tab:5069', 'uvsp1006.tab:5070', 'uvsp1006.tab:5071', 'uvsp1006.tab:5072', 'uvsp1006.tab:5073', 'uvsp1006.tab:5074', 'uvsp1006.tab:5075', 'uvsp1006.tab:5076', 'uvsp1006.tab:5077', 'uvsp1006.tab:5078', 'uvsp1006.tab:5079', 'uvsp1006.tab:5080', 'uvsp1006.tab:5081', 'uvsp1006.tab:5082', 'uvsp1006.tab:5083', 'uvsp1006.tab:5084', 'uvsp1006.tab:5085', 'uvsp1006.tab:5086', 'uvsp1006.tab:5087', 'uvsp1006.tab:5088', 'uvsp1006.tab:5089', 'uvsp1006.tab:5090', 'uvsp1006.tab:5091', 'uvsp1006.tab:5092', 'uvsp1006.tab:5093', 'uvsp1006.tab:5094', 'uvsp1006.tab:5095', 'uvsp1006.tab:5096', 'uvsp1006.tab:5097', 'uvsp1006.tab:5098', 'uvsp1006.tab:5099', 'uvsp1006.tab:5100', 'uvsp1006.tab:5101']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.subset=False
        self.etcid="['uvsp1006.tab:5001', 'uvsp1006.tab:5006', 'uvsp1006.tab:5011', 'uvsp1006.tab:5016', 'uvsp1006.tab:5021', 'uvsp1006.tab:5026']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.subset=False
        self.etcid="['uvsp1006.tab:5102', 'uvsp1006.tab:5103', 'uvsp1006.tab:5104', 'uvsp1006.tab:5105', 'uvsp1006.tab:5106', 'uvsp1006.tab:5107', 'uvsp1006.tab:5108', 'uvsp1006.tab:5109', 'uvsp1006.tab:5110', 'uvsp1006.tab:5111', 'uvsp1006.tab:5112', 'uvsp1006.tab:5113', 'uvsp1006.tab:5114', 'uvsp1006.tab:5115', 'uvsp1006.tab:5116', 'uvsp1006.tab:5117', 'uvsp1006.tab:5118', 'uvsp1006.tab:5119', 'uvsp1006.tab:5120', 'uvsp1006.tab:5121', 'uvsp1006.tab:5122', 'uvsp1006.tab:5123', 'uvsp1006.tab:5124', 'uvsp1006.tab:5125']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase127(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5126"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5128"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5129"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5130"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5131"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="uvsp1006.tab:5132"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="uvsp1006.tab:5134"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvsp1006.tab:5135"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="uvsp1006.tab:5136"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvsp1006.tab:5137"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="uvsp1006.tab:5138"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvsp1006.tab:5140"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvsp1006.tab:5144"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.subset=True
        self.etcid="uvsp1006.tab:5146"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5147"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5148"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.subset=True
        self.etcid="uvsp1006.tab:5149"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5150"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5150"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5150"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5151"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5151"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5151"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5152"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5152"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5152"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5153"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5153"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5153"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5154"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5154"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5154"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5155"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5155"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.subset=True
        self.etcid="uvsp1006.tab:5155"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5156"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5156"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5156"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5157"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp1006.tab:5157"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp1006.tab:5157"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:141 - 133 dup =8
#thermback:0 - 0 dup =0
#calcphot:10 - 1 dup =9
#countrate:10 - 1 dup =9
#SpecSourcerateSpec:36 - 1 dup =35
