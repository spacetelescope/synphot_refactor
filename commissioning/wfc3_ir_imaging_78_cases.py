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
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0000', 'irim006.tab:0001', 'irim006.tab:0002', 'irim006.tab:0003', 'irim006.tab:0004', 'irim006.tab:0075', 'irim006.tab:0090', 'irim006.tab:0105', 'irim006.tab:0120', 'irim006.tab:0135', 'irim006.tab:0150', 'irim006.tab:0165', 'irim006.tab:0180', 'irim006.tab:0195', 'irim006.tab:0210', 'irim006.tab:0225', 'irim006.tab:0240', 'irim006.tab:0255', 'irim006.tab:0270', 'irim006.tab:0285', 'irim006.tab:0300', 'irim006.tab:0315', 'irim006.tab:0330', 'irim006.tab:0345', 'irim006.tab:0360', 'irim006.tab:0375', 'irim006.tab:0390', 'irim006.tab:0405', 'irim006.tab:0420', 'irim006.tab:0435', 'irim006.tab:0450', 'irim006.tab:0465', 'irim006.tab:0480', 'irim006.tab:0495', 'irim006.tab:0510', 'irim006.tab:0525', 'irim006.tab:0636', 'irim006.tab:0637', 'irim006.tab:0638', 'irim006.tab:0639', 'irim006.tab:0640', 'irim006.tab:0641', 'irim006.tab:0642', 'irim006.tab:0643']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0000', 'irim006.tab:0001', 'irim006.tab:0002', 'irim006.tab:0003', 'irim006.tab:0004', 'irim006.tab:0075', 'irim006.tab:0090', 'irim006.tab:0105', 'irim006.tab:0120', 'irim006.tab:0135', 'irim006.tab:0150', 'irim006.tab:0165', 'irim006.tab:0180', 'irim006.tab:0195', 'irim006.tab:0210', 'irim006.tab:0225', 'irim006.tab:0240', 'irim006.tab:0255', 'irim006.tab:0270', 'irim006.tab:0285', 'irim006.tab:0300', 'irim006.tab:0315', 'irim006.tab:0330', 'irim006.tab:0345', 'irim006.tab:0360', 'irim006.tab:0375', 'irim006.tab:0390', 'irim006.tab:0405', 'irim006.tab:0420', 'irim006.tab:0435', 'irim006.tab:0450', 'irim006.tab:0465', 'irim006.tab:0480', 'irim006.tab:0495', 'irim006.tab:0510', 'irim006.tab:0525', 'irim006.tab:0636', 'irim006.tab:0637', 'irim006.tab:0638', 'irim006.tab:0639', 'irim006.tab:0640', 'irim006.tab:0641', 'irim006.tab:0642', 'irim006.tab:0643']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0000', 'irim006.tab:0002', 'irim006.tab:0003', 'irim006.tab:0004', 'irim006.tab:0075', 'irim006.tab:0090', 'irim006.tab:0105', 'irim006.tab:0120', 'irim006.tab:0135', 'irim006.tab:0150', 'irim006.tab:0165', 'irim006.tab:0180', 'irim006.tab:0195', 'irim006.tab:0210', 'irim006.tab:0225', 'irim006.tab:0240', 'irim006.tab:0255', 'irim006.tab:0270', 'irim006.tab:0285', 'irim006.tab:0300', 'irim006.tab:0315', 'irim006.tab:0330', 'irim006.tab:0345', 'irim006.tab:0360', 'irim006.tab:0375', 'irim006.tab:0390', 'irim006.tab:0405', 'irim006.tab:0420', 'irim006.tab:0435', 'irim006.tab:0450', 'irim006.tab:0465', 'irim006.tab:0480', 'irim006.tab:0495']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0000', 'irim006.tab:0002', 'irim006.tab:0003', 'irim006.tab:0004', 'irim006.tab:0075', 'irim006.tab:0090', 'irim006.tab:0105', 'irim006.tab:0120', 'irim006.tab:0135', 'irim006.tab:0150', 'irim006.tab:0165', 'irim006.tab:0180', 'irim006.tab:0195', 'irim006.tab:0210', 'irim006.tab:0225', 'irim006.tab:0240', 'irim006.tab:0255', 'irim006.tab:0270', 'irim006.tab:0285', 'irim006.tab:0300', 'irim006.tab:0315', 'irim006.tab:0330', 'irim006.tab:0345', 'irim006.tab:0360', 'irim006.tab:0375', 'irim006.tab:0390', 'irim006.tab:0405', 'irim006.tab:0420', 'irim006.tab:0435', 'irim006.tab:0450', 'irim006.tab:0465', 'irim006.tab:0480', 'irim006.tab:0495']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0001', 'irim006.tab:0510', 'irim006.tab:0525']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0001', 'irim006.tab:0510', 'irim006.tab:0525']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0005', 'irim006.tab:0006', 'irim006.tab:0007', 'irim006.tab:0008', 'irim006.tab:0009', 'irim006.tab:0076', 'irim006.tab:0091', 'irim006.tab:0106', 'irim006.tab:0121', 'irim006.tab:0136', 'irim006.tab:0151', 'irim006.tab:0166', 'irim006.tab:0181', 'irim006.tab:0196', 'irim006.tab:0211', 'irim006.tab:0226', 'irim006.tab:0241', 'irim006.tab:0256', 'irim006.tab:0271', 'irim006.tab:0286', 'irim006.tab:0301', 'irim006.tab:0316', 'irim006.tab:0331', 'irim006.tab:0346', 'irim006.tab:0361', 'irim006.tab:0376', 'irim006.tab:0391', 'irim006.tab:0406', 'irim006.tab:0421', 'irim006.tab:0436', 'irim006.tab:0451', 'irim006.tab:0466', 'irim006.tab:0481', 'irim006.tab:0496', 'irim006.tab:0511', 'irim006.tab:0526']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0005', 'irim006.tab:0006', 'irim006.tab:0007', 'irim006.tab:0008', 'irim006.tab:0009', 'irim006.tab:0076', 'irim006.tab:0091', 'irim006.tab:0106', 'irim006.tab:0121', 'irim006.tab:0136', 'irim006.tab:0151', 'irim006.tab:0166', 'irim006.tab:0181', 'irim006.tab:0196', 'irim006.tab:0211', 'irim006.tab:0226', 'irim006.tab:0241', 'irim006.tab:0256', 'irim006.tab:0271', 'irim006.tab:0286', 'irim006.tab:0301', 'irim006.tab:0316', 'irim006.tab:0331', 'irim006.tab:0346', 'irim006.tab:0361', 'irim006.tab:0376', 'irim006.tab:0391', 'irim006.tab:0406', 'irim006.tab:0421', 'irim006.tab:0436', 'irim006.tab:0451', 'irim006.tab:0466', 'irim006.tab:0481', 'irim006.tab:0496', 'irim006.tab:0511', 'irim006.tab:0526']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0005', 'irim006.tab:0007', 'irim006.tab:0008', 'irim006.tab:0009', 'irim006.tab:0076', 'irim006.tab:0091', 'irim006.tab:0106', 'irim006.tab:0121', 'irim006.tab:0136', 'irim006.tab:0151', 'irim006.tab:0166', 'irim006.tab:0181', 'irim006.tab:0196', 'irim006.tab:0211', 'irim006.tab:0226', 'irim006.tab:0241', 'irim006.tab:0256', 'irim006.tab:0271', 'irim006.tab:0286', 'irim006.tab:0301', 'irim006.tab:0316', 'irim006.tab:0331', 'irim006.tab:0346', 'irim006.tab:0361', 'irim006.tab:0376', 'irim006.tab:0391', 'irim006.tab:0406', 'irim006.tab:0421', 'irim006.tab:0436', 'irim006.tab:0451', 'irim006.tab:0466', 'irim006.tab:0481', 'irim006.tab:0496']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=True
        self.etcid="['irim006.tab:0005', 'irim006.tab:0007', 'irim006.tab:0008', 'irim006.tab:0009', 'irim006.tab:0076', 'irim006.tab:0091', 'irim006.tab:0106', 'irim006.tab:0121', 'irim006.tab:0136', 'irim006.tab:0151', 'irim006.tab:0166', 'irim006.tab:0181', 'irim006.tab:0196', 'irim006.tab:0211', 'irim006.tab:0226', 'irim006.tab:0241', 'irim006.tab:0256', 'irim006.tab:0271', 'irim006.tab:0286', 'irim006.tab:0301', 'irim006.tab:0316', 'irim006.tab:0331', 'irim006.tab:0346', 'irim006.tab:0361', 'irim006.tab:0376', 'irim006.tab:0391', 'irim006.tab:0406', 'irim006.tab:0421', 'irim006.tab:0436', 'irim006.tab:0451', 'irim006.tab:0466', 'irim006.tab:0481', 'irim006.tab:0496']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0006', 'irim006.tab:0511', 'irim006.tab:0526']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0006', 'irim006.tab:0511', 'irim006.tab:0526']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0010', 'irim006.tab:0011', 'irim006.tab:0012', 'irim006.tab:0013', 'irim006.tab:0014', 'irim006.tab:0077', 'irim006.tab:0092', 'irim006.tab:0107', 'irim006.tab:0122', 'irim006.tab:0137', 'irim006.tab:0152', 'irim006.tab:0167', 'irim006.tab:0182', 'irim006.tab:0197', 'irim006.tab:0212', 'irim006.tab:0227', 'irim006.tab:0242', 'irim006.tab:0257', 'irim006.tab:0272', 'irim006.tab:0287', 'irim006.tab:0302', 'irim006.tab:0317', 'irim006.tab:0332', 'irim006.tab:0347', 'irim006.tab:0362', 'irim006.tab:0377', 'irim006.tab:0392', 'irim006.tab:0407', 'irim006.tab:0422', 'irim006.tab:0437', 'irim006.tab:0452', 'irim006.tab:0467', 'irim006.tab:0482', 'irim006.tab:0497', 'irim006.tab:0512', 'irim006.tab:0527']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0010', 'irim006.tab:0011', 'irim006.tab:0012', 'irim006.tab:0013', 'irim006.tab:0014', 'irim006.tab:0077', 'irim006.tab:0092', 'irim006.tab:0107', 'irim006.tab:0122', 'irim006.tab:0137', 'irim006.tab:0152', 'irim006.tab:0167', 'irim006.tab:0182', 'irim006.tab:0197', 'irim006.tab:0212', 'irim006.tab:0227', 'irim006.tab:0242', 'irim006.tab:0257', 'irim006.tab:0272', 'irim006.tab:0287', 'irim006.tab:0302', 'irim006.tab:0317', 'irim006.tab:0332', 'irim006.tab:0347', 'irim006.tab:0362', 'irim006.tab:0377', 'irim006.tab:0392', 'irim006.tab:0407', 'irim006.tab:0422', 'irim006.tab:0437', 'irim006.tab:0452', 'irim006.tab:0467', 'irim006.tab:0482', 'irim006.tab:0497', 'irim006.tab:0512', 'irim006.tab:0527']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0010', 'irim006.tab:0012', 'irim006.tab:0013', 'irim006.tab:0014', 'irim006.tab:0077', 'irim006.tab:0092', 'irim006.tab:0107', 'irim006.tab:0122', 'irim006.tab:0137', 'irim006.tab:0152', 'irim006.tab:0167', 'irim006.tab:0182', 'irim006.tab:0197', 'irim006.tab:0212', 'irim006.tab:0227', 'irim006.tab:0242', 'irim006.tab:0257', 'irim006.tab:0272', 'irim006.tab:0287', 'irim006.tab:0302', 'irim006.tab:0317', 'irim006.tab:0332', 'irim006.tab:0347', 'irim006.tab:0362', 'irim006.tab:0377', 'irim006.tab:0392', 'irim006.tab:0407', 'irim006.tab:0422', 'irim006.tab:0437', 'irim006.tab:0452', 'irim006.tab:0467', 'irim006.tab:0482', 'irim006.tab:0497']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0010', 'irim006.tab:0012', 'irim006.tab:0013', 'irim006.tab:0014', 'irim006.tab:0077', 'irim006.tab:0092', 'irim006.tab:0107', 'irim006.tab:0122', 'irim006.tab:0137', 'irim006.tab:0152', 'irim006.tab:0167', 'irim006.tab:0182', 'irim006.tab:0197', 'irim006.tab:0212', 'irim006.tab:0227', 'irim006.tab:0242', 'irim006.tab:0257', 'irim006.tab:0272', 'irim006.tab:0287', 'irim006.tab:0302', 'irim006.tab:0317', 'irim006.tab:0332', 'irim006.tab:0347', 'irim006.tab:0362', 'irim006.tab:0377', 'irim006.tab:0392', 'irim006.tab:0407', 'irim006.tab:0422', 'irim006.tab:0437', 'irim006.tab:0452', 'irim006.tab:0467', 'irim006.tab:0482', 'irim006.tab:0497']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0011', 'irim006.tab:0512', 'irim006.tab:0527']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0011', 'irim006.tab:0512', 'irim006.tab:0527']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0015', 'irim006.tab:0016', 'irim006.tab:0017', 'irim006.tab:0018', 'irim006.tab:0019', 'irim006.tab:0078', 'irim006.tab:0093', 'irim006.tab:0108', 'irim006.tab:0123', 'irim006.tab:0138', 'irim006.tab:0153', 'irim006.tab:0168', 'irim006.tab:0183', 'irim006.tab:0198', 'irim006.tab:0213', 'irim006.tab:0228', 'irim006.tab:0243', 'irim006.tab:0258', 'irim006.tab:0273', 'irim006.tab:0288', 'irim006.tab:0303', 'irim006.tab:0318', 'irim006.tab:0333', 'irim006.tab:0348', 'irim006.tab:0363', 'irim006.tab:0378', 'irim006.tab:0393', 'irim006.tab:0408', 'irim006.tab:0423', 'irim006.tab:0438', 'irim006.tab:0453', 'irim006.tab:0468', 'irim006.tab:0483', 'irim006.tab:0498', 'irim006.tab:0513', 'irim006.tab:0528', 'irim006.tab:0540', 'irim006.tab:0541', 'irim006.tab:0542', 'irim006.tab:0543', 'irim006.tab:0544', 'irim006.tab:0545', 'irim006.tab:0546', 'irim006.tab:0547', 'irim006.tab:0548', 'irim006.tab:0549', 'irim006.tab:0550', 'irim006.tab:0551', 'irim006.tab:0552', 'irim006.tab:0553', 'irim006.tab:0554', 'irim006.tab:0555', 'irim006.tab:0556', 'irim006.tab:0557', 'irim006.tab:0558', 'irim006.tab:0559', 'irim006.tab:0560', 'irim006.tab:0561', 'irim006.tab:0562', 'irim006.tab:0563']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['irim006.tab:0015', 'irim006.tab:0016', 'irim006.tab:0017', 'irim006.tab:0018', 'irim006.tab:0019', 'irim006.tab:0078', 'irim006.tab:0093', 'irim006.tab:0108', 'irim006.tab:0123', 'irim006.tab:0138', 'irim006.tab:0153', 'irim006.tab:0168', 'irim006.tab:0183', 'irim006.tab:0198', 'irim006.tab:0213', 'irim006.tab:0228', 'irim006.tab:0243', 'irim006.tab:0258', 'irim006.tab:0273', 'irim006.tab:0288', 'irim006.tab:0303', 'irim006.tab:0318', 'irim006.tab:0333', 'irim006.tab:0348', 'irim006.tab:0363', 'irim006.tab:0378', 'irim006.tab:0393', 'irim006.tab:0408', 'irim006.tab:0423', 'irim006.tab:0438', 'irim006.tab:0453', 'irim006.tab:0468', 'irim006.tab:0483', 'irim006.tab:0498', 'irim006.tab:0513', 'irim006.tab:0528', 'irim006.tab:0540', 'irim006.tab:0541', 'irim006.tab:0542', 'irim006.tab:0543', 'irim006.tab:0544', 'irim006.tab:0545', 'irim006.tab:0546', 'irim006.tab:0547', 'irim006.tab:0548', 'irim006.tab:0549', 'irim006.tab:0550', 'irim006.tab:0551', 'irim006.tab:0552', 'irim006.tab:0553', 'irim006.tab:0554', 'irim006.tab:0555', 'irim006.tab:0556', 'irim006.tab:0557', 'irim006.tab:0558', 'irim006.tab:0559', 'irim006.tab:0560', 'irim006.tab:0561', 'irim006.tab:0562', 'irim006.tab:0563']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=True
        self.etcid="['irim006.tab:0015', 'irim006.tab:0017', 'irim006.tab:0018', 'irim006.tab:0019', 'irim006.tab:0078', 'irim006.tab:0093', 'irim006.tab:0108', 'irim006.tab:0123', 'irim006.tab:0138', 'irim006.tab:0153', 'irim006.tab:0168', 'irim006.tab:0183', 'irim006.tab:0198', 'irim006.tab:0213', 'irim006.tab:0228', 'irim006.tab:0243', 'irim006.tab:0258', 'irim006.tab:0273', 'irim006.tab:0288', 'irim006.tab:0303', 'irim006.tab:0318', 'irim006.tab:0333', 'irim006.tab:0348', 'irim006.tab:0363', 'irim006.tab:0378', 'irim006.tab:0393', 'irim006.tab:0408', 'irim006.tab:0423', 'irim006.tab:0438', 'irim006.tab:0453', 'irim006.tab:0468', 'irim006.tab:0483', 'irim006.tab:0498']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0015', 'irim006.tab:0017', 'irim006.tab:0018', 'irim006.tab:0019', 'irim006.tab:0078', 'irim006.tab:0093', 'irim006.tab:0108', 'irim006.tab:0123', 'irim006.tab:0138', 'irim006.tab:0153', 'irim006.tab:0168', 'irim006.tab:0183', 'irim006.tab:0198', 'irim006.tab:0213', 'irim006.tab:0228', 'irim006.tab:0243', 'irim006.tab:0258', 'irim006.tab:0273', 'irim006.tab:0288', 'irim006.tab:0303', 'irim006.tab:0318', 'irim006.tab:0333', 'irim006.tab:0348', 'irim006.tab:0363', 'irim006.tab:0378', 'irim006.tab:0393', 'irim006.tab:0408', 'irim006.tab:0423', 'irim006.tab:0438', 'irim006.tab:0453', 'irim006.tab:0468', 'irim006.tab:0483', 'irim006.tab:0498']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0016', 'irim006.tab:0513', 'irim006.tab:0528']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0016', 'irim006.tab:0513', 'irim006.tab:0528']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0020', 'irim006.tab:0021', 'irim006.tab:0022', 'irim006.tab:0023', 'irim006.tab:0024', 'irim006.tab:0079', 'irim006.tab:0094', 'irim006.tab:0109', 'irim006.tab:0124', 'irim006.tab:0139', 'irim006.tab:0154', 'irim006.tab:0169', 'irim006.tab:0184', 'irim006.tab:0199', 'irim006.tab:0214', 'irim006.tab:0229', 'irim006.tab:0244', 'irim006.tab:0259', 'irim006.tab:0274', 'irim006.tab:0289', 'irim006.tab:0304', 'irim006.tab:0319', 'irim006.tab:0334', 'irim006.tab:0349', 'irim006.tab:0364', 'irim006.tab:0379', 'irim006.tab:0394', 'irim006.tab:0409', 'irim006.tab:0424', 'irim006.tab:0439', 'irim006.tab:0454', 'irim006.tab:0469', 'irim006.tab:0484', 'irim006.tab:0499', 'irim006.tab:0514', 'irim006.tab:0529', 'irim006.tab:0645']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0020', 'irim006.tab:0021', 'irim006.tab:0022', 'irim006.tab:0023', 'irim006.tab:0024', 'irim006.tab:0079', 'irim006.tab:0094', 'irim006.tab:0109', 'irim006.tab:0124', 'irim006.tab:0139', 'irim006.tab:0154', 'irim006.tab:0169', 'irim006.tab:0184', 'irim006.tab:0199', 'irim006.tab:0214', 'irim006.tab:0229', 'irim006.tab:0244', 'irim006.tab:0259', 'irim006.tab:0274', 'irim006.tab:0289', 'irim006.tab:0304', 'irim006.tab:0319', 'irim006.tab:0334', 'irim006.tab:0349', 'irim006.tab:0364', 'irim006.tab:0379', 'irim006.tab:0394', 'irim006.tab:0409', 'irim006.tab:0424', 'irim006.tab:0439', 'irim006.tab:0454', 'irim006.tab:0469', 'irim006.tab:0484', 'irim006.tab:0499', 'irim006.tab:0514', 'irim006.tab:0529', 'irim006.tab:0645']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0020', 'irim006.tab:0022', 'irim006.tab:0023', 'irim006.tab:0024', 'irim006.tab:0079', 'irim006.tab:0094', 'irim006.tab:0109', 'irim006.tab:0124', 'irim006.tab:0139', 'irim006.tab:0154', 'irim006.tab:0169', 'irim006.tab:0184', 'irim006.tab:0199', 'irim006.tab:0214', 'irim006.tab:0229', 'irim006.tab:0244', 'irim006.tab:0259', 'irim006.tab:0274', 'irim006.tab:0289', 'irim006.tab:0304', 'irim006.tab:0319', 'irim006.tab:0334', 'irim006.tab:0349', 'irim006.tab:0364', 'irim006.tab:0379', 'irim006.tab:0394', 'irim006.tab:0409', 'irim006.tab:0424', 'irim006.tab:0439', 'irim006.tab:0454', 'irim006.tab:0469', 'irim006.tab:0484', 'irim006.tab:0499']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0020', 'irim006.tab:0022', 'irim006.tab:0023', 'irim006.tab:0024', 'irim006.tab:0079', 'irim006.tab:0094', 'irim006.tab:0109', 'irim006.tab:0124', 'irim006.tab:0139', 'irim006.tab:0154', 'irim006.tab:0169', 'irim006.tab:0184', 'irim006.tab:0199', 'irim006.tab:0214', 'irim006.tab:0229', 'irim006.tab:0244', 'irim006.tab:0259', 'irim006.tab:0274', 'irim006.tab:0289', 'irim006.tab:0304', 'irim006.tab:0319', 'irim006.tab:0334', 'irim006.tab:0349', 'irim006.tab:0364', 'irim006.tab:0379', 'irim006.tab:0394', 'irim006.tab:0409', 'irim006.tab:0424', 'irim006.tab:0439', 'irim006.tab:0454', 'irim006.tab:0469', 'irim006.tab:0484', 'irim006.tab:0499']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0021', 'irim006.tab:0514', 'irim006.tab:0529']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0021', 'irim006.tab:0514', 'irim006.tab:0529']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0025', 'irim006.tab:0026', 'irim006.tab:0027', 'irim006.tab:0028', 'irim006.tab:0029', 'irim006.tab:0080', 'irim006.tab:0095', 'irim006.tab:0110', 'irim006.tab:0125', 'irim006.tab:0140', 'irim006.tab:0155', 'irim006.tab:0170', 'irim006.tab:0185', 'irim006.tab:0200', 'irim006.tab:0215', 'irim006.tab:0230', 'irim006.tab:0245', 'irim006.tab:0260', 'irim006.tab:0275', 'irim006.tab:0290', 'irim006.tab:0305', 'irim006.tab:0320', 'irim006.tab:0335', 'irim006.tab:0350', 'irim006.tab:0365', 'irim006.tab:0380', 'irim006.tab:0395', 'irim006.tab:0410', 'irim006.tab:0425', 'irim006.tab:0440', 'irim006.tab:0455', 'irim006.tab:0470', 'irim006.tab:0485', 'irim006.tab:0500', 'irim006.tab:0515', 'irim006.tab:0530']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0025', 'irim006.tab:0026', 'irim006.tab:0027', 'irim006.tab:0028', 'irim006.tab:0029', 'irim006.tab:0080', 'irim006.tab:0095', 'irim006.tab:0110', 'irim006.tab:0125', 'irim006.tab:0140', 'irim006.tab:0155', 'irim006.tab:0170', 'irim006.tab:0185', 'irim006.tab:0200', 'irim006.tab:0215', 'irim006.tab:0230', 'irim006.tab:0245', 'irim006.tab:0260', 'irim006.tab:0275', 'irim006.tab:0290', 'irim006.tab:0305', 'irim006.tab:0320', 'irim006.tab:0335', 'irim006.tab:0350', 'irim006.tab:0365', 'irim006.tab:0380', 'irim006.tab:0395', 'irim006.tab:0410', 'irim006.tab:0425', 'irim006.tab:0440', 'irim006.tab:0455', 'irim006.tab:0470', 'irim006.tab:0485', 'irim006.tab:0500', 'irim006.tab:0515', 'irim006.tab:0530']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0025', 'irim006.tab:0027', 'irim006.tab:0028', 'irim006.tab:0029', 'irim006.tab:0080', 'irim006.tab:0095', 'irim006.tab:0110', 'irim006.tab:0125', 'irim006.tab:0140', 'irim006.tab:0155', 'irim006.tab:0170', 'irim006.tab:0185', 'irim006.tab:0200', 'irim006.tab:0215', 'irim006.tab:0230', 'irim006.tab:0245', 'irim006.tab:0260', 'irim006.tab:0275', 'irim006.tab:0290', 'irim006.tab:0305', 'irim006.tab:0320', 'irim006.tab:0335', 'irim006.tab:0350', 'irim006.tab:0365', 'irim006.tab:0380', 'irim006.tab:0395', 'irim006.tab:0410', 'irim006.tab:0425', 'irim006.tab:0440', 'irim006.tab:0455', 'irim006.tab:0470', 'irim006.tab:0485', 'irim006.tab:0500']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0025', 'irim006.tab:0027', 'irim006.tab:0028', 'irim006.tab:0029', 'irim006.tab:0080', 'irim006.tab:0095', 'irim006.tab:0110', 'irim006.tab:0125', 'irim006.tab:0140', 'irim006.tab:0155', 'irim006.tab:0170', 'irim006.tab:0185', 'irim006.tab:0200', 'irim006.tab:0215', 'irim006.tab:0230', 'irim006.tab:0245', 'irim006.tab:0260', 'irim006.tab:0275', 'irim006.tab:0290', 'irim006.tab:0305', 'irim006.tab:0320', 'irim006.tab:0335', 'irim006.tab:0350', 'irim006.tab:0365', 'irim006.tab:0380', 'irim006.tab:0395', 'irim006.tab:0410', 'irim006.tab:0425', 'irim006.tab:0440', 'irim006.tab:0455', 'irim006.tab:0470', 'irim006.tab:0485', 'irim006.tab:0500']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0026', 'irim006.tab:0515', 'irim006.tab:0530']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0026', 'irim006.tab:0515', 'irim006.tab:0530']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0030', 'irim006.tab:0031', 'irim006.tab:0032', 'irim006.tab:0033', 'irim006.tab:0034', 'irim006.tab:0081', 'irim006.tab:0096', 'irim006.tab:0111', 'irim006.tab:0126', 'irim006.tab:0141', 'irim006.tab:0156', 'irim006.tab:0171', 'irim006.tab:0186', 'irim006.tab:0201', 'irim006.tab:0216', 'irim006.tab:0231', 'irim006.tab:0246', 'irim006.tab:0261', 'irim006.tab:0276', 'irim006.tab:0291', 'irim006.tab:0306', 'irim006.tab:0321', 'irim006.tab:0336', 'irim006.tab:0351', 'irim006.tab:0366', 'irim006.tab:0381', 'irim006.tab:0396', 'irim006.tab:0411', 'irim006.tab:0426', 'irim006.tab:0441', 'irim006.tab:0456', 'irim006.tab:0471', 'irim006.tab:0486', 'irim006.tab:0501', 'irim006.tab:0516', 'irim006.tab:0531']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0030', 'irim006.tab:0031', 'irim006.tab:0032', 'irim006.tab:0033', 'irim006.tab:0034', 'irim006.tab:0081', 'irim006.tab:0096', 'irim006.tab:0111', 'irim006.tab:0126', 'irim006.tab:0141', 'irim006.tab:0156', 'irim006.tab:0171', 'irim006.tab:0186', 'irim006.tab:0201', 'irim006.tab:0216', 'irim006.tab:0231', 'irim006.tab:0246', 'irim006.tab:0261', 'irim006.tab:0276', 'irim006.tab:0291', 'irim006.tab:0306', 'irim006.tab:0321', 'irim006.tab:0336', 'irim006.tab:0351', 'irim006.tab:0366', 'irim006.tab:0381', 'irim006.tab:0396', 'irim006.tab:0411', 'irim006.tab:0426', 'irim006.tab:0441', 'irim006.tab:0456', 'irim006.tab:0471', 'irim006.tab:0486', 'irim006.tab:0501', 'irim006.tab:0516', 'irim006.tab:0531']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0030', 'irim006.tab:0032', 'irim006.tab:0033', 'irim006.tab:0034', 'irim006.tab:0081', 'irim006.tab:0096', 'irim006.tab:0111', 'irim006.tab:0126', 'irim006.tab:0141', 'irim006.tab:0156', 'irim006.tab:0171', 'irim006.tab:0186', 'irim006.tab:0201', 'irim006.tab:0216', 'irim006.tab:0231', 'irim006.tab:0246', 'irim006.tab:0261', 'irim006.tab:0276', 'irim006.tab:0291', 'irim006.tab:0306', 'irim006.tab:0321', 'irim006.tab:0336', 'irim006.tab:0351', 'irim006.tab:0366', 'irim006.tab:0381', 'irim006.tab:0396', 'irim006.tab:0411', 'irim006.tab:0426', 'irim006.tab:0441', 'irim006.tab:0456', 'irim006.tab:0471', 'irim006.tab:0486', 'irim006.tab:0501']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0030', 'irim006.tab:0032', 'irim006.tab:0033', 'irim006.tab:0034', 'irim006.tab:0081', 'irim006.tab:0096', 'irim006.tab:0111', 'irim006.tab:0126', 'irim006.tab:0141', 'irim006.tab:0156', 'irim006.tab:0171', 'irim006.tab:0186', 'irim006.tab:0201', 'irim006.tab:0216', 'irim006.tab:0231', 'irim006.tab:0246', 'irim006.tab:0261', 'irim006.tab:0276', 'irim006.tab:0291', 'irim006.tab:0306', 'irim006.tab:0321', 'irim006.tab:0336', 'irim006.tab:0351', 'irim006.tab:0366', 'irim006.tab:0381', 'irim006.tab:0396', 'irim006.tab:0411', 'irim006.tab:0426', 'irim006.tab:0441', 'irim006.tab:0456', 'irim006.tab:0471', 'irim006.tab:0486', 'irim006.tab:0501']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0031', 'irim006.tab:0516', 'irim006.tab:0531']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0031', 'irim006.tab:0516', 'irim006.tab:0531']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0035', 'irim006.tab:0036', 'irim006.tab:0037', 'irim006.tab:0038', 'irim006.tab:0039', 'irim006.tab:0082', 'irim006.tab:0097', 'irim006.tab:0112', 'irim006.tab:0127', 'irim006.tab:0142', 'irim006.tab:0157', 'irim006.tab:0172', 'irim006.tab:0187', 'irim006.tab:0202', 'irim006.tab:0217', 'irim006.tab:0232', 'irim006.tab:0247', 'irim006.tab:0262', 'irim006.tab:0277', 'irim006.tab:0292', 'irim006.tab:0307', 'irim006.tab:0322', 'irim006.tab:0337', 'irim006.tab:0352', 'irim006.tab:0367', 'irim006.tab:0382', 'irim006.tab:0397', 'irim006.tab:0412', 'irim006.tab:0427', 'irim006.tab:0442', 'irim006.tab:0457', 'irim006.tab:0472', 'irim006.tab:0487', 'irim006.tab:0502', 'irim006.tab:0517', 'irim006.tab:0532']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0035', 'irim006.tab:0036', 'irim006.tab:0037', 'irim006.tab:0038', 'irim006.tab:0039', 'irim006.tab:0082', 'irim006.tab:0097', 'irim006.tab:0112', 'irim006.tab:0127', 'irim006.tab:0142', 'irim006.tab:0157', 'irim006.tab:0172', 'irim006.tab:0187', 'irim006.tab:0202', 'irim006.tab:0217', 'irim006.tab:0232', 'irim006.tab:0247', 'irim006.tab:0262', 'irim006.tab:0277', 'irim006.tab:0292', 'irim006.tab:0307', 'irim006.tab:0322', 'irim006.tab:0337', 'irim006.tab:0352', 'irim006.tab:0367', 'irim006.tab:0382', 'irim006.tab:0397', 'irim006.tab:0412', 'irim006.tab:0427', 'irim006.tab:0442', 'irim006.tab:0457', 'irim006.tab:0472', 'irim006.tab:0487', 'irim006.tab:0502', 'irim006.tab:0517', 'irim006.tab:0532']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0035', 'irim006.tab:0037', 'irim006.tab:0038', 'irim006.tab:0039', 'irim006.tab:0082', 'irim006.tab:0097', 'irim006.tab:0112', 'irim006.tab:0127', 'irim006.tab:0142', 'irim006.tab:0157', 'irim006.tab:0172', 'irim006.tab:0187', 'irim006.tab:0202', 'irim006.tab:0217', 'irim006.tab:0232', 'irim006.tab:0247', 'irim006.tab:0262', 'irim006.tab:0277', 'irim006.tab:0292', 'irim006.tab:0307', 'irim006.tab:0322', 'irim006.tab:0337', 'irim006.tab:0352', 'irim006.tab:0367', 'irim006.tab:0382', 'irim006.tab:0397', 'irim006.tab:0412', 'irim006.tab:0427', 'irim006.tab:0442', 'irim006.tab:0457', 'irim006.tab:0472', 'irim006.tab:0487', 'irim006.tab:0502']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0035', 'irim006.tab:0037', 'irim006.tab:0038', 'irim006.tab:0039', 'irim006.tab:0082', 'irim006.tab:0097', 'irim006.tab:0112', 'irim006.tab:0127', 'irim006.tab:0142', 'irim006.tab:0157', 'irim006.tab:0172', 'irim006.tab:0187', 'irim006.tab:0202', 'irim006.tab:0217', 'irim006.tab:0232', 'irim006.tab:0247', 'irim006.tab:0262', 'irim006.tab:0277', 'irim006.tab:0292', 'irim006.tab:0307', 'irim006.tab:0322', 'irim006.tab:0337', 'irim006.tab:0352', 'irim006.tab:0367', 'irim006.tab:0382', 'irim006.tab:0397', 'irim006.tab:0412', 'irim006.tab:0427', 'irim006.tab:0442', 'irim006.tab:0457', 'irim006.tab:0472', 'irim006.tab:0487', 'irim006.tab:0502']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0036', 'irim006.tab:0517', 'irim006.tab:0532']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0036', 'irim006.tab:0517', 'irim006.tab:0532']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0040', 'irim006.tab:0041', 'irim006.tab:0042', 'irim006.tab:0043', 'irim006.tab:0044', 'irim006.tab:0083', 'irim006.tab:0098', 'irim006.tab:0113', 'irim006.tab:0128', 'irim006.tab:0143', 'irim006.tab:0158', 'irim006.tab:0173', 'irim006.tab:0188', 'irim006.tab:0203', 'irim006.tab:0218', 'irim006.tab:0233', 'irim006.tab:0248', 'irim006.tab:0263', 'irim006.tab:0278', 'irim006.tab:0293', 'irim006.tab:0308', 'irim006.tab:0323', 'irim006.tab:0338', 'irim006.tab:0353', 'irim006.tab:0368', 'irim006.tab:0383', 'irim006.tab:0398', 'irim006.tab:0413', 'irim006.tab:0428', 'irim006.tab:0443', 'irim006.tab:0458', 'irim006.tab:0473', 'irim006.tab:0488', 'irim006.tab:0503', 'irim006.tab:0518', 'irim006.tab:0533']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0040', 'irim006.tab:0041', 'irim006.tab:0042', 'irim006.tab:0043', 'irim006.tab:0044', 'irim006.tab:0083', 'irim006.tab:0098', 'irim006.tab:0113', 'irim006.tab:0128', 'irim006.tab:0143', 'irim006.tab:0158', 'irim006.tab:0173', 'irim006.tab:0188', 'irim006.tab:0203', 'irim006.tab:0218', 'irim006.tab:0233', 'irim006.tab:0248', 'irim006.tab:0263', 'irim006.tab:0278', 'irim006.tab:0293', 'irim006.tab:0308', 'irim006.tab:0323', 'irim006.tab:0338', 'irim006.tab:0353', 'irim006.tab:0368', 'irim006.tab:0383', 'irim006.tab:0398', 'irim006.tab:0413', 'irim006.tab:0428', 'irim006.tab:0443', 'irim006.tab:0458', 'irim006.tab:0473', 'irim006.tab:0488', 'irim006.tab:0503', 'irim006.tab:0518', 'irim006.tab:0533']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0040', 'irim006.tab:0042', 'irim006.tab:0043', 'irim006.tab:0044', 'irim006.tab:0083', 'irim006.tab:0098', 'irim006.tab:0113', 'irim006.tab:0128', 'irim006.tab:0143', 'irim006.tab:0158', 'irim006.tab:0173', 'irim006.tab:0188', 'irim006.tab:0203', 'irim006.tab:0218', 'irim006.tab:0233', 'irim006.tab:0248', 'irim006.tab:0263', 'irim006.tab:0278', 'irim006.tab:0293', 'irim006.tab:0308', 'irim006.tab:0323', 'irim006.tab:0338', 'irim006.tab:0353', 'irim006.tab:0368', 'irim006.tab:0383', 'irim006.tab:0398', 'irim006.tab:0413', 'irim006.tab:0428', 'irim006.tab:0443', 'irim006.tab:0458', 'irim006.tab:0473', 'irim006.tab:0488', 'irim006.tab:0503']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0040', 'irim006.tab:0042', 'irim006.tab:0043', 'irim006.tab:0044', 'irim006.tab:0083', 'irim006.tab:0098', 'irim006.tab:0113', 'irim006.tab:0128', 'irim006.tab:0143', 'irim006.tab:0158', 'irim006.tab:0173', 'irim006.tab:0188', 'irim006.tab:0203', 'irim006.tab:0218', 'irim006.tab:0233', 'irim006.tab:0248', 'irim006.tab:0263', 'irim006.tab:0278', 'irim006.tab:0293', 'irim006.tab:0308', 'irim006.tab:0323', 'irim006.tab:0338', 'irim006.tab:0353', 'irim006.tab:0368', 'irim006.tab:0383', 'irim006.tab:0398', 'irim006.tab:0413', 'irim006.tab:0428', 'irim006.tab:0443', 'irim006.tab:0458', 'irim006.tab:0473', 'irim006.tab:0488', 'irim006.tab:0503']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0041', 'irim006.tab:0518', 'irim006.tab:0533']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0041', 'irim006.tab:0518', 'irim006.tab:0533']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0045', 'irim006.tab:0046', 'irim006.tab:0047', 'irim006.tab:0048', 'irim006.tab:0049', 'irim006.tab:0084', 'irim006.tab:0099', 'irim006.tab:0114', 'irim006.tab:0129', 'irim006.tab:0144', 'irim006.tab:0159', 'irim006.tab:0174', 'irim006.tab:0189', 'irim006.tab:0204', 'irim006.tab:0219', 'irim006.tab:0234', 'irim006.tab:0249', 'irim006.tab:0264', 'irim006.tab:0279', 'irim006.tab:0294', 'irim006.tab:0309', 'irim006.tab:0324', 'irim006.tab:0339', 'irim006.tab:0354', 'irim006.tab:0369', 'irim006.tab:0384', 'irim006.tab:0399', 'irim006.tab:0414', 'irim006.tab:0429', 'irim006.tab:0444', 'irim006.tab:0459', 'irim006.tab:0474', 'irim006.tab:0489', 'irim006.tab:0504', 'irim006.tab:0519', 'irim006.tab:0534', 'irim006.tab:0655']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0045', 'irim006.tab:0046', 'irim006.tab:0047', 'irim006.tab:0048', 'irim006.tab:0049', 'irim006.tab:0084', 'irim006.tab:0099', 'irim006.tab:0114', 'irim006.tab:0129', 'irim006.tab:0144', 'irim006.tab:0159', 'irim006.tab:0174', 'irim006.tab:0189', 'irim006.tab:0204', 'irim006.tab:0219', 'irim006.tab:0234', 'irim006.tab:0249', 'irim006.tab:0264', 'irim006.tab:0279', 'irim006.tab:0294', 'irim006.tab:0309', 'irim006.tab:0324', 'irim006.tab:0339', 'irim006.tab:0354', 'irim006.tab:0369', 'irim006.tab:0384', 'irim006.tab:0399', 'irim006.tab:0414', 'irim006.tab:0429', 'irim006.tab:0444', 'irim006.tab:0459', 'irim006.tab:0474', 'irim006.tab:0489', 'irim006.tab:0504', 'irim006.tab:0519', 'irim006.tab:0534', 'irim006.tab:0655']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0045', 'irim006.tab:0047', 'irim006.tab:0048', 'irim006.tab:0049', 'irim006.tab:0084', 'irim006.tab:0099', 'irim006.tab:0114', 'irim006.tab:0129', 'irim006.tab:0144', 'irim006.tab:0159', 'irim006.tab:0174', 'irim006.tab:0189', 'irim006.tab:0204', 'irim006.tab:0219', 'irim006.tab:0234', 'irim006.tab:0249', 'irim006.tab:0264', 'irim006.tab:0279', 'irim006.tab:0294', 'irim006.tab:0309', 'irim006.tab:0324', 'irim006.tab:0339', 'irim006.tab:0354', 'irim006.tab:0369', 'irim006.tab:0384', 'irim006.tab:0399', 'irim006.tab:0414', 'irim006.tab:0429', 'irim006.tab:0444', 'irim006.tab:0459', 'irim006.tab:0474', 'irim006.tab:0489', 'irim006.tab:0504']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0045', 'irim006.tab:0047', 'irim006.tab:0048', 'irim006.tab:0049', 'irim006.tab:0084', 'irim006.tab:0099', 'irim006.tab:0114', 'irim006.tab:0129', 'irim006.tab:0144', 'irim006.tab:0159', 'irim006.tab:0174', 'irim006.tab:0189', 'irim006.tab:0204', 'irim006.tab:0219', 'irim006.tab:0234', 'irim006.tab:0249', 'irim006.tab:0264', 'irim006.tab:0279', 'irim006.tab:0294', 'irim006.tab:0309', 'irim006.tab:0324', 'irim006.tab:0339', 'irim006.tab:0354', 'irim006.tab:0369', 'irim006.tab:0384', 'irim006.tab:0399', 'irim006.tab:0414', 'irim006.tab:0429', 'irim006.tab:0444', 'irim006.tab:0459', 'irim006.tab:0474', 'irim006.tab:0489', 'irim006.tab:0504']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0046', 'irim006.tab:0519', 'irim006.tab:0534']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0046', 'irim006.tab:0519', 'irim006.tab:0534']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0050', 'irim006.tab:0051', 'irim006.tab:0052', 'irim006.tab:0053', 'irim006.tab:0054', 'irim006.tab:0085', 'irim006.tab:0100', 'irim006.tab:0115', 'irim006.tab:0130', 'irim006.tab:0145', 'irim006.tab:0160', 'irim006.tab:0175', 'irim006.tab:0190', 'irim006.tab:0205', 'irim006.tab:0220', 'irim006.tab:0235', 'irim006.tab:0250', 'irim006.tab:0265', 'irim006.tab:0280', 'irim006.tab:0295', 'irim006.tab:0310', 'irim006.tab:0325', 'irim006.tab:0340', 'irim006.tab:0355', 'irim006.tab:0370', 'irim006.tab:0385', 'irim006.tab:0400', 'irim006.tab:0415', 'irim006.tab:0430', 'irim006.tab:0445', 'irim006.tab:0460', 'irim006.tab:0475', 'irim006.tab:0490', 'irim006.tab:0505', 'irim006.tab:0520', 'irim006.tab:0535']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0050', 'irim006.tab:0051', 'irim006.tab:0052', 'irim006.tab:0053', 'irim006.tab:0054', 'irim006.tab:0085', 'irim006.tab:0100', 'irim006.tab:0115', 'irim006.tab:0130', 'irim006.tab:0145', 'irim006.tab:0160', 'irim006.tab:0175', 'irim006.tab:0190', 'irim006.tab:0205', 'irim006.tab:0220', 'irim006.tab:0235', 'irim006.tab:0250', 'irim006.tab:0265', 'irim006.tab:0280', 'irim006.tab:0295', 'irim006.tab:0310', 'irim006.tab:0325', 'irim006.tab:0340', 'irim006.tab:0355', 'irim006.tab:0370', 'irim006.tab:0385', 'irim006.tab:0400', 'irim006.tab:0415', 'irim006.tab:0430', 'irim006.tab:0445', 'irim006.tab:0460', 'irim006.tab:0475', 'irim006.tab:0490', 'irim006.tab:0505', 'irim006.tab:0520', 'irim006.tab:0535']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0050', 'irim006.tab:0052', 'irim006.tab:0053', 'irim006.tab:0054', 'irim006.tab:0085', 'irim006.tab:0100', 'irim006.tab:0115', 'irim006.tab:0130', 'irim006.tab:0145', 'irim006.tab:0160', 'irim006.tab:0175', 'irim006.tab:0190', 'irim006.tab:0205', 'irim006.tab:0220', 'irim006.tab:0235', 'irim006.tab:0250', 'irim006.tab:0265', 'irim006.tab:0280', 'irim006.tab:0295', 'irim006.tab:0310', 'irim006.tab:0325', 'irim006.tab:0340', 'irim006.tab:0355', 'irim006.tab:0370', 'irim006.tab:0385', 'irim006.tab:0400', 'irim006.tab:0415', 'irim006.tab:0430', 'irim006.tab:0445', 'irim006.tab:0460', 'irim006.tab:0475', 'irim006.tab:0490', 'irim006.tab:0505']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0050', 'irim006.tab:0052', 'irim006.tab:0053', 'irim006.tab:0054', 'irim006.tab:0085', 'irim006.tab:0100', 'irim006.tab:0115', 'irim006.tab:0130', 'irim006.tab:0145', 'irim006.tab:0160', 'irim006.tab:0175', 'irim006.tab:0190', 'irim006.tab:0205', 'irim006.tab:0220', 'irim006.tab:0235', 'irim006.tab:0250', 'irim006.tab:0265', 'irim006.tab:0280', 'irim006.tab:0295', 'irim006.tab:0310', 'irim006.tab:0325', 'irim006.tab:0340', 'irim006.tab:0355', 'irim006.tab:0370', 'irim006.tab:0385', 'irim006.tab:0400', 'irim006.tab:0415', 'irim006.tab:0430', 'irim006.tab:0445', 'irim006.tab:0460', 'irim006.tab:0475', 'irim006.tab:0490', 'irim006.tab:0505']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0051', 'irim006.tab:0520', 'irim006.tab:0535']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0051', 'irim006.tab:0520', 'irim006.tab:0535']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0055', 'irim006.tab:0056', 'irim006.tab:0057', 'irim006.tab:0058', 'irim006.tab:0059', 'irim006.tab:0086', 'irim006.tab:0101', 'irim006.tab:0116', 'irim006.tab:0131', 'irim006.tab:0146', 'irim006.tab:0161', 'irim006.tab:0176', 'irim006.tab:0191', 'irim006.tab:0206', 'irim006.tab:0221', 'irim006.tab:0236', 'irim006.tab:0251', 'irim006.tab:0266', 'irim006.tab:0281', 'irim006.tab:0296', 'irim006.tab:0311', 'irim006.tab:0326', 'irim006.tab:0341', 'irim006.tab:0356', 'irim006.tab:0371', 'irim006.tab:0386', 'irim006.tab:0401', 'irim006.tab:0416', 'irim006.tab:0431', 'irim006.tab:0446', 'irim006.tab:0461', 'irim006.tab:0476', 'irim006.tab:0491', 'irim006.tab:0506', 'irim006.tab:0521', 'irim006.tab:0536', 'irim006.tab:0658']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0055', 'irim006.tab:0056', 'irim006.tab:0057', 'irim006.tab:0058', 'irim006.tab:0059', 'irim006.tab:0086', 'irim006.tab:0101', 'irim006.tab:0116', 'irim006.tab:0131', 'irim006.tab:0146', 'irim006.tab:0161', 'irim006.tab:0176', 'irim006.tab:0191', 'irim006.tab:0206', 'irim006.tab:0221', 'irim006.tab:0236', 'irim006.tab:0251', 'irim006.tab:0266', 'irim006.tab:0281', 'irim006.tab:0296', 'irim006.tab:0311', 'irim006.tab:0326', 'irim006.tab:0341', 'irim006.tab:0356', 'irim006.tab:0371', 'irim006.tab:0386', 'irim006.tab:0401', 'irim006.tab:0416', 'irim006.tab:0431', 'irim006.tab:0446', 'irim006.tab:0461', 'irim006.tab:0476', 'irim006.tab:0491', 'irim006.tab:0506', 'irim006.tab:0521', 'irim006.tab:0536', 'irim006.tab:0658']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0055', 'irim006.tab:0057', 'irim006.tab:0058', 'irim006.tab:0059', 'irim006.tab:0086', 'irim006.tab:0101', 'irim006.tab:0116', 'irim006.tab:0131', 'irim006.tab:0146', 'irim006.tab:0161', 'irim006.tab:0176', 'irim006.tab:0191', 'irim006.tab:0206', 'irim006.tab:0221', 'irim006.tab:0236', 'irim006.tab:0251', 'irim006.tab:0266', 'irim006.tab:0281', 'irim006.tab:0296', 'irim006.tab:0311', 'irim006.tab:0326', 'irim006.tab:0341', 'irim006.tab:0356', 'irim006.tab:0371', 'irim006.tab:0386', 'irim006.tab:0401', 'irim006.tab:0416', 'irim006.tab:0431', 'irim006.tab:0446', 'irim006.tab:0461', 'irim006.tab:0476', 'irim006.tab:0491', 'irim006.tab:0506']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0055', 'irim006.tab:0057', 'irim006.tab:0058', 'irim006.tab:0059', 'irim006.tab:0086', 'irim006.tab:0101', 'irim006.tab:0116', 'irim006.tab:0131', 'irim006.tab:0146', 'irim006.tab:0161', 'irim006.tab:0176', 'irim006.tab:0191', 'irim006.tab:0206', 'irim006.tab:0221', 'irim006.tab:0236', 'irim006.tab:0251', 'irim006.tab:0266', 'irim006.tab:0281', 'irim006.tab:0296', 'irim006.tab:0311', 'irim006.tab:0326', 'irim006.tab:0341', 'irim006.tab:0356', 'irim006.tab:0371', 'irim006.tab:0386', 'irim006.tab:0401', 'irim006.tab:0416', 'irim006.tab:0431', 'irim006.tab:0446', 'irim006.tab:0461', 'irim006.tab:0476', 'irim006.tab:0491', 'irim006.tab:0506']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0056', 'irim006.tab:0521', 'irim006.tab:0536']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0056', 'irim006.tab:0521', 'irim006.tab:0536']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0060', 'irim006.tab:0061', 'irim006.tab:0062', 'irim006.tab:0063', 'irim006.tab:0064', 'irim006.tab:0087', 'irim006.tab:0102', 'irim006.tab:0117', 'irim006.tab:0132', 'irim006.tab:0147', 'irim006.tab:0162', 'irim006.tab:0177', 'irim006.tab:0192', 'irim006.tab:0207', 'irim006.tab:0222', 'irim006.tab:0237', 'irim006.tab:0252', 'irim006.tab:0267', 'irim006.tab:0282', 'irim006.tab:0297', 'irim006.tab:0312', 'irim006.tab:0327', 'irim006.tab:0342', 'irim006.tab:0357', 'irim006.tab:0372', 'irim006.tab:0387', 'irim006.tab:0402', 'irim006.tab:0417', 'irim006.tab:0432', 'irim006.tab:0447', 'irim006.tab:0462', 'irim006.tab:0477', 'irim006.tab:0492', 'irim006.tab:0507', 'irim006.tab:0522', 'irim006.tab:0537', 'irim006.tab:0564', 'irim006.tab:0565', 'irim006.tab:0566', 'irim006.tab:0567', 'irim006.tab:0568', 'irim006.tab:0569', 'irim006.tab:0570', 'irim006.tab:0571', 'irim006.tab:0572', 'irim006.tab:0573', 'irim006.tab:0574', 'irim006.tab:0575', 'irim006.tab:0576', 'irim006.tab:0577', 'irim006.tab:0578', 'irim006.tab:0579', 'irim006.tab:0580', 'irim006.tab:0581', 'irim006.tab:0582', 'irim006.tab:0583', 'irim006.tab:0584', 'irim006.tab:0585', 'irim006.tab:0586', 'irim006.tab:0587', 'irim006.tab:0588', 'irim006.tab:0589', 'irim006.tab:0590', 'irim006.tab:0591', 'irim006.tab:0592', 'irim006.tab:0593', 'irim006.tab:0594', 'irim006.tab:0595', 'irim006.tab:0596', 'irim006.tab:0597', 'irim006.tab:0598', 'irim006.tab:0599', 'irim006.tab:0600', 'irim006.tab:0601', 'irim006.tab:0602', 'irim006.tab:0603', 'irim006.tab:0604', 'irim006.tab:0605', 'irim006.tab:0606', 'irim006.tab:0607', 'irim006.tab:0608', 'irim006.tab:0609', 'irim006.tab:0610', 'irim006.tab:0611', 'irim006.tab:0612', 'irim006.tab:0613', 'irim006.tab:0614', 'irim006.tab:0615', 'irim006.tab:0616', 'irim006.tab:0617', 'irim006.tab:0618', 'irim006.tab:0619', 'irim006.tab:0620', 'irim006.tab:0621', 'irim006.tab:0622', 'irim006.tab:0623', 'irim006.tab:0624', 'irim006.tab:0625', 'irim006.tab:0626', 'irim006.tab:0627', 'irim006.tab:0628', 'irim006.tab:0629', 'irim006.tab:0630', 'irim006.tab:0631', 'irim006.tab:0632', 'irim006.tab:0633', 'irim006.tab:0634', 'irim006.tab:0635']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0060', 'irim006.tab:0061', 'irim006.tab:0062', 'irim006.tab:0063', 'irim006.tab:0064', 'irim006.tab:0087', 'irim006.tab:0102', 'irim006.tab:0117', 'irim006.tab:0132', 'irim006.tab:0147', 'irim006.tab:0162', 'irim006.tab:0177', 'irim006.tab:0192', 'irim006.tab:0207', 'irim006.tab:0222', 'irim006.tab:0237', 'irim006.tab:0252', 'irim006.tab:0267', 'irim006.tab:0282', 'irim006.tab:0297', 'irim006.tab:0312', 'irim006.tab:0327', 'irim006.tab:0342', 'irim006.tab:0357', 'irim006.tab:0372', 'irim006.tab:0387', 'irim006.tab:0402', 'irim006.tab:0417', 'irim006.tab:0432', 'irim006.tab:0447', 'irim006.tab:0462', 'irim006.tab:0477', 'irim006.tab:0492', 'irim006.tab:0507', 'irim006.tab:0522', 'irim006.tab:0537', 'irim006.tab:0564', 'irim006.tab:0565', 'irim006.tab:0566', 'irim006.tab:0567', 'irim006.tab:0568', 'irim006.tab:0569', 'irim006.tab:0570', 'irim006.tab:0571', 'irim006.tab:0572', 'irim006.tab:0573', 'irim006.tab:0574', 'irim006.tab:0575', 'irim006.tab:0576', 'irim006.tab:0577', 'irim006.tab:0578', 'irim006.tab:0579', 'irim006.tab:0580', 'irim006.tab:0581', 'irim006.tab:0582', 'irim006.tab:0583', 'irim006.tab:0584', 'irim006.tab:0585', 'irim006.tab:0586', 'irim006.tab:0587', 'irim006.tab:0588', 'irim006.tab:0589', 'irim006.tab:0590', 'irim006.tab:0591', 'irim006.tab:0592', 'irim006.tab:0593', 'irim006.tab:0594', 'irim006.tab:0595', 'irim006.tab:0596', 'irim006.tab:0597', 'irim006.tab:0598', 'irim006.tab:0599', 'irim006.tab:0600', 'irim006.tab:0601', 'irim006.tab:0602', 'irim006.tab:0603', 'irim006.tab:0604', 'irim006.tab:0605', 'irim006.tab:0606', 'irim006.tab:0607', 'irim006.tab:0608', 'irim006.tab:0609', 'irim006.tab:0610', 'irim006.tab:0611', 'irim006.tab:0612', 'irim006.tab:0613', 'irim006.tab:0614', 'irim006.tab:0615', 'irim006.tab:0616', 'irim006.tab:0617', 'irim006.tab:0618', 'irim006.tab:0619', 'irim006.tab:0620', 'irim006.tab:0621', 'irim006.tab:0622', 'irim006.tab:0623', 'irim006.tab:0624', 'irim006.tab:0625', 'irim006.tab:0626', 'irim006.tab:0627', 'irim006.tab:0628', 'irim006.tab:0629', 'irim006.tab:0630', 'irim006.tab:0631', 'irim006.tab:0632', 'irim006.tab:0633', 'irim006.tab:0634', 'irim006.tab:0635']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0060', 'irim006.tab:0062', 'irim006.tab:0063', 'irim006.tab:0064', 'irim006.tab:0087', 'irim006.tab:0102', 'irim006.tab:0117', 'irim006.tab:0132', 'irim006.tab:0147', 'irim006.tab:0162', 'irim006.tab:0177', 'irim006.tab:0192', 'irim006.tab:0207', 'irim006.tab:0222', 'irim006.tab:0237', 'irim006.tab:0252', 'irim006.tab:0267', 'irim006.tab:0282', 'irim006.tab:0297', 'irim006.tab:0312', 'irim006.tab:0327', 'irim006.tab:0342', 'irim006.tab:0357', 'irim006.tab:0372', 'irim006.tab:0387', 'irim006.tab:0402', 'irim006.tab:0417', 'irim006.tab:0432', 'irim006.tab:0447', 'irim006.tab:0462', 'irim006.tab:0477', 'irim006.tab:0492', 'irim006.tab:0507']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0060', 'irim006.tab:0062', 'irim006.tab:0063', 'irim006.tab:0064', 'irim006.tab:0087', 'irim006.tab:0102', 'irim006.tab:0117', 'irim006.tab:0132', 'irim006.tab:0147', 'irim006.tab:0162', 'irim006.tab:0177', 'irim006.tab:0192', 'irim006.tab:0207', 'irim006.tab:0222', 'irim006.tab:0237', 'irim006.tab:0252', 'irim006.tab:0267', 'irim006.tab:0282', 'irim006.tab:0297', 'irim006.tab:0312', 'irim006.tab:0327', 'irim006.tab:0342', 'irim006.tab:0357', 'irim006.tab:0372', 'irim006.tab:0387', 'irim006.tab:0402', 'irim006.tab:0417', 'irim006.tab:0432', 'irim006.tab:0447', 'irim006.tab:0462', 'irim006.tab:0477', 'irim006.tab:0492', 'irim006.tab:0507']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0061', 'irim006.tab:0522', 'irim006.tab:0537']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0061', 'irim006.tab:0522', 'irim006.tab:0537']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0065', 'irim006.tab:0066', 'irim006.tab:0067', 'irim006.tab:0068', 'irim006.tab:0069', 'irim006.tab:0088', 'irim006.tab:0103', 'irim006.tab:0118', 'irim006.tab:0133', 'irim006.tab:0148', 'irim006.tab:0163', 'irim006.tab:0178', 'irim006.tab:0193', 'irim006.tab:0208', 'irim006.tab:0223', 'irim006.tab:0238', 'irim006.tab:0253', 'irim006.tab:0268', 'irim006.tab:0283', 'irim006.tab:0298', 'irim006.tab:0313', 'irim006.tab:0328', 'irim006.tab:0343', 'irim006.tab:0358', 'irim006.tab:0373', 'irim006.tab:0388', 'irim006.tab:0403', 'irim006.tab:0418', 'irim006.tab:0433', 'irim006.tab:0448', 'irim006.tab:0463', 'irim006.tab:0478', 'irim006.tab:0493', 'irim006.tab:0508', 'irim006.tab:0523', 'irim006.tab:0538']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0065', 'irim006.tab:0066', 'irim006.tab:0067', 'irim006.tab:0068', 'irim006.tab:0069', 'irim006.tab:0088', 'irim006.tab:0103', 'irim006.tab:0118', 'irim006.tab:0133', 'irim006.tab:0148', 'irim006.tab:0163', 'irim006.tab:0178', 'irim006.tab:0193', 'irim006.tab:0208', 'irim006.tab:0223', 'irim006.tab:0238', 'irim006.tab:0253', 'irim006.tab:0268', 'irim006.tab:0283', 'irim006.tab:0298', 'irim006.tab:0313', 'irim006.tab:0328', 'irim006.tab:0343', 'irim006.tab:0358', 'irim006.tab:0373', 'irim006.tab:0388', 'irim006.tab:0403', 'irim006.tab:0418', 'irim006.tab:0433', 'irim006.tab:0448', 'irim006.tab:0463', 'irim006.tab:0478', 'irim006.tab:0493', 'irim006.tab:0508', 'irim006.tab:0523', 'irim006.tab:0538']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0065', 'irim006.tab:0067', 'irim006.tab:0068', 'irim006.tab:0069', 'irim006.tab:0088', 'irim006.tab:0103', 'irim006.tab:0118', 'irim006.tab:0133', 'irim006.tab:0148', 'irim006.tab:0163', 'irim006.tab:0178', 'irim006.tab:0193', 'irim006.tab:0208', 'irim006.tab:0223', 'irim006.tab:0238', 'irim006.tab:0253', 'irim006.tab:0268', 'irim006.tab:0283', 'irim006.tab:0298', 'irim006.tab:0313', 'irim006.tab:0328', 'irim006.tab:0343', 'irim006.tab:0358', 'irim006.tab:0373', 'irim006.tab:0388', 'irim006.tab:0403', 'irim006.tab:0418', 'irim006.tab:0433', 'irim006.tab:0448', 'irim006.tab:0463', 'irim006.tab:0478', 'irim006.tab:0493', 'irim006.tab:0508']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0065', 'irim006.tab:0067', 'irim006.tab:0068', 'irim006.tab:0069', 'irim006.tab:0088', 'irim006.tab:0103', 'irim006.tab:0118', 'irim006.tab:0133', 'irim006.tab:0148', 'irim006.tab:0163', 'irim006.tab:0178', 'irim006.tab:0193', 'irim006.tab:0208', 'irim006.tab:0223', 'irim006.tab:0238', 'irim006.tab:0253', 'irim006.tab:0268', 'irim006.tab:0283', 'irim006.tab:0298', 'irim006.tab:0313', 'irim006.tab:0328', 'irim006.tab:0343', 'irim006.tab:0358', 'irim006.tab:0373', 'irim006.tab:0388', 'irim006.tab:0403', 'irim006.tab:0418', 'irim006.tab:0433', 'irim006.tab:0448', 'irim006.tab:0463', 'irim006.tab:0478', 'irim006.tab:0493', 'irim006.tab:0508']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=True
        self.etcid="['irim006.tab:0066', 'irim006.tab:0523', 'irim006.tab:0538']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0066', 'irim006.tab:0523', 'irim006.tab:0538']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0070', 'irim006.tab:0071', 'irim006.tab:0072', 'irim006.tab:0073', 'irim006.tab:0074', 'irim006.tab:0089', 'irim006.tab:0104', 'irim006.tab:0119', 'irim006.tab:0134', 'irim006.tab:0149', 'irim006.tab:0164', 'irim006.tab:0179', 'irim006.tab:0194', 'irim006.tab:0209', 'irim006.tab:0224', 'irim006.tab:0239', 'irim006.tab:0254', 'irim006.tab:0269', 'irim006.tab:0284', 'irim006.tab:0299', 'irim006.tab:0314', 'irim006.tab:0329', 'irim006.tab:0344', 'irim006.tab:0359', 'irim006.tab:0374', 'irim006.tab:0389', 'irim006.tab:0404', 'irim006.tab:0419', 'irim006.tab:0434', 'irim006.tab:0449', 'irim006.tab:0464', 'irim006.tab:0479', 'irim006.tab:0494', 'irim006.tab:0509', 'irim006.tab:0524', 'irim006.tab:0539']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irim006.tab:0070', 'irim006.tab:0071', 'irim006.tab:0072', 'irim006.tab:0073', 'irim006.tab:0074', 'irim006.tab:0089', 'irim006.tab:0104', 'irim006.tab:0119', 'irim006.tab:0134', 'irim006.tab:0149', 'irim006.tab:0164', 'irim006.tab:0179', 'irim006.tab:0194', 'irim006.tab:0209', 'irim006.tab:0224', 'irim006.tab:0239', 'irim006.tab:0254', 'irim006.tab:0269', 'irim006.tab:0284', 'irim006.tab:0299', 'irim006.tab:0314', 'irim006.tab:0329', 'irim006.tab:0344', 'irim006.tab:0359', 'irim006.tab:0374', 'irim006.tab:0389', 'irim006.tab:0404', 'irim006.tab:0419', 'irim006.tab:0434', 'irim006.tab:0449', 'irim006.tab:0464', 'irim006.tab:0479', 'irim006.tab:0494', 'irim006.tab:0509', 'irim006.tab:0524', 'irim006.tab:0539']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0070', 'irim006.tab:0072', 'irim006.tab:0073', 'irim006.tab:0074', 'irim006.tab:0089', 'irim006.tab:0104', 'irim006.tab:0119', 'irim006.tab:0134', 'irim006.tab:0149', 'irim006.tab:0164', 'irim006.tab:0179', 'irim006.tab:0194', 'irim006.tab:0209', 'irim006.tab:0224', 'irim006.tab:0239', 'irim006.tab:0254', 'irim006.tab:0269', 'irim006.tab:0284', 'irim006.tab:0299', 'irim006.tab:0314', 'irim006.tab:0329', 'irim006.tab:0344', 'irim006.tab:0359', 'irim006.tab:0374', 'irim006.tab:0389', 'irim006.tab:0404', 'irim006.tab:0419', 'irim006.tab:0434', 'irim006.tab:0449', 'irim006.tab:0464', 'irim006.tab:0479', 'irim006.tab:0494', 'irim006.tab:0509']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0070', 'irim006.tab:0072', 'irim006.tab:0073', 'irim006.tab:0074', 'irim006.tab:0089', 'irim006.tab:0104', 'irim006.tab:0119', 'irim006.tab:0134', 'irim006.tab:0149', 'irim006.tab:0164', 'irim006.tab:0179', 'irim006.tab:0194', 'irim006.tab:0209', 'irim006.tab:0224', 'irim006.tab:0239', 'irim006.tab:0254', 'irim006.tab:0269', 'irim006.tab:0284', 'irim006.tab:0299', 'irim006.tab:0314', 'irim006.tab:0329', 'irim006.tab:0344', 'irim006.tab:0359', 'irim006.tab:0374', 'irim006.tab:0389', 'irim006.tab:0404', 'irim006.tab:0419', 'irim006.tab:0434', 'irim006.tab:0449', 'irim006.tab:0464', 'irim006.tab:0479', 'irim006.tab:0494', 'irim006.tab:0509']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['irim006.tab:0071', 'irim006.tab:0524', 'irim006.tab:0539']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=True
        self.etcid="['irim006.tab:0071', 'irim006.tab:0524', 'irim006.tab:0539']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase541(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0540"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0540"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase542(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase543(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0542"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0542"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase544(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0543"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0543"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase545(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0544"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0544"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0545"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0545"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase547(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8720,0.0,4.2)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0546"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0546"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase548(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8200,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase549(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0548"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0548"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase550(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0549"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0549"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase551(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6890,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0550"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0550"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase552(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0551"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0551"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase553(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0552"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0552"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase554(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase555(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0554"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0554"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase556(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0555"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0555"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase557(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5570,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0556"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0556"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase558(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5250,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0557"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0557"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase559(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4560,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0558"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0558"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase560(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4060,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase561(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0560"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0560"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase562(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0561"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0561"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase563(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,38000.,0.0,4.5)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0562"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0562"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase564(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,33000.,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0563"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0563"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0564"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="irim006.tab:0564"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0566"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0566"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0567"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0567"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0568"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0568"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0569"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0569"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0570"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0570"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0572"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0572"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0581"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0581"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0576"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0576"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0578"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0578"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0582"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0582"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0594"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0594"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0596"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0596"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="irim006.tab:0603"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0603"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0604"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="irim006.tab:0604"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0587"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0587"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0606"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0606"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="irim006.tab:0608"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0608"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0609"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="irim006.tab:0609"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0610"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0610"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0611"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0611"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="irim006.tab:0616"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0616"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0593"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="irim006.tab:0593"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0618"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0618"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0620"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0620"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0621"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0621"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0622"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0622"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0623"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irim006.tab:0623"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0624"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irim006.tab:0624"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="irim006.tab:0626"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irim006.tab:0626"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="irim006.tab:0627"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="irim006.tab:0627"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0628"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irim006.tab:0628"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0636"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0636"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0637"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0637"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0638"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0638"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0639"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0639"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0640"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0640"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0641"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0641"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0642"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0642"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0643"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0643"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase565(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0645"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0645"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0646"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0646"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0646"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0646"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0647"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0647"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0647"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0647"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0648"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0648"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0648"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0648"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0649"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0649"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0649"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0649"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0650"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0650"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0650"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0650"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase571(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="irim006.tab:0651"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0651"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0651"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0651"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0652"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0652"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0652"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0652"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0653"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irim006.tab:0653"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0653"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0653"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="irim006.tab:0654"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="irim006.tab:0654"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0654"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0654"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="irim006.tab:0655"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="irim006.tab:0655"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="irim006.tab:0656"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=True
        self.etcid="irim006.tab:0656"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0656"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0656"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0657"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="irim006.tab:0657"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0657"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=True
        self.etcid="irim006.tab:0657"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=True
        self.etcid="irim006.tab:0658"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=True
        self.etcid="irim006.tab:0658"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:573 - 547 dup =26
#thermback:0 - 0 dup =0
#calcphot:176 - 2 dup =174
#countrate:175 - 1 dup =174
#SpecSourcerateSpec:0 - 0 dup =0
