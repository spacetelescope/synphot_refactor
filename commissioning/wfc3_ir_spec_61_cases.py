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
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irsp006.tab:0000', 'irsp006.tab:0001', 'irsp006.tab:0002', 'irsp006.tab:0003', 'irsp006.tab:0004', 'irsp006.tab:0005', 'irsp006.tab:0006', 'irsp006.tab:0007', 'irsp006.tab:0008', 'irsp006.tab:0009', 'irsp006.tab:0010', 'irsp006.tab:0011', 'irsp006.tab:0012', 'irsp006.tab:0013', 'irsp006.tab:0014', 'irsp006.tab:0015', 'irsp006.tab:0016', 'irsp006.tab:0017', 'irsp006.tab:0018', 'irsp006.tab:0019', 'irsp006.tab:0020', 'irsp006.tab:0021', 'irsp006.tab:0022', 'irsp006.tab:0023', 'irsp006.tab:0024', 'irsp006.tab:0025', 'irsp006.tab:0026', 'irsp006.tab:0027', 'irsp006.tab:0028', 'irsp006.tab:0029', 'irsp006.tab:0060', 'irsp006.tab:0061', 'irsp006.tab:0062', 'irsp006.tab:0063', 'irsp006.tab:0064', 'irsp006.tab:0065', 'irsp006.tab:0072', 'irsp006.tab:0073', 'irsp006.tab:0074', 'irsp006.tab:0075', 'irsp006.tab:0076', 'irsp006.tab:0077', 'irsp006.tab:0084', 'irsp006.tab:0085', 'irsp006.tab:0086', 'irsp006.tab:0087', 'irsp006.tab:0088', 'irsp006.tab:0089', 'irsp006.tab:0096', 'irsp006.tab:0097', 'irsp006.tab:0098', 'irsp006.tab:0099', 'irsp006.tab:0100', 'irsp006.tab:0101', 'irsp006.tab:0108', 'irsp006.tab:0109', 'irsp006.tab:0110', 'irsp006.tab:0111', 'irsp006.tab:0112', 'irsp006.tab:0113', 'irsp006.tab:0120', 'irsp006.tab:0121', 'irsp006.tab:0122', 'irsp006.tab:0123', 'irsp006.tab:0124', 'irsp006.tab:0125', 'irsp006.tab:0132', 'irsp006.tab:0133', 'irsp006.tab:0134', 'irsp006.tab:0135', 'irsp006.tab:0136', 'irsp006.tab:0137', 'irsp006.tab:0144', 'irsp006.tab:0145', 'irsp006.tab:0146', 'irsp006.tab:0147', 'irsp006.tab:0148', 'irsp006.tab:0149', 'irsp006.tab:0156', 'irsp006.tab:0157', 'irsp006.tab:0158', 'irsp006.tab:0159', 'irsp006.tab:0160', 'irsp006.tab:0161', 'irsp006.tab:0168', 'irsp006.tab:0169', 'irsp006.tab:0170', 'irsp006.tab:0171', 'irsp006.tab:0172', 'irsp006.tab:0173', 'irsp006.tab:0180', 'irsp006.tab:0181', 'irsp006.tab:0182', 'irsp006.tab:0183', 'irsp006.tab:0184', 'irsp006.tab:0185', 'irsp006.tab:0192', 'irsp006.tab:0193', 'irsp006.tab:0194', 'irsp006.tab:0195', 'irsp006.tab:0196', 'irsp006.tab:0197', 'irsp006.tab:0204', 'irsp006.tab:0205', 'irsp006.tab:0206', 'irsp006.tab:0207', 'irsp006.tab:0208', 'irsp006.tab:0209', 'irsp006.tab:0216', 'irsp006.tab:0217', 'irsp006.tab:0218', 'irsp006.tab:0219', 'irsp006.tab:0220', 'irsp006.tab:0221', 'irsp006.tab:0228', 'irsp006.tab:0229', 'irsp006.tab:0230', 'irsp006.tab:0231', 'irsp006.tab:0232', 'irsp006.tab:0233', 'irsp006.tab:0240', 'irsp006.tab:0241', 'irsp006.tab:0242', 'irsp006.tab:0243', 'irsp006.tab:0244', 'irsp006.tab:0245', 'irsp006.tab:0252', 'irsp006.tab:0253', 'irsp006.tab:0254', 'irsp006.tab:0255', 'irsp006.tab:0256', 'irsp006.tab:0257', 'irsp006.tab:0272', 'irsp006.tab:0273', 'irsp006.tab:0274']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irsp006.tab:0000', 'irsp006.tab:0001', 'irsp006.tab:0002', 'irsp006.tab:0003', 'irsp006.tab:0004', 'irsp006.tab:0005', 'irsp006.tab:0006', 'irsp006.tab:0007', 'irsp006.tab:0008', 'irsp006.tab:0009', 'irsp006.tab:0010', 'irsp006.tab:0011', 'irsp006.tab:0012', 'irsp006.tab:0013', 'irsp006.tab:0014', 'irsp006.tab:0015', 'irsp006.tab:0016', 'irsp006.tab:0017', 'irsp006.tab:0018', 'irsp006.tab:0019', 'irsp006.tab:0020', 'irsp006.tab:0021', 'irsp006.tab:0022', 'irsp006.tab:0023', 'irsp006.tab:0024', 'irsp006.tab:0025', 'irsp006.tab:0026', 'irsp006.tab:0027', 'irsp006.tab:0028', 'irsp006.tab:0029', 'irsp006.tab:0060', 'irsp006.tab:0061', 'irsp006.tab:0062', 'irsp006.tab:0063', 'irsp006.tab:0064', 'irsp006.tab:0065', 'irsp006.tab:0072', 'irsp006.tab:0073', 'irsp006.tab:0074', 'irsp006.tab:0075', 'irsp006.tab:0076', 'irsp006.tab:0077', 'irsp006.tab:0084', 'irsp006.tab:0085', 'irsp006.tab:0086', 'irsp006.tab:0087', 'irsp006.tab:0088', 'irsp006.tab:0089', 'irsp006.tab:0096', 'irsp006.tab:0097', 'irsp006.tab:0098', 'irsp006.tab:0099', 'irsp006.tab:0100', 'irsp006.tab:0101', 'irsp006.tab:0108', 'irsp006.tab:0109', 'irsp006.tab:0110', 'irsp006.tab:0111', 'irsp006.tab:0112', 'irsp006.tab:0113', 'irsp006.tab:0120', 'irsp006.tab:0121', 'irsp006.tab:0122', 'irsp006.tab:0123', 'irsp006.tab:0124', 'irsp006.tab:0125', 'irsp006.tab:0132', 'irsp006.tab:0133', 'irsp006.tab:0134', 'irsp006.tab:0135', 'irsp006.tab:0136', 'irsp006.tab:0137', 'irsp006.tab:0144', 'irsp006.tab:0145', 'irsp006.tab:0146', 'irsp006.tab:0147', 'irsp006.tab:0148', 'irsp006.tab:0149', 'irsp006.tab:0156', 'irsp006.tab:0157', 'irsp006.tab:0158', 'irsp006.tab:0159', 'irsp006.tab:0160', 'irsp006.tab:0161', 'irsp006.tab:0168', 'irsp006.tab:0169', 'irsp006.tab:0170', 'irsp006.tab:0171', 'irsp006.tab:0172', 'irsp006.tab:0173', 'irsp006.tab:0180', 'irsp006.tab:0181', 'irsp006.tab:0182', 'irsp006.tab:0183', 'irsp006.tab:0184', 'irsp006.tab:0185', 'irsp006.tab:0192', 'irsp006.tab:0193', 'irsp006.tab:0194', 'irsp006.tab:0195', 'irsp006.tab:0196', 'irsp006.tab:0197', 'irsp006.tab:0204', 'irsp006.tab:0205', 'irsp006.tab:0206', 'irsp006.tab:0207', 'irsp006.tab:0208', 'irsp006.tab:0209', 'irsp006.tab:0216', 'irsp006.tab:0217', 'irsp006.tab:0218', 'irsp006.tab:0219', 'irsp006.tab:0220', 'irsp006.tab:0221', 'irsp006.tab:0228', 'irsp006.tab:0229', 'irsp006.tab:0230', 'irsp006.tab:0231', 'irsp006.tab:0232', 'irsp006.tab:0233', 'irsp006.tab:0240', 'irsp006.tab:0241', 'irsp006.tab:0242', 'irsp006.tab:0243', 'irsp006.tab:0244', 'irsp006.tab:0245', 'irsp006.tab:0252', 'irsp006.tab:0253', 'irsp006.tab:0254', 'irsp006.tab:0255', 'irsp006.tab:0256', 'irsp006.tab:0257', 'irsp006.tab:0272', 'irsp006.tab:0273', 'irsp006.tab:0274']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.subset=False
        self.etcid="['irsp006.tab:0000', 'irsp006.tab:0002', 'irsp006.tab:0003', 'irsp006.tab:0004', 'irsp006.tab:0005', 'irsp006.tab:0007', 'irsp006.tab:0008', 'irsp006.tab:0009', 'irsp006.tab:0010', 'irsp006.tab:0012', 'irsp006.tab:0013', 'irsp006.tab:0014', 'irsp006.tab:0015', 'irsp006.tab:0017', 'irsp006.tab:0018', 'irsp006.tab:0019', 'irsp006.tab:0020', 'irsp006.tab:0022', 'irsp006.tab:0023', 'irsp006.tab:0024', 'irsp006.tab:0025', 'irsp006.tab:0027', 'irsp006.tab:0028', 'irsp006.tab:0029', 'irsp006.tab:0060', 'irsp006.tab:0061', 'irsp006.tab:0062', 'irsp006.tab:0063', 'irsp006.tab:0064', 'irsp006.tab:0065', 'irsp006.tab:0072', 'irsp006.tab:0073', 'irsp006.tab:0074', 'irsp006.tab:0075', 'irsp006.tab:0076', 'irsp006.tab:0077', 'irsp006.tab:0084', 'irsp006.tab:0085', 'irsp006.tab:0086', 'irsp006.tab:0087', 'irsp006.tab:0088', 'irsp006.tab:0089', 'irsp006.tab:0096', 'irsp006.tab:0097', 'irsp006.tab:0098', 'irsp006.tab:0099', 'irsp006.tab:0100', 'irsp006.tab:0101', 'irsp006.tab:0108', 'irsp006.tab:0109', 'irsp006.tab:0110', 'irsp006.tab:0111', 'irsp006.tab:0112', 'irsp006.tab:0113', 'irsp006.tab:0120', 'irsp006.tab:0121', 'irsp006.tab:0122', 'irsp006.tab:0123', 'irsp006.tab:0124', 'irsp006.tab:0125', 'irsp006.tab:0132', 'irsp006.tab:0133', 'irsp006.tab:0134', 'irsp006.tab:0135', 'irsp006.tab:0136', 'irsp006.tab:0137', 'irsp006.tab:0144', 'irsp006.tab:0145', 'irsp006.tab:0146', 'irsp006.tab:0147', 'irsp006.tab:0148', 'irsp006.tab:0149', 'irsp006.tab:0156', 'irsp006.tab:0157', 'irsp006.tab:0158', 'irsp006.tab:0159', 'irsp006.tab:0160', 'irsp006.tab:0161', 'irsp006.tab:0168', 'irsp006.tab:0169', 'irsp006.tab:0170', 'irsp006.tab:0171', 'irsp006.tab:0172', 'irsp006.tab:0173', 'irsp006.tab:0180', 'irsp006.tab:0181', 'irsp006.tab:0182', 'irsp006.tab:0183', 'irsp006.tab:0184', 'irsp006.tab:0185', 'irsp006.tab:0192', 'irsp006.tab:0193', 'irsp006.tab:0194', 'irsp006.tab:0195', 'irsp006.tab:0196', 'irsp006.tab:0197']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.subset=False
        self.etcid="['irsp006.tab:0001', 'irsp006.tab:0006', 'irsp006.tab:0011', 'irsp006.tab:0016', 'irsp006.tab:0021', 'irsp006.tab:0026']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irsp006.tab:0030', 'irsp006.tab:0031', 'irsp006.tab:0032', 'irsp006.tab:0033', 'irsp006.tab:0034', 'irsp006.tab:0035', 'irsp006.tab:0036', 'irsp006.tab:0037', 'irsp006.tab:0038', 'irsp006.tab:0039', 'irsp006.tab:0040', 'irsp006.tab:0041', 'irsp006.tab:0042', 'irsp006.tab:0043', 'irsp006.tab:0044', 'irsp006.tab:0045', 'irsp006.tab:0046', 'irsp006.tab:0047', 'irsp006.tab:0048', 'irsp006.tab:0049', 'irsp006.tab:0050', 'irsp006.tab:0051', 'irsp006.tab:0052', 'irsp006.tab:0053', 'irsp006.tab:0054', 'irsp006.tab:0055', 'irsp006.tab:0056', 'irsp006.tab:0057', 'irsp006.tab:0058', 'irsp006.tab:0059', 'irsp006.tab:0066', 'irsp006.tab:0067', 'irsp006.tab:0068', 'irsp006.tab:0069', 'irsp006.tab:0070', 'irsp006.tab:0071', 'irsp006.tab:0078', 'irsp006.tab:0079', 'irsp006.tab:0080', 'irsp006.tab:0081', 'irsp006.tab:0082', 'irsp006.tab:0083', 'irsp006.tab:0090', 'irsp006.tab:0091', 'irsp006.tab:0092', 'irsp006.tab:0093', 'irsp006.tab:0094', 'irsp006.tab:0095', 'irsp006.tab:0102', 'irsp006.tab:0103', 'irsp006.tab:0104', 'irsp006.tab:0105', 'irsp006.tab:0106', 'irsp006.tab:0107', 'irsp006.tab:0114', 'irsp006.tab:0115', 'irsp006.tab:0116', 'irsp006.tab:0117', 'irsp006.tab:0118', 'irsp006.tab:0119', 'irsp006.tab:0126', 'irsp006.tab:0127', 'irsp006.tab:0128', 'irsp006.tab:0129', 'irsp006.tab:0130', 'irsp006.tab:0131', 'irsp006.tab:0138', 'irsp006.tab:0139', 'irsp006.tab:0140', 'irsp006.tab:0141', 'irsp006.tab:0142', 'irsp006.tab:0143', 'irsp006.tab:0150', 'irsp006.tab:0151', 'irsp006.tab:0152', 'irsp006.tab:0153', 'irsp006.tab:0154', 'irsp006.tab:0155', 'irsp006.tab:0162', 'irsp006.tab:0163', 'irsp006.tab:0164', 'irsp006.tab:0165', 'irsp006.tab:0166', 'irsp006.tab:0167', 'irsp006.tab:0174', 'irsp006.tab:0175', 'irsp006.tab:0176', 'irsp006.tab:0177', 'irsp006.tab:0178', 'irsp006.tab:0179', 'irsp006.tab:0186', 'irsp006.tab:0187', 'irsp006.tab:0188', 'irsp006.tab:0189', 'irsp006.tab:0190', 'irsp006.tab:0191', 'irsp006.tab:0198', 'irsp006.tab:0199', 'irsp006.tab:0200', 'irsp006.tab:0201', 'irsp006.tab:0202', 'irsp006.tab:0203', 'irsp006.tab:0210', 'irsp006.tab:0211', 'irsp006.tab:0212', 'irsp006.tab:0213', 'irsp006.tab:0214', 'irsp006.tab:0215', 'irsp006.tab:0222', 'irsp006.tab:0223', 'irsp006.tab:0224', 'irsp006.tab:0225', 'irsp006.tab:0226', 'irsp006.tab:0227', 'irsp006.tab:0234', 'irsp006.tab:0235', 'irsp006.tab:0236', 'irsp006.tab:0237', 'irsp006.tab:0238', 'irsp006.tab:0239', 'irsp006.tab:0246', 'irsp006.tab:0247', 'irsp006.tab:0248', 'irsp006.tab:0249', 'irsp006.tab:0250', 'irsp006.tab:0251', 'irsp006.tab:0258', 'irsp006.tab:0259', 'irsp006.tab:0260', 'irsp006.tab:0261', 'irsp006.tab:0262', 'irsp006.tab:0263', 'irsp006.tab:0264', 'irsp006.tab:0265', 'irsp006.tab:0266', 'irsp006.tab:0267', 'irsp006.tab:0268', 'irsp006.tab:0269', 'irsp006.tab:0270', 'irsp006.tab:0271', 'irsp006.tab:0275']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['irsp006.tab:0030', 'irsp006.tab:0031', 'irsp006.tab:0032', 'irsp006.tab:0033', 'irsp006.tab:0034', 'irsp006.tab:0035', 'irsp006.tab:0036', 'irsp006.tab:0037', 'irsp006.tab:0038', 'irsp006.tab:0039', 'irsp006.tab:0040', 'irsp006.tab:0041', 'irsp006.tab:0042', 'irsp006.tab:0043', 'irsp006.tab:0044', 'irsp006.tab:0045', 'irsp006.tab:0046', 'irsp006.tab:0047', 'irsp006.tab:0048', 'irsp006.tab:0049', 'irsp006.tab:0050', 'irsp006.tab:0051', 'irsp006.tab:0052', 'irsp006.tab:0053', 'irsp006.tab:0054', 'irsp006.tab:0055', 'irsp006.tab:0056', 'irsp006.tab:0057', 'irsp006.tab:0058', 'irsp006.tab:0059', 'irsp006.tab:0066', 'irsp006.tab:0067', 'irsp006.tab:0068', 'irsp006.tab:0069', 'irsp006.tab:0070', 'irsp006.tab:0071', 'irsp006.tab:0078', 'irsp006.tab:0079', 'irsp006.tab:0080', 'irsp006.tab:0081', 'irsp006.tab:0082', 'irsp006.tab:0083', 'irsp006.tab:0090', 'irsp006.tab:0091', 'irsp006.tab:0092', 'irsp006.tab:0093', 'irsp006.tab:0094', 'irsp006.tab:0095', 'irsp006.tab:0102', 'irsp006.tab:0103', 'irsp006.tab:0104', 'irsp006.tab:0105', 'irsp006.tab:0106', 'irsp006.tab:0107', 'irsp006.tab:0114', 'irsp006.tab:0115', 'irsp006.tab:0116', 'irsp006.tab:0117', 'irsp006.tab:0118', 'irsp006.tab:0119', 'irsp006.tab:0126', 'irsp006.tab:0127', 'irsp006.tab:0128', 'irsp006.tab:0129', 'irsp006.tab:0130', 'irsp006.tab:0131', 'irsp006.tab:0138', 'irsp006.tab:0139', 'irsp006.tab:0140', 'irsp006.tab:0141', 'irsp006.tab:0142', 'irsp006.tab:0143', 'irsp006.tab:0150', 'irsp006.tab:0151', 'irsp006.tab:0152', 'irsp006.tab:0153', 'irsp006.tab:0154', 'irsp006.tab:0155', 'irsp006.tab:0162', 'irsp006.tab:0163', 'irsp006.tab:0164', 'irsp006.tab:0165', 'irsp006.tab:0166', 'irsp006.tab:0167', 'irsp006.tab:0174', 'irsp006.tab:0175', 'irsp006.tab:0176', 'irsp006.tab:0177', 'irsp006.tab:0178', 'irsp006.tab:0179', 'irsp006.tab:0186', 'irsp006.tab:0187', 'irsp006.tab:0188', 'irsp006.tab:0189', 'irsp006.tab:0190', 'irsp006.tab:0191', 'irsp006.tab:0198', 'irsp006.tab:0199', 'irsp006.tab:0200', 'irsp006.tab:0201', 'irsp006.tab:0202', 'irsp006.tab:0203', 'irsp006.tab:0210', 'irsp006.tab:0211', 'irsp006.tab:0212', 'irsp006.tab:0213', 'irsp006.tab:0214', 'irsp006.tab:0215', 'irsp006.tab:0222', 'irsp006.tab:0223', 'irsp006.tab:0224', 'irsp006.tab:0225', 'irsp006.tab:0226', 'irsp006.tab:0227', 'irsp006.tab:0234', 'irsp006.tab:0235', 'irsp006.tab:0236', 'irsp006.tab:0237', 'irsp006.tab:0238', 'irsp006.tab:0239', 'irsp006.tab:0246', 'irsp006.tab:0247', 'irsp006.tab:0248', 'irsp006.tab:0249', 'irsp006.tab:0250', 'irsp006.tab:0251', 'irsp006.tab:0258', 'irsp006.tab:0259', 'irsp006.tab:0260', 'irsp006.tab:0261', 'irsp006.tab:0262', 'irsp006.tab:0263', 'irsp006.tab:0264', 'irsp006.tab:0265', 'irsp006.tab:0266', 'irsp006.tab:0267', 'irsp006.tab:0268', 'irsp006.tab:0269', 'irsp006.tab:0270', 'irsp006.tab:0271', 'irsp006.tab:0275']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.subset=False
        self.etcid="['irsp006.tab:0030', 'irsp006.tab:0032', 'irsp006.tab:0033', 'irsp006.tab:0034', 'irsp006.tab:0035', 'irsp006.tab:0037', 'irsp006.tab:0038', 'irsp006.tab:0039', 'irsp006.tab:0040', 'irsp006.tab:0042', 'irsp006.tab:0043', 'irsp006.tab:0044', 'irsp006.tab:0045', 'irsp006.tab:0047', 'irsp006.tab:0048', 'irsp006.tab:0049', 'irsp006.tab:0050', 'irsp006.tab:0052', 'irsp006.tab:0053', 'irsp006.tab:0054', 'irsp006.tab:0055', 'irsp006.tab:0057', 'irsp006.tab:0058', 'irsp006.tab:0059', 'irsp006.tab:0066', 'irsp006.tab:0067', 'irsp006.tab:0068', 'irsp006.tab:0069', 'irsp006.tab:0070', 'irsp006.tab:0071', 'irsp006.tab:0078', 'irsp006.tab:0079', 'irsp006.tab:0080', 'irsp006.tab:0081', 'irsp006.tab:0082', 'irsp006.tab:0083', 'irsp006.tab:0090', 'irsp006.tab:0091', 'irsp006.tab:0092', 'irsp006.tab:0093', 'irsp006.tab:0094', 'irsp006.tab:0095', 'irsp006.tab:0102', 'irsp006.tab:0103', 'irsp006.tab:0104', 'irsp006.tab:0105', 'irsp006.tab:0106', 'irsp006.tab:0107', 'irsp006.tab:0114', 'irsp006.tab:0115', 'irsp006.tab:0116', 'irsp006.tab:0117', 'irsp006.tab:0118', 'irsp006.tab:0119', 'irsp006.tab:0126', 'irsp006.tab:0127', 'irsp006.tab:0128', 'irsp006.tab:0129', 'irsp006.tab:0130', 'irsp006.tab:0131', 'irsp006.tab:0138', 'irsp006.tab:0139', 'irsp006.tab:0140', 'irsp006.tab:0141', 'irsp006.tab:0142', 'irsp006.tab:0143', 'irsp006.tab:0150', 'irsp006.tab:0151', 'irsp006.tab:0152', 'irsp006.tab:0153', 'irsp006.tab:0154', 'irsp006.tab:0155', 'irsp006.tab:0162', 'irsp006.tab:0163', 'irsp006.tab:0164', 'irsp006.tab:0165', 'irsp006.tab:0166', 'irsp006.tab:0167', 'irsp006.tab:0174', 'irsp006.tab:0175', 'irsp006.tab:0176', 'irsp006.tab:0177', 'irsp006.tab:0178', 'irsp006.tab:0179', 'irsp006.tab:0186', 'irsp006.tab:0187', 'irsp006.tab:0188', 'irsp006.tab:0189', 'irsp006.tab:0190', 'irsp006.tab:0191', 'irsp006.tab:0198', 'irsp006.tab:0199', 'irsp006.tab:0200', 'irsp006.tab:0201', 'irsp006.tab:0202', 'irsp006.tab:0203']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.subset=False
        self.etcid="['irsp006.tab:0031', 'irsp006.tab:0036', 'irsp006.tab:0041', 'irsp006.tab:0046', 'irsp006.tab:0051', 'irsp006.tab:0056']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.subset=False
        self.etcid="['irsp006.tab:0204', 'irsp006.tab:0205', 'irsp006.tab:0206', 'irsp006.tab:0207', 'irsp006.tab:0208', 'irsp006.tab:0209', 'irsp006.tab:0216', 'irsp006.tab:0217', 'irsp006.tab:0218', 'irsp006.tab:0219', 'irsp006.tab:0220', 'irsp006.tab:0221', 'irsp006.tab:0228', 'irsp006.tab:0229', 'irsp006.tab:0230', 'irsp006.tab:0231', 'irsp006.tab:0232', 'irsp006.tab:0233', 'irsp006.tab:0240', 'irsp006.tab:0241', 'irsp006.tab:0242', 'irsp006.tab:0243', 'irsp006.tab:0244', 'irsp006.tab:0245']"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.subset=True
        self.etcid="['irsp006.tab:0210', 'irsp006.tab:0211', 'irsp006.tab:0212', 'irsp006.tab:0213', 'irsp006.tab:0214', 'irsp006.tab:0215', 'irsp006.tab:0222', 'irsp006.tab:0223', 'irsp006.tab:0224', 'irsp006.tab:0225', 'irsp006.tab:0226', 'irsp006.tab:0227', 'irsp006.tab:0234', 'irsp006.tab:0235', 'irsp006.tab:0236', 'irsp006.tab:0237', 'irsp006.tab:0238', 'irsp006.tab:0239', 'irsp006.tab:0246', 'irsp006.tab:0247', 'irsp006.tab:0248', 'irsp006.tab:0249', 'irsp006.tab:0250', 'irsp006.tab:0251']"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase253(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.subset=True
        self.etcid="irsp006.tab:0252"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase254(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase255(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0254"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase256(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0255"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0256"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0257"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=True
        self.etcid="irsp006.tab:0258"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="irsp006.tab:0260"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="irsp006.tab:0261"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="irsp006.tab:0262"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="irsp006.tab:0263"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irsp006.tab:0264"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="irsp006.tab:0266"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="irsp006.tab:0270"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0272"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.subset=True
        self.etcid="irsp006.tab:0273"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0274"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase259(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.subset=True
        self.etcid="irsp006.tab:0275"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0276"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0276"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0276"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="irsp006.tab:0277"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0277"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0277"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0278"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0278"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0278"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0279"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="irsp006.tab:0279"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0279"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0280"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0280"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0280"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase265(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="irsp006.tab:0281"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0281"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase37(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0281"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0282"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0282"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase38(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.subset=True
        self.etcid="irsp006.tab:0282"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="irsp006.tab:0283"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="irsp006.tab:0283"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase39(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.subset=False
        self.etcid="irsp006.tab:0283"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:267 - 259 dup =8
#thermback:0 - 0 dup =0
#calcphot:11 - 1 dup =10
#countrate:11 - 1 dup =10
#SpecSourcerateSpec:39 - 1 dup =38
