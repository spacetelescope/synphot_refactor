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
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['uvim1006.tab:5000', 'uvim1006.tab:5001', 'uvim1006.tab:5002', 'uvim1006.tab:5003', 'uvim1006.tab:5004', 'uvim1006.tab:5310', 'uvim1006.tab:5372', 'uvim1006.tab:5434', 'uvim1006.tab:5496', 'uvim1006.tab:5558', 'uvim1006.tab:5620', 'uvim1006.tab:5682', 'uvim1006.tab:5744', 'uvim1006.tab:5806', 'uvim1006.tab:5868', 'uvim1006.tab:5930', 'uvim1006.tab:5992', 'uvim1006.tab:6054', 'uvim1006.tab:6116', 'uvim1006.tab:6178', 'uvim1006.tab:6240', 'uvim1006.tab:6302', 'uvim1006.tab:6364', 'uvim1006.tab:6426', 'uvim1006.tab:6488', 'uvim1006.tab:6550', 'uvim1006.tab:6612', 'uvim1006.tab:6674', 'uvim1006.tab:6736', 'uvim1006.tab:6798', 'uvim1006.tab:6860', 'uvim1006.tab:6922', 'uvim1006.tab:6984', 'uvim1006.tab:7046', 'uvim1006.tab:7108', 'uvim1006.tab:7170']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5000', 'uvim1006.tab:5001', 'uvim1006.tab:5002', 'uvim1006.tab:5003', 'uvim1006.tab:5004', 'uvim1006.tab:5310', 'uvim1006.tab:5372', 'uvim1006.tab:5434', 'uvim1006.tab:5496', 'uvim1006.tab:5558', 'uvim1006.tab:5620', 'uvim1006.tab:5682', 'uvim1006.tab:5744', 'uvim1006.tab:5806', 'uvim1006.tab:5868', 'uvim1006.tab:5930', 'uvim1006.tab:5992', 'uvim1006.tab:6054', 'uvim1006.tab:6116', 'uvim1006.tab:6178', 'uvim1006.tab:6240', 'uvim1006.tab:6302', 'uvim1006.tab:6364', 'uvim1006.tab:6426', 'uvim1006.tab:6488', 'uvim1006.tab:6550', 'uvim1006.tab:6612', 'uvim1006.tab:6674', 'uvim1006.tab:6736', 'uvim1006.tab:6798', 'uvim1006.tab:6860', 'uvim1006.tab:6922', 'uvim1006.tab:6984', 'uvim1006.tab:7046', 'uvim1006.tab:7108', 'uvim1006.tab:7170']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5000', 'uvim1006.tab:5002', 'uvim1006.tab:5003', 'uvim1006.tab:5004', 'uvim1006.tab:5310', 'uvim1006.tab:5372', 'uvim1006.tab:5434', 'uvim1006.tab:5496', 'uvim1006.tab:5558', 'uvim1006.tab:5620', 'uvim1006.tab:5682', 'uvim1006.tab:5744', 'uvim1006.tab:5806', 'uvim1006.tab:5868', 'uvim1006.tab:5930', 'uvim1006.tab:5992', 'uvim1006.tab:6054', 'uvim1006.tab:6116', 'uvim1006.tab:6178', 'uvim1006.tab:6240', 'uvim1006.tab:6302', 'uvim1006.tab:6364', 'uvim1006.tab:6426', 'uvim1006.tab:6488', 'uvim1006.tab:6550', 'uvim1006.tab:6612', 'uvim1006.tab:6674', 'uvim1006.tab:6736', 'uvim1006.tab:6798', 'uvim1006.tab:6860', 'uvim1006.tab:6922', 'uvim1006.tab:6984', 'uvim1006.tab:7046']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5000', 'uvim1006.tab:5002', 'uvim1006.tab:5003', 'uvim1006.tab:5004', 'uvim1006.tab:5310', 'uvim1006.tab:5372', 'uvim1006.tab:5434', 'uvim1006.tab:5496', 'uvim1006.tab:5558', 'uvim1006.tab:5620', 'uvim1006.tab:5682', 'uvim1006.tab:5744', 'uvim1006.tab:5806', 'uvim1006.tab:5868', 'uvim1006.tab:5930', 'uvim1006.tab:5992', 'uvim1006.tab:6054', 'uvim1006.tab:6116', 'uvim1006.tab:6178', 'uvim1006.tab:6240', 'uvim1006.tab:6302', 'uvim1006.tab:6364', 'uvim1006.tab:6426', 'uvim1006.tab:6488', 'uvim1006.tab:6550', 'uvim1006.tab:6612', 'uvim1006.tab:6674', 'uvim1006.tab:6736', 'uvim1006.tab:6798', 'uvim1006.tab:6860', 'uvim1006.tab:6922', 'uvim1006.tab:6984', 'uvim1006.tab:7046']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=True
        self.etcid="['uvim1006.tab:5001', 'uvim1006.tab:7108', 'uvim1006.tab:7170']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5001', 'uvim1006.tab:7108', 'uvim1006.tab:7170']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5005', 'uvim1006.tab:5006', 'uvim1006.tab:5007', 'uvim1006.tab:5008', 'uvim1006.tab:5009', 'uvim1006.tab:5311', 'uvim1006.tab:5373', 'uvim1006.tab:5435', 'uvim1006.tab:5497', 'uvim1006.tab:5559', 'uvim1006.tab:5621', 'uvim1006.tab:5683', 'uvim1006.tab:5745', 'uvim1006.tab:5807', 'uvim1006.tab:5869', 'uvim1006.tab:5931', 'uvim1006.tab:5993', 'uvim1006.tab:6055', 'uvim1006.tab:6117', 'uvim1006.tab:6179', 'uvim1006.tab:6241', 'uvim1006.tab:6303', 'uvim1006.tab:6365', 'uvim1006.tab:6427', 'uvim1006.tab:6489', 'uvim1006.tab:6551', 'uvim1006.tab:6613', 'uvim1006.tab:6675', 'uvim1006.tab:6737', 'uvim1006.tab:6799', 'uvim1006.tab:6861', 'uvim1006.tab:6923', 'uvim1006.tab:6985', 'uvim1006.tab:7047', 'uvim1006.tab:7109', 'uvim1006.tab:7171']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5005', 'uvim1006.tab:5006', 'uvim1006.tab:5007', 'uvim1006.tab:5008', 'uvim1006.tab:5009', 'uvim1006.tab:5311', 'uvim1006.tab:5373', 'uvim1006.tab:5435', 'uvim1006.tab:5497', 'uvim1006.tab:5559', 'uvim1006.tab:5621', 'uvim1006.tab:5683', 'uvim1006.tab:5745', 'uvim1006.tab:5807', 'uvim1006.tab:5869', 'uvim1006.tab:5931', 'uvim1006.tab:5993', 'uvim1006.tab:6055', 'uvim1006.tab:6117', 'uvim1006.tab:6179', 'uvim1006.tab:6241', 'uvim1006.tab:6303', 'uvim1006.tab:6365', 'uvim1006.tab:6427', 'uvim1006.tab:6489', 'uvim1006.tab:6551', 'uvim1006.tab:6613', 'uvim1006.tab:6675', 'uvim1006.tab:6737', 'uvim1006.tab:6799', 'uvim1006.tab:6861', 'uvim1006.tab:6923', 'uvim1006.tab:6985', 'uvim1006.tab:7047', 'uvim1006.tab:7109', 'uvim1006.tab:7171']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5005', 'uvim1006.tab:5007', 'uvim1006.tab:5008', 'uvim1006.tab:5009', 'uvim1006.tab:5311', 'uvim1006.tab:5373', 'uvim1006.tab:5435', 'uvim1006.tab:5497', 'uvim1006.tab:5559', 'uvim1006.tab:5621', 'uvim1006.tab:5683', 'uvim1006.tab:5745', 'uvim1006.tab:5807', 'uvim1006.tab:5869', 'uvim1006.tab:5931', 'uvim1006.tab:5993', 'uvim1006.tab:6055', 'uvim1006.tab:6117', 'uvim1006.tab:6179', 'uvim1006.tab:6241', 'uvim1006.tab:6303', 'uvim1006.tab:6365', 'uvim1006.tab:6427', 'uvim1006.tab:6489', 'uvim1006.tab:6551', 'uvim1006.tab:6613', 'uvim1006.tab:6675', 'uvim1006.tab:6737', 'uvim1006.tab:6799', 'uvim1006.tab:6861', 'uvim1006.tab:6923', 'uvim1006.tab:6985', 'uvim1006.tab:7047']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5005', 'uvim1006.tab:5007', 'uvim1006.tab:5008', 'uvim1006.tab:5009', 'uvim1006.tab:5311', 'uvim1006.tab:5373', 'uvim1006.tab:5435', 'uvim1006.tab:5497', 'uvim1006.tab:5559', 'uvim1006.tab:5621', 'uvim1006.tab:5683', 'uvim1006.tab:5745', 'uvim1006.tab:5807', 'uvim1006.tab:5869', 'uvim1006.tab:5931', 'uvim1006.tab:5993', 'uvim1006.tab:6055', 'uvim1006.tab:6117', 'uvim1006.tab:6179', 'uvim1006.tab:6241', 'uvim1006.tab:6303', 'uvim1006.tab:6365', 'uvim1006.tab:6427', 'uvim1006.tab:6489', 'uvim1006.tab:6551', 'uvim1006.tab:6613', 'uvim1006.tab:6675', 'uvim1006.tab:6737', 'uvim1006.tab:6799', 'uvim1006.tab:6861', 'uvim1006.tab:6923', 'uvim1006.tab:6985', 'uvim1006.tab:7047']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5006', 'uvim1006.tab:7109', 'uvim1006.tab:7171']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5006', 'uvim1006.tab:7109', 'uvim1006.tab:7171']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5010', 'uvim1006.tab:5011', 'uvim1006.tab:5012', 'uvim1006.tab:5013', 'uvim1006.tab:5014', 'uvim1006.tab:5312', 'uvim1006.tab:5374', 'uvim1006.tab:5436', 'uvim1006.tab:5498', 'uvim1006.tab:5560', 'uvim1006.tab:5622', 'uvim1006.tab:5684', 'uvim1006.tab:5746', 'uvim1006.tab:5808', 'uvim1006.tab:5870', 'uvim1006.tab:5932', 'uvim1006.tab:5994', 'uvim1006.tab:6056', 'uvim1006.tab:6118', 'uvim1006.tab:6180', 'uvim1006.tab:6242', 'uvim1006.tab:6304', 'uvim1006.tab:6366', 'uvim1006.tab:6428', 'uvim1006.tab:6490', 'uvim1006.tab:6552', 'uvim1006.tab:6614', 'uvim1006.tab:6676', 'uvim1006.tab:6738', 'uvim1006.tab:6800', 'uvim1006.tab:6862', 'uvim1006.tab:6924', 'uvim1006.tab:6986', 'uvim1006.tab:7048', 'uvim1006.tab:7110', 'uvim1006.tab:7172', 'uvim1006.tab:7369']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5010', 'uvim1006.tab:5011', 'uvim1006.tab:5012', 'uvim1006.tab:5013', 'uvim1006.tab:5014', 'uvim1006.tab:5312', 'uvim1006.tab:5374', 'uvim1006.tab:5436', 'uvim1006.tab:5498', 'uvim1006.tab:5560', 'uvim1006.tab:5622', 'uvim1006.tab:5684', 'uvim1006.tab:5746', 'uvim1006.tab:5808', 'uvim1006.tab:5870', 'uvim1006.tab:5932', 'uvim1006.tab:5994', 'uvim1006.tab:6056', 'uvim1006.tab:6118', 'uvim1006.tab:6180', 'uvim1006.tab:6242', 'uvim1006.tab:6304', 'uvim1006.tab:6366', 'uvim1006.tab:6428', 'uvim1006.tab:6490', 'uvim1006.tab:6552', 'uvim1006.tab:6614', 'uvim1006.tab:6676', 'uvim1006.tab:6738', 'uvim1006.tab:6800', 'uvim1006.tab:6862', 'uvim1006.tab:6924', 'uvim1006.tab:6986', 'uvim1006.tab:7048', 'uvim1006.tab:7110', 'uvim1006.tab:7172', 'uvim1006.tab:7369']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5010', 'uvim1006.tab:5012', 'uvim1006.tab:5013', 'uvim1006.tab:5014', 'uvim1006.tab:5312', 'uvim1006.tab:5374', 'uvim1006.tab:5436', 'uvim1006.tab:5498', 'uvim1006.tab:5560', 'uvim1006.tab:5622', 'uvim1006.tab:5684', 'uvim1006.tab:5746', 'uvim1006.tab:5808', 'uvim1006.tab:5870', 'uvim1006.tab:5932', 'uvim1006.tab:5994', 'uvim1006.tab:6056', 'uvim1006.tab:6118', 'uvim1006.tab:6180', 'uvim1006.tab:6242', 'uvim1006.tab:6304', 'uvim1006.tab:6366', 'uvim1006.tab:6428', 'uvim1006.tab:6490', 'uvim1006.tab:6552', 'uvim1006.tab:6614', 'uvim1006.tab:6676', 'uvim1006.tab:6738', 'uvim1006.tab:6800', 'uvim1006.tab:6862', 'uvim1006.tab:6924', 'uvim1006.tab:6986', 'uvim1006.tab:7048']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5010', 'uvim1006.tab:5012', 'uvim1006.tab:5013', 'uvim1006.tab:5014', 'uvim1006.tab:5312', 'uvim1006.tab:5374', 'uvim1006.tab:5436', 'uvim1006.tab:5498', 'uvim1006.tab:5560', 'uvim1006.tab:5622', 'uvim1006.tab:5684', 'uvim1006.tab:5746', 'uvim1006.tab:5808', 'uvim1006.tab:5870', 'uvim1006.tab:5932', 'uvim1006.tab:5994', 'uvim1006.tab:6056', 'uvim1006.tab:6118', 'uvim1006.tab:6180', 'uvim1006.tab:6242', 'uvim1006.tab:6304', 'uvim1006.tab:6366', 'uvim1006.tab:6428', 'uvim1006.tab:6490', 'uvim1006.tab:6552', 'uvim1006.tab:6614', 'uvim1006.tab:6676', 'uvim1006.tab:6738', 'uvim1006.tab:6800', 'uvim1006.tab:6862', 'uvim1006.tab:6924', 'uvim1006.tab:6986', 'uvim1006.tab:7048']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5011', 'uvim1006.tab:7110', 'uvim1006.tab:7172']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5011', 'uvim1006.tab:7110', 'uvim1006.tab:7172']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5015', 'uvim1006.tab:5016', 'uvim1006.tab:5017', 'uvim1006.tab:5018', 'uvim1006.tab:5019', 'uvim1006.tab:5313', 'uvim1006.tab:5375', 'uvim1006.tab:5437', 'uvim1006.tab:5499', 'uvim1006.tab:5561', 'uvim1006.tab:5623', 'uvim1006.tab:5685', 'uvim1006.tab:5747', 'uvim1006.tab:5809', 'uvim1006.tab:5871', 'uvim1006.tab:5933', 'uvim1006.tab:5995', 'uvim1006.tab:6057', 'uvim1006.tab:6119', 'uvim1006.tab:6181', 'uvim1006.tab:6243', 'uvim1006.tab:6305', 'uvim1006.tab:6367', 'uvim1006.tab:6429', 'uvim1006.tab:6491', 'uvim1006.tab:6553', 'uvim1006.tab:6615', 'uvim1006.tab:6677', 'uvim1006.tab:6739', 'uvim1006.tab:6801', 'uvim1006.tab:6863', 'uvim1006.tab:6925', 'uvim1006.tab:6987', 'uvim1006.tab:7049', 'uvim1006.tab:7111', 'uvim1006.tab:7173']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5015', 'uvim1006.tab:5016', 'uvim1006.tab:5017', 'uvim1006.tab:5018', 'uvim1006.tab:5019', 'uvim1006.tab:5313', 'uvim1006.tab:5375', 'uvim1006.tab:5437', 'uvim1006.tab:5499', 'uvim1006.tab:5561', 'uvim1006.tab:5623', 'uvim1006.tab:5685', 'uvim1006.tab:5747', 'uvim1006.tab:5809', 'uvim1006.tab:5871', 'uvim1006.tab:5933', 'uvim1006.tab:5995', 'uvim1006.tab:6057', 'uvim1006.tab:6119', 'uvim1006.tab:6181', 'uvim1006.tab:6243', 'uvim1006.tab:6305', 'uvim1006.tab:6367', 'uvim1006.tab:6429', 'uvim1006.tab:6491', 'uvim1006.tab:6553', 'uvim1006.tab:6615', 'uvim1006.tab:6677', 'uvim1006.tab:6739', 'uvim1006.tab:6801', 'uvim1006.tab:6863', 'uvim1006.tab:6925', 'uvim1006.tab:6987', 'uvim1006.tab:7049', 'uvim1006.tab:7111', 'uvim1006.tab:7173']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5015', 'uvim1006.tab:5017', 'uvim1006.tab:5018', 'uvim1006.tab:5019', 'uvim1006.tab:5313', 'uvim1006.tab:5375', 'uvim1006.tab:5437', 'uvim1006.tab:5499', 'uvim1006.tab:5561', 'uvim1006.tab:5623', 'uvim1006.tab:5685', 'uvim1006.tab:5747', 'uvim1006.tab:5809', 'uvim1006.tab:5871', 'uvim1006.tab:5933', 'uvim1006.tab:5995', 'uvim1006.tab:6057', 'uvim1006.tab:6119', 'uvim1006.tab:6181', 'uvim1006.tab:6243', 'uvim1006.tab:6305', 'uvim1006.tab:6367', 'uvim1006.tab:6429', 'uvim1006.tab:6491', 'uvim1006.tab:6553', 'uvim1006.tab:6615', 'uvim1006.tab:6677', 'uvim1006.tab:6739', 'uvim1006.tab:6801', 'uvim1006.tab:6863', 'uvim1006.tab:6925', 'uvim1006.tab:6987', 'uvim1006.tab:7049']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5015', 'uvim1006.tab:5017', 'uvim1006.tab:5018', 'uvim1006.tab:5019', 'uvim1006.tab:5313', 'uvim1006.tab:5375', 'uvim1006.tab:5437', 'uvim1006.tab:5499', 'uvim1006.tab:5561', 'uvim1006.tab:5623', 'uvim1006.tab:5685', 'uvim1006.tab:5747', 'uvim1006.tab:5809', 'uvim1006.tab:5871', 'uvim1006.tab:5933', 'uvim1006.tab:5995', 'uvim1006.tab:6057', 'uvim1006.tab:6119', 'uvim1006.tab:6181', 'uvim1006.tab:6243', 'uvim1006.tab:6305', 'uvim1006.tab:6367', 'uvim1006.tab:6429', 'uvim1006.tab:6491', 'uvim1006.tab:6553', 'uvim1006.tab:6615', 'uvim1006.tab:6677', 'uvim1006.tab:6739', 'uvim1006.tab:6801', 'uvim1006.tab:6863', 'uvim1006.tab:6925', 'uvim1006.tab:6987', 'uvim1006.tab:7049']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5016', 'uvim1006.tab:7111', 'uvim1006.tab:7173']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5016', 'uvim1006.tab:7111', 'uvim1006.tab:7173']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5020', 'uvim1006.tab:5021', 'uvim1006.tab:5022', 'uvim1006.tab:5023', 'uvim1006.tab:5024', 'uvim1006.tab:5314', 'uvim1006.tab:5376', 'uvim1006.tab:5438', 'uvim1006.tab:5500', 'uvim1006.tab:5562', 'uvim1006.tab:5624', 'uvim1006.tab:5686', 'uvim1006.tab:5748', 'uvim1006.tab:5810', 'uvim1006.tab:5872', 'uvim1006.tab:5934', 'uvim1006.tab:5996', 'uvim1006.tab:6058', 'uvim1006.tab:6120', 'uvim1006.tab:6182', 'uvim1006.tab:6244', 'uvim1006.tab:6306', 'uvim1006.tab:6368', 'uvim1006.tab:6430', 'uvim1006.tab:6492', 'uvim1006.tab:6554', 'uvim1006.tab:6616', 'uvim1006.tab:6678', 'uvim1006.tab:6740', 'uvim1006.tab:6802', 'uvim1006.tab:6864', 'uvim1006.tab:6926', 'uvim1006.tab:6988', 'uvim1006.tab:7050', 'uvim1006.tab:7112', 'uvim1006.tab:7174']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5020', 'uvim1006.tab:5021', 'uvim1006.tab:5022', 'uvim1006.tab:5023', 'uvim1006.tab:5024', 'uvim1006.tab:5314', 'uvim1006.tab:5376', 'uvim1006.tab:5438', 'uvim1006.tab:5500', 'uvim1006.tab:5562', 'uvim1006.tab:5624', 'uvim1006.tab:5686', 'uvim1006.tab:5748', 'uvim1006.tab:5810', 'uvim1006.tab:5872', 'uvim1006.tab:5934', 'uvim1006.tab:5996', 'uvim1006.tab:6058', 'uvim1006.tab:6120', 'uvim1006.tab:6182', 'uvim1006.tab:6244', 'uvim1006.tab:6306', 'uvim1006.tab:6368', 'uvim1006.tab:6430', 'uvim1006.tab:6492', 'uvim1006.tab:6554', 'uvim1006.tab:6616', 'uvim1006.tab:6678', 'uvim1006.tab:6740', 'uvim1006.tab:6802', 'uvim1006.tab:6864', 'uvim1006.tab:6926', 'uvim1006.tab:6988', 'uvim1006.tab:7050', 'uvim1006.tab:7112', 'uvim1006.tab:7174']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5020', 'uvim1006.tab:5022', 'uvim1006.tab:5023', 'uvim1006.tab:5024', 'uvim1006.tab:5314', 'uvim1006.tab:5376', 'uvim1006.tab:5438', 'uvim1006.tab:5500', 'uvim1006.tab:5562', 'uvim1006.tab:5624', 'uvim1006.tab:5686', 'uvim1006.tab:5748', 'uvim1006.tab:5810', 'uvim1006.tab:5872', 'uvim1006.tab:5934', 'uvim1006.tab:5996', 'uvim1006.tab:6058', 'uvim1006.tab:6120', 'uvim1006.tab:6182', 'uvim1006.tab:6244', 'uvim1006.tab:6306', 'uvim1006.tab:6368', 'uvim1006.tab:6430', 'uvim1006.tab:6492', 'uvim1006.tab:6554', 'uvim1006.tab:6616', 'uvim1006.tab:6678', 'uvim1006.tab:6740', 'uvim1006.tab:6802', 'uvim1006.tab:6864', 'uvim1006.tab:6926', 'uvim1006.tab:6988', 'uvim1006.tab:7050']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5020', 'uvim1006.tab:5022', 'uvim1006.tab:5023', 'uvim1006.tab:5024', 'uvim1006.tab:5314', 'uvim1006.tab:5376', 'uvim1006.tab:5438', 'uvim1006.tab:5500', 'uvim1006.tab:5562', 'uvim1006.tab:5624', 'uvim1006.tab:5686', 'uvim1006.tab:5748', 'uvim1006.tab:5810', 'uvim1006.tab:5872', 'uvim1006.tab:5934', 'uvim1006.tab:5996', 'uvim1006.tab:6058', 'uvim1006.tab:6120', 'uvim1006.tab:6182', 'uvim1006.tab:6244', 'uvim1006.tab:6306', 'uvim1006.tab:6368', 'uvim1006.tab:6430', 'uvim1006.tab:6492', 'uvim1006.tab:6554', 'uvim1006.tab:6616', 'uvim1006.tab:6678', 'uvim1006.tab:6740', 'uvim1006.tab:6802', 'uvim1006.tab:6864', 'uvim1006.tab:6926', 'uvim1006.tab:6988', 'uvim1006.tab:7050']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5021', 'uvim1006.tab:7112', 'uvim1006.tab:7174']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5021', 'uvim1006.tab:7112', 'uvim1006.tab:7174']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5025', 'uvim1006.tab:5026', 'uvim1006.tab:5027', 'uvim1006.tab:5028', 'uvim1006.tab:5029', 'uvim1006.tab:5315', 'uvim1006.tab:5377', 'uvim1006.tab:5439', 'uvim1006.tab:5501', 'uvim1006.tab:5563', 'uvim1006.tab:5625', 'uvim1006.tab:5687', 'uvim1006.tab:5749', 'uvim1006.tab:5811', 'uvim1006.tab:5873', 'uvim1006.tab:5935', 'uvim1006.tab:5997', 'uvim1006.tab:6059', 'uvim1006.tab:6121', 'uvim1006.tab:6183', 'uvim1006.tab:6245', 'uvim1006.tab:6307', 'uvim1006.tab:6369', 'uvim1006.tab:6431', 'uvim1006.tab:6493', 'uvim1006.tab:6555', 'uvim1006.tab:6617', 'uvim1006.tab:6679', 'uvim1006.tab:6741', 'uvim1006.tab:6803', 'uvim1006.tab:6865', 'uvim1006.tab:6927', 'uvim1006.tab:6989', 'uvim1006.tab:7051', 'uvim1006.tab:7113', 'uvim1006.tab:7175']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5025', 'uvim1006.tab:5026', 'uvim1006.tab:5027', 'uvim1006.tab:5028', 'uvim1006.tab:5029', 'uvim1006.tab:5315', 'uvim1006.tab:5377', 'uvim1006.tab:5439', 'uvim1006.tab:5501', 'uvim1006.tab:5563', 'uvim1006.tab:5625', 'uvim1006.tab:5687', 'uvim1006.tab:5749', 'uvim1006.tab:5811', 'uvim1006.tab:5873', 'uvim1006.tab:5935', 'uvim1006.tab:5997', 'uvim1006.tab:6059', 'uvim1006.tab:6121', 'uvim1006.tab:6183', 'uvim1006.tab:6245', 'uvim1006.tab:6307', 'uvim1006.tab:6369', 'uvim1006.tab:6431', 'uvim1006.tab:6493', 'uvim1006.tab:6555', 'uvim1006.tab:6617', 'uvim1006.tab:6679', 'uvim1006.tab:6741', 'uvim1006.tab:6803', 'uvim1006.tab:6865', 'uvim1006.tab:6927', 'uvim1006.tab:6989', 'uvim1006.tab:7051', 'uvim1006.tab:7113', 'uvim1006.tab:7175']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5025', 'uvim1006.tab:5027', 'uvim1006.tab:5028', 'uvim1006.tab:5029', 'uvim1006.tab:5315', 'uvim1006.tab:5377', 'uvim1006.tab:5439', 'uvim1006.tab:5501', 'uvim1006.tab:5563', 'uvim1006.tab:5625', 'uvim1006.tab:5687', 'uvim1006.tab:5749', 'uvim1006.tab:5811', 'uvim1006.tab:5873', 'uvim1006.tab:5935', 'uvim1006.tab:5997', 'uvim1006.tab:6059', 'uvim1006.tab:6121', 'uvim1006.tab:6183', 'uvim1006.tab:6245', 'uvim1006.tab:6307', 'uvim1006.tab:6369', 'uvim1006.tab:6431', 'uvim1006.tab:6493', 'uvim1006.tab:6555', 'uvim1006.tab:6617', 'uvim1006.tab:6679', 'uvim1006.tab:6741', 'uvim1006.tab:6803', 'uvim1006.tab:6865', 'uvim1006.tab:6927', 'uvim1006.tab:6989', 'uvim1006.tab:7051']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5025', 'uvim1006.tab:5027', 'uvim1006.tab:5028', 'uvim1006.tab:5029', 'uvim1006.tab:5315', 'uvim1006.tab:5377', 'uvim1006.tab:5439', 'uvim1006.tab:5501', 'uvim1006.tab:5563', 'uvim1006.tab:5625', 'uvim1006.tab:5687', 'uvim1006.tab:5749', 'uvim1006.tab:5811', 'uvim1006.tab:5873', 'uvim1006.tab:5935', 'uvim1006.tab:5997', 'uvim1006.tab:6059', 'uvim1006.tab:6121', 'uvim1006.tab:6183', 'uvim1006.tab:6245', 'uvim1006.tab:6307', 'uvim1006.tab:6369', 'uvim1006.tab:6431', 'uvim1006.tab:6493', 'uvim1006.tab:6555', 'uvim1006.tab:6617', 'uvim1006.tab:6679', 'uvim1006.tab:6741', 'uvim1006.tab:6803', 'uvim1006.tab:6865', 'uvim1006.tab:6927', 'uvim1006.tab:6989', 'uvim1006.tab:7051']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5026', 'uvim1006.tab:7113', 'uvim1006.tab:7175']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5026', 'uvim1006.tab:7113', 'uvim1006.tab:7175']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5030', 'uvim1006.tab:5031', 'uvim1006.tab:5032', 'uvim1006.tab:5033', 'uvim1006.tab:5034', 'uvim1006.tab:5316', 'uvim1006.tab:5378', 'uvim1006.tab:5440', 'uvim1006.tab:5502', 'uvim1006.tab:5564', 'uvim1006.tab:5626', 'uvim1006.tab:5688', 'uvim1006.tab:5750', 'uvim1006.tab:5812', 'uvim1006.tab:5874', 'uvim1006.tab:5936', 'uvim1006.tab:5998', 'uvim1006.tab:6060', 'uvim1006.tab:6122', 'uvim1006.tab:6184', 'uvim1006.tab:6246', 'uvim1006.tab:6308', 'uvim1006.tab:6370', 'uvim1006.tab:6432', 'uvim1006.tab:6494', 'uvim1006.tab:6556', 'uvim1006.tab:6618', 'uvim1006.tab:6680', 'uvim1006.tab:6742', 'uvim1006.tab:6804', 'uvim1006.tab:6866', 'uvim1006.tab:6928', 'uvim1006.tab:6990', 'uvim1006.tab:7052', 'uvim1006.tab:7114', 'uvim1006.tab:7176']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5030', 'uvim1006.tab:5031', 'uvim1006.tab:5032', 'uvim1006.tab:5033', 'uvim1006.tab:5034', 'uvim1006.tab:5316', 'uvim1006.tab:5378', 'uvim1006.tab:5440', 'uvim1006.tab:5502', 'uvim1006.tab:5564', 'uvim1006.tab:5626', 'uvim1006.tab:5688', 'uvim1006.tab:5750', 'uvim1006.tab:5812', 'uvim1006.tab:5874', 'uvim1006.tab:5936', 'uvim1006.tab:5998', 'uvim1006.tab:6060', 'uvim1006.tab:6122', 'uvim1006.tab:6184', 'uvim1006.tab:6246', 'uvim1006.tab:6308', 'uvim1006.tab:6370', 'uvim1006.tab:6432', 'uvim1006.tab:6494', 'uvim1006.tab:6556', 'uvim1006.tab:6618', 'uvim1006.tab:6680', 'uvim1006.tab:6742', 'uvim1006.tab:6804', 'uvim1006.tab:6866', 'uvim1006.tab:6928', 'uvim1006.tab:6990', 'uvim1006.tab:7052', 'uvim1006.tab:7114', 'uvim1006.tab:7176']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5030', 'uvim1006.tab:5032', 'uvim1006.tab:5033', 'uvim1006.tab:5034', 'uvim1006.tab:5316', 'uvim1006.tab:5378', 'uvim1006.tab:5440', 'uvim1006.tab:5502', 'uvim1006.tab:5564', 'uvim1006.tab:5626', 'uvim1006.tab:5688', 'uvim1006.tab:5750', 'uvim1006.tab:5812', 'uvim1006.tab:5874', 'uvim1006.tab:5936', 'uvim1006.tab:5998', 'uvim1006.tab:6060', 'uvim1006.tab:6122', 'uvim1006.tab:6184', 'uvim1006.tab:6246', 'uvim1006.tab:6308', 'uvim1006.tab:6370', 'uvim1006.tab:6432', 'uvim1006.tab:6494', 'uvim1006.tab:6556', 'uvim1006.tab:6618', 'uvim1006.tab:6680', 'uvim1006.tab:6742', 'uvim1006.tab:6804', 'uvim1006.tab:6866', 'uvim1006.tab:6928', 'uvim1006.tab:6990', 'uvim1006.tab:7052']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5030', 'uvim1006.tab:5032', 'uvim1006.tab:5033', 'uvim1006.tab:5034', 'uvim1006.tab:5316', 'uvim1006.tab:5378', 'uvim1006.tab:5440', 'uvim1006.tab:5502', 'uvim1006.tab:5564', 'uvim1006.tab:5626', 'uvim1006.tab:5688', 'uvim1006.tab:5750', 'uvim1006.tab:5812', 'uvim1006.tab:5874', 'uvim1006.tab:5936', 'uvim1006.tab:5998', 'uvim1006.tab:6060', 'uvim1006.tab:6122', 'uvim1006.tab:6184', 'uvim1006.tab:6246', 'uvim1006.tab:6308', 'uvim1006.tab:6370', 'uvim1006.tab:6432', 'uvim1006.tab:6494', 'uvim1006.tab:6556', 'uvim1006.tab:6618', 'uvim1006.tab:6680', 'uvim1006.tab:6742', 'uvim1006.tab:6804', 'uvim1006.tab:6866', 'uvim1006.tab:6928', 'uvim1006.tab:6990', 'uvim1006.tab:7052']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5031', 'uvim1006.tab:7114', 'uvim1006.tab:7176']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5031', 'uvim1006.tab:7114', 'uvim1006.tab:7176']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5035', 'uvim1006.tab:5036', 'uvim1006.tab:5037', 'uvim1006.tab:5038', 'uvim1006.tab:5039', 'uvim1006.tab:5317', 'uvim1006.tab:5379', 'uvim1006.tab:5441', 'uvim1006.tab:5503', 'uvim1006.tab:5565', 'uvim1006.tab:5627', 'uvim1006.tab:5689', 'uvim1006.tab:5751', 'uvim1006.tab:5813', 'uvim1006.tab:5875', 'uvim1006.tab:5937', 'uvim1006.tab:5999', 'uvim1006.tab:6061', 'uvim1006.tab:6123', 'uvim1006.tab:6185', 'uvim1006.tab:6247', 'uvim1006.tab:6309', 'uvim1006.tab:6371', 'uvim1006.tab:6433', 'uvim1006.tab:6495', 'uvim1006.tab:6557', 'uvim1006.tab:6619', 'uvim1006.tab:6681', 'uvim1006.tab:6743', 'uvim1006.tab:6805', 'uvim1006.tab:6867', 'uvim1006.tab:6929', 'uvim1006.tab:6991', 'uvim1006.tab:7053', 'uvim1006.tab:7115', 'uvim1006.tab:7177', 'uvim1006.tab:7356']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5035', 'uvim1006.tab:5036', 'uvim1006.tab:5037', 'uvim1006.tab:5038', 'uvim1006.tab:5039', 'uvim1006.tab:5317', 'uvim1006.tab:5379', 'uvim1006.tab:5441', 'uvim1006.tab:5503', 'uvim1006.tab:5565', 'uvim1006.tab:5627', 'uvim1006.tab:5689', 'uvim1006.tab:5751', 'uvim1006.tab:5813', 'uvim1006.tab:5875', 'uvim1006.tab:5937', 'uvim1006.tab:5999', 'uvim1006.tab:6061', 'uvim1006.tab:6123', 'uvim1006.tab:6185', 'uvim1006.tab:6247', 'uvim1006.tab:6309', 'uvim1006.tab:6371', 'uvim1006.tab:6433', 'uvim1006.tab:6495', 'uvim1006.tab:6557', 'uvim1006.tab:6619', 'uvim1006.tab:6681', 'uvim1006.tab:6743', 'uvim1006.tab:6805', 'uvim1006.tab:6867', 'uvim1006.tab:6929', 'uvim1006.tab:6991', 'uvim1006.tab:7053', 'uvim1006.tab:7115', 'uvim1006.tab:7177', 'uvim1006.tab:7356']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5035', 'uvim1006.tab:5037', 'uvim1006.tab:5038', 'uvim1006.tab:5039', 'uvim1006.tab:5317', 'uvim1006.tab:5379', 'uvim1006.tab:5441', 'uvim1006.tab:5503', 'uvim1006.tab:5565', 'uvim1006.tab:5627', 'uvim1006.tab:5689', 'uvim1006.tab:5751', 'uvim1006.tab:5813', 'uvim1006.tab:5875', 'uvim1006.tab:5937', 'uvim1006.tab:5999', 'uvim1006.tab:6061', 'uvim1006.tab:6123', 'uvim1006.tab:6185', 'uvim1006.tab:6247', 'uvim1006.tab:6309', 'uvim1006.tab:6371', 'uvim1006.tab:6433', 'uvim1006.tab:6495', 'uvim1006.tab:6557', 'uvim1006.tab:6619', 'uvim1006.tab:6681', 'uvim1006.tab:6743', 'uvim1006.tab:6805', 'uvim1006.tab:6867', 'uvim1006.tab:6929', 'uvim1006.tab:6991', 'uvim1006.tab:7053']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5035', 'uvim1006.tab:5037', 'uvim1006.tab:5038', 'uvim1006.tab:5039', 'uvim1006.tab:5317', 'uvim1006.tab:5379', 'uvim1006.tab:5441', 'uvim1006.tab:5503', 'uvim1006.tab:5565', 'uvim1006.tab:5627', 'uvim1006.tab:5689', 'uvim1006.tab:5751', 'uvim1006.tab:5813', 'uvim1006.tab:5875', 'uvim1006.tab:5937', 'uvim1006.tab:5999', 'uvim1006.tab:6061', 'uvim1006.tab:6123', 'uvim1006.tab:6185', 'uvim1006.tab:6247', 'uvim1006.tab:6309', 'uvim1006.tab:6371', 'uvim1006.tab:6433', 'uvim1006.tab:6495', 'uvim1006.tab:6557', 'uvim1006.tab:6619', 'uvim1006.tab:6681', 'uvim1006.tab:6743', 'uvim1006.tab:6805', 'uvim1006.tab:6867', 'uvim1006.tab:6929', 'uvim1006.tab:6991', 'uvim1006.tab:7053']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5036', 'uvim1006.tab:7115', 'uvim1006.tab:7177']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5036', 'uvim1006.tab:7115', 'uvim1006.tab:7177']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5040', 'uvim1006.tab:5041', 'uvim1006.tab:5042', 'uvim1006.tab:5043', 'uvim1006.tab:5044', 'uvim1006.tab:5318', 'uvim1006.tab:5380', 'uvim1006.tab:5442', 'uvim1006.tab:5504', 'uvim1006.tab:5566', 'uvim1006.tab:5628', 'uvim1006.tab:5690', 'uvim1006.tab:5752', 'uvim1006.tab:5814', 'uvim1006.tab:5876', 'uvim1006.tab:5938', 'uvim1006.tab:6000', 'uvim1006.tab:6062', 'uvim1006.tab:6124', 'uvim1006.tab:6186', 'uvim1006.tab:6248', 'uvim1006.tab:6310', 'uvim1006.tab:6372', 'uvim1006.tab:6434', 'uvim1006.tab:6496', 'uvim1006.tab:6558', 'uvim1006.tab:6620', 'uvim1006.tab:6682', 'uvim1006.tab:6744', 'uvim1006.tab:6806', 'uvim1006.tab:6868', 'uvim1006.tab:6930', 'uvim1006.tab:6992', 'uvim1006.tab:7054', 'uvim1006.tab:7116', 'uvim1006.tab:7178']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5040', 'uvim1006.tab:5041', 'uvim1006.tab:5042', 'uvim1006.tab:5043', 'uvim1006.tab:5044', 'uvim1006.tab:5318', 'uvim1006.tab:5380', 'uvim1006.tab:5442', 'uvim1006.tab:5504', 'uvim1006.tab:5566', 'uvim1006.tab:5628', 'uvim1006.tab:5690', 'uvim1006.tab:5752', 'uvim1006.tab:5814', 'uvim1006.tab:5876', 'uvim1006.tab:5938', 'uvim1006.tab:6000', 'uvim1006.tab:6062', 'uvim1006.tab:6124', 'uvim1006.tab:6186', 'uvim1006.tab:6248', 'uvim1006.tab:6310', 'uvim1006.tab:6372', 'uvim1006.tab:6434', 'uvim1006.tab:6496', 'uvim1006.tab:6558', 'uvim1006.tab:6620', 'uvim1006.tab:6682', 'uvim1006.tab:6744', 'uvim1006.tab:6806', 'uvim1006.tab:6868', 'uvim1006.tab:6930', 'uvim1006.tab:6992', 'uvim1006.tab:7054', 'uvim1006.tab:7116', 'uvim1006.tab:7178']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5040', 'uvim1006.tab:5042', 'uvim1006.tab:5043', 'uvim1006.tab:5044', 'uvim1006.tab:5318', 'uvim1006.tab:5380', 'uvim1006.tab:5442', 'uvim1006.tab:5504', 'uvim1006.tab:5566', 'uvim1006.tab:5628', 'uvim1006.tab:5690', 'uvim1006.tab:5752', 'uvim1006.tab:5814', 'uvim1006.tab:5876', 'uvim1006.tab:5938', 'uvim1006.tab:6000', 'uvim1006.tab:6062', 'uvim1006.tab:6124', 'uvim1006.tab:6186', 'uvim1006.tab:6248', 'uvim1006.tab:6310', 'uvim1006.tab:6372', 'uvim1006.tab:6434', 'uvim1006.tab:6496', 'uvim1006.tab:6558', 'uvim1006.tab:6620', 'uvim1006.tab:6682', 'uvim1006.tab:6744', 'uvim1006.tab:6806', 'uvim1006.tab:6868', 'uvim1006.tab:6930', 'uvim1006.tab:6992', 'uvim1006.tab:7054']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5040', 'uvim1006.tab:5042', 'uvim1006.tab:5043', 'uvim1006.tab:5044', 'uvim1006.tab:5318', 'uvim1006.tab:5380', 'uvim1006.tab:5442', 'uvim1006.tab:5504', 'uvim1006.tab:5566', 'uvim1006.tab:5628', 'uvim1006.tab:5690', 'uvim1006.tab:5752', 'uvim1006.tab:5814', 'uvim1006.tab:5876', 'uvim1006.tab:5938', 'uvim1006.tab:6000', 'uvim1006.tab:6062', 'uvim1006.tab:6124', 'uvim1006.tab:6186', 'uvim1006.tab:6248', 'uvim1006.tab:6310', 'uvim1006.tab:6372', 'uvim1006.tab:6434', 'uvim1006.tab:6496', 'uvim1006.tab:6558', 'uvim1006.tab:6620', 'uvim1006.tab:6682', 'uvim1006.tab:6744', 'uvim1006.tab:6806', 'uvim1006.tab:6868', 'uvim1006.tab:6930', 'uvim1006.tab:6992', 'uvim1006.tab:7054']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5041', 'uvim1006.tab:7116', 'uvim1006.tab:7178']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5041', 'uvim1006.tab:7116', 'uvim1006.tab:7178']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5045', 'uvim1006.tab:5046', 'uvim1006.tab:5047', 'uvim1006.tab:5048', 'uvim1006.tab:5049', 'uvim1006.tab:5319', 'uvim1006.tab:5381', 'uvim1006.tab:5443', 'uvim1006.tab:5505', 'uvim1006.tab:5567', 'uvim1006.tab:5629', 'uvim1006.tab:5691', 'uvim1006.tab:5753', 'uvim1006.tab:5815', 'uvim1006.tab:5877', 'uvim1006.tab:5939', 'uvim1006.tab:6001', 'uvim1006.tab:6063', 'uvim1006.tab:6125', 'uvim1006.tab:6187', 'uvim1006.tab:6249', 'uvim1006.tab:6311', 'uvim1006.tab:6373', 'uvim1006.tab:6435', 'uvim1006.tab:6497', 'uvim1006.tab:6559', 'uvim1006.tab:6621', 'uvim1006.tab:6683', 'uvim1006.tab:6745', 'uvim1006.tab:6807', 'uvim1006.tab:6869', 'uvim1006.tab:6931', 'uvim1006.tab:6993', 'uvim1006.tab:7055', 'uvim1006.tab:7117', 'uvim1006.tab:7179']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5045', 'uvim1006.tab:5046', 'uvim1006.tab:5047', 'uvim1006.tab:5048', 'uvim1006.tab:5049', 'uvim1006.tab:5319', 'uvim1006.tab:5381', 'uvim1006.tab:5443', 'uvim1006.tab:5505', 'uvim1006.tab:5567', 'uvim1006.tab:5629', 'uvim1006.tab:5691', 'uvim1006.tab:5753', 'uvim1006.tab:5815', 'uvim1006.tab:5877', 'uvim1006.tab:5939', 'uvim1006.tab:6001', 'uvim1006.tab:6063', 'uvim1006.tab:6125', 'uvim1006.tab:6187', 'uvim1006.tab:6249', 'uvim1006.tab:6311', 'uvim1006.tab:6373', 'uvim1006.tab:6435', 'uvim1006.tab:6497', 'uvim1006.tab:6559', 'uvim1006.tab:6621', 'uvim1006.tab:6683', 'uvim1006.tab:6745', 'uvim1006.tab:6807', 'uvim1006.tab:6869', 'uvim1006.tab:6931', 'uvim1006.tab:6993', 'uvim1006.tab:7055', 'uvim1006.tab:7117', 'uvim1006.tab:7179']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5045', 'uvim1006.tab:5047', 'uvim1006.tab:5048', 'uvim1006.tab:5049', 'uvim1006.tab:5319', 'uvim1006.tab:5381', 'uvim1006.tab:5443', 'uvim1006.tab:5505', 'uvim1006.tab:5567', 'uvim1006.tab:5629', 'uvim1006.tab:5691', 'uvim1006.tab:5753', 'uvim1006.tab:5815', 'uvim1006.tab:5877', 'uvim1006.tab:5939', 'uvim1006.tab:6001', 'uvim1006.tab:6063', 'uvim1006.tab:6125', 'uvim1006.tab:6187', 'uvim1006.tab:6249', 'uvim1006.tab:6311', 'uvim1006.tab:6373', 'uvim1006.tab:6435', 'uvim1006.tab:6497', 'uvim1006.tab:6559', 'uvim1006.tab:6621', 'uvim1006.tab:6683', 'uvim1006.tab:6745', 'uvim1006.tab:6807', 'uvim1006.tab:6869', 'uvim1006.tab:6931', 'uvim1006.tab:6993', 'uvim1006.tab:7055']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5045', 'uvim1006.tab:5047', 'uvim1006.tab:5048', 'uvim1006.tab:5049', 'uvim1006.tab:5319', 'uvim1006.tab:5381', 'uvim1006.tab:5443', 'uvim1006.tab:5505', 'uvim1006.tab:5567', 'uvim1006.tab:5629', 'uvim1006.tab:5691', 'uvim1006.tab:5753', 'uvim1006.tab:5815', 'uvim1006.tab:5877', 'uvim1006.tab:5939', 'uvim1006.tab:6001', 'uvim1006.tab:6063', 'uvim1006.tab:6125', 'uvim1006.tab:6187', 'uvim1006.tab:6249', 'uvim1006.tab:6311', 'uvim1006.tab:6373', 'uvim1006.tab:6435', 'uvim1006.tab:6497', 'uvim1006.tab:6559', 'uvim1006.tab:6621', 'uvim1006.tab:6683', 'uvim1006.tab:6745', 'uvim1006.tab:6807', 'uvim1006.tab:6869', 'uvim1006.tab:6931', 'uvim1006.tab:6993', 'uvim1006.tab:7055']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5046', 'uvim1006.tab:7117', 'uvim1006.tab:7179']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5046', 'uvim1006.tab:7117', 'uvim1006.tab:7179']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5050', 'uvim1006.tab:5051', 'uvim1006.tab:5052', 'uvim1006.tab:5053', 'uvim1006.tab:5054', 'uvim1006.tab:5320', 'uvim1006.tab:5382', 'uvim1006.tab:5444', 'uvim1006.tab:5506', 'uvim1006.tab:5568', 'uvim1006.tab:5630', 'uvim1006.tab:5692', 'uvim1006.tab:5754', 'uvim1006.tab:5816', 'uvim1006.tab:5878', 'uvim1006.tab:5940', 'uvim1006.tab:6002', 'uvim1006.tab:6064', 'uvim1006.tab:6126', 'uvim1006.tab:6188', 'uvim1006.tab:6250', 'uvim1006.tab:6312', 'uvim1006.tab:6374', 'uvim1006.tab:6436', 'uvim1006.tab:6498', 'uvim1006.tab:6560', 'uvim1006.tab:6622', 'uvim1006.tab:6684', 'uvim1006.tab:6746', 'uvim1006.tab:6808', 'uvim1006.tab:6870', 'uvim1006.tab:6932', 'uvim1006.tab:6994', 'uvim1006.tab:7056', 'uvim1006.tab:7118', 'uvim1006.tab:7180']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['uvim1006.tab:5050', 'uvim1006.tab:5051', 'uvim1006.tab:5052', 'uvim1006.tab:5053', 'uvim1006.tab:5054', 'uvim1006.tab:5320', 'uvim1006.tab:5382', 'uvim1006.tab:5444', 'uvim1006.tab:5506', 'uvim1006.tab:5568', 'uvim1006.tab:5630', 'uvim1006.tab:5692', 'uvim1006.tab:5754', 'uvim1006.tab:5816', 'uvim1006.tab:5878', 'uvim1006.tab:5940', 'uvim1006.tab:6002', 'uvim1006.tab:6064', 'uvim1006.tab:6126', 'uvim1006.tab:6188', 'uvim1006.tab:6250', 'uvim1006.tab:6312', 'uvim1006.tab:6374', 'uvim1006.tab:6436', 'uvim1006.tab:6498', 'uvim1006.tab:6560', 'uvim1006.tab:6622', 'uvim1006.tab:6684', 'uvim1006.tab:6746', 'uvim1006.tab:6808', 'uvim1006.tab:6870', 'uvim1006.tab:6932', 'uvim1006.tab:6994', 'uvim1006.tab:7056', 'uvim1006.tab:7118', 'uvim1006.tab:7180']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5050', 'uvim1006.tab:5052', 'uvim1006.tab:5053', 'uvim1006.tab:5054', 'uvim1006.tab:5320', 'uvim1006.tab:5382', 'uvim1006.tab:5444', 'uvim1006.tab:5506', 'uvim1006.tab:5568', 'uvim1006.tab:5630', 'uvim1006.tab:5692', 'uvim1006.tab:5754', 'uvim1006.tab:5816', 'uvim1006.tab:5878', 'uvim1006.tab:5940', 'uvim1006.tab:6002', 'uvim1006.tab:6064', 'uvim1006.tab:6126', 'uvim1006.tab:6188', 'uvim1006.tab:6250', 'uvim1006.tab:6312', 'uvim1006.tab:6374', 'uvim1006.tab:6436', 'uvim1006.tab:6498', 'uvim1006.tab:6560', 'uvim1006.tab:6622', 'uvim1006.tab:6684', 'uvim1006.tab:6746', 'uvim1006.tab:6808', 'uvim1006.tab:6870', 'uvim1006.tab:6932', 'uvim1006.tab:6994', 'uvim1006.tab:7056']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5050', 'uvim1006.tab:5052', 'uvim1006.tab:5053', 'uvim1006.tab:5054', 'uvim1006.tab:5320', 'uvim1006.tab:5382', 'uvim1006.tab:5444', 'uvim1006.tab:5506', 'uvim1006.tab:5568', 'uvim1006.tab:5630', 'uvim1006.tab:5692', 'uvim1006.tab:5754', 'uvim1006.tab:5816', 'uvim1006.tab:5878', 'uvim1006.tab:5940', 'uvim1006.tab:6002', 'uvim1006.tab:6064', 'uvim1006.tab:6126', 'uvim1006.tab:6188', 'uvim1006.tab:6250', 'uvim1006.tab:6312', 'uvim1006.tab:6374', 'uvim1006.tab:6436', 'uvim1006.tab:6498', 'uvim1006.tab:6560', 'uvim1006.tab:6622', 'uvim1006.tab:6684', 'uvim1006.tab:6746', 'uvim1006.tab:6808', 'uvim1006.tab:6870', 'uvim1006.tab:6932', 'uvim1006.tab:6994', 'uvim1006.tab:7056']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5051', 'uvim1006.tab:7118', 'uvim1006.tab:7180']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5051', 'uvim1006.tab:7118', 'uvim1006.tab:7180']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5055', 'uvim1006.tab:5056', 'uvim1006.tab:5057', 'uvim1006.tab:5058', 'uvim1006.tab:5059', 'uvim1006.tab:5321', 'uvim1006.tab:5383', 'uvim1006.tab:5445', 'uvim1006.tab:5507', 'uvim1006.tab:5569', 'uvim1006.tab:5631', 'uvim1006.tab:5693', 'uvim1006.tab:5755', 'uvim1006.tab:5817', 'uvim1006.tab:5879', 'uvim1006.tab:5941', 'uvim1006.tab:6003', 'uvim1006.tab:6065', 'uvim1006.tab:6127', 'uvim1006.tab:6189', 'uvim1006.tab:6251', 'uvim1006.tab:6313', 'uvim1006.tab:6375', 'uvim1006.tab:6437', 'uvim1006.tab:6499', 'uvim1006.tab:6561', 'uvim1006.tab:6623', 'uvim1006.tab:6685', 'uvim1006.tab:6747', 'uvim1006.tab:6809', 'uvim1006.tab:6871', 'uvim1006.tab:6933', 'uvim1006.tab:6995', 'uvim1006.tab:7057', 'uvim1006.tab:7119', 'uvim1006.tab:7181']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5055', 'uvim1006.tab:5056', 'uvim1006.tab:5057', 'uvim1006.tab:5058', 'uvim1006.tab:5059', 'uvim1006.tab:5321', 'uvim1006.tab:5383', 'uvim1006.tab:5445', 'uvim1006.tab:5507', 'uvim1006.tab:5569', 'uvim1006.tab:5631', 'uvim1006.tab:5693', 'uvim1006.tab:5755', 'uvim1006.tab:5817', 'uvim1006.tab:5879', 'uvim1006.tab:5941', 'uvim1006.tab:6003', 'uvim1006.tab:6065', 'uvim1006.tab:6127', 'uvim1006.tab:6189', 'uvim1006.tab:6251', 'uvim1006.tab:6313', 'uvim1006.tab:6375', 'uvim1006.tab:6437', 'uvim1006.tab:6499', 'uvim1006.tab:6561', 'uvim1006.tab:6623', 'uvim1006.tab:6685', 'uvim1006.tab:6747', 'uvim1006.tab:6809', 'uvim1006.tab:6871', 'uvim1006.tab:6933', 'uvim1006.tab:6995', 'uvim1006.tab:7057', 'uvim1006.tab:7119', 'uvim1006.tab:7181']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5055', 'uvim1006.tab:5057', 'uvim1006.tab:5058', 'uvim1006.tab:5059', 'uvim1006.tab:5321', 'uvim1006.tab:5383', 'uvim1006.tab:5445', 'uvim1006.tab:5507', 'uvim1006.tab:5569', 'uvim1006.tab:5631', 'uvim1006.tab:5693', 'uvim1006.tab:5755', 'uvim1006.tab:5817', 'uvim1006.tab:5879', 'uvim1006.tab:5941', 'uvim1006.tab:6003', 'uvim1006.tab:6065', 'uvim1006.tab:6127', 'uvim1006.tab:6189', 'uvim1006.tab:6251', 'uvim1006.tab:6313', 'uvim1006.tab:6375', 'uvim1006.tab:6437', 'uvim1006.tab:6499', 'uvim1006.tab:6561', 'uvim1006.tab:6623', 'uvim1006.tab:6685', 'uvim1006.tab:6747', 'uvim1006.tab:6809', 'uvim1006.tab:6871', 'uvim1006.tab:6933', 'uvim1006.tab:6995', 'uvim1006.tab:7057']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5055', 'uvim1006.tab:5057', 'uvim1006.tab:5058', 'uvim1006.tab:5059', 'uvim1006.tab:5321', 'uvim1006.tab:5383', 'uvim1006.tab:5445', 'uvim1006.tab:5507', 'uvim1006.tab:5569', 'uvim1006.tab:5631', 'uvim1006.tab:5693', 'uvim1006.tab:5755', 'uvim1006.tab:5817', 'uvim1006.tab:5879', 'uvim1006.tab:5941', 'uvim1006.tab:6003', 'uvim1006.tab:6065', 'uvim1006.tab:6127', 'uvim1006.tab:6189', 'uvim1006.tab:6251', 'uvim1006.tab:6313', 'uvim1006.tab:6375', 'uvim1006.tab:6437', 'uvim1006.tab:6499', 'uvim1006.tab:6561', 'uvim1006.tab:6623', 'uvim1006.tab:6685', 'uvim1006.tab:6747', 'uvim1006.tab:6809', 'uvim1006.tab:6871', 'uvim1006.tab:6933', 'uvim1006.tab:6995', 'uvim1006.tab:7057']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5056', 'uvim1006.tab:7119', 'uvim1006.tab:7181']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5056', 'uvim1006.tab:7119', 'uvim1006.tab:7181']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5060', 'uvim1006.tab:5061', 'uvim1006.tab:5062', 'uvim1006.tab:5063', 'uvim1006.tab:5064', 'uvim1006.tab:5322', 'uvim1006.tab:5384', 'uvim1006.tab:5446', 'uvim1006.tab:5508', 'uvim1006.tab:5570', 'uvim1006.tab:5632', 'uvim1006.tab:5694', 'uvim1006.tab:5756', 'uvim1006.tab:5818', 'uvim1006.tab:5880', 'uvim1006.tab:5942', 'uvim1006.tab:6004', 'uvim1006.tab:6066', 'uvim1006.tab:6128', 'uvim1006.tab:6190', 'uvim1006.tab:6252', 'uvim1006.tab:6314', 'uvim1006.tab:6376', 'uvim1006.tab:6438', 'uvim1006.tab:6500', 'uvim1006.tab:6562', 'uvim1006.tab:6624', 'uvim1006.tab:6686', 'uvim1006.tab:6748', 'uvim1006.tab:6810', 'uvim1006.tab:6872', 'uvim1006.tab:6934', 'uvim1006.tab:6996', 'uvim1006.tab:7058', 'uvim1006.tab:7120', 'uvim1006.tab:7182']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5060', 'uvim1006.tab:5061', 'uvim1006.tab:5062', 'uvim1006.tab:5063', 'uvim1006.tab:5064', 'uvim1006.tab:5322', 'uvim1006.tab:5384', 'uvim1006.tab:5446', 'uvim1006.tab:5508', 'uvim1006.tab:5570', 'uvim1006.tab:5632', 'uvim1006.tab:5694', 'uvim1006.tab:5756', 'uvim1006.tab:5818', 'uvim1006.tab:5880', 'uvim1006.tab:5942', 'uvim1006.tab:6004', 'uvim1006.tab:6066', 'uvim1006.tab:6128', 'uvim1006.tab:6190', 'uvim1006.tab:6252', 'uvim1006.tab:6314', 'uvim1006.tab:6376', 'uvim1006.tab:6438', 'uvim1006.tab:6500', 'uvim1006.tab:6562', 'uvim1006.tab:6624', 'uvim1006.tab:6686', 'uvim1006.tab:6748', 'uvim1006.tab:6810', 'uvim1006.tab:6872', 'uvim1006.tab:6934', 'uvim1006.tab:6996', 'uvim1006.tab:7058', 'uvim1006.tab:7120', 'uvim1006.tab:7182']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5060', 'uvim1006.tab:5062', 'uvim1006.tab:5063', 'uvim1006.tab:5064', 'uvim1006.tab:5322', 'uvim1006.tab:5384', 'uvim1006.tab:5446', 'uvim1006.tab:5508', 'uvim1006.tab:5570', 'uvim1006.tab:5632', 'uvim1006.tab:5694', 'uvim1006.tab:5756', 'uvim1006.tab:5818', 'uvim1006.tab:5880', 'uvim1006.tab:5942', 'uvim1006.tab:6004', 'uvim1006.tab:6066', 'uvim1006.tab:6128', 'uvim1006.tab:6190', 'uvim1006.tab:6252', 'uvim1006.tab:6314', 'uvim1006.tab:6376', 'uvim1006.tab:6438', 'uvim1006.tab:6500', 'uvim1006.tab:6562', 'uvim1006.tab:6624', 'uvim1006.tab:6686', 'uvim1006.tab:6748', 'uvim1006.tab:6810', 'uvim1006.tab:6872', 'uvim1006.tab:6934', 'uvim1006.tab:6996', 'uvim1006.tab:7058']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5060', 'uvim1006.tab:5062', 'uvim1006.tab:5063', 'uvim1006.tab:5064', 'uvim1006.tab:5322', 'uvim1006.tab:5384', 'uvim1006.tab:5446', 'uvim1006.tab:5508', 'uvim1006.tab:5570', 'uvim1006.tab:5632', 'uvim1006.tab:5694', 'uvim1006.tab:5756', 'uvim1006.tab:5818', 'uvim1006.tab:5880', 'uvim1006.tab:5942', 'uvim1006.tab:6004', 'uvim1006.tab:6066', 'uvim1006.tab:6128', 'uvim1006.tab:6190', 'uvim1006.tab:6252', 'uvim1006.tab:6314', 'uvim1006.tab:6376', 'uvim1006.tab:6438', 'uvim1006.tab:6500', 'uvim1006.tab:6562', 'uvim1006.tab:6624', 'uvim1006.tab:6686', 'uvim1006.tab:6748', 'uvim1006.tab:6810', 'uvim1006.tab:6872', 'uvim1006.tab:6934', 'uvim1006.tab:6996', 'uvim1006.tab:7058']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5061', 'uvim1006.tab:7120', 'uvim1006.tab:7182']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5061', 'uvim1006.tab:7120', 'uvim1006.tab:7182']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5065', 'uvim1006.tab:5066', 'uvim1006.tab:5067', 'uvim1006.tab:5068', 'uvim1006.tab:5069', 'uvim1006.tab:5323', 'uvim1006.tab:5385', 'uvim1006.tab:5447', 'uvim1006.tab:5509', 'uvim1006.tab:5571', 'uvim1006.tab:5633', 'uvim1006.tab:5695', 'uvim1006.tab:5757', 'uvim1006.tab:5819', 'uvim1006.tab:5881', 'uvim1006.tab:5943', 'uvim1006.tab:6005', 'uvim1006.tab:6067', 'uvim1006.tab:6129', 'uvim1006.tab:6191', 'uvim1006.tab:6253', 'uvim1006.tab:6315', 'uvim1006.tab:6377', 'uvim1006.tab:6439', 'uvim1006.tab:6501', 'uvim1006.tab:6563', 'uvim1006.tab:6625', 'uvim1006.tab:6687', 'uvim1006.tab:6749', 'uvim1006.tab:6811', 'uvim1006.tab:6873', 'uvim1006.tab:6935', 'uvim1006.tab:6997', 'uvim1006.tab:7059', 'uvim1006.tab:7121', 'uvim1006.tab:7183']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5065', 'uvim1006.tab:5066', 'uvim1006.tab:5067', 'uvim1006.tab:5068', 'uvim1006.tab:5069', 'uvim1006.tab:5323', 'uvim1006.tab:5385', 'uvim1006.tab:5447', 'uvim1006.tab:5509', 'uvim1006.tab:5571', 'uvim1006.tab:5633', 'uvim1006.tab:5695', 'uvim1006.tab:5757', 'uvim1006.tab:5819', 'uvim1006.tab:5881', 'uvim1006.tab:5943', 'uvim1006.tab:6005', 'uvim1006.tab:6067', 'uvim1006.tab:6129', 'uvim1006.tab:6191', 'uvim1006.tab:6253', 'uvim1006.tab:6315', 'uvim1006.tab:6377', 'uvim1006.tab:6439', 'uvim1006.tab:6501', 'uvim1006.tab:6563', 'uvim1006.tab:6625', 'uvim1006.tab:6687', 'uvim1006.tab:6749', 'uvim1006.tab:6811', 'uvim1006.tab:6873', 'uvim1006.tab:6935', 'uvim1006.tab:6997', 'uvim1006.tab:7059', 'uvim1006.tab:7121', 'uvim1006.tab:7183']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5065', 'uvim1006.tab:5067', 'uvim1006.tab:5068', 'uvim1006.tab:5069', 'uvim1006.tab:5323', 'uvim1006.tab:5385', 'uvim1006.tab:5447', 'uvim1006.tab:5509', 'uvim1006.tab:5571', 'uvim1006.tab:5633', 'uvim1006.tab:5695', 'uvim1006.tab:5757', 'uvim1006.tab:5819', 'uvim1006.tab:5881', 'uvim1006.tab:5943', 'uvim1006.tab:6005', 'uvim1006.tab:6067', 'uvim1006.tab:6129', 'uvim1006.tab:6191', 'uvim1006.tab:6253', 'uvim1006.tab:6315', 'uvim1006.tab:6377', 'uvim1006.tab:6439', 'uvim1006.tab:6501', 'uvim1006.tab:6563', 'uvim1006.tab:6625', 'uvim1006.tab:6687', 'uvim1006.tab:6749', 'uvim1006.tab:6811', 'uvim1006.tab:6873', 'uvim1006.tab:6935', 'uvim1006.tab:6997', 'uvim1006.tab:7059']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5065', 'uvim1006.tab:5067', 'uvim1006.tab:5068', 'uvim1006.tab:5069', 'uvim1006.tab:5323', 'uvim1006.tab:5385', 'uvim1006.tab:5447', 'uvim1006.tab:5509', 'uvim1006.tab:5571', 'uvim1006.tab:5633', 'uvim1006.tab:5695', 'uvim1006.tab:5757', 'uvim1006.tab:5819', 'uvim1006.tab:5881', 'uvim1006.tab:5943', 'uvim1006.tab:6005', 'uvim1006.tab:6067', 'uvim1006.tab:6129', 'uvim1006.tab:6191', 'uvim1006.tab:6253', 'uvim1006.tab:6315', 'uvim1006.tab:6377', 'uvim1006.tab:6439', 'uvim1006.tab:6501', 'uvim1006.tab:6563', 'uvim1006.tab:6625', 'uvim1006.tab:6687', 'uvim1006.tab:6749', 'uvim1006.tab:6811', 'uvim1006.tab:6873', 'uvim1006.tab:6935', 'uvim1006.tab:6997', 'uvim1006.tab:7059']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5066', 'uvim1006.tab:7121', 'uvim1006.tab:7183']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5066', 'uvim1006.tab:7121', 'uvim1006.tab:7183']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5070', 'uvim1006.tab:5071', 'uvim1006.tab:5072', 'uvim1006.tab:5073', 'uvim1006.tab:5074', 'uvim1006.tab:5324', 'uvim1006.tab:5386', 'uvim1006.tab:5448', 'uvim1006.tab:5510', 'uvim1006.tab:5572', 'uvim1006.tab:5634', 'uvim1006.tab:5696', 'uvim1006.tab:5758', 'uvim1006.tab:5820', 'uvim1006.tab:5882', 'uvim1006.tab:5944', 'uvim1006.tab:6006', 'uvim1006.tab:6068', 'uvim1006.tab:6130', 'uvim1006.tab:6192', 'uvim1006.tab:6254', 'uvim1006.tab:6316', 'uvim1006.tab:6378', 'uvim1006.tab:6440', 'uvim1006.tab:6502', 'uvim1006.tab:6564', 'uvim1006.tab:6626', 'uvim1006.tab:6688', 'uvim1006.tab:6750', 'uvim1006.tab:6812', 'uvim1006.tab:6874', 'uvim1006.tab:6936', 'uvim1006.tab:6998', 'uvim1006.tab:7060', 'uvim1006.tab:7122', 'uvim1006.tab:7184']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5070', 'uvim1006.tab:5071', 'uvim1006.tab:5072', 'uvim1006.tab:5073', 'uvim1006.tab:5074', 'uvim1006.tab:5324', 'uvim1006.tab:5386', 'uvim1006.tab:5448', 'uvim1006.tab:5510', 'uvim1006.tab:5572', 'uvim1006.tab:5634', 'uvim1006.tab:5696', 'uvim1006.tab:5758', 'uvim1006.tab:5820', 'uvim1006.tab:5882', 'uvim1006.tab:5944', 'uvim1006.tab:6006', 'uvim1006.tab:6068', 'uvim1006.tab:6130', 'uvim1006.tab:6192', 'uvim1006.tab:6254', 'uvim1006.tab:6316', 'uvim1006.tab:6378', 'uvim1006.tab:6440', 'uvim1006.tab:6502', 'uvim1006.tab:6564', 'uvim1006.tab:6626', 'uvim1006.tab:6688', 'uvim1006.tab:6750', 'uvim1006.tab:6812', 'uvim1006.tab:6874', 'uvim1006.tab:6936', 'uvim1006.tab:6998', 'uvim1006.tab:7060', 'uvim1006.tab:7122', 'uvim1006.tab:7184']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5070', 'uvim1006.tab:5072', 'uvim1006.tab:5073', 'uvim1006.tab:5074', 'uvim1006.tab:5324', 'uvim1006.tab:5386', 'uvim1006.tab:5448', 'uvim1006.tab:5510', 'uvim1006.tab:5572', 'uvim1006.tab:5634', 'uvim1006.tab:5696', 'uvim1006.tab:5758', 'uvim1006.tab:5820', 'uvim1006.tab:5882', 'uvim1006.tab:5944', 'uvim1006.tab:6006', 'uvim1006.tab:6068', 'uvim1006.tab:6130', 'uvim1006.tab:6192', 'uvim1006.tab:6254', 'uvim1006.tab:6316', 'uvim1006.tab:6378', 'uvim1006.tab:6440', 'uvim1006.tab:6502', 'uvim1006.tab:6564', 'uvim1006.tab:6626', 'uvim1006.tab:6688', 'uvim1006.tab:6750', 'uvim1006.tab:6812', 'uvim1006.tab:6874', 'uvim1006.tab:6936', 'uvim1006.tab:6998', 'uvim1006.tab:7060']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5070', 'uvim1006.tab:5072', 'uvim1006.tab:5073', 'uvim1006.tab:5074', 'uvim1006.tab:5324', 'uvim1006.tab:5386', 'uvim1006.tab:5448', 'uvim1006.tab:5510', 'uvim1006.tab:5572', 'uvim1006.tab:5634', 'uvim1006.tab:5696', 'uvim1006.tab:5758', 'uvim1006.tab:5820', 'uvim1006.tab:5882', 'uvim1006.tab:5944', 'uvim1006.tab:6006', 'uvim1006.tab:6068', 'uvim1006.tab:6130', 'uvim1006.tab:6192', 'uvim1006.tab:6254', 'uvim1006.tab:6316', 'uvim1006.tab:6378', 'uvim1006.tab:6440', 'uvim1006.tab:6502', 'uvim1006.tab:6564', 'uvim1006.tab:6626', 'uvim1006.tab:6688', 'uvim1006.tab:6750', 'uvim1006.tab:6812', 'uvim1006.tab:6874', 'uvim1006.tab:6936', 'uvim1006.tab:6998', 'uvim1006.tab:7060']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5071', 'uvim1006.tab:7122', 'uvim1006.tab:7184']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5071', 'uvim1006.tab:7122', 'uvim1006.tab:7184']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5075', 'uvim1006.tab:5076', 'uvim1006.tab:5077', 'uvim1006.tab:5078', 'uvim1006.tab:5079', 'uvim1006.tab:5325', 'uvim1006.tab:5387', 'uvim1006.tab:5449', 'uvim1006.tab:5511', 'uvim1006.tab:5573', 'uvim1006.tab:5635', 'uvim1006.tab:5697', 'uvim1006.tab:5759', 'uvim1006.tab:5821', 'uvim1006.tab:5883', 'uvim1006.tab:5945', 'uvim1006.tab:6007', 'uvim1006.tab:6069', 'uvim1006.tab:6131', 'uvim1006.tab:6193', 'uvim1006.tab:6255', 'uvim1006.tab:6317', 'uvim1006.tab:6379', 'uvim1006.tab:6441', 'uvim1006.tab:6503', 'uvim1006.tab:6565', 'uvim1006.tab:6627', 'uvim1006.tab:6689', 'uvim1006.tab:6751', 'uvim1006.tab:6813', 'uvim1006.tab:6875', 'uvim1006.tab:6937', 'uvim1006.tab:6999', 'uvim1006.tab:7061', 'uvim1006.tab:7123', 'uvim1006.tab:7185']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5075', 'uvim1006.tab:5076', 'uvim1006.tab:5077', 'uvim1006.tab:5078', 'uvim1006.tab:5079', 'uvim1006.tab:5325', 'uvim1006.tab:5387', 'uvim1006.tab:5449', 'uvim1006.tab:5511', 'uvim1006.tab:5573', 'uvim1006.tab:5635', 'uvim1006.tab:5697', 'uvim1006.tab:5759', 'uvim1006.tab:5821', 'uvim1006.tab:5883', 'uvim1006.tab:5945', 'uvim1006.tab:6007', 'uvim1006.tab:6069', 'uvim1006.tab:6131', 'uvim1006.tab:6193', 'uvim1006.tab:6255', 'uvim1006.tab:6317', 'uvim1006.tab:6379', 'uvim1006.tab:6441', 'uvim1006.tab:6503', 'uvim1006.tab:6565', 'uvim1006.tab:6627', 'uvim1006.tab:6689', 'uvim1006.tab:6751', 'uvim1006.tab:6813', 'uvim1006.tab:6875', 'uvim1006.tab:6937', 'uvim1006.tab:6999', 'uvim1006.tab:7061', 'uvim1006.tab:7123', 'uvim1006.tab:7185']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5075', 'uvim1006.tab:5077', 'uvim1006.tab:5078', 'uvim1006.tab:5079', 'uvim1006.tab:5325', 'uvim1006.tab:5387', 'uvim1006.tab:5449', 'uvim1006.tab:5511', 'uvim1006.tab:5573', 'uvim1006.tab:5635', 'uvim1006.tab:5697', 'uvim1006.tab:5759', 'uvim1006.tab:5821', 'uvim1006.tab:5883', 'uvim1006.tab:5945', 'uvim1006.tab:6007', 'uvim1006.tab:6069', 'uvim1006.tab:6131', 'uvim1006.tab:6193', 'uvim1006.tab:6255', 'uvim1006.tab:6317', 'uvim1006.tab:6379', 'uvim1006.tab:6441', 'uvim1006.tab:6503', 'uvim1006.tab:6565', 'uvim1006.tab:6627', 'uvim1006.tab:6689', 'uvim1006.tab:6751', 'uvim1006.tab:6813', 'uvim1006.tab:6875', 'uvim1006.tab:6937', 'uvim1006.tab:6999', 'uvim1006.tab:7061']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5075', 'uvim1006.tab:5077', 'uvim1006.tab:5078', 'uvim1006.tab:5079', 'uvim1006.tab:5325', 'uvim1006.tab:5387', 'uvim1006.tab:5449', 'uvim1006.tab:5511', 'uvim1006.tab:5573', 'uvim1006.tab:5635', 'uvim1006.tab:5697', 'uvim1006.tab:5759', 'uvim1006.tab:5821', 'uvim1006.tab:5883', 'uvim1006.tab:5945', 'uvim1006.tab:6007', 'uvim1006.tab:6069', 'uvim1006.tab:6131', 'uvim1006.tab:6193', 'uvim1006.tab:6255', 'uvim1006.tab:6317', 'uvim1006.tab:6379', 'uvim1006.tab:6441', 'uvim1006.tab:6503', 'uvim1006.tab:6565', 'uvim1006.tab:6627', 'uvim1006.tab:6689', 'uvim1006.tab:6751', 'uvim1006.tab:6813', 'uvim1006.tab:6875', 'uvim1006.tab:6937', 'uvim1006.tab:6999', 'uvim1006.tab:7061']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5076', 'uvim1006.tab:7123', 'uvim1006.tab:7185']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5076', 'uvim1006.tab:7123', 'uvim1006.tab:7185']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5080', 'uvim1006.tab:5081', 'uvim1006.tab:5082', 'uvim1006.tab:5083', 'uvim1006.tab:5084', 'uvim1006.tab:5326', 'uvim1006.tab:5388', 'uvim1006.tab:5450', 'uvim1006.tab:5512', 'uvim1006.tab:5574', 'uvim1006.tab:5636', 'uvim1006.tab:5698', 'uvim1006.tab:5760', 'uvim1006.tab:5822', 'uvim1006.tab:5884', 'uvim1006.tab:5946', 'uvim1006.tab:6008', 'uvim1006.tab:6070', 'uvim1006.tab:6132', 'uvim1006.tab:6194', 'uvim1006.tab:6256', 'uvim1006.tab:6318', 'uvim1006.tab:6380', 'uvim1006.tab:6442', 'uvim1006.tab:6504', 'uvim1006.tab:6566', 'uvim1006.tab:6628', 'uvim1006.tab:6690', 'uvim1006.tab:6752', 'uvim1006.tab:6814', 'uvim1006.tab:6876', 'uvim1006.tab:6938', 'uvim1006.tab:7000', 'uvim1006.tab:7062', 'uvim1006.tab:7124', 'uvim1006.tab:7186']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5080', 'uvim1006.tab:5081', 'uvim1006.tab:5082', 'uvim1006.tab:5083', 'uvim1006.tab:5084', 'uvim1006.tab:5326', 'uvim1006.tab:5388', 'uvim1006.tab:5450', 'uvim1006.tab:5512', 'uvim1006.tab:5574', 'uvim1006.tab:5636', 'uvim1006.tab:5698', 'uvim1006.tab:5760', 'uvim1006.tab:5822', 'uvim1006.tab:5884', 'uvim1006.tab:5946', 'uvim1006.tab:6008', 'uvim1006.tab:6070', 'uvim1006.tab:6132', 'uvim1006.tab:6194', 'uvim1006.tab:6256', 'uvim1006.tab:6318', 'uvim1006.tab:6380', 'uvim1006.tab:6442', 'uvim1006.tab:6504', 'uvim1006.tab:6566', 'uvim1006.tab:6628', 'uvim1006.tab:6690', 'uvim1006.tab:6752', 'uvim1006.tab:6814', 'uvim1006.tab:6876', 'uvim1006.tab:6938', 'uvim1006.tab:7000', 'uvim1006.tab:7062', 'uvim1006.tab:7124', 'uvim1006.tab:7186']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5080', 'uvim1006.tab:5082', 'uvim1006.tab:5083', 'uvim1006.tab:5084', 'uvim1006.tab:5326', 'uvim1006.tab:5388', 'uvim1006.tab:5450', 'uvim1006.tab:5512', 'uvim1006.tab:5574', 'uvim1006.tab:5636', 'uvim1006.tab:5698', 'uvim1006.tab:5760', 'uvim1006.tab:5822', 'uvim1006.tab:5884', 'uvim1006.tab:5946', 'uvim1006.tab:6008', 'uvim1006.tab:6070', 'uvim1006.tab:6132', 'uvim1006.tab:6194', 'uvim1006.tab:6256', 'uvim1006.tab:6318', 'uvim1006.tab:6380', 'uvim1006.tab:6442', 'uvim1006.tab:6504', 'uvim1006.tab:6566', 'uvim1006.tab:6628', 'uvim1006.tab:6690', 'uvim1006.tab:6752', 'uvim1006.tab:6814', 'uvim1006.tab:6876', 'uvim1006.tab:6938', 'uvim1006.tab:7000', 'uvim1006.tab:7062']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5080', 'uvim1006.tab:5082', 'uvim1006.tab:5083', 'uvim1006.tab:5084', 'uvim1006.tab:5326', 'uvim1006.tab:5388', 'uvim1006.tab:5450', 'uvim1006.tab:5512', 'uvim1006.tab:5574', 'uvim1006.tab:5636', 'uvim1006.tab:5698', 'uvim1006.tab:5760', 'uvim1006.tab:5822', 'uvim1006.tab:5884', 'uvim1006.tab:5946', 'uvim1006.tab:6008', 'uvim1006.tab:6070', 'uvim1006.tab:6132', 'uvim1006.tab:6194', 'uvim1006.tab:6256', 'uvim1006.tab:6318', 'uvim1006.tab:6380', 'uvim1006.tab:6442', 'uvim1006.tab:6504', 'uvim1006.tab:6566', 'uvim1006.tab:6628', 'uvim1006.tab:6690', 'uvim1006.tab:6752', 'uvim1006.tab:6814', 'uvim1006.tab:6876', 'uvim1006.tab:6938', 'uvim1006.tab:7000', 'uvim1006.tab:7062']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5081', 'uvim1006.tab:7124', 'uvim1006.tab:7186']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5081', 'uvim1006.tab:7124', 'uvim1006.tab:7186']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5085', 'uvim1006.tab:5086', 'uvim1006.tab:5087', 'uvim1006.tab:5088', 'uvim1006.tab:5089', 'uvim1006.tab:5327', 'uvim1006.tab:5389', 'uvim1006.tab:5451', 'uvim1006.tab:5513', 'uvim1006.tab:5575', 'uvim1006.tab:5637', 'uvim1006.tab:5699', 'uvim1006.tab:5761', 'uvim1006.tab:5823', 'uvim1006.tab:5885', 'uvim1006.tab:5947', 'uvim1006.tab:6009', 'uvim1006.tab:6071', 'uvim1006.tab:6133', 'uvim1006.tab:6195', 'uvim1006.tab:6257', 'uvim1006.tab:6319', 'uvim1006.tab:6381', 'uvim1006.tab:6443', 'uvim1006.tab:6505', 'uvim1006.tab:6567', 'uvim1006.tab:6629', 'uvim1006.tab:6691', 'uvim1006.tab:6753', 'uvim1006.tab:6815', 'uvim1006.tab:6877', 'uvim1006.tab:6939', 'uvim1006.tab:7001', 'uvim1006.tab:7063', 'uvim1006.tab:7125', 'uvim1006.tab:7187']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5085', 'uvim1006.tab:5086', 'uvim1006.tab:5087', 'uvim1006.tab:5088', 'uvim1006.tab:5089', 'uvim1006.tab:5327', 'uvim1006.tab:5389', 'uvim1006.tab:5451', 'uvim1006.tab:5513', 'uvim1006.tab:5575', 'uvim1006.tab:5637', 'uvim1006.tab:5699', 'uvim1006.tab:5761', 'uvim1006.tab:5823', 'uvim1006.tab:5885', 'uvim1006.tab:5947', 'uvim1006.tab:6009', 'uvim1006.tab:6071', 'uvim1006.tab:6133', 'uvim1006.tab:6195', 'uvim1006.tab:6257', 'uvim1006.tab:6319', 'uvim1006.tab:6381', 'uvim1006.tab:6443', 'uvim1006.tab:6505', 'uvim1006.tab:6567', 'uvim1006.tab:6629', 'uvim1006.tab:6691', 'uvim1006.tab:6753', 'uvim1006.tab:6815', 'uvim1006.tab:6877', 'uvim1006.tab:6939', 'uvim1006.tab:7001', 'uvim1006.tab:7063', 'uvim1006.tab:7125', 'uvim1006.tab:7187']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5085', 'uvim1006.tab:5087', 'uvim1006.tab:5088', 'uvim1006.tab:5089', 'uvim1006.tab:5327', 'uvim1006.tab:5389', 'uvim1006.tab:5451', 'uvim1006.tab:5513', 'uvim1006.tab:5575', 'uvim1006.tab:5637', 'uvim1006.tab:5699', 'uvim1006.tab:5761', 'uvim1006.tab:5823', 'uvim1006.tab:5885', 'uvim1006.tab:5947', 'uvim1006.tab:6009', 'uvim1006.tab:6071', 'uvim1006.tab:6133', 'uvim1006.tab:6195', 'uvim1006.tab:6257', 'uvim1006.tab:6319', 'uvim1006.tab:6381', 'uvim1006.tab:6443', 'uvim1006.tab:6505', 'uvim1006.tab:6567', 'uvim1006.tab:6629', 'uvim1006.tab:6691', 'uvim1006.tab:6753', 'uvim1006.tab:6815', 'uvim1006.tab:6877', 'uvim1006.tab:6939', 'uvim1006.tab:7001', 'uvim1006.tab:7063']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5085', 'uvim1006.tab:5087', 'uvim1006.tab:5088', 'uvim1006.tab:5089', 'uvim1006.tab:5327', 'uvim1006.tab:5389', 'uvim1006.tab:5451', 'uvim1006.tab:5513', 'uvim1006.tab:5575', 'uvim1006.tab:5637', 'uvim1006.tab:5699', 'uvim1006.tab:5761', 'uvim1006.tab:5823', 'uvim1006.tab:5885', 'uvim1006.tab:5947', 'uvim1006.tab:6009', 'uvim1006.tab:6071', 'uvim1006.tab:6133', 'uvim1006.tab:6195', 'uvim1006.tab:6257', 'uvim1006.tab:6319', 'uvim1006.tab:6381', 'uvim1006.tab:6443', 'uvim1006.tab:6505', 'uvim1006.tab:6567', 'uvim1006.tab:6629', 'uvim1006.tab:6691', 'uvim1006.tab:6753', 'uvim1006.tab:6815', 'uvim1006.tab:6877', 'uvim1006.tab:6939', 'uvim1006.tab:7001', 'uvim1006.tab:7063']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5086', 'uvim1006.tab:7125', 'uvim1006.tab:7187']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5086', 'uvim1006.tab:7125', 'uvim1006.tab:7187']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5090', 'uvim1006.tab:5091', 'uvim1006.tab:5092', 'uvim1006.tab:5093', 'uvim1006.tab:5094', 'uvim1006.tab:5328', 'uvim1006.tab:5390', 'uvim1006.tab:5452', 'uvim1006.tab:5514', 'uvim1006.tab:5576', 'uvim1006.tab:5638', 'uvim1006.tab:5700', 'uvim1006.tab:5762', 'uvim1006.tab:5824', 'uvim1006.tab:5886', 'uvim1006.tab:5948', 'uvim1006.tab:6010', 'uvim1006.tab:6072', 'uvim1006.tab:6134', 'uvim1006.tab:6196', 'uvim1006.tab:6258', 'uvim1006.tab:6320', 'uvim1006.tab:6382', 'uvim1006.tab:6444', 'uvim1006.tab:6506', 'uvim1006.tab:6568', 'uvim1006.tab:6630', 'uvim1006.tab:6692', 'uvim1006.tab:6754', 'uvim1006.tab:6816', 'uvim1006.tab:6878', 'uvim1006.tab:6940', 'uvim1006.tab:7002', 'uvim1006.tab:7064', 'uvim1006.tab:7126', 'uvim1006.tab:7188']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5090', 'uvim1006.tab:5091', 'uvim1006.tab:5092', 'uvim1006.tab:5093', 'uvim1006.tab:5094', 'uvim1006.tab:5328', 'uvim1006.tab:5390', 'uvim1006.tab:5452', 'uvim1006.tab:5514', 'uvim1006.tab:5576', 'uvim1006.tab:5638', 'uvim1006.tab:5700', 'uvim1006.tab:5762', 'uvim1006.tab:5824', 'uvim1006.tab:5886', 'uvim1006.tab:5948', 'uvim1006.tab:6010', 'uvim1006.tab:6072', 'uvim1006.tab:6134', 'uvim1006.tab:6196', 'uvim1006.tab:6258', 'uvim1006.tab:6320', 'uvim1006.tab:6382', 'uvim1006.tab:6444', 'uvim1006.tab:6506', 'uvim1006.tab:6568', 'uvim1006.tab:6630', 'uvim1006.tab:6692', 'uvim1006.tab:6754', 'uvim1006.tab:6816', 'uvim1006.tab:6878', 'uvim1006.tab:6940', 'uvim1006.tab:7002', 'uvim1006.tab:7064', 'uvim1006.tab:7126', 'uvim1006.tab:7188']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5090', 'uvim1006.tab:5092', 'uvim1006.tab:5093', 'uvim1006.tab:5094', 'uvim1006.tab:5328', 'uvim1006.tab:5390', 'uvim1006.tab:5452', 'uvim1006.tab:5514', 'uvim1006.tab:5576', 'uvim1006.tab:5638', 'uvim1006.tab:5700', 'uvim1006.tab:5762', 'uvim1006.tab:5824', 'uvim1006.tab:5886', 'uvim1006.tab:5948', 'uvim1006.tab:6010', 'uvim1006.tab:6072', 'uvim1006.tab:6134', 'uvim1006.tab:6196', 'uvim1006.tab:6258', 'uvim1006.tab:6320', 'uvim1006.tab:6382', 'uvim1006.tab:6444', 'uvim1006.tab:6506', 'uvim1006.tab:6568', 'uvim1006.tab:6630', 'uvim1006.tab:6692', 'uvim1006.tab:6754', 'uvim1006.tab:6816', 'uvim1006.tab:6878', 'uvim1006.tab:6940', 'uvim1006.tab:7002', 'uvim1006.tab:7064']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5090', 'uvim1006.tab:5092', 'uvim1006.tab:5093', 'uvim1006.tab:5094', 'uvim1006.tab:5328', 'uvim1006.tab:5390', 'uvim1006.tab:5452', 'uvim1006.tab:5514', 'uvim1006.tab:5576', 'uvim1006.tab:5638', 'uvim1006.tab:5700', 'uvim1006.tab:5762', 'uvim1006.tab:5824', 'uvim1006.tab:5886', 'uvim1006.tab:5948', 'uvim1006.tab:6010', 'uvim1006.tab:6072', 'uvim1006.tab:6134', 'uvim1006.tab:6196', 'uvim1006.tab:6258', 'uvim1006.tab:6320', 'uvim1006.tab:6382', 'uvim1006.tab:6444', 'uvim1006.tab:6506', 'uvim1006.tab:6568', 'uvim1006.tab:6630', 'uvim1006.tab:6692', 'uvim1006.tab:6754', 'uvim1006.tab:6816', 'uvim1006.tab:6878', 'uvim1006.tab:6940', 'uvim1006.tab:7002', 'uvim1006.tab:7064']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5091', 'uvim1006.tab:7126', 'uvim1006.tab:7188']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5091', 'uvim1006.tab:7126', 'uvim1006.tab:7188']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5095', 'uvim1006.tab:5096', 'uvim1006.tab:5097', 'uvim1006.tab:5098', 'uvim1006.tab:5099', 'uvim1006.tab:5329', 'uvim1006.tab:5391', 'uvim1006.tab:5453', 'uvim1006.tab:5515', 'uvim1006.tab:5577', 'uvim1006.tab:5639', 'uvim1006.tab:5701', 'uvim1006.tab:5763', 'uvim1006.tab:5825', 'uvim1006.tab:5887', 'uvim1006.tab:5949', 'uvim1006.tab:6011', 'uvim1006.tab:6073', 'uvim1006.tab:6135', 'uvim1006.tab:6197', 'uvim1006.tab:6259', 'uvim1006.tab:6321', 'uvim1006.tab:6383', 'uvim1006.tab:6445', 'uvim1006.tab:6507', 'uvim1006.tab:6569', 'uvim1006.tab:6631', 'uvim1006.tab:6693', 'uvim1006.tab:6755', 'uvim1006.tab:6817', 'uvim1006.tab:6879', 'uvim1006.tab:6941', 'uvim1006.tab:7003', 'uvim1006.tab:7065', 'uvim1006.tab:7127', 'uvim1006.tab:7189']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5095', 'uvim1006.tab:5096', 'uvim1006.tab:5097', 'uvim1006.tab:5098', 'uvim1006.tab:5099', 'uvim1006.tab:5329', 'uvim1006.tab:5391', 'uvim1006.tab:5453', 'uvim1006.tab:5515', 'uvim1006.tab:5577', 'uvim1006.tab:5639', 'uvim1006.tab:5701', 'uvim1006.tab:5763', 'uvim1006.tab:5825', 'uvim1006.tab:5887', 'uvim1006.tab:5949', 'uvim1006.tab:6011', 'uvim1006.tab:6073', 'uvim1006.tab:6135', 'uvim1006.tab:6197', 'uvim1006.tab:6259', 'uvim1006.tab:6321', 'uvim1006.tab:6383', 'uvim1006.tab:6445', 'uvim1006.tab:6507', 'uvim1006.tab:6569', 'uvim1006.tab:6631', 'uvim1006.tab:6693', 'uvim1006.tab:6755', 'uvim1006.tab:6817', 'uvim1006.tab:6879', 'uvim1006.tab:6941', 'uvim1006.tab:7003', 'uvim1006.tab:7065', 'uvim1006.tab:7127', 'uvim1006.tab:7189']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5095', 'uvim1006.tab:5097', 'uvim1006.tab:5098', 'uvim1006.tab:5099', 'uvim1006.tab:5329', 'uvim1006.tab:5391', 'uvim1006.tab:5453', 'uvim1006.tab:5515', 'uvim1006.tab:5577', 'uvim1006.tab:5639', 'uvim1006.tab:5701', 'uvim1006.tab:5763', 'uvim1006.tab:5825', 'uvim1006.tab:5887', 'uvim1006.tab:5949', 'uvim1006.tab:6011', 'uvim1006.tab:6073', 'uvim1006.tab:6135', 'uvim1006.tab:6197', 'uvim1006.tab:6259', 'uvim1006.tab:6321', 'uvim1006.tab:6383', 'uvim1006.tab:6445', 'uvim1006.tab:6507', 'uvim1006.tab:6569', 'uvim1006.tab:6631', 'uvim1006.tab:6693', 'uvim1006.tab:6755', 'uvim1006.tab:6817', 'uvim1006.tab:6879', 'uvim1006.tab:6941', 'uvim1006.tab:7003', 'uvim1006.tab:7065']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5095', 'uvim1006.tab:5097', 'uvim1006.tab:5098', 'uvim1006.tab:5099', 'uvim1006.tab:5329', 'uvim1006.tab:5391', 'uvim1006.tab:5453', 'uvim1006.tab:5515', 'uvim1006.tab:5577', 'uvim1006.tab:5639', 'uvim1006.tab:5701', 'uvim1006.tab:5763', 'uvim1006.tab:5825', 'uvim1006.tab:5887', 'uvim1006.tab:5949', 'uvim1006.tab:6011', 'uvim1006.tab:6073', 'uvim1006.tab:6135', 'uvim1006.tab:6197', 'uvim1006.tab:6259', 'uvim1006.tab:6321', 'uvim1006.tab:6383', 'uvim1006.tab:6445', 'uvim1006.tab:6507', 'uvim1006.tab:6569', 'uvim1006.tab:6631', 'uvim1006.tab:6693', 'uvim1006.tab:6755', 'uvim1006.tab:6817', 'uvim1006.tab:6879', 'uvim1006.tab:6941', 'uvim1006.tab:7003', 'uvim1006.tab:7065']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5096', 'uvim1006.tab:7127', 'uvim1006.tab:7189']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5096', 'uvim1006.tab:7127', 'uvim1006.tab:7189']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5100', 'uvim1006.tab:5101', 'uvim1006.tab:5102', 'uvim1006.tab:5103', 'uvim1006.tab:5104', 'uvim1006.tab:5330', 'uvim1006.tab:5392', 'uvim1006.tab:5454', 'uvim1006.tab:5516', 'uvim1006.tab:5578', 'uvim1006.tab:5640', 'uvim1006.tab:5702', 'uvim1006.tab:5764', 'uvim1006.tab:5826', 'uvim1006.tab:5888', 'uvim1006.tab:5950', 'uvim1006.tab:6012', 'uvim1006.tab:6074', 'uvim1006.tab:6136', 'uvim1006.tab:6198', 'uvim1006.tab:6260', 'uvim1006.tab:6322', 'uvim1006.tab:6384', 'uvim1006.tab:6446', 'uvim1006.tab:6508', 'uvim1006.tab:6570', 'uvim1006.tab:6632', 'uvim1006.tab:6694', 'uvim1006.tab:6756', 'uvim1006.tab:6818', 'uvim1006.tab:6880', 'uvim1006.tab:6942', 'uvim1006.tab:7004', 'uvim1006.tab:7066', 'uvim1006.tab:7128', 'uvim1006.tab:7190']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5100', 'uvim1006.tab:5101', 'uvim1006.tab:5102', 'uvim1006.tab:5103', 'uvim1006.tab:5104', 'uvim1006.tab:5330', 'uvim1006.tab:5392', 'uvim1006.tab:5454', 'uvim1006.tab:5516', 'uvim1006.tab:5578', 'uvim1006.tab:5640', 'uvim1006.tab:5702', 'uvim1006.tab:5764', 'uvim1006.tab:5826', 'uvim1006.tab:5888', 'uvim1006.tab:5950', 'uvim1006.tab:6012', 'uvim1006.tab:6074', 'uvim1006.tab:6136', 'uvim1006.tab:6198', 'uvim1006.tab:6260', 'uvim1006.tab:6322', 'uvim1006.tab:6384', 'uvim1006.tab:6446', 'uvim1006.tab:6508', 'uvim1006.tab:6570', 'uvim1006.tab:6632', 'uvim1006.tab:6694', 'uvim1006.tab:6756', 'uvim1006.tab:6818', 'uvim1006.tab:6880', 'uvim1006.tab:6942', 'uvim1006.tab:7004', 'uvim1006.tab:7066', 'uvim1006.tab:7128', 'uvim1006.tab:7190']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5100', 'uvim1006.tab:5102', 'uvim1006.tab:5103', 'uvim1006.tab:5104', 'uvim1006.tab:5330', 'uvim1006.tab:5392', 'uvim1006.tab:5454', 'uvim1006.tab:5516', 'uvim1006.tab:5578', 'uvim1006.tab:5640', 'uvim1006.tab:5702', 'uvim1006.tab:5764', 'uvim1006.tab:5826', 'uvim1006.tab:5888', 'uvim1006.tab:5950', 'uvim1006.tab:6012', 'uvim1006.tab:6074', 'uvim1006.tab:6136', 'uvim1006.tab:6198', 'uvim1006.tab:6260', 'uvim1006.tab:6322', 'uvim1006.tab:6384', 'uvim1006.tab:6446', 'uvim1006.tab:6508', 'uvim1006.tab:6570', 'uvim1006.tab:6632', 'uvim1006.tab:6694', 'uvim1006.tab:6756', 'uvim1006.tab:6818', 'uvim1006.tab:6880', 'uvim1006.tab:6942', 'uvim1006.tab:7004', 'uvim1006.tab:7066']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5100', 'uvim1006.tab:5102', 'uvim1006.tab:5103', 'uvim1006.tab:5104', 'uvim1006.tab:5330', 'uvim1006.tab:5392', 'uvim1006.tab:5454', 'uvim1006.tab:5516', 'uvim1006.tab:5578', 'uvim1006.tab:5640', 'uvim1006.tab:5702', 'uvim1006.tab:5764', 'uvim1006.tab:5826', 'uvim1006.tab:5888', 'uvim1006.tab:5950', 'uvim1006.tab:6012', 'uvim1006.tab:6074', 'uvim1006.tab:6136', 'uvim1006.tab:6198', 'uvim1006.tab:6260', 'uvim1006.tab:6322', 'uvim1006.tab:6384', 'uvim1006.tab:6446', 'uvim1006.tab:6508', 'uvim1006.tab:6570', 'uvim1006.tab:6632', 'uvim1006.tab:6694', 'uvim1006.tab:6756', 'uvim1006.tab:6818', 'uvim1006.tab:6880', 'uvim1006.tab:6942', 'uvim1006.tab:7004', 'uvim1006.tab:7066']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5101', 'uvim1006.tab:7128', 'uvim1006.tab:7190']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5101', 'uvim1006.tab:7128', 'uvim1006.tab:7190']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5105', 'uvim1006.tab:5106', 'uvim1006.tab:5107', 'uvim1006.tab:5108', 'uvim1006.tab:5109', 'uvim1006.tab:5331', 'uvim1006.tab:5393', 'uvim1006.tab:5455', 'uvim1006.tab:5517', 'uvim1006.tab:5579', 'uvim1006.tab:5641', 'uvim1006.tab:5703', 'uvim1006.tab:5765', 'uvim1006.tab:5827', 'uvim1006.tab:5889', 'uvim1006.tab:5951', 'uvim1006.tab:6013', 'uvim1006.tab:6075', 'uvim1006.tab:6137', 'uvim1006.tab:6199', 'uvim1006.tab:6261', 'uvim1006.tab:6323', 'uvim1006.tab:6385', 'uvim1006.tab:6447', 'uvim1006.tab:6509', 'uvim1006.tab:6571', 'uvim1006.tab:6633', 'uvim1006.tab:6695', 'uvim1006.tab:6757', 'uvim1006.tab:6819', 'uvim1006.tab:6881', 'uvim1006.tab:6943', 'uvim1006.tab:7005', 'uvim1006.tab:7067', 'uvim1006.tab:7129', 'uvim1006.tab:7191']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5105', 'uvim1006.tab:5106', 'uvim1006.tab:5107', 'uvim1006.tab:5108', 'uvim1006.tab:5109', 'uvim1006.tab:5331', 'uvim1006.tab:5393', 'uvim1006.tab:5455', 'uvim1006.tab:5517', 'uvim1006.tab:5579', 'uvim1006.tab:5641', 'uvim1006.tab:5703', 'uvim1006.tab:5765', 'uvim1006.tab:5827', 'uvim1006.tab:5889', 'uvim1006.tab:5951', 'uvim1006.tab:6013', 'uvim1006.tab:6075', 'uvim1006.tab:6137', 'uvim1006.tab:6199', 'uvim1006.tab:6261', 'uvim1006.tab:6323', 'uvim1006.tab:6385', 'uvim1006.tab:6447', 'uvim1006.tab:6509', 'uvim1006.tab:6571', 'uvim1006.tab:6633', 'uvim1006.tab:6695', 'uvim1006.tab:6757', 'uvim1006.tab:6819', 'uvim1006.tab:6881', 'uvim1006.tab:6943', 'uvim1006.tab:7005', 'uvim1006.tab:7067', 'uvim1006.tab:7129', 'uvim1006.tab:7191']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5105', 'uvim1006.tab:5107', 'uvim1006.tab:5108', 'uvim1006.tab:5109', 'uvim1006.tab:5331', 'uvim1006.tab:5393', 'uvim1006.tab:5455', 'uvim1006.tab:5517', 'uvim1006.tab:5579', 'uvim1006.tab:5641', 'uvim1006.tab:5703', 'uvim1006.tab:5765', 'uvim1006.tab:5827', 'uvim1006.tab:5889', 'uvim1006.tab:5951', 'uvim1006.tab:6013', 'uvim1006.tab:6075', 'uvim1006.tab:6137', 'uvim1006.tab:6199', 'uvim1006.tab:6261', 'uvim1006.tab:6323', 'uvim1006.tab:6385', 'uvim1006.tab:6447', 'uvim1006.tab:6509', 'uvim1006.tab:6571', 'uvim1006.tab:6633', 'uvim1006.tab:6695', 'uvim1006.tab:6757', 'uvim1006.tab:6819', 'uvim1006.tab:6881', 'uvim1006.tab:6943', 'uvim1006.tab:7005', 'uvim1006.tab:7067']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5105', 'uvim1006.tab:5107', 'uvim1006.tab:5108', 'uvim1006.tab:5109', 'uvim1006.tab:5331', 'uvim1006.tab:5393', 'uvim1006.tab:5455', 'uvim1006.tab:5517', 'uvim1006.tab:5579', 'uvim1006.tab:5641', 'uvim1006.tab:5703', 'uvim1006.tab:5765', 'uvim1006.tab:5827', 'uvim1006.tab:5889', 'uvim1006.tab:5951', 'uvim1006.tab:6013', 'uvim1006.tab:6075', 'uvim1006.tab:6137', 'uvim1006.tab:6199', 'uvim1006.tab:6261', 'uvim1006.tab:6323', 'uvim1006.tab:6385', 'uvim1006.tab:6447', 'uvim1006.tab:6509', 'uvim1006.tab:6571', 'uvim1006.tab:6633', 'uvim1006.tab:6695', 'uvim1006.tab:6757', 'uvim1006.tab:6819', 'uvim1006.tab:6881', 'uvim1006.tab:6943', 'uvim1006.tab:7005', 'uvim1006.tab:7067']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5106', 'uvim1006.tab:7129', 'uvim1006.tab:7191']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5106', 'uvim1006.tab:7129', 'uvim1006.tab:7191']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5110', 'uvim1006.tab:5111', 'uvim1006.tab:5112', 'uvim1006.tab:5113', 'uvim1006.tab:5114', 'uvim1006.tab:5332', 'uvim1006.tab:5394', 'uvim1006.tab:5456', 'uvim1006.tab:5518', 'uvim1006.tab:5580', 'uvim1006.tab:5642', 'uvim1006.tab:5704', 'uvim1006.tab:5766', 'uvim1006.tab:5828', 'uvim1006.tab:5890', 'uvim1006.tab:5952', 'uvim1006.tab:6014', 'uvim1006.tab:6076', 'uvim1006.tab:6138', 'uvim1006.tab:6200', 'uvim1006.tab:6262', 'uvim1006.tab:6324', 'uvim1006.tab:6386', 'uvim1006.tab:6448', 'uvim1006.tab:6510', 'uvim1006.tab:6572', 'uvim1006.tab:6634', 'uvim1006.tab:6696', 'uvim1006.tab:6758', 'uvim1006.tab:6820', 'uvim1006.tab:6882', 'uvim1006.tab:6944', 'uvim1006.tab:7006', 'uvim1006.tab:7068', 'uvim1006.tab:7130', 'uvim1006.tab:7192']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5110', 'uvim1006.tab:5111', 'uvim1006.tab:5112', 'uvim1006.tab:5113', 'uvim1006.tab:5114', 'uvim1006.tab:5332', 'uvim1006.tab:5394', 'uvim1006.tab:5456', 'uvim1006.tab:5518', 'uvim1006.tab:5580', 'uvim1006.tab:5642', 'uvim1006.tab:5704', 'uvim1006.tab:5766', 'uvim1006.tab:5828', 'uvim1006.tab:5890', 'uvim1006.tab:5952', 'uvim1006.tab:6014', 'uvim1006.tab:6076', 'uvim1006.tab:6138', 'uvim1006.tab:6200', 'uvim1006.tab:6262', 'uvim1006.tab:6324', 'uvim1006.tab:6386', 'uvim1006.tab:6448', 'uvim1006.tab:6510', 'uvim1006.tab:6572', 'uvim1006.tab:6634', 'uvim1006.tab:6696', 'uvim1006.tab:6758', 'uvim1006.tab:6820', 'uvim1006.tab:6882', 'uvim1006.tab:6944', 'uvim1006.tab:7006', 'uvim1006.tab:7068', 'uvim1006.tab:7130', 'uvim1006.tab:7192']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5110', 'uvim1006.tab:5112', 'uvim1006.tab:5113', 'uvim1006.tab:5114', 'uvim1006.tab:5332', 'uvim1006.tab:5394', 'uvim1006.tab:5456', 'uvim1006.tab:5518', 'uvim1006.tab:5580', 'uvim1006.tab:5642', 'uvim1006.tab:5704', 'uvim1006.tab:5766', 'uvim1006.tab:5828', 'uvim1006.tab:5890', 'uvim1006.tab:5952', 'uvim1006.tab:6014', 'uvim1006.tab:6076', 'uvim1006.tab:6138', 'uvim1006.tab:6200', 'uvim1006.tab:6262', 'uvim1006.tab:6324', 'uvim1006.tab:6386', 'uvim1006.tab:6448', 'uvim1006.tab:6510', 'uvim1006.tab:6572', 'uvim1006.tab:6634', 'uvim1006.tab:6696', 'uvim1006.tab:6758', 'uvim1006.tab:6820', 'uvim1006.tab:6882', 'uvim1006.tab:6944', 'uvim1006.tab:7006', 'uvim1006.tab:7068']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5110', 'uvim1006.tab:5112', 'uvim1006.tab:5113', 'uvim1006.tab:5114', 'uvim1006.tab:5332', 'uvim1006.tab:5394', 'uvim1006.tab:5456', 'uvim1006.tab:5518', 'uvim1006.tab:5580', 'uvim1006.tab:5642', 'uvim1006.tab:5704', 'uvim1006.tab:5766', 'uvim1006.tab:5828', 'uvim1006.tab:5890', 'uvim1006.tab:5952', 'uvim1006.tab:6014', 'uvim1006.tab:6076', 'uvim1006.tab:6138', 'uvim1006.tab:6200', 'uvim1006.tab:6262', 'uvim1006.tab:6324', 'uvim1006.tab:6386', 'uvim1006.tab:6448', 'uvim1006.tab:6510', 'uvim1006.tab:6572', 'uvim1006.tab:6634', 'uvim1006.tab:6696', 'uvim1006.tab:6758', 'uvim1006.tab:6820', 'uvim1006.tab:6882', 'uvim1006.tab:6944', 'uvim1006.tab:7006', 'uvim1006.tab:7068']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5111', 'uvim1006.tab:7130', 'uvim1006.tab:7192']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5111', 'uvim1006.tab:7130', 'uvim1006.tab:7192']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5115', 'uvim1006.tab:5116', 'uvim1006.tab:5117', 'uvim1006.tab:5118', 'uvim1006.tab:5119', 'uvim1006.tab:5333', 'uvim1006.tab:5395', 'uvim1006.tab:5457', 'uvim1006.tab:5519', 'uvim1006.tab:5581', 'uvim1006.tab:5643', 'uvim1006.tab:5705', 'uvim1006.tab:5767', 'uvim1006.tab:5829', 'uvim1006.tab:5891', 'uvim1006.tab:5953', 'uvim1006.tab:6015', 'uvim1006.tab:6077', 'uvim1006.tab:6139', 'uvim1006.tab:6201', 'uvim1006.tab:6263', 'uvim1006.tab:6325', 'uvim1006.tab:6387', 'uvim1006.tab:6449', 'uvim1006.tab:6511', 'uvim1006.tab:6573', 'uvim1006.tab:6635', 'uvim1006.tab:6697', 'uvim1006.tab:6759', 'uvim1006.tab:6821', 'uvim1006.tab:6883', 'uvim1006.tab:6945', 'uvim1006.tab:7007', 'uvim1006.tab:7069', 'uvim1006.tab:7131', 'uvim1006.tab:7193']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5115', 'uvim1006.tab:5116', 'uvim1006.tab:5117', 'uvim1006.tab:5118', 'uvim1006.tab:5119', 'uvim1006.tab:5333', 'uvim1006.tab:5395', 'uvim1006.tab:5457', 'uvim1006.tab:5519', 'uvim1006.tab:5581', 'uvim1006.tab:5643', 'uvim1006.tab:5705', 'uvim1006.tab:5767', 'uvim1006.tab:5829', 'uvim1006.tab:5891', 'uvim1006.tab:5953', 'uvim1006.tab:6015', 'uvim1006.tab:6077', 'uvim1006.tab:6139', 'uvim1006.tab:6201', 'uvim1006.tab:6263', 'uvim1006.tab:6325', 'uvim1006.tab:6387', 'uvim1006.tab:6449', 'uvim1006.tab:6511', 'uvim1006.tab:6573', 'uvim1006.tab:6635', 'uvim1006.tab:6697', 'uvim1006.tab:6759', 'uvim1006.tab:6821', 'uvim1006.tab:6883', 'uvim1006.tab:6945', 'uvim1006.tab:7007', 'uvim1006.tab:7069', 'uvim1006.tab:7131', 'uvim1006.tab:7193']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5115', 'uvim1006.tab:5117', 'uvim1006.tab:5118', 'uvim1006.tab:5119', 'uvim1006.tab:5333', 'uvim1006.tab:5395', 'uvim1006.tab:5457', 'uvim1006.tab:5519', 'uvim1006.tab:5581', 'uvim1006.tab:5643', 'uvim1006.tab:5705', 'uvim1006.tab:5767', 'uvim1006.tab:5829', 'uvim1006.tab:5891', 'uvim1006.tab:5953', 'uvim1006.tab:6015', 'uvim1006.tab:6077', 'uvim1006.tab:6139', 'uvim1006.tab:6201', 'uvim1006.tab:6263', 'uvim1006.tab:6325', 'uvim1006.tab:6387', 'uvim1006.tab:6449', 'uvim1006.tab:6511', 'uvim1006.tab:6573', 'uvim1006.tab:6635', 'uvim1006.tab:6697', 'uvim1006.tab:6759', 'uvim1006.tab:6821', 'uvim1006.tab:6883', 'uvim1006.tab:6945', 'uvim1006.tab:7007', 'uvim1006.tab:7069']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5115', 'uvim1006.tab:5117', 'uvim1006.tab:5118', 'uvim1006.tab:5119', 'uvim1006.tab:5333', 'uvim1006.tab:5395', 'uvim1006.tab:5457', 'uvim1006.tab:5519', 'uvim1006.tab:5581', 'uvim1006.tab:5643', 'uvim1006.tab:5705', 'uvim1006.tab:5767', 'uvim1006.tab:5829', 'uvim1006.tab:5891', 'uvim1006.tab:5953', 'uvim1006.tab:6015', 'uvim1006.tab:6077', 'uvim1006.tab:6139', 'uvim1006.tab:6201', 'uvim1006.tab:6263', 'uvim1006.tab:6325', 'uvim1006.tab:6387', 'uvim1006.tab:6449', 'uvim1006.tab:6511', 'uvim1006.tab:6573', 'uvim1006.tab:6635', 'uvim1006.tab:6697', 'uvim1006.tab:6759', 'uvim1006.tab:6821', 'uvim1006.tab:6883', 'uvim1006.tab:6945', 'uvim1006.tab:7007', 'uvim1006.tab:7069']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5116', 'uvim1006.tab:7131', 'uvim1006.tab:7193']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5116', 'uvim1006.tab:7131', 'uvim1006.tab:7193']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5120', 'uvim1006.tab:5121', 'uvim1006.tab:5122', 'uvim1006.tab:5123', 'uvim1006.tab:5124', 'uvim1006.tab:5334', 'uvim1006.tab:5396', 'uvim1006.tab:5458', 'uvim1006.tab:5520', 'uvim1006.tab:5582', 'uvim1006.tab:5644', 'uvim1006.tab:5706', 'uvim1006.tab:5768', 'uvim1006.tab:5830', 'uvim1006.tab:5892', 'uvim1006.tab:5954', 'uvim1006.tab:6016', 'uvim1006.tab:6078', 'uvim1006.tab:6140', 'uvim1006.tab:6202', 'uvim1006.tab:6264', 'uvim1006.tab:6326', 'uvim1006.tab:6388', 'uvim1006.tab:6450', 'uvim1006.tab:6512', 'uvim1006.tab:6574', 'uvim1006.tab:6636', 'uvim1006.tab:6698', 'uvim1006.tab:6760', 'uvim1006.tab:6822', 'uvim1006.tab:6884', 'uvim1006.tab:6946', 'uvim1006.tab:7008', 'uvim1006.tab:7070', 'uvim1006.tab:7132', 'uvim1006.tab:7194']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5120', 'uvim1006.tab:5121', 'uvim1006.tab:5122', 'uvim1006.tab:5123', 'uvim1006.tab:5124', 'uvim1006.tab:5334', 'uvim1006.tab:5396', 'uvim1006.tab:5458', 'uvim1006.tab:5520', 'uvim1006.tab:5582', 'uvim1006.tab:5644', 'uvim1006.tab:5706', 'uvim1006.tab:5768', 'uvim1006.tab:5830', 'uvim1006.tab:5892', 'uvim1006.tab:5954', 'uvim1006.tab:6016', 'uvim1006.tab:6078', 'uvim1006.tab:6140', 'uvim1006.tab:6202', 'uvim1006.tab:6264', 'uvim1006.tab:6326', 'uvim1006.tab:6388', 'uvim1006.tab:6450', 'uvim1006.tab:6512', 'uvim1006.tab:6574', 'uvim1006.tab:6636', 'uvim1006.tab:6698', 'uvim1006.tab:6760', 'uvim1006.tab:6822', 'uvim1006.tab:6884', 'uvim1006.tab:6946', 'uvim1006.tab:7008', 'uvim1006.tab:7070', 'uvim1006.tab:7132', 'uvim1006.tab:7194']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5120', 'uvim1006.tab:5122', 'uvim1006.tab:5123', 'uvim1006.tab:5124', 'uvim1006.tab:5334', 'uvim1006.tab:5396', 'uvim1006.tab:5458', 'uvim1006.tab:5520', 'uvim1006.tab:5582', 'uvim1006.tab:5644', 'uvim1006.tab:5706', 'uvim1006.tab:5768', 'uvim1006.tab:5830', 'uvim1006.tab:5892', 'uvim1006.tab:5954', 'uvim1006.tab:6016', 'uvim1006.tab:6078', 'uvim1006.tab:6140', 'uvim1006.tab:6202', 'uvim1006.tab:6264', 'uvim1006.tab:6326', 'uvim1006.tab:6388', 'uvim1006.tab:6450', 'uvim1006.tab:6512', 'uvim1006.tab:6574', 'uvim1006.tab:6636', 'uvim1006.tab:6698', 'uvim1006.tab:6760', 'uvim1006.tab:6822', 'uvim1006.tab:6884', 'uvim1006.tab:6946', 'uvim1006.tab:7008', 'uvim1006.tab:7070']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5120', 'uvim1006.tab:5122', 'uvim1006.tab:5123', 'uvim1006.tab:5124', 'uvim1006.tab:5334', 'uvim1006.tab:5396', 'uvim1006.tab:5458', 'uvim1006.tab:5520', 'uvim1006.tab:5582', 'uvim1006.tab:5644', 'uvim1006.tab:5706', 'uvim1006.tab:5768', 'uvim1006.tab:5830', 'uvim1006.tab:5892', 'uvim1006.tab:5954', 'uvim1006.tab:6016', 'uvim1006.tab:6078', 'uvim1006.tab:6140', 'uvim1006.tab:6202', 'uvim1006.tab:6264', 'uvim1006.tab:6326', 'uvim1006.tab:6388', 'uvim1006.tab:6450', 'uvim1006.tab:6512', 'uvim1006.tab:6574', 'uvim1006.tab:6636', 'uvim1006.tab:6698', 'uvim1006.tab:6760', 'uvim1006.tab:6822', 'uvim1006.tab:6884', 'uvim1006.tab:6946', 'uvim1006.tab:7008', 'uvim1006.tab:7070']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5121', 'uvim1006.tab:7132', 'uvim1006.tab:7194']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5121', 'uvim1006.tab:7132', 'uvim1006.tab:7194']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5125', 'uvim1006.tab:5126', 'uvim1006.tab:5127', 'uvim1006.tab:5128', 'uvim1006.tab:5129', 'uvim1006.tab:5335', 'uvim1006.tab:5397', 'uvim1006.tab:5459', 'uvim1006.tab:5521', 'uvim1006.tab:5583', 'uvim1006.tab:5645', 'uvim1006.tab:5707', 'uvim1006.tab:5769', 'uvim1006.tab:5831', 'uvim1006.tab:5893', 'uvim1006.tab:5955', 'uvim1006.tab:6017', 'uvim1006.tab:6079', 'uvim1006.tab:6141', 'uvim1006.tab:6203', 'uvim1006.tab:6265', 'uvim1006.tab:6327', 'uvim1006.tab:6389', 'uvim1006.tab:6451', 'uvim1006.tab:6513', 'uvim1006.tab:6575', 'uvim1006.tab:6637', 'uvim1006.tab:6699', 'uvim1006.tab:6761', 'uvim1006.tab:6823', 'uvim1006.tab:6885', 'uvim1006.tab:6947', 'uvim1006.tab:7009', 'uvim1006.tab:7071', 'uvim1006.tab:7133', 'uvim1006.tab:7195']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5125', 'uvim1006.tab:5126', 'uvim1006.tab:5127', 'uvim1006.tab:5128', 'uvim1006.tab:5129', 'uvim1006.tab:5335', 'uvim1006.tab:5397', 'uvim1006.tab:5459', 'uvim1006.tab:5521', 'uvim1006.tab:5583', 'uvim1006.tab:5645', 'uvim1006.tab:5707', 'uvim1006.tab:5769', 'uvim1006.tab:5831', 'uvim1006.tab:5893', 'uvim1006.tab:5955', 'uvim1006.tab:6017', 'uvim1006.tab:6079', 'uvim1006.tab:6141', 'uvim1006.tab:6203', 'uvim1006.tab:6265', 'uvim1006.tab:6327', 'uvim1006.tab:6389', 'uvim1006.tab:6451', 'uvim1006.tab:6513', 'uvim1006.tab:6575', 'uvim1006.tab:6637', 'uvim1006.tab:6699', 'uvim1006.tab:6761', 'uvim1006.tab:6823', 'uvim1006.tab:6885', 'uvim1006.tab:6947', 'uvim1006.tab:7009', 'uvim1006.tab:7071', 'uvim1006.tab:7133', 'uvim1006.tab:7195']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5125', 'uvim1006.tab:5127', 'uvim1006.tab:5128', 'uvim1006.tab:5129', 'uvim1006.tab:5335', 'uvim1006.tab:5397', 'uvim1006.tab:5459', 'uvim1006.tab:5521', 'uvim1006.tab:5583', 'uvim1006.tab:5645', 'uvim1006.tab:5707', 'uvim1006.tab:5769', 'uvim1006.tab:5831', 'uvim1006.tab:5893', 'uvim1006.tab:5955', 'uvim1006.tab:6017', 'uvim1006.tab:6079', 'uvim1006.tab:6141', 'uvim1006.tab:6203', 'uvim1006.tab:6265', 'uvim1006.tab:6327', 'uvim1006.tab:6389', 'uvim1006.tab:6451', 'uvim1006.tab:6513', 'uvim1006.tab:6575', 'uvim1006.tab:6637', 'uvim1006.tab:6699', 'uvim1006.tab:6761', 'uvim1006.tab:6823', 'uvim1006.tab:6885', 'uvim1006.tab:6947', 'uvim1006.tab:7009', 'uvim1006.tab:7071']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5125', 'uvim1006.tab:5127', 'uvim1006.tab:5128', 'uvim1006.tab:5129', 'uvim1006.tab:5335', 'uvim1006.tab:5397', 'uvim1006.tab:5459', 'uvim1006.tab:5521', 'uvim1006.tab:5583', 'uvim1006.tab:5645', 'uvim1006.tab:5707', 'uvim1006.tab:5769', 'uvim1006.tab:5831', 'uvim1006.tab:5893', 'uvim1006.tab:5955', 'uvim1006.tab:6017', 'uvim1006.tab:6079', 'uvim1006.tab:6141', 'uvim1006.tab:6203', 'uvim1006.tab:6265', 'uvim1006.tab:6327', 'uvim1006.tab:6389', 'uvim1006.tab:6451', 'uvim1006.tab:6513', 'uvim1006.tab:6575', 'uvim1006.tab:6637', 'uvim1006.tab:6699', 'uvim1006.tab:6761', 'uvim1006.tab:6823', 'uvim1006.tab:6885', 'uvim1006.tab:6947', 'uvim1006.tab:7009', 'uvim1006.tab:7071']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5126', 'uvim1006.tab:7133', 'uvim1006.tab:7195']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5126', 'uvim1006.tab:7133', 'uvim1006.tab:7195']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5130', 'uvim1006.tab:5131', 'uvim1006.tab:5132', 'uvim1006.tab:5133', 'uvim1006.tab:5134', 'uvim1006.tab:5336', 'uvim1006.tab:5398', 'uvim1006.tab:5460', 'uvim1006.tab:5522', 'uvim1006.tab:5584', 'uvim1006.tab:5646', 'uvim1006.tab:5708', 'uvim1006.tab:5770', 'uvim1006.tab:5832', 'uvim1006.tab:5894', 'uvim1006.tab:5956', 'uvim1006.tab:6018', 'uvim1006.tab:6080', 'uvim1006.tab:6142', 'uvim1006.tab:6204', 'uvim1006.tab:6266', 'uvim1006.tab:6328', 'uvim1006.tab:6390', 'uvim1006.tab:6452', 'uvim1006.tab:6514', 'uvim1006.tab:6576', 'uvim1006.tab:6638', 'uvim1006.tab:6700', 'uvim1006.tab:6762', 'uvim1006.tab:6824', 'uvim1006.tab:6886', 'uvim1006.tab:6948', 'uvim1006.tab:7010', 'uvim1006.tab:7072', 'uvim1006.tab:7134', 'uvim1006.tab:7196']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5130', 'uvim1006.tab:5131', 'uvim1006.tab:5132', 'uvim1006.tab:5133', 'uvim1006.tab:5134', 'uvim1006.tab:5336', 'uvim1006.tab:5398', 'uvim1006.tab:5460', 'uvim1006.tab:5522', 'uvim1006.tab:5584', 'uvim1006.tab:5646', 'uvim1006.tab:5708', 'uvim1006.tab:5770', 'uvim1006.tab:5832', 'uvim1006.tab:5894', 'uvim1006.tab:5956', 'uvim1006.tab:6018', 'uvim1006.tab:6080', 'uvim1006.tab:6142', 'uvim1006.tab:6204', 'uvim1006.tab:6266', 'uvim1006.tab:6328', 'uvim1006.tab:6390', 'uvim1006.tab:6452', 'uvim1006.tab:6514', 'uvim1006.tab:6576', 'uvim1006.tab:6638', 'uvim1006.tab:6700', 'uvim1006.tab:6762', 'uvim1006.tab:6824', 'uvim1006.tab:6886', 'uvim1006.tab:6948', 'uvim1006.tab:7010', 'uvim1006.tab:7072', 'uvim1006.tab:7134', 'uvim1006.tab:7196']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5130', 'uvim1006.tab:5132', 'uvim1006.tab:5133', 'uvim1006.tab:5134', 'uvim1006.tab:5336', 'uvim1006.tab:5398', 'uvim1006.tab:5460', 'uvim1006.tab:5522', 'uvim1006.tab:5584', 'uvim1006.tab:5646', 'uvim1006.tab:5708', 'uvim1006.tab:5770', 'uvim1006.tab:5832', 'uvim1006.tab:5894', 'uvim1006.tab:5956', 'uvim1006.tab:6018', 'uvim1006.tab:6080', 'uvim1006.tab:6142', 'uvim1006.tab:6204', 'uvim1006.tab:6266', 'uvim1006.tab:6328', 'uvim1006.tab:6390', 'uvim1006.tab:6452', 'uvim1006.tab:6514', 'uvim1006.tab:6576', 'uvim1006.tab:6638', 'uvim1006.tab:6700', 'uvim1006.tab:6762', 'uvim1006.tab:6824', 'uvim1006.tab:6886', 'uvim1006.tab:6948', 'uvim1006.tab:7010', 'uvim1006.tab:7072']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5130', 'uvim1006.tab:5132', 'uvim1006.tab:5133', 'uvim1006.tab:5134', 'uvim1006.tab:5336', 'uvim1006.tab:5398', 'uvim1006.tab:5460', 'uvim1006.tab:5522', 'uvim1006.tab:5584', 'uvim1006.tab:5646', 'uvim1006.tab:5708', 'uvim1006.tab:5770', 'uvim1006.tab:5832', 'uvim1006.tab:5894', 'uvim1006.tab:5956', 'uvim1006.tab:6018', 'uvim1006.tab:6080', 'uvim1006.tab:6142', 'uvim1006.tab:6204', 'uvim1006.tab:6266', 'uvim1006.tab:6328', 'uvim1006.tab:6390', 'uvim1006.tab:6452', 'uvim1006.tab:6514', 'uvim1006.tab:6576', 'uvim1006.tab:6638', 'uvim1006.tab:6700', 'uvim1006.tab:6762', 'uvim1006.tab:6824', 'uvim1006.tab:6886', 'uvim1006.tab:6948', 'uvim1006.tab:7010', 'uvim1006.tab:7072']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5131', 'uvim1006.tab:7134', 'uvim1006.tab:7196']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5131', 'uvim1006.tab:7134', 'uvim1006.tab:7196']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5135', 'uvim1006.tab:5136', 'uvim1006.tab:5137', 'uvim1006.tab:5138', 'uvim1006.tab:5139', 'uvim1006.tab:5337', 'uvim1006.tab:5399', 'uvim1006.tab:5461', 'uvim1006.tab:5523', 'uvim1006.tab:5585', 'uvim1006.tab:5647', 'uvim1006.tab:5709', 'uvim1006.tab:5771', 'uvim1006.tab:5833', 'uvim1006.tab:5895', 'uvim1006.tab:5957', 'uvim1006.tab:6019', 'uvim1006.tab:6081', 'uvim1006.tab:6143', 'uvim1006.tab:6205', 'uvim1006.tab:6267', 'uvim1006.tab:6329', 'uvim1006.tab:6391', 'uvim1006.tab:6453', 'uvim1006.tab:6515', 'uvim1006.tab:6577', 'uvim1006.tab:6639', 'uvim1006.tab:6701', 'uvim1006.tab:6763', 'uvim1006.tab:6825', 'uvim1006.tab:6887', 'uvim1006.tab:6949', 'uvim1006.tab:7011', 'uvim1006.tab:7073', 'uvim1006.tab:7135', 'uvim1006.tab:7197']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5135', 'uvim1006.tab:5136', 'uvim1006.tab:5137', 'uvim1006.tab:5138', 'uvim1006.tab:5139', 'uvim1006.tab:5337', 'uvim1006.tab:5399', 'uvim1006.tab:5461', 'uvim1006.tab:5523', 'uvim1006.tab:5585', 'uvim1006.tab:5647', 'uvim1006.tab:5709', 'uvim1006.tab:5771', 'uvim1006.tab:5833', 'uvim1006.tab:5895', 'uvim1006.tab:5957', 'uvim1006.tab:6019', 'uvim1006.tab:6081', 'uvim1006.tab:6143', 'uvim1006.tab:6205', 'uvim1006.tab:6267', 'uvim1006.tab:6329', 'uvim1006.tab:6391', 'uvim1006.tab:6453', 'uvim1006.tab:6515', 'uvim1006.tab:6577', 'uvim1006.tab:6639', 'uvim1006.tab:6701', 'uvim1006.tab:6763', 'uvim1006.tab:6825', 'uvim1006.tab:6887', 'uvim1006.tab:6949', 'uvim1006.tab:7011', 'uvim1006.tab:7073', 'uvim1006.tab:7135', 'uvim1006.tab:7197']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5135', 'uvim1006.tab:5137', 'uvim1006.tab:5138', 'uvim1006.tab:5139', 'uvim1006.tab:5337', 'uvim1006.tab:5399', 'uvim1006.tab:5461', 'uvim1006.tab:5523', 'uvim1006.tab:5585', 'uvim1006.tab:5647', 'uvim1006.tab:5709', 'uvim1006.tab:5771', 'uvim1006.tab:5833', 'uvim1006.tab:5895', 'uvim1006.tab:5957', 'uvim1006.tab:6019', 'uvim1006.tab:6081', 'uvim1006.tab:6143', 'uvim1006.tab:6205', 'uvim1006.tab:6267', 'uvim1006.tab:6329', 'uvim1006.tab:6391', 'uvim1006.tab:6453', 'uvim1006.tab:6515', 'uvim1006.tab:6577', 'uvim1006.tab:6639', 'uvim1006.tab:6701', 'uvim1006.tab:6763', 'uvim1006.tab:6825', 'uvim1006.tab:6887', 'uvim1006.tab:6949', 'uvim1006.tab:7011', 'uvim1006.tab:7073']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5135', 'uvim1006.tab:5137', 'uvim1006.tab:5138', 'uvim1006.tab:5139', 'uvim1006.tab:5337', 'uvim1006.tab:5399', 'uvim1006.tab:5461', 'uvim1006.tab:5523', 'uvim1006.tab:5585', 'uvim1006.tab:5647', 'uvim1006.tab:5709', 'uvim1006.tab:5771', 'uvim1006.tab:5833', 'uvim1006.tab:5895', 'uvim1006.tab:5957', 'uvim1006.tab:6019', 'uvim1006.tab:6081', 'uvim1006.tab:6143', 'uvim1006.tab:6205', 'uvim1006.tab:6267', 'uvim1006.tab:6329', 'uvim1006.tab:6391', 'uvim1006.tab:6453', 'uvim1006.tab:6515', 'uvim1006.tab:6577', 'uvim1006.tab:6639', 'uvim1006.tab:6701', 'uvim1006.tab:6763', 'uvim1006.tab:6825', 'uvim1006.tab:6887', 'uvim1006.tab:6949', 'uvim1006.tab:7011', 'uvim1006.tab:7073']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5136', 'uvim1006.tab:7135', 'uvim1006.tab:7197']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5136', 'uvim1006.tab:7135', 'uvim1006.tab:7197']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5140', 'uvim1006.tab:5141', 'uvim1006.tab:5142', 'uvim1006.tab:5143', 'uvim1006.tab:5144', 'uvim1006.tab:5338', 'uvim1006.tab:5400', 'uvim1006.tab:5462', 'uvim1006.tab:5524', 'uvim1006.tab:5586', 'uvim1006.tab:5648', 'uvim1006.tab:5710', 'uvim1006.tab:5772', 'uvim1006.tab:5834', 'uvim1006.tab:5896', 'uvim1006.tab:5958', 'uvim1006.tab:6020', 'uvim1006.tab:6082', 'uvim1006.tab:6144', 'uvim1006.tab:6206', 'uvim1006.tab:6268', 'uvim1006.tab:6330', 'uvim1006.tab:6392', 'uvim1006.tab:6454', 'uvim1006.tab:6516', 'uvim1006.tab:6578', 'uvim1006.tab:6640', 'uvim1006.tab:6702', 'uvim1006.tab:6764', 'uvim1006.tab:6826', 'uvim1006.tab:6888', 'uvim1006.tab:6950', 'uvim1006.tab:7012', 'uvim1006.tab:7074', 'uvim1006.tab:7136', 'uvim1006.tab:7198', 'uvim1006.tab:7366']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5140', 'uvim1006.tab:5141', 'uvim1006.tab:5142', 'uvim1006.tab:5143', 'uvim1006.tab:5144', 'uvim1006.tab:5338', 'uvim1006.tab:5400', 'uvim1006.tab:5462', 'uvim1006.tab:5524', 'uvim1006.tab:5586', 'uvim1006.tab:5648', 'uvim1006.tab:5710', 'uvim1006.tab:5772', 'uvim1006.tab:5834', 'uvim1006.tab:5896', 'uvim1006.tab:5958', 'uvim1006.tab:6020', 'uvim1006.tab:6082', 'uvim1006.tab:6144', 'uvim1006.tab:6206', 'uvim1006.tab:6268', 'uvim1006.tab:6330', 'uvim1006.tab:6392', 'uvim1006.tab:6454', 'uvim1006.tab:6516', 'uvim1006.tab:6578', 'uvim1006.tab:6640', 'uvim1006.tab:6702', 'uvim1006.tab:6764', 'uvim1006.tab:6826', 'uvim1006.tab:6888', 'uvim1006.tab:6950', 'uvim1006.tab:7012', 'uvim1006.tab:7074', 'uvim1006.tab:7136', 'uvim1006.tab:7198', 'uvim1006.tab:7366']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5140', 'uvim1006.tab:5142', 'uvim1006.tab:5143', 'uvim1006.tab:5144', 'uvim1006.tab:5338', 'uvim1006.tab:5400', 'uvim1006.tab:5462', 'uvim1006.tab:5524', 'uvim1006.tab:5586', 'uvim1006.tab:5648', 'uvim1006.tab:5710', 'uvim1006.tab:5772', 'uvim1006.tab:5834', 'uvim1006.tab:5896', 'uvim1006.tab:5958', 'uvim1006.tab:6020', 'uvim1006.tab:6082', 'uvim1006.tab:6144', 'uvim1006.tab:6206', 'uvim1006.tab:6268', 'uvim1006.tab:6330', 'uvim1006.tab:6392', 'uvim1006.tab:6454', 'uvim1006.tab:6516', 'uvim1006.tab:6578', 'uvim1006.tab:6640', 'uvim1006.tab:6702', 'uvim1006.tab:6764', 'uvim1006.tab:6826', 'uvim1006.tab:6888', 'uvim1006.tab:6950', 'uvim1006.tab:7012', 'uvim1006.tab:7074']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5140', 'uvim1006.tab:5142', 'uvim1006.tab:5143', 'uvim1006.tab:5144', 'uvim1006.tab:5338', 'uvim1006.tab:5400', 'uvim1006.tab:5462', 'uvim1006.tab:5524', 'uvim1006.tab:5586', 'uvim1006.tab:5648', 'uvim1006.tab:5710', 'uvim1006.tab:5772', 'uvim1006.tab:5834', 'uvim1006.tab:5896', 'uvim1006.tab:5958', 'uvim1006.tab:6020', 'uvim1006.tab:6082', 'uvim1006.tab:6144', 'uvim1006.tab:6206', 'uvim1006.tab:6268', 'uvim1006.tab:6330', 'uvim1006.tab:6392', 'uvim1006.tab:6454', 'uvim1006.tab:6516', 'uvim1006.tab:6578', 'uvim1006.tab:6640', 'uvim1006.tab:6702', 'uvim1006.tab:6764', 'uvim1006.tab:6826', 'uvim1006.tab:6888', 'uvim1006.tab:6950', 'uvim1006.tab:7012', 'uvim1006.tab:7074']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5141', 'uvim1006.tab:7136', 'uvim1006.tab:7198']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5141', 'uvim1006.tab:7136', 'uvim1006.tab:7198']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5145', 'uvim1006.tab:5146', 'uvim1006.tab:5147', 'uvim1006.tab:5148', 'uvim1006.tab:5149', 'uvim1006.tab:5339', 'uvim1006.tab:5401', 'uvim1006.tab:5463', 'uvim1006.tab:5525', 'uvim1006.tab:5587', 'uvim1006.tab:5649', 'uvim1006.tab:5711', 'uvim1006.tab:5773', 'uvim1006.tab:5835', 'uvim1006.tab:5897', 'uvim1006.tab:5959', 'uvim1006.tab:6021', 'uvim1006.tab:6083', 'uvim1006.tab:6145', 'uvim1006.tab:6207', 'uvim1006.tab:6269', 'uvim1006.tab:6331', 'uvim1006.tab:6393', 'uvim1006.tab:6455', 'uvim1006.tab:6517', 'uvim1006.tab:6579', 'uvim1006.tab:6641', 'uvim1006.tab:6703', 'uvim1006.tab:6765', 'uvim1006.tab:6827', 'uvim1006.tab:6889', 'uvim1006.tab:6951', 'uvim1006.tab:7013', 'uvim1006.tab:7075', 'uvim1006.tab:7137', 'uvim1006.tab:7199']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5145', 'uvim1006.tab:5146', 'uvim1006.tab:5147', 'uvim1006.tab:5148', 'uvim1006.tab:5149', 'uvim1006.tab:5339', 'uvim1006.tab:5401', 'uvim1006.tab:5463', 'uvim1006.tab:5525', 'uvim1006.tab:5587', 'uvim1006.tab:5649', 'uvim1006.tab:5711', 'uvim1006.tab:5773', 'uvim1006.tab:5835', 'uvim1006.tab:5897', 'uvim1006.tab:5959', 'uvim1006.tab:6021', 'uvim1006.tab:6083', 'uvim1006.tab:6145', 'uvim1006.tab:6207', 'uvim1006.tab:6269', 'uvim1006.tab:6331', 'uvim1006.tab:6393', 'uvim1006.tab:6455', 'uvim1006.tab:6517', 'uvim1006.tab:6579', 'uvim1006.tab:6641', 'uvim1006.tab:6703', 'uvim1006.tab:6765', 'uvim1006.tab:6827', 'uvim1006.tab:6889', 'uvim1006.tab:6951', 'uvim1006.tab:7013', 'uvim1006.tab:7075', 'uvim1006.tab:7137', 'uvim1006.tab:7199']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5145', 'uvim1006.tab:5147', 'uvim1006.tab:5148', 'uvim1006.tab:5149', 'uvim1006.tab:5339', 'uvim1006.tab:5401', 'uvim1006.tab:5463', 'uvim1006.tab:5525', 'uvim1006.tab:5587', 'uvim1006.tab:5649', 'uvim1006.tab:5711', 'uvim1006.tab:5773', 'uvim1006.tab:5835', 'uvim1006.tab:5897', 'uvim1006.tab:5959', 'uvim1006.tab:6021', 'uvim1006.tab:6083', 'uvim1006.tab:6145', 'uvim1006.tab:6207', 'uvim1006.tab:6269', 'uvim1006.tab:6331', 'uvim1006.tab:6393', 'uvim1006.tab:6455', 'uvim1006.tab:6517', 'uvim1006.tab:6579', 'uvim1006.tab:6641', 'uvim1006.tab:6703', 'uvim1006.tab:6765', 'uvim1006.tab:6827', 'uvim1006.tab:6889', 'uvim1006.tab:6951', 'uvim1006.tab:7013', 'uvim1006.tab:7075']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5145', 'uvim1006.tab:5147', 'uvim1006.tab:5148', 'uvim1006.tab:5149', 'uvim1006.tab:5339', 'uvim1006.tab:5401', 'uvim1006.tab:5463', 'uvim1006.tab:5525', 'uvim1006.tab:5587', 'uvim1006.tab:5649', 'uvim1006.tab:5711', 'uvim1006.tab:5773', 'uvim1006.tab:5835', 'uvim1006.tab:5897', 'uvim1006.tab:5959', 'uvim1006.tab:6021', 'uvim1006.tab:6083', 'uvim1006.tab:6145', 'uvim1006.tab:6207', 'uvim1006.tab:6269', 'uvim1006.tab:6331', 'uvim1006.tab:6393', 'uvim1006.tab:6455', 'uvim1006.tab:6517', 'uvim1006.tab:6579', 'uvim1006.tab:6641', 'uvim1006.tab:6703', 'uvim1006.tab:6765', 'uvim1006.tab:6827', 'uvim1006.tab:6889', 'uvim1006.tab:6951', 'uvim1006.tab:7013', 'uvim1006.tab:7075']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5146', 'uvim1006.tab:7137', 'uvim1006.tab:7199']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5146', 'uvim1006.tab:7137', 'uvim1006.tab:7199']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5150', 'uvim1006.tab:5151', 'uvim1006.tab:5152', 'uvim1006.tab:5153', 'uvim1006.tab:5154', 'uvim1006.tab:5340', 'uvim1006.tab:5402', 'uvim1006.tab:5464', 'uvim1006.tab:5526', 'uvim1006.tab:5588', 'uvim1006.tab:5650', 'uvim1006.tab:5712', 'uvim1006.tab:5774', 'uvim1006.tab:5836', 'uvim1006.tab:5898', 'uvim1006.tab:5960', 'uvim1006.tab:6022', 'uvim1006.tab:6084', 'uvim1006.tab:6146', 'uvim1006.tab:6208', 'uvim1006.tab:6270', 'uvim1006.tab:6332', 'uvim1006.tab:6394', 'uvim1006.tab:6456', 'uvim1006.tab:6518', 'uvim1006.tab:6580', 'uvim1006.tab:6642', 'uvim1006.tab:6704', 'uvim1006.tab:6766', 'uvim1006.tab:6828', 'uvim1006.tab:6890', 'uvim1006.tab:6952', 'uvim1006.tab:7014', 'uvim1006.tab:7076', 'uvim1006.tab:7138', 'uvim1006.tab:7200']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5150', 'uvim1006.tab:5151', 'uvim1006.tab:5152', 'uvim1006.tab:5153', 'uvim1006.tab:5154', 'uvim1006.tab:5340', 'uvim1006.tab:5402', 'uvim1006.tab:5464', 'uvim1006.tab:5526', 'uvim1006.tab:5588', 'uvim1006.tab:5650', 'uvim1006.tab:5712', 'uvim1006.tab:5774', 'uvim1006.tab:5836', 'uvim1006.tab:5898', 'uvim1006.tab:5960', 'uvim1006.tab:6022', 'uvim1006.tab:6084', 'uvim1006.tab:6146', 'uvim1006.tab:6208', 'uvim1006.tab:6270', 'uvim1006.tab:6332', 'uvim1006.tab:6394', 'uvim1006.tab:6456', 'uvim1006.tab:6518', 'uvim1006.tab:6580', 'uvim1006.tab:6642', 'uvim1006.tab:6704', 'uvim1006.tab:6766', 'uvim1006.tab:6828', 'uvim1006.tab:6890', 'uvim1006.tab:6952', 'uvim1006.tab:7014', 'uvim1006.tab:7076', 'uvim1006.tab:7138', 'uvim1006.tab:7200']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5150', 'uvim1006.tab:5152', 'uvim1006.tab:5153', 'uvim1006.tab:5154', 'uvim1006.tab:5340', 'uvim1006.tab:5402', 'uvim1006.tab:5464', 'uvim1006.tab:5526', 'uvim1006.tab:5588', 'uvim1006.tab:5650', 'uvim1006.tab:5712', 'uvim1006.tab:5774', 'uvim1006.tab:5836', 'uvim1006.tab:5898', 'uvim1006.tab:5960', 'uvim1006.tab:6022', 'uvim1006.tab:6084', 'uvim1006.tab:6146', 'uvim1006.tab:6208', 'uvim1006.tab:6270', 'uvim1006.tab:6332', 'uvim1006.tab:6394', 'uvim1006.tab:6456', 'uvim1006.tab:6518', 'uvim1006.tab:6580', 'uvim1006.tab:6642', 'uvim1006.tab:6704', 'uvim1006.tab:6766', 'uvim1006.tab:6828', 'uvim1006.tab:6890', 'uvim1006.tab:6952', 'uvim1006.tab:7014', 'uvim1006.tab:7076']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5150', 'uvim1006.tab:5152', 'uvim1006.tab:5153', 'uvim1006.tab:5154', 'uvim1006.tab:5340', 'uvim1006.tab:5402', 'uvim1006.tab:5464', 'uvim1006.tab:5526', 'uvim1006.tab:5588', 'uvim1006.tab:5650', 'uvim1006.tab:5712', 'uvim1006.tab:5774', 'uvim1006.tab:5836', 'uvim1006.tab:5898', 'uvim1006.tab:5960', 'uvim1006.tab:6022', 'uvim1006.tab:6084', 'uvim1006.tab:6146', 'uvim1006.tab:6208', 'uvim1006.tab:6270', 'uvim1006.tab:6332', 'uvim1006.tab:6394', 'uvim1006.tab:6456', 'uvim1006.tab:6518', 'uvim1006.tab:6580', 'uvim1006.tab:6642', 'uvim1006.tab:6704', 'uvim1006.tab:6766', 'uvim1006.tab:6828', 'uvim1006.tab:6890', 'uvim1006.tab:6952', 'uvim1006.tab:7014', 'uvim1006.tab:7076']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5151', 'uvim1006.tab:7138', 'uvim1006.tab:7200']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5151', 'uvim1006.tab:7138', 'uvim1006.tab:7200']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5155', 'uvim1006.tab:5156', 'uvim1006.tab:5157', 'uvim1006.tab:5158', 'uvim1006.tab:5159', 'uvim1006.tab:5341', 'uvim1006.tab:5403', 'uvim1006.tab:5465', 'uvim1006.tab:5527', 'uvim1006.tab:5589', 'uvim1006.tab:5651', 'uvim1006.tab:5713', 'uvim1006.tab:5775', 'uvim1006.tab:5837', 'uvim1006.tab:5899', 'uvim1006.tab:5961', 'uvim1006.tab:6023', 'uvim1006.tab:6085', 'uvim1006.tab:6147', 'uvim1006.tab:6209', 'uvim1006.tab:6271', 'uvim1006.tab:6333', 'uvim1006.tab:6395', 'uvim1006.tab:6457', 'uvim1006.tab:6519', 'uvim1006.tab:6581', 'uvim1006.tab:6643', 'uvim1006.tab:6705', 'uvim1006.tab:6767', 'uvim1006.tab:6829', 'uvim1006.tab:6891', 'uvim1006.tab:6953', 'uvim1006.tab:7015', 'uvim1006.tab:7077', 'uvim1006.tab:7139', 'uvim1006.tab:7201', 'uvim1006.tab:7328', 'uvim1006.tab:7329', 'uvim1006.tab:7330', 'uvim1006.tab:7331', 'uvim1006.tab:7332', 'uvim1006.tab:7333', 'uvim1006.tab:7334', 'uvim1006.tab:7335', 'uvim1006.tab:7336', 'uvim1006.tab:7337', 'uvim1006.tab:7338', 'uvim1006.tab:7339', 'uvim1006.tab:7340', 'uvim1006.tab:7341', 'uvim1006.tab:7342', 'uvim1006.tab:7343', 'uvim1006.tab:7344', 'uvim1006.tab:7345', 'uvim1006.tab:7346', 'uvim1006.tab:7347', 'uvim1006.tab:7348', 'uvim1006.tab:7349', 'uvim1006.tab:7350', 'uvim1006.tab:7351', 'uvim1006.tab:7352', 'uvim1006.tab:7353', 'uvim1006.tab:7354', 'uvim1006.tab:7355']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5155', 'uvim1006.tab:5156', 'uvim1006.tab:5157', 'uvim1006.tab:5158', 'uvim1006.tab:5159', 'uvim1006.tab:5341', 'uvim1006.tab:5403', 'uvim1006.tab:5465', 'uvim1006.tab:5527', 'uvim1006.tab:5589', 'uvim1006.tab:5651', 'uvim1006.tab:5713', 'uvim1006.tab:5775', 'uvim1006.tab:5837', 'uvim1006.tab:5899', 'uvim1006.tab:5961', 'uvim1006.tab:6023', 'uvim1006.tab:6085', 'uvim1006.tab:6147', 'uvim1006.tab:6209', 'uvim1006.tab:6271', 'uvim1006.tab:6333', 'uvim1006.tab:6395', 'uvim1006.tab:6457', 'uvim1006.tab:6519', 'uvim1006.tab:6581', 'uvim1006.tab:6643', 'uvim1006.tab:6705', 'uvim1006.tab:6767', 'uvim1006.tab:6829', 'uvim1006.tab:6891', 'uvim1006.tab:6953', 'uvim1006.tab:7015', 'uvim1006.tab:7077', 'uvim1006.tab:7139', 'uvim1006.tab:7201', 'uvim1006.tab:7328', 'uvim1006.tab:7329', 'uvim1006.tab:7330', 'uvim1006.tab:7331', 'uvim1006.tab:7332', 'uvim1006.tab:7333', 'uvim1006.tab:7334', 'uvim1006.tab:7335', 'uvim1006.tab:7336', 'uvim1006.tab:7337', 'uvim1006.tab:7338', 'uvim1006.tab:7339', 'uvim1006.tab:7340', 'uvim1006.tab:7341', 'uvim1006.tab:7342', 'uvim1006.tab:7343', 'uvim1006.tab:7344', 'uvim1006.tab:7345', 'uvim1006.tab:7346', 'uvim1006.tab:7347', 'uvim1006.tab:7348', 'uvim1006.tab:7349', 'uvim1006.tab:7350', 'uvim1006.tab:7351', 'uvim1006.tab:7352', 'uvim1006.tab:7353', 'uvim1006.tab:7354', 'uvim1006.tab:7355']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5155', 'uvim1006.tab:5157', 'uvim1006.tab:5158', 'uvim1006.tab:5159', 'uvim1006.tab:5341', 'uvim1006.tab:5403', 'uvim1006.tab:5465', 'uvim1006.tab:5527', 'uvim1006.tab:5589', 'uvim1006.tab:5651', 'uvim1006.tab:5713', 'uvim1006.tab:5775', 'uvim1006.tab:5837', 'uvim1006.tab:5899', 'uvim1006.tab:5961', 'uvim1006.tab:6023', 'uvim1006.tab:6085', 'uvim1006.tab:6147', 'uvim1006.tab:6209', 'uvim1006.tab:6271', 'uvim1006.tab:6333', 'uvim1006.tab:6395', 'uvim1006.tab:6457', 'uvim1006.tab:6519', 'uvim1006.tab:6581', 'uvim1006.tab:6643', 'uvim1006.tab:6705', 'uvim1006.tab:6767', 'uvim1006.tab:6829', 'uvim1006.tab:6891', 'uvim1006.tab:6953', 'uvim1006.tab:7015', 'uvim1006.tab:7077']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5155', 'uvim1006.tab:5157', 'uvim1006.tab:5158', 'uvim1006.tab:5159', 'uvim1006.tab:5341', 'uvim1006.tab:5403', 'uvim1006.tab:5465', 'uvim1006.tab:5527', 'uvim1006.tab:5589', 'uvim1006.tab:5651', 'uvim1006.tab:5713', 'uvim1006.tab:5775', 'uvim1006.tab:5837', 'uvim1006.tab:5899', 'uvim1006.tab:5961', 'uvim1006.tab:6023', 'uvim1006.tab:6085', 'uvim1006.tab:6147', 'uvim1006.tab:6209', 'uvim1006.tab:6271', 'uvim1006.tab:6333', 'uvim1006.tab:6395', 'uvim1006.tab:6457', 'uvim1006.tab:6519', 'uvim1006.tab:6581', 'uvim1006.tab:6643', 'uvim1006.tab:6705', 'uvim1006.tab:6767', 'uvim1006.tab:6829', 'uvim1006.tab:6891', 'uvim1006.tab:6953', 'uvim1006.tab:7015', 'uvim1006.tab:7077']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5156', 'uvim1006.tab:7139', 'uvim1006.tab:7201']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5156', 'uvim1006.tab:7139', 'uvim1006.tab:7201']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5160', 'uvim1006.tab:5161', 'uvim1006.tab:5162', 'uvim1006.tab:5163', 'uvim1006.tab:5164', 'uvim1006.tab:5342', 'uvim1006.tab:5404', 'uvim1006.tab:5466', 'uvim1006.tab:5528', 'uvim1006.tab:5590', 'uvim1006.tab:5652', 'uvim1006.tab:5714', 'uvim1006.tab:5776', 'uvim1006.tab:5838', 'uvim1006.tab:5900', 'uvim1006.tab:5962', 'uvim1006.tab:6024', 'uvim1006.tab:6086', 'uvim1006.tab:6148', 'uvim1006.tab:6210', 'uvim1006.tab:6272', 'uvim1006.tab:6334', 'uvim1006.tab:6396', 'uvim1006.tab:6458', 'uvim1006.tab:6520', 'uvim1006.tab:6582', 'uvim1006.tab:6644', 'uvim1006.tab:6706', 'uvim1006.tab:6768', 'uvim1006.tab:6830', 'uvim1006.tab:6892', 'uvim1006.tab:6954', 'uvim1006.tab:7016', 'uvim1006.tab:7078', 'uvim1006.tab:7140', 'uvim1006.tab:7202']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5160', 'uvim1006.tab:5161', 'uvim1006.tab:5162', 'uvim1006.tab:5163', 'uvim1006.tab:5164', 'uvim1006.tab:5342', 'uvim1006.tab:5404', 'uvim1006.tab:5466', 'uvim1006.tab:5528', 'uvim1006.tab:5590', 'uvim1006.tab:5652', 'uvim1006.tab:5714', 'uvim1006.tab:5776', 'uvim1006.tab:5838', 'uvim1006.tab:5900', 'uvim1006.tab:5962', 'uvim1006.tab:6024', 'uvim1006.tab:6086', 'uvim1006.tab:6148', 'uvim1006.tab:6210', 'uvim1006.tab:6272', 'uvim1006.tab:6334', 'uvim1006.tab:6396', 'uvim1006.tab:6458', 'uvim1006.tab:6520', 'uvim1006.tab:6582', 'uvim1006.tab:6644', 'uvim1006.tab:6706', 'uvim1006.tab:6768', 'uvim1006.tab:6830', 'uvim1006.tab:6892', 'uvim1006.tab:6954', 'uvim1006.tab:7016', 'uvim1006.tab:7078', 'uvim1006.tab:7140', 'uvim1006.tab:7202']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5160', 'uvim1006.tab:5162', 'uvim1006.tab:5163', 'uvim1006.tab:5164', 'uvim1006.tab:5342', 'uvim1006.tab:5404', 'uvim1006.tab:5466', 'uvim1006.tab:5528', 'uvim1006.tab:5590', 'uvim1006.tab:5652', 'uvim1006.tab:5714', 'uvim1006.tab:5776', 'uvim1006.tab:5838', 'uvim1006.tab:5900', 'uvim1006.tab:5962', 'uvim1006.tab:6024', 'uvim1006.tab:6086', 'uvim1006.tab:6148', 'uvim1006.tab:6210', 'uvim1006.tab:6272', 'uvim1006.tab:6334', 'uvim1006.tab:6396', 'uvim1006.tab:6458', 'uvim1006.tab:6520', 'uvim1006.tab:6582', 'uvim1006.tab:6644', 'uvim1006.tab:6706', 'uvim1006.tab:6768', 'uvim1006.tab:6830', 'uvim1006.tab:6892', 'uvim1006.tab:6954', 'uvim1006.tab:7016', 'uvim1006.tab:7078']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5160', 'uvim1006.tab:5162', 'uvim1006.tab:5163', 'uvim1006.tab:5164', 'uvim1006.tab:5342', 'uvim1006.tab:5404', 'uvim1006.tab:5466', 'uvim1006.tab:5528', 'uvim1006.tab:5590', 'uvim1006.tab:5652', 'uvim1006.tab:5714', 'uvim1006.tab:5776', 'uvim1006.tab:5838', 'uvim1006.tab:5900', 'uvim1006.tab:5962', 'uvim1006.tab:6024', 'uvim1006.tab:6086', 'uvim1006.tab:6148', 'uvim1006.tab:6210', 'uvim1006.tab:6272', 'uvim1006.tab:6334', 'uvim1006.tab:6396', 'uvim1006.tab:6458', 'uvim1006.tab:6520', 'uvim1006.tab:6582', 'uvim1006.tab:6644', 'uvim1006.tab:6706', 'uvim1006.tab:6768', 'uvim1006.tab:6830', 'uvim1006.tab:6892', 'uvim1006.tab:6954', 'uvim1006.tab:7016', 'uvim1006.tab:7078']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5161', 'uvim1006.tab:7140', 'uvim1006.tab:7202']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5161', 'uvim1006.tab:7140', 'uvim1006.tab:7202']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5165', 'uvim1006.tab:5166', 'uvim1006.tab:5167', 'uvim1006.tab:5168', 'uvim1006.tab:5169', 'uvim1006.tab:5343', 'uvim1006.tab:5405', 'uvim1006.tab:5467', 'uvim1006.tab:5529', 'uvim1006.tab:5591', 'uvim1006.tab:5653', 'uvim1006.tab:5715', 'uvim1006.tab:5777', 'uvim1006.tab:5839', 'uvim1006.tab:5901', 'uvim1006.tab:5963', 'uvim1006.tab:6025', 'uvim1006.tab:6087', 'uvim1006.tab:6149', 'uvim1006.tab:6211', 'uvim1006.tab:6273', 'uvim1006.tab:6335', 'uvim1006.tab:6397', 'uvim1006.tab:6459', 'uvim1006.tab:6521', 'uvim1006.tab:6583', 'uvim1006.tab:6645', 'uvim1006.tab:6707', 'uvim1006.tab:6769', 'uvim1006.tab:6831', 'uvim1006.tab:6893', 'uvim1006.tab:6955', 'uvim1006.tab:7017', 'uvim1006.tab:7079', 'uvim1006.tab:7141', 'uvim1006.tab:7203']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5165', 'uvim1006.tab:5166', 'uvim1006.tab:5167', 'uvim1006.tab:5168', 'uvim1006.tab:5169', 'uvim1006.tab:5343', 'uvim1006.tab:5405', 'uvim1006.tab:5467', 'uvim1006.tab:5529', 'uvim1006.tab:5591', 'uvim1006.tab:5653', 'uvim1006.tab:5715', 'uvim1006.tab:5777', 'uvim1006.tab:5839', 'uvim1006.tab:5901', 'uvim1006.tab:5963', 'uvim1006.tab:6025', 'uvim1006.tab:6087', 'uvim1006.tab:6149', 'uvim1006.tab:6211', 'uvim1006.tab:6273', 'uvim1006.tab:6335', 'uvim1006.tab:6397', 'uvim1006.tab:6459', 'uvim1006.tab:6521', 'uvim1006.tab:6583', 'uvim1006.tab:6645', 'uvim1006.tab:6707', 'uvim1006.tab:6769', 'uvim1006.tab:6831', 'uvim1006.tab:6893', 'uvim1006.tab:6955', 'uvim1006.tab:7017', 'uvim1006.tab:7079', 'uvim1006.tab:7141', 'uvim1006.tab:7203']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5165', 'uvim1006.tab:5167', 'uvim1006.tab:5168', 'uvim1006.tab:5169', 'uvim1006.tab:5343', 'uvim1006.tab:5405', 'uvim1006.tab:5467', 'uvim1006.tab:5529', 'uvim1006.tab:5591', 'uvim1006.tab:5653', 'uvim1006.tab:5715', 'uvim1006.tab:5777', 'uvim1006.tab:5839', 'uvim1006.tab:5901', 'uvim1006.tab:5963', 'uvim1006.tab:6025', 'uvim1006.tab:6087', 'uvim1006.tab:6149', 'uvim1006.tab:6211', 'uvim1006.tab:6273', 'uvim1006.tab:6335', 'uvim1006.tab:6397', 'uvim1006.tab:6459', 'uvim1006.tab:6521', 'uvim1006.tab:6583', 'uvim1006.tab:6645', 'uvim1006.tab:6707', 'uvim1006.tab:6769', 'uvim1006.tab:6831', 'uvim1006.tab:6893', 'uvim1006.tab:6955', 'uvim1006.tab:7017', 'uvim1006.tab:7079']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5165', 'uvim1006.tab:5167', 'uvim1006.tab:5168', 'uvim1006.tab:5169', 'uvim1006.tab:5343', 'uvim1006.tab:5405', 'uvim1006.tab:5467', 'uvim1006.tab:5529', 'uvim1006.tab:5591', 'uvim1006.tab:5653', 'uvim1006.tab:5715', 'uvim1006.tab:5777', 'uvim1006.tab:5839', 'uvim1006.tab:5901', 'uvim1006.tab:5963', 'uvim1006.tab:6025', 'uvim1006.tab:6087', 'uvim1006.tab:6149', 'uvim1006.tab:6211', 'uvim1006.tab:6273', 'uvim1006.tab:6335', 'uvim1006.tab:6397', 'uvim1006.tab:6459', 'uvim1006.tab:6521', 'uvim1006.tab:6583', 'uvim1006.tab:6645', 'uvim1006.tab:6707', 'uvim1006.tab:6769', 'uvim1006.tab:6831', 'uvim1006.tab:6893', 'uvim1006.tab:6955', 'uvim1006.tab:7017', 'uvim1006.tab:7079']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5166', 'uvim1006.tab:7141', 'uvim1006.tab:7203']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5166', 'uvim1006.tab:7141', 'uvim1006.tab:7203']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5170', 'uvim1006.tab:5171', 'uvim1006.tab:5172', 'uvim1006.tab:5173', 'uvim1006.tab:5174', 'uvim1006.tab:5344', 'uvim1006.tab:5406', 'uvim1006.tab:5468', 'uvim1006.tab:5530', 'uvim1006.tab:5592', 'uvim1006.tab:5654', 'uvim1006.tab:5716', 'uvim1006.tab:5778', 'uvim1006.tab:5840', 'uvim1006.tab:5902', 'uvim1006.tab:5964', 'uvim1006.tab:6026', 'uvim1006.tab:6088', 'uvim1006.tab:6150', 'uvim1006.tab:6212', 'uvim1006.tab:6274', 'uvim1006.tab:6336', 'uvim1006.tab:6398', 'uvim1006.tab:6460', 'uvim1006.tab:6522', 'uvim1006.tab:6584', 'uvim1006.tab:6646', 'uvim1006.tab:6708', 'uvim1006.tab:6770', 'uvim1006.tab:6832', 'uvim1006.tab:6894', 'uvim1006.tab:6956', 'uvim1006.tab:7018', 'uvim1006.tab:7080', 'uvim1006.tab:7142', 'uvim1006.tab:7204', 'uvim1006.tab:7232', 'uvim1006.tab:7233', 'uvim1006.tab:7234', 'uvim1006.tab:7235', 'uvim1006.tab:7236', 'uvim1006.tab:7237', 'uvim1006.tab:7238', 'uvim1006.tab:7239', 'uvim1006.tab:7240', 'uvim1006.tab:7241', 'uvim1006.tab:7242', 'uvim1006.tab:7243', 'uvim1006.tab:7244', 'uvim1006.tab:7245', 'uvim1006.tab:7246', 'uvim1006.tab:7247', 'uvim1006.tab:7248', 'uvim1006.tab:7249', 'uvim1006.tab:7250', 'uvim1006.tab:7251', 'uvim1006.tab:7252', 'uvim1006.tab:7253', 'uvim1006.tab:7254', 'uvim1006.tab:7255']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5170', 'uvim1006.tab:5171', 'uvim1006.tab:5172', 'uvim1006.tab:5173', 'uvim1006.tab:5174', 'uvim1006.tab:5344', 'uvim1006.tab:5406', 'uvim1006.tab:5468', 'uvim1006.tab:5530', 'uvim1006.tab:5592', 'uvim1006.tab:5654', 'uvim1006.tab:5716', 'uvim1006.tab:5778', 'uvim1006.tab:5840', 'uvim1006.tab:5902', 'uvim1006.tab:5964', 'uvim1006.tab:6026', 'uvim1006.tab:6088', 'uvim1006.tab:6150', 'uvim1006.tab:6212', 'uvim1006.tab:6274', 'uvim1006.tab:6336', 'uvim1006.tab:6398', 'uvim1006.tab:6460', 'uvim1006.tab:6522', 'uvim1006.tab:6584', 'uvim1006.tab:6646', 'uvim1006.tab:6708', 'uvim1006.tab:6770', 'uvim1006.tab:6832', 'uvim1006.tab:6894', 'uvim1006.tab:6956', 'uvim1006.tab:7018', 'uvim1006.tab:7080', 'uvim1006.tab:7142', 'uvim1006.tab:7204', 'uvim1006.tab:7232', 'uvim1006.tab:7233', 'uvim1006.tab:7234', 'uvim1006.tab:7235', 'uvim1006.tab:7236', 'uvim1006.tab:7237', 'uvim1006.tab:7238', 'uvim1006.tab:7239', 'uvim1006.tab:7240', 'uvim1006.tab:7241', 'uvim1006.tab:7242', 'uvim1006.tab:7243', 'uvim1006.tab:7244', 'uvim1006.tab:7245', 'uvim1006.tab:7246', 'uvim1006.tab:7247', 'uvim1006.tab:7248', 'uvim1006.tab:7249', 'uvim1006.tab:7250', 'uvim1006.tab:7251', 'uvim1006.tab:7252', 'uvim1006.tab:7253', 'uvim1006.tab:7254', 'uvim1006.tab:7255']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5170', 'uvim1006.tab:5172', 'uvim1006.tab:5173', 'uvim1006.tab:5174', 'uvim1006.tab:5344', 'uvim1006.tab:5406', 'uvim1006.tab:5468', 'uvim1006.tab:5530', 'uvim1006.tab:5592', 'uvim1006.tab:5654', 'uvim1006.tab:5716', 'uvim1006.tab:5778', 'uvim1006.tab:5840', 'uvim1006.tab:5902', 'uvim1006.tab:5964', 'uvim1006.tab:6026', 'uvim1006.tab:6088', 'uvim1006.tab:6150', 'uvim1006.tab:6212', 'uvim1006.tab:6274', 'uvim1006.tab:6336', 'uvim1006.tab:6398', 'uvim1006.tab:6460', 'uvim1006.tab:6522', 'uvim1006.tab:6584', 'uvim1006.tab:6646', 'uvim1006.tab:6708', 'uvim1006.tab:6770', 'uvim1006.tab:6832', 'uvim1006.tab:6894', 'uvim1006.tab:6956', 'uvim1006.tab:7018', 'uvim1006.tab:7080']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5170', 'uvim1006.tab:5172', 'uvim1006.tab:5173', 'uvim1006.tab:5174', 'uvim1006.tab:5344', 'uvim1006.tab:5406', 'uvim1006.tab:5468', 'uvim1006.tab:5530', 'uvim1006.tab:5592', 'uvim1006.tab:5654', 'uvim1006.tab:5716', 'uvim1006.tab:5778', 'uvim1006.tab:5840', 'uvim1006.tab:5902', 'uvim1006.tab:5964', 'uvim1006.tab:6026', 'uvim1006.tab:6088', 'uvim1006.tab:6150', 'uvim1006.tab:6212', 'uvim1006.tab:6274', 'uvim1006.tab:6336', 'uvim1006.tab:6398', 'uvim1006.tab:6460', 'uvim1006.tab:6522', 'uvim1006.tab:6584', 'uvim1006.tab:6646', 'uvim1006.tab:6708', 'uvim1006.tab:6770', 'uvim1006.tab:6832', 'uvim1006.tab:6894', 'uvim1006.tab:6956', 'uvim1006.tab:7018', 'uvim1006.tab:7080']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5171', 'uvim1006.tab:7142', 'uvim1006.tab:7204']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5171', 'uvim1006.tab:7142', 'uvim1006.tab:7204']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5175', 'uvim1006.tab:5176', 'uvim1006.tab:5177', 'uvim1006.tab:5178', 'uvim1006.tab:5179', 'uvim1006.tab:5345', 'uvim1006.tab:5407', 'uvim1006.tab:5469', 'uvim1006.tab:5531', 'uvim1006.tab:5593', 'uvim1006.tab:5655', 'uvim1006.tab:5717', 'uvim1006.tab:5779', 'uvim1006.tab:5841', 'uvim1006.tab:5903', 'uvim1006.tab:5965', 'uvim1006.tab:6027', 'uvim1006.tab:6089', 'uvim1006.tab:6151', 'uvim1006.tab:6213', 'uvim1006.tab:6275', 'uvim1006.tab:6337', 'uvim1006.tab:6399', 'uvim1006.tab:6461', 'uvim1006.tab:6523', 'uvim1006.tab:6585', 'uvim1006.tab:6647', 'uvim1006.tab:6709', 'uvim1006.tab:6771', 'uvim1006.tab:6833', 'uvim1006.tab:6895', 'uvim1006.tab:6957', 'uvim1006.tab:7019', 'uvim1006.tab:7081', 'uvim1006.tab:7143', 'uvim1006.tab:7205']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5175', 'uvim1006.tab:5176', 'uvim1006.tab:5177', 'uvim1006.tab:5178', 'uvim1006.tab:5179', 'uvim1006.tab:5345', 'uvim1006.tab:5407', 'uvim1006.tab:5469', 'uvim1006.tab:5531', 'uvim1006.tab:5593', 'uvim1006.tab:5655', 'uvim1006.tab:5717', 'uvim1006.tab:5779', 'uvim1006.tab:5841', 'uvim1006.tab:5903', 'uvim1006.tab:5965', 'uvim1006.tab:6027', 'uvim1006.tab:6089', 'uvim1006.tab:6151', 'uvim1006.tab:6213', 'uvim1006.tab:6275', 'uvim1006.tab:6337', 'uvim1006.tab:6399', 'uvim1006.tab:6461', 'uvim1006.tab:6523', 'uvim1006.tab:6585', 'uvim1006.tab:6647', 'uvim1006.tab:6709', 'uvim1006.tab:6771', 'uvim1006.tab:6833', 'uvim1006.tab:6895', 'uvim1006.tab:6957', 'uvim1006.tab:7019', 'uvim1006.tab:7081', 'uvim1006.tab:7143', 'uvim1006.tab:7205']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5175', 'uvim1006.tab:5177', 'uvim1006.tab:5178', 'uvim1006.tab:5179', 'uvim1006.tab:5345', 'uvim1006.tab:5407', 'uvim1006.tab:5469', 'uvim1006.tab:5531', 'uvim1006.tab:5593', 'uvim1006.tab:5655', 'uvim1006.tab:5717', 'uvim1006.tab:5779', 'uvim1006.tab:5841', 'uvim1006.tab:5903', 'uvim1006.tab:5965', 'uvim1006.tab:6027', 'uvim1006.tab:6089', 'uvim1006.tab:6151', 'uvim1006.tab:6213', 'uvim1006.tab:6275', 'uvim1006.tab:6337', 'uvim1006.tab:6399', 'uvim1006.tab:6461', 'uvim1006.tab:6523', 'uvim1006.tab:6585', 'uvim1006.tab:6647', 'uvim1006.tab:6709', 'uvim1006.tab:6771', 'uvim1006.tab:6833', 'uvim1006.tab:6895', 'uvim1006.tab:6957', 'uvim1006.tab:7019', 'uvim1006.tab:7081']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5175', 'uvim1006.tab:5177', 'uvim1006.tab:5178', 'uvim1006.tab:5179', 'uvim1006.tab:5345', 'uvim1006.tab:5407', 'uvim1006.tab:5469', 'uvim1006.tab:5531', 'uvim1006.tab:5593', 'uvim1006.tab:5655', 'uvim1006.tab:5717', 'uvim1006.tab:5779', 'uvim1006.tab:5841', 'uvim1006.tab:5903', 'uvim1006.tab:5965', 'uvim1006.tab:6027', 'uvim1006.tab:6089', 'uvim1006.tab:6151', 'uvim1006.tab:6213', 'uvim1006.tab:6275', 'uvim1006.tab:6337', 'uvim1006.tab:6399', 'uvim1006.tab:6461', 'uvim1006.tab:6523', 'uvim1006.tab:6585', 'uvim1006.tab:6647', 'uvim1006.tab:6709', 'uvim1006.tab:6771', 'uvim1006.tab:6833', 'uvim1006.tab:6895', 'uvim1006.tab:6957', 'uvim1006.tab:7019', 'uvim1006.tab:7081']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5176', 'uvim1006.tab:7143', 'uvim1006.tab:7205']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5176', 'uvim1006.tab:7143', 'uvim1006.tab:7205']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5180', 'uvim1006.tab:5181', 'uvim1006.tab:5182', 'uvim1006.tab:5183', 'uvim1006.tab:5184', 'uvim1006.tab:5346', 'uvim1006.tab:5408', 'uvim1006.tab:5470', 'uvim1006.tab:5532', 'uvim1006.tab:5594', 'uvim1006.tab:5656', 'uvim1006.tab:5718', 'uvim1006.tab:5780', 'uvim1006.tab:5842', 'uvim1006.tab:5904', 'uvim1006.tab:5966', 'uvim1006.tab:6028', 'uvim1006.tab:6090', 'uvim1006.tab:6152', 'uvim1006.tab:6214', 'uvim1006.tab:6276', 'uvim1006.tab:6338', 'uvim1006.tab:6400', 'uvim1006.tab:6462', 'uvim1006.tab:6524', 'uvim1006.tab:6586', 'uvim1006.tab:6648', 'uvim1006.tab:6710', 'uvim1006.tab:6772', 'uvim1006.tab:6834', 'uvim1006.tab:6896', 'uvim1006.tab:6958', 'uvim1006.tab:7020', 'uvim1006.tab:7082', 'uvim1006.tab:7144', 'uvim1006.tab:7206']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5180', 'uvim1006.tab:5181', 'uvim1006.tab:5182', 'uvim1006.tab:5183', 'uvim1006.tab:5184', 'uvim1006.tab:5346', 'uvim1006.tab:5408', 'uvim1006.tab:5470', 'uvim1006.tab:5532', 'uvim1006.tab:5594', 'uvim1006.tab:5656', 'uvim1006.tab:5718', 'uvim1006.tab:5780', 'uvim1006.tab:5842', 'uvim1006.tab:5904', 'uvim1006.tab:5966', 'uvim1006.tab:6028', 'uvim1006.tab:6090', 'uvim1006.tab:6152', 'uvim1006.tab:6214', 'uvim1006.tab:6276', 'uvim1006.tab:6338', 'uvim1006.tab:6400', 'uvim1006.tab:6462', 'uvim1006.tab:6524', 'uvim1006.tab:6586', 'uvim1006.tab:6648', 'uvim1006.tab:6710', 'uvim1006.tab:6772', 'uvim1006.tab:6834', 'uvim1006.tab:6896', 'uvim1006.tab:6958', 'uvim1006.tab:7020', 'uvim1006.tab:7082', 'uvim1006.tab:7144', 'uvim1006.tab:7206']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5180', 'uvim1006.tab:5182', 'uvim1006.tab:5183', 'uvim1006.tab:5184', 'uvim1006.tab:5346', 'uvim1006.tab:5408', 'uvim1006.tab:5470', 'uvim1006.tab:5532', 'uvim1006.tab:5594', 'uvim1006.tab:5656', 'uvim1006.tab:5718', 'uvim1006.tab:5780', 'uvim1006.tab:5842', 'uvim1006.tab:5904', 'uvim1006.tab:5966', 'uvim1006.tab:6028', 'uvim1006.tab:6090', 'uvim1006.tab:6152', 'uvim1006.tab:6214', 'uvim1006.tab:6276', 'uvim1006.tab:6338', 'uvim1006.tab:6400', 'uvim1006.tab:6462', 'uvim1006.tab:6524', 'uvim1006.tab:6586', 'uvim1006.tab:6648', 'uvim1006.tab:6710', 'uvim1006.tab:6772', 'uvim1006.tab:6834', 'uvim1006.tab:6896', 'uvim1006.tab:6958', 'uvim1006.tab:7020', 'uvim1006.tab:7082']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5180', 'uvim1006.tab:5182', 'uvim1006.tab:5183', 'uvim1006.tab:5184', 'uvim1006.tab:5346', 'uvim1006.tab:5408', 'uvim1006.tab:5470', 'uvim1006.tab:5532', 'uvim1006.tab:5594', 'uvim1006.tab:5656', 'uvim1006.tab:5718', 'uvim1006.tab:5780', 'uvim1006.tab:5842', 'uvim1006.tab:5904', 'uvim1006.tab:5966', 'uvim1006.tab:6028', 'uvim1006.tab:6090', 'uvim1006.tab:6152', 'uvim1006.tab:6214', 'uvim1006.tab:6276', 'uvim1006.tab:6338', 'uvim1006.tab:6400', 'uvim1006.tab:6462', 'uvim1006.tab:6524', 'uvim1006.tab:6586', 'uvim1006.tab:6648', 'uvim1006.tab:6710', 'uvim1006.tab:6772', 'uvim1006.tab:6834', 'uvim1006.tab:6896', 'uvim1006.tab:6958', 'uvim1006.tab:7020', 'uvim1006.tab:7082']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5181', 'uvim1006.tab:7144', 'uvim1006.tab:7206']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5181', 'uvim1006.tab:7144', 'uvim1006.tab:7206']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5185', 'uvim1006.tab:5186', 'uvim1006.tab:5187', 'uvim1006.tab:5188', 'uvim1006.tab:5189', 'uvim1006.tab:5347', 'uvim1006.tab:5409', 'uvim1006.tab:5471', 'uvim1006.tab:5533', 'uvim1006.tab:5595', 'uvim1006.tab:5657', 'uvim1006.tab:5719', 'uvim1006.tab:5781', 'uvim1006.tab:5843', 'uvim1006.tab:5905', 'uvim1006.tab:5967', 'uvim1006.tab:6029', 'uvim1006.tab:6091', 'uvim1006.tab:6153', 'uvim1006.tab:6215', 'uvim1006.tab:6277', 'uvim1006.tab:6339', 'uvim1006.tab:6401', 'uvim1006.tab:6463', 'uvim1006.tab:6525', 'uvim1006.tab:6587', 'uvim1006.tab:6649', 'uvim1006.tab:6711', 'uvim1006.tab:6773', 'uvim1006.tab:6835', 'uvim1006.tab:6897', 'uvim1006.tab:6959', 'uvim1006.tab:7021', 'uvim1006.tab:7083', 'uvim1006.tab:7145', 'uvim1006.tab:7207']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5185', 'uvim1006.tab:5186', 'uvim1006.tab:5187', 'uvim1006.tab:5188', 'uvim1006.tab:5189', 'uvim1006.tab:5347', 'uvim1006.tab:5409', 'uvim1006.tab:5471', 'uvim1006.tab:5533', 'uvim1006.tab:5595', 'uvim1006.tab:5657', 'uvim1006.tab:5719', 'uvim1006.tab:5781', 'uvim1006.tab:5843', 'uvim1006.tab:5905', 'uvim1006.tab:5967', 'uvim1006.tab:6029', 'uvim1006.tab:6091', 'uvim1006.tab:6153', 'uvim1006.tab:6215', 'uvim1006.tab:6277', 'uvim1006.tab:6339', 'uvim1006.tab:6401', 'uvim1006.tab:6463', 'uvim1006.tab:6525', 'uvim1006.tab:6587', 'uvim1006.tab:6649', 'uvim1006.tab:6711', 'uvim1006.tab:6773', 'uvim1006.tab:6835', 'uvim1006.tab:6897', 'uvim1006.tab:6959', 'uvim1006.tab:7021', 'uvim1006.tab:7083', 'uvim1006.tab:7145', 'uvim1006.tab:7207']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5185', 'uvim1006.tab:5187', 'uvim1006.tab:5188', 'uvim1006.tab:5189', 'uvim1006.tab:5347', 'uvim1006.tab:5409', 'uvim1006.tab:5471', 'uvim1006.tab:5533', 'uvim1006.tab:5595', 'uvim1006.tab:5657', 'uvim1006.tab:5719', 'uvim1006.tab:5781', 'uvim1006.tab:5843', 'uvim1006.tab:5905', 'uvim1006.tab:5967', 'uvim1006.tab:6029', 'uvim1006.tab:6091', 'uvim1006.tab:6153', 'uvim1006.tab:6215', 'uvim1006.tab:6277', 'uvim1006.tab:6339', 'uvim1006.tab:6401', 'uvim1006.tab:6463', 'uvim1006.tab:6525', 'uvim1006.tab:6587', 'uvim1006.tab:6649', 'uvim1006.tab:6711', 'uvim1006.tab:6773', 'uvim1006.tab:6835', 'uvim1006.tab:6897', 'uvim1006.tab:6959', 'uvim1006.tab:7021', 'uvim1006.tab:7083']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5185', 'uvim1006.tab:5187', 'uvim1006.tab:5188', 'uvim1006.tab:5189', 'uvim1006.tab:5347', 'uvim1006.tab:5409', 'uvim1006.tab:5471', 'uvim1006.tab:5533', 'uvim1006.tab:5595', 'uvim1006.tab:5657', 'uvim1006.tab:5719', 'uvim1006.tab:5781', 'uvim1006.tab:5843', 'uvim1006.tab:5905', 'uvim1006.tab:5967', 'uvim1006.tab:6029', 'uvim1006.tab:6091', 'uvim1006.tab:6153', 'uvim1006.tab:6215', 'uvim1006.tab:6277', 'uvim1006.tab:6339', 'uvim1006.tab:6401', 'uvim1006.tab:6463', 'uvim1006.tab:6525', 'uvim1006.tab:6587', 'uvim1006.tab:6649', 'uvim1006.tab:6711', 'uvim1006.tab:6773', 'uvim1006.tab:6835', 'uvim1006.tab:6897', 'uvim1006.tab:6959', 'uvim1006.tab:7021', 'uvim1006.tab:7083']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5186', 'uvim1006.tab:7145', 'uvim1006.tab:7207']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5186', 'uvim1006.tab:7145', 'uvim1006.tab:7207']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5190', 'uvim1006.tab:5191', 'uvim1006.tab:5192', 'uvim1006.tab:5193', 'uvim1006.tab:5194', 'uvim1006.tab:5348', 'uvim1006.tab:5410', 'uvim1006.tab:5472', 'uvim1006.tab:5534', 'uvim1006.tab:5596', 'uvim1006.tab:5658', 'uvim1006.tab:5720', 'uvim1006.tab:5782', 'uvim1006.tab:5844', 'uvim1006.tab:5906', 'uvim1006.tab:5968', 'uvim1006.tab:6030', 'uvim1006.tab:6092', 'uvim1006.tab:6154', 'uvim1006.tab:6216', 'uvim1006.tab:6278', 'uvim1006.tab:6340', 'uvim1006.tab:6402', 'uvim1006.tab:6464', 'uvim1006.tab:6526', 'uvim1006.tab:6588', 'uvim1006.tab:6650', 'uvim1006.tab:6712', 'uvim1006.tab:6774', 'uvim1006.tab:6836', 'uvim1006.tab:6898', 'uvim1006.tab:6960', 'uvim1006.tab:7022', 'uvim1006.tab:7084', 'uvim1006.tab:7146', 'uvim1006.tab:7208']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5190', 'uvim1006.tab:5191', 'uvim1006.tab:5192', 'uvim1006.tab:5193', 'uvim1006.tab:5194', 'uvim1006.tab:5348', 'uvim1006.tab:5410', 'uvim1006.tab:5472', 'uvim1006.tab:5534', 'uvim1006.tab:5596', 'uvim1006.tab:5658', 'uvim1006.tab:5720', 'uvim1006.tab:5782', 'uvim1006.tab:5844', 'uvim1006.tab:5906', 'uvim1006.tab:5968', 'uvim1006.tab:6030', 'uvim1006.tab:6092', 'uvim1006.tab:6154', 'uvim1006.tab:6216', 'uvim1006.tab:6278', 'uvim1006.tab:6340', 'uvim1006.tab:6402', 'uvim1006.tab:6464', 'uvim1006.tab:6526', 'uvim1006.tab:6588', 'uvim1006.tab:6650', 'uvim1006.tab:6712', 'uvim1006.tab:6774', 'uvim1006.tab:6836', 'uvim1006.tab:6898', 'uvim1006.tab:6960', 'uvim1006.tab:7022', 'uvim1006.tab:7084', 'uvim1006.tab:7146', 'uvim1006.tab:7208']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5190', 'uvim1006.tab:5192', 'uvim1006.tab:5193', 'uvim1006.tab:5194', 'uvim1006.tab:5348', 'uvim1006.tab:5410', 'uvim1006.tab:5472', 'uvim1006.tab:5534', 'uvim1006.tab:5596', 'uvim1006.tab:5658', 'uvim1006.tab:5720', 'uvim1006.tab:5782', 'uvim1006.tab:5844', 'uvim1006.tab:5906', 'uvim1006.tab:5968', 'uvim1006.tab:6030', 'uvim1006.tab:6092', 'uvim1006.tab:6154', 'uvim1006.tab:6216', 'uvim1006.tab:6278', 'uvim1006.tab:6340', 'uvim1006.tab:6402', 'uvim1006.tab:6464', 'uvim1006.tab:6526', 'uvim1006.tab:6588', 'uvim1006.tab:6650', 'uvim1006.tab:6712', 'uvim1006.tab:6774', 'uvim1006.tab:6836', 'uvim1006.tab:6898', 'uvim1006.tab:6960', 'uvim1006.tab:7022', 'uvim1006.tab:7084']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5190', 'uvim1006.tab:5192', 'uvim1006.tab:5193', 'uvim1006.tab:5194', 'uvim1006.tab:5348', 'uvim1006.tab:5410', 'uvim1006.tab:5472', 'uvim1006.tab:5534', 'uvim1006.tab:5596', 'uvim1006.tab:5658', 'uvim1006.tab:5720', 'uvim1006.tab:5782', 'uvim1006.tab:5844', 'uvim1006.tab:5906', 'uvim1006.tab:5968', 'uvim1006.tab:6030', 'uvim1006.tab:6092', 'uvim1006.tab:6154', 'uvim1006.tab:6216', 'uvim1006.tab:6278', 'uvim1006.tab:6340', 'uvim1006.tab:6402', 'uvim1006.tab:6464', 'uvim1006.tab:6526', 'uvim1006.tab:6588', 'uvim1006.tab:6650', 'uvim1006.tab:6712', 'uvim1006.tab:6774', 'uvim1006.tab:6836', 'uvim1006.tab:6898', 'uvim1006.tab:6960', 'uvim1006.tab:7022', 'uvim1006.tab:7084']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5191', 'uvim1006.tab:7146', 'uvim1006.tab:7208']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5191', 'uvim1006.tab:7146', 'uvim1006.tab:7208']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5195', 'uvim1006.tab:5196', 'uvim1006.tab:5197', 'uvim1006.tab:5198', 'uvim1006.tab:5199', 'uvim1006.tab:5349', 'uvim1006.tab:5411', 'uvim1006.tab:5473', 'uvim1006.tab:5535', 'uvim1006.tab:5597', 'uvim1006.tab:5659', 'uvim1006.tab:5721', 'uvim1006.tab:5783', 'uvim1006.tab:5845', 'uvim1006.tab:5907', 'uvim1006.tab:5969', 'uvim1006.tab:6031', 'uvim1006.tab:6093', 'uvim1006.tab:6155', 'uvim1006.tab:6217', 'uvim1006.tab:6279', 'uvim1006.tab:6341', 'uvim1006.tab:6403', 'uvim1006.tab:6465', 'uvim1006.tab:6527', 'uvim1006.tab:6589', 'uvim1006.tab:6651', 'uvim1006.tab:6713', 'uvim1006.tab:6775', 'uvim1006.tab:6837', 'uvim1006.tab:6899', 'uvim1006.tab:6961', 'uvim1006.tab:7023', 'uvim1006.tab:7085', 'uvim1006.tab:7147', 'uvim1006.tab:7209']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5195', 'uvim1006.tab:5196', 'uvim1006.tab:5197', 'uvim1006.tab:5198', 'uvim1006.tab:5199', 'uvim1006.tab:5349', 'uvim1006.tab:5411', 'uvim1006.tab:5473', 'uvim1006.tab:5535', 'uvim1006.tab:5597', 'uvim1006.tab:5659', 'uvim1006.tab:5721', 'uvim1006.tab:5783', 'uvim1006.tab:5845', 'uvim1006.tab:5907', 'uvim1006.tab:5969', 'uvim1006.tab:6031', 'uvim1006.tab:6093', 'uvim1006.tab:6155', 'uvim1006.tab:6217', 'uvim1006.tab:6279', 'uvim1006.tab:6341', 'uvim1006.tab:6403', 'uvim1006.tab:6465', 'uvim1006.tab:6527', 'uvim1006.tab:6589', 'uvim1006.tab:6651', 'uvim1006.tab:6713', 'uvim1006.tab:6775', 'uvim1006.tab:6837', 'uvim1006.tab:6899', 'uvim1006.tab:6961', 'uvim1006.tab:7023', 'uvim1006.tab:7085', 'uvim1006.tab:7147', 'uvim1006.tab:7209']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5195', 'uvim1006.tab:5197', 'uvim1006.tab:5198', 'uvim1006.tab:5199', 'uvim1006.tab:5349', 'uvim1006.tab:5411', 'uvim1006.tab:5473', 'uvim1006.tab:5535', 'uvim1006.tab:5597', 'uvim1006.tab:5659', 'uvim1006.tab:5721', 'uvim1006.tab:5783', 'uvim1006.tab:5845', 'uvim1006.tab:5907', 'uvim1006.tab:5969', 'uvim1006.tab:6031', 'uvim1006.tab:6093', 'uvim1006.tab:6155', 'uvim1006.tab:6217', 'uvim1006.tab:6279', 'uvim1006.tab:6341', 'uvim1006.tab:6403', 'uvim1006.tab:6465', 'uvim1006.tab:6527', 'uvim1006.tab:6589', 'uvim1006.tab:6651', 'uvim1006.tab:6713', 'uvim1006.tab:6775', 'uvim1006.tab:6837', 'uvim1006.tab:6899', 'uvim1006.tab:6961', 'uvim1006.tab:7023', 'uvim1006.tab:7085']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5195', 'uvim1006.tab:5197', 'uvim1006.tab:5198', 'uvim1006.tab:5199', 'uvim1006.tab:5349', 'uvim1006.tab:5411', 'uvim1006.tab:5473', 'uvim1006.tab:5535', 'uvim1006.tab:5597', 'uvim1006.tab:5659', 'uvim1006.tab:5721', 'uvim1006.tab:5783', 'uvim1006.tab:5845', 'uvim1006.tab:5907', 'uvim1006.tab:5969', 'uvim1006.tab:6031', 'uvim1006.tab:6093', 'uvim1006.tab:6155', 'uvim1006.tab:6217', 'uvim1006.tab:6279', 'uvim1006.tab:6341', 'uvim1006.tab:6403', 'uvim1006.tab:6465', 'uvim1006.tab:6527', 'uvim1006.tab:6589', 'uvim1006.tab:6651', 'uvim1006.tab:6713', 'uvim1006.tab:6775', 'uvim1006.tab:6837', 'uvim1006.tab:6899', 'uvim1006.tab:6961', 'uvim1006.tab:7023', 'uvim1006.tab:7085']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5196', 'uvim1006.tab:7147', 'uvim1006.tab:7209']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5196', 'uvim1006.tab:7147', 'uvim1006.tab:7209']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5200', 'uvim1006.tab:5201', 'uvim1006.tab:5202', 'uvim1006.tab:5203', 'uvim1006.tab:5204', 'uvim1006.tab:5350', 'uvim1006.tab:5412', 'uvim1006.tab:5474', 'uvim1006.tab:5536', 'uvim1006.tab:5598', 'uvim1006.tab:5660', 'uvim1006.tab:5722', 'uvim1006.tab:5784', 'uvim1006.tab:5846', 'uvim1006.tab:5908', 'uvim1006.tab:5970', 'uvim1006.tab:6032', 'uvim1006.tab:6094', 'uvim1006.tab:6156', 'uvim1006.tab:6218', 'uvim1006.tab:6280', 'uvim1006.tab:6342', 'uvim1006.tab:6404', 'uvim1006.tab:6466', 'uvim1006.tab:6528', 'uvim1006.tab:6590', 'uvim1006.tab:6652', 'uvim1006.tab:6714', 'uvim1006.tab:6776', 'uvim1006.tab:6838', 'uvim1006.tab:6900', 'uvim1006.tab:6962', 'uvim1006.tab:7024', 'uvim1006.tab:7086', 'uvim1006.tab:7148', 'uvim1006.tab:7210']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5200', 'uvim1006.tab:5201', 'uvim1006.tab:5202', 'uvim1006.tab:5203', 'uvim1006.tab:5204', 'uvim1006.tab:5350', 'uvim1006.tab:5412', 'uvim1006.tab:5474', 'uvim1006.tab:5536', 'uvim1006.tab:5598', 'uvim1006.tab:5660', 'uvim1006.tab:5722', 'uvim1006.tab:5784', 'uvim1006.tab:5846', 'uvim1006.tab:5908', 'uvim1006.tab:5970', 'uvim1006.tab:6032', 'uvim1006.tab:6094', 'uvim1006.tab:6156', 'uvim1006.tab:6218', 'uvim1006.tab:6280', 'uvim1006.tab:6342', 'uvim1006.tab:6404', 'uvim1006.tab:6466', 'uvim1006.tab:6528', 'uvim1006.tab:6590', 'uvim1006.tab:6652', 'uvim1006.tab:6714', 'uvim1006.tab:6776', 'uvim1006.tab:6838', 'uvim1006.tab:6900', 'uvim1006.tab:6962', 'uvim1006.tab:7024', 'uvim1006.tab:7086', 'uvim1006.tab:7148', 'uvim1006.tab:7210']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5200', 'uvim1006.tab:5202', 'uvim1006.tab:5203', 'uvim1006.tab:5204', 'uvim1006.tab:5350', 'uvim1006.tab:5412', 'uvim1006.tab:5474', 'uvim1006.tab:5536', 'uvim1006.tab:5598', 'uvim1006.tab:5660', 'uvim1006.tab:5722', 'uvim1006.tab:5784', 'uvim1006.tab:5846', 'uvim1006.tab:5908', 'uvim1006.tab:5970', 'uvim1006.tab:6032', 'uvim1006.tab:6094', 'uvim1006.tab:6156', 'uvim1006.tab:6218', 'uvim1006.tab:6280', 'uvim1006.tab:6342', 'uvim1006.tab:6404', 'uvim1006.tab:6466', 'uvim1006.tab:6528', 'uvim1006.tab:6590', 'uvim1006.tab:6652', 'uvim1006.tab:6714', 'uvim1006.tab:6776', 'uvim1006.tab:6838', 'uvim1006.tab:6900', 'uvim1006.tab:6962', 'uvim1006.tab:7024', 'uvim1006.tab:7086']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5200', 'uvim1006.tab:5202', 'uvim1006.tab:5203', 'uvim1006.tab:5204', 'uvim1006.tab:5350', 'uvim1006.tab:5412', 'uvim1006.tab:5474', 'uvim1006.tab:5536', 'uvim1006.tab:5598', 'uvim1006.tab:5660', 'uvim1006.tab:5722', 'uvim1006.tab:5784', 'uvim1006.tab:5846', 'uvim1006.tab:5908', 'uvim1006.tab:5970', 'uvim1006.tab:6032', 'uvim1006.tab:6094', 'uvim1006.tab:6156', 'uvim1006.tab:6218', 'uvim1006.tab:6280', 'uvim1006.tab:6342', 'uvim1006.tab:6404', 'uvim1006.tab:6466', 'uvim1006.tab:6528', 'uvim1006.tab:6590', 'uvim1006.tab:6652', 'uvim1006.tab:6714', 'uvim1006.tab:6776', 'uvim1006.tab:6838', 'uvim1006.tab:6900', 'uvim1006.tab:6962', 'uvim1006.tab:7024', 'uvim1006.tab:7086']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5201', 'uvim1006.tab:7148', 'uvim1006.tab:7210']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5201', 'uvim1006.tab:7148', 'uvim1006.tab:7210']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5205', 'uvim1006.tab:5206', 'uvim1006.tab:5207', 'uvim1006.tab:5208', 'uvim1006.tab:5209', 'uvim1006.tab:5351', 'uvim1006.tab:5413', 'uvim1006.tab:5475', 'uvim1006.tab:5537', 'uvim1006.tab:5599', 'uvim1006.tab:5661', 'uvim1006.tab:5723', 'uvim1006.tab:5785', 'uvim1006.tab:5847', 'uvim1006.tab:5909', 'uvim1006.tab:5971', 'uvim1006.tab:6033', 'uvim1006.tab:6095', 'uvim1006.tab:6157', 'uvim1006.tab:6219', 'uvim1006.tab:6281', 'uvim1006.tab:6343', 'uvim1006.tab:6405', 'uvim1006.tab:6467', 'uvim1006.tab:6529', 'uvim1006.tab:6591', 'uvim1006.tab:6653', 'uvim1006.tab:6715', 'uvim1006.tab:6777', 'uvim1006.tab:6839', 'uvim1006.tab:6901', 'uvim1006.tab:6963', 'uvim1006.tab:7025', 'uvim1006.tab:7087', 'uvim1006.tab:7149', 'uvim1006.tab:7211']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5205', 'uvim1006.tab:5206', 'uvim1006.tab:5207', 'uvim1006.tab:5208', 'uvim1006.tab:5209', 'uvim1006.tab:5351', 'uvim1006.tab:5413', 'uvim1006.tab:5475', 'uvim1006.tab:5537', 'uvim1006.tab:5599', 'uvim1006.tab:5661', 'uvim1006.tab:5723', 'uvim1006.tab:5785', 'uvim1006.tab:5847', 'uvim1006.tab:5909', 'uvim1006.tab:5971', 'uvim1006.tab:6033', 'uvim1006.tab:6095', 'uvim1006.tab:6157', 'uvim1006.tab:6219', 'uvim1006.tab:6281', 'uvim1006.tab:6343', 'uvim1006.tab:6405', 'uvim1006.tab:6467', 'uvim1006.tab:6529', 'uvim1006.tab:6591', 'uvim1006.tab:6653', 'uvim1006.tab:6715', 'uvim1006.tab:6777', 'uvim1006.tab:6839', 'uvim1006.tab:6901', 'uvim1006.tab:6963', 'uvim1006.tab:7025', 'uvim1006.tab:7087', 'uvim1006.tab:7149', 'uvim1006.tab:7211']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5205', 'uvim1006.tab:5207', 'uvim1006.tab:5208', 'uvim1006.tab:5209', 'uvim1006.tab:5351', 'uvim1006.tab:5413', 'uvim1006.tab:5475', 'uvim1006.tab:5537', 'uvim1006.tab:5599', 'uvim1006.tab:5661', 'uvim1006.tab:5723', 'uvim1006.tab:5785', 'uvim1006.tab:5847', 'uvim1006.tab:5909', 'uvim1006.tab:5971', 'uvim1006.tab:6033', 'uvim1006.tab:6095', 'uvim1006.tab:6157', 'uvim1006.tab:6219', 'uvim1006.tab:6281', 'uvim1006.tab:6343', 'uvim1006.tab:6405', 'uvim1006.tab:6467', 'uvim1006.tab:6529', 'uvim1006.tab:6591', 'uvim1006.tab:6653', 'uvim1006.tab:6715', 'uvim1006.tab:6777', 'uvim1006.tab:6839', 'uvim1006.tab:6901', 'uvim1006.tab:6963', 'uvim1006.tab:7025', 'uvim1006.tab:7087']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5205', 'uvim1006.tab:5207', 'uvim1006.tab:5208', 'uvim1006.tab:5209', 'uvim1006.tab:5351', 'uvim1006.tab:5413', 'uvim1006.tab:5475', 'uvim1006.tab:5537', 'uvim1006.tab:5599', 'uvim1006.tab:5661', 'uvim1006.tab:5723', 'uvim1006.tab:5785', 'uvim1006.tab:5847', 'uvim1006.tab:5909', 'uvim1006.tab:5971', 'uvim1006.tab:6033', 'uvim1006.tab:6095', 'uvim1006.tab:6157', 'uvim1006.tab:6219', 'uvim1006.tab:6281', 'uvim1006.tab:6343', 'uvim1006.tab:6405', 'uvim1006.tab:6467', 'uvim1006.tab:6529', 'uvim1006.tab:6591', 'uvim1006.tab:6653', 'uvim1006.tab:6715', 'uvim1006.tab:6777', 'uvim1006.tab:6839', 'uvim1006.tab:6901', 'uvim1006.tab:6963', 'uvim1006.tab:7025', 'uvim1006.tab:7087']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5206', 'uvim1006.tab:7149', 'uvim1006.tab:7211']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5206', 'uvim1006.tab:7149', 'uvim1006.tab:7211']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5210', 'uvim1006.tab:5211', 'uvim1006.tab:5212', 'uvim1006.tab:5213', 'uvim1006.tab:5214', 'uvim1006.tab:5352', 'uvim1006.tab:5414', 'uvim1006.tab:5476', 'uvim1006.tab:5538', 'uvim1006.tab:5600', 'uvim1006.tab:5662', 'uvim1006.tab:5724', 'uvim1006.tab:5786', 'uvim1006.tab:5848', 'uvim1006.tab:5910', 'uvim1006.tab:5972', 'uvim1006.tab:6034', 'uvim1006.tab:6096', 'uvim1006.tab:6158', 'uvim1006.tab:6220', 'uvim1006.tab:6282', 'uvim1006.tab:6344', 'uvim1006.tab:6406', 'uvim1006.tab:6468', 'uvim1006.tab:6530', 'uvim1006.tab:6592', 'uvim1006.tab:6654', 'uvim1006.tab:6716', 'uvim1006.tab:6778', 'uvim1006.tab:6840', 'uvim1006.tab:6902', 'uvim1006.tab:6964', 'uvim1006.tab:7026', 'uvim1006.tab:7088', 'uvim1006.tab:7150', 'uvim1006.tab:7212']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5210', 'uvim1006.tab:5211', 'uvim1006.tab:5212', 'uvim1006.tab:5213', 'uvim1006.tab:5214', 'uvim1006.tab:5352', 'uvim1006.tab:5414', 'uvim1006.tab:5476', 'uvim1006.tab:5538', 'uvim1006.tab:5600', 'uvim1006.tab:5662', 'uvim1006.tab:5724', 'uvim1006.tab:5786', 'uvim1006.tab:5848', 'uvim1006.tab:5910', 'uvim1006.tab:5972', 'uvim1006.tab:6034', 'uvim1006.tab:6096', 'uvim1006.tab:6158', 'uvim1006.tab:6220', 'uvim1006.tab:6282', 'uvim1006.tab:6344', 'uvim1006.tab:6406', 'uvim1006.tab:6468', 'uvim1006.tab:6530', 'uvim1006.tab:6592', 'uvim1006.tab:6654', 'uvim1006.tab:6716', 'uvim1006.tab:6778', 'uvim1006.tab:6840', 'uvim1006.tab:6902', 'uvim1006.tab:6964', 'uvim1006.tab:7026', 'uvim1006.tab:7088', 'uvim1006.tab:7150', 'uvim1006.tab:7212']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5210', 'uvim1006.tab:5212', 'uvim1006.tab:5213', 'uvim1006.tab:5214', 'uvim1006.tab:5352', 'uvim1006.tab:5414', 'uvim1006.tab:5476', 'uvim1006.tab:5538', 'uvim1006.tab:5600', 'uvim1006.tab:5662', 'uvim1006.tab:5724', 'uvim1006.tab:5786', 'uvim1006.tab:5848', 'uvim1006.tab:5910', 'uvim1006.tab:5972', 'uvim1006.tab:6034', 'uvim1006.tab:6096', 'uvim1006.tab:6158', 'uvim1006.tab:6220', 'uvim1006.tab:6282', 'uvim1006.tab:6344', 'uvim1006.tab:6406', 'uvim1006.tab:6468', 'uvim1006.tab:6530', 'uvim1006.tab:6592', 'uvim1006.tab:6654', 'uvim1006.tab:6716', 'uvim1006.tab:6778', 'uvim1006.tab:6840', 'uvim1006.tab:6902', 'uvim1006.tab:6964', 'uvim1006.tab:7026', 'uvim1006.tab:7088']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5210', 'uvim1006.tab:5212', 'uvim1006.tab:5213', 'uvim1006.tab:5214', 'uvim1006.tab:5352', 'uvim1006.tab:5414', 'uvim1006.tab:5476', 'uvim1006.tab:5538', 'uvim1006.tab:5600', 'uvim1006.tab:5662', 'uvim1006.tab:5724', 'uvim1006.tab:5786', 'uvim1006.tab:5848', 'uvim1006.tab:5910', 'uvim1006.tab:5972', 'uvim1006.tab:6034', 'uvim1006.tab:6096', 'uvim1006.tab:6158', 'uvim1006.tab:6220', 'uvim1006.tab:6282', 'uvim1006.tab:6344', 'uvim1006.tab:6406', 'uvim1006.tab:6468', 'uvim1006.tab:6530', 'uvim1006.tab:6592', 'uvim1006.tab:6654', 'uvim1006.tab:6716', 'uvim1006.tab:6778', 'uvim1006.tab:6840', 'uvim1006.tab:6902', 'uvim1006.tab:6964', 'uvim1006.tab:7026', 'uvim1006.tab:7088']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5211', 'uvim1006.tab:7150', 'uvim1006.tab:7212']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5211', 'uvim1006.tab:7150', 'uvim1006.tab:7212']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5215', 'uvim1006.tab:5216', 'uvim1006.tab:5217', 'uvim1006.tab:5218', 'uvim1006.tab:5219', 'uvim1006.tab:5353', 'uvim1006.tab:5415', 'uvim1006.tab:5477', 'uvim1006.tab:5539', 'uvim1006.tab:5601', 'uvim1006.tab:5663', 'uvim1006.tab:5725', 'uvim1006.tab:5787', 'uvim1006.tab:5849', 'uvim1006.tab:5911', 'uvim1006.tab:5973', 'uvim1006.tab:6035', 'uvim1006.tab:6097', 'uvim1006.tab:6159', 'uvim1006.tab:6221', 'uvim1006.tab:6283', 'uvim1006.tab:6345', 'uvim1006.tab:6407', 'uvim1006.tab:6469', 'uvim1006.tab:6531', 'uvim1006.tab:6593', 'uvim1006.tab:6655', 'uvim1006.tab:6717', 'uvim1006.tab:6779', 'uvim1006.tab:6841', 'uvim1006.tab:6903', 'uvim1006.tab:6965', 'uvim1006.tab:7027', 'uvim1006.tab:7089', 'uvim1006.tab:7151', 'uvim1006.tab:7213']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5215', 'uvim1006.tab:5216', 'uvim1006.tab:5217', 'uvim1006.tab:5218', 'uvim1006.tab:5219', 'uvim1006.tab:5353', 'uvim1006.tab:5415', 'uvim1006.tab:5477', 'uvim1006.tab:5539', 'uvim1006.tab:5601', 'uvim1006.tab:5663', 'uvim1006.tab:5725', 'uvim1006.tab:5787', 'uvim1006.tab:5849', 'uvim1006.tab:5911', 'uvim1006.tab:5973', 'uvim1006.tab:6035', 'uvim1006.tab:6097', 'uvim1006.tab:6159', 'uvim1006.tab:6221', 'uvim1006.tab:6283', 'uvim1006.tab:6345', 'uvim1006.tab:6407', 'uvim1006.tab:6469', 'uvim1006.tab:6531', 'uvim1006.tab:6593', 'uvim1006.tab:6655', 'uvim1006.tab:6717', 'uvim1006.tab:6779', 'uvim1006.tab:6841', 'uvim1006.tab:6903', 'uvim1006.tab:6965', 'uvim1006.tab:7027', 'uvim1006.tab:7089', 'uvim1006.tab:7151', 'uvim1006.tab:7213']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5215', 'uvim1006.tab:5217', 'uvim1006.tab:5218', 'uvim1006.tab:5219', 'uvim1006.tab:5353', 'uvim1006.tab:5415', 'uvim1006.tab:5477', 'uvim1006.tab:5539', 'uvim1006.tab:5601', 'uvim1006.tab:5663', 'uvim1006.tab:5725', 'uvim1006.tab:5787', 'uvim1006.tab:5849', 'uvim1006.tab:5911', 'uvim1006.tab:5973', 'uvim1006.tab:6035', 'uvim1006.tab:6097', 'uvim1006.tab:6159', 'uvim1006.tab:6221', 'uvim1006.tab:6283', 'uvim1006.tab:6345', 'uvim1006.tab:6407', 'uvim1006.tab:6469', 'uvim1006.tab:6531', 'uvim1006.tab:6593', 'uvim1006.tab:6655', 'uvim1006.tab:6717', 'uvim1006.tab:6779', 'uvim1006.tab:6841', 'uvim1006.tab:6903', 'uvim1006.tab:6965', 'uvim1006.tab:7027', 'uvim1006.tab:7089']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5215', 'uvim1006.tab:5217', 'uvim1006.tab:5218', 'uvim1006.tab:5219', 'uvim1006.tab:5353', 'uvim1006.tab:5415', 'uvim1006.tab:5477', 'uvim1006.tab:5539', 'uvim1006.tab:5601', 'uvim1006.tab:5663', 'uvim1006.tab:5725', 'uvim1006.tab:5787', 'uvim1006.tab:5849', 'uvim1006.tab:5911', 'uvim1006.tab:5973', 'uvim1006.tab:6035', 'uvim1006.tab:6097', 'uvim1006.tab:6159', 'uvim1006.tab:6221', 'uvim1006.tab:6283', 'uvim1006.tab:6345', 'uvim1006.tab:6407', 'uvim1006.tab:6469', 'uvim1006.tab:6531', 'uvim1006.tab:6593', 'uvim1006.tab:6655', 'uvim1006.tab:6717', 'uvim1006.tab:6779', 'uvim1006.tab:6841', 'uvim1006.tab:6903', 'uvim1006.tab:6965', 'uvim1006.tab:7027', 'uvim1006.tab:7089']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5216', 'uvim1006.tab:7151', 'uvim1006.tab:7213']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5216', 'uvim1006.tab:7151', 'uvim1006.tab:7213']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5220', 'uvim1006.tab:5221', 'uvim1006.tab:5222', 'uvim1006.tab:5223', 'uvim1006.tab:5224', 'uvim1006.tab:5354', 'uvim1006.tab:5416', 'uvim1006.tab:5478', 'uvim1006.tab:5540', 'uvim1006.tab:5602', 'uvim1006.tab:5664', 'uvim1006.tab:5726', 'uvim1006.tab:5788', 'uvim1006.tab:5850', 'uvim1006.tab:5912', 'uvim1006.tab:5974', 'uvim1006.tab:6036', 'uvim1006.tab:6098', 'uvim1006.tab:6160', 'uvim1006.tab:6222', 'uvim1006.tab:6284', 'uvim1006.tab:6346', 'uvim1006.tab:6408', 'uvim1006.tab:6470', 'uvim1006.tab:6532', 'uvim1006.tab:6594', 'uvim1006.tab:6656', 'uvim1006.tab:6718', 'uvim1006.tab:6780', 'uvim1006.tab:6842', 'uvim1006.tab:6904', 'uvim1006.tab:6966', 'uvim1006.tab:7028', 'uvim1006.tab:7090', 'uvim1006.tab:7152', 'uvim1006.tab:7214']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5220', 'uvim1006.tab:5221', 'uvim1006.tab:5222', 'uvim1006.tab:5223', 'uvim1006.tab:5224', 'uvim1006.tab:5354', 'uvim1006.tab:5416', 'uvim1006.tab:5478', 'uvim1006.tab:5540', 'uvim1006.tab:5602', 'uvim1006.tab:5664', 'uvim1006.tab:5726', 'uvim1006.tab:5788', 'uvim1006.tab:5850', 'uvim1006.tab:5912', 'uvim1006.tab:5974', 'uvim1006.tab:6036', 'uvim1006.tab:6098', 'uvim1006.tab:6160', 'uvim1006.tab:6222', 'uvim1006.tab:6284', 'uvim1006.tab:6346', 'uvim1006.tab:6408', 'uvim1006.tab:6470', 'uvim1006.tab:6532', 'uvim1006.tab:6594', 'uvim1006.tab:6656', 'uvim1006.tab:6718', 'uvim1006.tab:6780', 'uvim1006.tab:6842', 'uvim1006.tab:6904', 'uvim1006.tab:6966', 'uvim1006.tab:7028', 'uvim1006.tab:7090', 'uvim1006.tab:7152', 'uvim1006.tab:7214']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5220', 'uvim1006.tab:5222', 'uvim1006.tab:5223', 'uvim1006.tab:5224', 'uvim1006.tab:5354', 'uvim1006.tab:5416', 'uvim1006.tab:5478', 'uvim1006.tab:5540', 'uvim1006.tab:5602', 'uvim1006.tab:5664', 'uvim1006.tab:5726', 'uvim1006.tab:5788', 'uvim1006.tab:5850', 'uvim1006.tab:5912', 'uvim1006.tab:5974', 'uvim1006.tab:6036', 'uvim1006.tab:6098', 'uvim1006.tab:6160', 'uvim1006.tab:6222', 'uvim1006.tab:6284', 'uvim1006.tab:6346', 'uvim1006.tab:6408', 'uvim1006.tab:6470', 'uvim1006.tab:6532', 'uvim1006.tab:6594', 'uvim1006.tab:6656', 'uvim1006.tab:6718', 'uvim1006.tab:6780', 'uvim1006.tab:6842', 'uvim1006.tab:6904', 'uvim1006.tab:6966', 'uvim1006.tab:7028', 'uvim1006.tab:7090']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5220', 'uvim1006.tab:5222', 'uvim1006.tab:5223', 'uvim1006.tab:5224', 'uvim1006.tab:5354', 'uvim1006.tab:5416', 'uvim1006.tab:5478', 'uvim1006.tab:5540', 'uvim1006.tab:5602', 'uvim1006.tab:5664', 'uvim1006.tab:5726', 'uvim1006.tab:5788', 'uvim1006.tab:5850', 'uvim1006.tab:5912', 'uvim1006.tab:5974', 'uvim1006.tab:6036', 'uvim1006.tab:6098', 'uvim1006.tab:6160', 'uvim1006.tab:6222', 'uvim1006.tab:6284', 'uvim1006.tab:6346', 'uvim1006.tab:6408', 'uvim1006.tab:6470', 'uvim1006.tab:6532', 'uvim1006.tab:6594', 'uvim1006.tab:6656', 'uvim1006.tab:6718', 'uvim1006.tab:6780', 'uvim1006.tab:6842', 'uvim1006.tab:6904', 'uvim1006.tab:6966', 'uvim1006.tab:7028', 'uvim1006.tab:7090']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5221', 'uvim1006.tab:7152', 'uvim1006.tab:7214']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5221', 'uvim1006.tab:7152', 'uvim1006.tab:7214']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5225', 'uvim1006.tab:5226', 'uvim1006.tab:5227', 'uvim1006.tab:5228', 'uvim1006.tab:5229', 'uvim1006.tab:5355', 'uvim1006.tab:5417', 'uvim1006.tab:5479', 'uvim1006.tab:5541', 'uvim1006.tab:5603', 'uvim1006.tab:5665', 'uvim1006.tab:5727', 'uvim1006.tab:5789', 'uvim1006.tab:5851', 'uvim1006.tab:5913', 'uvim1006.tab:5975', 'uvim1006.tab:6037', 'uvim1006.tab:6099', 'uvim1006.tab:6161', 'uvim1006.tab:6223', 'uvim1006.tab:6285', 'uvim1006.tab:6347', 'uvim1006.tab:6409', 'uvim1006.tab:6471', 'uvim1006.tab:6533', 'uvim1006.tab:6595', 'uvim1006.tab:6657', 'uvim1006.tab:6719', 'uvim1006.tab:6781', 'uvim1006.tab:6843', 'uvim1006.tab:6905', 'uvim1006.tab:6967', 'uvim1006.tab:7029', 'uvim1006.tab:7091', 'uvim1006.tab:7153', 'uvim1006.tab:7215']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5225', 'uvim1006.tab:5226', 'uvim1006.tab:5227', 'uvim1006.tab:5228', 'uvim1006.tab:5229', 'uvim1006.tab:5355', 'uvim1006.tab:5417', 'uvim1006.tab:5479', 'uvim1006.tab:5541', 'uvim1006.tab:5603', 'uvim1006.tab:5665', 'uvim1006.tab:5727', 'uvim1006.tab:5789', 'uvim1006.tab:5851', 'uvim1006.tab:5913', 'uvim1006.tab:5975', 'uvim1006.tab:6037', 'uvim1006.tab:6099', 'uvim1006.tab:6161', 'uvim1006.tab:6223', 'uvim1006.tab:6285', 'uvim1006.tab:6347', 'uvim1006.tab:6409', 'uvim1006.tab:6471', 'uvim1006.tab:6533', 'uvim1006.tab:6595', 'uvim1006.tab:6657', 'uvim1006.tab:6719', 'uvim1006.tab:6781', 'uvim1006.tab:6843', 'uvim1006.tab:6905', 'uvim1006.tab:6967', 'uvim1006.tab:7029', 'uvim1006.tab:7091', 'uvim1006.tab:7153', 'uvim1006.tab:7215']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5225', 'uvim1006.tab:5227', 'uvim1006.tab:5228', 'uvim1006.tab:5229', 'uvim1006.tab:5355', 'uvim1006.tab:5417', 'uvim1006.tab:5479', 'uvim1006.tab:5541', 'uvim1006.tab:5603', 'uvim1006.tab:5665', 'uvim1006.tab:5727', 'uvim1006.tab:5789', 'uvim1006.tab:5851', 'uvim1006.tab:5913', 'uvim1006.tab:5975', 'uvim1006.tab:6037', 'uvim1006.tab:6099', 'uvim1006.tab:6161', 'uvim1006.tab:6223', 'uvim1006.tab:6285', 'uvim1006.tab:6347', 'uvim1006.tab:6409', 'uvim1006.tab:6471', 'uvim1006.tab:6533', 'uvim1006.tab:6595', 'uvim1006.tab:6657', 'uvim1006.tab:6719', 'uvim1006.tab:6781', 'uvim1006.tab:6843', 'uvim1006.tab:6905', 'uvim1006.tab:6967', 'uvim1006.tab:7029', 'uvim1006.tab:7091']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5225', 'uvim1006.tab:5227', 'uvim1006.tab:5228', 'uvim1006.tab:5229', 'uvim1006.tab:5355', 'uvim1006.tab:5417', 'uvim1006.tab:5479', 'uvim1006.tab:5541', 'uvim1006.tab:5603', 'uvim1006.tab:5665', 'uvim1006.tab:5727', 'uvim1006.tab:5789', 'uvim1006.tab:5851', 'uvim1006.tab:5913', 'uvim1006.tab:5975', 'uvim1006.tab:6037', 'uvim1006.tab:6099', 'uvim1006.tab:6161', 'uvim1006.tab:6223', 'uvim1006.tab:6285', 'uvim1006.tab:6347', 'uvim1006.tab:6409', 'uvim1006.tab:6471', 'uvim1006.tab:6533', 'uvim1006.tab:6595', 'uvim1006.tab:6657', 'uvim1006.tab:6719', 'uvim1006.tab:6781', 'uvim1006.tab:6843', 'uvim1006.tab:6905', 'uvim1006.tab:6967', 'uvim1006.tab:7029', 'uvim1006.tab:7091']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5226', 'uvim1006.tab:7153', 'uvim1006.tab:7215']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5226', 'uvim1006.tab:7153', 'uvim1006.tab:7215']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5230', 'uvim1006.tab:5231', 'uvim1006.tab:5232', 'uvim1006.tab:5233', 'uvim1006.tab:5234', 'uvim1006.tab:5356', 'uvim1006.tab:5418', 'uvim1006.tab:5480', 'uvim1006.tab:5542', 'uvim1006.tab:5604', 'uvim1006.tab:5666', 'uvim1006.tab:5728', 'uvim1006.tab:5790', 'uvim1006.tab:5852', 'uvim1006.tab:5914', 'uvim1006.tab:5976', 'uvim1006.tab:6038', 'uvim1006.tab:6100', 'uvim1006.tab:6162', 'uvim1006.tab:6224', 'uvim1006.tab:6286', 'uvim1006.tab:6348', 'uvim1006.tab:6410', 'uvim1006.tab:6472', 'uvim1006.tab:6534', 'uvim1006.tab:6596', 'uvim1006.tab:6658', 'uvim1006.tab:6720', 'uvim1006.tab:6782', 'uvim1006.tab:6844', 'uvim1006.tab:6906', 'uvim1006.tab:6968', 'uvim1006.tab:7030', 'uvim1006.tab:7092', 'uvim1006.tab:7154', 'uvim1006.tab:7216']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5230', 'uvim1006.tab:5231', 'uvim1006.tab:5232', 'uvim1006.tab:5233', 'uvim1006.tab:5234', 'uvim1006.tab:5356', 'uvim1006.tab:5418', 'uvim1006.tab:5480', 'uvim1006.tab:5542', 'uvim1006.tab:5604', 'uvim1006.tab:5666', 'uvim1006.tab:5728', 'uvim1006.tab:5790', 'uvim1006.tab:5852', 'uvim1006.tab:5914', 'uvim1006.tab:5976', 'uvim1006.tab:6038', 'uvim1006.tab:6100', 'uvim1006.tab:6162', 'uvim1006.tab:6224', 'uvim1006.tab:6286', 'uvim1006.tab:6348', 'uvim1006.tab:6410', 'uvim1006.tab:6472', 'uvim1006.tab:6534', 'uvim1006.tab:6596', 'uvim1006.tab:6658', 'uvim1006.tab:6720', 'uvim1006.tab:6782', 'uvim1006.tab:6844', 'uvim1006.tab:6906', 'uvim1006.tab:6968', 'uvim1006.tab:7030', 'uvim1006.tab:7092', 'uvim1006.tab:7154', 'uvim1006.tab:7216']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5230', 'uvim1006.tab:5232', 'uvim1006.tab:5233', 'uvim1006.tab:5234', 'uvim1006.tab:5356', 'uvim1006.tab:5418', 'uvim1006.tab:5480', 'uvim1006.tab:5542', 'uvim1006.tab:5604', 'uvim1006.tab:5666', 'uvim1006.tab:5728', 'uvim1006.tab:5790', 'uvim1006.tab:5852', 'uvim1006.tab:5914', 'uvim1006.tab:5976', 'uvim1006.tab:6038', 'uvim1006.tab:6100', 'uvim1006.tab:6162', 'uvim1006.tab:6224', 'uvim1006.tab:6286', 'uvim1006.tab:6348', 'uvim1006.tab:6410', 'uvim1006.tab:6472', 'uvim1006.tab:6534', 'uvim1006.tab:6596', 'uvim1006.tab:6658', 'uvim1006.tab:6720', 'uvim1006.tab:6782', 'uvim1006.tab:6844', 'uvim1006.tab:6906', 'uvim1006.tab:6968', 'uvim1006.tab:7030', 'uvim1006.tab:7092']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5230', 'uvim1006.tab:5232', 'uvim1006.tab:5233', 'uvim1006.tab:5234', 'uvim1006.tab:5356', 'uvim1006.tab:5418', 'uvim1006.tab:5480', 'uvim1006.tab:5542', 'uvim1006.tab:5604', 'uvim1006.tab:5666', 'uvim1006.tab:5728', 'uvim1006.tab:5790', 'uvim1006.tab:5852', 'uvim1006.tab:5914', 'uvim1006.tab:5976', 'uvim1006.tab:6038', 'uvim1006.tab:6100', 'uvim1006.tab:6162', 'uvim1006.tab:6224', 'uvim1006.tab:6286', 'uvim1006.tab:6348', 'uvim1006.tab:6410', 'uvim1006.tab:6472', 'uvim1006.tab:6534', 'uvim1006.tab:6596', 'uvim1006.tab:6658', 'uvim1006.tab:6720', 'uvim1006.tab:6782', 'uvim1006.tab:6844', 'uvim1006.tab:6906', 'uvim1006.tab:6968', 'uvim1006.tab:7030', 'uvim1006.tab:7092']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5231', 'uvim1006.tab:7154', 'uvim1006.tab:7216']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5231', 'uvim1006.tab:7154', 'uvim1006.tab:7216']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5235', 'uvim1006.tab:5236', 'uvim1006.tab:5237', 'uvim1006.tab:5238', 'uvim1006.tab:5239', 'uvim1006.tab:5357', 'uvim1006.tab:5419', 'uvim1006.tab:5481', 'uvim1006.tab:5543', 'uvim1006.tab:5605', 'uvim1006.tab:5667', 'uvim1006.tab:5729', 'uvim1006.tab:5791', 'uvim1006.tab:5853', 'uvim1006.tab:5915', 'uvim1006.tab:5977', 'uvim1006.tab:6039', 'uvim1006.tab:6101', 'uvim1006.tab:6163', 'uvim1006.tab:6225', 'uvim1006.tab:6287', 'uvim1006.tab:6349', 'uvim1006.tab:6411', 'uvim1006.tab:6473', 'uvim1006.tab:6535', 'uvim1006.tab:6597', 'uvim1006.tab:6659', 'uvim1006.tab:6721', 'uvim1006.tab:6783', 'uvim1006.tab:6845', 'uvim1006.tab:6907', 'uvim1006.tab:6969', 'uvim1006.tab:7031', 'uvim1006.tab:7093', 'uvim1006.tab:7155', 'uvim1006.tab:7217']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5235', 'uvim1006.tab:5236', 'uvim1006.tab:5237', 'uvim1006.tab:5238', 'uvim1006.tab:5239', 'uvim1006.tab:5357', 'uvim1006.tab:5419', 'uvim1006.tab:5481', 'uvim1006.tab:5543', 'uvim1006.tab:5605', 'uvim1006.tab:5667', 'uvim1006.tab:5729', 'uvim1006.tab:5791', 'uvim1006.tab:5853', 'uvim1006.tab:5915', 'uvim1006.tab:5977', 'uvim1006.tab:6039', 'uvim1006.tab:6101', 'uvim1006.tab:6163', 'uvim1006.tab:6225', 'uvim1006.tab:6287', 'uvim1006.tab:6349', 'uvim1006.tab:6411', 'uvim1006.tab:6473', 'uvim1006.tab:6535', 'uvim1006.tab:6597', 'uvim1006.tab:6659', 'uvim1006.tab:6721', 'uvim1006.tab:6783', 'uvim1006.tab:6845', 'uvim1006.tab:6907', 'uvim1006.tab:6969', 'uvim1006.tab:7031', 'uvim1006.tab:7093', 'uvim1006.tab:7155', 'uvim1006.tab:7217']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5235', 'uvim1006.tab:5237', 'uvim1006.tab:5238', 'uvim1006.tab:5239', 'uvim1006.tab:5357', 'uvim1006.tab:5419', 'uvim1006.tab:5481', 'uvim1006.tab:5543', 'uvim1006.tab:5605', 'uvim1006.tab:5667', 'uvim1006.tab:5729', 'uvim1006.tab:5791', 'uvim1006.tab:5853', 'uvim1006.tab:5915', 'uvim1006.tab:5977', 'uvim1006.tab:6039', 'uvim1006.tab:6101', 'uvim1006.tab:6163', 'uvim1006.tab:6225', 'uvim1006.tab:6287', 'uvim1006.tab:6349', 'uvim1006.tab:6411', 'uvim1006.tab:6473', 'uvim1006.tab:6535', 'uvim1006.tab:6597', 'uvim1006.tab:6659', 'uvim1006.tab:6721', 'uvim1006.tab:6783', 'uvim1006.tab:6845', 'uvim1006.tab:6907', 'uvim1006.tab:6969', 'uvim1006.tab:7031', 'uvim1006.tab:7093']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5235', 'uvim1006.tab:5237', 'uvim1006.tab:5238', 'uvim1006.tab:5239', 'uvim1006.tab:5357', 'uvim1006.tab:5419', 'uvim1006.tab:5481', 'uvim1006.tab:5543', 'uvim1006.tab:5605', 'uvim1006.tab:5667', 'uvim1006.tab:5729', 'uvim1006.tab:5791', 'uvim1006.tab:5853', 'uvim1006.tab:5915', 'uvim1006.tab:5977', 'uvim1006.tab:6039', 'uvim1006.tab:6101', 'uvim1006.tab:6163', 'uvim1006.tab:6225', 'uvim1006.tab:6287', 'uvim1006.tab:6349', 'uvim1006.tab:6411', 'uvim1006.tab:6473', 'uvim1006.tab:6535', 'uvim1006.tab:6597', 'uvim1006.tab:6659', 'uvim1006.tab:6721', 'uvim1006.tab:6783', 'uvim1006.tab:6845', 'uvim1006.tab:6907', 'uvim1006.tab:6969', 'uvim1006.tab:7031', 'uvim1006.tab:7093']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5236', 'uvim1006.tab:7155', 'uvim1006.tab:7217']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5236', 'uvim1006.tab:7155', 'uvim1006.tab:7217']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5240', 'uvim1006.tab:5241', 'uvim1006.tab:5242', 'uvim1006.tab:5243', 'uvim1006.tab:5244', 'uvim1006.tab:5358', 'uvim1006.tab:5420', 'uvim1006.tab:5482', 'uvim1006.tab:5544', 'uvim1006.tab:5606', 'uvim1006.tab:5668', 'uvim1006.tab:5730', 'uvim1006.tab:5792', 'uvim1006.tab:5854', 'uvim1006.tab:5916', 'uvim1006.tab:5978', 'uvim1006.tab:6040', 'uvim1006.tab:6102', 'uvim1006.tab:6164', 'uvim1006.tab:6226', 'uvim1006.tab:6288', 'uvim1006.tab:6350', 'uvim1006.tab:6412', 'uvim1006.tab:6474', 'uvim1006.tab:6536', 'uvim1006.tab:6598', 'uvim1006.tab:6660', 'uvim1006.tab:6722', 'uvim1006.tab:6784', 'uvim1006.tab:6846', 'uvim1006.tab:6908', 'uvim1006.tab:6970', 'uvim1006.tab:7032', 'uvim1006.tab:7094', 'uvim1006.tab:7156', 'uvim1006.tab:7218']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5240', 'uvim1006.tab:5241', 'uvim1006.tab:5242', 'uvim1006.tab:5243', 'uvim1006.tab:5244', 'uvim1006.tab:5358', 'uvim1006.tab:5420', 'uvim1006.tab:5482', 'uvim1006.tab:5544', 'uvim1006.tab:5606', 'uvim1006.tab:5668', 'uvim1006.tab:5730', 'uvim1006.tab:5792', 'uvim1006.tab:5854', 'uvim1006.tab:5916', 'uvim1006.tab:5978', 'uvim1006.tab:6040', 'uvim1006.tab:6102', 'uvim1006.tab:6164', 'uvim1006.tab:6226', 'uvim1006.tab:6288', 'uvim1006.tab:6350', 'uvim1006.tab:6412', 'uvim1006.tab:6474', 'uvim1006.tab:6536', 'uvim1006.tab:6598', 'uvim1006.tab:6660', 'uvim1006.tab:6722', 'uvim1006.tab:6784', 'uvim1006.tab:6846', 'uvim1006.tab:6908', 'uvim1006.tab:6970', 'uvim1006.tab:7032', 'uvim1006.tab:7094', 'uvim1006.tab:7156', 'uvim1006.tab:7218']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5240', 'uvim1006.tab:5242', 'uvim1006.tab:5243', 'uvim1006.tab:5244', 'uvim1006.tab:5358', 'uvim1006.tab:5420', 'uvim1006.tab:5482', 'uvim1006.tab:5544', 'uvim1006.tab:5606', 'uvim1006.tab:5668', 'uvim1006.tab:5730', 'uvim1006.tab:5792', 'uvim1006.tab:5854', 'uvim1006.tab:5916', 'uvim1006.tab:5978', 'uvim1006.tab:6040', 'uvim1006.tab:6102', 'uvim1006.tab:6164', 'uvim1006.tab:6226', 'uvim1006.tab:6288', 'uvim1006.tab:6350', 'uvim1006.tab:6412', 'uvim1006.tab:6474', 'uvim1006.tab:6536', 'uvim1006.tab:6598', 'uvim1006.tab:6660', 'uvim1006.tab:6722', 'uvim1006.tab:6784', 'uvim1006.tab:6846', 'uvim1006.tab:6908', 'uvim1006.tab:6970', 'uvim1006.tab:7032', 'uvim1006.tab:7094']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5240', 'uvim1006.tab:5242', 'uvim1006.tab:5243', 'uvim1006.tab:5244', 'uvim1006.tab:5358', 'uvim1006.tab:5420', 'uvim1006.tab:5482', 'uvim1006.tab:5544', 'uvim1006.tab:5606', 'uvim1006.tab:5668', 'uvim1006.tab:5730', 'uvim1006.tab:5792', 'uvim1006.tab:5854', 'uvim1006.tab:5916', 'uvim1006.tab:5978', 'uvim1006.tab:6040', 'uvim1006.tab:6102', 'uvim1006.tab:6164', 'uvim1006.tab:6226', 'uvim1006.tab:6288', 'uvim1006.tab:6350', 'uvim1006.tab:6412', 'uvim1006.tab:6474', 'uvim1006.tab:6536', 'uvim1006.tab:6598', 'uvim1006.tab:6660', 'uvim1006.tab:6722', 'uvim1006.tab:6784', 'uvim1006.tab:6846', 'uvim1006.tab:6908', 'uvim1006.tab:6970', 'uvim1006.tab:7032', 'uvim1006.tab:7094']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5241', 'uvim1006.tab:7156', 'uvim1006.tab:7218']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5241', 'uvim1006.tab:7156', 'uvim1006.tab:7218']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5245', 'uvim1006.tab:5246', 'uvim1006.tab:5247', 'uvim1006.tab:5248', 'uvim1006.tab:5249', 'uvim1006.tab:5359', 'uvim1006.tab:5421', 'uvim1006.tab:5483', 'uvim1006.tab:5545', 'uvim1006.tab:5607', 'uvim1006.tab:5669', 'uvim1006.tab:5731', 'uvim1006.tab:5793', 'uvim1006.tab:5855', 'uvim1006.tab:5917', 'uvim1006.tab:5979', 'uvim1006.tab:6041', 'uvim1006.tab:6103', 'uvim1006.tab:6165', 'uvim1006.tab:6227', 'uvim1006.tab:6289', 'uvim1006.tab:6351', 'uvim1006.tab:6413', 'uvim1006.tab:6475', 'uvim1006.tab:6537', 'uvim1006.tab:6599', 'uvim1006.tab:6661', 'uvim1006.tab:6723', 'uvim1006.tab:6785', 'uvim1006.tab:6847', 'uvim1006.tab:6909', 'uvim1006.tab:6971', 'uvim1006.tab:7033', 'uvim1006.tab:7095', 'uvim1006.tab:7157', 'uvim1006.tab:7219']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5245', 'uvim1006.tab:5246', 'uvim1006.tab:5247', 'uvim1006.tab:5248', 'uvim1006.tab:5249', 'uvim1006.tab:5359', 'uvim1006.tab:5421', 'uvim1006.tab:5483', 'uvim1006.tab:5545', 'uvim1006.tab:5607', 'uvim1006.tab:5669', 'uvim1006.tab:5731', 'uvim1006.tab:5793', 'uvim1006.tab:5855', 'uvim1006.tab:5917', 'uvim1006.tab:5979', 'uvim1006.tab:6041', 'uvim1006.tab:6103', 'uvim1006.tab:6165', 'uvim1006.tab:6227', 'uvim1006.tab:6289', 'uvim1006.tab:6351', 'uvim1006.tab:6413', 'uvim1006.tab:6475', 'uvim1006.tab:6537', 'uvim1006.tab:6599', 'uvim1006.tab:6661', 'uvim1006.tab:6723', 'uvim1006.tab:6785', 'uvim1006.tab:6847', 'uvim1006.tab:6909', 'uvim1006.tab:6971', 'uvim1006.tab:7033', 'uvim1006.tab:7095', 'uvim1006.tab:7157', 'uvim1006.tab:7219']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5245', 'uvim1006.tab:5247', 'uvim1006.tab:5248', 'uvim1006.tab:5249', 'uvim1006.tab:5359', 'uvim1006.tab:5421', 'uvim1006.tab:5483', 'uvim1006.tab:5545', 'uvim1006.tab:5607', 'uvim1006.tab:5669', 'uvim1006.tab:5731', 'uvim1006.tab:5793', 'uvim1006.tab:5855', 'uvim1006.tab:5917', 'uvim1006.tab:5979', 'uvim1006.tab:6041', 'uvim1006.tab:6103', 'uvim1006.tab:6165', 'uvim1006.tab:6227', 'uvim1006.tab:6289', 'uvim1006.tab:6351', 'uvim1006.tab:6413', 'uvim1006.tab:6475', 'uvim1006.tab:6537', 'uvim1006.tab:6599', 'uvim1006.tab:6661', 'uvim1006.tab:6723', 'uvim1006.tab:6785', 'uvim1006.tab:6847', 'uvim1006.tab:6909', 'uvim1006.tab:6971', 'uvim1006.tab:7033', 'uvim1006.tab:7095']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5245', 'uvim1006.tab:5247', 'uvim1006.tab:5248', 'uvim1006.tab:5249', 'uvim1006.tab:5359', 'uvim1006.tab:5421', 'uvim1006.tab:5483', 'uvim1006.tab:5545', 'uvim1006.tab:5607', 'uvim1006.tab:5669', 'uvim1006.tab:5731', 'uvim1006.tab:5793', 'uvim1006.tab:5855', 'uvim1006.tab:5917', 'uvim1006.tab:5979', 'uvim1006.tab:6041', 'uvim1006.tab:6103', 'uvim1006.tab:6165', 'uvim1006.tab:6227', 'uvim1006.tab:6289', 'uvim1006.tab:6351', 'uvim1006.tab:6413', 'uvim1006.tab:6475', 'uvim1006.tab:6537', 'uvim1006.tab:6599', 'uvim1006.tab:6661', 'uvim1006.tab:6723', 'uvim1006.tab:6785', 'uvim1006.tab:6847', 'uvim1006.tab:6909', 'uvim1006.tab:6971', 'uvim1006.tab:7033', 'uvim1006.tab:7095']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5246', 'uvim1006.tab:7157', 'uvim1006.tab:7219']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5246', 'uvim1006.tab:7157', 'uvim1006.tab:7219']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5250', 'uvim1006.tab:5251', 'uvim1006.tab:5252', 'uvim1006.tab:5253', 'uvim1006.tab:5254', 'uvim1006.tab:5360', 'uvim1006.tab:5422', 'uvim1006.tab:5484', 'uvim1006.tab:5546', 'uvim1006.tab:5608', 'uvim1006.tab:5670', 'uvim1006.tab:5732', 'uvim1006.tab:5794', 'uvim1006.tab:5856', 'uvim1006.tab:5918', 'uvim1006.tab:5980', 'uvim1006.tab:6042', 'uvim1006.tab:6104', 'uvim1006.tab:6166', 'uvim1006.tab:6228', 'uvim1006.tab:6290', 'uvim1006.tab:6352', 'uvim1006.tab:6414', 'uvim1006.tab:6476', 'uvim1006.tab:6538', 'uvim1006.tab:6600', 'uvim1006.tab:6662', 'uvim1006.tab:6724', 'uvim1006.tab:6786', 'uvim1006.tab:6848', 'uvim1006.tab:6910', 'uvim1006.tab:6972', 'uvim1006.tab:7034', 'uvim1006.tab:7096', 'uvim1006.tab:7158', 'uvim1006.tab:7220']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5250', 'uvim1006.tab:5251', 'uvim1006.tab:5252', 'uvim1006.tab:5253', 'uvim1006.tab:5254', 'uvim1006.tab:5360', 'uvim1006.tab:5422', 'uvim1006.tab:5484', 'uvim1006.tab:5546', 'uvim1006.tab:5608', 'uvim1006.tab:5670', 'uvim1006.tab:5732', 'uvim1006.tab:5794', 'uvim1006.tab:5856', 'uvim1006.tab:5918', 'uvim1006.tab:5980', 'uvim1006.tab:6042', 'uvim1006.tab:6104', 'uvim1006.tab:6166', 'uvim1006.tab:6228', 'uvim1006.tab:6290', 'uvim1006.tab:6352', 'uvim1006.tab:6414', 'uvim1006.tab:6476', 'uvim1006.tab:6538', 'uvim1006.tab:6600', 'uvim1006.tab:6662', 'uvim1006.tab:6724', 'uvim1006.tab:6786', 'uvim1006.tab:6848', 'uvim1006.tab:6910', 'uvim1006.tab:6972', 'uvim1006.tab:7034', 'uvim1006.tab:7096', 'uvim1006.tab:7158', 'uvim1006.tab:7220']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5250', 'uvim1006.tab:5252', 'uvim1006.tab:5253', 'uvim1006.tab:5254', 'uvim1006.tab:5360', 'uvim1006.tab:5422', 'uvim1006.tab:5484', 'uvim1006.tab:5546', 'uvim1006.tab:5608', 'uvim1006.tab:5670', 'uvim1006.tab:5732', 'uvim1006.tab:5794', 'uvim1006.tab:5856', 'uvim1006.tab:5918', 'uvim1006.tab:5980', 'uvim1006.tab:6042', 'uvim1006.tab:6104', 'uvim1006.tab:6166', 'uvim1006.tab:6228', 'uvim1006.tab:6290', 'uvim1006.tab:6352', 'uvim1006.tab:6414', 'uvim1006.tab:6476', 'uvim1006.tab:6538', 'uvim1006.tab:6600', 'uvim1006.tab:6662', 'uvim1006.tab:6724', 'uvim1006.tab:6786', 'uvim1006.tab:6848', 'uvim1006.tab:6910', 'uvim1006.tab:6972', 'uvim1006.tab:7034', 'uvim1006.tab:7096']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5250', 'uvim1006.tab:5252', 'uvim1006.tab:5253', 'uvim1006.tab:5254', 'uvim1006.tab:5360', 'uvim1006.tab:5422', 'uvim1006.tab:5484', 'uvim1006.tab:5546', 'uvim1006.tab:5608', 'uvim1006.tab:5670', 'uvim1006.tab:5732', 'uvim1006.tab:5794', 'uvim1006.tab:5856', 'uvim1006.tab:5918', 'uvim1006.tab:5980', 'uvim1006.tab:6042', 'uvim1006.tab:6104', 'uvim1006.tab:6166', 'uvim1006.tab:6228', 'uvim1006.tab:6290', 'uvim1006.tab:6352', 'uvim1006.tab:6414', 'uvim1006.tab:6476', 'uvim1006.tab:6538', 'uvim1006.tab:6600', 'uvim1006.tab:6662', 'uvim1006.tab:6724', 'uvim1006.tab:6786', 'uvim1006.tab:6848', 'uvim1006.tab:6910', 'uvim1006.tab:6972', 'uvim1006.tab:7034', 'uvim1006.tab:7096']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5251', 'uvim1006.tab:7158', 'uvim1006.tab:7220']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5251', 'uvim1006.tab:7158', 'uvim1006.tab:7220']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5255', 'uvim1006.tab:5256', 'uvim1006.tab:5257', 'uvim1006.tab:5258', 'uvim1006.tab:5259', 'uvim1006.tab:5361', 'uvim1006.tab:5423', 'uvim1006.tab:5485', 'uvim1006.tab:5547', 'uvim1006.tab:5609', 'uvim1006.tab:5671', 'uvim1006.tab:5733', 'uvim1006.tab:5795', 'uvim1006.tab:5857', 'uvim1006.tab:5919', 'uvim1006.tab:5981', 'uvim1006.tab:6043', 'uvim1006.tab:6105', 'uvim1006.tab:6167', 'uvim1006.tab:6229', 'uvim1006.tab:6291', 'uvim1006.tab:6353', 'uvim1006.tab:6415', 'uvim1006.tab:6477', 'uvim1006.tab:6539', 'uvim1006.tab:6601', 'uvim1006.tab:6663', 'uvim1006.tab:6725', 'uvim1006.tab:6787', 'uvim1006.tab:6849', 'uvim1006.tab:6911', 'uvim1006.tab:6973', 'uvim1006.tab:7035', 'uvim1006.tab:7097', 'uvim1006.tab:7159', 'uvim1006.tab:7221']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5255', 'uvim1006.tab:5256', 'uvim1006.tab:5257', 'uvim1006.tab:5258', 'uvim1006.tab:5259', 'uvim1006.tab:5361', 'uvim1006.tab:5423', 'uvim1006.tab:5485', 'uvim1006.tab:5547', 'uvim1006.tab:5609', 'uvim1006.tab:5671', 'uvim1006.tab:5733', 'uvim1006.tab:5795', 'uvim1006.tab:5857', 'uvim1006.tab:5919', 'uvim1006.tab:5981', 'uvim1006.tab:6043', 'uvim1006.tab:6105', 'uvim1006.tab:6167', 'uvim1006.tab:6229', 'uvim1006.tab:6291', 'uvim1006.tab:6353', 'uvim1006.tab:6415', 'uvim1006.tab:6477', 'uvim1006.tab:6539', 'uvim1006.tab:6601', 'uvim1006.tab:6663', 'uvim1006.tab:6725', 'uvim1006.tab:6787', 'uvim1006.tab:6849', 'uvim1006.tab:6911', 'uvim1006.tab:6973', 'uvim1006.tab:7035', 'uvim1006.tab:7097', 'uvim1006.tab:7159', 'uvim1006.tab:7221']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5255', 'uvim1006.tab:5257', 'uvim1006.tab:5258', 'uvim1006.tab:5259', 'uvim1006.tab:5361', 'uvim1006.tab:5423', 'uvim1006.tab:5485', 'uvim1006.tab:5547', 'uvim1006.tab:5609', 'uvim1006.tab:5671', 'uvim1006.tab:5733', 'uvim1006.tab:5795', 'uvim1006.tab:5857', 'uvim1006.tab:5919', 'uvim1006.tab:5981', 'uvim1006.tab:6043', 'uvim1006.tab:6105', 'uvim1006.tab:6167', 'uvim1006.tab:6229', 'uvim1006.tab:6291', 'uvim1006.tab:6353', 'uvim1006.tab:6415', 'uvim1006.tab:6477', 'uvim1006.tab:6539', 'uvim1006.tab:6601', 'uvim1006.tab:6663', 'uvim1006.tab:6725', 'uvim1006.tab:6787', 'uvim1006.tab:6849', 'uvim1006.tab:6911', 'uvim1006.tab:6973', 'uvim1006.tab:7035', 'uvim1006.tab:7097']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5255', 'uvim1006.tab:5257', 'uvim1006.tab:5258', 'uvim1006.tab:5259', 'uvim1006.tab:5361', 'uvim1006.tab:5423', 'uvim1006.tab:5485', 'uvim1006.tab:5547', 'uvim1006.tab:5609', 'uvim1006.tab:5671', 'uvim1006.tab:5733', 'uvim1006.tab:5795', 'uvim1006.tab:5857', 'uvim1006.tab:5919', 'uvim1006.tab:5981', 'uvim1006.tab:6043', 'uvim1006.tab:6105', 'uvim1006.tab:6167', 'uvim1006.tab:6229', 'uvim1006.tab:6291', 'uvim1006.tab:6353', 'uvim1006.tab:6415', 'uvim1006.tab:6477', 'uvim1006.tab:6539', 'uvim1006.tab:6601', 'uvim1006.tab:6663', 'uvim1006.tab:6725', 'uvim1006.tab:6787', 'uvim1006.tab:6849', 'uvim1006.tab:6911', 'uvim1006.tab:6973', 'uvim1006.tab:7035', 'uvim1006.tab:7097']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5256', 'uvim1006.tab:7159', 'uvim1006.tab:7221']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5256', 'uvim1006.tab:7159', 'uvim1006.tab:7221']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5260', 'uvim1006.tab:5261', 'uvim1006.tab:5262', 'uvim1006.tab:5263', 'uvim1006.tab:5264', 'uvim1006.tab:5362', 'uvim1006.tab:5424', 'uvim1006.tab:5486', 'uvim1006.tab:5548', 'uvim1006.tab:5610', 'uvim1006.tab:5672', 'uvim1006.tab:5734', 'uvim1006.tab:5796', 'uvim1006.tab:5858', 'uvim1006.tab:5920', 'uvim1006.tab:5982', 'uvim1006.tab:6044', 'uvim1006.tab:6106', 'uvim1006.tab:6168', 'uvim1006.tab:6230', 'uvim1006.tab:6292', 'uvim1006.tab:6354', 'uvim1006.tab:6416', 'uvim1006.tab:6478', 'uvim1006.tab:6540', 'uvim1006.tab:6602', 'uvim1006.tab:6664', 'uvim1006.tab:6726', 'uvim1006.tab:6788', 'uvim1006.tab:6850', 'uvim1006.tab:6912', 'uvim1006.tab:6974', 'uvim1006.tab:7036', 'uvim1006.tab:7098', 'uvim1006.tab:7160', 'uvim1006.tab:7222']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5260', 'uvim1006.tab:5261', 'uvim1006.tab:5262', 'uvim1006.tab:5263', 'uvim1006.tab:5264', 'uvim1006.tab:5362', 'uvim1006.tab:5424', 'uvim1006.tab:5486', 'uvim1006.tab:5548', 'uvim1006.tab:5610', 'uvim1006.tab:5672', 'uvim1006.tab:5734', 'uvim1006.tab:5796', 'uvim1006.tab:5858', 'uvim1006.tab:5920', 'uvim1006.tab:5982', 'uvim1006.tab:6044', 'uvim1006.tab:6106', 'uvim1006.tab:6168', 'uvim1006.tab:6230', 'uvim1006.tab:6292', 'uvim1006.tab:6354', 'uvim1006.tab:6416', 'uvim1006.tab:6478', 'uvim1006.tab:6540', 'uvim1006.tab:6602', 'uvim1006.tab:6664', 'uvim1006.tab:6726', 'uvim1006.tab:6788', 'uvim1006.tab:6850', 'uvim1006.tab:6912', 'uvim1006.tab:6974', 'uvim1006.tab:7036', 'uvim1006.tab:7098', 'uvim1006.tab:7160', 'uvim1006.tab:7222']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5260', 'uvim1006.tab:5262', 'uvim1006.tab:5263', 'uvim1006.tab:5264', 'uvim1006.tab:5362', 'uvim1006.tab:5424', 'uvim1006.tab:5486', 'uvim1006.tab:5548', 'uvim1006.tab:5610', 'uvim1006.tab:5672', 'uvim1006.tab:5734', 'uvim1006.tab:5796', 'uvim1006.tab:5858', 'uvim1006.tab:5920', 'uvim1006.tab:5982', 'uvim1006.tab:6044', 'uvim1006.tab:6106', 'uvim1006.tab:6168', 'uvim1006.tab:6230', 'uvim1006.tab:6292', 'uvim1006.tab:6354', 'uvim1006.tab:6416', 'uvim1006.tab:6478', 'uvim1006.tab:6540', 'uvim1006.tab:6602', 'uvim1006.tab:6664', 'uvim1006.tab:6726', 'uvim1006.tab:6788', 'uvim1006.tab:6850', 'uvim1006.tab:6912', 'uvim1006.tab:6974', 'uvim1006.tab:7036', 'uvim1006.tab:7098']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5260', 'uvim1006.tab:5262', 'uvim1006.tab:5263', 'uvim1006.tab:5264', 'uvim1006.tab:5362', 'uvim1006.tab:5424', 'uvim1006.tab:5486', 'uvim1006.tab:5548', 'uvim1006.tab:5610', 'uvim1006.tab:5672', 'uvim1006.tab:5734', 'uvim1006.tab:5796', 'uvim1006.tab:5858', 'uvim1006.tab:5920', 'uvim1006.tab:5982', 'uvim1006.tab:6044', 'uvim1006.tab:6106', 'uvim1006.tab:6168', 'uvim1006.tab:6230', 'uvim1006.tab:6292', 'uvim1006.tab:6354', 'uvim1006.tab:6416', 'uvim1006.tab:6478', 'uvim1006.tab:6540', 'uvim1006.tab:6602', 'uvim1006.tab:6664', 'uvim1006.tab:6726', 'uvim1006.tab:6788', 'uvim1006.tab:6850', 'uvim1006.tab:6912', 'uvim1006.tab:6974', 'uvim1006.tab:7036', 'uvim1006.tab:7098']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5261', 'uvim1006.tab:7160', 'uvim1006.tab:7222']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5261', 'uvim1006.tab:7160', 'uvim1006.tab:7222']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5265', 'uvim1006.tab:5266', 'uvim1006.tab:5267', 'uvim1006.tab:5268', 'uvim1006.tab:5269', 'uvim1006.tab:5363', 'uvim1006.tab:5425', 'uvim1006.tab:5487', 'uvim1006.tab:5549', 'uvim1006.tab:5611', 'uvim1006.tab:5673', 'uvim1006.tab:5735', 'uvim1006.tab:5797', 'uvim1006.tab:5859', 'uvim1006.tab:5921', 'uvim1006.tab:5983', 'uvim1006.tab:6045', 'uvim1006.tab:6107', 'uvim1006.tab:6169', 'uvim1006.tab:6231', 'uvim1006.tab:6293', 'uvim1006.tab:6355', 'uvim1006.tab:6417', 'uvim1006.tab:6479', 'uvim1006.tab:6541', 'uvim1006.tab:6603', 'uvim1006.tab:6665', 'uvim1006.tab:6727', 'uvim1006.tab:6789', 'uvim1006.tab:6851', 'uvim1006.tab:6913', 'uvim1006.tab:6975', 'uvim1006.tab:7037', 'uvim1006.tab:7099', 'uvim1006.tab:7161', 'uvim1006.tab:7223']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5265', 'uvim1006.tab:5266', 'uvim1006.tab:5267', 'uvim1006.tab:5268', 'uvim1006.tab:5269', 'uvim1006.tab:5363', 'uvim1006.tab:5425', 'uvim1006.tab:5487', 'uvim1006.tab:5549', 'uvim1006.tab:5611', 'uvim1006.tab:5673', 'uvim1006.tab:5735', 'uvim1006.tab:5797', 'uvim1006.tab:5859', 'uvim1006.tab:5921', 'uvim1006.tab:5983', 'uvim1006.tab:6045', 'uvim1006.tab:6107', 'uvim1006.tab:6169', 'uvim1006.tab:6231', 'uvim1006.tab:6293', 'uvim1006.tab:6355', 'uvim1006.tab:6417', 'uvim1006.tab:6479', 'uvim1006.tab:6541', 'uvim1006.tab:6603', 'uvim1006.tab:6665', 'uvim1006.tab:6727', 'uvim1006.tab:6789', 'uvim1006.tab:6851', 'uvim1006.tab:6913', 'uvim1006.tab:6975', 'uvim1006.tab:7037', 'uvim1006.tab:7099', 'uvim1006.tab:7161', 'uvim1006.tab:7223']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5265', 'uvim1006.tab:5267', 'uvim1006.tab:5268', 'uvim1006.tab:5269', 'uvim1006.tab:5363', 'uvim1006.tab:5425', 'uvim1006.tab:5487', 'uvim1006.tab:5549', 'uvim1006.tab:5611', 'uvim1006.tab:5673', 'uvim1006.tab:5735', 'uvim1006.tab:5797', 'uvim1006.tab:5859', 'uvim1006.tab:5921', 'uvim1006.tab:5983', 'uvim1006.tab:6045', 'uvim1006.tab:6107', 'uvim1006.tab:6169', 'uvim1006.tab:6231', 'uvim1006.tab:6293', 'uvim1006.tab:6355', 'uvim1006.tab:6417', 'uvim1006.tab:6479', 'uvim1006.tab:6541', 'uvim1006.tab:6603', 'uvim1006.tab:6665', 'uvim1006.tab:6727', 'uvim1006.tab:6789', 'uvim1006.tab:6851', 'uvim1006.tab:6913', 'uvim1006.tab:6975', 'uvim1006.tab:7037', 'uvim1006.tab:7099']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5265', 'uvim1006.tab:5267', 'uvim1006.tab:5268', 'uvim1006.tab:5269', 'uvim1006.tab:5363', 'uvim1006.tab:5425', 'uvim1006.tab:5487', 'uvim1006.tab:5549', 'uvim1006.tab:5611', 'uvim1006.tab:5673', 'uvim1006.tab:5735', 'uvim1006.tab:5797', 'uvim1006.tab:5859', 'uvim1006.tab:5921', 'uvim1006.tab:5983', 'uvim1006.tab:6045', 'uvim1006.tab:6107', 'uvim1006.tab:6169', 'uvim1006.tab:6231', 'uvim1006.tab:6293', 'uvim1006.tab:6355', 'uvim1006.tab:6417', 'uvim1006.tab:6479', 'uvim1006.tab:6541', 'uvim1006.tab:6603', 'uvim1006.tab:6665', 'uvim1006.tab:6727', 'uvim1006.tab:6789', 'uvim1006.tab:6851', 'uvim1006.tab:6913', 'uvim1006.tab:6975', 'uvim1006.tab:7037', 'uvim1006.tab:7099']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5266', 'uvim1006.tab:7161', 'uvim1006.tab:7223']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5266', 'uvim1006.tab:7161', 'uvim1006.tab:7223']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5270', 'uvim1006.tab:5271', 'uvim1006.tab:5272', 'uvim1006.tab:5273', 'uvim1006.tab:5274', 'uvim1006.tab:5364', 'uvim1006.tab:5426', 'uvim1006.tab:5488', 'uvim1006.tab:5550', 'uvim1006.tab:5612', 'uvim1006.tab:5674', 'uvim1006.tab:5736', 'uvim1006.tab:5798', 'uvim1006.tab:5860', 'uvim1006.tab:5922', 'uvim1006.tab:5984', 'uvim1006.tab:6046', 'uvim1006.tab:6108', 'uvim1006.tab:6170', 'uvim1006.tab:6232', 'uvim1006.tab:6294', 'uvim1006.tab:6356', 'uvim1006.tab:6418', 'uvim1006.tab:6480', 'uvim1006.tab:6542', 'uvim1006.tab:6604', 'uvim1006.tab:6666', 'uvim1006.tab:6728', 'uvim1006.tab:6790', 'uvim1006.tab:6852', 'uvim1006.tab:6914', 'uvim1006.tab:6976', 'uvim1006.tab:7038', 'uvim1006.tab:7100', 'uvim1006.tab:7162', 'uvim1006.tab:7224', 'uvim1006.tab:7256', 'uvim1006.tab:7257', 'uvim1006.tab:7258', 'uvim1006.tab:7259', 'uvim1006.tab:7260', 'uvim1006.tab:7261', 'uvim1006.tab:7262', 'uvim1006.tab:7263', 'uvim1006.tab:7264', 'uvim1006.tab:7265', 'uvim1006.tab:7266', 'uvim1006.tab:7267', 'uvim1006.tab:7268', 'uvim1006.tab:7269', 'uvim1006.tab:7270', 'uvim1006.tab:7271', 'uvim1006.tab:7272', 'uvim1006.tab:7273', 'uvim1006.tab:7274', 'uvim1006.tab:7275', 'uvim1006.tab:7276', 'uvim1006.tab:7277', 'uvim1006.tab:7278', 'uvim1006.tab:7279', 'uvim1006.tab:7280', 'uvim1006.tab:7281', 'uvim1006.tab:7282', 'uvim1006.tab:7283', 'uvim1006.tab:7284', 'uvim1006.tab:7285', 'uvim1006.tab:7286', 'uvim1006.tab:7287', 'uvim1006.tab:7288', 'uvim1006.tab:7289', 'uvim1006.tab:7290', 'uvim1006.tab:7291', 'uvim1006.tab:7292', 'uvim1006.tab:7293', 'uvim1006.tab:7294', 'uvim1006.tab:7295', 'uvim1006.tab:7296', 'uvim1006.tab:7297', 'uvim1006.tab:7298', 'uvim1006.tab:7299', 'uvim1006.tab:7300', 'uvim1006.tab:7301', 'uvim1006.tab:7302', 'uvim1006.tab:7303', 'uvim1006.tab:7304', 'uvim1006.tab:7305', 'uvim1006.tab:7306', 'uvim1006.tab:7307', 'uvim1006.tab:7308', 'uvim1006.tab:7309', 'uvim1006.tab:7310', 'uvim1006.tab:7311', 'uvim1006.tab:7312', 'uvim1006.tab:7313', 'uvim1006.tab:7314', 'uvim1006.tab:7315', 'uvim1006.tab:7316', 'uvim1006.tab:7317', 'uvim1006.tab:7318', 'uvim1006.tab:7319', 'uvim1006.tab:7320', 'uvim1006.tab:7321', 'uvim1006.tab:7322', 'uvim1006.tab:7323', 'uvim1006.tab:7324', 'uvim1006.tab:7325', 'uvim1006.tab:7326', 'uvim1006.tab:7327']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5270', 'uvim1006.tab:5271', 'uvim1006.tab:5272', 'uvim1006.tab:5273', 'uvim1006.tab:5274', 'uvim1006.tab:5364', 'uvim1006.tab:5426', 'uvim1006.tab:5488', 'uvim1006.tab:5550', 'uvim1006.tab:5612', 'uvim1006.tab:5674', 'uvim1006.tab:5736', 'uvim1006.tab:5798', 'uvim1006.tab:5860', 'uvim1006.tab:5922', 'uvim1006.tab:5984', 'uvim1006.tab:6046', 'uvim1006.tab:6108', 'uvim1006.tab:6170', 'uvim1006.tab:6232', 'uvim1006.tab:6294', 'uvim1006.tab:6356', 'uvim1006.tab:6418', 'uvim1006.tab:6480', 'uvim1006.tab:6542', 'uvim1006.tab:6604', 'uvim1006.tab:6666', 'uvim1006.tab:6728', 'uvim1006.tab:6790', 'uvim1006.tab:6852', 'uvim1006.tab:6914', 'uvim1006.tab:6976', 'uvim1006.tab:7038', 'uvim1006.tab:7100', 'uvim1006.tab:7162', 'uvim1006.tab:7224', 'uvim1006.tab:7256', 'uvim1006.tab:7257', 'uvim1006.tab:7258', 'uvim1006.tab:7259', 'uvim1006.tab:7260', 'uvim1006.tab:7261', 'uvim1006.tab:7262', 'uvim1006.tab:7263', 'uvim1006.tab:7264', 'uvim1006.tab:7265', 'uvim1006.tab:7266', 'uvim1006.tab:7267', 'uvim1006.tab:7268', 'uvim1006.tab:7269', 'uvim1006.tab:7270', 'uvim1006.tab:7271', 'uvim1006.tab:7272', 'uvim1006.tab:7273', 'uvim1006.tab:7274', 'uvim1006.tab:7275', 'uvim1006.tab:7276', 'uvim1006.tab:7277', 'uvim1006.tab:7278', 'uvim1006.tab:7279', 'uvim1006.tab:7280', 'uvim1006.tab:7281', 'uvim1006.tab:7282', 'uvim1006.tab:7283', 'uvim1006.tab:7284', 'uvim1006.tab:7285', 'uvim1006.tab:7286', 'uvim1006.tab:7287', 'uvim1006.tab:7288', 'uvim1006.tab:7289', 'uvim1006.tab:7290', 'uvim1006.tab:7291', 'uvim1006.tab:7292', 'uvim1006.tab:7293', 'uvim1006.tab:7294', 'uvim1006.tab:7295', 'uvim1006.tab:7296', 'uvim1006.tab:7297', 'uvim1006.tab:7298', 'uvim1006.tab:7299', 'uvim1006.tab:7300', 'uvim1006.tab:7301', 'uvim1006.tab:7302', 'uvim1006.tab:7303', 'uvim1006.tab:7304', 'uvim1006.tab:7305', 'uvim1006.tab:7306', 'uvim1006.tab:7307', 'uvim1006.tab:7308', 'uvim1006.tab:7309', 'uvim1006.tab:7310', 'uvim1006.tab:7311', 'uvim1006.tab:7312', 'uvim1006.tab:7313', 'uvim1006.tab:7314', 'uvim1006.tab:7315', 'uvim1006.tab:7316', 'uvim1006.tab:7317', 'uvim1006.tab:7318', 'uvim1006.tab:7319', 'uvim1006.tab:7320', 'uvim1006.tab:7321', 'uvim1006.tab:7322', 'uvim1006.tab:7323', 'uvim1006.tab:7324', 'uvim1006.tab:7325', 'uvim1006.tab:7326', 'uvim1006.tab:7327']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5270', 'uvim1006.tab:5272', 'uvim1006.tab:5273', 'uvim1006.tab:5274', 'uvim1006.tab:5364', 'uvim1006.tab:5426', 'uvim1006.tab:5488', 'uvim1006.tab:5550', 'uvim1006.tab:5612', 'uvim1006.tab:5674', 'uvim1006.tab:5736', 'uvim1006.tab:5798', 'uvim1006.tab:5860', 'uvim1006.tab:5922', 'uvim1006.tab:5984', 'uvim1006.tab:6046', 'uvim1006.tab:6108', 'uvim1006.tab:6170', 'uvim1006.tab:6232', 'uvim1006.tab:6294', 'uvim1006.tab:6356', 'uvim1006.tab:6418', 'uvim1006.tab:6480', 'uvim1006.tab:6542', 'uvim1006.tab:6604', 'uvim1006.tab:6666', 'uvim1006.tab:6728', 'uvim1006.tab:6790', 'uvim1006.tab:6852', 'uvim1006.tab:6914', 'uvim1006.tab:6976', 'uvim1006.tab:7038', 'uvim1006.tab:7100']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5270', 'uvim1006.tab:5272', 'uvim1006.tab:5273', 'uvim1006.tab:5274', 'uvim1006.tab:5364', 'uvim1006.tab:5426', 'uvim1006.tab:5488', 'uvim1006.tab:5550', 'uvim1006.tab:5612', 'uvim1006.tab:5674', 'uvim1006.tab:5736', 'uvim1006.tab:5798', 'uvim1006.tab:5860', 'uvim1006.tab:5922', 'uvim1006.tab:5984', 'uvim1006.tab:6046', 'uvim1006.tab:6108', 'uvim1006.tab:6170', 'uvim1006.tab:6232', 'uvim1006.tab:6294', 'uvim1006.tab:6356', 'uvim1006.tab:6418', 'uvim1006.tab:6480', 'uvim1006.tab:6542', 'uvim1006.tab:6604', 'uvim1006.tab:6666', 'uvim1006.tab:6728', 'uvim1006.tab:6790', 'uvim1006.tab:6852', 'uvim1006.tab:6914', 'uvim1006.tab:6976', 'uvim1006.tab:7038', 'uvim1006.tab:7100']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5271', 'uvim1006.tab:7162', 'uvim1006.tab:7224']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5271', 'uvim1006.tab:7162', 'uvim1006.tab:7224']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5275', 'uvim1006.tab:5276', 'uvim1006.tab:5277', 'uvim1006.tab:5278', 'uvim1006.tab:5279', 'uvim1006.tab:5365', 'uvim1006.tab:5427', 'uvim1006.tab:5489', 'uvim1006.tab:5551', 'uvim1006.tab:5613', 'uvim1006.tab:5675', 'uvim1006.tab:5737', 'uvim1006.tab:5799', 'uvim1006.tab:5861', 'uvim1006.tab:5923', 'uvim1006.tab:5985', 'uvim1006.tab:6047', 'uvim1006.tab:6109', 'uvim1006.tab:6171', 'uvim1006.tab:6233', 'uvim1006.tab:6295', 'uvim1006.tab:6357', 'uvim1006.tab:6419', 'uvim1006.tab:6481', 'uvim1006.tab:6543', 'uvim1006.tab:6605', 'uvim1006.tab:6667', 'uvim1006.tab:6729', 'uvim1006.tab:6791', 'uvim1006.tab:6853', 'uvim1006.tab:6915', 'uvim1006.tab:6977', 'uvim1006.tab:7039', 'uvim1006.tab:7101', 'uvim1006.tab:7163', 'uvim1006.tab:7225']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5275', 'uvim1006.tab:5276', 'uvim1006.tab:5277', 'uvim1006.tab:5278', 'uvim1006.tab:5279', 'uvim1006.tab:5365', 'uvim1006.tab:5427', 'uvim1006.tab:5489', 'uvim1006.tab:5551', 'uvim1006.tab:5613', 'uvim1006.tab:5675', 'uvim1006.tab:5737', 'uvim1006.tab:5799', 'uvim1006.tab:5861', 'uvim1006.tab:5923', 'uvim1006.tab:5985', 'uvim1006.tab:6047', 'uvim1006.tab:6109', 'uvim1006.tab:6171', 'uvim1006.tab:6233', 'uvim1006.tab:6295', 'uvim1006.tab:6357', 'uvim1006.tab:6419', 'uvim1006.tab:6481', 'uvim1006.tab:6543', 'uvim1006.tab:6605', 'uvim1006.tab:6667', 'uvim1006.tab:6729', 'uvim1006.tab:6791', 'uvim1006.tab:6853', 'uvim1006.tab:6915', 'uvim1006.tab:6977', 'uvim1006.tab:7039', 'uvim1006.tab:7101', 'uvim1006.tab:7163', 'uvim1006.tab:7225']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5275', 'uvim1006.tab:5277', 'uvim1006.tab:5278', 'uvim1006.tab:5279', 'uvim1006.tab:5365', 'uvim1006.tab:5427', 'uvim1006.tab:5489', 'uvim1006.tab:5551', 'uvim1006.tab:5613', 'uvim1006.tab:5675', 'uvim1006.tab:5737', 'uvim1006.tab:5799', 'uvim1006.tab:5861', 'uvim1006.tab:5923', 'uvim1006.tab:5985', 'uvim1006.tab:6047', 'uvim1006.tab:6109', 'uvim1006.tab:6171', 'uvim1006.tab:6233', 'uvim1006.tab:6295', 'uvim1006.tab:6357', 'uvim1006.tab:6419', 'uvim1006.tab:6481', 'uvim1006.tab:6543', 'uvim1006.tab:6605', 'uvim1006.tab:6667', 'uvim1006.tab:6729', 'uvim1006.tab:6791', 'uvim1006.tab:6853', 'uvim1006.tab:6915', 'uvim1006.tab:6977', 'uvim1006.tab:7039', 'uvim1006.tab:7101']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5275', 'uvim1006.tab:5277', 'uvim1006.tab:5278', 'uvim1006.tab:5279', 'uvim1006.tab:5365', 'uvim1006.tab:5427', 'uvim1006.tab:5489', 'uvim1006.tab:5551', 'uvim1006.tab:5613', 'uvim1006.tab:5675', 'uvim1006.tab:5737', 'uvim1006.tab:5799', 'uvim1006.tab:5861', 'uvim1006.tab:5923', 'uvim1006.tab:5985', 'uvim1006.tab:6047', 'uvim1006.tab:6109', 'uvim1006.tab:6171', 'uvim1006.tab:6233', 'uvim1006.tab:6295', 'uvim1006.tab:6357', 'uvim1006.tab:6419', 'uvim1006.tab:6481', 'uvim1006.tab:6543', 'uvim1006.tab:6605', 'uvim1006.tab:6667', 'uvim1006.tab:6729', 'uvim1006.tab:6791', 'uvim1006.tab:6853', 'uvim1006.tab:6915', 'uvim1006.tab:6977', 'uvim1006.tab:7039', 'uvim1006.tab:7101']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5276', 'uvim1006.tab:7163', 'uvim1006.tab:7225']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5276', 'uvim1006.tab:7163', 'uvim1006.tab:7225']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5280', 'uvim1006.tab:5281', 'uvim1006.tab:5282', 'uvim1006.tab:5283', 'uvim1006.tab:5284', 'uvim1006.tab:5366', 'uvim1006.tab:5428', 'uvim1006.tab:5490', 'uvim1006.tab:5552', 'uvim1006.tab:5614', 'uvim1006.tab:5676', 'uvim1006.tab:5738', 'uvim1006.tab:5800', 'uvim1006.tab:5862', 'uvim1006.tab:5924', 'uvim1006.tab:5986', 'uvim1006.tab:6048', 'uvim1006.tab:6110', 'uvim1006.tab:6172', 'uvim1006.tab:6234', 'uvim1006.tab:6296', 'uvim1006.tab:6358', 'uvim1006.tab:6420', 'uvim1006.tab:6482', 'uvim1006.tab:6544', 'uvim1006.tab:6606', 'uvim1006.tab:6668', 'uvim1006.tab:6730', 'uvim1006.tab:6792', 'uvim1006.tab:6854', 'uvim1006.tab:6916', 'uvim1006.tab:6978', 'uvim1006.tab:7040', 'uvim1006.tab:7102', 'uvim1006.tab:7164', 'uvim1006.tab:7226']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5280', 'uvim1006.tab:5281', 'uvim1006.tab:5282', 'uvim1006.tab:5283', 'uvim1006.tab:5284', 'uvim1006.tab:5366', 'uvim1006.tab:5428', 'uvim1006.tab:5490', 'uvim1006.tab:5552', 'uvim1006.tab:5614', 'uvim1006.tab:5676', 'uvim1006.tab:5738', 'uvim1006.tab:5800', 'uvim1006.tab:5862', 'uvim1006.tab:5924', 'uvim1006.tab:5986', 'uvim1006.tab:6048', 'uvim1006.tab:6110', 'uvim1006.tab:6172', 'uvim1006.tab:6234', 'uvim1006.tab:6296', 'uvim1006.tab:6358', 'uvim1006.tab:6420', 'uvim1006.tab:6482', 'uvim1006.tab:6544', 'uvim1006.tab:6606', 'uvim1006.tab:6668', 'uvim1006.tab:6730', 'uvim1006.tab:6792', 'uvim1006.tab:6854', 'uvim1006.tab:6916', 'uvim1006.tab:6978', 'uvim1006.tab:7040', 'uvim1006.tab:7102', 'uvim1006.tab:7164', 'uvim1006.tab:7226']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5280', 'uvim1006.tab:5282', 'uvim1006.tab:5283', 'uvim1006.tab:5284', 'uvim1006.tab:5366', 'uvim1006.tab:5428', 'uvim1006.tab:5490', 'uvim1006.tab:5552', 'uvim1006.tab:5614', 'uvim1006.tab:5676', 'uvim1006.tab:5738', 'uvim1006.tab:5800', 'uvim1006.tab:5862', 'uvim1006.tab:5924', 'uvim1006.tab:5986', 'uvim1006.tab:6048', 'uvim1006.tab:6110', 'uvim1006.tab:6172', 'uvim1006.tab:6234', 'uvim1006.tab:6296', 'uvim1006.tab:6358', 'uvim1006.tab:6420', 'uvim1006.tab:6482', 'uvim1006.tab:6544', 'uvim1006.tab:6606', 'uvim1006.tab:6668', 'uvim1006.tab:6730', 'uvim1006.tab:6792', 'uvim1006.tab:6854', 'uvim1006.tab:6916', 'uvim1006.tab:6978', 'uvim1006.tab:7040', 'uvim1006.tab:7102']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5280', 'uvim1006.tab:5282', 'uvim1006.tab:5283', 'uvim1006.tab:5284', 'uvim1006.tab:5366', 'uvim1006.tab:5428', 'uvim1006.tab:5490', 'uvim1006.tab:5552', 'uvim1006.tab:5614', 'uvim1006.tab:5676', 'uvim1006.tab:5738', 'uvim1006.tab:5800', 'uvim1006.tab:5862', 'uvim1006.tab:5924', 'uvim1006.tab:5986', 'uvim1006.tab:6048', 'uvim1006.tab:6110', 'uvim1006.tab:6172', 'uvim1006.tab:6234', 'uvim1006.tab:6296', 'uvim1006.tab:6358', 'uvim1006.tab:6420', 'uvim1006.tab:6482', 'uvim1006.tab:6544', 'uvim1006.tab:6606', 'uvim1006.tab:6668', 'uvim1006.tab:6730', 'uvim1006.tab:6792', 'uvim1006.tab:6854', 'uvim1006.tab:6916', 'uvim1006.tab:6978', 'uvim1006.tab:7040', 'uvim1006.tab:7102']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5281', 'uvim1006.tab:7164', 'uvim1006.tab:7226']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5281', 'uvim1006.tab:7164', 'uvim1006.tab:7226']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5285', 'uvim1006.tab:5286', 'uvim1006.tab:5287', 'uvim1006.tab:5288', 'uvim1006.tab:5289', 'uvim1006.tab:5367', 'uvim1006.tab:5429', 'uvim1006.tab:5491', 'uvim1006.tab:5553', 'uvim1006.tab:5615', 'uvim1006.tab:5677', 'uvim1006.tab:5739', 'uvim1006.tab:5801', 'uvim1006.tab:5863', 'uvim1006.tab:5925', 'uvim1006.tab:5987', 'uvim1006.tab:6049', 'uvim1006.tab:6111', 'uvim1006.tab:6173', 'uvim1006.tab:6235', 'uvim1006.tab:6297', 'uvim1006.tab:6359', 'uvim1006.tab:6421', 'uvim1006.tab:6483', 'uvim1006.tab:6545', 'uvim1006.tab:6607', 'uvim1006.tab:6669', 'uvim1006.tab:6731', 'uvim1006.tab:6793', 'uvim1006.tab:6855', 'uvim1006.tab:6917', 'uvim1006.tab:6979', 'uvim1006.tab:7041', 'uvim1006.tab:7103', 'uvim1006.tab:7165', 'uvim1006.tab:7227']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5285', 'uvim1006.tab:5286', 'uvim1006.tab:5287', 'uvim1006.tab:5288', 'uvim1006.tab:5289', 'uvim1006.tab:5367', 'uvim1006.tab:5429', 'uvim1006.tab:5491', 'uvim1006.tab:5553', 'uvim1006.tab:5615', 'uvim1006.tab:5677', 'uvim1006.tab:5739', 'uvim1006.tab:5801', 'uvim1006.tab:5863', 'uvim1006.tab:5925', 'uvim1006.tab:5987', 'uvim1006.tab:6049', 'uvim1006.tab:6111', 'uvim1006.tab:6173', 'uvim1006.tab:6235', 'uvim1006.tab:6297', 'uvim1006.tab:6359', 'uvim1006.tab:6421', 'uvim1006.tab:6483', 'uvim1006.tab:6545', 'uvim1006.tab:6607', 'uvim1006.tab:6669', 'uvim1006.tab:6731', 'uvim1006.tab:6793', 'uvim1006.tab:6855', 'uvim1006.tab:6917', 'uvim1006.tab:6979', 'uvim1006.tab:7041', 'uvim1006.tab:7103', 'uvim1006.tab:7165', 'uvim1006.tab:7227']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5285', 'uvim1006.tab:5287', 'uvim1006.tab:5288', 'uvim1006.tab:5289', 'uvim1006.tab:5367', 'uvim1006.tab:5429', 'uvim1006.tab:5491', 'uvim1006.tab:5553', 'uvim1006.tab:5615', 'uvim1006.tab:5677', 'uvim1006.tab:5739', 'uvim1006.tab:5801', 'uvim1006.tab:5863', 'uvim1006.tab:5925', 'uvim1006.tab:5987', 'uvim1006.tab:6049', 'uvim1006.tab:6111', 'uvim1006.tab:6173', 'uvim1006.tab:6235', 'uvim1006.tab:6297', 'uvim1006.tab:6359', 'uvim1006.tab:6421', 'uvim1006.tab:6483', 'uvim1006.tab:6545', 'uvim1006.tab:6607', 'uvim1006.tab:6669', 'uvim1006.tab:6731', 'uvim1006.tab:6793', 'uvim1006.tab:6855', 'uvim1006.tab:6917', 'uvim1006.tab:6979', 'uvim1006.tab:7041', 'uvim1006.tab:7103']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5285', 'uvim1006.tab:5287', 'uvim1006.tab:5288', 'uvim1006.tab:5289', 'uvim1006.tab:5367', 'uvim1006.tab:5429', 'uvim1006.tab:5491', 'uvim1006.tab:5553', 'uvim1006.tab:5615', 'uvim1006.tab:5677', 'uvim1006.tab:5739', 'uvim1006.tab:5801', 'uvim1006.tab:5863', 'uvim1006.tab:5925', 'uvim1006.tab:5987', 'uvim1006.tab:6049', 'uvim1006.tab:6111', 'uvim1006.tab:6173', 'uvim1006.tab:6235', 'uvim1006.tab:6297', 'uvim1006.tab:6359', 'uvim1006.tab:6421', 'uvim1006.tab:6483', 'uvim1006.tab:6545', 'uvim1006.tab:6607', 'uvim1006.tab:6669', 'uvim1006.tab:6731', 'uvim1006.tab:6793', 'uvim1006.tab:6855', 'uvim1006.tab:6917', 'uvim1006.tab:6979', 'uvim1006.tab:7041', 'uvim1006.tab:7103']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5286', 'uvim1006.tab:7165', 'uvim1006.tab:7227']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5286', 'uvim1006.tab:7165', 'uvim1006.tab:7227']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5290', 'uvim1006.tab:5291', 'uvim1006.tab:5292', 'uvim1006.tab:5293', 'uvim1006.tab:5294', 'uvim1006.tab:5368', 'uvim1006.tab:5430', 'uvim1006.tab:5492', 'uvim1006.tab:5554', 'uvim1006.tab:5616', 'uvim1006.tab:5678', 'uvim1006.tab:5740', 'uvim1006.tab:5802', 'uvim1006.tab:5864', 'uvim1006.tab:5926', 'uvim1006.tab:5988', 'uvim1006.tab:6050', 'uvim1006.tab:6112', 'uvim1006.tab:6174', 'uvim1006.tab:6236', 'uvim1006.tab:6298', 'uvim1006.tab:6360', 'uvim1006.tab:6422', 'uvim1006.tab:6484', 'uvim1006.tab:6546', 'uvim1006.tab:6608', 'uvim1006.tab:6670', 'uvim1006.tab:6732', 'uvim1006.tab:6794', 'uvim1006.tab:6856', 'uvim1006.tab:6918', 'uvim1006.tab:6980', 'uvim1006.tab:7042', 'uvim1006.tab:7104', 'uvim1006.tab:7166', 'uvim1006.tab:7228']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5290', 'uvim1006.tab:5291', 'uvim1006.tab:5292', 'uvim1006.tab:5293', 'uvim1006.tab:5294', 'uvim1006.tab:5368', 'uvim1006.tab:5430', 'uvim1006.tab:5492', 'uvim1006.tab:5554', 'uvim1006.tab:5616', 'uvim1006.tab:5678', 'uvim1006.tab:5740', 'uvim1006.tab:5802', 'uvim1006.tab:5864', 'uvim1006.tab:5926', 'uvim1006.tab:5988', 'uvim1006.tab:6050', 'uvim1006.tab:6112', 'uvim1006.tab:6174', 'uvim1006.tab:6236', 'uvim1006.tab:6298', 'uvim1006.tab:6360', 'uvim1006.tab:6422', 'uvim1006.tab:6484', 'uvim1006.tab:6546', 'uvim1006.tab:6608', 'uvim1006.tab:6670', 'uvim1006.tab:6732', 'uvim1006.tab:6794', 'uvim1006.tab:6856', 'uvim1006.tab:6918', 'uvim1006.tab:6980', 'uvim1006.tab:7042', 'uvim1006.tab:7104', 'uvim1006.tab:7166', 'uvim1006.tab:7228']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5290', 'uvim1006.tab:5292', 'uvim1006.tab:5293', 'uvim1006.tab:5294', 'uvim1006.tab:5368', 'uvim1006.tab:5430', 'uvim1006.tab:5492', 'uvim1006.tab:5554', 'uvim1006.tab:5616', 'uvim1006.tab:5678', 'uvim1006.tab:5740', 'uvim1006.tab:5802', 'uvim1006.tab:5864', 'uvim1006.tab:5926', 'uvim1006.tab:5988', 'uvim1006.tab:6050', 'uvim1006.tab:6112', 'uvim1006.tab:6174', 'uvim1006.tab:6236', 'uvim1006.tab:6298', 'uvim1006.tab:6360', 'uvim1006.tab:6422', 'uvim1006.tab:6484', 'uvim1006.tab:6546', 'uvim1006.tab:6608', 'uvim1006.tab:6670', 'uvim1006.tab:6732', 'uvim1006.tab:6794', 'uvim1006.tab:6856', 'uvim1006.tab:6918', 'uvim1006.tab:6980', 'uvim1006.tab:7042', 'uvim1006.tab:7104']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5290', 'uvim1006.tab:5292', 'uvim1006.tab:5293', 'uvim1006.tab:5294', 'uvim1006.tab:5368', 'uvim1006.tab:5430', 'uvim1006.tab:5492', 'uvim1006.tab:5554', 'uvim1006.tab:5616', 'uvim1006.tab:5678', 'uvim1006.tab:5740', 'uvim1006.tab:5802', 'uvim1006.tab:5864', 'uvim1006.tab:5926', 'uvim1006.tab:5988', 'uvim1006.tab:6050', 'uvim1006.tab:6112', 'uvim1006.tab:6174', 'uvim1006.tab:6236', 'uvim1006.tab:6298', 'uvim1006.tab:6360', 'uvim1006.tab:6422', 'uvim1006.tab:6484', 'uvim1006.tab:6546', 'uvim1006.tab:6608', 'uvim1006.tab:6670', 'uvim1006.tab:6732', 'uvim1006.tab:6794', 'uvim1006.tab:6856', 'uvim1006.tab:6918', 'uvim1006.tab:6980', 'uvim1006.tab:7042', 'uvim1006.tab:7104']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5291', 'uvim1006.tab:7166', 'uvim1006.tab:7228']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5291', 'uvim1006.tab:7166', 'uvim1006.tab:7228']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5295', 'uvim1006.tab:5296', 'uvim1006.tab:5297', 'uvim1006.tab:5298', 'uvim1006.tab:5299', 'uvim1006.tab:5369', 'uvim1006.tab:5431', 'uvim1006.tab:5493', 'uvim1006.tab:5555', 'uvim1006.tab:5617', 'uvim1006.tab:5679', 'uvim1006.tab:5741', 'uvim1006.tab:5803', 'uvim1006.tab:5865', 'uvim1006.tab:5927', 'uvim1006.tab:5989', 'uvim1006.tab:6051', 'uvim1006.tab:6113', 'uvim1006.tab:6175', 'uvim1006.tab:6237', 'uvim1006.tab:6299', 'uvim1006.tab:6361', 'uvim1006.tab:6423', 'uvim1006.tab:6485', 'uvim1006.tab:6547', 'uvim1006.tab:6609', 'uvim1006.tab:6671', 'uvim1006.tab:6733', 'uvim1006.tab:6795', 'uvim1006.tab:6857', 'uvim1006.tab:6919', 'uvim1006.tab:6981', 'uvim1006.tab:7043', 'uvim1006.tab:7105', 'uvim1006.tab:7167', 'uvim1006.tab:7229']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5295', 'uvim1006.tab:5296', 'uvim1006.tab:5297', 'uvim1006.tab:5298', 'uvim1006.tab:5299', 'uvim1006.tab:5369', 'uvim1006.tab:5431', 'uvim1006.tab:5493', 'uvim1006.tab:5555', 'uvim1006.tab:5617', 'uvim1006.tab:5679', 'uvim1006.tab:5741', 'uvim1006.tab:5803', 'uvim1006.tab:5865', 'uvim1006.tab:5927', 'uvim1006.tab:5989', 'uvim1006.tab:6051', 'uvim1006.tab:6113', 'uvim1006.tab:6175', 'uvim1006.tab:6237', 'uvim1006.tab:6299', 'uvim1006.tab:6361', 'uvim1006.tab:6423', 'uvim1006.tab:6485', 'uvim1006.tab:6547', 'uvim1006.tab:6609', 'uvim1006.tab:6671', 'uvim1006.tab:6733', 'uvim1006.tab:6795', 'uvim1006.tab:6857', 'uvim1006.tab:6919', 'uvim1006.tab:6981', 'uvim1006.tab:7043', 'uvim1006.tab:7105', 'uvim1006.tab:7167', 'uvim1006.tab:7229']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5295', 'uvim1006.tab:5297', 'uvim1006.tab:5298', 'uvim1006.tab:5299', 'uvim1006.tab:5369', 'uvim1006.tab:5431', 'uvim1006.tab:5493', 'uvim1006.tab:5555', 'uvim1006.tab:5617', 'uvim1006.tab:5679', 'uvim1006.tab:5741', 'uvim1006.tab:5803', 'uvim1006.tab:5865', 'uvim1006.tab:5927', 'uvim1006.tab:5989', 'uvim1006.tab:6051', 'uvim1006.tab:6113', 'uvim1006.tab:6175', 'uvim1006.tab:6237', 'uvim1006.tab:6299', 'uvim1006.tab:6361', 'uvim1006.tab:6423', 'uvim1006.tab:6485', 'uvim1006.tab:6547', 'uvim1006.tab:6609', 'uvim1006.tab:6671', 'uvim1006.tab:6733', 'uvim1006.tab:6795', 'uvim1006.tab:6857', 'uvim1006.tab:6919', 'uvim1006.tab:6981', 'uvim1006.tab:7043', 'uvim1006.tab:7105']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5295', 'uvim1006.tab:5297', 'uvim1006.tab:5298', 'uvim1006.tab:5299', 'uvim1006.tab:5369', 'uvim1006.tab:5431', 'uvim1006.tab:5493', 'uvim1006.tab:5555', 'uvim1006.tab:5617', 'uvim1006.tab:5679', 'uvim1006.tab:5741', 'uvim1006.tab:5803', 'uvim1006.tab:5865', 'uvim1006.tab:5927', 'uvim1006.tab:5989', 'uvim1006.tab:6051', 'uvim1006.tab:6113', 'uvim1006.tab:6175', 'uvim1006.tab:6237', 'uvim1006.tab:6299', 'uvim1006.tab:6361', 'uvim1006.tab:6423', 'uvim1006.tab:6485', 'uvim1006.tab:6547', 'uvim1006.tab:6609', 'uvim1006.tab:6671', 'uvim1006.tab:6733', 'uvim1006.tab:6795', 'uvim1006.tab:6857', 'uvim1006.tab:6919', 'uvim1006.tab:6981', 'uvim1006.tab:7043', 'uvim1006.tab:7105']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5296', 'uvim1006.tab:7167', 'uvim1006.tab:7229']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5296', 'uvim1006.tab:7167', 'uvim1006.tab:7229']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5300', 'uvim1006.tab:5301', 'uvim1006.tab:5302', 'uvim1006.tab:5303', 'uvim1006.tab:5304', 'uvim1006.tab:5370', 'uvim1006.tab:5432', 'uvim1006.tab:5494', 'uvim1006.tab:5556', 'uvim1006.tab:5618', 'uvim1006.tab:5680', 'uvim1006.tab:5742', 'uvim1006.tab:5804', 'uvim1006.tab:5866', 'uvim1006.tab:5928', 'uvim1006.tab:5990', 'uvim1006.tab:6052', 'uvim1006.tab:6114', 'uvim1006.tab:6176', 'uvim1006.tab:6238', 'uvim1006.tab:6300', 'uvim1006.tab:6362', 'uvim1006.tab:6424', 'uvim1006.tab:6486', 'uvim1006.tab:6548', 'uvim1006.tab:6610', 'uvim1006.tab:6672', 'uvim1006.tab:6734', 'uvim1006.tab:6796', 'uvim1006.tab:6858', 'uvim1006.tab:6920', 'uvim1006.tab:6982', 'uvim1006.tab:7044', 'uvim1006.tab:7106', 'uvim1006.tab:7168', 'uvim1006.tab:7230']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5300', 'uvim1006.tab:5301', 'uvim1006.tab:5302', 'uvim1006.tab:5303', 'uvim1006.tab:5304', 'uvim1006.tab:5370', 'uvim1006.tab:5432', 'uvim1006.tab:5494', 'uvim1006.tab:5556', 'uvim1006.tab:5618', 'uvim1006.tab:5680', 'uvim1006.tab:5742', 'uvim1006.tab:5804', 'uvim1006.tab:5866', 'uvim1006.tab:5928', 'uvim1006.tab:5990', 'uvim1006.tab:6052', 'uvim1006.tab:6114', 'uvim1006.tab:6176', 'uvim1006.tab:6238', 'uvim1006.tab:6300', 'uvim1006.tab:6362', 'uvim1006.tab:6424', 'uvim1006.tab:6486', 'uvim1006.tab:6548', 'uvim1006.tab:6610', 'uvim1006.tab:6672', 'uvim1006.tab:6734', 'uvim1006.tab:6796', 'uvim1006.tab:6858', 'uvim1006.tab:6920', 'uvim1006.tab:6982', 'uvim1006.tab:7044', 'uvim1006.tab:7106', 'uvim1006.tab:7168', 'uvim1006.tab:7230']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5300', 'uvim1006.tab:5302', 'uvim1006.tab:5303', 'uvim1006.tab:5304', 'uvim1006.tab:5370', 'uvim1006.tab:5432', 'uvim1006.tab:5494', 'uvim1006.tab:5556', 'uvim1006.tab:5618', 'uvim1006.tab:5680', 'uvim1006.tab:5742', 'uvim1006.tab:5804', 'uvim1006.tab:5866', 'uvim1006.tab:5928', 'uvim1006.tab:5990', 'uvim1006.tab:6052', 'uvim1006.tab:6114', 'uvim1006.tab:6176', 'uvim1006.tab:6238', 'uvim1006.tab:6300', 'uvim1006.tab:6362', 'uvim1006.tab:6424', 'uvim1006.tab:6486', 'uvim1006.tab:6548', 'uvim1006.tab:6610', 'uvim1006.tab:6672', 'uvim1006.tab:6734', 'uvim1006.tab:6796', 'uvim1006.tab:6858', 'uvim1006.tab:6920', 'uvim1006.tab:6982', 'uvim1006.tab:7044', 'uvim1006.tab:7106']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5300', 'uvim1006.tab:5302', 'uvim1006.tab:5303', 'uvim1006.tab:5304', 'uvim1006.tab:5370', 'uvim1006.tab:5432', 'uvim1006.tab:5494', 'uvim1006.tab:5556', 'uvim1006.tab:5618', 'uvim1006.tab:5680', 'uvim1006.tab:5742', 'uvim1006.tab:5804', 'uvim1006.tab:5866', 'uvim1006.tab:5928', 'uvim1006.tab:5990', 'uvim1006.tab:6052', 'uvim1006.tab:6114', 'uvim1006.tab:6176', 'uvim1006.tab:6238', 'uvim1006.tab:6300', 'uvim1006.tab:6362', 'uvim1006.tab:6424', 'uvim1006.tab:6486', 'uvim1006.tab:6548', 'uvim1006.tab:6610', 'uvim1006.tab:6672', 'uvim1006.tab:6734', 'uvim1006.tab:6796', 'uvim1006.tab:6858', 'uvim1006.tab:6920', 'uvim1006.tab:6982', 'uvim1006.tab:7044', 'uvim1006.tab:7106']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5301', 'uvim1006.tab:7168', 'uvim1006.tab:7230']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5301', 'uvim1006.tab:7168', 'uvim1006.tab:7230']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5305', 'uvim1006.tab:5306', 'uvim1006.tab:5307', 'uvim1006.tab:5308', 'uvim1006.tab:5309', 'uvim1006.tab:5371', 'uvim1006.tab:5433', 'uvim1006.tab:5495', 'uvim1006.tab:5557', 'uvim1006.tab:5619', 'uvim1006.tab:5681', 'uvim1006.tab:5743', 'uvim1006.tab:5805', 'uvim1006.tab:5867', 'uvim1006.tab:5929', 'uvim1006.tab:5991', 'uvim1006.tab:6053', 'uvim1006.tab:6115', 'uvim1006.tab:6177', 'uvim1006.tab:6239', 'uvim1006.tab:6301', 'uvim1006.tab:6363', 'uvim1006.tab:6425', 'uvim1006.tab:6487', 'uvim1006.tab:6549', 'uvim1006.tab:6611', 'uvim1006.tab:6673', 'uvim1006.tab:6735', 'uvim1006.tab:6797', 'uvim1006.tab:6859', 'uvim1006.tab:6921', 'uvim1006.tab:6983', 'uvim1006.tab:7045', 'uvim1006.tab:7107', 'uvim1006.tab:7169', 'uvim1006.tab:7231']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim1006.tab:5305', 'uvim1006.tab:5306', 'uvim1006.tab:5307', 'uvim1006.tab:5308', 'uvim1006.tab:5309', 'uvim1006.tab:5371', 'uvim1006.tab:5433', 'uvim1006.tab:5495', 'uvim1006.tab:5557', 'uvim1006.tab:5619', 'uvim1006.tab:5681', 'uvim1006.tab:5743', 'uvim1006.tab:5805', 'uvim1006.tab:5867', 'uvim1006.tab:5929', 'uvim1006.tab:5991', 'uvim1006.tab:6053', 'uvim1006.tab:6115', 'uvim1006.tab:6177', 'uvim1006.tab:6239', 'uvim1006.tab:6301', 'uvim1006.tab:6363', 'uvim1006.tab:6425', 'uvim1006.tab:6487', 'uvim1006.tab:6549', 'uvim1006.tab:6611', 'uvim1006.tab:6673', 'uvim1006.tab:6735', 'uvim1006.tab:6797', 'uvim1006.tab:6859', 'uvim1006.tab:6921', 'uvim1006.tab:6983', 'uvim1006.tab:7045', 'uvim1006.tab:7107', 'uvim1006.tab:7169', 'uvim1006.tab:7231']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5305', 'uvim1006.tab:5307', 'uvim1006.tab:5308', 'uvim1006.tab:5309', 'uvim1006.tab:5371', 'uvim1006.tab:5433', 'uvim1006.tab:5495', 'uvim1006.tab:5557', 'uvim1006.tab:5619', 'uvim1006.tab:5681', 'uvim1006.tab:5743', 'uvim1006.tab:5805', 'uvim1006.tab:5867', 'uvim1006.tab:5929', 'uvim1006.tab:5991', 'uvim1006.tab:6053', 'uvim1006.tab:6115', 'uvim1006.tab:6177', 'uvim1006.tab:6239', 'uvim1006.tab:6301', 'uvim1006.tab:6363', 'uvim1006.tab:6425', 'uvim1006.tab:6487', 'uvim1006.tab:6549', 'uvim1006.tab:6611', 'uvim1006.tab:6673', 'uvim1006.tab:6735', 'uvim1006.tab:6797', 'uvim1006.tab:6859', 'uvim1006.tab:6921', 'uvim1006.tab:6983', 'uvim1006.tab:7045', 'uvim1006.tab:7107']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5305', 'uvim1006.tab:5307', 'uvim1006.tab:5308', 'uvim1006.tab:5309', 'uvim1006.tab:5371', 'uvim1006.tab:5433', 'uvim1006.tab:5495', 'uvim1006.tab:5557', 'uvim1006.tab:5619', 'uvim1006.tab:5681', 'uvim1006.tab:5743', 'uvim1006.tab:5805', 'uvim1006.tab:5867', 'uvim1006.tab:5929', 'uvim1006.tab:5991', 'uvim1006.tab:6053', 'uvim1006.tab:6115', 'uvim1006.tab:6177', 'uvim1006.tab:6239', 'uvim1006.tab:6301', 'uvim1006.tab:6363', 'uvim1006.tab:6425', 'uvim1006.tab:6487', 'uvim1006.tab:6549', 'uvim1006.tab:6611', 'uvim1006.tab:6673', 'uvim1006.tab:6735', 'uvim1006.tab:6797', 'uvim1006.tab:6859', 'uvim1006.tab:6921', 'uvim1006.tab:6983', 'uvim1006.tab:7045', 'uvim1006.tab:7107']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5306', 'uvim1006.tab:7169', 'uvim1006.tab:7231']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim1006.tab:5306', 'uvim1006.tab:7169', 'uvim1006.tab:7231']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2233(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7232"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7232"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2234(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2235(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7234"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase191(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7234"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2236(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase191(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7235"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase192(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7235"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2237(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase192(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7236"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase193(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7236"
        self.setglobal(__file__)
        self.runpy()
class countrateCase193(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7237"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase194(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7237"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2239(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8720,0.0,4.2)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase194(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7238"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase195(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7238"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2240(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8200,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase195(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase196(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2241(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase196(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7240"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase197(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7240"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2242(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase197(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7241"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase198(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7241"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2243(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6890,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase198(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7242"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase199(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7242"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2244(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase199(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7243"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase200(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7243"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2245(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase200(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7244"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase201(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7244"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2246(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase201(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase202(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2247(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase202(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7246"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase203(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7246"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2248(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase203(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7247"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase204(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7247"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2249(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5570,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase204(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7248"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase205(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7248"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2250(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5250,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase205(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7249"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase206(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7249"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2251(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4560,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase206(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7250"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase207(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7250"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2252(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4060,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase207(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase208(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2253(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase208(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7252"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase209(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7252"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2254(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase209(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7253"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase210(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7253"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2255(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,38000.,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase210(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7254"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase211(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7254"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2256(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,33000.,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase211(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7255"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase212(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7255"
        self.setglobal(__file__)
        self.runpy()
class countrateCase212(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7256"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase213(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="uvim1006.tab:7256"
        self.setglobal(__file__)
        self.runpy()
class countrateCase213(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase214(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase214(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7258"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase215(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7258"
        self.setglobal(__file__)
        self.runpy()
class countrateCase215(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7259"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase216(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7259"
        self.setglobal(__file__)
        self.runpy()
class countrateCase216(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7260"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase217(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7260"
        self.setglobal(__file__)
        self.runpy()
class countrateCase217(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7261"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase218(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7261"
        self.setglobal(__file__)
        self.runpy()
class countrateCase218(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7262"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase219(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7262"
        self.setglobal(__file__)
        self.runpy()
class countrateCase219(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase220(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase220(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="uvim1006.tab:7264"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase221(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7264"
        self.setglobal(__file__)
        self.runpy()
class countrateCase221(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase222(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase222(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase223(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase223(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7273"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase224(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7273"
        self.setglobal(__file__)
        self.runpy()
class countrateCase224(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7268"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase225(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7268"
        self.setglobal(__file__)
        self.runpy()
class countrateCase225(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase226(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase226(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7270"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase227(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7270"
        self.setglobal(__file__)
        self.runpy()
class countrateCase227(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase228(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase228(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase229(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase229(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase230(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase230(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase231(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase231(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase232(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase232(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase233(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase233(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase234(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase234(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase235(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase235(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase236(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase236(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7274"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase237(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7274"
        self.setglobal(__file__)
        self.runpy()
class countrateCase237(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase238(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase238(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase239(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase239(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase240(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase240(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase241(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase241(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase242(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase242(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7286"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase243(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7286"
        self.setglobal(__file__)
        self.runpy()
class countrateCase243(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase244(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase244(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7288"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase245(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7288"
        self.setglobal(__file__)
        self.runpy()
class countrateCase245(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase246(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase246(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase247(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase247(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase248(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase248(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase249(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase249(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase250(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase250(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase251(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase251(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7295"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase252(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7295"
        self.setglobal(__file__)
        self.runpy()
class countrateCase252(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7296"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase253(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7296"
        self.setglobal(__file__)
        self.runpy()
class countrateCase253(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7279"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase254(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7279"
        self.setglobal(__file__)
        self.runpy()
class countrateCase254(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7298"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase255(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7298"
        self.setglobal(__file__)
        self.runpy()
class countrateCase255(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase256(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase256(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7300"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase257(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7300"
        self.setglobal(__file__)
        self.runpy()
class countrateCase257(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7301"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase258(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7301"
        self.setglobal(__file__)
        self.runpy()
class countrateCase258(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7302"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase259(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7302"
        self.setglobal(__file__)
        self.runpy()
class countrateCase259(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7303"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase260(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="uvim1006.tab:7303"
        self.setglobal(__file__)
        self.runpy()
class countrateCase260(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase261(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase261(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase262(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase262(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase263(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase263(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase264(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase264(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7308"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase265(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7308"
        self.setglobal(__file__)
        self.runpy()
class countrateCase265(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7285"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase266(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7285"
        self.setglobal(__file__)
        self.runpy()
class countrateCase266(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7310"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase267(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7310"
        self.setglobal(__file__)
        self.runpy()
class countrateCase267(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase268(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase268(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7312"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase269(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7312"
        self.setglobal(__file__)
        self.runpy()
class countrateCase269(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="uvim1006.tab:7313"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase270(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7313"
        self.setglobal(__file__)
        self.runpy()
class countrateCase270(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7314"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase271(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="uvim1006.tab:7314"
        self.setglobal(__file__)
        self.runpy()
class countrateCase271(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7315"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase272(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim1006.tab:7315"
        self.setglobal(__file__)
        self.runpy()
class countrateCase272(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7316"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase273(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim1006.tab:7316"
        self.setglobal(__file__)
        self.runpy()
class countrateCase273(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase274(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase274(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7318"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase275(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim1006.tab:7318"
        self.setglobal(__file__)
        self.runpy()
class countrateCase275(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7319"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase276(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim1006.tab:7319"
        self.setglobal(__file__)
        self.runpy()
class countrateCase276(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7320"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase277(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim1006.tab:7320"
        self.setglobal(__file__)
        self.runpy()
class countrateCase277(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase278(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase278(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase279(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase279(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase280(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase280(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase281(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase281(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase282(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase282(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase283(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase283(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase284(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase284(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase285(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase285(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase286(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase286(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase287(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase287(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase288(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase288(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase289(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase289(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7333"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase290(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7333"
        self.setglobal(__file__)
        self.runpy()
class countrateCase290(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7334"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase291(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7334"
        self.setglobal(__file__)
        self.runpy()
class countrateCase291(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7335"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase292(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7335"
        self.setglobal(__file__)
        self.runpy()
class countrateCase292(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7336"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase293(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7336"
        self.setglobal(__file__)
        self.runpy()
class countrateCase293(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase294(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase294(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7338"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase295(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7338"
        self.setglobal(__file__)
        self.runpy()
class countrateCase295(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7339"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase296(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7339"
        self.setglobal(__file__)
        self.runpy()
class countrateCase296(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase297(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase297(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase298(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase298(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase299(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase299(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase300(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase300(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7344"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase301(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7344"
        self.setglobal(__file__)
        self.runpy()
class countrateCase301(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase302(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase302(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7346"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase303(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7346"
        self.setglobal(__file__)
        self.runpy()
class countrateCase303(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase304(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase304(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase305(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase305(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7349"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase306(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7349"
        self.setglobal(__file__)
        self.runpy()
class countrateCase306(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7350"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase307(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7350"
        self.setglobal(__file__)
        self.runpy()
class countrateCase307(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7351"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase308(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7351"
        self.setglobal(__file__)
        self.runpy()
class countrateCase308(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7352"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase309(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7352"
        self.setglobal(__file__)
        self.runpy()
class countrateCase309(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7353"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase310(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7353"
        self.setglobal(__file__)
        self.runpy()
class countrateCase310(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7354"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase311(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7354"
        self.setglobal(__file__)
        self.runpy()
class countrateCase311(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7355"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase312(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7355"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase312(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7356"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase313(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7356"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase314(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7357"
        self.setglobal(__file__)
        self.runpy()
class countrateCase313(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7357"
        self.setglobal(__file__)
        self.runpy()
class countrateCase314(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7357"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase315(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7357"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase316(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7358"
        self.setglobal(__file__)
        self.runpy()
class countrateCase315(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7358"
        self.setglobal(__file__)
        self.runpy()
class countrateCase316(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7358"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase317(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7358"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase318(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7359"
        self.setglobal(__file__)
        self.runpy()
class countrateCase317(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7359"
        self.setglobal(__file__)
        self.runpy()
class countrateCase318(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7359"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase319(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7359"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase320(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7360"
        self.setglobal(__file__)
        self.runpy()
class countrateCase319(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7360"
        self.setglobal(__file__)
        self.runpy()
class countrateCase320(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7360"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase321(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7360"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase322(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7361"
        self.setglobal(__file__)
        self.runpy()
class countrateCase321(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7361"
        self.setglobal(__file__)
        self.runpy()
class countrateCase322(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7361"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase323(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7361"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2263(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase324(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7362"
        self.setglobal(__file__)
        self.runpy()
class countrateCase323(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7362"
        self.setglobal(__file__)
        self.runpy()
class countrateCase324(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7362"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase325(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7362"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase326(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7363"
        self.setglobal(__file__)
        self.runpy()
class countrateCase325(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7363"
        self.setglobal(__file__)
        self.runpy()
class countrateCase326(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7363"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase327(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7363"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase328(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7364"
        self.setglobal(__file__)
        self.runpy()
class countrateCase327(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim1006.tab:7364"
        self.setglobal(__file__)
        self.runpy()
class countrateCase328(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7364"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase329(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7364"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase330(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="uvim1006.tab:7365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase329(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="uvim1006.tab:7365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase330(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7365"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase331(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase331(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="uvim1006.tab:7366"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase332(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="uvim1006.tab:7366"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase333(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="uvim1006.tab:7367"
        self.setglobal(__file__)
        self.runpy()
class countrateCase332(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="uvim1006.tab:7367"
        self.setglobal(__file__)
        self.runpy()
class countrateCase333(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7367"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase334(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7367"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase335(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase334(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase335(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim1006.tab:7368"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase336(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim1006.tab:7368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase336(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=False
        self.etcid="uvim1006.tab:7369"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase337(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=True
        self.etcid="uvim1006.tab:7369"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:2265 - 2239 dup =26
#thermback:0 - 0 dup =0
#calcphot:337 - 2 dup =335
#countrate:336 - 1 dup =335
#SpecSourcerateSpec:0 - 0 dup =0
