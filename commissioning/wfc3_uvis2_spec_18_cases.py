from pytools import testutil
import sys
import basecase
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvsp2006.tab:0000', 'uvsp2006.tab:0001', 'uvsp2006.tab:0002', 'uvsp2006.tab:0003', 'uvsp2006.tab:0004', 'uvsp2006.tab:0005', 'uvsp2006.tab:0006', 'uvsp2006.tab:0007', 'uvsp2006.tab:0008', 'uvsp2006.tab:0009', 'uvsp2006.tab:0010', 'uvsp2006.tab:0011', 'uvsp2006.tab:0012', 'uvsp2006.tab:0013', 'uvsp2006.tab:0014', 'uvsp2006.tab:0015', 'uvsp2006.tab:0016', 'uvsp2006.tab:0017', 'uvsp2006.tab:0018', 'uvsp2006.tab:0019', 'uvsp2006.tab:0020', 'uvsp2006.tab:0021', 'uvsp2006.tab:0022', 'uvsp2006.tab:0023', 'uvsp2006.tab:0024', 'uvsp2006.tab:0025', 'uvsp2006.tab:0026', 'uvsp2006.tab:0027', 'uvsp2006.tab:0028', 'uvsp2006.tab:0029', 'uvsp2006.tab:0030', 'uvsp2006.tab:0031', 'uvsp2006.tab:0032', 'uvsp2006.tab:0033', 'uvsp2006.tab:0034', 'uvsp2006.tab:0035', 'uvsp2006.tab:0036', 'uvsp2006.tab:0037', 'uvsp2006.tab:0038', 'uvsp2006.tab:0039', 'uvsp2006.tab:0040', 'uvsp2006.tab:0041', 'uvsp2006.tab:0042', 'uvsp2006.tab:0043', 'uvsp2006.tab:0044', 'uvsp2006.tab:0045', 'uvsp2006.tab:0046', 'uvsp2006.tab:0047', 'uvsp2006.tab:0048', 'uvsp2006.tab:0049', 'uvsp2006.tab:0050', 'uvsp2006.tab:0051', 'uvsp2006.tab:0052', 'uvsp2006.tab:0053', 'uvsp2006.tab:0054', 'uvsp2006.tab:0055', 'uvsp2006.tab:0056', 'uvsp2006.tab:0057', 'uvsp2006.tab:0058', 'uvsp2006.tab:0059', 'uvsp2006.tab:0060', 'uvsp2006.tab:0061', 'uvsp2006.tab:0062', 'uvsp2006.tab:0063', 'uvsp2006.tab:0064', 'uvsp2006.tab:0065', 'uvsp2006.tab:0066', 'uvsp2006.tab:0067', 'uvsp2006.tab:0068', 'uvsp2006.tab:0069', 'uvsp2006.tab:0070', 'uvsp2006.tab:0071', 'uvsp2006.tab:0072', 'uvsp2006.tab:0073', 'uvsp2006.tab:0074', 'uvsp2006.tab:0075', 'uvsp2006.tab:0076', 'uvsp2006.tab:0077', 'uvsp2006.tab:0078', 'uvsp2006.tab:0079', 'uvsp2006.tab:0080', 'uvsp2006.tab:0081', 'uvsp2006.tab:0082', 'uvsp2006.tab:0083', 'uvsp2006.tab:0084', 'uvsp2006.tab:0085', 'uvsp2006.tab:0086', 'uvsp2006.tab:0087', 'uvsp2006.tab:0088', 'uvsp2006.tab:0089', 'uvsp2006.tab:0090', 'uvsp2006.tab:0091', 'uvsp2006.tab:0092', 'uvsp2006.tab:0093', 'uvsp2006.tab:0094', 'uvsp2006.tab:0095', 'uvsp2006.tab:0096', 'uvsp2006.tab:0097', 'uvsp2006.tab:0098', 'uvsp2006.tab:0099', 'uvsp2006.tab:0100', 'uvsp2006.tab:0101', 'uvsp2006.tab:0102', 'uvsp2006.tab:0103', 'uvsp2006.tab:0104', 'uvsp2006.tab:0105', 'uvsp2006.tab:0106', 'uvsp2006.tab:0107', 'uvsp2006.tab:0108', 'uvsp2006.tab:0109', 'uvsp2006.tab:0110', 'uvsp2006.tab:0111', 'uvsp2006.tab:0112', 'uvsp2006.tab:0113', 'uvsp2006.tab:0114', 'uvsp2006.tab:0115', 'uvsp2006.tab:0116', 'uvsp2006.tab:0117', 'uvsp2006.tab:0118', 'uvsp2006.tab:0119', 'uvsp2006.tab:0120', 'uvsp2006.tab:0121', 'uvsp2006.tab:0122', 'uvsp2006.tab:0123', 'uvsp2006.tab:0124', 'uvsp2006.tab:0125', 'uvsp2006.tab:0126', 'uvsp2006.tab:0127', 'uvsp2006.tab:0128', 'uvsp2006.tab:0129', 'uvsp2006.tab:0130', 'uvsp2006.tab:0131', 'uvsp2006.tab:0132', 'uvsp2006.tab:0133', 'uvsp2006.tab:0134', 'uvsp2006.tab:0135', 'uvsp2006.tab:0136', 'uvsp2006.tab:0137', 'uvsp2006.tab:0138', 'uvsp2006.tab:0139', 'uvsp2006.tab:0140', 'uvsp2006.tab:0141', 'uvsp2006.tab:0142', 'uvsp2006.tab:0143', 'uvsp2006.tab:0144', 'uvsp2006.tab:0145', 'uvsp2006.tab:0146', 'uvsp2006.tab:0147', 'uvsp2006.tab:0148', 'uvsp2006.tab:0149']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvsp2006.tab:0000', 'uvsp2006.tab:0001', 'uvsp2006.tab:0002', 'uvsp2006.tab:0003', 'uvsp2006.tab:0004', 'uvsp2006.tab:0005', 'uvsp2006.tab:0006', 'uvsp2006.tab:0007', 'uvsp2006.tab:0008', 'uvsp2006.tab:0009', 'uvsp2006.tab:0010', 'uvsp2006.tab:0011', 'uvsp2006.tab:0012', 'uvsp2006.tab:0013', 'uvsp2006.tab:0014', 'uvsp2006.tab:0015', 'uvsp2006.tab:0016', 'uvsp2006.tab:0017', 'uvsp2006.tab:0018', 'uvsp2006.tab:0019', 'uvsp2006.tab:0020', 'uvsp2006.tab:0021', 'uvsp2006.tab:0022', 'uvsp2006.tab:0023', 'uvsp2006.tab:0024', 'uvsp2006.tab:0025', 'uvsp2006.tab:0026', 'uvsp2006.tab:0027', 'uvsp2006.tab:0028', 'uvsp2006.tab:0029', 'uvsp2006.tab:0030', 'uvsp2006.tab:0031', 'uvsp2006.tab:0032', 'uvsp2006.tab:0033', 'uvsp2006.tab:0034', 'uvsp2006.tab:0035', 'uvsp2006.tab:0036', 'uvsp2006.tab:0037', 'uvsp2006.tab:0038', 'uvsp2006.tab:0039', 'uvsp2006.tab:0040', 'uvsp2006.tab:0041', 'uvsp2006.tab:0042', 'uvsp2006.tab:0043', 'uvsp2006.tab:0044', 'uvsp2006.tab:0045', 'uvsp2006.tab:0046', 'uvsp2006.tab:0047', 'uvsp2006.tab:0048', 'uvsp2006.tab:0049', 'uvsp2006.tab:0050', 'uvsp2006.tab:0051', 'uvsp2006.tab:0052', 'uvsp2006.tab:0053', 'uvsp2006.tab:0054', 'uvsp2006.tab:0055', 'uvsp2006.tab:0056', 'uvsp2006.tab:0057', 'uvsp2006.tab:0058', 'uvsp2006.tab:0059', 'uvsp2006.tab:0060', 'uvsp2006.tab:0061', 'uvsp2006.tab:0062', 'uvsp2006.tab:0063', 'uvsp2006.tab:0064', 'uvsp2006.tab:0065', 'uvsp2006.tab:0066', 'uvsp2006.tab:0067', 'uvsp2006.tab:0068', 'uvsp2006.tab:0069', 'uvsp2006.tab:0070', 'uvsp2006.tab:0071', 'uvsp2006.tab:0072', 'uvsp2006.tab:0073', 'uvsp2006.tab:0074', 'uvsp2006.tab:0075', 'uvsp2006.tab:0076', 'uvsp2006.tab:0077', 'uvsp2006.tab:0078', 'uvsp2006.tab:0079', 'uvsp2006.tab:0080', 'uvsp2006.tab:0081', 'uvsp2006.tab:0082', 'uvsp2006.tab:0083', 'uvsp2006.tab:0084', 'uvsp2006.tab:0085', 'uvsp2006.tab:0086', 'uvsp2006.tab:0087', 'uvsp2006.tab:0088', 'uvsp2006.tab:0089', 'uvsp2006.tab:0090', 'uvsp2006.tab:0091', 'uvsp2006.tab:0092', 'uvsp2006.tab:0093', 'uvsp2006.tab:0094', 'uvsp2006.tab:0095', 'uvsp2006.tab:0096', 'uvsp2006.tab:0097', 'uvsp2006.tab:0098', 'uvsp2006.tab:0099', 'uvsp2006.tab:0100', 'uvsp2006.tab:0101', 'uvsp2006.tab:0102', 'uvsp2006.tab:0103', 'uvsp2006.tab:0104', 'uvsp2006.tab:0105', 'uvsp2006.tab:0106', 'uvsp2006.tab:0107', 'uvsp2006.tab:0108', 'uvsp2006.tab:0109', 'uvsp2006.tab:0110', 'uvsp2006.tab:0111', 'uvsp2006.tab:0112', 'uvsp2006.tab:0113', 'uvsp2006.tab:0114', 'uvsp2006.tab:0115', 'uvsp2006.tab:0116', 'uvsp2006.tab:0117', 'uvsp2006.tab:0118', 'uvsp2006.tab:0119', 'uvsp2006.tab:0120', 'uvsp2006.tab:0121', 'uvsp2006.tab:0122', 'uvsp2006.tab:0123', 'uvsp2006.tab:0124', 'uvsp2006.tab:0125', 'uvsp2006.tab:0126', 'uvsp2006.tab:0127', 'uvsp2006.tab:0128', 'uvsp2006.tab:0129', 'uvsp2006.tab:0130', 'uvsp2006.tab:0131', 'uvsp2006.tab:0132', 'uvsp2006.tab:0133', 'uvsp2006.tab:0134', 'uvsp2006.tab:0135', 'uvsp2006.tab:0136', 'uvsp2006.tab:0137', 'uvsp2006.tab:0138', 'uvsp2006.tab:0139', 'uvsp2006.tab:0140', 'uvsp2006.tab:0141', 'uvsp2006.tab:0142', 'uvsp2006.tab:0143', 'uvsp2006.tab:0144', 'uvsp2006.tab:0145', 'uvsp2006.tab:0146', 'uvsp2006.tab:0147', 'uvsp2006.tab:0148', 'uvsp2006.tab:0149']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.subset=False
        self.etcid="['uvsp2006.tab:0000', 'uvsp2006.tab:0002', 'uvsp2006.tab:0003', 'uvsp2006.tab:0004', 'uvsp2006.tab:0005', 'uvsp2006.tab:0007', 'uvsp2006.tab:0008', 'uvsp2006.tab:0009', 'uvsp2006.tab:0010', 'uvsp2006.tab:0012', 'uvsp2006.tab:0013', 'uvsp2006.tab:0014', 'uvsp2006.tab:0015', 'uvsp2006.tab:0017', 'uvsp2006.tab:0018', 'uvsp2006.tab:0019', 'uvsp2006.tab:0020', 'uvsp2006.tab:0022', 'uvsp2006.tab:0023', 'uvsp2006.tab:0024', 'uvsp2006.tab:0025', 'uvsp2006.tab:0027', 'uvsp2006.tab:0028', 'uvsp2006.tab:0029', 'uvsp2006.tab:0030', 'uvsp2006.tab:0031', 'uvsp2006.tab:0032', 'uvsp2006.tab:0033', 'uvsp2006.tab:0034', 'uvsp2006.tab:0035', 'uvsp2006.tab:0036', 'uvsp2006.tab:0037', 'uvsp2006.tab:0038', 'uvsp2006.tab:0039', 'uvsp2006.tab:0040', 'uvsp2006.tab:0041', 'uvsp2006.tab:0042', 'uvsp2006.tab:0043', 'uvsp2006.tab:0044', 'uvsp2006.tab:0045', 'uvsp2006.tab:0046', 'uvsp2006.tab:0047', 'uvsp2006.tab:0048', 'uvsp2006.tab:0049', 'uvsp2006.tab:0050', 'uvsp2006.tab:0051', 'uvsp2006.tab:0052', 'uvsp2006.tab:0053', 'uvsp2006.tab:0054', 'uvsp2006.tab:0055', 'uvsp2006.tab:0056', 'uvsp2006.tab:0057', 'uvsp2006.tab:0058', 'uvsp2006.tab:0059', 'uvsp2006.tab:0060', 'uvsp2006.tab:0061', 'uvsp2006.tab:0062', 'uvsp2006.tab:0063', 'uvsp2006.tab:0064', 'uvsp2006.tab:0065', 'uvsp2006.tab:0066', 'uvsp2006.tab:0067', 'uvsp2006.tab:0068', 'uvsp2006.tab:0069', 'uvsp2006.tab:0070', 'uvsp2006.tab:0071', 'uvsp2006.tab:0072', 'uvsp2006.tab:0073', 'uvsp2006.tab:0074', 'uvsp2006.tab:0075', 'uvsp2006.tab:0076', 'uvsp2006.tab:0077', 'uvsp2006.tab:0078', 'uvsp2006.tab:0079', 'uvsp2006.tab:0080', 'uvsp2006.tab:0081', 'uvsp2006.tab:0082', 'uvsp2006.tab:0083', 'uvsp2006.tab:0084', 'uvsp2006.tab:0085', 'uvsp2006.tab:0086', 'uvsp2006.tab:0087', 'uvsp2006.tab:0088', 'uvsp2006.tab:0089', 'uvsp2006.tab:0090', 'uvsp2006.tab:0091', 'uvsp2006.tab:0092', 'uvsp2006.tab:0093', 'uvsp2006.tab:0094', 'uvsp2006.tab:0095', 'uvsp2006.tab:0096', 'uvsp2006.tab:0097', 'uvsp2006.tab:0098', 'uvsp2006.tab:0099', 'uvsp2006.tab:0100', 'uvsp2006.tab:0101']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.subset=True
        self.etcid="['uvsp2006.tab:0001', 'uvsp2006.tab:0006', 'uvsp2006.tab:0011', 'uvsp2006.tab:0016', 'uvsp2006.tab:0021', 'uvsp2006.tab:0026']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.subset=False
        self.etcid="['uvsp2006.tab:0102', 'uvsp2006.tab:0103', 'uvsp2006.tab:0104', 'uvsp2006.tab:0105', 'uvsp2006.tab:0106', 'uvsp2006.tab:0107', 'uvsp2006.tab:0108', 'uvsp2006.tab:0109', 'uvsp2006.tab:0110', 'uvsp2006.tab:0111', 'uvsp2006.tab:0112', 'uvsp2006.tab:0113', 'uvsp2006.tab:0114', 'uvsp2006.tab:0115', 'uvsp2006.tab:0116', 'uvsp2006.tab:0117', 'uvsp2006.tab:0118', 'uvsp2006.tab:0119', 'uvsp2006.tab:0120', 'uvsp2006.tab:0121', 'uvsp2006.tab:0122', 'uvsp2006.tab:0123', 'uvsp2006.tab:0124', 'uvsp2006.tab:0125']"
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
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0126"
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
        self.obsmode="wfc3,uvis2,g280"
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
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0128"
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
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0129"
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
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0130"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0131"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvsp2006.tab:0132"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvsp2006.tab:0134"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvsp2006.tab:0135"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvsp2006.tab:0136"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvsp2006.tab:0137"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvsp2006.tab:0138"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvsp2006.tab:0140"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvsp2006.tab:0144"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0146"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0147"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0148"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0149"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="uvsp2006.tab:0150"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="uvsp2006.tab:0150"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.subset=True
        self.etcid="uvsp2006.tab:0150"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0151"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0151"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0151"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0152"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0152"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0152"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0153"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0153"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0153"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0154"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0154"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0154"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0155"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0155"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.subset=True
        self.etcid="uvsp2006.tab:0155"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0156"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0156"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0156"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0157"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvsp2006.tab:0157"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.subset=False
        self.etcid="uvsp2006.tab:0157"
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
