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
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=True
        self.etcid="['uvim2006.tab:0000', 'uvim2006.tab:0001', 'uvim2006.tab:0002', 'uvim2006.tab:0003', 'uvim2006.tab:0004', 'uvim2006.tab:0310', 'uvim2006.tab:0372', 'uvim2006.tab:0434', 'uvim2006.tab:0496', 'uvim2006.tab:0558', 'uvim2006.tab:0620', 'uvim2006.tab:0682', 'uvim2006.tab:0744', 'uvim2006.tab:0806', 'uvim2006.tab:0868', 'uvim2006.tab:0930', 'uvim2006.tab:0992', 'uvim2006.tab:1054', 'uvim2006.tab:1116', 'uvim2006.tab:1178', 'uvim2006.tab:1240', 'uvim2006.tab:1302', 'uvim2006.tab:1364', 'uvim2006.tab:1426', 'uvim2006.tab:1488', 'uvim2006.tab:1550', 'uvim2006.tab:1612', 'uvim2006.tab:1674', 'uvim2006.tab:1736', 'uvim2006.tab:1798', 'uvim2006.tab:1860', 'uvim2006.tab:1922', 'uvim2006.tab:1984', 'uvim2006.tab:2046', 'uvim2006.tab:2108', 'uvim2006.tab:2170']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0000', 'uvim2006.tab:0001', 'uvim2006.tab:0002', 'uvim2006.tab:0003', 'uvim2006.tab:0004', 'uvim2006.tab:0310', 'uvim2006.tab:0372', 'uvim2006.tab:0434', 'uvim2006.tab:0496', 'uvim2006.tab:0558', 'uvim2006.tab:0620', 'uvim2006.tab:0682', 'uvim2006.tab:0744', 'uvim2006.tab:0806', 'uvim2006.tab:0868', 'uvim2006.tab:0930', 'uvim2006.tab:0992', 'uvim2006.tab:1054', 'uvim2006.tab:1116', 'uvim2006.tab:1178', 'uvim2006.tab:1240', 'uvim2006.tab:1302', 'uvim2006.tab:1364', 'uvim2006.tab:1426', 'uvim2006.tab:1488', 'uvim2006.tab:1550', 'uvim2006.tab:1612', 'uvim2006.tab:1674', 'uvim2006.tab:1736', 'uvim2006.tab:1798', 'uvim2006.tab:1860', 'uvim2006.tab:1922', 'uvim2006.tab:1984', 'uvim2006.tab:2046', 'uvim2006.tab:2108', 'uvim2006.tab:2170']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0000', 'uvim2006.tab:0002', 'uvim2006.tab:0003', 'uvim2006.tab:0004', 'uvim2006.tab:0310', 'uvim2006.tab:0372', 'uvim2006.tab:0434', 'uvim2006.tab:0496', 'uvim2006.tab:0558', 'uvim2006.tab:0620', 'uvim2006.tab:0682', 'uvim2006.tab:0744', 'uvim2006.tab:0806', 'uvim2006.tab:0868', 'uvim2006.tab:0930', 'uvim2006.tab:0992', 'uvim2006.tab:1054', 'uvim2006.tab:1116', 'uvim2006.tab:1178', 'uvim2006.tab:1240', 'uvim2006.tab:1302', 'uvim2006.tab:1364', 'uvim2006.tab:1426', 'uvim2006.tab:1488', 'uvim2006.tab:1550', 'uvim2006.tab:1612', 'uvim2006.tab:1674', 'uvim2006.tab:1736', 'uvim2006.tab:1798', 'uvim2006.tab:1860', 'uvim2006.tab:1922', 'uvim2006.tab:1984', 'uvim2006.tab:2046']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0000', 'uvim2006.tab:0002', 'uvim2006.tab:0003', 'uvim2006.tab:0004', 'uvim2006.tab:0310', 'uvim2006.tab:0372', 'uvim2006.tab:0434', 'uvim2006.tab:0496', 'uvim2006.tab:0558', 'uvim2006.tab:0620', 'uvim2006.tab:0682', 'uvim2006.tab:0744', 'uvim2006.tab:0806', 'uvim2006.tab:0868', 'uvim2006.tab:0930', 'uvim2006.tab:0992', 'uvim2006.tab:1054', 'uvim2006.tab:1116', 'uvim2006.tab:1178', 'uvim2006.tab:1240', 'uvim2006.tab:1302', 'uvim2006.tab:1364', 'uvim2006.tab:1426', 'uvim2006.tab:1488', 'uvim2006.tab:1550', 'uvim2006.tab:1612', 'uvim2006.tab:1674', 'uvim2006.tab:1736', 'uvim2006.tab:1798', 'uvim2006.tab:1860', 'uvim2006.tab:1922', 'uvim2006.tab:1984', 'uvim2006.tab:2046']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0001', 'uvim2006.tab:2108', 'uvim2006.tab:2170']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0001', 'uvim2006.tab:2108', 'uvim2006.tab:2170']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0005', 'uvim2006.tab:0006', 'uvim2006.tab:0007', 'uvim2006.tab:0008', 'uvim2006.tab:0009', 'uvim2006.tab:0311', 'uvim2006.tab:0373', 'uvim2006.tab:0435', 'uvim2006.tab:0497', 'uvim2006.tab:0559', 'uvim2006.tab:0621', 'uvim2006.tab:0683', 'uvim2006.tab:0745', 'uvim2006.tab:0807', 'uvim2006.tab:0869', 'uvim2006.tab:0931', 'uvim2006.tab:0993', 'uvim2006.tab:1055', 'uvim2006.tab:1117', 'uvim2006.tab:1179', 'uvim2006.tab:1241', 'uvim2006.tab:1303', 'uvim2006.tab:1365', 'uvim2006.tab:1427', 'uvim2006.tab:1489', 'uvim2006.tab:1551', 'uvim2006.tab:1613', 'uvim2006.tab:1675', 'uvim2006.tab:1737', 'uvim2006.tab:1799', 'uvim2006.tab:1861', 'uvim2006.tab:1923', 'uvim2006.tab:1985', 'uvim2006.tab:2047', 'uvim2006.tab:2109', 'uvim2006.tab:2171']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0005', 'uvim2006.tab:0006', 'uvim2006.tab:0007', 'uvim2006.tab:0008', 'uvim2006.tab:0009', 'uvim2006.tab:0311', 'uvim2006.tab:0373', 'uvim2006.tab:0435', 'uvim2006.tab:0497', 'uvim2006.tab:0559', 'uvim2006.tab:0621', 'uvim2006.tab:0683', 'uvim2006.tab:0745', 'uvim2006.tab:0807', 'uvim2006.tab:0869', 'uvim2006.tab:0931', 'uvim2006.tab:0993', 'uvim2006.tab:1055', 'uvim2006.tab:1117', 'uvim2006.tab:1179', 'uvim2006.tab:1241', 'uvim2006.tab:1303', 'uvim2006.tab:1365', 'uvim2006.tab:1427', 'uvim2006.tab:1489', 'uvim2006.tab:1551', 'uvim2006.tab:1613', 'uvim2006.tab:1675', 'uvim2006.tab:1737', 'uvim2006.tab:1799', 'uvim2006.tab:1861', 'uvim2006.tab:1923', 'uvim2006.tab:1985', 'uvim2006.tab:2047', 'uvim2006.tab:2109', 'uvim2006.tab:2171']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0005', 'uvim2006.tab:0007', 'uvim2006.tab:0008', 'uvim2006.tab:0009', 'uvim2006.tab:0311', 'uvim2006.tab:0373', 'uvim2006.tab:0435', 'uvim2006.tab:0497', 'uvim2006.tab:0559', 'uvim2006.tab:0621', 'uvim2006.tab:0683', 'uvim2006.tab:0745', 'uvim2006.tab:0807', 'uvim2006.tab:0869', 'uvim2006.tab:0931', 'uvim2006.tab:0993', 'uvim2006.tab:1055', 'uvim2006.tab:1117', 'uvim2006.tab:1179', 'uvim2006.tab:1241', 'uvim2006.tab:1303', 'uvim2006.tab:1365', 'uvim2006.tab:1427', 'uvim2006.tab:1489', 'uvim2006.tab:1551', 'uvim2006.tab:1613', 'uvim2006.tab:1675', 'uvim2006.tab:1737', 'uvim2006.tab:1799', 'uvim2006.tab:1861', 'uvim2006.tab:1923', 'uvim2006.tab:1985', 'uvim2006.tab:2047']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0005', 'uvim2006.tab:0007', 'uvim2006.tab:0008', 'uvim2006.tab:0009', 'uvim2006.tab:0311', 'uvim2006.tab:0373', 'uvim2006.tab:0435', 'uvim2006.tab:0497', 'uvim2006.tab:0559', 'uvim2006.tab:0621', 'uvim2006.tab:0683', 'uvim2006.tab:0745', 'uvim2006.tab:0807', 'uvim2006.tab:0869', 'uvim2006.tab:0931', 'uvim2006.tab:0993', 'uvim2006.tab:1055', 'uvim2006.tab:1117', 'uvim2006.tab:1179', 'uvim2006.tab:1241', 'uvim2006.tab:1303', 'uvim2006.tab:1365', 'uvim2006.tab:1427', 'uvim2006.tab:1489', 'uvim2006.tab:1551', 'uvim2006.tab:1613', 'uvim2006.tab:1675', 'uvim2006.tab:1737', 'uvim2006.tab:1799', 'uvim2006.tab:1861', 'uvim2006.tab:1923', 'uvim2006.tab:1985', 'uvim2006.tab:2047']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0006', 'uvim2006.tab:2109', 'uvim2006.tab:2171']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0006', 'uvim2006.tab:2109', 'uvim2006.tab:2171']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0010', 'uvim2006.tab:0011', 'uvim2006.tab:0012', 'uvim2006.tab:0013', 'uvim2006.tab:0014', 'uvim2006.tab:0312', 'uvim2006.tab:0374', 'uvim2006.tab:0436', 'uvim2006.tab:0498', 'uvim2006.tab:0560', 'uvim2006.tab:0622', 'uvim2006.tab:0684', 'uvim2006.tab:0746', 'uvim2006.tab:0808', 'uvim2006.tab:0870', 'uvim2006.tab:0932', 'uvim2006.tab:0994', 'uvim2006.tab:1056', 'uvim2006.tab:1118', 'uvim2006.tab:1180', 'uvim2006.tab:1242', 'uvim2006.tab:1304', 'uvim2006.tab:1366', 'uvim2006.tab:1428', 'uvim2006.tab:1490', 'uvim2006.tab:1552', 'uvim2006.tab:1614', 'uvim2006.tab:1676', 'uvim2006.tab:1738', 'uvim2006.tab:1800', 'uvim2006.tab:1862', 'uvim2006.tab:1924', 'uvim2006.tab:1986', 'uvim2006.tab:2048', 'uvim2006.tab:2110', 'uvim2006.tab:2172', 'uvim2006.tab:2369']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0010', 'uvim2006.tab:0011', 'uvim2006.tab:0012', 'uvim2006.tab:0013', 'uvim2006.tab:0014', 'uvim2006.tab:0312', 'uvim2006.tab:0374', 'uvim2006.tab:0436', 'uvim2006.tab:0498', 'uvim2006.tab:0560', 'uvim2006.tab:0622', 'uvim2006.tab:0684', 'uvim2006.tab:0746', 'uvim2006.tab:0808', 'uvim2006.tab:0870', 'uvim2006.tab:0932', 'uvim2006.tab:0994', 'uvim2006.tab:1056', 'uvim2006.tab:1118', 'uvim2006.tab:1180', 'uvim2006.tab:1242', 'uvim2006.tab:1304', 'uvim2006.tab:1366', 'uvim2006.tab:1428', 'uvim2006.tab:1490', 'uvim2006.tab:1552', 'uvim2006.tab:1614', 'uvim2006.tab:1676', 'uvim2006.tab:1738', 'uvim2006.tab:1800', 'uvim2006.tab:1862', 'uvim2006.tab:1924', 'uvim2006.tab:1986', 'uvim2006.tab:2048', 'uvim2006.tab:2110', 'uvim2006.tab:2172', 'uvim2006.tab:2369']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0010', 'uvim2006.tab:0012', 'uvim2006.tab:0013', 'uvim2006.tab:0014', 'uvim2006.tab:0312', 'uvim2006.tab:0374', 'uvim2006.tab:0436', 'uvim2006.tab:0498', 'uvim2006.tab:0560', 'uvim2006.tab:0622', 'uvim2006.tab:0684', 'uvim2006.tab:0746', 'uvim2006.tab:0808', 'uvim2006.tab:0870', 'uvim2006.tab:0932', 'uvim2006.tab:0994', 'uvim2006.tab:1056', 'uvim2006.tab:1118', 'uvim2006.tab:1180', 'uvim2006.tab:1242', 'uvim2006.tab:1304', 'uvim2006.tab:1366', 'uvim2006.tab:1428', 'uvim2006.tab:1490', 'uvim2006.tab:1552', 'uvim2006.tab:1614', 'uvim2006.tab:1676', 'uvim2006.tab:1738', 'uvim2006.tab:1800', 'uvim2006.tab:1862', 'uvim2006.tab:1924', 'uvim2006.tab:1986', 'uvim2006.tab:2048']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0010', 'uvim2006.tab:0012', 'uvim2006.tab:0013', 'uvim2006.tab:0014', 'uvim2006.tab:0312', 'uvim2006.tab:0374', 'uvim2006.tab:0436', 'uvim2006.tab:0498', 'uvim2006.tab:0560', 'uvim2006.tab:0622', 'uvim2006.tab:0684', 'uvim2006.tab:0746', 'uvim2006.tab:0808', 'uvim2006.tab:0870', 'uvim2006.tab:0932', 'uvim2006.tab:0994', 'uvim2006.tab:1056', 'uvim2006.tab:1118', 'uvim2006.tab:1180', 'uvim2006.tab:1242', 'uvim2006.tab:1304', 'uvim2006.tab:1366', 'uvim2006.tab:1428', 'uvim2006.tab:1490', 'uvim2006.tab:1552', 'uvim2006.tab:1614', 'uvim2006.tab:1676', 'uvim2006.tab:1738', 'uvim2006.tab:1800', 'uvim2006.tab:1862', 'uvim2006.tab:1924', 'uvim2006.tab:1986', 'uvim2006.tab:2048']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0011', 'uvim2006.tab:2110', 'uvim2006.tab:2172']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0011', 'uvim2006.tab:2110', 'uvim2006.tab:2172']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0015', 'uvim2006.tab:0016', 'uvim2006.tab:0017', 'uvim2006.tab:0018', 'uvim2006.tab:0019', 'uvim2006.tab:0313', 'uvim2006.tab:0375', 'uvim2006.tab:0437', 'uvim2006.tab:0499', 'uvim2006.tab:0561', 'uvim2006.tab:0623', 'uvim2006.tab:0685', 'uvim2006.tab:0747', 'uvim2006.tab:0809', 'uvim2006.tab:0871', 'uvim2006.tab:0933', 'uvim2006.tab:0995', 'uvim2006.tab:1057', 'uvim2006.tab:1119', 'uvim2006.tab:1181', 'uvim2006.tab:1243', 'uvim2006.tab:1305', 'uvim2006.tab:1367', 'uvim2006.tab:1429', 'uvim2006.tab:1491', 'uvim2006.tab:1553', 'uvim2006.tab:1615', 'uvim2006.tab:1677', 'uvim2006.tab:1739', 'uvim2006.tab:1801', 'uvim2006.tab:1863', 'uvim2006.tab:1925', 'uvim2006.tab:1987', 'uvim2006.tab:2049', 'uvim2006.tab:2111', 'uvim2006.tab:2173']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0015', 'uvim2006.tab:0016', 'uvim2006.tab:0017', 'uvim2006.tab:0018', 'uvim2006.tab:0019', 'uvim2006.tab:0313', 'uvim2006.tab:0375', 'uvim2006.tab:0437', 'uvim2006.tab:0499', 'uvim2006.tab:0561', 'uvim2006.tab:0623', 'uvim2006.tab:0685', 'uvim2006.tab:0747', 'uvim2006.tab:0809', 'uvim2006.tab:0871', 'uvim2006.tab:0933', 'uvim2006.tab:0995', 'uvim2006.tab:1057', 'uvim2006.tab:1119', 'uvim2006.tab:1181', 'uvim2006.tab:1243', 'uvim2006.tab:1305', 'uvim2006.tab:1367', 'uvim2006.tab:1429', 'uvim2006.tab:1491', 'uvim2006.tab:1553', 'uvim2006.tab:1615', 'uvim2006.tab:1677', 'uvim2006.tab:1739', 'uvim2006.tab:1801', 'uvim2006.tab:1863', 'uvim2006.tab:1925', 'uvim2006.tab:1987', 'uvim2006.tab:2049', 'uvim2006.tab:2111', 'uvim2006.tab:2173']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0015', 'uvim2006.tab:0017', 'uvim2006.tab:0018', 'uvim2006.tab:0019', 'uvim2006.tab:0313', 'uvim2006.tab:0375', 'uvim2006.tab:0437', 'uvim2006.tab:0499', 'uvim2006.tab:0561', 'uvim2006.tab:0623', 'uvim2006.tab:0685', 'uvim2006.tab:0747', 'uvim2006.tab:0809', 'uvim2006.tab:0871', 'uvim2006.tab:0933', 'uvim2006.tab:0995', 'uvim2006.tab:1057', 'uvim2006.tab:1119', 'uvim2006.tab:1181', 'uvim2006.tab:1243', 'uvim2006.tab:1305', 'uvim2006.tab:1367', 'uvim2006.tab:1429', 'uvim2006.tab:1491', 'uvim2006.tab:1553', 'uvim2006.tab:1615', 'uvim2006.tab:1677', 'uvim2006.tab:1739', 'uvim2006.tab:1801', 'uvim2006.tab:1863', 'uvim2006.tab:1925', 'uvim2006.tab:1987', 'uvim2006.tab:2049']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0015', 'uvim2006.tab:0017', 'uvim2006.tab:0018', 'uvim2006.tab:0019', 'uvim2006.tab:0313', 'uvim2006.tab:0375', 'uvim2006.tab:0437', 'uvim2006.tab:0499', 'uvim2006.tab:0561', 'uvim2006.tab:0623', 'uvim2006.tab:0685', 'uvim2006.tab:0747', 'uvim2006.tab:0809', 'uvim2006.tab:0871', 'uvim2006.tab:0933', 'uvim2006.tab:0995', 'uvim2006.tab:1057', 'uvim2006.tab:1119', 'uvim2006.tab:1181', 'uvim2006.tab:1243', 'uvim2006.tab:1305', 'uvim2006.tab:1367', 'uvim2006.tab:1429', 'uvim2006.tab:1491', 'uvim2006.tab:1553', 'uvim2006.tab:1615', 'uvim2006.tab:1677', 'uvim2006.tab:1739', 'uvim2006.tab:1801', 'uvim2006.tab:1863', 'uvim2006.tab:1925', 'uvim2006.tab:1987', 'uvim2006.tab:2049']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0016', 'uvim2006.tab:2111', 'uvim2006.tab:2173']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0016', 'uvim2006.tab:2111', 'uvim2006.tab:2173']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0020', 'uvim2006.tab:0021', 'uvim2006.tab:0022', 'uvim2006.tab:0023', 'uvim2006.tab:0024', 'uvim2006.tab:0314', 'uvim2006.tab:0376', 'uvim2006.tab:0438', 'uvim2006.tab:0500', 'uvim2006.tab:0562', 'uvim2006.tab:0624', 'uvim2006.tab:0686', 'uvim2006.tab:0748', 'uvim2006.tab:0810', 'uvim2006.tab:0872', 'uvim2006.tab:0934', 'uvim2006.tab:0996', 'uvim2006.tab:1058', 'uvim2006.tab:1120', 'uvim2006.tab:1182', 'uvim2006.tab:1244', 'uvim2006.tab:1306', 'uvim2006.tab:1368', 'uvim2006.tab:1430', 'uvim2006.tab:1492', 'uvim2006.tab:1554', 'uvim2006.tab:1616', 'uvim2006.tab:1678', 'uvim2006.tab:1740', 'uvim2006.tab:1802', 'uvim2006.tab:1864', 'uvim2006.tab:1926', 'uvim2006.tab:1988', 'uvim2006.tab:2050', 'uvim2006.tab:2112', 'uvim2006.tab:2174']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0020', 'uvim2006.tab:0021', 'uvim2006.tab:0022', 'uvim2006.tab:0023', 'uvim2006.tab:0024', 'uvim2006.tab:0314', 'uvim2006.tab:0376', 'uvim2006.tab:0438', 'uvim2006.tab:0500', 'uvim2006.tab:0562', 'uvim2006.tab:0624', 'uvim2006.tab:0686', 'uvim2006.tab:0748', 'uvim2006.tab:0810', 'uvim2006.tab:0872', 'uvim2006.tab:0934', 'uvim2006.tab:0996', 'uvim2006.tab:1058', 'uvim2006.tab:1120', 'uvim2006.tab:1182', 'uvim2006.tab:1244', 'uvim2006.tab:1306', 'uvim2006.tab:1368', 'uvim2006.tab:1430', 'uvim2006.tab:1492', 'uvim2006.tab:1554', 'uvim2006.tab:1616', 'uvim2006.tab:1678', 'uvim2006.tab:1740', 'uvim2006.tab:1802', 'uvim2006.tab:1864', 'uvim2006.tab:1926', 'uvim2006.tab:1988', 'uvim2006.tab:2050', 'uvim2006.tab:2112', 'uvim2006.tab:2174']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0020', 'uvim2006.tab:0022', 'uvim2006.tab:0023', 'uvim2006.tab:0024', 'uvim2006.tab:0314', 'uvim2006.tab:0376', 'uvim2006.tab:0438', 'uvim2006.tab:0500', 'uvim2006.tab:0562', 'uvim2006.tab:0624', 'uvim2006.tab:0686', 'uvim2006.tab:0748', 'uvim2006.tab:0810', 'uvim2006.tab:0872', 'uvim2006.tab:0934', 'uvim2006.tab:0996', 'uvim2006.tab:1058', 'uvim2006.tab:1120', 'uvim2006.tab:1182', 'uvim2006.tab:1244', 'uvim2006.tab:1306', 'uvim2006.tab:1368', 'uvim2006.tab:1430', 'uvim2006.tab:1492', 'uvim2006.tab:1554', 'uvim2006.tab:1616', 'uvim2006.tab:1678', 'uvim2006.tab:1740', 'uvim2006.tab:1802', 'uvim2006.tab:1864', 'uvim2006.tab:1926', 'uvim2006.tab:1988', 'uvim2006.tab:2050']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0020', 'uvim2006.tab:0022', 'uvim2006.tab:0023', 'uvim2006.tab:0024', 'uvim2006.tab:0314', 'uvim2006.tab:0376', 'uvim2006.tab:0438', 'uvim2006.tab:0500', 'uvim2006.tab:0562', 'uvim2006.tab:0624', 'uvim2006.tab:0686', 'uvim2006.tab:0748', 'uvim2006.tab:0810', 'uvim2006.tab:0872', 'uvim2006.tab:0934', 'uvim2006.tab:0996', 'uvim2006.tab:1058', 'uvim2006.tab:1120', 'uvim2006.tab:1182', 'uvim2006.tab:1244', 'uvim2006.tab:1306', 'uvim2006.tab:1368', 'uvim2006.tab:1430', 'uvim2006.tab:1492', 'uvim2006.tab:1554', 'uvim2006.tab:1616', 'uvim2006.tab:1678', 'uvim2006.tab:1740', 'uvim2006.tab:1802', 'uvim2006.tab:1864', 'uvim2006.tab:1926', 'uvim2006.tab:1988', 'uvim2006.tab:2050']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0021', 'uvim2006.tab:2112', 'uvim2006.tab:2174']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0021', 'uvim2006.tab:2112', 'uvim2006.tab:2174']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0025', 'uvim2006.tab:0026', 'uvim2006.tab:0027', 'uvim2006.tab:0028', 'uvim2006.tab:0029', 'uvim2006.tab:0315', 'uvim2006.tab:0377', 'uvim2006.tab:0439', 'uvim2006.tab:0501', 'uvim2006.tab:0563', 'uvim2006.tab:0625', 'uvim2006.tab:0687', 'uvim2006.tab:0749', 'uvim2006.tab:0811', 'uvim2006.tab:0873', 'uvim2006.tab:0935', 'uvim2006.tab:0997', 'uvim2006.tab:1059', 'uvim2006.tab:1121', 'uvim2006.tab:1183', 'uvim2006.tab:1245', 'uvim2006.tab:1307', 'uvim2006.tab:1369', 'uvim2006.tab:1431', 'uvim2006.tab:1493', 'uvim2006.tab:1555', 'uvim2006.tab:1617', 'uvim2006.tab:1679', 'uvim2006.tab:1741', 'uvim2006.tab:1803', 'uvim2006.tab:1865', 'uvim2006.tab:1927', 'uvim2006.tab:1989', 'uvim2006.tab:2051', 'uvim2006.tab:2113', 'uvim2006.tab:2175']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0025', 'uvim2006.tab:0026', 'uvim2006.tab:0027', 'uvim2006.tab:0028', 'uvim2006.tab:0029', 'uvim2006.tab:0315', 'uvim2006.tab:0377', 'uvim2006.tab:0439', 'uvim2006.tab:0501', 'uvim2006.tab:0563', 'uvim2006.tab:0625', 'uvim2006.tab:0687', 'uvim2006.tab:0749', 'uvim2006.tab:0811', 'uvim2006.tab:0873', 'uvim2006.tab:0935', 'uvim2006.tab:0997', 'uvim2006.tab:1059', 'uvim2006.tab:1121', 'uvim2006.tab:1183', 'uvim2006.tab:1245', 'uvim2006.tab:1307', 'uvim2006.tab:1369', 'uvim2006.tab:1431', 'uvim2006.tab:1493', 'uvim2006.tab:1555', 'uvim2006.tab:1617', 'uvim2006.tab:1679', 'uvim2006.tab:1741', 'uvim2006.tab:1803', 'uvim2006.tab:1865', 'uvim2006.tab:1927', 'uvim2006.tab:1989', 'uvim2006.tab:2051', 'uvim2006.tab:2113', 'uvim2006.tab:2175']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0025', 'uvim2006.tab:0027', 'uvim2006.tab:0028', 'uvim2006.tab:0029', 'uvim2006.tab:0315', 'uvim2006.tab:0377', 'uvim2006.tab:0439', 'uvim2006.tab:0501', 'uvim2006.tab:0563', 'uvim2006.tab:0625', 'uvim2006.tab:0687', 'uvim2006.tab:0749', 'uvim2006.tab:0811', 'uvim2006.tab:0873', 'uvim2006.tab:0935', 'uvim2006.tab:0997', 'uvim2006.tab:1059', 'uvim2006.tab:1121', 'uvim2006.tab:1183', 'uvim2006.tab:1245', 'uvim2006.tab:1307', 'uvim2006.tab:1369', 'uvim2006.tab:1431', 'uvim2006.tab:1493', 'uvim2006.tab:1555', 'uvim2006.tab:1617', 'uvim2006.tab:1679', 'uvim2006.tab:1741', 'uvim2006.tab:1803', 'uvim2006.tab:1865', 'uvim2006.tab:1927', 'uvim2006.tab:1989', 'uvim2006.tab:2051']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0025', 'uvim2006.tab:0027', 'uvim2006.tab:0028', 'uvim2006.tab:0029', 'uvim2006.tab:0315', 'uvim2006.tab:0377', 'uvim2006.tab:0439', 'uvim2006.tab:0501', 'uvim2006.tab:0563', 'uvim2006.tab:0625', 'uvim2006.tab:0687', 'uvim2006.tab:0749', 'uvim2006.tab:0811', 'uvim2006.tab:0873', 'uvim2006.tab:0935', 'uvim2006.tab:0997', 'uvim2006.tab:1059', 'uvim2006.tab:1121', 'uvim2006.tab:1183', 'uvim2006.tab:1245', 'uvim2006.tab:1307', 'uvim2006.tab:1369', 'uvim2006.tab:1431', 'uvim2006.tab:1493', 'uvim2006.tab:1555', 'uvim2006.tab:1617', 'uvim2006.tab:1679', 'uvim2006.tab:1741', 'uvim2006.tab:1803', 'uvim2006.tab:1865', 'uvim2006.tab:1927', 'uvim2006.tab:1989', 'uvim2006.tab:2051']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0026', 'uvim2006.tab:2113', 'uvim2006.tab:2175']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0026', 'uvim2006.tab:2113', 'uvim2006.tab:2175']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0030', 'uvim2006.tab:0031', 'uvim2006.tab:0032', 'uvim2006.tab:0033', 'uvim2006.tab:0034', 'uvim2006.tab:0316', 'uvim2006.tab:0378', 'uvim2006.tab:0440', 'uvim2006.tab:0502', 'uvim2006.tab:0564', 'uvim2006.tab:0626', 'uvim2006.tab:0688', 'uvim2006.tab:0750', 'uvim2006.tab:0812', 'uvim2006.tab:0874', 'uvim2006.tab:0936', 'uvim2006.tab:0998', 'uvim2006.tab:1060', 'uvim2006.tab:1122', 'uvim2006.tab:1184', 'uvim2006.tab:1246', 'uvim2006.tab:1308', 'uvim2006.tab:1370', 'uvim2006.tab:1432', 'uvim2006.tab:1494', 'uvim2006.tab:1556', 'uvim2006.tab:1618', 'uvim2006.tab:1680', 'uvim2006.tab:1742', 'uvim2006.tab:1804', 'uvim2006.tab:1866', 'uvim2006.tab:1928', 'uvim2006.tab:1990', 'uvim2006.tab:2052', 'uvim2006.tab:2114', 'uvim2006.tab:2176']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0030', 'uvim2006.tab:0031', 'uvim2006.tab:0032', 'uvim2006.tab:0033', 'uvim2006.tab:0034', 'uvim2006.tab:0316', 'uvim2006.tab:0378', 'uvim2006.tab:0440', 'uvim2006.tab:0502', 'uvim2006.tab:0564', 'uvim2006.tab:0626', 'uvim2006.tab:0688', 'uvim2006.tab:0750', 'uvim2006.tab:0812', 'uvim2006.tab:0874', 'uvim2006.tab:0936', 'uvim2006.tab:0998', 'uvim2006.tab:1060', 'uvim2006.tab:1122', 'uvim2006.tab:1184', 'uvim2006.tab:1246', 'uvim2006.tab:1308', 'uvim2006.tab:1370', 'uvim2006.tab:1432', 'uvim2006.tab:1494', 'uvim2006.tab:1556', 'uvim2006.tab:1618', 'uvim2006.tab:1680', 'uvim2006.tab:1742', 'uvim2006.tab:1804', 'uvim2006.tab:1866', 'uvim2006.tab:1928', 'uvim2006.tab:1990', 'uvim2006.tab:2052', 'uvim2006.tab:2114', 'uvim2006.tab:2176']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0030', 'uvim2006.tab:0032', 'uvim2006.tab:0033', 'uvim2006.tab:0034', 'uvim2006.tab:0316', 'uvim2006.tab:0378', 'uvim2006.tab:0440', 'uvim2006.tab:0502', 'uvim2006.tab:0564', 'uvim2006.tab:0626', 'uvim2006.tab:0688', 'uvim2006.tab:0750', 'uvim2006.tab:0812', 'uvim2006.tab:0874', 'uvim2006.tab:0936', 'uvim2006.tab:0998', 'uvim2006.tab:1060', 'uvim2006.tab:1122', 'uvim2006.tab:1184', 'uvim2006.tab:1246', 'uvim2006.tab:1308', 'uvim2006.tab:1370', 'uvim2006.tab:1432', 'uvim2006.tab:1494', 'uvim2006.tab:1556', 'uvim2006.tab:1618', 'uvim2006.tab:1680', 'uvim2006.tab:1742', 'uvim2006.tab:1804', 'uvim2006.tab:1866', 'uvim2006.tab:1928', 'uvim2006.tab:1990', 'uvim2006.tab:2052']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0030', 'uvim2006.tab:0032', 'uvim2006.tab:0033', 'uvim2006.tab:0034', 'uvim2006.tab:0316', 'uvim2006.tab:0378', 'uvim2006.tab:0440', 'uvim2006.tab:0502', 'uvim2006.tab:0564', 'uvim2006.tab:0626', 'uvim2006.tab:0688', 'uvim2006.tab:0750', 'uvim2006.tab:0812', 'uvim2006.tab:0874', 'uvim2006.tab:0936', 'uvim2006.tab:0998', 'uvim2006.tab:1060', 'uvim2006.tab:1122', 'uvim2006.tab:1184', 'uvim2006.tab:1246', 'uvim2006.tab:1308', 'uvim2006.tab:1370', 'uvim2006.tab:1432', 'uvim2006.tab:1494', 'uvim2006.tab:1556', 'uvim2006.tab:1618', 'uvim2006.tab:1680', 'uvim2006.tab:1742', 'uvim2006.tab:1804', 'uvim2006.tab:1866', 'uvim2006.tab:1928', 'uvim2006.tab:1990', 'uvim2006.tab:2052']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0031', 'uvim2006.tab:2114', 'uvim2006.tab:2176']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0031', 'uvim2006.tab:2114', 'uvim2006.tab:2176']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0035', 'uvim2006.tab:0036', 'uvim2006.tab:0037', 'uvim2006.tab:0038', 'uvim2006.tab:0039', 'uvim2006.tab:0317', 'uvim2006.tab:0379', 'uvim2006.tab:0441', 'uvim2006.tab:0503', 'uvim2006.tab:0565', 'uvim2006.tab:0627', 'uvim2006.tab:0689', 'uvim2006.tab:0751', 'uvim2006.tab:0813', 'uvim2006.tab:0875', 'uvim2006.tab:0937', 'uvim2006.tab:0999', 'uvim2006.tab:1061', 'uvim2006.tab:1123', 'uvim2006.tab:1185', 'uvim2006.tab:1247', 'uvim2006.tab:1309', 'uvim2006.tab:1371', 'uvim2006.tab:1433', 'uvim2006.tab:1495', 'uvim2006.tab:1557', 'uvim2006.tab:1619', 'uvim2006.tab:1681', 'uvim2006.tab:1743', 'uvim2006.tab:1805', 'uvim2006.tab:1867', 'uvim2006.tab:1929', 'uvim2006.tab:1991', 'uvim2006.tab:2053', 'uvim2006.tab:2115', 'uvim2006.tab:2177', 'uvim2006.tab:2356']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0035', 'uvim2006.tab:0036', 'uvim2006.tab:0037', 'uvim2006.tab:0038', 'uvim2006.tab:0039', 'uvim2006.tab:0317', 'uvim2006.tab:0379', 'uvim2006.tab:0441', 'uvim2006.tab:0503', 'uvim2006.tab:0565', 'uvim2006.tab:0627', 'uvim2006.tab:0689', 'uvim2006.tab:0751', 'uvim2006.tab:0813', 'uvim2006.tab:0875', 'uvim2006.tab:0937', 'uvim2006.tab:0999', 'uvim2006.tab:1061', 'uvim2006.tab:1123', 'uvim2006.tab:1185', 'uvim2006.tab:1247', 'uvim2006.tab:1309', 'uvim2006.tab:1371', 'uvim2006.tab:1433', 'uvim2006.tab:1495', 'uvim2006.tab:1557', 'uvim2006.tab:1619', 'uvim2006.tab:1681', 'uvim2006.tab:1743', 'uvim2006.tab:1805', 'uvim2006.tab:1867', 'uvim2006.tab:1929', 'uvim2006.tab:1991', 'uvim2006.tab:2053', 'uvim2006.tab:2115', 'uvim2006.tab:2177', 'uvim2006.tab:2356']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0035', 'uvim2006.tab:0037', 'uvim2006.tab:0038', 'uvim2006.tab:0039', 'uvim2006.tab:0317', 'uvim2006.tab:0379', 'uvim2006.tab:0441', 'uvim2006.tab:0503', 'uvim2006.tab:0565', 'uvim2006.tab:0627', 'uvim2006.tab:0689', 'uvim2006.tab:0751', 'uvim2006.tab:0813', 'uvim2006.tab:0875', 'uvim2006.tab:0937', 'uvim2006.tab:0999', 'uvim2006.tab:1061', 'uvim2006.tab:1123', 'uvim2006.tab:1185', 'uvim2006.tab:1247', 'uvim2006.tab:1309', 'uvim2006.tab:1371', 'uvim2006.tab:1433', 'uvim2006.tab:1495', 'uvim2006.tab:1557', 'uvim2006.tab:1619', 'uvim2006.tab:1681', 'uvim2006.tab:1743', 'uvim2006.tab:1805', 'uvim2006.tab:1867', 'uvim2006.tab:1929', 'uvim2006.tab:1991', 'uvim2006.tab:2053']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0035', 'uvim2006.tab:0037', 'uvim2006.tab:0038', 'uvim2006.tab:0039', 'uvim2006.tab:0317', 'uvim2006.tab:0379', 'uvim2006.tab:0441', 'uvim2006.tab:0503', 'uvim2006.tab:0565', 'uvim2006.tab:0627', 'uvim2006.tab:0689', 'uvim2006.tab:0751', 'uvim2006.tab:0813', 'uvim2006.tab:0875', 'uvim2006.tab:0937', 'uvim2006.tab:0999', 'uvim2006.tab:1061', 'uvim2006.tab:1123', 'uvim2006.tab:1185', 'uvim2006.tab:1247', 'uvim2006.tab:1309', 'uvim2006.tab:1371', 'uvim2006.tab:1433', 'uvim2006.tab:1495', 'uvim2006.tab:1557', 'uvim2006.tab:1619', 'uvim2006.tab:1681', 'uvim2006.tab:1743', 'uvim2006.tab:1805', 'uvim2006.tab:1867', 'uvim2006.tab:1929', 'uvim2006.tab:1991', 'uvim2006.tab:2053']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0036', 'uvim2006.tab:2115', 'uvim2006.tab:2177']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0036', 'uvim2006.tab:2115', 'uvim2006.tab:2177']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0040', 'uvim2006.tab:0041', 'uvim2006.tab:0042', 'uvim2006.tab:0043', 'uvim2006.tab:0044', 'uvim2006.tab:0318', 'uvim2006.tab:0380', 'uvim2006.tab:0442', 'uvim2006.tab:0504', 'uvim2006.tab:0566', 'uvim2006.tab:0628', 'uvim2006.tab:0690', 'uvim2006.tab:0752', 'uvim2006.tab:0814', 'uvim2006.tab:0876', 'uvim2006.tab:0938', 'uvim2006.tab:1000', 'uvim2006.tab:1062', 'uvim2006.tab:1124', 'uvim2006.tab:1186', 'uvim2006.tab:1248', 'uvim2006.tab:1310', 'uvim2006.tab:1372', 'uvim2006.tab:1434', 'uvim2006.tab:1496', 'uvim2006.tab:1558', 'uvim2006.tab:1620', 'uvim2006.tab:1682', 'uvim2006.tab:1744', 'uvim2006.tab:1806', 'uvim2006.tab:1868', 'uvim2006.tab:1930', 'uvim2006.tab:1992', 'uvim2006.tab:2054', 'uvim2006.tab:2116', 'uvim2006.tab:2178']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0040', 'uvim2006.tab:0041', 'uvim2006.tab:0042', 'uvim2006.tab:0043', 'uvim2006.tab:0044', 'uvim2006.tab:0318', 'uvim2006.tab:0380', 'uvim2006.tab:0442', 'uvim2006.tab:0504', 'uvim2006.tab:0566', 'uvim2006.tab:0628', 'uvim2006.tab:0690', 'uvim2006.tab:0752', 'uvim2006.tab:0814', 'uvim2006.tab:0876', 'uvim2006.tab:0938', 'uvim2006.tab:1000', 'uvim2006.tab:1062', 'uvim2006.tab:1124', 'uvim2006.tab:1186', 'uvim2006.tab:1248', 'uvim2006.tab:1310', 'uvim2006.tab:1372', 'uvim2006.tab:1434', 'uvim2006.tab:1496', 'uvim2006.tab:1558', 'uvim2006.tab:1620', 'uvim2006.tab:1682', 'uvim2006.tab:1744', 'uvim2006.tab:1806', 'uvim2006.tab:1868', 'uvim2006.tab:1930', 'uvim2006.tab:1992', 'uvim2006.tab:2054', 'uvim2006.tab:2116', 'uvim2006.tab:2178']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0040', 'uvim2006.tab:0042', 'uvim2006.tab:0043', 'uvim2006.tab:0044', 'uvim2006.tab:0318', 'uvim2006.tab:0380', 'uvim2006.tab:0442', 'uvim2006.tab:0504', 'uvim2006.tab:0566', 'uvim2006.tab:0628', 'uvim2006.tab:0690', 'uvim2006.tab:0752', 'uvim2006.tab:0814', 'uvim2006.tab:0876', 'uvim2006.tab:0938', 'uvim2006.tab:1000', 'uvim2006.tab:1062', 'uvim2006.tab:1124', 'uvim2006.tab:1186', 'uvim2006.tab:1248', 'uvim2006.tab:1310', 'uvim2006.tab:1372', 'uvim2006.tab:1434', 'uvim2006.tab:1496', 'uvim2006.tab:1558', 'uvim2006.tab:1620', 'uvim2006.tab:1682', 'uvim2006.tab:1744', 'uvim2006.tab:1806', 'uvim2006.tab:1868', 'uvim2006.tab:1930', 'uvim2006.tab:1992', 'uvim2006.tab:2054']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0040', 'uvim2006.tab:0042', 'uvim2006.tab:0043', 'uvim2006.tab:0044', 'uvim2006.tab:0318', 'uvim2006.tab:0380', 'uvim2006.tab:0442', 'uvim2006.tab:0504', 'uvim2006.tab:0566', 'uvim2006.tab:0628', 'uvim2006.tab:0690', 'uvim2006.tab:0752', 'uvim2006.tab:0814', 'uvim2006.tab:0876', 'uvim2006.tab:0938', 'uvim2006.tab:1000', 'uvim2006.tab:1062', 'uvim2006.tab:1124', 'uvim2006.tab:1186', 'uvim2006.tab:1248', 'uvim2006.tab:1310', 'uvim2006.tab:1372', 'uvim2006.tab:1434', 'uvim2006.tab:1496', 'uvim2006.tab:1558', 'uvim2006.tab:1620', 'uvim2006.tab:1682', 'uvim2006.tab:1744', 'uvim2006.tab:1806', 'uvim2006.tab:1868', 'uvim2006.tab:1930', 'uvim2006.tab:1992', 'uvim2006.tab:2054']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0041', 'uvim2006.tab:2116', 'uvim2006.tab:2178']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0041', 'uvim2006.tab:2116', 'uvim2006.tab:2178']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0045', 'uvim2006.tab:0046', 'uvim2006.tab:0047', 'uvim2006.tab:0048', 'uvim2006.tab:0049', 'uvim2006.tab:0319', 'uvim2006.tab:0381', 'uvim2006.tab:0443', 'uvim2006.tab:0505', 'uvim2006.tab:0567', 'uvim2006.tab:0629', 'uvim2006.tab:0691', 'uvim2006.tab:0753', 'uvim2006.tab:0815', 'uvim2006.tab:0877', 'uvim2006.tab:0939', 'uvim2006.tab:1001', 'uvim2006.tab:1063', 'uvim2006.tab:1125', 'uvim2006.tab:1187', 'uvim2006.tab:1249', 'uvim2006.tab:1311', 'uvim2006.tab:1373', 'uvim2006.tab:1435', 'uvim2006.tab:1497', 'uvim2006.tab:1559', 'uvim2006.tab:1621', 'uvim2006.tab:1683', 'uvim2006.tab:1745', 'uvim2006.tab:1807', 'uvim2006.tab:1869', 'uvim2006.tab:1931', 'uvim2006.tab:1993', 'uvim2006.tab:2055', 'uvim2006.tab:2117', 'uvim2006.tab:2179']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0045', 'uvim2006.tab:0046', 'uvim2006.tab:0047', 'uvim2006.tab:0048', 'uvim2006.tab:0049', 'uvim2006.tab:0319', 'uvim2006.tab:0381', 'uvim2006.tab:0443', 'uvim2006.tab:0505', 'uvim2006.tab:0567', 'uvim2006.tab:0629', 'uvim2006.tab:0691', 'uvim2006.tab:0753', 'uvim2006.tab:0815', 'uvim2006.tab:0877', 'uvim2006.tab:0939', 'uvim2006.tab:1001', 'uvim2006.tab:1063', 'uvim2006.tab:1125', 'uvim2006.tab:1187', 'uvim2006.tab:1249', 'uvim2006.tab:1311', 'uvim2006.tab:1373', 'uvim2006.tab:1435', 'uvim2006.tab:1497', 'uvim2006.tab:1559', 'uvim2006.tab:1621', 'uvim2006.tab:1683', 'uvim2006.tab:1745', 'uvim2006.tab:1807', 'uvim2006.tab:1869', 'uvim2006.tab:1931', 'uvim2006.tab:1993', 'uvim2006.tab:2055', 'uvim2006.tab:2117', 'uvim2006.tab:2179']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0045', 'uvim2006.tab:0047', 'uvim2006.tab:0048', 'uvim2006.tab:0049', 'uvim2006.tab:0319', 'uvim2006.tab:0381', 'uvim2006.tab:0443', 'uvim2006.tab:0505', 'uvim2006.tab:0567', 'uvim2006.tab:0629', 'uvim2006.tab:0691', 'uvim2006.tab:0753', 'uvim2006.tab:0815', 'uvim2006.tab:0877', 'uvim2006.tab:0939', 'uvim2006.tab:1001', 'uvim2006.tab:1063', 'uvim2006.tab:1125', 'uvim2006.tab:1187', 'uvim2006.tab:1249', 'uvim2006.tab:1311', 'uvim2006.tab:1373', 'uvim2006.tab:1435', 'uvim2006.tab:1497', 'uvim2006.tab:1559', 'uvim2006.tab:1621', 'uvim2006.tab:1683', 'uvim2006.tab:1745', 'uvim2006.tab:1807', 'uvim2006.tab:1869', 'uvim2006.tab:1931', 'uvim2006.tab:1993', 'uvim2006.tab:2055']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0045', 'uvim2006.tab:0047', 'uvim2006.tab:0048', 'uvim2006.tab:0049', 'uvim2006.tab:0319', 'uvim2006.tab:0381', 'uvim2006.tab:0443', 'uvim2006.tab:0505', 'uvim2006.tab:0567', 'uvim2006.tab:0629', 'uvim2006.tab:0691', 'uvim2006.tab:0753', 'uvim2006.tab:0815', 'uvim2006.tab:0877', 'uvim2006.tab:0939', 'uvim2006.tab:1001', 'uvim2006.tab:1063', 'uvim2006.tab:1125', 'uvim2006.tab:1187', 'uvim2006.tab:1249', 'uvim2006.tab:1311', 'uvim2006.tab:1373', 'uvim2006.tab:1435', 'uvim2006.tab:1497', 'uvim2006.tab:1559', 'uvim2006.tab:1621', 'uvim2006.tab:1683', 'uvim2006.tab:1745', 'uvim2006.tab:1807', 'uvim2006.tab:1869', 'uvim2006.tab:1931', 'uvim2006.tab:1993', 'uvim2006.tab:2055']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0046', 'uvim2006.tab:2117', 'uvim2006.tab:2179']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0046', 'uvim2006.tab:2117', 'uvim2006.tab:2179']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0050', 'uvim2006.tab:0051', 'uvim2006.tab:0052', 'uvim2006.tab:0053', 'uvim2006.tab:0054', 'uvim2006.tab:0320', 'uvim2006.tab:0382', 'uvim2006.tab:0444', 'uvim2006.tab:0506', 'uvim2006.tab:0568', 'uvim2006.tab:0630', 'uvim2006.tab:0692', 'uvim2006.tab:0754', 'uvim2006.tab:0816', 'uvim2006.tab:0878', 'uvim2006.tab:0940', 'uvim2006.tab:1002', 'uvim2006.tab:1064', 'uvim2006.tab:1126', 'uvim2006.tab:1188', 'uvim2006.tab:1250', 'uvim2006.tab:1312', 'uvim2006.tab:1374', 'uvim2006.tab:1436', 'uvim2006.tab:1498', 'uvim2006.tab:1560', 'uvim2006.tab:1622', 'uvim2006.tab:1684', 'uvim2006.tab:1746', 'uvim2006.tab:1808', 'uvim2006.tab:1870', 'uvim2006.tab:1932', 'uvim2006.tab:1994', 'uvim2006.tab:2056', 'uvim2006.tab:2118', 'uvim2006.tab:2180']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0050', 'uvim2006.tab:0051', 'uvim2006.tab:0052', 'uvim2006.tab:0053', 'uvim2006.tab:0054', 'uvim2006.tab:0320', 'uvim2006.tab:0382', 'uvim2006.tab:0444', 'uvim2006.tab:0506', 'uvim2006.tab:0568', 'uvim2006.tab:0630', 'uvim2006.tab:0692', 'uvim2006.tab:0754', 'uvim2006.tab:0816', 'uvim2006.tab:0878', 'uvim2006.tab:0940', 'uvim2006.tab:1002', 'uvim2006.tab:1064', 'uvim2006.tab:1126', 'uvim2006.tab:1188', 'uvim2006.tab:1250', 'uvim2006.tab:1312', 'uvim2006.tab:1374', 'uvim2006.tab:1436', 'uvim2006.tab:1498', 'uvim2006.tab:1560', 'uvim2006.tab:1622', 'uvim2006.tab:1684', 'uvim2006.tab:1746', 'uvim2006.tab:1808', 'uvim2006.tab:1870', 'uvim2006.tab:1932', 'uvim2006.tab:1994', 'uvim2006.tab:2056', 'uvim2006.tab:2118', 'uvim2006.tab:2180']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0050', 'uvim2006.tab:0052', 'uvim2006.tab:0053', 'uvim2006.tab:0054', 'uvim2006.tab:0320', 'uvim2006.tab:0382', 'uvim2006.tab:0444', 'uvim2006.tab:0506', 'uvim2006.tab:0568', 'uvim2006.tab:0630', 'uvim2006.tab:0692', 'uvim2006.tab:0754', 'uvim2006.tab:0816', 'uvim2006.tab:0878', 'uvim2006.tab:0940', 'uvim2006.tab:1002', 'uvim2006.tab:1064', 'uvim2006.tab:1126', 'uvim2006.tab:1188', 'uvim2006.tab:1250', 'uvim2006.tab:1312', 'uvim2006.tab:1374', 'uvim2006.tab:1436', 'uvim2006.tab:1498', 'uvim2006.tab:1560', 'uvim2006.tab:1622', 'uvim2006.tab:1684', 'uvim2006.tab:1746', 'uvim2006.tab:1808', 'uvim2006.tab:1870', 'uvim2006.tab:1932', 'uvim2006.tab:1994', 'uvim2006.tab:2056']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=True
        self.etcid="['uvim2006.tab:0050', 'uvim2006.tab:0052', 'uvim2006.tab:0053', 'uvim2006.tab:0054', 'uvim2006.tab:0320', 'uvim2006.tab:0382', 'uvim2006.tab:0444', 'uvim2006.tab:0506', 'uvim2006.tab:0568', 'uvim2006.tab:0630', 'uvim2006.tab:0692', 'uvim2006.tab:0754', 'uvim2006.tab:0816', 'uvim2006.tab:0878', 'uvim2006.tab:0940', 'uvim2006.tab:1002', 'uvim2006.tab:1064', 'uvim2006.tab:1126', 'uvim2006.tab:1188', 'uvim2006.tab:1250', 'uvim2006.tab:1312', 'uvim2006.tab:1374', 'uvim2006.tab:1436', 'uvim2006.tab:1498', 'uvim2006.tab:1560', 'uvim2006.tab:1622', 'uvim2006.tab:1684', 'uvim2006.tab:1746', 'uvim2006.tab:1808', 'uvim2006.tab:1870', 'uvim2006.tab:1932', 'uvim2006.tab:1994', 'uvim2006.tab:2056']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0051', 'uvim2006.tab:2118', 'uvim2006.tab:2180']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0051', 'uvim2006.tab:2118', 'uvim2006.tab:2180']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0055', 'uvim2006.tab:0056', 'uvim2006.tab:0057', 'uvim2006.tab:0058', 'uvim2006.tab:0059', 'uvim2006.tab:0321', 'uvim2006.tab:0383', 'uvim2006.tab:0445', 'uvim2006.tab:0507', 'uvim2006.tab:0569', 'uvim2006.tab:0631', 'uvim2006.tab:0693', 'uvim2006.tab:0755', 'uvim2006.tab:0817', 'uvim2006.tab:0879', 'uvim2006.tab:0941', 'uvim2006.tab:1003', 'uvim2006.tab:1065', 'uvim2006.tab:1127', 'uvim2006.tab:1189', 'uvim2006.tab:1251', 'uvim2006.tab:1313', 'uvim2006.tab:1375', 'uvim2006.tab:1437', 'uvim2006.tab:1499', 'uvim2006.tab:1561', 'uvim2006.tab:1623', 'uvim2006.tab:1685', 'uvim2006.tab:1747', 'uvim2006.tab:1809', 'uvim2006.tab:1871', 'uvim2006.tab:1933', 'uvim2006.tab:1995', 'uvim2006.tab:2057', 'uvim2006.tab:2119', 'uvim2006.tab:2181']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0055', 'uvim2006.tab:0056', 'uvim2006.tab:0057', 'uvim2006.tab:0058', 'uvim2006.tab:0059', 'uvim2006.tab:0321', 'uvim2006.tab:0383', 'uvim2006.tab:0445', 'uvim2006.tab:0507', 'uvim2006.tab:0569', 'uvim2006.tab:0631', 'uvim2006.tab:0693', 'uvim2006.tab:0755', 'uvim2006.tab:0817', 'uvim2006.tab:0879', 'uvim2006.tab:0941', 'uvim2006.tab:1003', 'uvim2006.tab:1065', 'uvim2006.tab:1127', 'uvim2006.tab:1189', 'uvim2006.tab:1251', 'uvim2006.tab:1313', 'uvim2006.tab:1375', 'uvim2006.tab:1437', 'uvim2006.tab:1499', 'uvim2006.tab:1561', 'uvim2006.tab:1623', 'uvim2006.tab:1685', 'uvim2006.tab:1747', 'uvim2006.tab:1809', 'uvim2006.tab:1871', 'uvim2006.tab:1933', 'uvim2006.tab:1995', 'uvim2006.tab:2057', 'uvim2006.tab:2119', 'uvim2006.tab:2181']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0055', 'uvim2006.tab:0057', 'uvim2006.tab:0058', 'uvim2006.tab:0059', 'uvim2006.tab:0321', 'uvim2006.tab:0383', 'uvim2006.tab:0445', 'uvim2006.tab:0507', 'uvim2006.tab:0569', 'uvim2006.tab:0631', 'uvim2006.tab:0693', 'uvim2006.tab:0755', 'uvim2006.tab:0817', 'uvim2006.tab:0879', 'uvim2006.tab:0941', 'uvim2006.tab:1003', 'uvim2006.tab:1065', 'uvim2006.tab:1127', 'uvim2006.tab:1189', 'uvim2006.tab:1251', 'uvim2006.tab:1313', 'uvim2006.tab:1375', 'uvim2006.tab:1437', 'uvim2006.tab:1499', 'uvim2006.tab:1561', 'uvim2006.tab:1623', 'uvim2006.tab:1685', 'uvim2006.tab:1747', 'uvim2006.tab:1809', 'uvim2006.tab:1871', 'uvim2006.tab:1933', 'uvim2006.tab:1995', 'uvim2006.tab:2057']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0055', 'uvim2006.tab:0057', 'uvim2006.tab:0058', 'uvim2006.tab:0059', 'uvim2006.tab:0321', 'uvim2006.tab:0383', 'uvim2006.tab:0445', 'uvim2006.tab:0507', 'uvim2006.tab:0569', 'uvim2006.tab:0631', 'uvim2006.tab:0693', 'uvim2006.tab:0755', 'uvim2006.tab:0817', 'uvim2006.tab:0879', 'uvim2006.tab:0941', 'uvim2006.tab:1003', 'uvim2006.tab:1065', 'uvim2006.tab:1127', 'uvim2006.tab:1189', 'uvim2006.tab:1251', 'uvim2006.tab:1313', 'uvim2006.tab:1375', 'uvim2006.tab:1437', 'uvim2006.tab:1499', 'uvim2006.tab:1561', 'uvim2006.tab:1623', 'uvim2006.tab:1685', 'uvim2006.tab:1747', 'uvim2006.tab:1809', 'uvim2006.tab:1871', 'uvim2006.tab:1933', 'uvim2006.tab:1995', 'uvim2006.tab:2057']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0056', 'uvim2006.tab:2119', 'uvim2006.tab:2181']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0056', 'uvim2006.tab:2119', 'uvim2006.tab:2181']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0060', 'uvim2006.tab:0061', 'uvim2006.tab:0062', 'uvim2006.tab:0063', 'uvim2006.tab:0064', 'uvim2006.tab:0322', 'uvim2006.tab:0384', 'uvim2006.tab:0446', 'uvim2006.tab:0508', 'uvim2006.tab:0570', 'uvim2006.tab:0632', 'uvim2006.tab:0694', 'uvim2006.tab:0756', 'uvim2006.tab:0818', 'uvim2006.tab:0880', 'uvim2006.tab:0942', 'uvim2006.tab:1004', 'uvim2006.tab:1066', 'uvim2006.tab:1128', 'uvim2006.tab:1190', 'uvim2006.tab:1252', 'uvim2006.tab:1314', 'uvim2006.tab:1376', 'uvim2006.tab:1438', 'uvim2006.tab:1500', 'uvim2006.tab:1562', 'uvim2006.tab:1624', 'uvim2006.tab:1686', 'uvim2006.tab:1748', 'uvim2006.tab:1810', 'uvim2006.tab:1872', 'uvim2006.tab:1934', 'uvim2006.tab:1996', 'uvim2006.tab:2058', 'uvim2006.tab:2120', 'uvim2006.tab:2182']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0060', 'uvim2006.tab:0061', 'uvim2006.tab:0062', 'uvim2006.tab:0063', 'uvim2006.tab:0064', 'uvim2006.tab:0322', 'uvim2006.tab:0384', 'uvim2006.tab:0446', 'uvim2006.tab:0508', 'uvim2006.tab:0570', 'uvim2006.tab:0632', 'uvim2006.tab:0694', 'uvim2006.tab:0756', 'uvim2006.tab:0818', 'uvim2006.tab:0880', 'uvim2006.tab:0942', 'uvim2006.tab:1004', 'uvim2006.tab:1066', 'uvim2006.tab:1128', 'uvim2006.tab:1190', 'uvim2006.tab:1252', 'uvim2006.tab:1314', 'uvim2006.tab:1376', 'uvim2006.tab:1438', 'uvim2006.tab:1500', 'uvim2006.tab:1562', 'uvim2006.tab:1624', 'uvim2006.tab:1686', 'uvim2006.tab:1748', 'uvim2006.tab:1810', 'uvim2006.tab:1872', 'uvim2006.tab:1934', 'uvim2006.tab:1996', 'uvim2006.tab:2058', 'uvim2006.tab:2120', 'uvim2006.tab:2182']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0060', 'uvim2006.tab:0062', 'uvim2006.tab:0063', 'uvim2006.tab:0064', 'uvim2006.tab:0322', 'uvim2006.tab:0384', 'uvim2006.tab:0446', 'uvim2006.tab:0508', 'uvim2006.tab:0570', 'uvim2006.tab:0632', 'uvim2006.tab:0694', 'uvim2006.tab:0756', 'uvim2006.tab:0818', 'uvim2006.tab:0880', 'uvim2006.tab:0942', 'uvim2006.tab:1004', 'uvim2006.tab:1066', 'uvim2006.tab:1128', 'uvim2006.tab:1190', 'uvim2006.tab:1252', 'uvim2006.tab:1314', 'uvim2006.tab:1376', 'uvim2006.tab:1438', 'uvim2006.tab:1500', 'uvim2006.tab:1562', 'uvim2006.tab:1624', 'uvim2006.tab:1686', 'uvim2006.tab:1748', 'uvim2006.tab:1810', 'uvim2006.tab:1872', 'uvim2006.tab:1934', 'uvim2006.tab:1996', 'uvim2006.tab:2058']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0060', 'uvim2006.tab:0062', 'uvim2006.tab:0063', 'uvim2006.tab:0064', 'uvim2006.tab:0322', 'uvim2006.tab:0384', 'uvim2006.tab:0446', 'uvim2006.tab:0508', 'uvim2006.tab:0570', 'uvim2006.tab:0632', 'uvim2006.tab:0694', 'uvim2006.tab:0756', 'uvim2006.tab:0818', 'uvim2006.tab:0880', 'uvim2006.tab:0942', 'uvim2006.tab:1004', 'uvim2006.tab:1066', 'uvim2006.tab:1128', 'uvim2006.tab:1190', 'uvim2006.tab:1252', 'uvim2006.tab:1314', 'uvim2006.tab:1376', 'uvim2006.tab:1438', 'uvim2006.tab:1500', 'uvim2006.tab:1562', 'uvim2006.tab:1624', 'uvim2006.tab:1686', 'uvim2006.tab:1748', 'uvim2006.tab:1810', 'uvim2006.tab:1872', 'uvim2006.tab:1934', 'uvim2006.tab:1996', 'uvim2006.tab:2058']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0061', 'uvim2006.tab:2120', 'uvim2006.tab:2182']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0061', 'uvim2006.tab:2120', 'uvim2006.tab:2182']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0065', 'uvim2006.tab:0066', 'uvim2006.tab:0067', 'uvim2006.tab:0068', 'uvim2006.tab:0069', 'uvim2006.tab:0323', 'uvim2006.tab:0385', 'uvim2006.tab:0447', 'uvim2006.tab:0509', 'uvim2006.tab:0571', 'uvim2006.tab:0633', 'uvim2006.tab:0695', 'uvim2006.tab:0757', 'uvim2006.tab:0819', 'uvim2006.tab:0881', 'uvim2006.tab:0943', 'uvim2006.tab:1005', 'uvim2006.tab:1067', 'uvim2006.tab:1129', 'uvim2006.tab:1191', 'uvim2006.tab:1253', 'uvim2006.tab:1315', 'uvim2006.tab:1377', 'uvim2006.tab:1439', 'uvim2006.tab:1501', 'uvim2006.tab:1563', 'uvim2006.tab:1625', 'uvim2006.tab:1687', 'uvim2006.tab:1749', 'uvim2006.tab:1811', 'uvim2006.tab:1873', 'uvim2006.tab:1935', 'uvim2006.tab:1997', 'uvim2006.tab:2059', 'uvim2006.tab:2121', 'uvim2006.tab:2183']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0065', 'uvim2006.tab:0066', 'uvim2006.tab:0067', 'uvim2006.tab:0068', 'uvim2006.tab:0069', 'uvim2006.tab:0323', 'uvim2006.tab:0385', 'uvim2006.tab:0447', 'uvim2006.tab:0509', 'uvim2006.tab:0571', 'uvim2006.tab:0633', 'uvim2006.tab:0695', 'uvim2006.tab:0757', 'uvim2006.tab:0819', 'uvim2006.tab:0881', 'uvim2006.tab:0943', 'uvim2006.tab:1005', 'uvim2006.tab:1067', 'uvim2006.tab:1129', 'uvim2006.tab:1191', 'uvim2006.tab:1253', 'uvim2006.tab:1315', 'uvim2006.tab:1377', 'uvim2006.tab:1439', 'uvim2006.tab:1501', 'uvim2006.tab:1563', 'uvim2006.tab:1625', 'uvim2006.tab:1687', 'uvim2006.tab:1749', 'uvim2006.tab:1811', 'uvim2006.tab:1873', 'uvim2006.tab:1935', 'uvim2006.tab:1997', 'uvim2006.tab:2059', 'uvim2006.tab:2121', 'uvim2006.tab:2183']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0065', 'uvim2006.tab:0067', 'uvim2006.tab:0068', 'uvim2006.tab:0069', 'uvim2006.tab:0323', 'uvim2006.tab:0385', 'uvim2006.tab:0447', 'uvim2006.tab:0509', 'uvim2006.tab:0571', 'uvim2006.tab:0633', 'uvim2006.tab:0695', 'uvim2006.tab:0757', 'uvim2006.tab:0819', 'uvim2006.tab:0881', 'uvim2006.tab:0943', 'uvim2006.tab:1005', 'uvim2006.tab:1067', 'uvim2006.tab:1129', 'uvim2006.tab:1191', 'uvim2006.tab:1253', 'uvim2006.tab:1315', 'uvim2006.tab:1377', 'uvim2006.tab:1439', 'uvim2006.tab:1501', 'uvim2006.tab:1563', 'uvim2006.tab:1625', 'uvim2006.tab:1687', 'uvim2006.tab:1749', 'uvim2006.tab:1811', 'uvim2006.tab:1873', 'uvim2006.tab:1935', 'uvim2006.tab:1997', 'uvim2006.tab:2059']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0065', 'uvim2006.tab:0067', 'uvim2006.tab:0068', 'uvim2006.tab:0069', 'uvim2006.tab:0323', 'uvim2006.tab:0385', 'uvim2006.tab:0447', 'uvim2006.tab:0509', 'uvim2006.tab:0571', 'uvim2006.tab:0633', 'uvim2006.tab:0695', 'uvim2006.tab:0757', 'uvim2006.tab:0819', 'uvim2006.tab:0881', 'uvim2006.tab:0943', 'uvim2006.tab:1005', 'uvim2006.tab:1067', 'uvim2006.tab:1129', 'uvim2006.tab:1191', 'uvim2006.tab:1253', 'uvim2006.tab:1315', 'uvim2006.tab:1377', 'uvim2006.tab:1439', 'uvim2006.tab:1501', 'uvim2006.tab:1563', 'uvim2006.tab:1625', 'uvim2006.tab:1687', 'uvim2006.tab:1749', 'uvim2006.tab:1811', 'uvim2006.tab:1873', 'uvim2006.tab:1935', 'uvim2006.tab:1997', 'uvim2006.tab:2059']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0066', 'uvim2006.tab:2121', 'uvim2006.tab:2183']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0066', 'uvim2006.tab:2121', 'uvim2006.tab:2183']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0070', 'uvim2006.tab:0071', 'uvim2006.tab:0072', 'uvim2006.tab:0073', 'uvim2006.tab:0074', 'uvim2006.tab:0324', 'uvim2006.tab:0386', 'uvim2006.tab:0448', 'uvim2006.tab:0510', 'uvim2006.tab:0572', 'uvim2006.tab:0634', 'uvim2006.tab:0696', 'uvim2006.tab:0758', 'uvim2006.tab:0820', 'uvim2006.tab:0882', 'uvim2006.tab:0944', 'uvim2006.tab:1006', 'uvim2006.tab:1068', 'uvim2006.tab:1130', 'uvim2006.tab:1192', 'uvim2006.tab:1254', 'uvim2006.tab:1316', 'uvim2006.tab:1378', 'uvim2006.tab:1440', 'uvim2006.tab:1502', 'uvim2006.tab:1564', 'uvim2006.tab:1626', 'uvim2006.tab:1688', 'uvim2006.tab:1750', 'uvim2006.tab:1812', 'uvim2006.tab:1874', 'uvim2006.tab:1936', 'uvim2006.tab:1998', 'uvim2006.tab:2060', 'uvim2006.tab:2122', 'uvim2006.tab:2184']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0070', 'uvim2006.tab:0071', 'uvim2006.tab:0072', 'uvim2006.tab:0073', 'uvim2006.tab:0074', 'uvim2006.tab:0324', 'uvim2006.tab:0386', 'uvim2006.tab:0448', 'uvim2006.tab:0510', 'uvim2006.tab:0572', 'uvim2006.tab:0634', 'uvim2006.tab:0696', 'uvim2006.tab:0758', 'uvim2006.tab:0820', 'uvim2006.tab:0882', 'uvim2006.tab:0944', 'uvim2006.tab:1006', 'uvim2006.tab:1068', 'uvim2006.tab:1130', 'uvim2006.tab:1192', 'uvim2006.tab:1254', 'uvim2006.tab:1316', 'uvim2006.tab:1378', 'uvim2006.tab:1440', 'uvim2006.tab:1502', 'uvim2006.tab:1564', 'uvim2006.tab:1626', 'uvim2006.tab:1688', 'uvim2006.tab:1750', 'uvim2006.tab:1812', 'uvim2006.tab:1874', 'uvim2006.tab:1936', 'uvim2006.tab:1998', 'uvim2006.tab:2060', 'uvim2006.tab:2122', 'uvim2006.tab:2184']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0070', 'uvim2006.tab:0072', 'uvim2006.tab:0073', 'uvim2006.tab:0074', 'uvim2006.tab:0324', 'uvim2006.tab:0386', 'uvim2006.tab:0448', 'uvim2006.tab:0510', 'uvim2006.tab:0572', 'uvim2006.tab:0634', 'uvim2006.tab:0696', 'uvim2006.tab:0758', 'uvim2006.tab:0820', 'uvim2006.tab:0882', 'uvim2006.tab:0944', 'uvim2006.tab:1006', 'uvim2006.tab:1068', 'uvim2006.tab:1130', 'uvim2006.tab:1192', 'uvim2006.tab:1254', 'uvim2006.tab:1316', 'uvim2006.tab:1378', 'uvim2006.tab:1440', 'uvim2006.tab:1502', 'uvim2006.tab:1564', 'uvim2006.tab:1626', 'uvim2006.tab:1688', 'uvim2006.tab:1750', 'uvim2006.tab:1812', 'uvim2006.tab:1874', 'uvim2006.tab:1936', 'uvim2006.tab:1998', 'uvim2006.tab:2060']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0070', 'uvim2006.tab:0072', 'uvim2006.tab:0073', 'uvim2006.tab:0074', 'uvim2006.tab:0324', 'uvim2006.tab:0386', 'uvim2006.tab:0448', 'uvim2006.tab:0510', 'uvim2006.tab:0572', 'uvim2006.tab:0634', 'uvim2006.tab:0696', 'uvim2006.tab:0758', 'uvim2006.tab:0820', 'uvim2006.tab:0882', 'uvim2006.tab:0944', 'uvim2006.tab:1006', 'uvim2006.tab:1068', 'uvim2006.tab:1130', 'uvim2006.tab:1192', 'uvim2006.tab:1254', 'uvim2006.tab:1316', 'uvim2006.tab:1378', 'uvim2006.tab:1440', 'uvim2006.tab:1502', 'uvim2006.tab:1564', 'uvim2006.tab:1626', 'uvim2006.tab:1688', 'uvim2006.tab:1750', 'uvim2006.tab:1812', 'uvim2006.tab:1874', 'uvim2006.tab:1936', 'uvim2006.tab:1998', 'uvim2006.tab:2060']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0071', 'uvim2006.tab:2122', 'uvim2006.tab:2184']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0071', 'uvim2006.tab:2122', 'uvim2006.tab:2184']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0075', 'uvim2006.tab:0076', 'uvim2006.tab:0077', 'uvim2006.tab:0078', 'uvim2006.tab:0079', 'uvim2006.tab:0325', 'uvim2006.tab:0387', 'uvim2006.tab:0449', 'uvim2006.tab:0511', 'uvim2006.tab:0573', 'uvim2006.tab:0635', 'uvim2006.tab:0697', 'uvim2006.tab:0759', 'uvim2006.tab:0821', 'uvim2006.tab:0883', 'uvim2006.tab:0945', 'uvim2006.tab:1007', 'uvim2006.tab:1069', 'uvim2006.tab:1131', 'uvim2006.tab:1193', 'uvim2006.tab:1255', 'uvim2006.tab:1317', 'uvim2006.tab:1379', 'uvim2006.tab:1441', 'uvim2006.tab:1503', 'uvim2006.tab:1565', 'uvim2006.tab:1627', 'uvim2006.tab:1689', 'uvim2006.tab:1751', 'uvim2006.tab:1813', 'uvim2006.tab:1875', 'uvim2006.tab:1937', 'uvim2006.tab:1999', 'uvim2006.tab:2061', 'uvim2006.tab:2123', 'uvim2006.tab:2185']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0075', 'uvim2006.tab:0076', 'uvim2006.tab:0077', 'uvim2006.tab:0078', 'uvim2006.tab:0079', 'uvim2006.tab:0325', 'uvim2006.tab:0387', 'uvim2006.tab:0449', 'uvim2006.tab:0511', 'uvim2006.tab:0573', 'uvim2006.tab:0635', 'uvim2006.tab:0697', 'uvim2006.tab:0759', 'uvim2006.tab:0821', 'uvim2006.tab:0883', 'uvim2006.tab:0945', 'uvim2006.tab:1007', 'uvim2006.tab:1069', 'uvim2006.tab:1131', 'uvim2006.tab:1193', 'uvim2006.tab:1255', 'uvim2006.tab:1317', 'uvim2006.tab:1379', 'uvim2006.tab:1441', 'uvim2006.tab:1503', 'uvim2006.tab:1565', 'uvim2006.tab:1627', 'uvim2006.tab:1689', 'uvim2006.tab:1751', 'uvim2006.tab:1813', 'uvim2006.tab:1875', 'uvim2006.tab:1937', 'uvim2006.tab:1999', 'uvim2006.tab:2061', 'uvim2006.tab:2123', 'uvim2006.tab:2185']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0075', 'uvim2006.tab:0077', 'uvim2006.tab:0078', 'uvim2006.tab:0079', 'uvim2006.tab:0325', 'uvim2006.tab:0387', 'uvim2006.tab:0449', 'uvim2006.tab:0511', 'uvim2006.tab:0573', 'uvim2006.tab:0635', 'uvim2006.tab:0697', 'uvim2006.tab:0759', 'uvim2006.tab:0821', 'uvim2006.tab:0883', 'uvim2006.tab:0945', 'uvim2006.tab:1007', 'uvim2006.tab:1069', 'uvim2006.tab:1131', 'uvim2006.tab:1193', 'uvim2006.tab:1255', 'uvim2006.tab:1317', 'uvim2006.tab:1379', 'uvim2006.tab:1441', 'uvim2006.tab:1503', 'uvim2006.tab:1565', 'uvim2006.tab:1627', 'uvim2006.tab:1689', 'uvim2006.tab:1751', 'uvim2006.tab:1813', 'uvim2006.tab:1875', 'uvim2006.tab:1937', 'uvim2006.tab:1999', 'uvim2006.tab:2061']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0075', 'uvim2006.tab:0077', 'uvim2006.tab:0078', 'uvim2006.tab:0079', 'uvim2006.tab:0325', 'uvim2006.tab:0387', 'uvim2006.tab:0449', 'uvim2006.tab:0511', 'uvim2006.tab:0573', 'uvim2006.tab:0635', 'uvim2006.tab:0697', 'uvim2006.tab:0759', 'uvim2006.tab:0821', 'uvim2006.tab:0883', 'uvim2006.tab:0945', 'uvim2006.tab:1007', 'uvim2006.tab:1069', 'uvim2006.tab:1131', 'uvim2006.tab:1193', 'uvim2006.tab:1255', 'uvim2006.tab:1317', 'uvim2006.tab:1379', 'uvim2006.tab:1441', 'uvim2006.tab:1503', 'uvim2006.tab:1565', 'uvim2006.tab:1627', 'uvim2006.tab:1689', 'uvim2006.tab:1751', 'uvim2006.tab:1813', 'uvim2006.tab:1875', 'uvim2006.tab:1937', 'uvim2006.tab:1999', 'uvim2006.tab:2061']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0076', 'uvim2006.tab:2123', 'uvim2006.tab:2185']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0076', 'uvim2006.tab:2123', 'uvim2006.tab:2185']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0080', 'uvim2006.tab:0081', 'uvim2006.tab:0082', 'uvim2006.tab:0083', 'uvim2006.tab:0084', 'uvim2006.tab:0326', 'uvim2006.tab:0388', 'uvim2006.tab:0450', 'uvim2006.tab:0512', 'uvim2006.tab:0574', 'uvim2006.tab:0636', 'uvim2006.tab:0698', 'uvim2006.tab:0760', 'uvim2006.tab:0822', 'uvim2006.tab:0884', 'uvim2006.tab:0946', 'uvim2006.tab:1008', 'uvim2006.tab:1070', 'uvim2006.tab:1132', 'uvim2006.tab:1194', 'uvim2006.tab:1256', 'uvim2006.tab:1318', 'uvim2006.tab:1380', 'uvim2006.tab:1442', 'uvim2006.tab:1504', 'uvim2006.tab:1566', 'uvim2006.tab:1628', 'uvim2006.tab:1690', 'uvim2006.tab:1752', 'uvim2006.tab:1814', 'uvim2006.tab:1876', 'uvim2006.tab:1938', 'uvim2006.tab:2000', 'uvim2006.tab:2062', 'uvim2006.tab:2124', 'uvim2006.tab:2186']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0080', 'uvim2006.tab:0081', 'uvim2006.tab:0082', 'uvim2006.tab:0083', 'uvim2006.tab:0084', 'uvim2006.tab:0326', 'uvim2006.tab:0388', 'uvim2006.tab:0450', 'uvim2006.tab:0512', 'uvim2006.tab:0574', 'uvim2006.tab:0636', 'uvim2006.tab:0698', 'uvim2006.tab:0760', 'uvim2006.tab:0822', 'uvim2006.tab:0884', 'uvim2006.tab:0946', 'uvim2006.tab:1008', 'uvim2006.tab:1070', 'uvim2006.tab:1132', 'uvim2006.tab:1194', 'uvim2006.tab:1256', 'uvim2006.tab:1318', 'uvim2006.tab:1380', 'uvim2006.tab:1442', 'uvim2006.tab:1504', 'uvim2006.tab:1566', 'uvim2006.tab:1628', 'uvim2006.tab:1690', 'uvim2006.tab:1752', 'uvim2006.tab:1814', 'uvim2006.tab:1876', 'uvim2006.tab:1938', 'uvim2006.tab:2000', 'uvim2006.tab:2062', 'uvim2006.tab:2124', 'uvim2006.tab:2186']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0080', 'uvim2006.tab:0082', 'uvim2006.tab:0083', 'uvim2006.tab:0084', 'uvim2006.tab:0326', 'uvim2006.tab:0388', 'uvim2006.tab:0450', 'uvim2006.tab:0512', 'uvim2006.tab:0574', 'uvim2006.tab:0636', 'uvim2006.tab:0698', 'uvim2006.tab:0760', 'uvim2006.tab:0822', 'uvim2006.tab:0884', 'uvim2006.tab:0946', 'uvim2006.tab:1008', 'uvim2006.tab:1070', 'uvim2006.tab:1132', 'uvim2006.tab:1194', 'uvim2006.tab:1256', 'uvim2006.tab:1318', 'uvim2006.tab:1380', 'uvim2006.tab:1442', 'uvim2006.tab:1504', 'uvim2006.tab:1566', 'uvim2006.tab:1628', 'uvim2006.tab:1690', 'uvim2006.tab:1752', 'uvim2006.tab:1814', 'uvim2006.tab:1876', 'uvim2006.tab:1938', 'uvim2006.tab:2000', 'uvim2006.tab:2062']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0080', 'uvim2006.tab:0082', 'uvim2006.tab:0083', 'uvim2006.tab:0084', 'uvim2006.tab:0326', 'uvim2006.tab:0388', 'uvim2006.tab:0450', 'uvim2006.tab:0512', 'uvim2006.tab:0574', 'uvim2006.tab:0636', 'uvim2006.tab:0698', 'uvim2006.tab:0760', 'uvim2006.tab:0822', 'uvim2006.tab:0884', 'uvim2006.tab:0946', 'uvim2006.tab:1008', 'uvim2006.tab:1070', 'uvim2006.tab:1132', 'uvim2006.tab:1194', 'uvim2006.tab:1256', 'uvim2006.tab:1318', 'uvim2006.tab:1380', 'uvim2006.tab:1442', 'uvim2006.tab:1504', 'uvim2006.tab:1566', 'uvim2006.tab:1628', 'uvim2006.tab:1690', 'uvim2006.tab:1752', 'uvim2006.tab:1814', 'uvim2006.tab:1876', 'uvim2006.tab:1938', 'uvim2006.tab:2000', 'uvim2006.tab:2062']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0081', 'uvim2006.tab:2124', 'uvim2006.tab:2186']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0081', 'uvim2006.tab:2124', 'uvim2006.tab:2186']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0085', 'uvim2006.tab:0086', 'uvim2006.tab:0087', 'uvim2006.tab:0088', 'uvim2006.tab:0089', 'uvim2006.tab:0327', 'uvim2006.tab:0389', 'uvim2006.tab:0451', 'uvim2006.tab:0513', 'uvim2006.tab:0575', 'uvim2006.tab:0637', 'uvim2006.tab:0699', 'uvim2006.tab:0761', 'uvim2006.tab:0823', 'uvim2006.tab:0885', 'uvim2006.tab:0947', 'uvim2006.tab:1009', 'uvim2006.tab:1071', 'uvim2006.tab:1133', 'uvim2006.tab:1195', 'uvim2006.tab:1257', 'uvim2006.tab:1319', 'uvim2006.tab:1381', 'uvim2006.tab:1443', 'uvim2006.tab:1505', 'uvim2006.tab:1567', 'uvim2006.tab:1629', 'uvim2006.tab:1691', 'uvim2006.tab:1753', 'uvim2006.tab:1815', 'uvim2006.tab:1877', 'uvim2006.tab:1939', 'uvim2006.tab:2001', 'uvim2006.tab:2063', 'uvim2006.tab:2125', 'uvim2006.tab:2187']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0085', 'uvim2006.tab:0086', 'uvim2006.tab:0087', 'uvim2006.tab:0088', 'uvim2006.tab:0089', 'uvim2006.tab:0327', 'uvim2006.tab:0389', 'uvim2006.tab:0451', 'uvim2006.tab:0513', 'uvim2006.tab:0575', 'uvim2006.tab:0637', 'uvim2006.tab:0699', 'uvim2006.tab:0761', 'uvim2006.tab:0823', 'uvim2006.tab:0885', 'uvim2006.tab:0947', 'uvim2006.tab:1009', 'uvim2006.tab:1071', 'uvim2006.tab:1133', 'uvim2006.tab:1195', 'uvim2006.tab:1257', 'uvim2006.tab:1319', 'uvim2006.tab:1381', 'uvim2006.tab:1443', 'uvim2006.tab:1505', 'uvim2006.tab:1567', 'uvim2006.tab:1629', 'uvim2006.tab:1691', 'uvim2006.tab:1753', 'uvim2006.tab:1815', 'uvim2006.tab:1877', 'uvim2006.tab:1939', 'uvim2006.tab:2001', 'uvim2006.tab:2063', 'uvim2006.tab:2125', 'uvim2006.tab:2187']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0085', 'uvim2006.tab:0087', 'uvim2006.tab:0088', 'uvim2006.tab:0089', 'uvim2006.tab:0327', 'uvim2006.tab:0389', 'uvim2006.tab:0451', 'uvim2006.tab:0513', 'uvim2006.tab:0575', 'uvim2006.tab:0637', 'uvim2006.tab:0699', 'uvim2006.tab:0761', 'uvim2006.tab:0823', 'uvim2006.tab:0885', 'uvim2006.tab:0947', 'uvim2006.tab:1009', 'uvim2006.tab:1071', 'uvim2006.tab:1133', 'uvim2006.tab:1195', 'uvim2006.tab:1257', 'uvim2006.tab:1319', 'uvim2006.tab:1381', 'uvim2006.tab:1443', 'uvim2006.tab:1505', 'uvim2006.tab:1567', 'uvim2006.tab:1629', 'uvim2006.tab:1691', 'uvim2006.tab:1753', 'uvim2006.tab:1815', 'uvim2006.tab:1877', 'uvim2006.tab:1939', 'uvim2006.tab:2001', 'uvim2006.tab:2063']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0085', 'uvim2006.tab:0087', 'uvim2006.tab:0088', 'uvim2006.tab:0089', 'uvim2006.tab:0327', 'uvim2006.tab:0389', 'uvim2006.tab:0451', 'uvim2006.tab:0513', 'uvim2006.tab:0575', 'uvim2006.tab:0637', 'uvim2006.tab:0699', 'uvim2006.tab:0761', 'uvim2006.tab:0823', 'uvim2006.tab:0885', 'uvim2006.tab:0947', 'uvim2006.tab:1009', 'uvim2006.tab:1071', 'uvim2006.tab:1133', 'uvim2006.tab:1195', 'uvim2006.tab:1257', 'uvim2006.tab:1319', 'uvim2006.tab:1381', 'uvim2006.tab:1443', 'uvim2006.tab:1505', 'uvim2006.tab:1567', 'uvim2006.tab:1629', 'uvim2006.tab:1691', 'uvim2006.tab:1753', 'uvim2006.tab:1815', 'uvim2006.tab:1877', 'uvim2006.tab:1939', 'uvim2006.tab:2001', 'uvim2006.tab:2063']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0086', 'uvim2006.tab:2125', 'uvim2006.tab:2187']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0086', 'uvim2006.tab:2125', 'uvim2006.tab:2187']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0090', 'uvim2006.tab:0091', 'uvim2006.tab:0092', 'uvim2006.tab:0093', 'uvim2006.tab:0094', 'uvim2006.tab:0328', 'uvim2006.tab:0390', 'uvim2006.tab:0452', 'uvim2006.tab:0514', 'uvim2006.tab:0576', 'uvim2006.tab:0638', 'uvim2006.tab:0700', 'uvim2006.tab:0762', 'uvim2006.tab:0824', 'uvim2006.tab:0886', 'uvim2006.tab:0948', 'uvim2006.tab:1010', 'uvim2006.tab:1072', 'uvim2006.tab:1134', 'uvim2006.tab:1196', 'uvim2006.tab:1258', 'uvim2006.tab:1320', 'uvim2006.tab:1382', 'uvim2006.tab:1444', 'uvim2006.tab:1506', 'uvim2006.tab:1568', 'uvim2006.tab:1630', 'uvim2006.tab:1692', 'uvim2006.tab:1754', 'uvim2006.tab:1816', 'uvim2006.tab:1878', 'uvim2006.tab:1940', 'uvim2006.tab:2002', 'uvim2006.tab:2064', 'uvim2006.tab:2126', 'uvim2006.tab:2188']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0090', 'uvim2006.tab:0091', 'uvim2006.tab:0092', 'uvim2006.tab:0093', 'uvim2006.tab:0094', 'uvim2006.tab:0328', 'uvim2006.tab:0390', 'uvim2006.tab:0452', 'uvim2006.tab:0514', 'uvim2006.tab:0576', 'uvim2006.tab:0638', 'uvim2006.tab:0700', 'uvim2006.tab:0762', 'uvim2006.tab:0824', 'uvim2006.tab:0886', 'uvim2006.tab:0948', 'uvim2006.tab:1010', 'uvim2006.tab:1072', 'uvim2006.tab:1134', 'uvim2006.tab:1196', 'uvim2006.tab:1258', 'uvim2006.tab:1320', 'uvim2006.tab:1382', 'uvim2006.tab:1444', 'uvim2006.tab:1506', 'uvim2006.tab:1568', 'uvim2006.tab:1630', 'uvim2006.tab:1692', 'uvim2006.tab:1754', 'uvim2006.tab:1816', 'uvim2006.tab:1878', 'uvim2006.tab:1940', 'uvim2006.tab:2002', 'uvim2006.tab:2064', 'uvim2006.tab:2126', 'uvim2006.tab:2188']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0090', 'uvim2006.tab:0092', 'uvim2006.tab:0093', 'uvim2006.tab:0094', 'uvim2006.tab:0328', 'uvim2006.tab:0390', 'uvim2006.tab:0452', 'uvim2006.tab:0514', 'uvim2006.tab:0576', 'uvim2006.tab:0638', 'uvim2006.tab:0700', 'uvim2006.tab:0762', 'uvim2006.tab:0824', 'uvim2006.tab:0886', 'uvim2006.tab:0948', 'uvim2006.tab:1010', 'uvim2006.tab:1072', 'uvim2006.tab:1134', 'uvim2006.tab:1196', 'uvim2006.tab:1258', 'uvim2006.tab:1320', 'uvim2006.tab:1382', 'uvim2006.tab:1444', 'uvim2006.tab:1506', 'uvim2006.tab:1568', 'uvim2006.tab:1630', 'uvim2006.tab:1692', 'uvim2006.tab:1754', 'uvim2006.tab:1816', 'uvim2006.tab:1878', 'uvim2006.tab:1940', 'uvim2006.tab:2002', 'uvim2006.tab:2064']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0090', 'uvim2006.tab:0092', 'uvim2006.tab:0093', 'uvim2006.tab:0094', 'uvim2006.tab:0328', 'uvim2006.tab:0390', 'uvim2006.tab:0452', 'uvim2006.tab:0514', 'uvim2006.tab:0576', 'uvim2006.tab:0638', 'uvim2006.tab:0700', 'uvim2006.tab:0762', 'uvim2006.tab:0824', 'uvim2006.tab:0886', 'uvim2006.tab:0948', 'uvim2006.tab:1010', 'uvim2006.tab:1072', 'uvim2006.tab:1134', 'uvim2006.tab:1196', 'uvim2006.tab:1258', 'uvim2006.tab:1320', 'uvim2006.tab:1382', 'uvim2006.tab:1444', 'uvim2006.tab:1506', 'uvim2006.tab:1568', 'uvim2006.tab:1630', 'uvim2006.tab:1692', 'uvim2006.tab:1754', 'uvim2006.tab:1816', 'uvim2006.tab:1878', 'uvim2006.tab:1940', 'uvim2006.tab:2002', 'uvim2006.tab:2064']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0091', 'uvim2006.tab:2126', 'uvim2006.tab:2188']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0091', 'uvim2006.tab:2126', 'uvim2006.tab:2188']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0095', 'uvim2006.tab:0096', 'uvim2006.tab:0097', 'uvim2006.tab:0098', 'uvim2006.tab:0099', 'uvim2006.tab:0329', 'uvim2006.tab:0391', 'uvim2006.tab:0453', 'uvim2006.tab:0515', 'uvim2006.tab:0577', 'uvim2006.tab:0639', 'uvim2006.tab:0701', 'uvim2006.tab:0763', 'uvim2006.tab:0825', 'uvim2006.tab:0887', 'uvim2006.tab:0949', 'uvim2006.tab:1011', 'uvim2006.tab:1073', 'uvim2006.tab:1135', 'uvim2006.tab:1197', 'uvim2006.tab:1259', 'uvim2006.tab:1321', 'uvim2006.tab:1383', 'uvim2006.tab:1445', 'uvim2006.tab:1507', 'uvim2006.tab:1569', 'uvim2006.tab:1631', 'uvim2006.tab:1693', 'uvim2006.tab:1755', 'uvim2006.tab:1817', 'uvim2006.tab:1879', 'uvim2006.tab:1941', 'uvim2006.tab:2003', 'uvim2006.tab:2065', 'uvim2006.tab:2127', 'uvim2006.tab:2189']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0095', 'uvim2006.tab:0096', 'uvim2006.tab:0097', 'uvim2006.tab:0098', 'uvim2006.tab:0099', 'uvim2006.tab:0329', 'uvim2006.tab:0391', 'uvim2006.tab:0453', 'uvim2006.tab:0515', 'uvim2006.tab:0577', 'uvim2006.tab:0639', 'uvim2006.tab:0701', 'uvim2006.tab:0763', 'uvim2006.tab:0825', 'uvim2006.tab:0887', 'uvim2006.tab:0949', 'uvim2006.tab:1011', 'uvim2006.tab:1073', 'uvim2006.tab:1135', 'uvim2006.tab:1197', 'uvim2006.tab:1259', 'uvim2006.tab:1321', 'uvim2006.tab:1383', 'uvim2006.tab:1445', 'uvim2006.tab:1507', 'uvim2006.tab:1569', 'uvim2006.tab:1631', 'uvim2006.tab:1693', 'uvim2006.tab:1755', 'uvim2006.tab:1817', 'uvim2006.tab:1879', 'uvim2006.tab:1941', 'uvim2006.tab:2003', 'uvim2006.tab:2065', 'uvim2006.tab:2127', 'uvim2006.tab:2189']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0095', 'uvim2006.tab:0097', 'uvim2006.tab:0098', 'uvim2006.tab:0099', 'uvim2006.tab:0329', 'uvim2006.tab:0391', 'uvim2006.tab:0453', 'uvim2006.tab:0515', 'uvim2006.tab:0577', 'uvim2006.tab:0639', 'uvim2006.tab:0701', 'uvim2006.tab:0763', 'uvim2006.tab:0825', 'uvim2006.tab:0887', 'uvim2006.tab:0949', 'uvim2006.tab:1011', 'uvim2006.tab:1073', 'uvim2006.tab:1135', 'uvim2006.tab:1197', 'uvim2006.tab:1259', 'uvim2006.tab:1321', 'uvim2006.tab:1383', 'uvim2006.tab:1445', 'uvim2006.tab:1507', 'uvim2006.tab:1569', 'uvim2006.tab:1631', 'uvim2006.tab:1693', 'uvim2006.tab:1755', 'uvim2006.tab:1817', 'uvim2006.tab:1879', 'uvim2006.tab:1941', 'uvim2006.tab:2003', 'uvim2006.tab:2065']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0095', 'uvim2006.tab:0097', 'uvim2006.tab:0098', 'uvim2006.tab:0099', 'uvim2006.tab:0329', 'uvim2006.tab:0391', 'uvim2006.tab:0453', 'uvim2006.tab:0515', 'uvim2006.tab:0577', 'uvim2006.tab:0639', 'uvim2006.tab:0701', 'uvim2006.tab:0763', 'uvim2006.tab:0825', 'uvim2006.tab:0887', 'uvim2006.tab:0949', 'uvim2006.tab:1011', 'uvim2006.tab:1073', 'uvim2006.tab:1135', 'uvim2006.tab:1197', 'uvim2006.tab:1259', 'uvim2006.tab:1321', 'uvim2006.tab:1383', 'uvim2006.tab:1445', 'uvim2006.tab:1507', 'uvim2006.tab:1569', 'uvim2006.tab:1631', 'uvim2006.tab:1693', 'uvim2006.tab:1755', 'uvim2006.tab:1817', 'uvim2006.tab:1879', 'uvim2006.tab:1941', 'uvim2006.tab:2003', 'uvim2006.tab:2065']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0096', 'uvim2006.tab:2127', 'uvim2006.tab:2189']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0096', 'uvim2006.tab:2127', 'uvim2006.tab:2189']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0100', 'uvim2006.tab:0101', 'uvim2006.tab:0102', 'uvim2006.tab:0103', 'uvim2006.tab:0104', 'uvim2006.tab:0330', 'uvim2006.tab:0392', 'uvim2006.tab:0454', 'uvim2006.tab:0516', 'uvim2006.tab:0578', 'uvim2006.tab:0640', 'uvim2006.tab:0702', 'uvim2006.tab:0764', 'uvim2006.tab:0826', 'uvim2006.tab:0888', 'uvim2006.tab:0950', 'uvim2006.tab:1012', 'uvim2006.tab:1074', 'uvim2006.tab:1136', 'uvim2006.tab:1198', 'uvim2006.tab:1260', 'uvim2006.tab:1322', 'uvim2006.tab:1384', 'uvim2006.tab:1446', 'uvim2006.tab:1508', 'uvim2006.tab:1570', 'uvim2006.tab:1632', 'uvim2006.tab:1694', 'uvim2006.tab:1756', 'uvim2006.tab:1818', 'uvim2006.tab:1880', 'uvim2006.tab:1942', 'uvim2006.tab:2004', 'uvim2006.tab:2066', 'uvim2006.tab:2128', 'uvim2006.tab:2190']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0100', 'uvim2006.tab:0101', 'uvim2006.tab:0102', 'uvim2006.tab:0103', 'uvim2006.tab:0104', 'uvim2006.tab:0330', 'uvim2006.tab:0392', 'uvim2006.tab:0454', 'uvim2006.tab:0516', 'uvim2006.tab:0578', 'uvim2006.tab:0640', 'uvim2006.tab:0702', 'uvim2006.tab:0764', 'uvim2006.tab:0826', 'uvim2006.tab:0888', 'uvim2006.tab:0950', 'uvim2006.tab:1012', 'uvim2006.tab:1074', 'uvim2006.tab:1136', 'uvim2006.tab:1198', 'uvim2006.tab:1260', 'uvim2006.tab:1322', 'uvim2006.tab:1384', 'uvim2006.tab:1446', 'uvim2006.tab:1508', 'uvim2006.tab:1570', 'uvim2006.tab:1632', 'uvim2006.tab:1694', 'uvim2006.tab:1756', 'uvim2006.tab:1818', 'uvim2006.tab:1880', 'uvim2006.tab:1942', 'uvim2006.tab:2004', 'uvim2006.tab:2066', 'uvim2006.tab:2128', 'uvim2006.tab:2190']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0100', 'uvim2006.tab:0102', 'uvim2006.tab:0103', 'uvim2006.tab:0104', 'uvim2006.tab:0330', 'uvim2006.tab:0392', 'uvim2006.tab:0454', 'uvim2006.tab:0516', 'uvim2006.tab:0578', 'uvim2006.tab:0640', 'uvim2006.tab:0702', 'uvim2006.tab:0764', 'uvim2006.tab:0826', 'uvim2006.tab:0888', 'uvim2006.tab:0950', 'uvim2006.tab:1012', 'uvim2006.tab:1074', 'uvim2006.tab:1136', 'uvim2006.tab:1198', 'uvim2006.tab:1260', 'uvim2006.tab:1322', 'uvim2006.tab:1384', 'uvim2006.tab:1446', 'uvim2006.tab:1508', 'uvim2006.tab:1570', 'uvim2006.tab:1632', 'uvim2006.tab:1694', 'uvim2006.tab:1756', 'uvim2006.tab:1818', 'uvim2006.tab:1880', 'uvim2006.tab:1942', 'uvim2006.tab:2004', 'uvim2006.tab:2066']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0100', 'uvim2006.tab:0102', 'uvim2006.tab:0103', 'uvim2006.tab:0104', 'uvim2006.tab:0330', 'uvim2006.tab:0392', 'uvim2006.tab:0454', 'uvim2006.tab:0516', 'uvim2006.tab:0578', 'uvim2006.tab:0640', 'uvim2006.tab:0702', 'uvim2006.tab:0764', 'uvim2006.tab:0826', 'uvim2006.tab:0888', 'uvim2006.tab:0950', 'uvim2006.tab:1012', 'uvim2006.tab:1074', 'uvim2006.tab:1136', 'uvim2006.tab:1198', 'uvim2006.tab:1260', 'uvim2006.tab:1322', 'uvim2006.tab:1384', 'uvim2006.tab:1446', 'uvim2006.tab:1508', 'uvim2006.tab:1570', 'uvim2006.tab:1632', 'uvim2006.tab:1694', 'uvim2006.tab:1756', 'uvim2006.tab:1818', 'uvim2006.tab:1880', 'uvim2006.tab:1942', 'uvim2006.tab:2004', 'uvim2006.tab:2066']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0101', 'uvim2006.tab:2128', 'uvim2006.tab:2190']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0101', 'uvim2006.tab:2128', 'uvim2006.tab:2190']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0105', 'uvim2006.tab:0106', 'uvim2006.tab:0107', 'uvim2006.tab:0108', 'uvim2006.tab:0109', 'uvim2006.tab:0331', 'uvim2006.tab:0393', 'uvim2006.tab:0455', 'uvim2006.tab:0517', 'uvim2006.tab:0579', 'uvim2006.tab:0641', 'uvim2006.tab:0703', 'uvim2006.tab:0765', 'uvim2006.tab:0827', 'uvim2006.tab:0889', 'uvim2006.tab:0951', 'uvim2006.tab:1013', 'uvim2006.tab:1075', 'uvim2006.tab:1137', 'uvim2006.tab:1199', 'uvim2006.tab:1261', 'uvim2006.tab:1323', 'uvim2006.tab:1385', 'uvim2006.tab:1447', 'uvim2006.tab:1509', 'uvim2006.tab:1571', 'uvim2006.tab:1633', 'uvim2006.tab:1695', 'uvim2006.tab:1757', 'uvim2006.tab:1819', 'uvim2006.tab:1881', 'uvim2006.tab:1943', 'uvim2006.tab:2005', 'uvim2006.tab:2067', 'uvim2006.tab:2129', 'uvim2006.tab:2191']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0105', 'uvim2006.tab:0106', 'uvim2006.tab:0107', 'uvim2006.tab:0108', 'uvim2006.tab:0109', 'uvim2006.tab:0331', 'uvim2006.tab:0393', 'uvim2006.tab:0455', 'uvim2006.tab:0517', 'uvim2006.tab:0579', 'uvim2006.tab:0641', 'uvim2006.tab:0703', 'uvim2006.tab:0765', 'uvim2006.tab:0827', 'uvim2006.tab:0889', 'uvim2006.tab:0951', 'uvim2006.tab:1013', 'uvim2006.tab:1075', 'uvim2006.tab:1137', 'uvim2006.tab:1199', 'uvim2006.tab:1261', 'uvim2006.tab:1323', 'uvim2006.tab:1385', 'uvim2006.tab:1447', 'uvim2006.tab:1509', 'uvim2006.tab:1571', 'uvim2006.tab:1633', 'uvim2006.tab:1695', 'uvim2006.tab:1757', 'uvim2006.tab:1819', 'uvim2006.tab:1881', 'uvim2006.tab:1943', 'uvim2006.tab:2005', 'uvim2006.tab:2067', 'uvim2006.tab:2129', 'uvim2006.tab:2191']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0105', 'uvim2006.tab:0107', 'uvim2006.tab:0108', 'uvim2006.tab:0109', 'uvim2006.tab:0331', 'uvim2006.tab:0393', 'uvim2006.tab:0455', 'uvim2006.tab:0517', 'uvim2006.tab:0579', 'uvim2006.tab:0641', 'uvim2006.tab:0703', 'uvim2006.tab:0765', 'uvim2006.tab:0827', 'uvim2006.tab:0889', 'uvim2006.tab:0951', 'uvim2006.tab:1013', 'uvim2006.tab:1075', 'uvim2006.tab:1137', 'uvim2006.tab:1199', 'uvim2006.tab:1261', 'uvim2006.tab:1323', 'uvim2006.tab:1385', 'uvim2006.tab:1447', 'uvim2006.tab:1509', 'uvim2006.tab:1571', 'uvim2006.tab:1633', 'uvim2006.tab:1695', 'uvim2006.tab:1757', 'uvim2006.tab:1819', 'uvim2006.tab:1881', 'uvim2006.tab:1943', 'uvim2006.tab:2005', 'uvim2006.tab:2067']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0105', 'uvim2006.tab:0107', 'uvim2006.tab:0108', 'uvim2006.tab:0109', 'uvim2006.tab:0331', 'uvim2006.tab:0393', 'uvim2006.tab:0455', 'uvim2006.tab:0517', 'uvim2006.tab:0579', 'uvim2006.tab:0641', 'uvim2006.tab:0703', 'uvim2006.tab:0765', 'uvim2006.tab:0827', 'uvim2006.tab:0889', 'uvim2006.tab:0951', 'uvim2006.tab:1013', 'uvim2006.tab:1075', 'uvim2006.tab:1137', 'uvim2006.tab:1199', 'uvim2006.tab:1261', 'uvim2006.tab:1323', 'uvim2006.tab:1385', 'uvim2006.tab:1447', 'uvim2006.tab:1509', 'uvim2006.tab:1571', 'uvim2006.tab:1633', 'uvim2006.tab:1695', 'uvim2006.tab:1757', 'uvim2006.tab:1819', 'uvim2006.tab:1881', 'uvim2006.tab:1943', 'uvim2006.tab:2005', 'uvim2006.tab:2067']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0106', 'uvim2006.tab:2129', 'uvim2006.tab:2191']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0106', 'uvim2006.tab:2129', 'uvim2006.tab:2191']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0110', 'uvim2006.tab:0111', 'uvim2006.tab:0112', 'uvim2006.tab:0113', 'uvim2006.tab:0114', 'uvim2006.tab:0332', 'uvim2006.tab:0394', 'uvim2006.tab:0456', 'uvim2006.tab:0518', 'uvim2006.tab:0580', 'uvim2006.tab:0642', 'uvim2006.tab:0704', 'uvim2006.tab:0766', 'uvim2006.tab:0828', 'uvim2006.tab:0890', 'uvim2006.tab:0952', 'uvim2006.tab:1014', 'uvim2006.tab:1076', 'uvim2006.tab:1138', 'uvim2006.tab:1200', 'uvim2006.tab:1262', 'uvim2006.tab:1324', 'uvim2006.tab:1386', 'uvim2006.tab:1448', 'uvim2006.tab:1510', 'uvim2006.tab:1572', 'uvim2006.tab:1634', 'uvim2006.tab:1696', 'uvim2006.tab:1758', 'uvim2006.tab:1820', 'uvim2006.tab:1882', 'uvim2006.tab:1944', 'uvim2006.tab:2006', 'uvim2006.tab:2068', 'uvim2006.tab:2130', 'uvim2006.tab:2192']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0110', 'uvim2006.tab:0111', 'uvim2006.tab:0112', 'uvim2006.tab:0113', 'uvim2006.tab:0114', 'uvim2006.tab:0332', 'uvim2006.tab:0394', 'uvim2006.tab:0456', 'uvim2006.tab:0518', 'uvim2006.tab:0580', 'uvim2006.tab:0642', 'uvim2006.tab:0704', 'uvim2006.tab:0766', 'uvim2006.tab:0828', 'uvim2006.tab:0890', 'uvim2006.tab:0952', 'uvim2006.tab:1014', 'uvim2006.tab:1076', 'uvim2006.tab:1138', 'uvim2006.tab:1200', 'uvim2006.tab:1262', 'uvim2006.tab:1324', 'uvim2006.tab:1386', 'uvim2006.tab:1448', 'uvim2006.tab:1510', 'uvim2006.tab:1572', 'uvim2006.tab:1634', 'uvim2006.tab:1696', 'uvim2006.tab:1758', 'uvim2006.tab:1820', 'uvim2006.tab:1882', 'uvim2006.tab:1944', 'uvim2006.tab:2006', 'uvim2006.tab:2068', 'uvim2006.tab:2130', 'uvim2006.tab:2192']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0110', 'uvim2006.tab:0112', 'uvim2006.tab:0113', 'uvim2006.tab:0114', 'uvim2006.tab:0332', 'uvim2006.tab:0394', 'uvim2006.tab:0456', 'uvim2006.tab:0518', 'uvim2006.tab:0580', 'uvim2006.tab:0642', 'uvim2006.tab:0704', 'uvim2006.tab:0766', 'uvim2006.tab:0828', 'uvim2006.tab:0890', 'uvim2006.tab:0952', 'uvim2006.tab:1014', 'uvim2006.tab:1076', 'uvim2006.tab:1138', 'uvim2006.tab:1200', 'uvim2006.tab:1262', 'uvim2006.tab:1324', 'uvim2006.tab:1386', 'uvim2006.tab:1448', 'uvim2006.tab:1510', 'uvim2006.tab:1572', 'uvim2006.tab:1634', 'uvim2006.tab:1696', 'uvim2006.tab:1758', 'uvim2006.tab:1820', 'uvim2006.tab:1882', 'uvim2006.tab:1944', 'uvim2006.tab:2006', 'uvim2006.tab:2068']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0110', 'uvim2006.tab:0112', 'uvim2006.tab:0113', 'uvim2006.tab:0114', 'uvim2006.tab:0332', 'uvim2006.tab:0394', 'uvim2006.tab:0456', 'uvim2006.tab:0518', 'uvim2006.tab:0580', 'uvim2006.tab:0642', 'uvim2006.tab:0704', 'uvim2006.tab:0766', 'uvim2006.tab:0828', 'uvim2006.tab:0890', 'uvim2006.tab:0952', 'uvim2006.tab:1014', 'uvim2006.tab:1076', 'uvim2006.tab:1138', 'uvim2006.tab:1200', 'uvim2006.tab:1262', 'uvim2006.tab:1324', 'uvim2006.tab:1386', 'uvim2006.tab:1448', 'uvim2006.tab:1510', 'uvim2006.tab:1572', 'uvim2006.tab:1634', 'uvim2006.tab:1696', 'uvim2006.tab:1758', 'uvim2006.tab:1820', 'uvim2006.tab:1882', 'uvim2006.tab:1944', 'uvim2006.tab:2006', 'uvim2006.tab:2068']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0111', 'uvim2006.tab:2130', 'uvim2006.tab:2192']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0111', 'uvim2006.tab:2130', 'uvim2006.tab:2192']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0115', 'uvim2006.tab:0116', 'uvim2006.tab:0117', 'uvim2006.tab:0118', 'uvim2006.tab:0119', 'uvim2006.tab:0333', 'uvim2006.tab:0395', 'uvim2006.tab:0457', 'uvim2006.tab:0519', 'uvim2006.tab:0581', 'uvim2006.tab:0643', 'uvim2006.tab:0705', 'uvim2006.tab:0767', 'uvim2006.tab:0829', 'uvim2006.tab:0891', 'uvim2006.tab:0953', 'uvim2006.tab:1015', 'uvim2006.tab:1077', 'uvim2006.tab:1139', 'uvim2006.tab:1201', 'uvim2006.tab:1263', 'uvim2006.tab:1325', 'uvim2006.tab:1387', 'uvim2006.tab:1449', 'uvim2006.tab:1511', 'uvim2006.tab:1573', 'uvim2006.tab:1635', 'uvim2006.tab:1697', 'uvim2006.tab:1759', 'uvim2006.tab:1821', 'uvim2006.tab:1883', 'uvim2006.tab:1945', 'uvim2006.tab:2007', 'uvim2006.tab:2069', 'uvim2006.tab:2131', 'uvim2006.tab:2193']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0115', 'uvim2006.tab:0116', 'uvim2006.tab:0117', 'uvim2006.tab:0118', 'uvim2006.tab:0119', 'uvim2006.tab:0333', 'uvim2006.tab:0395', 'uvim2006.tab:0457', 'uvim2006.tab:0519', 'uvim2006.tab:0581', 'uvim2006.tab:0643', 'uvim2006.tab:0705', 'uvim2006.tab:0767', 'uvim2006.tab:0829', 'uvim2006.tab:0891', 'uvim2006.tab:0953', 'uvim2006.tab:1015', 'uvim2006.tab:1077', 'uvim2006.tab:1139', 'uvim2006.tab:1201', 'uvim2006.tab:1263', 'uvim2006.tab:1325', 'uvim2006.tab:1387', 'uvim2006.tab:1449', 'uvim2006.tab:1511', 'uvim2006.tab:1573', 'uvim2006.tab:1635', 'uvim2006.tab:1697', 'uvim2006.tab:1759', 'uvim2006.tab:1821', 'uvim2006.tab:1883', 'uvim2006.tab:1945', 'uvim2006.tab:2007', 'uvim2006.tab:2069', 'uvim2006.tab:2131', 'uvim2006.tab:2193']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0115', 'uvim2006.tab:0117', 'uvim2006.tab:0118', 'uvim2006.tab:0119', 'uvim2006.tab:0333', 'uvim2006.tab:0395', 'uvim2006.tab:0457', 'uvim2006.tab:0519', 'uvim2006.tab:0581', 'uvim2006.tab:0643', 'uvim2006.tab:0705', 'uvim2006.tab:0767', 'uvim2006.tab:0829', 'uvim2006.tab:0891', 'uvim2006.tab:0953', 'uvim2006.tab:1015', 'uvim2006.tab:1077', 'uvim2006.tab:1139', 'uvim2006.tab:1201', 'uvim2006.tab:1263', 'uvim2006.tab:1325', 'uvim2006.tab:1387', 'uvim2006.tab:1449', 'uvim2006.tab:1511', 'uvim2006.tab:1573', 'uvim2006.tab:1635', 'uvim2006.tab:1697', 'uvim2006.tab:1759', 'uvim2006.tab:1821', 'uvim2006.tab:1883', 'uvim2006.tab:1945', 'uvim2006.tab:2007', 'uvim2006.tab:2069']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0115', 'uvim2006.tab:0117', 'uvim2006.tab:0118', 'uvim2006.tab:0119', 'uvim2006.tab:0333', 'uvim2006.tab:0395', 'uvim2006.tab:0457', 'uvim2006.tab:0519', 'uvim2006.tab:0581', 'uvim2006.tab:0643', 'uvim2006.tab:0705', 'uvim2006.tab:0767', 'uvim2006.tab:0829', 'uvim2006.tab:0891', 'uvim2006.tab:0953', 'uvim2006.tab:1015', 'uvim2006.tab:1077', 'uvim2006.tab:1139', 'uvim2006.tab:1201', 'uvim2006.tab:1263', 'uvim2006.tab:1325', 'uvim2006.tab:1387', 'uvim2006.tab:1449', 'uvim2006.tab:1511', 'uvim2006.tab:1573', 'uvim2006.tab:1635', 'uvim2006.tab:1697', 'uvim2006.tab:1759', 'uvim2006.tab:1821', 'uvim2006.tab:1883', 'uvim2006.tab:1945', 'uvim2006.tab:2007', 'uvim2006.tab:2069']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0116', 'uvim2006.tab:2131', 'uvim2006.tab:2193']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0116', 'uvim2006.tab:2131', 'uvim2006.tab:2193']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0120', 'uvim2006.tab:0121', 'uvim2006.tab:0122', 'uvim2006.tab:0123', 'uvim2006.tab:0124', 'uvim2006.tab:0334', 'uvim2006.tab:0396', 'uvim2006.tab:0458', 'uvim2006.tab:0520', 'uvim2006.tab:0582', 'uvim2006.tab:0644', 'uvim2006.tab:0706', 'uvim2006.tab:0768', 'uvim2006.tab:0830', 'uvim2006.tab:0892', 'uvim2006.tab:0954', 'uvim2006.tab:1016', 'uvim2006.tab:1078', 'uvim2006.tab:1140', 'uvim2006.tab:1202', 'uvim2006.tab:1264', 'uvim2006.tab:1326', 'uvim2006.tab:1388', 'uvim2006.tab:1450', 'uvim2006.tab:1512', 'uvim2006.tab:1574', 'uvim2006.tab:1636', 'uvim2006.tab:1698', 'uvim2006.tab:1760', 'uvim2006.tab:1822', 'uvim2006.tab:1884', 'uvim2006.tab:1946', 'uvim2006.tab:2008', 'uvim2006.tab:2070', 'uvim2006.tab:2132', 'uvim2006.tab:2194']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0120', 'uvim2006.tab:0121', 'uvim2006.tab:0122', 'uvim2006.tab:0123', 'uvim2006.tab:0124', 'uvim2006.tab:0334', 'uvim2006.tab:0396', 'uvim2006.tab:0458', 'uvim2006.tab:0520', 'uvim2006.tab:0582', 'uvim2006.tab:0644', 'uvim2006.tab:0706', 'uvim2006.tab:0768', 'uvim2006.tab:0830', 'uvim2006.tab:0892', 'uvim2006.tab:0954', 'uvim2006.tab:1016', 'uvim2006.tab:1078', 'uvim2006.tab:1140', 'uvim2006.tab:1202', 'uvim2006.tab:1264', 'uvim2006.tab:1326', 'uvim2006.tab:1388', 'uvim2006.tab:1450', 'uvim2006.tab:1512', 'uvim2006.tab:1574', 'uvim2006.tab:1636', 'uvim2006.tab:1698', 'uvim2006.tab:1760', 'uvim2006.tab:1822', 'uvim2006.tab:1884', 'uvim2006.tab:1946', 'uvim2006.tab:2008', 'uvim2006.tab:2070', 'uvim2006.tab:2132', 'uvim2006.tab:2194']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0120', 'uvim2006.tab:0122', 'uvim2006.tab:0123', 'uvim2006.tab:0124', 'uvim2006.tab:0334', 'uvim2006.tab:0396', 'uvim2006.tab:0458', 'uvim2006.tab:0520', 'uvim2006.tab:0582', 'uvim2006.tab:0644', 'uvim2006.tab:0706', 'uvim2006.tab:0768', 'uvim2006.tab:0830', 'uvim2006.tab:0892', 'uvim2006.tab:0954', 'uvim2006.tab:1016', 'uvim2006.tab:1078', 'uvim2006.tab:1140', 'uvim2006.tab:1202', 'uvim2006.tab:1264', 'uvim2006.tab:1326', 'uvim2006.tab:1388', 'uvim2006.tab:1450', 'uvim2006.tab:1512', 'uvim2006.tab:1574', 'uvim2006.tab:1636', 'uvim2006.tab:1698', 'uvim2006.tab:1760', 'uvim2006.tab:1822', 'uvim2006.tab:1884', 'uvim2006.tab:1946', 'uvim2006.tab:2008', 'uvim2006.tab:2070']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0120', 'uvim2006.tab:0122', 'uvim2006.tab:0123', 'uvim2006.tab:0124', 'uvim2006.tab:0334', 'uvim2006.tab:0396', 'uvim2006.tab:0458', 'uvim2006.tab:0520', 'uvim2006.tab:0582', 'uvim2006.tab:0644', 'uvim2006.tab:0706', 'uvim2006.tab:0768', 'uvim2006.tab:0830', 'uvim2006.tab:0892', 'uvim2006.tab:0954', 'uvim2006.tab:1016', 'uvim2006.tab:1078', 'uvim2006.tab:1140', 'uvim2006.tab:1202', 'uvim2006.tab:1264', 'uvim2006.tab:1326', 'uvim2006.tab:1388', 'uvim2006.tab:1450', 'uvim2006.tab:1512', 'uvim2006.tab:1574', 'uvim2006.tab:1636', 'uvim2006.tab:1698', 'uvim2006.tab:1760', 'uvim2006.tab:1822', 'uvim2006.tab:1884', 'uvim2006.tab:1946', 'uvim2006.tab:2008', 'uvim2006.tab:2070']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0121', 'uvim2006.tab:2132', 'uvim2006.tab:2194']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0121', 'uvim2006.tab:2132', 'uvim2006.tab:2194']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0125', 'uvim2006.tab:0126', 'uvim2006.tab:0127', 'uvim2006.tab:0128', 'uvim2006.tab:0129', 'uvim2006.tab:0335', 'uvim2006.tab:0397', 'uvim2006.tab:0459', 'uvim2006.tab:0521', 'uvim2006.tab:0583', 'uvim2006.tab:0645', 'uvim2006.tab:0707', 'uvim2006.tab:0769', 'uvim2006.tab:0831', 'uvim2006.tab:0893', 'uvim2006.tab:0955', 'uvim2006.tab:1017', 'uvim2006.tab:1079', 'uvim2006.tab:1141', 'uvim2006.tab:1203', 'uvim2006.tab:1265', 'uvim2006.tab:1327', 'uvim2006.tab:1389', 'uvim2006.tab:1451', 'uvim2006.tab:1513', 'uvim2006.tab:1575', 'uvim2006.tab:1637', 'uvim2006.tab:1699', 'uvim2006.tab:1761', 'uvim2006.tab:1823', 'uvim2006.tab:1885', 'uvim2006.tab:1947', 'uvim2006.tab:2009', 'uvim2006.tab:2071', 'uvim2006.tab:2133', 'uvim2006.tab:2195']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0125', 'uvim2006.tab:0126', 'uvim2006.tab:0127', 'uvim2006.tab:0128', 'uvim2006.tab:0129', 'uvim2006.tab:0335', 'uvim2006.tab:0397', 'uvim2006.tab:0459', 'uvim2006.tab:0521', 'uvim2006.tab:0583', 'uvim2006.tab:0645', 'uvim2006.tab:0707', 'uvim2006.tab:0769', 'uvim2006.tab:0831', 'uvim2006.tab:0893', 'uvim2006.tab:0955', 'uvim2006.tab:1017', 'uvim2006.tab:1079', 'uvim2006.tab:1141', 'uvim2006.tab:1203', 'uvim2006.tab:1265', 'uvim2006.tab:1327', 'uvim2006.tab:1389', 'uvim2006.tab:1451', 'uvim2006.tab:1513', 'uvim2006.tab:1575', 'uvim2006.tab:1637', 'uvim2006.tab:1699', 'uvim2006.tab:1761', 'uvim2006.tab:1823', 'uvim2006.tab:1885', 'uvim2006.tab:1947', 'uvim2006.tab:2009', 'uvim2006.tab:2071', 'uvim2006.tab:2133', 'uvim2006.tab:2195']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0125', 'uvim2006.tab:0127', 'uvim2006.tab:0128', 'uvim2006.tab:0129', 'uvim2006.tab:0335', 'uvim2006.tab:0397', 'uvim2006.tab:0459', 'uvim2006.tab:0521', 'uvim2006.tab:0583', 'uvim2006.tab:0645', 'uvim2006.tab:0707', 'uvim2006.tab:0769', 'uvim2006.tab:0831', 'uvim2006.tab:0893', 'uvim2006.tab:0955', 'uvim2006.tab:1017', 'uvim2006.tab:1079', 'uvim2006.tab:1141', 'uvim2006.tab:1203', 'uvim2006.tab:1265', 'uvim2006.tab:1327', 'uvim2006.tab:1389', 'uvim2006.tab:1451', 'uvim2006.tab:1513', 'uvim2006.tab:1575', 'uvim2006.tab:1637', 'uvim2006.tab:1699', 'uvim2006.tab:1761', 'uvim2006.tab:1823', 'uvim2006.tab:1885', 'uvim2006.tab:1947', 'uvim2006.tab:2009', 'uvim2006.tab:2071']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0125', 'uvim2006.tab:0127', 'uvim2006.tab:0128', 'uvim2006.tab:0129', 'uvim2006.tab:0335', 'uvim2006.tab:0397', 'uvim2006.tab:0459', 'uvim2006.tab:0521', 'uvim2006.tab:0583', 'uvim2006.tab:0645', 'uvim2006.tab:0707', 'uvim2006.tab:0769', 'uvim2006.tab:0831', 'uvim2006.tab:0893', 'uvim2006.tab:0955', 'uvim2006.tab:1017', 'uvim2006.tab:1079', 'uvim2006.tab:1141', 'uvim2006.tab:1203', 'uvim2006.tab:1265', 'uvim2006.tab:1327', 'uvim2006.tab:1389', 'uvim2006.tab:1451', 'uvim2006.tab:1513', 'uvim2006.tab:1575', 'uvim2006.tab:1637', 'uvim2006.tab:1699', 'uvim2006.tab:1761', 'uvim2006.tab:1823', 'uvim2006.tab:1885', 'uvim2006.tab:1947', 'uvim2006.tab:2009', 'uvim2006.tab:2071']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0126', 'uvim2006.tab:2133', 'uvim2006.tab:2195']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0126', 'uvim2006.tab:2133', 'uvim2006.tab:2195']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0130', 'uvim2006.tab:0131', 'uvim2006.tab:0132', 'uvim2006.tab:0133', 'uvim2006.tab:0134', 'uvim2006.tab:0336', 'uvim2006.tab:0398', 'uvim2006.tab:0460', 'uvim2006.tab:0522', 'uvim2006.tab:0584', 'uvim2006.tab:0646', 'uvim2006.tab:0708', 'uvim2006.tab:0770', 'uvim2006.tab:0832', 'uvim2006.tab:0894', 'uvim2006.tab:0956', 'uvim2006.tab:1018', 'uvim2006.tab:1080', 'uvim2006.tab:1142', 'uvim2006.tab:1204', 'uvim2006.tab:1266', 'uvim2006.tab:1328', 'uvim2006.tab:1390', 'uvim2006.tab:1452', 'uvim2006.tab:1514', 'uvim2006.tab:1576', 'uvim2006.tab:1638', 'uvim2006.tab:1700', 'uvim2006.tab:1762', 'uvim2006.tab:1824', 'uvim2006.tab:1886', 'uvim2006.tab:1948', 'uvim2006.tab:2010', 'uvim2006.tab:2072', 'uvim2006.tab:2134', 'uvim2006.tab:2196']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0130', 'uvim2006.tab:0131', 'uvim2006.tab:0132', 'uvim2006.tab:0133', 'uvim2006.tab:0134', 'uvim2006.tab:0336', 'uvim2006.tab:0398', 'uvim2006.tab:0460', 'uvim2006.tab:0522', 'uvim2006.tab:0584', 'uvim2006.tab:0646', 'uvim2006.tab:0708', 'uvim2006.tab:0770', 'uvim2006.tab:0832', 'uvim2006.tab:0894', 'uvim2006.tab:0956', 'uvim2006.tab:1018', 'uvim2006.tab:1080', 'uvim2006.tab:1142', 'uvim2006.tab:1204', 'uvim2006.tab:1266', 'uvim2006.tab:1328', 'uvim2006.tab:1390', 'uvim2006.tab:1452', 'uvim2006.tab:1514', 'uvim2006.tab:1576', 'uvim2006.tab:1638', 'uvim2006.tab:1700', 'uvim2006.tab:1762', 'uvim2006.tab:1824', 'uvim2006.tab:1886', 'uvim2006.tab:1948', 'uvim2006.tab:2010', 'uvim2006.tab:2072', 'uvim2006.tab:2134', 'uvim2006.tab:2196']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0130', 'uvim2006.tab:0132', 'uvim2006.tab:0133', 'uvim2006.tab:0134', 'uvim2006.tab:0336', 'uvim2006.tab:0398', 'uvim2006.tab:0460', 'uvim2006.tab:0522', 'uvim2006.tab:0584', 'uvim2006.tab:0646', 'uvim2006.tab:0708', 'uvim2006.tab:0770', 'uvim2006.tab:0832', 'uvim2006.tab:0894', 'uvim2006.tab:0956', 'uvim2006.tab:1018', 'uvim2006.tab:1080', 'uvim2006.tab:1142', 'uvim2006.tab:1204', 'uvim2006.tab:1266', 'uvim2006.tab:1328', 'uvim2006.tab:1390', 'uvim2006.tab:1452', 'uvim2006.tab:1514', 'uvim2006.tab:1576', 'uvim2006.tab:1638', 'uvim2006.tab:1700', 'uvim2006.tab:1762', 'uvim2006.tab:1824', 'uvim2006.tab:1886', 'uvim2006.tab:1948', 'uvim2006.tab:2010', 'uvim2006.tab:2072']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0130', 'uvim2006.tab:0132', 'uvim2006.tab:0133', 'uvim2006.tab:0134', 'uvim2006.tab:0336', 'uvim2006.tab:0398', 'uvim2006.tab:0460', 'uvim2006.tab:0522', 'uvim2006.tab:0584', 'uvim2006.tab:0646', 'uvim2006.tab:0708', 'uvim2006.tab:0770', 'uvim2006.tab:0832', 'uvim2006.tab:0894', 'uvim2006.tab:0956', 'uvim2006.tab:1018', 'uvim2006.tab:1080', 'uvim2006.tab:1142', 'uvim2006.tab:1204', 'uvim2006.tab:1266', 'uvim2006.tab:1328', 'uvim2006.tab:1390', 'uvim2006.tab:1452', 'uvim2006.tab:1514', 'uvim2006.tab:1576', 'uvim2006.tab:1638', 'uvim2006.tab:1700', 'uvim2006.tab:1762', 'uvim2006.tab:1824', 'uvim2006.tab:1886', 'uvim2006.tab:1948', 'uvim2006.tab:2010', 'uvim2006.tab:2072']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0131', 'uvim2006.tab:2134', 'uvim2006.tab:2196']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0131', 'uvim2006.tab:2134', 'uvim2006.tab:2196']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0135', 'uvim2006.tab:0136', 'uvim2006.tab:0137', 'uvim2006.tab:0138', 'uvim2006.tab:0139', 'uvim2006.tab:0337', 'uvim2006.tab:0399', 'uvim2006.tab:0461', 'uvim2006.tab:0523', 'uvim2006.tab:0585', 'uvim2006.tab:0647', 'uvim2006.tab:0709', 'uvim2006.tab:0771', 'uvim2006.tab:0833', 'uvim2006.tab:0895', 'uvim2006.tab:0957', 'uvim2006.tab:1019', 'uvim2006.tab:1081', 'uvim2006.tab:1143', 'uvim2006.tab:1205', 'uvim2006.tab:1267', 'uvim2006.tab:1329', 'uvim2006.tab:1391', 'uvim2006.tab:1453', 'uvim2006.tab:1515', 'uvim2006.tab:1577', 'uvim2006.tab:1639', 'uvim2006.tab:1701', 'uvim2006.tab:1763', 'uvim2006.tab:1825', 'uvim2006.tab:1887', 'uvim2006.tab:1949', 'uvim2006.tab:2011', 'uvim2006.tab:2073', 'uvim2006.tab:2135', 'uvim2006.tab:2197']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0135', 'uvim2006.tab:0136', 'uvim2006.tab:0137', 'uvim2006.tab:0138', 'uvim2006.tab:0139', 'uvim2006.tab:0337', 'uvim2006.tab:0399', 'uvim2006.tab:0461', 'uvim2006.tab:0523', 'uvim2006.tab:0585', 'uvim2006.tab:0647', 'uvim2006.tab:0709', 'uvim2006.tab:0771', 'uvim2006.tab:0833', 'uvim2006.tab:0895', 'uvim2006.tab:0957', 'uvim2006.tab:1019', 'uvim2006.tab:1081', 'uvim2006.tab:1143', 'uvim2006.tab:1205', 'uvim2006.tab:1267', 'uvim2006.tab:1329', 'uvim2006.tab:1391', 'uvim2006.tab:1453', 'uvim2006.tab:1515', 'uvim2006.tab:1577', 'uvim2006.tab:1639', 'uvim2006.tab:1701', 'uvim2006.tab:1763', 'uvim2006.tab:1825', 'uvim2006.tab:1887', 'uvim2006.tab:1949', 'uvim2006.tab:2011', 'uvim2006.tab:2073', 'uvim2006.tab:2135', 'uvim2006.tab:2197']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0135', 'uvim2006.tab:0137', 'uvim2006.tab:0138', 'uvim2006.tab:0139', 'uvim2006.tab:0337', 'uvim2006.tab:0399', 'uvim2006.tab:0461', 'uvim2006.tab:0523', 'uvim2006.tab:0585', 'uvim2006.tab:0647', 'uvim2006.tab:0709', 'uvim2006.tab:0771', 'uvim2006.tab:0833', 'uvim2006.tab:0895', 'uvim2006.tab:0957', 'uvim2006.tab:1019', 'uvim2006.tab:1081', 'uvim2006.tab:1143', 'uvim2006.tab:1205', 'uvim2006.tab:1267', 'uvim2006.tab:1329', 'uvim2006.tab:1391', 'uvim2006.tab:1453', 'uvim2006.tab:1515', 'uvim2006.tab:1577', 'uvim2006.tab:1639', 'uvim2006.tab:1701', 'uvim2006.tab:1763', 'uvim2006.tab:1825', 'uvim2006.tab:1887', 'uvim2006.tab:1949', 'uvim2006.tab:2011', 'uvim2006.tab:2073']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0135', 'uvim2006.tab:0137', 'uvim2006.tab:0138', 'uvim2006.tab:0139', 'uvim2006.tab:0337', 'uvim2006.tab:0399', 'uvim2006.tab:0461', 'uvim2006.tab:0523', 'uvim2006.tab:0585', 'uvim2006.tab:0647', 'uvim2006.tab:0709', 'uvim2006.tab:0771', 'uvim2006.tab:0833', 'uvim2006.tab:0895', 'uvim2006.tab:0957', 'uvim2006.tab:1019', 'uvim2006.tab:1081', 'uvim2006.tab:1143', 'uvim2006.tab:1205', 'uvim2006.tab:1267', 'uvim2006.tab:1329', 'uvim2006.tab:1391', 'uvim2006.tab:1453', 'uvim2006.tab:1515', 'uvim2006.tab:1577', 'uvim2006.tab:1639', 'uvim2006.tab:1701', 'uvim2006.tab:1763', 'uvim2006.tab:1825', 'uvim2006.tab:1887', 'uvim2006.tab:1949', 'uvim2006.tab:2011', 'uvim2006.tab:2073']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0136', 'uvim2006.tab:2135', 'uvim2006.tab:2197']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0136', 'uvim2006.tab:2135', 'uvim2006.tab:2197']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0140', 'uvim2006.tab:0141', 'uvim2006.tab:0142', 'uvim2006.tab:0143', 'uvim2006.tab:0144', 'uvim2006.tab:0338', 'uvim2006.tab:0400', 'uvim2006.tab:0462', 'uvim2006.tab:0524', 'uvim2006.tab:0586', 'uvim2006.tab:0648', 'uvim2006.tab:0710', 'uvim2006.tab:0772', 'uvim2006.tab:0834', 'uvim2006.tab:0896', 'uvim2006.tab:0958', 'uvim2006.tab:1020', 'uvim2006.tab:1082', 'uvim2006.tab:1144', 'uvim2006.tab:1206', 'uvim2006.tab:1268', 'uvim2006.tab:1330', 'uvim2006.tab:1392', 'uvim2006.tab:1454', 'uvim2006.tab:1516', 'uvim2006.tab:1578', 'uvim2006.tab:1640', 'uvim2006.tab:1702', 'uvim2006.tab:1764', 'uvim2006.tab:1826', 'uvim2006.tab:1888', 'uvim2006.tab:1950', 'uvim2006.tab:2012', 'uvim2006.tab:2074', 'uvim2006.tab:2136', 'uvim2006.tab:2198', 'uvim2006.tab:2366']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0140', 'uvim2006.tab:0141', 'uvim2006.tab:0142', 'uvim2006.tab:0143', 'uvim2006.tab:0144', 'uvim2006.tab:0338', 'uvim2006.tab:0400', 'uvim2006.tab:0462', 'uvim2006.tab:0524', 'uvim2006.tab:0586', 'uvim2006.tab:0648', 'uvim2006.tab:0710', 'uvim2006.tab:0772', 'uvim2006.tab:0834', 'uvim2006.tab:0896', 'uvim2006.tab:0958', 'uvim2006.tab:1020', 'uvim2006.tab:1082', 'uvim2006.tab:1144', 'uvim2006.tab:1206', 'uvim2006.tab:1268', 'uvim2006.tab:1330', 'uvim2006.tab:1392', 'uvim2006.tab:1454', 'uvim2006.tab:1516', 'uvim2006.tab:1578', 'uvim2006.tab:1640', 'uvim2006.tab:1702', 'uvim2006.tab:1764', 'uvim2006.tab:1826', 'uvim2006.tab:1888', 'uvim2006.tab:1950', 'uvim2006.tab:2012', 'uvim2006.tab:2074', 'uvim2006.tab:2136', 'uvim2006.tab:2198', 'uvim2006.tab:2366']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0140', 'uvim2006.tab:0142', 'uvim2006.tab:0143', 'uvim2006.tab:0144', 'uvim2006.tab:0338', 'uvim2006.tab:0400', 'uvim2006.tab:0462', 'uvim2006.tab:0524', 'uvim2006.tab:0586', 'uvim2006.tab:0648', 'uvim2006.tab:0710', 'uvim2006.tab:0772', 'uvim2006.tab:0834', 'uvim2006.tab:0896', 'uvim2006.tab:0958', 'uvim2006.tab:1020', 'uvim2006.tab:1082', 'uvim2006.tab:1144', 'uvim2006.tab:1206', 'uvim2006.tab:1268', 'uvim2006.tab:1330', 'uvim2006.tab:1392', 'uvim2006.tab:1454', 'uvim2006.tab:1516', 'uvim2006.tab:1578', 'uvim2006.tab:1640', 'uvim2006.tab:1702', 'uvim2006.tab:1764', 'uvim2006.tab:1826', 'uvim2006.tab:1888', 'uvim2006.tab:1950', 'uvim2006.tab:2012', 'uvim2006.tab:2074']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0140', 'uvim2006.tab:0142', 'uvim2006.tab:0143', 'uvim2006.tab:0144', 'uvim2006.tab:0338', 'uvim2006.tab:0400', 'uvim2006.tab:0462', 'uvim2006.tab:0524', 'uvim2006.tab:0586', 'uvim2006.tab:0648', 'uvim2006.tab:0710', 'uvim2006.tab:0772', 'uvim2006.tab:0834', 'uvim2006.tab:0896', 'uvim2006.tab:0958', 'uvim2006.tab:1020', 'uvim2006.tab:1082', 'uvim2006.tab:1144', 'uvim2006.tab:1206', 'uvim2006.tab:1268', 'uvim2006.tab:1330', 'uvim2006.tab:1392', 'uvim2006.tab:1454', 'uvim2006.tab:1516', 'uvim2006.tab:1578', 'uvim2006.tab:1640', 'uvim2006.tab:1702', 'uvim2006.tab:1764', 'uvim2006.tab:1826', 'uvim2006.tab:1888', 'uvim2006.tab:1950', 'uvim2006.tab:2012', 'uvim2006.tab:2074']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0141', 'uvim2006.tab:2136', 'uvim2006.tab:2198']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0141', 'uvim2006.tab:2136', 'uvim2006.tab:2198']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0145', 'uvim2006.tab:0146', 'uvim2006.tab:0147', 'uvim2006.tab:0148', 'uvim2006.tab:0149', 'uvim2006.tab:0339', 'uvim2006.tab:0401', 'uvim2006.tab:0463', 'uvim2006.tab:0525', 'uvim2006.tab:0587', 'uvim2006.tab:0649', 'uvim2006.tab:0711', 'uvim2006.tab:0773', 'uvim2006.tab:0835', 'uvim2006.tab:0897', 'uvim2006.tab:0959', 'uvim2006.tab:1021', 'uvim2006.tab:1083', 'uvim2006.tab:1145', 'uvim2006.tab:1207', 'uvim2006.tab:1269', 'uvim2006.tab:1331', 'uvim2006.tab:1393', 'uvim2006.tab:1455', 'uvim2006.tab:1517', 'uvim2006.tab:1579', 'uvim2006.tab:1641', 'uvim2006.tab:1703', 'uvim2006.tab:1765', 'uvim2006.tab:1827', 'uvim2006.tab:1889', 'uvim2006.tab:1951', 'uvim2006.tab:2013', 'uvim2006.tab:2075', 'uvim2006.tab:2137', 'uvim2006.tab:2199']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0145', 'uvim2006.tab:0146', 'uvim2006.tab:0147', 'uvim2006.tab:0148', 'uvim2006.tab:0149', 'uvim2006.tab:0339', 'uvim2006.tab:0401', 'uvim2006.tab:0463', 'uvim2006.tab:0525', 'uvim2006.tab:0587', 'uvim2006.tab:0649', 'uvim2006.tab:0711', 'uvim2006.tab:0773', 'uvim2006.tab:0835', 'uvim2006.tab:0897', 'uvim2006.tab:0959', 'uvim2006.tab:1021', 'uvim2006.tab:1083', 'uvim2006.tab:1145', 'uvim2006.tab:1207', 'uvim2006.tab:1269', 'uvim2006.tab:1331', 'uvim2006.tab:1393', 'uvim2006.tab:1455', 'uvim2006.tab:1517', 'uvim2006.tab:1579', 'uvim2006.tab:1641', 'uvim2006.tab:1703', 'uvim2006.tab:1765', 'uvim2006.tab:1827', 'uvim2006.tab:1889', 'uvim2006.tab:1951', 'uvim2006.tab:2013', 'uvim2006.tab:2075', 'uvim2006.tab:2137', 'uvim2006.tab:2199']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0145', 'uvim2006.tab:0147', 'uvim2006.tab:0148', 'uvim2006.tab:0149', 'uvim2006.tab:0339', 'uvim2006.tab:0401', 'uvim2006.tab:0463', 'uvim2006.tab:0525', 'uvim2006.tab:0587', 'uvim2006.tab:0649', 'uvim2006.tab:0711', 'uvim2006.tab:0773', 'uvim2006.tab:0835', 'uvim2006.tab:0897', 'uvim2006.tab:0959', 'uvim2006.tab:1021', 'uvim2006.tab:1083', 'uvim2006.tab:1145', 'uvim2006.tab:1207', 'uvim2006.tab:1269', 'uvim2006.tab:1331', 'uvim2006.tab:1393', 'uvim2006.tab:1455', 'uvim2006.tab:1517', 'uvim2006.tab:1579', 'uvim2006.tab:1641', 'uvim2006.tab:1703', 'uvim2006.tab:1765', 'uvim2006.tab:1827', 'uvim2006.tab:1889', 'uvim2006.tab:1951', 'uvim2006.tab:2013', 'uvim2006.tab:2075']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0145', 'uvim2006.tab:0147', 'uvim2006.tab:0148', 'uvim2006.tab:0149', 'uvim2006.tab:0339', 'uvim2006.tab:0401', 'uvim2006.tab:0463', 'uvim2006.tab:0525', 'uvim2006.tab:0587', 'uvim2006.tab:0649', 'uvim2006.tab:0711', 'uvim2006.tab:0773', 'uvim2006.tab:0835', 'uvim2006.tab:0897', 'uvim2006.tab:0959', 'uvim2006.tab:1021', 'uvim2006.tab:1083', 'uvim2006.tab:1145', 'uvim2006.tab:1207', 'uvim2006.tab:1269', 'uvim2006.tab:1331', 'uvim2006.tab:1393', 'uvim2006.tab:1455', 'uvim2006.tab:1517', 'uvim2006.tab:1579', 'uvim2006.tab:1641', 'uvim2006.tab:1703', 'uvim2006.tab:1765', 'uvim2006.tab:1827', 'uvim2006.tab:1889', 'uvim2006.tab:1951', 'uvim2006.tab:2013', 'uvim2006.tab:2075']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0146', 'uvim2006.tab:2137', 'uvim2006.tab:2199']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0146', 'uvim2006.tab:2137', 'uvim2006.tab:2199']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0150', 'uvim2006.tab:0151', 'uvim2006.tab:0152', 'uvim2006.tab:0153', 'uvim2006.tab:0154', 'uvim2006.tab:0340', 'uvim2006.tab:0402', 'uvim2006.tab:0464', 'uvim2006.tab:0526', 'uvim2006.tab:0588', 'uvim2006.tab:0650', 'uvim2006.tab:0712', 'uvim2006.tab:0774', 'uvim2006.tab:0836', 'uvim2006.tab:0898', 'uvim2006.tab:0960', 'uvim2006.tab:1022', 'uvim2006.tab:1084', 'uvim2006.tab:1146', 'uvim2006.tab:1208', 'uvim2006.tab:1270', 'uvim2006.tab:1332', 'uvim2006.tab:1394', 'uvim2006.tab:1456', 'uvim2006.tab:1518', 'uvim2006.tab:1580', 'uvim2006.tab:1642', 'uvim2006.tab:1704', 'uvim2006.tab:1766', 'uvim2006.tab:1828', 'uvim2006.tab:1890', 'uvim2006.tab:1952', 'uvim2006.tab:2014', 'uvim2006.tab:2076', 'uvim2006.tab:2138', 'uvim2006.tab:2200']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0150', 'uvim2006.tab:0151', 'uvim2006.tab:0152', 'uvim2006.tab:0153', 'uvim2006.tab:0154', 'uvim2006.tab:0340', 'uvim2006.tab:0402', 'uvim2006.tab:0464', 'uvim2006.tab:0526', 'uvim2006.tab:0588', 'uvim2006.tab:0650', 'uvim2006.tab:0712', 'uvim2006.tab:0774', 'uvim2006.tab:0836', 'uvim2006.tab:0898', 'uvim2006.tab:0960', 'uvim2006.tab:1022', 'uvim2006.tab:1084', 'uvim2006.tab:1146', 'uvim2006.tab:1208', 'uvim2006.tab:1270', 'uvim2006.tab:1332', 'uvim2006.tab:1394', 'uvim2006.tab:1456', 'uvim2006.tab:1518', 'uvim2006.tab:1580', 'uvim2006.tab:1642', 'uvim2006.tab:1704', 'uvim2006.tab:1766', 'uvim2006.tab:1828', 'uvim2006.tab:1890', 'uvim2006.tab:1952', 'uvim2006.tab:2014', 'uvim2006.tab:2076', 'uvim2006.tab:2138', 'uvim2006.tab:2200']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0150', 'uvim2006.tab:0152', 'uvim2006.tab:0153', 'uvim2006.tab:0154', 'uvim2006.tab:0340', 'uvim2006.tab:0402', 'uvim2006.tab:0464', 'uvim2006.tab:0526', 'uvim2006.tab:0588', 'uvim2006.tab:0650', 'uvim2006.tab:0712', 'uvim2006.tab:0774', 'uvim2006.tab:0836', 'uvim2006.tab:0898', 'uvim2006.tab:0960', 'uvim2006.tab:1022', 'uvim2006.tab:1084', 'uvim2006.tab:1146', 'uvim2006.tab:1208', 'uvim2006.tab:1270', 'uvim2006.tab:1332', 'uvim2006.tab:1394', 'uvim2006.tab:1456', 'uvim2006.tab:1518', 'uvim2006.tab:1580', 'uvim2006.tab:1642', 'uvim2006.tab:1704', 'uvim2006.tab:1766', 'uvim2006.tab:1828', 'uvim2006.tab:1890', 'uvim2006.tab:1952', 'uvim2006.tab:2014', 'uvim2006.tab:2076']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0150', 'uvim2006.tab:0152', 'uvim2006.tab:0153', 'uvim2006.tab:0154', 'uvim2006.tab:0340', 'uvim2006.tab:0402', 'uvim2006.tab:0464', 'uvim2006.tab:0526', 'uvim2006.tab:0588', 'uvim2006.tab:0650', 'uvim2006.tab:0712', 'uvim2006.tab:0774', 'uvim2006.tab:0836', 'uvim2006.tab:0898', 'uvim2006.tab:0960', 'uvim2006.tab:1022', 'uvim2006.tab:1084', 'uvim2006.tab:1146', 'uvim2006.tab:1208', 'uvim2006.tab:1270', 'uvim2006.tab:1332', 'uvim2006.tab:1394', 'uvim2006.tab:1456', 'uvim2006.tab:1518', 'uvim2006.tab:1580', 'uvim2006.tab:1642', 'uvim2006.tab:1704', 'uvim2006.tab:1766', 'uvim2006.tab:1828', 'uvim2006.tab:1890', 'uvim2006.tab:1952', 'uvim2006.tab:2014', 'uvim2006.tab:2076']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0151', 'uvim2006.tab:2138', 'uvim2006.tab:2200']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0151', 'uvim2006.tab:2138', 'uvim2006.tab:2200']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0155', 'uvim2006.tab:0156', 'uvim2006.tab:0157', 'uvim2006.tab:0158', 'uvim2006.tab:0159', 'uvim2006.tab:0341', 'uvim2006.tab:0403', 'uvim2006.tab:0465', 'uvim2006.tab:0527', 'uvim2006.tab:0589', 'uvim2006.tab:0651', 'uvim2006.tab:0713', 'uvim2006.tab:0775', 'uvim2006.tab:0837', 'uvim2006.tab:0899', 'uvim2006.tab:0961', 'uvim2006.tab:1023', 'uvim2006.tab:1085', 'uvim2006.tab:1147', 'uvim2006.tab:1209', 'uvim2006.tab:1271', 'uvim2006.tab:1333', 'uvim2006.tab:1395', 'uvim2006.tab:1457', 'uvim2006.tab:1519', 'uvim2006.tab:1581', 'uvim2006.tab:1643', 'uvim2006.tab:1705', 'uvim2006.tab:1767', 'uvim2006.tab:1829', 'uvim2006.tab:1891', 'uvim2006.tab:1953', 'uvim2006.tab:2015', 'uvim2006.tab:2077', 'uvim2006.tab:2139', 'uvim2006.tab:2201', 'uvim2006.tab:2328', 'uvim2006.tab:2329', 'uvim2006.tab:2330', 'uvim2006.tab:2331', 'uvim2006.tab:2332', 'uvim2006.tab:2333', 'uvim2006.tab:2334', 'uvim2006.tab:2335', 'uvim2006.tab:2336', 'uvim2006.tab:2337', 'uvim2006.tab:2338', 'uvim2006.tab:2339', 'uvim2006.tab:2340', 'uvim2006.tab:2341', 'uvim2006.tab:2342', 'uvim2006.tab:2343', 'uvim2006.tab:2344', 'uvim2006.tab:2345', 'uvim2006.tab:2346', 'uvim2006.tab:2347', 'uvim2006.tab:2348', 'uvim2006.tab:2349', 'uvim2006.tab:2350', 'uvim2006.tab:2351', 'uvim2006.tab:2352', 'uvim2006.tab:2353', 'uvim2006.tab:2354', 'uvim2006.tab:2355']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0155', 'uvim2006.tab:0156', 'uvim2006.tab:0157', 'uvim2006.tab:0158', 'uvim2006.tab:0159', 'uvim2006.tab:0341', 'uvim2006.tab:0403', 'uvim2006.tab:0465', 'uvim2006.tab:0527', 'uvim2006.tab:0589', 'uvim2006.tab:0651', 'uvim2006.tab:0713', 'uvim2006.tab:0775', 'uvim2006.tab:0837', 'uvim2006.tab:0899', 'uvim2006.tab:0961', 'uvim2006.tab:1023', 'uvim2006.tab:1085', 'uvim2006.tab:1147', 'uvim2006.tab:1209', 'uvim2006.tab:1271', 'uvim2006.tab:1333', 'uvim2006.tab:1395', 'uvim2006.tab:1457', 'uvim2006.tab:1519', 'uvim2006.tab:1581', 'uvim2006.tab:1643', 'uvim2006.tab:1705', 'uvim2006.tab:1767', 'uvim2006.tab:1829', 'uvim2006.tab:1891', 'uvim2006.tab:1953', 'uvim2006.tab:2015', 'uvim2006.tab:2077', 'uvim2006.tab:2139', 'uvim2006.tab:2201', 'uvim2006.tab:2328', 'uvim2006.tab:2329', 'uvim2006.tab:2330', 'uvim2006.tab:2331', 'uvim2006.tab:2332', 'uvim2006.tab:2333', 'uvim2006.tab:2334', 'uvim2006.tab:2335', 'uvim2006.tab:2336', 'uvim2006.tab:2337', 'uvim2006.tab:2338', 'uvim2006.tab:2339', 'uvim2006.tab:2340', 'uvim2006.tab:2341', 'uvim2006.tab:2342', 'uvim2006.tab:2343', 'uvim2006.tab:2344', 'uvim2006.tab:2345', 'uvim2006.tab:2346', 'uvim2006.tab:2347', 'uvim2006.tab:2348', 'uvim2006.tab:2349', 'uvim2006.tab:2350', 'uvim2006.tab:2351', 'uvim2006.tab:2352', 'uvim2006.tab:2353', 'uvim2006.tab:2354', 'uvim2006.tab:2355']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0155', 'uvim2006.tab:0157', 'uvim2006.tab:0158', 'uvim2006.tab:0159', 'uvim2006.tab:0341', 'uvim2006.tab:0403', 'uvim2006.tab:0465', 'uvim2006.tab:0527', 'uvim2006.tab:0589', 'uvim2006.tab:0651', 'uvim2006.tab:0713', 'uvim2006.tab:0775', 'uvim2006.tab:0837', 'uvim2006.tab:0899', 'uvim2006.tab:0961', 'uvim2006.tab:1023', 'uvim2006.tab:1085', 'uvim2006.tab:1147', 'uvim2006.tab:1209', 'uvim2006.tab:1271', 'uvim2006.tab:1333', 'uvim2006.tab:1395', 'uvim2006.tab:1457', 'uvim2006.tab:1519', 'uvim2006.tab:1581', 'uvim2006.tab:1643', 'uvim2006.tab:1705', 'uvim2006.tab:1767', 'uvim2006.tab:1829', 'uvim2006.tab:1891', 'uvim2006.tab:1953', 'uvim2006.tab:2015', 'uvim2006.tab:2077']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0155', 'uvim2006.tab:0157', 'uvim2006.tab:0158', 'uvim2006.tab:0159', 'uvim2006.tab:0341', 'uvim2006.tab:0403', 'uvim2006.tab:0465', 'uvim2006.tab:0527', 'uvim2006.tab:0589', 'uvim2006.tab:0651', 'uvim2006.tab:0713', 'uvim2006.tab:0775', 'uvim2006.tab:0837', 'uvim2006.tab:0899', 'uvim2006.tab:0961', 'uvim2006.tab:1023', 'uvim2006.tab:1085', 'uvim2006.tab:1147', 'uvim2006.tab:1209', 'uvim2006.tab:1271', 'uvim2006.tab:1333', 'uvim2006.tab:1395', 'uvim2006.tab:1457', 'uvim2006.tab:1519', 'uvim2006.tab:1581', 'uvim2006.tab:1643', 'uvim2006.tab:1705', 'uvim2006.tab:1767', 'uvim2006.tab:1829', 'uvim2006.tab:1891', 'uvim2006.tab:1953', 'uvim2006.tab:2015', 'uvim2006.tab:2077']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0156', 'uvim2006.tab:2139', 'uvim2006.tab:2201']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0156', 'uvim2006.tab:2139', 'uvim2006.tab:2201']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0160', 'uvim2006.tab:0161', 'uvim2006.tab:0162', 'uvim2006.tab:0163', 'uvim2006.tab:0164', 'uvim2006.tab:0342', 'uvim2006.tab:0404', 'uvim2006.tab:0466', 'uvim2006.tab:0528', 'uvim2006.tab:0590', 'uvim2006.tab:0652', 'uvim2006.tab:0714', 'uvim2006.tab:0776', 'uvim2006.tab:0838', 'uvim2006.tab:0900', 'uvim2006.tab:0962', 'uvim2006.tab:1024', 'uvim2006.tab:1086', 'uvim2006.tab:1148', 'uvim2006.tab:1210', 'uvim2006.tab:1272', 'uvim2006.tab:1334', 'uvim2006.tab:1396', 'uvim2006.tab:1458', 'uvim2006.tab:1520', 'uvim2006.tab:1582', 'uvim2006.tab:1644', 'uvim2006.tab:1706', 'uvim2006.tab:1768', 'uvim2006.tab:1830', 'uvim2006.tab:1892', 'uvim2006.tab:1954', 'uvim2006.tab:2016', 'uvim2006.tab:2078', 'uvim2006.tab:2140', 'uvim2006.tab:2202']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0160', 'uvim2006.tab:0161', 'uvim2006.tab:0162', 'uvim2006.tab:0163', 'uvim2006.tab:0164', 'uvim2006.tab:0342', 'uvim2006.tab:0404', 'uvim2006.tab:0466', 'uvim2006.tab:0528', 'uvim2006.tab:0590', 'uvim2006.tab:0652', 'uvim2006.tab:0714', 'uvim2006.tab:0776', 'uvim2006.tab:0838', 'uvim2006.tab:0900', 'uvim2006.tab:0962', 'uvim2006.tab:1024', 'uvim2006.tab:1086', 'uvim2006.tab:1148', 'uvim2006.tab:1210', 'uvim2006.tab:1272', 'uvim2006.tab:1334', 'uvim2006.tab:1396', 'uvim2006.tab:1458', 'uvim2006.tab:1520', 'uvim2006.tab:1582', 'uvim2006.tab:1644', 'uvim2006.tab:1706', 'uvim2006.tab:1768', 'uvim2006.tab:1830', 'uvim2006.tab:1892', 'uvim2006.tab:1954', 'uvim2006.tab:2016', 'uvim2006.tab:2078', 'uvim2006.tab:2140', 'uvim2006.tab:2202']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0160', 'uvim2006.tab:0162', 'uvim2006.tab:0163', 'uvim2006.tab:0164', 'uvim2006.tab:0342', 'uvim2006.tab:0404', 'uvim2006.tab:0466', 'uvim2006.tab:0528', 'uvim2006.tab:0590', 'uvim2006.tab:0652', 'uvim2006.tab:0714', 'uvim2006.tab:0776', 'uvim2006.tab:0838', 'uvim2006.tab:0900', 'uvim2006.tab:0962', 'uvim2006.tab:1024', 'uvim2006.tab:1086', 'uvim2006.tab:1148', 'uvim2006.tab:1210', 'uvim2006.tab:1272', 'uvim2006.tab:1334', 'uvim2006.tab:1396', 'uvim2006.tab:1458', 'uvim2006.tab:1520', 'uvim2006.tab:1582', 'uvim2006.tab:1644', 'uvim2006.tab:1706', 'uvim2006.tab:1768', 'uvim2006.tab:1830', 'uvim2006.tab:1892', 'uvim2006.tab:1954', 'uvim2006.tab:2016', 'uvim2006.tab:2078']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0160', 'uvim2006.tab:0162', 'uvim2006.tab:0163', 'uvim2006.tab:0164', 'uvim2006.tab:0342', 'uvim2006.tab:0404', 'uvim2006.tab:0466', 'uvim2006.tab:0528', 'uvim2006.tab:0590', 'uvim2006.tab:0652', 'uvim2006.tab:0714', 'uvim2006.tab:0776', 'uvim2006.tab:0838', 'uvim2006.tab:0900', 'uvim2006.tab:0962', 'uvim2006.tab:1024', 'uvim2006.tab:1086', 'uvim2006.tab:1148', 'uvim2006.tab:1210', 'uvim2006.tab:1272', 'uvim2006.tab:1334', 'uvim2006.tab:1396', 'uvim2006.tab:1458', 'uvim2006.tab:1520', 'uvim2006.tab:1582', 'uvim2006.tab:1644', 'uvim2006.tab:1706', 'uvim2006.tab:1768', 'uvim2006.tab:1830', 'uvim2006.tab:1892', 'uvim2006.tab:1954', 'uvim2006.tab:2016', 'uvim2006.tab:2078']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0161', 'uvim2006.tab:2140', 'uvim2006.tab:2202']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0161', 'uvim2006.tab:2140', 'uvim2006.tab:2202']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0165', 'uvim2006.tab:0166', 'uvim2006.tab:0167', 'uvim2006.tab:0168', 'uvim2006.tab:0169', 'uvim2006.tab:0343', 'uvim2006.tab:0405', 'uvim2006.tab:0467', 'uvim2006.tab:0529', 'uvim2006.tab:0591', 'uvim2006.tab:0653', 'uvim2006.tab:0715', 'uvim2006.tab:0777', 'uvim2006.tab:0839', 'uvim2006.tab:0901', 'uvim2006.tab:0963', 'uvim2006.tab:1025', 'uvim2006.tab:1087', 'uvim2006.tab:1149', 'uvim2006.tab:1211', 'uvim2006.tab:1273', 'uvim2006.tab:1335', 'uvim2006.tab:1397', 'uvim2006.tab:1459', 'uvim2006.tab:1521', 'uvim2006.tab:1583', 'uvim2006.tab:1645', 'uvim2006.tab:1707', 'uvim2006.tab:1769', 'uvim2006.tab:1831', 'uvim2006.tab:1893', 'uvim2006.tab:1955', 'uvim2006.tab:2017', 'uvim2006.tab:2079', 'uvim2006.tab:2141', 'uvim2006.tab:2203']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0165', 'uvim2006.tab:0166', 'uvim2006.tab:0167', 'uvim2006.tab:0168', 'uvim2006.tab:0169', 'uvim2006.tab:0343', 'uvim2006.tab:0405', 'uvim2006.tab:0467', 'uvim2006.tab:0529', 'uvim2006.tab:0591', 'uvim2006.tab:0653', 'uvim2006.tab:0715', 'uvim2006.tab:0777', 'uvim2006.tab:0839', 'uvim2006.tab:0901', 'uvim2006.tab:0963', 'uvim2006.tab:1025', 'uvim2006.tab:1087', 'uvim2006.tab:1149', 'uvim2006.tab:1211', 'uvim2006.tab:1273', 'uvim2006.tab:1335', 'uvim2006.tab:1397', 'uvim2006.tab:1459', 'uvim2006.tab:1521', 'uvim2006.tab:1583', 'uvim2006.tab:1645', 'uvim2006.tab:1707', 'uvim2006.tab:1769', 'uvim2006.tab:1831', 'uvim2006.tab:1893', 'uvim2006.tab:1955', 'uvim2006.tab:2017', 'uvim2006.tab:2079', 'uvim2006.tab:2141', 'uvim2006.tab:2203']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0165', 'uvim2006.tab:0167', 'uvim2006.tab:0168', 'uvim2006.tab:0169', 'uvim2006.tab:0343', 'uvim2006.tab:0405', 'uvim2006.tab:0467', 'uvim2006.tab:0529', 'uvim2006.tab:0591', 'uvim2006.tab:0653', 'uvim2006.tab:0715', 'uvim2006.tab:0777', 'uvim2006.tab:0839', 'uvim2006.tab:0901', 'uvim2006.tab:0963', 'uvim2006.tab:1025', 'uvim2006.tab:1087', 'uvim2006.tab:1149', 'uvim2006.tab:1211', 'uvim2006.tab:1273', 'uvim2006.tab:1335', 'uvim2006.tab:1397', 'uvim2006.tab:1459', 'uvim2006.tab:1521', 'uvim2006.tab:1583', 'uvim2006.tab:1645', 'uvim2006.tab:1707', 'uvim2006.tab:1769', 'uvim2006.tab:1831', 'uvim2006.tab:1893', 'uvim2006.tab:1955', 'uvim2006.tab:2017', 'uvim2006.tab:2079']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0165', 'uvim2006.tab:0167', 'uvim2006.tab:0168', 'uvim2006.tab:0169', 'uvim2006.tab:0343', 'uvim2006.tab:0405', 'uvim2006.tab:0467', 'uvim2006.tab:0529', 'uvim2006.tab:0591', 'uvim2006.tab:0653', 'uvim2006.tab:0715', 'uvim2006.tab:0777', 'uvim2006.tab:0839', 'uvim2006.tab:0901', 'uvim2006.tab:0963', 'uvim2006.tab:1025', 'uvim2006.tab:1087', 'uvim2006.tab:1149', 'uvim2006.tab:1211', 'uvim2006.tab:1273', 'uvim2006.tab:1335', 'uvim2006.tab:1397', 'uvim2006.tab:1459', 'uvim2006.tab:1521', 'uvim2006.tab:1583', 'uvim2006.tab:1645', 'uvim2006.tab:1707', 'uvim2006.tab:1769', 'uvim2006.tab:1831', 'uvim2006.tab:1893', 'uvim2006.tab:1955', 'uvim2006.tab:2017', 'uvim2006.tab:2079']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0166', 'uvim2006.tab:2141', 'uvim2006.tab:2203']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0166', 'uvim2006.tab:2141', 'uvim2006.tab:2203']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0170', 'uvim2006.tab:0171', 'uvim2006.tab:0172', 'uvim2006.tab:0173', 'uvim2006.tab:0174', 'uvim2006.tab:0344', 'uvim2006.tab:0406', 'uvim2006.tab:0468', 'uvim2006.tab:0530', 'uvim2006.tab:0592', 'uvim2006.tab:0654', 'uvim2006.tab:0716', 'uvim2006.tab:0778', 'uvim2006.tab:0840', 'uvim2006.tab:0902', 'uvim2006.tab:0964', 'uvim2006.tab:1026', 'uvim2006.tab:1088', 'uvim2006.tab:1150', 'uvim2006.tab:1212', 'uvim2006.tab:1274', 'uvim2006.tab:1336', 'uvim2006.tab:1398', 'uvim2006.tab:1460', 'uvim2006.tab:1522', 'uvim2006.tab:1584', 'uvim2006.tab:1646', 'uvim2006.tab:1708', 'uvim2006.tab:1770', 'uvim2006.tab:1832', 'uvim2006.tab:1894', 'uvim2006.tab:1956', 'uvim2006.tab:2018', 'uvim2006.tab:2080', 'uvim2006.tab:2142', 'uvim2006.tab:2204', 'uvim2006.tab:2232', 'uvim2006.tab:2233', 'uvim2006.tab:2234', 'uvim2006.tab:2235', 'uvim2006.tab:2236', 'uvim2006.tab:2237', 'uvim2006.tab:2238', 'uvim2006.tab:2239', 'uvim2006.tab:2240', 'uvim2006.tab:2241', 'uvim2006.tab:2242', 'uvim2006.tab:2243', 'uvim2006.tab:2244', 'uvim2006.tab:2245', 'uvim2006.tab:2246', 'uvim2006.tab:2247', 'uvim2006.tab:2248', 'uvim2006.tab:2249', 'uvim2006.tab:2250', 'uvim2006.tab:2251', 'uvim2006.tab:2252', 'uvim2006.tab:2253', 'uvim2006.tab:2254', 'uvim2006.tab:2255']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0170', 'uvim2006.tab:0171', 'uvim2006.tab:0172', 'uvim2006.tab:0173', 'uvim2006.tab:0174', 'uvim2006.tab:0344', 'uvim2006.tab:0406', 'uvim2006.tab:0468', 'uvim2006.tab:0530', 'uvim2006.tab:0592', 'uvim2006.tab:0654', 'uvim2006.tab:0716', 'uvim2006.tab:0778', 'uvim2006.tab:0840', 'uvim2006.tab:0902', 'uvim2006.tab:0964', 'uvim2006.tab:1026', 'uvim2006.tab:1088', 'uvim2006.tab:1150', 'uvim2006.tab:1212', 'uvim2006.tab:1274', 'uvim2006.tab:1336', 'uvim2006.tab:1398', 'uvim2006.tab:1460', 'uvim2006.tab:1522', 'uvim2006.tab:1584', 'uvim2006.tab:1646', 'uvim2006.tab:1708', 'uvim2006.tab:1770', 'uvim2006.tab:1832', 'uvim2006.tab:1894', 'uvim2006.tab:1956', 'uvim2006.tab:2018', 'uvim2006.tab:2080', 'uvim2006.tab:2142', 'uvim2006.tab:2204', 'uvim2006.tab:2232', 'uvim2006.tab:2233', 'uvim2006.tab:2234', 'uvim2006.tab:2235', 'uvim2006.tab:2236', 'uvim2006.tab:2237', 'uvim2006.tab:2238', 'uvim2006.tab:2239', 'uvim2006.tab:2240', 'uvim2006.tab:2241', 'uvim2006.tab:2242', 'uvim2006.tab:2243', 'uvim2006.tab:2244', 'uvim2006.tab:2245', 'uvim2006.tab:2246', 'uvim2006.tab:2247', 'uvim2006.tab:2248', 'uvim2006.tab:2249', 'uvim2006.tab:2250', 'uvim2006.tab:2251', 'uvim2006.tab:2252', 'uvim2006.tab:2253', 'uvim2006.tab:2254', 'uvim2006.tab:2255']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0170', 'uvim2006.tab:0172', 'uvim2006.tab:0173', 'uvim2006.tab:0174', 'uvim2006.tab:0344', 'uvim2006.tab:0406', 'uvim2006.tab:0468', 'uvim2006.tab:0530', 'uvim2006.tab:0592', 'uvim2006.tab:0654', 'uvim2006.tab:0716', 'uvim2006.tab:0778', 'uvim2006.tab:0840', 'uvim2006.tab:0902', 'uvim2006.tab:0964', 'uvim2006.tab:1026', 'uvim2006.tab:1088', 'uvim2006.tab:1150', 'uvim2006.tab:1212', 'uvim2006.tab:1274', 'uvim2006.tab:1336', 'uvim2006.tab:1398', 'uvim2006.tab:1460', 'uvim2006.tab:1522', 'uvim2006.tab:1584', 'uvim2006.tab:1646', 'uvim2006.tab:1708', 'uvim2006.tab:1770', 'uvim2006.tab:1832', 'uvim2006.tab:1894', 'uvim2006.tab:1956', 'uvim2006.tab:2018', 'uvim2006.tab:2080']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0170', 'uvim2006.tab:0172', 'uvim2006.tab:0173', 'uvim2006.tab:0174', 'uvim2006.tab:0344', 'uvim2006.tab:0406', 'uvim2006.tab:0468', 'uvim2006.tab:0530', 'uvim2006.tab:0592', 'uvim2006.tab:0654', 'uvim2006.tab:0716', 'uvim2006.tab:0778', 'uvim2006.tab:0840', 'uvim2006.tab:0902', 'uvim2006.tab:0964', 'uvim2006.tab:1026', 'uvim2006.tab:1088', 'uvim2006.tab:1150', 'uvim2006.tab:1212', 'uvim2006.tab:1274', 'uvim2006.tab:1336', 'uvim2006.tab:1398', 'uvim2006.tab:1460', 'uvim2006.tab:1522', 'uvim2006.tab:1584', 'uvim2006.tab:1646', 'uvim2006.tab:1708', 'uvim2006.tab:1770', 'uvim2006.tab:1832', 'uvim2006.tab:1894', 'uvim2006.tab:1956', 'uvim2006.tab:2018', 'uvim2006.tab:2080']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0171', 'uvim2006.tab:2142', 'uvim2006.tab:2204']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0171', 'uvim2006.tab:2142', 'uvim2006.tab:2204']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0175', 'uvim2006.tab:0176', 'uvim2006.tab:0177', 'uvim2006.tab:0178', 'uvim2006.tab:0179', 'uvim2006.tab:0345', 'uvim2006.tab:0407', 'uvim2006.tab:0469', 'uvim2006.tab:0531', 'uvim2006.tab:0593', 'uvim2006.tab:0655', 'uvim2006.tab:0717', 'uvim2006.tab:0779', 'uvim2006.tab:0841', 'uvim2006.tab:0903', 'uvim2006.tab:0965', 'uvim2006.tab:1027', 'uvim2006.tab:1089', 'uvim2006.tab:1151', 'uvim2006.tab:1213', 'uvim2006.tab:1275', 'uvim2006.tab:1337', 'uvim2006.tab:1399', 'uvim2006.tab:1461', 'uvim2006.tab:1523', 'uvim2006.tab:1585', 'uvim2006.tab:1647', 'uvim2006.tab:1709', 'uvim2006.tab:1771', 'uvim2006.tab:1833', 'uvim2006.tab:1895', 'uvim2006.tab:1957', 'uvim2006.tab:2019', 'uvim2006.tab:2081', 'uvim2006.tab:2143', 'uvim2006.tab:2205']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0175', 'uvim2006.tab:0176', 'uvim2006.tab:0177', 'uvim2006.tab:0178', 'uvim2006.tab:0179', 'uvim2006.tab:0345', 'uvim2006.tab:0407', 'uvim2006.tab:0469', 'uvim2006.tab:0531', 'uvim2006.tab:0593', 'uvim2006.tab:0655', 'uvim2006.tab:0717', 'uvim2006.tab:0779', 'uvim2006.tab:0841', 'uvim2006.tab:0903', 'uvim2006.tab:0965', 'uvim2006.tab:1027', 'uvim2006.tab:1089', 'uvim2006.tab:1151', 'uvim2006.tab:1213', 'uvim2006.tab:1275', 'uvim2006.tab:1337', 'uvim2006.tab:1399', 'uvim2006.tab:1461', 'uvim2006.tab:1523', 'uvim2006.tab:1585', 'uvim2006.tab:1647', 'uvim2006.tab:1709', 'uvim2006.tab:1771', 'uvim2006.tab:1833', 'uvim2006.tab:1895', 'uvim2006.tab:1957', 'uvim2006.tab:2019', 'uvim2006.tab:2081', 'uvim2006.tab:2143', 'uvim2006.tab:2205']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0175', 'uvim2006.tab:0177', 'uvim2006.tab:0178', 'uvim2006.tab:0179', 'uvim2006.tab:0345', 'uvim2006.tab:0407', 'uvim2006.tab:0469', 'uvim2006.tab:0531', 'uvim2006.tab:0593', 'uvim2006.tab:0655', 'uvim2006.tab:0717', 'uvim2006.tab:0779', 'uvim2006.tab:0841', 'uvim2006.tab:0903', 'uvim2006.tab:0965', 'uvim2006.tab:1027', 'uvim2006.tab:1089', 'uvim2006.tab:1151', 'uvim2006.tab:1213', 'uvim2006.tab:1275', 'uvim2006.tab:1337', 'uvim2006.tab:1399', 'uvim2006.tab:1461', 'uvim2006.tab:1523', 'uvim2006.tab:1585', 'uvim2006.tab:1647', 'uvim2006.tab:1709', 'uvim2006.tab:1771', 'uvim2006.tab:1833', 'uvim2006.tab:1895', 'uvim2006.tab:1957', 'uvim2006.tab:2019', 'uvim2006.tab:2081']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0175', 'uvim2006.tab:0177', 'uvim2006.tab:0178', 'uvim2006.tab:0179', 'uvim2006.tab:0345', 'uvim2006.tab:0407', 'uvim2006.tab:0469', 'uvim2006.tab:0531', 'uvim2006.tab:0593', 'uvim2006.tab:0655', 'uvim2006.tab:0717', 'uvim2006.tab:0779', 'uvim2006.tab:0841', 'uvim2006.tab:0903', 'uvim2006.tab:0965', 'uvim2006.tab:1027', 'uvim2006.tab:1089', 'uvim2006.tab:1151', 'uvim2006.tab:1213', 'uvim2006.tab:1275', 'uvim2006.tab:1337', 'uvim2006.tab:1399', 'uvim2006.tab:1461', 'uvim2006.tab:1523', 'uvim2006.tab:1585', 'uvim2006.tab:1647', 'uvim2006.tab:1709', 'uvim2006.tab:1771', 'uvim2006.tab:1833', 'uvim2006.tab:1895', 'uvim2006.tab:1957', 'uvim2006.tab:2019', 'uvim2006.tab:2081']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0176', 'uvim2006.tab:2143', 'uvim2006.tab:2205']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0176', 'uvim2006.tab:2143', 'uvim2006.tab:2205']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0180', 'uvim2006.tab:0181', 'uvim2006.tab:0182', 'uvim2006.tab:0183', 'uvim2006.tab:0184', 'uvim2006.tab:0346', 'uvim2006.tab:0408', 'uvim2006.tab:0470', 'uvim2006.tab:0532', 'uvim2006.tab:0594', 'uvim2006.tab:0656', 'uvim2006.tab:0718', 'uvim2006.tab:0780', 'uvim2006.tab:0842', 'uvim2006.tab:0904', 'uvim2006.tab:0966', 'uvim2006.tab:1028', 'uvim2006.tab:1090', 'uvim2006.tab:1152', 'uvim2006.tab:1214', 'uvim2006.tab:1276', 'uvim2006.tab:1338', 'uvim2006.tab:1400', 'uvim2006.tab:1462', 'uvim2006.tab:1524', 'uvim2006.tab:1586', 'uvim2006.tab:1648', 'uvim2006.tab:1710', 'uvim2006.tab:1772', 'uvim2006.tab:1834', 'uvim2006.tab:1896', 'uvim2006.tab:1958', 'uvim2006.tab:2020', 'uvim2006.tab:2082', 'uvim2006.tab:2144', 'uvim2006.tab:2206']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0180', 'uvim2006.tab:0181', 'uvim2006.tab:0182', 'uvim2006.tab:0183', 'uvim2006.tab:0184', 'uvim2006.tab:0346', 'uvim2006.tab:0408', 'uvim2006.tab:0470', 'uvim2006.tab:0532', 'uvim2006.tab:0594', 'uvim2006.tab:0656', 'uvim2006.tab:0718', 'uvim2006.tab:0780', 'uvim2006.tab:0842', 'uvim2006.tab:0904', 'uvim2006.tab:0966', 'uvim2006.tab:1028', 'uvim2006.tab:1090', 'uvim2006.tab:1152', 'uvim2006.tab:1214', 'uvim2006.tab:1276', 'uvim2006.tab:1338', 'uvim2006.tab:1400', 'uvim2006.tab:1462', 'uvim2006.tab:1524', 'uvim2006.tab:1586', 'uvim2006.tab:1648', 'uvim2006.tab:1710', 'uvim2006.tab:1772', 'uvim2006.tab:1834', 'uvim2006.tab:1896', 'uvim2006.tab:1958', 'uvim2006.tab:2020', 'uvim2006.tab:2082', 'uvim2006.tab:2144', 'uvim2006.tab:2206']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0180', 'uvim2006.tab:0182', 'uvim2006.tab:0183', 'uvim2006.tab:0184', 'uvim2006.tab:0346', 'uvim2006.tab:0408', 'uvim2006.tab:0470', 'uvim2006.tab:0532', 'uvim2006.tab:0594', 'uvim2006.tab:0656', 'uvim2006.tab:0718', 'uvim2006.tab:0780', 'uvim2006.tab:0842', 'uvim2006.tab:0904', 'uvim2006.tab:0966', 'uvim2006.tab:1028', 'uvim2006.tab:1090', 'uvim2006.tab:1152', 'uvim2006.tab:1214', 'uvim2006.tab:1276', 'uvim2006.tab:1338', 'uvim2006.tab:1400', 'uvim2006.tab:1462', 'uvim2006.tab:1524', 'uvim2006.tab:1586', 'uvim2006.tab:1648', 'uvim2006.tab:1710', 'uvim2006.tab:1772', 'uvim2006.tab:1834', 'uvim2006.tab:1896', 'uvim2006.tab:1958', 'uvim2006.tab:2020', 'uvim2006.tab:2082']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0180', 'uvim2006.tab:0182', 'uvim2006.tab:0183', 'uvim2006.tab:0184', 'uvim2006.tab:0346', 'uvim2006.tab:0408', 'uvim2006.tab:0470', 'uvim2006.tab:0532', 'uvim2006.tab:0594', 'uvim2006.tab:0656', 'uvim2006.tab:0718', 'uvim2006.tab:0780', 'uvim2006.tab:0842', 'uvim2006.tab:0904', 'uvim2006.tab:0966', 'uvim2006.tab:1028', 'uvim2006.tab:1090', 'uvim2006.tab:1152', 'uvim2006.tab:1214', 'uvim2006.tab:1276', 'uvim2006.tab:1338', 'uvim2006.tab:1400', 'uvim2006.tab:1462', 'uvim2006.tab:1524', 'uvim2006.tab:1586', 'uvim2006.tab:1648', 'uvim2006.tab:1710', 'uvim2006.tab:1772', 'uvim2006.tab:1834', 'uvim2006.tab:1896', 'uvim2006.tab:1958', 'uvim2006.tab:2020', 'uvim2006.tab:2082']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0181', 'uvim2006.tab:2144', 'uvim2006.tab:2206']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0181', 'uvim2006.tab:2144', 'uvim2006.tab:2206']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0185', 'uvim2006.tab:0186', 'uvim2006.tab:0187', 'uvim2006.tab:0188', 'uvim2006.tab:0189', 'uvim2006.tab:0347', 'uvim2006.tab:0409', 'uvim2006.tab:0471', 'uvim2006.tab:0533', 'uvim2006.tab:0595', 'uvim2006.tab:0657', 'uvim2006.tab:0719', 'uvim2006.tab:0781', 'uvim2006.tab:0843', 'uvim2006.tab:0905', 'uvim2006.tab:0967', 'uvim2006.tab:1029', 'uvim2006.tab:1091', 'uvim2006.tab:1153', 'uvim2006.tab:1215', 'uvim2006.tab:1277', 'uvim2006.tab:1339', 'uvim2006.tab:1401', 'uvim2006.tab:1463', 'uvim2006.tab:1525', 'uvim2006.tab:1587', 'uvim2006.tab:1649', 'uvim2006.tab:1711', 'uvim2006.tab:1773', 'uvim2006.tab:1835', 'uvim2006.tab:1897', 'uvim2006.tab:1959', 'uvim2006.tab:2021', 'uvim2006.tab:2083', 'uvim2006.tab:2145', 'uvim2006.tab:2207']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0185', 'uvim2006.tab:0186', 'uvim2006.tab:0187', 'uvim2006.tab:0188', 'uvim2006.tab:0189', 'uvim2006.tab:0347', 'uvim2006.tab:0409', 'uvim2006.tab:0471', 'uvim2006.tab:0533', 'uvim2006.tab:0595', 'uvim2006.tab:0657', 'uvim2006.tab:0719', 'uvim2006.tab:0781', 'uvim2006.tab:0843', 'uvim2006.tab:0905', 'uvim2006.tab:0967', 'uvim2006.tab:1029', 'uvim2006.tab:1091', 'uvim2006.tab:1153', 'uvim2006.tab:1215', 'uvim2006.tab:1277', 'uvim2006.tab:1339', 'uvim2006.tab:1401', 'uvim2006.tab:1463', 'uvim2006.tab:1525', 'uvim2006.tab:1587', 'uvim2006.tab:1649', 'uvim2006.tab:1711', 'uvim2006.tab:1773', 'uvim2006.tab:1835', 'uvim2006.tab:1897', 'uvim2006.tab:1959', 'uvim2006.tab:2021', 'uvim2006.tab:2083', 'uvim2006.tab:2145', 'uvim2006.tab:2207']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0185', 'uvim2006.tab:0187', 'uvim2006.tab:0188', 'uvim2006.tab:0189', 'uvim2006.tab:0347', 'uvim2006.tab:0409', 'uvim2006.tab:0471', 'uvim2006.tab:0533', 'uvim2006.tab:0595', 'uvim2006.tab:0657', 'uvim2006.tab:0719', 'uvim2006.tab:0781', 'uvim2006.tab:0843', 'uvim2006.tab:0905', 'uvim2006.tab:0967', 'uvim2006.tab:1029', 'uvim2006.tab:1091', 'uvim2006.tab:1153', 'uvim2006.tab:1215', 'uvim2006.tab:1277', 'uvim2006.tab:1339', 'uvim2006.tab:1401', 'uvim2006.tab:1463', 'uvim2006.tab:1525', 'uvim2006.tab:1587', 'uvim2006.tab:1649', 'uvim2006.tab:1711', 'uvim2006.tab:1773', 'uvim2006.tab:1835', 'uvim2006.tab:1897', 'uvim2006.tab:1959', 'uvim2006.tab:2021', 'uvim2006.tab:2083']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0185', 'uvim2006.tab:0187', 'uvim2006.tab:0188', 'uvim2006.tab:0189', 'uvim2006.tab:0347', 'uvim2006.tab:0409', 'uvim2006.tab:0471', 'uvim2006.tab:0533', 'uvim2006.tab:0595', 'uvim2006.tab:0657', 'uvim2006.tab:0719', 'uvim2006.tab:0781', 'uvim2006.tab:0843', 'uvim2006.tab:0905', 'uvim2006.tab:0967', 'uvim2006.tab:1029', 'uvim2006.tab:1091', 'uvim2006.tab:1153', 'uvim2006.tab:1215', 'uvim2006.tab:1277', 'uvim2006.tab:1339', 'uvim2006.tab:1401', 'uvim2006.tab:1463', 'uvim2006.tab:1525', 'uvim2006.tab:1587', 'uvim2006.tab:1649', 'uvim2006.tab:1711', 'uvim2006.tab:1773', 'uvim2006.tab:1835', 'uvim2006.tab:1897', 'uvim2006.tab:1959', 'uvim2006.tab:2021', 'uvim2006.tab:2083']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0186', 'uvim2006.tab:2145', 'uvim2006.tab:2207']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0186', 'uvim2006.tab:2145', 'uvim2006.tab:2207']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0190', 'uvim2006.tab:0191', 'uvim2006.tab:0192', 'uvim2006.tab:0193', 'uvim2006.tab:0194', 'uvim2006.tab:0348', 'uvim2006.tab:0410', 'uvim2006.tab:0472', 'uvim2006.tab:0534', 'uvim2006.tab:0596', 'uvim2006.tab:0658', 'uvim2006.tab:0720', 'uvim2006.tab:0782', 'uvim2006.tab:0844', 'uvim2006.tab:0906', 'uvim2006.tab:0968', 'uvim2006.tab:1030', 'uvim2006.tab:1092', 'uvim2006.tab:1154', 'uvim2006.tab:1216', 'uvim2006.tab:1278', 'uvim2006.tab:1340', 'uvim2006.tab:1402', 'uvim2006.tab:1464', 'uvim2006.tab:1526', 'uvim2006.tab:1588', 'uvim2006.tab:1650', 'uvim2006.tab:1712', 'uvim2006.tab:1774', 'uvim2006.tab:1836', 'uvim2006.tab:1898', 'uvim2006.tab:1960', 'uvim2006.tab:2022', 'uvim2006.tab:2084', 'uvim2006.tab:2146', 'uvim2006.tab:2208']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0190', 'uvim2006.tab:0191', 'uvim2006.tab:0192', 'uvim2006.tab:0193', 'uvim2006.tab:0194', 'uvim2006.tab:0348', 'uvim2006.tab:0410', 'uvim2006.tab:0472', 'uvim2006.tab:0534', 'uvim2006.tab:0596', 'uvim2006.tab:0658', 'uvim2006.tab:0720', 'uvim2006.tab:0782', 'uvim2006.tab:0844', 'uvim2006.tab:0906', 'uvim2006.tab:0968', 'uvim2006.tab:1030', 'uvim2006.tab:1092', 'uvim2006.tab:1154', 'uvim2006.tab:1216', 'uvim2006.tab:1278', 'uvim2006.tab:1340', 'uvim2006.tab:1402', 'uvim2006.tab:1464', 'uvim2006.tab:1526', 'uvim2006.tab:1588', 'uvim2006.tab:1650', 'uvim2006.tab:1712', 'uvim2006.tab:1774', 'uvim2006.tab:1836', 'uvim2006.tab:1898', 'uvim2006.tab:1960', 'uvim2006.tab:2022', 'uvim2006.tab:2084', 'uvim2006.tab:2146', 'uvim2006.tab:2208']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0190', 'uvim2006.tab:0192', 'uvim2006.tab:0193', 'uvim2006.tab:0194', 'uvim2006.tab:0348', 'uvim2006.tab:0410', 'uvim2006.tab:0472', 'uvim2006.tab:0534', 'uvim2006.tab:0596', 'uvim2006.tab:0658', 'uvim2006.tab:0720', 'uvim2006.tab:0782', 'uvim2006.tab:0844', 'uvim2006.tab:0906', 'uvim2006.tab:0968', 'uvim2006.tab:1030', 'uvim2006.tab:1092', 'uvim2006.tab:1154', 'uvim2006.tab:1216', 'uvim2006.tab:1278', 'uvim2006.tab:1340', 'uvim2006.tab:1402', 'uvim2006.tab:1464', 'uvim2006.tab:1526', 'uvim2006.tab:1588', 'uvim2006.tab:1650', 'uvim2006.tab:1712', 'uvim2006.tab:1774', 'uvim2006.tab:1836', 'uvim2006.tab:1898', 'uvim2006.tab:1960', 'uvim2006.tab:2022', 'uvim2006.tab:2084']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0190', 'uvim2006.tab:0192', 'uvim2006.tab:0193', 'uvim2006.tab:0194', 'uvim2006.tab:0348', 'uvim2006.tab:0410', 'uvim2006.tab:0472', 'uvim2006.tab:0534', 'uvim2006.tab:0596', 'uvim2006.tab:0658', 'uvim2006.tab:0720', 'uvim2006.tab:0782', 'uvim2006.tab:0844', 'uvim2006.tab:0906', 'uvim2006.tab:0968', 'uvim2006.tab:1030', 'uvim2006.tab:1092', 'uvim2006.tab:1154', 'uvim2006.tab:1216', 'uvim2006.tab:1278', 'uvim2006.tab:1340', 'uvim2006.tab:1402', 'uvim2006.tab:1464', 'uvim2006.tab:1526', 'uvim2006.tab:1588', 'uvim2006.tab:1650', 'uvim2006.tab:1712', 'uvim2006.tab:1774', 'uvim2006.tab:1836', 'uvim2006.tab:1898', 'uvim2006.tab:1960', 'uvim2006.tab:2022', 'uvim2006.tab:2084']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0191', 'uvim2006.tab:2146', 'uvim2006.tab:2208']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0191', 'uvim2006.tab:2146', 'uvim2006.tab:2208']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0195', 'uvim2006.tab:0196', 'uvim2006.tab:0197', 'uvim2006.tab:0198', 'uvim2006.tab:0199', 'uvim2006.tab:0349', 'uvim2006.tab:0411', 'uvim2006.tab:0473', 'uvim2006.tab:0535', 'uvim2006.tab:0597', 'uvim2006.tab:0659', 'uvim2006.tab:0721', 'uvim2006.tab:0783', 'uvim2006.tab:0845', 'uvim2006.tab:0907', 'uvim2006.tab:0969', 'uvim2006.tab:1031', 'uvim2006.tab:1093', 'uvim2006.tab:1155', 'uvim2006.tab:1217', 'uvim2006.tab:1279', 'uvim2006.tab:1341', 'uvim2006.tab:1403', 'uvim2006.tab:1465', 'uvim2006.tab:1527', 'uvim2006.tab:1589', 'uvim2006.tab:1651', 'uvim2006.tab:1713', 'uvim2006.tab:1775', 'uvim2006.tab:1837', 'uvim2006.tab:1899', 'uvim2006.tab:1961', 'uvim2006.tab:2023', 'uvim2006.tab:2085', 'uvim2006.tab:2147', 'uvim2006.tab:2209']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0195', 'uvim2006.tab:0196', 'uvim2006.tab:0197', 'uvim2006.tab:0198', 'uvim2006.tab:0199', 'uvim2006.tab:0349', 'uvim2006.tab:0411', 'uvim2006.tab:0473', 'uvim2006.tab:0535', 'uvim2006.tab:0597', 'uvim2006.tab:0659', 'uvim2006.tab:0721', 'uvim2006.tab:0783', 'uvim2006.tab:0845', 'uvim2006.tab:0907', 'uvim2006.tab:0969', 'uvim2006.tab:1031', 'uvim2006.tab:1093', 'uvim2006.tab:1155', 'uvim2006.tab:1217', 'uvim2006.tab:1279', 'uvim2006.tab:1341', 'uvim2006.tab:1403', 'uvim2006.tab:1465', 'uvim2006.tab:1527', 'uvim2006.tab:1589', 'uvim2006.tab:1651', 'uvim2006.tab:1713', 'uvim2006.tab:1775', 'uvim2006.tab:1837', 'uvim2006.tab:1899', 'uvim2006.tab:1961', 'uvim2006.tab:2023', 'uvim2006.tab:2085', 'uvim2006.tab:2147', 'uvim2006.tab:2209']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0195', 'uvim2006.tab:0197', 'uvim2006.tab:0198', 'uvim2006.tab:0199', 'uvim2006.tab:0349', 'uvim2006.tab:0411', 'uvim2006.tab:0473', 'uvim2006.tab:0535', 'uvim2006.tab:0597', 'uvim2006.tab:0659', 'uvim2006.tab:0721', 'uvim2006.tab:0783', 'uvim2006.tab:0845', 'uvim2006.tab:0907', 'uvim2006.tab:0969', 'uvim2006.tab:1031', 'uvim2006.tab:1093', 'uvim2006.tab:1155', 'uvim2006.tab:1217', 'uvim2006.tab:1279', 'uvim2006.tab:1341', 'uvim2006.tab:1403', 'uvim2006.tab:1465', 'uvim2006.tab:1527', 'uvim2006.tab:1589', 'uvim2006.tab:1651', 'uvim2006.tab:1713', 'uvim2006.tab:1775', 'uvim2006.tab:1837', 'uvim2006.tab:1899', 'uvim2006.tab:1961', 'uvim2006.tab:2023', 'uvim2006.tab:2085']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0195', 'uvim2006.tab:0197', 'uvim2006.tab:0198', 'uvim2006.tab:0199', 'uvim2006.tab:0349', 'uvim2006.tab:0411', 'uvim2006.tab:0473', 'uvim2006.tab:0535', 'uvim2006.tab:0597', 'uvim2006.tab:0659', 'uvim2006.tab:0721', 'uvim2006.tab:0783', 'uvim2006.tab:0845', 'uvim2006.tab:0907', 'uvim2006.tab:0969', 'uvim2006.tab:1031', 'uvim2006.tab:1093', 'uvim2006.tab:1155', 'uvim2006.tab:1217', 'uvim2006.tab:1279', 'uvim2006.tab:1341', 'uvim2006.tab:1403', 'uvim2006.tab:1465', 'uvim2006.tab:1527', 'uvim2006.tab:1589', 'uvim2006.tab:1651', 'uvim2006.tab:1713', 'uvim2006.tab:1775', 'uvim2006.tab:1837', 'uvim2006.tab:1899', 'uvim2006.tab:1961', 'uvim2006.tab:2023', 'uvim2006.tab:2085']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0196', 'uvim2006.tab:2147', 'uvim2006.tab:2209']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0196', 'uvim2006.tab:2147', 'uvim2006.tab:2209']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0200', 'uvim2006.tab:0201', 'uvim2006.tab:0202', 'uvim2006.tab:0203', 'uvim2006.tab:0204', 'uvim2006.tab:0350', 'uvim2006.tab:0412', 'uvim2006.tab:0474', 'uvim2006.tab:0536', 'uvim2006.tab:0598', 'uvim2006.tab:0660', 'uvim2006.tab:0722', 'uvim2006.tab:0784', 'uvim2006.tab:0846', 'uvim2006.tab:0908', 'uvim2006.tab:0970', 'uvim2006.tab:1032', 'uvim2006.tab:1094', 'uvim2006.tab:1156', 'uvim2006.tab:1218', 'uvim2006.tab:1280', 'uvim2006.tab:1342', 'uvim2006.tab:1404', 'uvim2006.tab:1466', 'uvim2006.tab:1528', 'uvim2006.tab:1590', 'uvim2006.tab:1652', 'uvim2006.tab:1714', 'uvim2006.tab:1776', 'uvim2006.tab:1838', 'uvim2006.tab:1900', 'uvim2006.tab:1962', 'uvim2006.tab:2024', 'uvim2006.tab:2086', 'uvim2006.tab:2148', 'uvim2006.tab:2210']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0200', 'uvim2006.tab:0201', 'uvim2006.tab:0202', 'uvim2006.tab:0203', 'uvim2006.tab:0204', 'uvim2006.tab:0350', 'uvim2006.tab:0412', 'uvim2006.tab:0474', 'uvim2006.tab:0536', 'uvim2006.tab:0598', 'uvim2006.tab:0660', 'uvim2006.tab:0722', 'uvim2006.tab:0784', 'uvim2006.tab:0846', 'uvim2006.tab:0908', 'uvim2006.tab:0970', 'uvim2006.tab:1032', 'uvim2006.tab:1094', 'uvim2006.tab:1156', 'uvim2006.tab:1218', 'uvim2006.tab:1280', 'uvim2006.tab:1342', 'uvim2006.tab:1404', 'uvim2006.tab:1466', 'uvim2006.tab:1528', 'uvim2006.tab:1590', 'uvim2006.tab:1652', 'uvim2006.tab:1714', 'uvim2006.tab:1776', 'uvim2006.tab:1838', 'uvim2006.tab:1900', 'uvim2006.tab:1962', 'uvim2006.tab:2024', 'uvim2006.tab:2086', 'uvim2006.tab:2148', 'uvim2006.tab:2210']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0200', 'uvim2006.tab:0202', 'uvim2006.tab:0203', 'uvim2006.tab:0204', 'uvim2006.tab:0350', 'uvim2006.tab:0412', 'uvim2006.tab:0474', 'uvim2006.tab:0536', 'uvim2006.tab:0598', 'uvim2006.tab:0660', 'uvim2006.tab:0722', 'uvim2006.tab:0784', 'uvim2006.tab:0846', 'uvim2006.tab:0908', 'uvim2006.tab:0970', 'uvim2006.tab:1032', 'uvim2006.tab:1094', 'uvim2006.tab:1156', 'uvim2006.tab:1218', 'uvim2006.tab:1280', 'uvim2006.tab:1342', 'uvim2006.tab:1404', 'uvim2006.tab:1466', 'uvim2006.tab:1528', 'uvim2006.tab:1590', 'uvim2006.tab:1652', 'uvim2006.tab:1714', 'uvim2006.tab:1776', 'uvim2006.tab:1838', 'uvim2006.tab:1900', 'uvim2006.tab:1962', 'uvim2006.tab:2024', 'uvim2006.tab:2086']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0200', 'uvim2006.tab:0202', 'uvim2006.tab:0203', 'uvim2006.tab:0204', 'uvim2006.tab:0350', 'uvim2006.tab:0412', 'uvim2006.tab:0474', 'uvim2006.tab:0536', 'uvim2006.tab:0598', 'uvim2006.tab:0660', 'uvim2006.tab:0722', 'uvim2006.tab:0784', 'uvim2006.tab:0846', 'uvim2006.tab:0908', 'uvim2006.tab:0970', 'uvim2006.tab:1032', 'uvim2006.tab:1094', 'uvim2006.tab:1156', 'uvim2006.tab:1218', 'uvim2006.tab:1280', 'uvim2006.tab:1342', 'uvim2006.tab:1404', 'uvim2006.tab:1466', 'uvim2006.tab:1528', 'uvim2006.tab:1590', 'uvim2006.tab:1652', 'uvim2006.tab:1714', 'uvim2006.tab:1776', 'uvim2006.tab:1838', 'uvim2006.tab:1900', 'uvim2006.tab:1962', 'uvim2006.tab:2024', 'uvim2006.tab:2086']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0201', 'uvim2006.tab:2148', 'uvim2006.tab:2210']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0201', 'uvim2006.tab:2148', 'uvim2006.tab:2210']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0205', 'uvim2006.tab:0206', 'uvim2006.tab:0207', 'uvim2006.tab:0208', 'uvim2006.tab:0209', 'uvim2006.tab:0351', 'uvim2006.tab:0413', 'uvim2006.tab:0475', 'uvim2006.tab:0537', 'uvim2006.tab:0599', 'uvim2006.tab:0661', 'uvim2006.tab:0723', 'uvim2006.tab:0785', 'uvim2006.tab:0847', 'uvim2006.tab:0909', 'uvim2006.tab:0971', 'uvim2006.tab:1033', 'uvim2006.tab:1095', 'uvim2006.tab:1157', 'uvim2006.tab:1219', 'uvim2006.tab:1281', 'uvim2006.tab:1343', 'uvim2006.tab:1405', 'uvim2006.tab:1467', 'uvim2006.tab:1529', 'uvim2006.tab:1591', 'uvim2006.tab:1653', 'uvim2006.tab:1715', 'uvim2006.tab:1777', 'uvim2006.tab:1839', 'uvim2006.tab:1901', 'uvim2006.tab:1963', 'uvim2006.tab:2025', 'uvim2006.tab:2087', 'uvim2006.tab:2149', 'uvim2006.tab:2211']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0205', 'uvim2006.tab:0206', 'uvim2006.tab:0207', 'uvim2006.tab:0208', 'uvim2006.tab:0209', 'uvim2006.tab:0351', 'uvim2006.tab:0413', 'uvim2006.tab:0475', 'uvim2006.tab:0537', 'uvim2006.tab:0599', 'uvim2006.tab:0661', 'uvim2006.tab:0723', 'uvim2006.tab:0785', 'uvim2006.tab:0847', 'uvim2006.tab:0909', 'uvim2006.tab:0971', 'uvim2006.tab:1033', 'uvim2006.tab:1095', 'uvim2006.tab:1157', 'uvim2006.tab:1219', 'uvim2006.tab:1281', 'uvim2006.tab:1343', 'uvim2006.tab:1405', 'uvim2006.tab:1467', 'uvim2006.tab:1529', 'uvim2006.tab:1591', 'uvim2006.tab:1653', 'uvim2006.tab:1715', 'uvim2006.tab:1777', 'uvim2006.tab:1839', 'uvim2006.tab:1901', 'uvim2006.tab:1963', 'uvim2006.tab:2025', 'uvim2006.tab:2087', 'uvim2006.tab:2149', 'uvim2006.tab:2211']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0205', 'uvim2006.tab:0207', 'uvim2006.tab:0208', 'uvim2006.tab:0209', 'uvim2006.tab:0351', 'uvim2006.tab:0413', 'uvim2006.tab:0475', 'uvim2006.tab:0537', 'uvim2006.tab:0599', 'uvim2006.tab:0661', 'uvim2006.tab:0723', 'uvim2006.tab:0785', 'uvim2006.tab:0847', 'uvim2006.tab:0909', 'uvim2006.tab:0971', 'uvim2006.tab:1033', 'uvim2006.tab:1095', 'uvim2006.tab:1157', 'uvim2006.tab:1219', 'uvim2006.tab:1281', 'uvim2006.tab:1343', 'uvim2006.tab:1405', 'uvim2006.tab:1467', 'uvim2006.tab:1529', 'uvim2006.tab:1591', 'uvim2006.tab:1653', 'uvim2006.tab:1715', 'uvim2006.tab:1777', 'uvim2006.tab:1839', 'uvim2006.tab:1901', 'uvim2006.tab:1963', 'uvim2006.tab:2025', 'uvim2006.tab:2087']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0205', 'uvim2006.tab:0207', 'uvim2006.tab:0208', 'uvim2006.tab:0209', 'uvim2006.tab:0351', 'uvim2006.tab:0413', 'uvim2006.tab:0475', 'uvim2006.tab:0537', 'uvim2006.tab:0599', 'uvim2006.tab:0661', 'uvim2006.tab:0723', 'uvim2006.tab:0785', 'uvim2006.tab:0847', 'uvim2006.tab:0909', 'uvim2006.tab:0971', 'uvim2006.tab:1033', 'uvim2006.tab:1095', 'uvim2006.tab:1157', 'uvim2006.tab:1219', 'uvim2006.tab:1281', 'uvim2006.tab:1343', 'uvim2006.tab:1405', 'uvim2006.tab:1467', 'uvim2006.tab:1529', 'uvim2006.tab:1591', 'uvim2006.tab:1653', 'uvim2006.tab:1715', 'uvim2006.tab:1777', 'uvim2006.tab:1839', 'uvim2006.tab:1901', 'uvim2006.tab:1963', 'uvim2006.tab:2025', 'uvim2006.tab:2087']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0206', 'uvim2006.tab:2149', 'uvim2006.tab:2211']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0206', 'uvim2006.tab:2149', 'uvim2006.tab:2211']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0210', 'uvim2006.tab:0211', 'uvim2006.tab:0212', 'uvim2006.tab:0213', 'uvim2006.tab:0214', 'uvim2006.tab:0352', 'uvim2006.tab:0414', 'uvim2006.tab:0476', 'uvim2006.tab:0538', 'uvim2006.tab:0600', 'uvim2006.tab:0662', 'uvim2006.tab:0724', 'uvim2006.tab:0786', 'uvim2006.tab:0848', 'uvim2006.tab:0910', 'uvim2006.tab:0972', 'uvim2006.tab:1034', 'uvim2006.tab:1096', 'uvim2006.tab:1158', 'uvim2006.tab:1220', 'uvim2006.tab:1282', 'uvim2006.tab:1344', 'uvim2006.tab:1406', 'uvim2006.tab:1468', 'uvim2006.tab:1530', 'uvim2006.tab:1592', 'uvim2006.tab:1654', 'uvim2006.tab:1716', 'uvim2006.tab:1778', 'uvim2006.tab:1840', 'uvim2006.tab:1902', 'uvim2006.tab:1964', 'uvim2006.tab:2026', 'uvim2006.tab:2088', 'uvim2006.tab:2150', 'uvim2006.tab:2212']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0210', 'uvim2006.tab:0211', 'uvim2006.tab:0212', 'uvim2006.tab:0213', 'uvim2006.tab:0214', 'uvim2006.tab:0352', 'uvim2006.tab:0414', 'uvim2006.tab:0476', 'uvim2006.tab:0538', 'uvim2006.tab:0600', 'uvim2006.tab:0662', 'uvim2006.tab:0724', 'uvim2006.tab:0786', 'uvim2006.tab:0848', 'uvim2006.tab:0910', 'uvim2006.tab:0972', 'uvim2006.tab:1034', 'uvim2006.tab:1096', 'uvim2006.tab:1158', 'uvim2006.tab:1220', 'uvim2006.tab:1282', 'uvim2006.tab:1344', 'uvim2006.tab:1406', 'uvim2006.tab:1468', 'uvim2006.tab:1530', 'uvim2006.tab:1592', 'uvim2006.tab:1654', 'uvim2006.tab:1716', 'uvim2006.tab:1778', 'uvim2006.tab:1840', 'uvim2006.tab:1902', 'uvim2006.tab:1964', 'uvim2006.tab:2026', 'uvim2006.tab:2088', 'uvim2006.tab:2150', 'uvim2006.tab:2212']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0210', 'uvim2006.tab:0212', 'uvim2006.tab:0213', 'uvim2006.tab:0214', 'uvim2006.tab:0352', 'uvim2006.tab:0414', 'uvim2006.tab:0476', 'uvim2006.tab:0538', 'uvim2006.tab:0600', 'uvim2006.tab:0662', 'uvim2006.tab:0724', 'uvim2006.tab:0786', 'uvim2006.tab:0848', 'uvim2006.tab:0910', 'uvim2006.tab:0972', 'uvim2006.tab:1034', 'uvim2006.tab:1096', 'uvim2006.tab:1158', 'uvim2006.tab:1220', 'uvim2006.tab:1282', 'uvim2006.tab:1344', 'uvim2006.tab:1406', 'uvim2006.tab:1468', 'uvim2006.tab:1530', 'uvim2006.tab:1592', 'uvim2006.tab:1654', 'uvim2006.tab:1716', 'uvim2006.tab:1778', 'uvim2006.tab:1840', 'uvim2006.tab:1902', 'uvim2006.tab:1964', 'uvim2006.tab:2026', 'uvim2006.tab:2088']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0210', 'uvim2006.tab:0212', 'uvim2006.tab:0213', 'uvim2006.tab:0214', 'uvim2006.tab:0352', 'uvim2006.tab:0414', 'uvim2006.tab:0476', 'uvim2006.tab:0538', 'uvim2006.tab:0600', 'uvim2006.tab:0662', 'uvim2006.tab:0724', 'uvim2006.tab:0786', 'uvim2006.tab:0848', 'uvim2006.tab:0910', 'uvim2006.tab:0972', 'uvim2006.tab:1034', 'uvim2006.tab:1096', 'uvim2006.tab:1158', 'uvim2006.tab:1220', 'uvim2006.tab:1282', 'uvim2006.tab:1344', 'uvim2006.tab:1406', 'uvim2006.tab:1468', 'uvim2006.tab:1530', 'uvim2006.tab:1592', 'uvim2006.tab:1654', 'uvim2006.tab:1716', 'uvim2006.tab:1778', 'uvim2006.tab:1840', 'uvim2006.tab:1902', 'uvim2006.tab:1964', 'uvim2006.tab:2026', 'uvim2006.tab:2088']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0211', 'uvim2006.tab:2150', 'uvim2006.tab:2212']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0211', 'uvim2006.tab:2150', 'uvim2006.tab:2212']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0215', 'uvim2006.tab:0216', 'uvim2006.tab:0217', 'uvim2006.tab:0218', 'uvim2006.tab:0219', 'uvim2006.tab:0353', 'uvim2006.tab:0415', 'uvim2006.tab:0477', 'uvim2006.tab:0539', 'uvim2006.tab:0601', 'uvim2006.tab:0663', 'uvim2006.tab:0725', 'uvim2006.tab:0787', 'uvim2006.tab:0849', 'uvim2006.tab:0911', 'uvim2006.tab:0973', 'uvim2006.tab:1035', 'uvim2006.tab:1097', 'uvim2006.tab:1159', 'uvim2006.tab:1221', 'uvim2006.tab:1283', 'uvim2006.tab:1345', 'uvim2006.tab:1407', 'uvim2006.tab:1469', 'uvim2006.tab:1531', 'uvim2006.tab:1593', 'uvim2006.tab:1655', 'uvim2006.tab:1717', 'uvim2006.tab:1779', 'uvim2006.tab:1841', 'uvim2006.tab:1903', 'uvim2006.tab:1965', 'uvim2006.tab:2027', 'uvim2006.tab:2089', 'uvim2006.tab:2151', 'uvim2006.tab:2213']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0215', 'uvim2006.tab:0216', 'uvim2006.tab:0217', 'uvim2006.tab:0218', 'uvim2006.tab:0219', 'uvim2006.tab:0353', 'uvim2006.tab:0415', 'uvim2006.tab:0477', 'uvim2006.tab:0539', 'uvim2006.tab:0601', 'uvim2006.tab:0663', 'uvim2006.tab:0725', 'uvim2006.tab:0787', 'uvim2006.tab:0849', 'uvim2006.tab:0911', 'uvim2006.tab:0973', 'uvim2006.tab:1035', 'uvim2006.tab:1097', 'uvim2006.tab:1159', 'uvim2006.tab:1221', 'uvim2006.tab:1283', 'uvim2006.tab:1345', 'uvim2006.tab:1407', 'uvim2006.tab:1469', 'uvim2006.tab:1531', 'uvim2006.tab:1593', 'uvim2006.tab:1655', 'uvim2006.tab:1717', 'uvim2006.tab:1779', 'uvim2006.tab:1841', 'uvim2006.tab:1903', 'uvim2006.tab:1965', 'uvim2006.tab:2027', 'uvim2006.tab:2089', 'uvim2006.tab:2151', 'uvim2006.tab:2213']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0215', 'uvim2006.tab:0217', 'uvim2006.tab:0218', 'uvim2006.tab:0219', 'uvim2006.tab:0353', 'uvim2006.tab:0415', 'uvim2006.tab:0477', 'uvim2006.tab:0539', 'uvim2006.tab:0601', 'uvim2006.tab:0663', 'uvim2006.tab:0725', 'uvim2006.tab:0787', 'uvim2006.tab:0849', 'uvim2006.tab:0911', 'uvim2006.tab:0973', 'uvim2006.tab:1035', 'uvim2006.tab:1097', 'uvim2006.tab:1159', 'uvim2006.tab:1221', 'uvim2006.tab:1283', 'uvim2006.tab:1345', 'uvim2006.tab:1407', 'uvim2006.tab:1469', 'uvim2006.tab:1531', 'uvim2006.tab:1593', 'uvim2006.tab:1655', 'uvim2006.tab:1717', 'uvim2006.tab:1779', 'uvim2006.tab:1841', 'uvim2006.tab:1903', 'uvim2006.tab:1965', 'uvim2006.tab:2027', 'uvim2006.tab:2089']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0215', 'uvim2006.tab:0217', 'uvim2006.tab:0218', 'uvim2006.tab:0219', 'uvim2006.tab:0353', 'uvim2006.tab:0415', 'uvim2006.tab:0477', 'uvim2006.tab:0539', 'uvim2006.tab:0601', 'uvim2006.tab:0663', 'uvim2006.tab:0725', 'uvim2006.tab:0787', 'uvim2006.tab:0849', 'uvim2006.tab:0911', 'uvim2006.tab:0973', 'uvim2006.tab:1035', 'uvim2006.tab:1097', 'uvim2006.tab:1159', 'uvim2006.tab:1221', 'uvim2006.tab:1283', 'uvim2006.tab:1345', 'uvim2006.tab:1407', 'uvim2006.tab:1469', 'uvim2006.tab:1531', 'uvim2006.tab:1593', 'uvim2006.tab:1655', 'uvim2006.tab:1717', 'uvim2006.tab:1779', 'uvim2006.tab:1841', 'uvim2006.tab:1903', 'uvim2006.tab:1965', 'uvim2006.tab:2027', 'uvim2006.tab:2089']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0216', 'uvim2006.tab:2151', 'uvim2006.tab:2213']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0216', 'uvim2006.tab:2151', 'uvim2006.tab:2213']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0220', 'uvim2006.tab:0221', 'uvim2006.tab:0222', 'uvim2006.tab:0223', 'uvim2006.tab:0224', 'uvim2006.tab:0354', 'uvim2006.tab:0416', 'uvim2006.tab:0478', 'uvim2006.tab:0540', 'uvim2006.tab:0602', 'uvim2006.tab:0664', 'uvim2006.tab:0726', 'uvim2006.tab:0788', 'uvim2006.tab:0850', 'uvim2006.tab:0912', 'uvim2006.tab:0974', 'uvim2006.tab:1036', 'uvim2006.tab:1098', 'uvim2006.tab:1160', 'uvim2006.tab:1222', 'uvim2006.tab:1284', 'uvim2006.tab:1346', 'uvim2006.tab:1408', 'uvim2006.tab:1470', 'uvim2006.tab:1532', 'uvim2006.tab:1594', 'uvim2006.tab:1656', 'uvim2006.tab:1718', 'uvim2006.tab:1780', 'uvim2006.tab:1842', 'uvim2006.tab:1904', 'uvim2006.tab:1966', 'uvim2006.tab:2028', 'uvim2006.tab:2090', 'uvim2006.tab:2152', 'uvim2006.tab:2214']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0220', 'uvim2006.tab:0221', 'uvim2006.tab:0222', 'uvim2006.tab:0223', 'uvim2006.tab:0224', 'uvim2006.tab:0354', 'uvim2006.tab:0416', 'uvim2006.tab:0478', 'uvim2006.tab:0540', 'uvim2006.tab:0602', 'uvim2006.tab:0664', 'uvim2006.tab:0726', 'uvim2006.tab:0788', 'uvim2006.tab:0850', 'uvim2006.tab:0912', 'uvim2006.tab:0974', 'uvim2006.tab:1036', 'uvim2006.tab:1098', 'uvim2006.tab:1160', 'uvim2006.tab:1222', 'uvim2006.tab:1284', 'uvim2006.tab:1346', 'uvim2006.tab:1408', 'uvim2006.tab:1470', 'uvim2006.tab:1532', 'uvim2006.tab:1594', 'uvim2006.tab:1656', 'uvim2006.tab:1718', 'uvim2006.tab:1780', 'uvim2006.tab:1842', 'uvim2006.tab:1904', 'uvim2006.tab:1966', 'uvim2006.tab:2028', 'uvim2006.tab:2090', 'uvim2006.tab:2152', 'uvim2006.tab:2214']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0220', 'uvim2006.tab:0222', 'uvim2006.tab:0223', 'uvim2006.tab:0224', 'uvim2006.tab:0354', 'uvim2006.tab:0416', 'uvim2006.tab:0478', 'uvim2006.tab:0540', 'uvim2006.tab:0602', 'uvim2006.tab:0664', 'uvim2006.tab:0726', 'uvim2006.tab:0788', 'uvim2006.tab:0850', 'uvim2006.tab:0912', 'uvim2006.tab:0974', 'uvim2006.tab:1036', 'uvim2006.tab:1098', 'uvim2006.tab:1160', 'uvim2006.tab:1222', 'uvim2006.tab:1284', 'uvim2006.tab:1346', 'uvim2006.tab:1408', 'uvim2006.tab:1470', 'uvim2006.tab:1532', 'uvim2006.tab:1594', 'uvim2006.tab:1656', 'uvim2006.tab:1718', 'uvim2006.tab:1780', 'uvim2006.tab:1842', 'uvim2006.tab:1904', 'uvim2006.tab:1966', 'uvim2006.tab:2028', 'uvim2006.tab:2090']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0220', 'uvim2006.tab:0222', 'uvim2006.tab:0223', 'uvim2006.tab:0224', 'uvim2006.tab:0354', 'uvim2006.tab:0416', 'uvim2006.tab:0478', 'uvim2006.tab:0540', 'uvim2006.tab:0602', 'uvim2006.tab:0664', 'uvim2006.tab:0726', 'uvim2006.tab:0788', 'uvim2006.tab:0850', 'uvim2006.tab:0912', 'uvim2006.tab:0974', 'uvim2006.tab:1036', 'uvim2006.tab:1098', 'uvim2006.tab:1160', 'uvim2006.tab:1222', 'uvim2006.tab:1284', 'uvim2006.tab:1346', 'uvim2006.tab:1408', 'uvim2006.tab:1470', 'uvim2006.tab:1532', 'uvim2006.tab:1594', 'uvim2006.tab:1656', 'uvim2006.tab:1718', 'uvim2006.tab:1780', 'uvim2006.tab:1842', 'uvim2006.tab:1904', 'uvim2006.tab:1966', 'uvim2006.tab:2028', 'uvim2006.tab:2090']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0221', 'uvim2006.tab:2152', 'uvim2006.tab:2214']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0221', 'uvim2006.tab:2152', 'uvim2006.tab:2214']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0225', 'uvim2006.tab:0226', 'uvim2006.tab:0227', 'uvim2006.tab:0228', 'uvim2006.tab:0229', 'uvim2006.tab:0355', 'uvim2006.tab:0417', 'uvim2006.tab:0479', 'uvim2006.tab:0541', 'uvim2006.tab:0603', 'uvim2006.tab:0665', 'uvim2006.tab:0727', 'uvim2006.tab:0789', 'uvim2006.tab:0851', 'uvim2006.tab:0913', 'uvim2006.tab:0975', 'uvim2006.tab:1037', 'uvim2006.tab:1099', 'uvim2006.tab:1161', 'uvim2006.tab:1223', 'uvim2006.tab:1285', 'uvim2006.tab:1347', 'uvim2006.tab:1409', 'uvim2006.tab:1471', 'uvim2006.tab:1533', 'uvim2006.tab:1595', 'uvim2006.tab:1657', 'uvim2006.tab:1719', 'uvim2006.tab:1781', 'uvim2006.tab:1843', 'uvim2006.tab:1905', 'uvim2006.tab:1967', 'uvim2006.tab:2029', 'uvim2006.tab:2091', 'uvim2006.tab:2153', 'uvim2006.tab:2215']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0225', 'uvim2006.tab:0226', 'uvim2006.tab:0227', 'uvim2006.tab:0228', 'uvim2006.tab:0229', 'uvim2006.tab:0355', 'uvim2006.tab:0417', 'uvim2006.tab:0479', 'uvim2006.tab:0541', 'uvim2006.tab:0603', 'uvim2006.tab:0665', 'uvim2006.tab:0727', 'uvim2006.tab:0789', 'uvim2006.tab:0851', 'uvim2006.tab:0913', 'uvim2006.tab:0975', 'uvim2006.tab:1037', 'uvim2006.tab:1099', 'uvim2006.tab:1161', 'uvim2006.tab:1223', 'uvim2006.tab:1285', 'uvim2006.tab:1347', 'uvim2006.tab:1409', 'uvim2006.tab:1471', 'uvim2006.tab:1533', 'uvim2006.tab:1595', 'uvim2006.tab:1657', 'uvim2006.tab:1719', 'uvim2006.tab:1781', 'uvim2006.tab:1843', 'uvim2006.tab:1905', 'uvim2006.tab:1967', 'uvim2006.tab:2029', 'uvim2006.tab:2091', 'uvim2006.tab:2153', 'uvim2006.tab:2215']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0225', 'uvim2006.tab:0227', 'uvim2006.tab:0228', 'uvim2006.tab:0229', 'uvim2006.tab:0355', 'uvim2006.tab:0417', 'uvim2006.tab:0479', 'uvim2006.tab:0541', 'uvim2006.tab:0603', 'uvim2006.tab:0665', 'uvim2006.tab:0727', 'uvim2006.tab:0789', 'uvim2006.tab:0851', 'uvim2006.tab:0913', 'uvim2006.tab:0975', 'uvim2006.tab:1037', 'uvim2006.tab:1099', 'uvim2006.tab:1161', 'uvim2006.tab:1223', 'uvim2006.tab:1285', 'uvim2006.tab:1347', 'uvim2006.tab:1409', 'uvim2006.tab:1471', 'uvim2006.tab:1533', 'uvim2006.tab:1595', 'uvim2006.tab:1657', 'uvim2006.tab:1719', 'uvim2006.tab:1781', 'uvim2006.tab:1843', 'uvim2006.tab:1905', 'uvim2006.tab:1967', 'uvim2006.tab:2029', 'uvim2006.tab:2091']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0225', 'uvim2006.tab:0227', 'uvim2006.tab:0228', 'uvim2006.tab:0229', 'uvim2006.tab:0355', 'uvim2006.tab:0417', 'uvim2006.tab:0479', 'uvim2006.tab:0541', 'uvim2006.tab:0603', 'uvim2006.tab:0665', 'uvim2006.tab:0727', 'uvim2006.tab:0789', 'uvim2006.tab:0851', 'uvim2006.tab:0913', 'uvim2006.tab:0975', 'uvim2006.tab:1037', 'uvim2006.tab:1099', 'uvim2006.tab:1161', 'uvim2006.tab:1223', 'uvim2006.tab:1285', 'uvim2006.tab:1347', 'uvim2006.tab:1409', 'uvim2006.tab:1471', 'uvim2006.tab:1533', 'uvim2006.tab:1595', 'uvim2006.tab:1657', 'uvim2006.tab:1719', 'uvim2006.tab:1781', 'uvim2006.tab:1843', 'uvim2006.tab:1905', 'uvim2006.tab:1967', 'uvim2006.tab:2029', 'uvim2006.tab:2091']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0226', 'uvim2006.tab:2153', 'uvim2006.tab:2215']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0226', 'uvim2006.tab:2153', 'uvim2006.tab:2215']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0230', 'uvim2006.tab:0231', 'uvim2006.tab:0232', 'uvim2006.tab:0233', 'uvim2006.tab:0234', 'uvim2006.tab:0356', 'uvim2006.tab:0418', 'uvim2006.tab:0480', 'uvim2006.tab:0542', 'uvim2006.tab:0604', 'uvim2006.tab:0666', 'uvim2006.tab:0728', 'uvim2006.tab:0790', 'uvim2006.tab:0852', 'uvim2006.tab:0914', 'uvim2006.tab:0976', 'uvim2006.tab:1038', 'uvim2006.tab:1100', 'uvim2006.tab:1162', 'uvim2006.tab:1224', 'uvim2006.tab:1286', 'uvim2006.tab:1348', 'uvim2006.tab:1410', 'uvim2006.tab:1472', 'uvim2006.tab:1534', 'uvim2006.tab:1596', 'uvim2006.tab:1658', 'uvim2006.tab:1720', 'uvim2006.tab:1782', 'uvim2006.tab:1844', 'uvim2006.tab:1906', 'uvim2006.tab:1968', 'uvim2006.tab:2030', 'uvim2006.tab:2092', 'uvim2006.tab:2154', 'uvim2006.tab:2216']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0230', 'uvim2006.tab:0231', 'uvim2006.tab:0232', 'uvim2006.tab:0233', 'uvim2006.tab:0234', 'uvim2006.tab:0356', 'uvim2006.tab:0418', 'uvim2006.tab:0480', 'uvim2006.tab:0542', 'uvim2006.tab:0604', 'uvim2006.tab:0666', 'uvim2006.tab:0728', 'uvim2006.tab:0790', 'uvim2006.tab:0852', 'uvim2006.tab:0914', 'uvim2006.tab:0976', 'uvim2006.tab:1038', 'uvim2006.tab:1100', 'uvim2006.tab:1162', 'uvim2006.tab:1224', 'uvim2006.tab:1286', 'uvim2006.tab:1348', 'uvim2006.tab:1410', 'uvim2006.tab:1472', 'uvim2006.tab:1534', 'uvim2006.tab:1596', 'uvim2006.tab:1658', 'uvim2006.tab:1720', 'uvim2006.tab:1782', 'uvim2006.tab:1844', 'uvim2006.tab:1906', 'uvim2006.tab:1968', 'uvim2006.tab:2030', 'uvim2006.tab:2092', 'uvim2006.tab:2154', 'uvim2006.tab:2216']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0230', 'uvim2006.tab:0232', 'uvim2006.tab:0233', 'uvim2006.tab:0234', 'uvim2006.tab:0356', 'uvim2006.tab:0418', 'uvim2006.tab:0480', 'uvim2006.tab:0542', 'uvim2006.tab:0604', 'uvim2006.tab:0666', 'uvim2006.tab:0728', 'uvim2006.tab:0790', 'uvim2006.tab:0852', 'uvim2006.tab:0914', 'uvim2006.tab:0976', 'uvim2006.tab:1038', 'uvim2006.tab:1100', 'uvim2006.tab:1162', 'uvim2006.tab:1224', 'uvim2006.tab:1286', 'uvim2006.tab:1348', 'uvim2006.tab:1410', 'uvim2006.tab:1472', 'uvim2006.tab:1534', 'uvim2006.tab:1596', 'uvim2006.tab:1658', 'uvim2006.tab:1720', 'uvim2006.tab:1782', 'uvim2006.tab:1844', 'uvim2006.tab:1906', 'uvim2006.tab:1968', 'uvim2006.tab:2030', 'uvim2006.tab:2092']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0230', 'uvim2006.tab:0232', 'uvim2006.tab:0233', 'uvim2006.tab:0234', 'uvim2006.tab:0356', 'uvim2006.tab:0418', 'uvim2006.tab:0480', 'uvim2006.tab:0542', 'uvim2006.tab:0604', 'uvim2006.tab:0666', 'uvim2006.tab:0728', 'uvim2006.tab:0790', 'uvim2006.tab:0852', 'uvim2006.tab:0914', 'uvim2006.tab:0976', 'uvim2006.tab:1038', 'uvim2006.tab:1100', 'uvim2006.tab:1162', 'uvim2006.tab:1224', 'uvim2006.tab:1286', 'uvim2006.tab:1348', 'uvim2006.tab:1410', 'uvim2006.tab:1472', 'uvim2006.tab:1534', 'uvim2006.tab:1596', 'uvim2006.tab:1658', 'uvim2006.tab:1720', 'uvim2006.tab:1782', 'uvim2006.tab:1844', 'uvim2006.tab:1906', 'uvim2006.tab:1968', 'uvim2006.tab:2030', 'uvim2006.tab:2092']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0231', 'uvim2006.tab:2154', 'uvim2006.tab:2216']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0231', 'uvim2006.tab:2154', 'uvim2006.tab:2216']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0235', 'uvim2006.tab:0236', 'uvim2006.tab:0237', 'uvim2006.tab:0238', 'uvim2006.tab:0239', 'uvim2006.tab:0357', 'uvim2006.tab:0419', 'uvim2006.tab:0481', 'uvim2006.tab:0543', 'uvim2006.tab:0605', 'uvim2006.tab:0667', 'uvim2006.tab:0729', 'uvim2006.tab:0791', 'uvim2006.tab:0853', 'uvim2006.tab:0915', 'uvim2006.tab:0977', 'uvim2006.tab:1039', 'uvim2006.tab:1101', 'uvim2006.tab:1163', 'uvim2006.tab:1225', 'uvim2006.tab:1287', 'uvim2006.tab:1349', 'uvim2006.tab:1411', 'uvim2006.tab:1473', 'uvim2006.tab:1535', 'uvim2006.tab:1597', 'uvim2006.tab:1659', 'uvim2006.tab:1721', 'uvim2006.tab:1783', 'uvim2006.tab:1845', 'uvim2006.tab:1907', 'uvim2006.tab:1969', 'uvim2006.tab:2031', 'uvim2006.tab:2093', 'uvim2006.tab:2155', 'uvim2006.tab:2217']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0235', 'uvim2006.tab:0236', 'uvim2006.tab:0237', 'uvim2006.tab:0238', 'uvim2006.tab:0239', 'uvim2006.tab:0357', 'uvim2006.tab:0419', 'uvim2006.tab:0481', 'uvim2006.tab:0543', 'uvim2006.tab:0605', 'uvim2006.tab:0667', 'uvim2006.tab:0729', 'uvim2006.tab:0791', 'uvim2006.tab:0853', 'uvim2006.tab:0915', 'uvim2006.tab:0977', 'uvim2006.tab:1039', 'uvim2006.tab:1101', 'uvim2006.tab:1163', 'uvim2006.tab:1225', 'uvim2006.tab:1287', 'uvim2006.tab:1349', 'uvim2006.tab:1411', 'uvim2006.tab:1473', 'uvim2006.tab:1535', 'uvim2006.tab:1597', 'uvim2006.tab:1659', 'uvim2006.tab:1721', 'uvim2006.tab:1783', 'uvim2006.tab:1845', 'uvim2006.tab:1907', 'uvim2006.tab:1969', 'uvim2006.tab:2031', 'uvim2006.tab:2093', 'uvim2006.tab:2155', 'uvim2006.tab:2217']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0235', 'uvim2006.tab:0237', 'uvim2006.tab:0238', 'uvim2006.tab:0239', 'uvim2006.tab:0357', 'uvim2006.tab:0419', 'uvim2006.tab:0481', 'uvim2006.tab:0543', 'uvim2006.tab:0605', 'uvim2006.tab:0667', 'uvim2006.tab:0729', 'uvim2006.tab:0791', 'uvim2006.tab:0853', 'uvim2006.tab:0915', 'uvim2006.tab:0977', 'uvim2006.tab:1039', 'uvim2006.tab:1101', 'uvim2006.tab:1163', 'uvim2006.tab:1225', 'uvim2006.tab:1287', 'uvim2006.tab:1349', 'uvim2006.tab:1411', 'uvim2006.tab:1473', 'uvim2006.tab:1535', 'uvim2006.tab:1597', 'uvim2006.tab:1659', 'uvim2006.tab:1721', 'uvim2006.tab:1783', 'uvim2006.tab:1845', 'uvim2006.tab:1907', 'uvim2006.tab:1969', 'uvim2006.tab:2031', 'uvim2006.tab:2093']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0235', 'uvim2006.tab:0237', 'uvim2006.tab:0238', 'uvim2006.tab:0239', 'uvim2006.tab:0357', 'uvim2006.tab:0419', 'uvim2006.tab:0481', 'uvim2006.tab:0543', 'uvim2006.tab:0605', 'uvim2006.tab:0667', 'uvim2006.tab:0729', 'uvim2006.tab:0791', 'uvim2006.tab:0853', 'uvim2006.tab:0915', 'uvim2006.tab:0977', 'uvim2006.tab:1039', 'uvim2006.tab:1101', 'uvim2006.tab:1163', 'uvim2006.tab:1225', 'uvim2006.tab:1287', 'uvim2006.tab:1349', 'uvim2006.tab:1411', 'uvim2006.tab:1473', 'uvim2006.tab:1535', 'uvim2006.tab:1597', 'uvim2006.tab:1659', 'uvim2006.tab:1721', 'uvim2006.tab:1783', 'uvim2006.tab:1845', 'uvim2006.tab:1907', 'uvim2006.tab:1969', 'uvim2006.tab:2031', 'uvim2006.tab:2093']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0236', 'uvim2006.tab:2155', 'uvim2006.tab:2217']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0236', 'uvim2006.tab:2155', 'uvim2006.tab:2217']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0240', 'uvim2006.tab:0241', 'uvim2006.tab:0242', 'uvim2006.tab:0243', 'uvim2006.tab:0244', 'uvim2006.tab:0358', 'uvim2006.tab:0420', 'uvim2006.tab:0482', 'uvim2006.tab:0544', 'uvim2006.tab:0606', 'uvim2006.tab:0668', 'uvim2006.tab:0730', 'uvim2006.tab:0792', 'uvim2006.tab:0854', 'uvim2006.tab:0916', 'uvim2006.tab:0978', 'uvim2006.tab:1040', 'uvim2006.tab:1102', 'uvim2006.tab:1164', 'uvim2006.tab:1226', 'uvim2006.tab:1288', 'uvim2006.tab:1350', 'uvim2006.tab:1412', 'uvim2006.tab:1474', 'uvim2006.tab:1536', 'uvim2006.tab:1598', 'uvim2006.tab:1660', 'uvim2006.tab:1722', 'uvim2006.tab:1784', 'uvim2006.tab:1846', 'uvim2006.tab:1908', 'uvim2006.tab:1970', 'uvim2006.tab:2032', 'uvim2006.tab:2094', 'uvim2006.tab:2156', 'uvim2006.tab:2218']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0240', 'uvim2006.tab:0241', 'uvim2006.tab:0242', 'uvim2006.tab:0243', 'uvim2006.tab:0244', 'uvim2006.tab:0358', 'uvim2006.tab:0420', 'uvim2006.tab:0482', 'uvim2006.tab:0544', 'uvim2006.tab:0606', 'uvim2006.tab:0668', 'uvim2006.tab:0730', 'uvim2006.tab:0792', 'uvim2006.tab:0854', 'uvim2006.tab:0916', 'uvim2006.tab:0978', 'uvim2006.tab:1040', 'uvim2006.tab:1102', 'uvim2006.tab:1164', 'uvim2006.tab:1226', 'uvim2006.tab:1288', 'uvim2006.tab:1350', 'uvim2006.tab:1412', 'uvim2006.tab:1474', 'uvim2006.tab:1536', 'uvim2006.tab:1598', 'uvim2006.tab:1660', 'uvim2006.tab:1722', 'uvim2006.tab:1784', 'uvim2006.tab:1846', 'uvim2006.tab:1908', 'uvim2006.tab:1970', 'uvim2006.tab:2032', 'uvim2006.tab:2094', 'uvim2006.tab:2156', 'uvim2006.tab:2218']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0240', 'uvim2006.tab:0242', 'uvim2006.tab:0243', 'uvim2006.tab:0244', 'uvim2006.tab:0358', 'uvim2006.tab:0420', 'uvim2006.tab:0482', 'uvim2006.tab:0544', 'uvim2006.tab:0606', 'uvim2006.tab:0668', 'uvim2006.tab:0730', 'uvim2006.tab:0792', 'uvim2006.tab:0854', 'uvim2006.tab:0916', 'uvim2006.tab:0978', 'uvim2006.tab:1040', 'uvim2006.tab:1102', 'uvim2006.tab:1164', 'uvim2006.tab:1226', 'uvim2006.tab:1288', 'uvim2006.tab:1350', 'uvim2006.tab:1412', 'uvim2006.tab:1474', 'uvim2006.tab:1536', 'uvim2006.tab:1598', 'uvim2006.tab:1660', 'uvim2006.tab:1722', 'uvim2006.tab:1784', 'uvim2006.tab:1846', 'uvim2006.tab:1908', 'uvim2006.tab:1970', 'uvim2006.tab:2032', 'uvim2006.tab:2094']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0240', 'uvim2006.tab:0242', 'uvim2006.tab:0243', 'uvim2006.tab:0244', 'uvim2006.tab:0358', 'uvim2006.tab:0420', 'uvim2006.tab:0482', 'uvim2006.tab:0544', 'uvim2006.tab:0606', 'uvim2006.tab:0668', 'uvim2006.tab:0730', 'uvim2006.tab:0792', 'uvim2006.tab:0854', 'uvim2006.tab:0916', 'uvim2006.tab:0978', 'uvim2006.tab:1040', 'uvim2006.tab:1102', 'uvim2006.tab:1164', 'uvim2006.tab:1226', 'uvim2006.tab:1288', 'uvim2006.tab:1350', 'uvim2006.tab:1412', 'uvim2006.tab:1474', 'uvim2006.tab:1536', 'uvim2006.tab:1598', 'uvim2006.tab:1660', 'uvim2006.tab:1722', 'uvim2006.tab:1784', 'uvim2006.tab:1846', 'uvim2006.tab:1908', 'uvim2006.tab:1970', 'uvim2006.tab:2032', 'uvim2006.tab:2094']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0241', 'uvim2006.tab:2156', 'uvim2006.tab:2218']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0241', 'uvim2006.tab:2156', 'uvim2006.tab:2218']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0245', 'uvim2006.tab:0246', 'uvim2006.tab:0247', 'uvim2006.tab:0248', 'uvim2006.tab:0249', 'uvim2006.tab:0359', 'uvim2006.tab:0421', 'uvim2006.tab:0483', 'uvim2006.tab:0545', 'uvim2006.tab:0607', 'uvim2006.tab:0669', 'uvim2006.tab:0731', 'uvim2006.tab:0793', 'uvim2006.tab:0855', 'uvim2006.tab:0917', 'uvim2006.tab:0979', 'uvim2006.tab:1041', 'uvim2006.tab:1103', 'uvim2006.tab:1165', 'uvim2006.tab:1227', 'uvim2006.tab:1289', 'uvim2006.tab:1351', 'uvim2006.tab:1413', 'uvim2006.tab:1475', 'uvim2006.tab:1537', 'uvim2006.tab:1599', 'uvim2006.tab:1661', 'uvim2006.tab:1723', 'uvim2006.tab:1785', 'uvim2006.tab:1847', 'uvim2006.tab:1909', 'uvim2006.tab:1971', 'uvim2006.tab:2033', 'uvim2006.tab:2095', 'uvim2006.tab:2157', 'uvim2006.tab:2219']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0245', 'uvim2006.tab:0246', 'uvim2006.tab:0247', 'uvim2006.tab:0248', 'uvim2006.tab:0249', 'uvim2006.tab:0359', 'uvim2006.tab:0421', 'uvim2006.tab:0483', 'uvim2006.tab:0545', 'uvim2006.tab:0607', 'uvim2006.tab:0669', 'uvim2006.tab:0731', 'uvim2006.tab:0793', 'uvim2006.tab:0855', 'uvim2006.tab:0917', 'uvim2006.tab:0979', 'uvim2006.tab:1041', 'uvim2006.tab:1103', 'uvim2006.tab:1165', 'uvim2006.tab:1227', 'uvim2006.tab:1289', 'uvim2006.tab:1351', 'uvim2006.tab:1413', 'uvim2006.tab:1475', 'uvim2006.tab:1537', 'uvim2006.tab:1599', 'uvim2006.tab:1661', 'uvim2006.tab:1723', 'uvim2006.tab:1785', 'uvim2006.tab:1847', 'uvim2006.tab:1909', 'uvim2006.tab:1971', 'uvim2006.tab:2033', 'uvim2006.tab:2095', 'uvim2006.tab:2157', 'uvim2006.tab:2219']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0245', 'uvim2006.tab:0247', 'uvim2006.tab:0248', 'uvim2006.tab:0249', 'uvim2006.tab:0359', 'uvim2006.tab:0421', 'uvim2006.tab:0483', 'uvim2006.tab:0545', 'uvim2006.tab:0607', 'uvim2006.tab:0669', 'uvim2006.tab:0731', 'uvim2006.tab:0793', 'uvim2006.tab:0855', 'uvim2006.tab:0917', 'uvim2006.tab:0979', 'uvim2006.tab:1041', 'uvim2006.tab:1103', 'uvim2006.tab:1165', 'uvim2006.tab:1227', 'uvim2006.tab:1289', 'uvim2006.tab:1351', 'uvim2006.tab:1413', 'uvim2006.tab:1475', 'uvim2006.tab:1537', 'uvim2006.tab:1599', 'uvim2006.tab:1661', 'uvim2006.tab:1723', 'uvim2006.tab:1785', 'uvim2006.tab:1847', 'uvim2006.tab:1909', 'uvim2006.tab:1971', 'uvim2006.tab:2033', 'uvim2006.tab:2095']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0245', 'uvim2006.tab:0247', 'uvim2006.tab:0248', 'uvim2006.tab:0249', 'uvim2006.tab:0359', 'uvim2006.tab:0421', 'uvim2006.tab:0483', 'uvim2006.tab:0545', 'uvim2006.tab:0607', 'uvim2006.tab:0669', 'uvim2006.tab:0731', 'uvim2006.tab:0793', 'uvim2006.tab:0855', 'uvim2006.tab:0917', 'uvim2006.tab:0979', 'uvim2006.tab:1041', 'uvim2006.tab:1103', 'uvim2006.tab:1165', 'uvim2006.tab:1227', 'uvim2006.tab:1289', 'uvim2006.tab:1351', 'uvim2006.tab:1413', 'uvim2006.tab:1475', 'uvim2006.tab:1537', 'uvim2006.tab:1599', 'uvim2006.tab:1661', 'uvim2006.tab:1723', 'uvim2006.tab:1785', 'uvim2006.tab:1847', 'uvim2006.tab:1909', 'uvim2006.tab:1971', 'uvim2006.tab:2033', 'uvim2006.tab:2095']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0246', 'uvim2006.tab:2157', 'uvim2006.tab:2219']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0246', 'uvim2006.tab:2157', 'uvim2006.tab:2219']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0250', 'uvim2006.tab:0251', 'uvim2006.tab:0252', 'uvim2006.tab:0253', 'uvim2006.tab:0254', 'uvim2006.tab:0360', 'uvim2006.tab:0422', 'uvim2006.tab:0484', 'uvim2006.tab:0546', 'uvim2006.tab:0608', 'uvim2006.tab:0670', 'uvim2006.tab:0732', 'uvim2006.tab:0794', 'uvim2006.tab:0856', 'uvim2006.tab:0918', 'uvim2006.tab:0980', 'uvim2006.tab:1042', 'uvim2006.tab:1104', 'uvim2006.tab:1166', 'uvim2006.tab:1228', 'uvim2006.tab:1290', 'uvim2006.tab:1352', 'uvim2006.tab:1414', 'uvim2006.tab:1476', 'uvim2006.tab:1538', 'uvim2006.tab:1600', 'uvim2006.tab:1662', 'uvim2006.tab:1724', 'uvim2006.tab:1786', 'uvim2006.tab:1848', 'uvim2006.tab:1910', 'uvim2006.tab:1972', 'uvim2006.tab:2034', 'uvim2006.tab:2096', 'uvim2006.tab:2158', 'uvim2006.tab:2220']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0250', 'uvim2006.tab:0251', 'uvim2006.tab:0252', 'uvim2006.tab:0253', 'uvim2006.tab:0254', 'uvim2006.tab:0360', 'uvim2006.tab:0422', 'uvim2006.tab:0484', 'uvim2006.tab:0546', 'uvim2006.tab:0608', 'uvim2006.tab:0670', 'uvim2006.tab:0732', 'uvim2006.tab:0794', 'uvim2006.tab:0856', 'uvim2006.tab:0918', 'uvim2006.tab:0980', 'uvim2006.tab:1042', 'uvim2006.tab:1104', 'uvim2006.tab:1166', 'uvim2006.tab:1228', 'uvim2006.tab:1290', 'uvim2006.tab:1352', 'uvim2006.tab:1414', 'uvim2006.tab:1476', 'uvim2006.tab:1538', 'uvim2006.tab:1600', 'uvim2006.tab:1662', 'uvim2006.tab:1724', 'uvim2006.tab:1786', 'uvim2006.tab:1848', 'uvim2006.tab:1910', 'uvim2006.tab:1972', 'uvim2006.tab:2034', 'uvim2006.tab:2096', 'uvim2006.tab:2158', 'uvim2006.tab:2220']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0250', 'uvim2006.tab:0252', 'uvim2006.tab:0253', 'uvim2006.tab:0254', 'uvim2006.tab:0360', 'uvim2006.tab:0422', 'uvim2006.tab:0484', 'uvim2006.tab:0546', 'uvim2006.tab:0608', 'uvim2006.tab:0670', 'uvim2006.tab:0732', 'uvim2006.tab:0794', 'uvim2006.tab:0856', 'uvim2006.tab:0918', 'uvim2006.tab:0980', 'uvim2006.tab:1042', 'uvim2006.tab:1104', 'uvim2006.tab:1166', 'uvim2006.tab:1228', 'uvim2006.tab:1290', 'uvim2006.tab:1352', 'uvim2006.tab:1414', 'uvim2006.tab:1476', 'uvim2006.tab:1538', 'uvim2006.tab:1600', 'uvim2006.tab:1662', 'uvim2006.tab:1724', 'uvim2006.tab:1786', 'uvim2006.tab:1848', 'uvim2006.tab:1910', 'uvim2006.tab:1972', 'uvim2006.tab:2034', 'uvim2006.tab:2096']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0250', 'uvim2006.tab:0252', 'uvim2006.tab:0253', 'uvim2006.tab:0254', 'uvim2006.tab:0360', 'uvim2006.tab:0422', 'uvim2006.tab:0484', 'uvim2006.tab:0546', 'uvim2006.tab:0608', 'uvim2006.tab:0670', 'uvim2006.tab:0732', 'uvim2006.tab:0794', 'uvim2006.tab:0856', 'uvim2006.tab:0918', 'uvim2006.tab:0980', 'uvim2006.tab:1042', 'uvim2006.tab:1104', 'uvim2006.tab:1166', 'uvim2006.tab:1228', 'uvim2006.tab:1290', 'uvim2006.tab:1352', 'uvim2006.tab:1414', 'uvim2006.tab:1476', 'uvim2006.tab:1538', 'uvim2006.tab:1600', 'uvim2006.tab:1662', 'uvim2006.tab:1724', 'uvim2006.tab:1786', 'uvim2006.tab:1848', 'uvim2006.tab:1910', 'uvim2006.tab:1972', 'uvim2006.tab:2034', 'uvim2006.tab:2096']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0251', 'uvim2006.tab:2158', 'uvim2006.tab:2220']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0251', 'uvim2006.tab:2158', 'uvim2006.tab:2220']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0255', 'uvim2006.tab:0256', 'uvim2006.tab:0257', 'uvim2006.tab:0258', 'uvim2006.tab:0259', 'uvim2006.tab:0361', 'uvim2006.tab:0423', 'uvim2006.tab:0485', 'uvim2006.tab:0547', 'uvim2006.tab:0609', 'uvim2006.tab:0671', 'uvim2006.tab:0733', 'uvim2006.tab:0795', 'uvim2006.tab:0857', 'uvim2006.tab:0919', 'uvim2006.tab:0981', 'uvim2006.tab:1043', 'uvim2006.tab:1105', 'uvim2006.tab:1167', 'uvim2006.tab:1229', 'uvim2006.tab:1291', 'uvim2006.tab:1353', 'uvim2006.tab:1415', 'uvim2006.tab:1477', 'uvim2006.tab:1539', 'uvim2006.tab:1601', 'uvim2006.tab:1663', 'uvim2006.tab:1725', 'uvim2006.tab:1787', 'uvim2006.tab:1849', 'uvim2006.tab:1911', 'uvim2006.tab:1973', 'uvim2006.tab:2035', 'uvim2006.tab:2097', 'uvim2006.tab:2159', 'uvim2006.tab:2221']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0255', 'uvim2006.tab:0256', 'uvim2006.tab:0257', 'uvim2006.tab:0258', 'uvim2006.tab:0259', 'uvim2006.tab:0361', 'uvim2006.tab:0423', 'uvim2006.tab:0485', 'uvim2006.tab:0547', 'uvim2006.tab:0609', 'uvim2006.tab:0671', 'uvim2006.tab:0733', 'uvim2006.tab:0795', 'uvim2006.tab:0857', 'uvim2006.tab:0919', 'uvim2006.tab:0981', 'uvim2006.tab:1043', 'uvim2006.tab:1105', 'uvim2006.tab:1167', 'uvim2006.tab:1229', 'uvim2006.tab:1291', 'uvim2006.tab:1353', 'uvim2006.tab:1415', 'uvim2006.tab:1477', 'uvim2006.tab:1539', 'uvim2006.tab:1601', 'uvim2006.tab:1663', 'uvim2006.tab:1725', 'uvim2006.tab:1787', 'uvim2006.tab:1849', 'uvim2006.tab:1911', 'uvim2006.tab:1973', 'uvim2006.tab:2035', 'uvim2006.tab:2097', 'uvim2006.tab:2159', 'uvim2006.tab:2221']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0255', 'uvim2006.tab:0257', 'uvim2006.tab:0258', 'uvim2006.tab:0259', 'uvim2006.tab:0361', 'uvim2006.tab:0423', 'uvim2006.tab:0485', 'uvim2006.tab:0547', 'uvim2006.tab:0609', 'uvim2006.tab:0671', 'uvim2006.tab:0733', 'uvim2006.tab:0795', 'uvim2006.tab:0857', 'uvim2006.tab:0919', 'uvim2006.tab:0981', 'uvim2006.tab:1043', 'uvim2006.tab:1105', 'uvim2006.tab:1167', 'uvim2006.tab:1229', 'uvim2006.tab:1291', 'uvim2006.tab:1353', 'uvim2006.tab:1415', 'uvim2006.tab:1477', 'uvim2006.tab:1539', 'uvim2006.tab:1601', 'uvim2006.tab:1663', 'uvim2006.tab:1725', 'uvim2006.tab:1787', 'uvim2006.tab:1849', 'uvim2006.tab:1911', 'uvim2006.tab:1973', 'uvim2006.tab:2035', 'uvim2006.tab:2097']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0255', 'uvim2006.tab:0257', 'uvim2006.tab:0258', 'uvim2006.tab:0259', 'uvim2006.tab:0361', 'uvim2006.tab:0423', 'uvim2006.tab:0485', 'uvim2006.tab:0547', 'uvim2006.tab:0609', 'uvim2006.tab:0671', 'uvim2006.tab:0733', 'uvim2006.tab:0795', 'uvim2006.tab:0857', 'uvim2006.tab:0919', 'uvim2006.tab:0981', 'uvim2006.tab:1043', 'uvim2006.tab:1105', 'uvim2006.tab:1167', 'uvim2006.tab:1229', 'uvim2006.tab:1291', 'uvim2006.tab:1353', 'uvim2006.tab:1415', 'uvim2006.tab:1477', 'uvim2006.tab:1539', 'uvim2006.tab:1601', 'uvim2006.tab:1663', 'uvim2006.tab:1725', 'uvim2006.tab:1787', 'uvim2006.tab:1849', 'uvim2006.tab:1911', 'uvim2006.tab:1973', 'uvim2006.tab:2035', 'uvim2006.tab:2097']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0256', 'uvim2006.tab:2159', 'uvim2006.tab:2221']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0256', 'uvim2006.tab:2159', 'uvim2006.tab:2221']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0260', 'uvim2006.tab:0261', 'uvim2006.tab:0262', 'uvim2006.tab:0263', 'uvim2006.tab:0264', 'uvim2006.tab:0362', 'uvim2006.tab:0424', 'uvim2006.tab:0486', 'uvim2006.tab:0548', 'uvim2006.tab:0610', 'uvim2006.tab:0672', 'uvim2006.tab:0734', 'uvim2006.tab:0796', 'uvim2006.tab:0858', 'uvim2006.tab:0920', 'uvim2006.tab:0982', 'uvim2006.tab:1044', 'uvim2006.tab:1106', 'uvim2006.tab:1168', 'uvim2006.tab:1230', 'uvim2006.tab:1292', 'uvim2006.tab:1354', 'uvim2006.tab:1416', 'uvim2006.tab:1478', 'uvim2006.tab:1540', 'uvim2006.tab:1602', 'uvim2006.tab:1664', 'uvim2006.tab:1726', 'uvim2006.tab:1788', 'uvim2006.tab:1850', 'uvim2006.tab:1912', 'uvim2006.tab:1974', 'uvim2006.tab:2036', 'uvim2006.tab:2098', 'uvim2006.tab:2160', 'uvim2006.tab:2222']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0260', 'uvim2006.tab:0261', 'uvim2006.tab:0262', 'uvim2006.tab:0263', 'uvim2006.tab:0264', 'uvim2006.tab:0362', 'uvim2006.tab:0424', 'uvim2006.tab:0486', 'uvim2006.tab:0548', 'uvim2006.tab:0610', 'uvim2006.tab:0672', 'uvim2006.tab:0734', 'uvim2006.tab:0796', 'uvim2006.tab:0858', 'uvim2006.tab:0920', 'uvim2006.tab:0982', 'uvim2006.tab:1044', 'uvim2006.tab:1106', 'uvim2006.tab:1168', 'uvim2006.tab:1230', 'uvim2006.tab:1292', 'uvim2006.tab:1354', 'uvim2006.tab:1416', 'uvim2006.tab:1478', 'uvim2006.tab:1540', 'uvim2006.tab:1602', 'uvim2006.tab:1664', 'uvim2006.tab:1726', 'uvim2006.tab:1788', 'uvim2006.tab:1850', 'uvim2006.tab:1912', 'uvim2006.tab:1974', 'uvim2006.tab:2036', 'uvim2006.tab:2098', 'uvim2006.tab:2160', 'uvim2006.tab:2222']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0260', 'uvim2006.tab:0262', 'uvim2006.tab:0263', 'uvim2006.tab:0264', 'uvim2006.tab:0362', 'uvim2006.tab:0424', 'uvim2006.tab:0486', 'uvim2006.tab:0548', 'uvim2006.tab:0610', 'uvim2006.tab:0672', 'uvim2006.tab:0734', 'uvim2006.tab:0796', 'uvim2006.tab:0858', 'uvim2006.tab:0920', 'uvim2006.tab:0982', 'uvim2006.tab:1044', 'uvim2006.tab:1106', 'uvim2006.tab:1168', 'uvim2006.tab:1230', 'uvim2006.tab:1292', 'uvim2006.tab:1354', 'uvim2006.tab:1416', 'uvim2006.tab:1478', 'uvim2006.tab:1540', 'uvim2006.tab:1602', 'uvim2006.tab:1664', 'uvim2006.tab:1726', 'uvim2006.tab:1788', 'uvim2006.tab:1850', 'uvim2006.tab:1912', 'uvim2006.tab:1974', 'uvim2006.tab:2036', 'uvim2006.tab:2098']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0260', 'uvim2006.tab:0262', 'uvim2006.tab:0263', 'uvim2006.tab:0264', 'uvim2006.tab:0362', 'uvim2006.tab:0424', 'uvim2006.tab:0486', 'uvim2006.tab:0548', 'uvim2006.tab:0610', 'uvim2006.tab:0672', 'uvim2006.tab:0734', 'uvim2006.tab:0796', 'uvim2006.tab:0858', 'uvim2006.tab:0920', 'uvim2006.tab:0982', 'uvim2006.tab:1044', 'uvim2006.tab:1106', 'uvim2006.tab:1168', 'uvim2006.tab:1230', 'uvim2006.tab:1292', 'uvim2006.tab:1354', 'uvim2006.tab:1416', 'uvim2006.tab:1478', 'uvim2006.tab:1540', 'uvim2006.tab:1602', 'uvim2006.tab:1664', 'uvim2006.tab:1726', 'uvim2006.tab:1788', 'uvim2006.tab:1850', 'uvim2006.tab:1912', 'uvim2006.tab:1974', 'uvim2006.tab:2036', 'uvim2006.tab:2098']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0261', 'uvim2006.tab:2160', 'uvim2006.tab:2222']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0261', 'uvim2006.tab:2160', 'uvim2006.tab:2222']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0265', 'uvim2006.tab:0266', 'uvim2006.tab:0267', 'uvim2006.tab:0268', 'uvim2006.tab:0269', 'uvim2006.tab:0363', 'uvim2006.tab:0425', 'uvim2006.tab:0487', 'uvim2006.tab:0549', 'uvim2006.tab:0611', 'uvim2006.tab:0673', 'uvim2006.tab:0735', 'uvim2006.tab:0797', 'uvim2006.tab:0859', 'uvim2006.tab:0921', 'uvim2006.tab:0983', 'uvim2006.tab:1045', 'uvim2006.tab:1107', 'uvim2006.tab:1169', 'uvim2006.tab:1231', 'uvim2006.tab:1293', 'uvim2006.tab:1355', 'uvim2006.tab:1417', 'uvim2006.tab:1479', 'uvim2006.tab:1541', 'uvim2006.tab:1603', 'uvim2006.tab:1665', 'uvim2006.tab:1727', 'uvim2006.tab:1789', 'uvim2006.tab:1851', 'uvim2006.tab:1913', 'uvim2006.tab:1975', 'uvim2006.tab:2037', 'uvim2006.tab:2099', 'uvim2006.tab:2161', 'uvim2006.tab:2223']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0265', 'uvim2006.tab:0266', 'uvim2006.tab:0267', 'uvim2006.tab:0268', 'uvim2006.tab:0269', 'uvim2006.tab:0363', 'uvim2006.tab:0425', 'uvim2006.tab:0487', 'uvim2006.tab:0549', 'uvim2006.tab:0611', 'uvim2006.tab:0673', 'uvim2006.tab:0735', 'uvim2006.tab:0797', 'uvim2006.tab:0859', 'uvim2006.tab:0921', 'uvim2006.tab:0983', 'uvim2006.tab:1045', 'uvim2006.tab:1107', 'uvim2006.tab:1169', 'uvim2006.tab:1231', 'uvim2006.tab:1293', 'uvim2006.tab:1355', 'uvim2006.tab:1417', 'uvim2006.tab:1479', 'uvim2006.tab:1541', 'uvim2006.tab:1603', 'uvim2006.tab:1665', 'uvim2006.tab:1727', 'uvim2006.tab:1789', 'uvim2006.tab:1851', 'uvim2006.tab:1913', 'uvim2006.tab:1975', 'uvim2006.tab:2037', 'uvim2006.tab:2099', 'uvim2006.tab:2161', 'uvim2006.tab:2223']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0265', 'uvim2006.tab:0267', 'uvim2006.tab:0268', 'uvim2006.tab:0269', 'uvim2006.tab:0363', 'uvim2006.tab:0425', 'uvim2006.tab:0487', 'uvim2006.tab:0549', 'uvim2006.tab:0611', 'uvim2006.tab:0673', 'uvim2006.tab:0735', 'uvim2006.tab:0797', 'uvim2006.tab:0859', 'uvim2006.tab:0921', 'uvim2006.tab:0983', 'uvim2006.tab:1045', 'uvim2006.tab:1107', 'uvim2006.tab:1169', 'uvim2006.tab:1231', 'uvim2006.tab:1293', 'uvim2006.tab:1355', 'uvim2006.tab:1417', 'uvim2006.tab:1479', 'uvim2006.tab:1541', 'uvim2006.tab:1603', 'uvim2006.tab:1665', 'uvim2006.tab:1727', 'uvim2006.tab:1789', 'uvim2006.tab:1851', 'uvim2006.tab:1913', 'uvim2006.tab:1975', 'uvim2006.tab:2037', 'uvim2006.tab:2099']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0265', 'uvim2006.tab:0267', 'uvim2006.tab:0268', 'uvim2006.tab:0269', 'uvim2006.tab:0363', 'uvim2006.tab:0425', 'uvim2006.tab:0487', 'uvim2006.tab:0549', 'uvim2006.tab:0611', 'uvim2006.tab:0673', 'uvim2006.tab:0735', 'uvim2006.tab:0797', 'uvim2006.tab:0859', 'uvim2006.tab:0921', 'uvim2006.tab:0983', 'uvim2006.tab:1045', 'uvim2006.tab:1107', 'uvim2006.tab:1169', 'uvim2006.tab:1231', 'uvim2006.tab:1293', 'uvim2006.tab:1355', 'uvim2006.tab:1417', 'uvim2006.tab:1479', 'uvim2006.tab:1541', 'uvim2006.tab:1603', 'uvim2006.tab:1665', 'uvim2006.tab:1727', 'uvim2006.tab:1789', 'uvim2006.tab:1851', 'uvim2006.tab:1913', 'uvim2006.tab:1975', 'uvim2006.tab:2037', 'uvim2006.tab:2099']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0266', 'uvim2006.tab:2161', 'uvim2006.tab:2223']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0266', 'uvim2006.tab:2161', 'uvim2006.tab:2223']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0270', 'uvim2006.tab:0271', 'uvim2006.tab:0272', 'uvim2006.tab:0273', 'uvim2006.tab:0274', 'uvim2006.tab:0364', 'uvim2006.tab:0426', 'uvim2006.tab:0488', 'uvim2006.tab:0550', 'uvim2006.tab:0612', 'uvim2006.tab:0674', 'uvim2006.tab:0736', 'uvim2006.tab:0798', 'uvim2006.tab:0860', 'uvim2006.tab:0922', 'uvim2006.tab:0984', 'uvim2006.tab:1046', 'uvim2006.tab:1108', 'uvim2006.tab:1170', 'uvim2006.tab:1232', 'uvim2006.tab:1294', 'uvim2006.tab:1356', 'uvim2006.tab:1418', 'uvim2006.tab:1480', 'uvim2006.tab:1542', 'uvim2006.tab:1604', 'uvim2006.tab:1666', 'uvim2006.tab:1728', 'uvim2006.tab:1790', 'uvim2006.tab:1852', 'uvim2006.tab:1914', 'uvim2006.tab:1976', 'uvim2006.tab:2038', 'uvim2006.tab:2100', 'uvim2006.tab:2162', 'uvim2006.tab:2224', 'uvim2006.tab:2256', 'uvim2006.tab:2257', 'uvim2006.tab:2258', 'uvim2006.tab:2259', 'uvim2006.tab:2260', 'uvim2006.tab:2261', 'uvim2006.tab:2262', 'uvim2006.tab:2263', 'uvim2006.tab:2264', 'uvim2006.tab:2265', 'uvim2006.tab:2266', 'uvim2006.tab:2267', 'uvim2006.tab:2268', 'uvim2006.tab:2269', 'uvim2006.tab:2270', 'uvim2006.tab:2271', 'uvim2006.tab:2272', 'uvim2006.tab:2273', 'uvim2006.tab:2274', 'uvim2006.tab:2275', 'uvim2006.tab:2276', 'uvim2006.tab:2277', 'uvim2006.tab:2278', 'uvim2006.tab:2279', 'uvim2006.tab:2280', 'uvim2006.tab:2281', 'uvim2006.tab:2282', 'uvim2006.tab:2283', 'uvim2006.tab:2284', 'uvim2006.tab:2285', 'uvim2006.tab:2286', 'uvim2006.tab:2287', 'uvim2006.tab:2288', 'uvim2006.tab:2289', 'uvim2006.tab:2290', 'uvim2006.tab:2291', 'uvim2006.tab:2292', 'uvim2006.tab:2293', 'uvim2006.tab:2294', 'uvim2006.tab:2295', 'uvim2006.tab:2296', 'uvim2006.tab:2297', 'uvim2006.tab:2298', 'uvim2006.tab:2299', 'uvim2006.tab:2300', 'uvim2006.tab:2301', 'uvim2006.tab:2302', 'uvim2006.tab:2303', 'uvim2006.tab:2304', 'uvim2006.tab:2305', 'uvim2006.tab:2306', 'uvim2006.tab:2307', 'uvim2006.tab:2308', 'uvim2006.tab:2309', 'uvim2006.tab:2310', 'uvim2006.tab:2311', 'uvim2006.tab:2312', 'uvim2006.tab:2313', 'uvim2006.tab:2314', 'uvim2006.tab:2315', 'uvim2006.tab:2316', 'uvim2006.tab:2317', 'uvim2006.tab:2318', 'uvim2006.tab:2319', 'uvim2006.tab:2320', 'uvim2006.tab:2321', 'uvim2006.tab:2322', 'uvim2006.tab:2323', 'uvim2006.tab:2324', 'uvim2006.tab:2325', 'uvim2006.tab:2326', 'uvim2006.tab:2327']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0270', 'uvim2006.tab:0271', 'uvim2006.tab:0272', 'uvim2006.tab:0273', 'uvim2006.tab:0274', 'uvim2006.tab:0364', 'uvim2006.tab:0426', 'uvim2006.tab:0488', 'uvim2006.tab:0550', 'uvim2006.tab:0612', 'uvim2006.tab:0674', 'uvim2006.tab:0736', 'uvim2006.tab:0798', 'uvim2006.tab:0860', 'uvim2006.tab:0922', 'uvim2006.tab:0984', 'uvim2006.tab:1046', 'uvim2006.tab:1108', 'uvim2006.tab:1170', 'uvim2006.tab:1232', 'uvim2006.tab:1294', 'uvim2006.tab:1356', 'uvim2006.tab:1418', 'uvim2006.tab:1480', 'uvim2006.tab:1542', 'uvim2006.tab:1604', 'uvim2006.tab:1666', 'uvim2006.tab:1728', 'uvim2006.tab:1790', 'uvim2006.tab:1852', 'uvim2006.tab:1914', 'uvim2006.tab:1976', 'uvim2006.tab:2038', 'uvim2006.tab:2100', 'uvim2006.tab:2162', 'uvim2006.tab:2224', 'uvim2006.tab:2256', 'uvim2006.tab:2257', 'uvim2006.tab:2258', 'uvim2006.tab:2259', 'uvim2006.tab:2260', 'uvim2006.tab:2261', 'uvim2006.tab:2262', 'uvim2006.tab:2263', 'uvim2006.tab:2264', 'uvim2006.tab:2265', 'uvim2006.tab:2266', 'uvim2006.tab:2267', 'uvim2006.tab:2268', 'uvim2006.tab:2269', 'uvim2006.tab:2270', 'uvim2006.tab:2271', 'uvim2006.tab:2272', 'uvim2006.tab:2273', 'uvim2006.tab:2274', 'uvim2006.tab:2275', 'uvim2006.tab:2276', 'uvim2006.tab:2277', 'uvim2006.tab:2278', 'uvim2006.tab:2279', 'uvim2006.tab:2280', 'uvim2006.tab:2281', 'uvim2006.tab:2282', 'uvim2006.tab:2283', 'uvim2006.tab:2284', 'uvim2006.tab:2285', 'uvim2006.tab:2286', 'uvim2006.tab:2287', 'uvim2006.tab:2288', 'uvim2006.tab:2289', 'uvim2006.tab:2290', 'uvim2006.tab:2291', 'uvim2006.tab:2292', 'uvim2006.tab:2293', 'uvim2006.tab:2294', 'uvim2006.tab:2295', 'uvim2006.tab:2296', 'uvim2006.tab:2297', 'uvim2006.tab:2298', 'uvim2006.tab:2299', 'uvim2006.tab:2300', 'uvim2006.tab:2301', 'uvim2006.tab:2302', 'uvim2006.tab:2303', 'uvim2006.tab:2304', 'uvim2006.tab:2305', 'uvim2006.tab:2306', 'uvim2006.tab:2307', 'uvim2006.tab:2308', 'uvim2006.tab:2309', 'uvim2006.tab:2310', 'uvim2006.tab:2311', 'uvim2006.tab:2312', 'uvim2006.tab:2313', 'uvim2006.tab:2314', 'uvim2006.tab:2315', 'uvim2006.tab:2316', 'uvim2006.tab:2317', 'uvim2006.tab:2318', 'uvim2006.tab:2319', 'uvim2006.tab:2320', 'uvim2006.tab:2321', 'uvim2006.tab:2322', 'uvim2006.tab:2323', 'uvim2006.tab:2324', 'uvim2006.tab:2325', 'uvim2006.tab:2326', 'uvim2006.tab:2327']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0270', 'uvim2006.tab:0272', 'uvim2006.tab:0273', 'uvim2006.tab:0274', 'uvim2006.tab:0364', 'uvim2006.tab:0426', 'uvim2006.tab:0488', 'uvim2006.tab:0550', 'uvim2006.tab:0612', 'uvim2006.tab:0674', 'uvim2006.tab:0736', 'uvim2006.tab:0798', 'uvim2006.tab:0860', 'uvim2006.tab:0922', 'uvim2006.tab:0984', 'uvim2006.tab:1046', 'uvim2006.tab:1108', 'uvim2006.tab:1170', 'uvim2006.tab:1232', 'uvim2006.tab:1294', 'uvim2006.tab:1356', 'uvim2006.tab:1418', 'uvim2006.tab:1480', 'uvim2006.tab:1542', 'uvim2006.tab:1604', 'uvim2006.tab:1666', 'uvim2006.tab:1728', 'uvim2006.tab:1790', 'uvim2006.tab:1852', 'uvim2006.tab:1914', 'uvim2006.tab:1976', 'uvim2006.tab:2038', 'uvim2006.tab:2100']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0270', 'uvim2006.tab:0272', 'uvim2006.tab:0273', 'uvim2006.tab:0274', 'uvim2006.tab:0364', 'uvim2006.tab:0426', 'uvim2006.tab:0488', 'uvim2006.tab:0550', 'uvim2006.tab:0612', 'uvim2006.tab:0674', 'uvim2006.tab:0736', 'uvim2006.tab:0798', 'uvim2006.tab:0860', 'uvim2006.tab:0922', 'uvim2006.tab:0984', 'uvim2006.tab:1046', 'uvim2006.tab:1108', 'uvim2006.tab:1170', 'uvim2006.tab:1232', 'uvim2006.tab:1294', 'uvim2006.tab:1356', 'uvim2006.tab:1418', 'uvim2006.tab:1480', 'uvim2006.tab:1542', 'uvim2006.tab:1604', 'uvim2006.tab:1666', 'uvim2006.tab:1728', 'uvim2006.tab:1790', 'uvim2006.tab:1852', 'uvim2006.tab:1914', 'uvim2006.tab:1976', 'uvim2006.tab:2038', 'uvim2006.tab:2100']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0271', 'uvim2006.tab:2162', 'uvim2006.tab:2224']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0271', 'uvim2006.tab:2162', 'uvim2006.tab:2224']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0275', 'uvim2006.tab:0276', 'uvim2006.tab:0277', 'uvim2006.tab:0278', 'uvim2006.tab:0279', 'uvim2006.tab:0365', 'uvim2006.tab:0427', 'uvim2006.tab:0489', 'uvim2006.tab:0551', 'uvim2006.tab:0613', 'uvim2006.tab:0675', 'uvim2006.tab:0737', 'uvim2006.tab:0799', 'uvim2006.tab:0861', 'uvim2006.tab:0923', 'uvim2006.tab:0985', 'uvim2006.tab:1047', 'uvim2006.tab:1109', 'uvim2006.tab:1171', 'uvim2006.tab:1233', 'uvim2006.tab:1295', 'uvim2006.tab:1357', 'uvim2006.tab:1419', 'uvim2006.tab:1481', 'uvim2006.tab:1543', 'uvim2006.tab:1605', 'uvim2006.tab:1667', 'uvim2006.tab:1729', 'uvim2006.tab:1791', 'uvim2006.tab:1853', 'uvim2006.tab:1915', 'uvim2006.tab:1977', 'uvim2006.tab:2039', 'uvim2006.tab:2101', 'uvim2006.tab:2163', 'uvim2006.tab:2225']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0275', 'uvim2006.tab:0276', 'uvim2006.tab:0277', 'uvim2006.tab:0278', 'uvim2006.tab:0279', 'uvim2006.tab:0365', 'uvim2006.tab:0427', 'uvim2006.tab:0489', 'uvim2006.tab:0551', 'uvim2006.tab:0613', 'uvim2006.tab:0675', 'uvim2006.tab:0737', 'uvim2006.tab:0799', 'uvim2006.tab:0861', 'uvim2006.tab:0923', 'uvim2006.tab:0985', 'uvim2006.tab:1047', 'uvim2006.tab:1109', 'uvim2006.tab:1171', 'uvim2006.tab:1233', 'uvim2006.tab:1295', 'uvim2006.tab:1357', 'uvim2006.tab:1419', 'uvim2006.tab:1481', 'uvim2006.tab:1543', 'uvim2006.tab:1605', 'uvim2006.tab:1667', 'uvim2006.tab:1729', 'uvim2006.tab:1791', 'uvim2006.tab:1853', 'uvim2006.tab:1915', 'uvim2006.tab:1977', 'uvim2006.tab:2039', 'uvim2006.tab:2101', 'uvim2006.tab:2163', 'uvim2006.tab:2225']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0275', 'uvim2006.tab:0277', 'uvim2006.tab:0278', 'uvim2006.tab:0279', 'uvim2006.tab:0365', 'uvim2006.tab:0427', 'uvim2006.tab:0489', 'uvim2006.tab:0551', 'uvim2006.tab:0613', 'uvim2006.tab:0675', 'uvim2006.tab:0737', 'uvim2006.tab:0799', 'uvim2006.tab:0861', 'uvim2006.tab:0923', 'uvim2006.tab:0985', 'uvim2006.tab:1047', 'uvim2006.tab:1109', 'uvim2006.tab:1171', 'uvim2006.tab:1233', 'uvim2006.tab:1295', 'uvim2006.tab:1357', 'uvim2006.tab:1419', 'uvim2006.tab:1481', 'uvim2006.tab:1543', 'uvim2006.tab:1605', 'uvim2006.tab:1667', 'uvim2006.tab:1729', 'uvim2006.tab:1791', 'uvim2006.tab:1853', 'uvim2006.tab:1915', 'uvim2006.tab:1977', 'uvim2006.tab:2039', 'uvim2006.tab:2101']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0275', 'uvim2006.tab:0277', 'uvim2006.tab:0278', 'uvim2006.tab:0279', 'uvim2006.tab:0365', 'uvim2006.tab:0427', 'uvim2006.tab:0489', 'uvim2006.tab:0551', 'uvim2006.tab:0613', 'uvim2006.tab:0675', 'uvim2006.tab:0737', 'uvim2006.tab:0799', 'uvim2006.tab:0861', 'uvim2006.tab:0923', 'uvim2006.tab:0985', 'uvim2006.tab:1047', 'uvim2006.tab:1109', 'uvim2006.tab:1171', 'uvim2006.tab:1233', 'uvim2006.tab:1295', 'uvim2006.tab:1357', 'uvim2006.tab:1419', 'uvim2006.tab:1481', 'uvim2006.tab:1543', 'uvim2006.tab:1605', 'uvim2006.tab:1667', 'uvim2006.tab:1729', 'uvim2006.tab:1791', 'uvim2006.tab:1853', 'uvim2006.tab:1915', 'uvim2006.tab:1977', 'uvim2006.tab:2039', 'uvim2006.tab:2101']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0276', 'uvim2006.tab:2163', 'uvim2006.tab:2225']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0276', 'uvim2006.tab:2163', 'uvim2006.tab:2225']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0280', 'uvim2006.tab:0281', 'uvim2006.tab:0282', 'uvim2006.tab:0283', 'uvim2006.tab:0284', 'uvim2006.tab:0366', 'uvim2006.tab:0428', 'uvim2006.tab:0490', 'uvim2006.tab:0552', 'uvim2006.tab:0614', 'uvim2006.tab:0676', 'uvim2006.tab:0738', 'uvim2006.tab:0800', 'uvim2006.tab:0862', 'uvim2006.tab:0924', 'uvim2006.tab:0986', 'uvim2006.tab:1048', 'uvim2006.tab:1110', 'uvim2006.tab:1172', 'uvim2006.tab:1234', 'uvim2006.tab:1296', 'uvim2006.tab:1358', 'uvim2006.tab:1420', 'uvim2006.tab:1482', 'uvim2006.tab:1544', 'uvim2006.tab:1606', 'uvim2006.tab:1668', 'uvim2006.tab:1730', 'uvim2006.tab:1792', 'uvim2006.tab:1854', 'uvim2006.tab:1916', 'uvim2006.tab:1978', 'uvim2006.tab:2040', 'uvim2006.tab:2102', 'uvim2006.tab:2164', 'uvim2006.tab:2226']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0280', 'uvim2006.tab:0281', 'uvim2006.tab:0282', 'uvim2006.tab:0283', 'uvim2006.tab:0284', 'uvim2006.tab:0366', 'uvim2006.tab:0428', 'uvim2006.tab:0490', 'uvim2006.tab:0552', 'uvim2006.tab:0614', 'uvim2006.tab:0676', 'uvim2006.tab:0738', 'uvim2006.tab:0800', 'uvim2006.tab:0862', 'uvim2006.tab:0924', 'uvim2006.tab:0986', 'uvim2006.tab:1048', 'uvim2006.tab:1110', 'uvim2006.tab:1172', 'uvim2006.tab:1234', 'uvim2006.tab:1296', 'uvim2006.tab:1358', 'uvim2006.tab:1420', 'uvim2006.tab:1482', 'uvim2006.tab:1544', 'uvim2006.tab:1606', 'uvim2006.tab:1668', 'uvim2006.tab:1730', 'uvim2006.tab:1792', 'uvim2006.tab:1854', 'uvim2006.tab:1916', 'uvim2006.tab:1978', 'uvim2006.tab:2040', 'uvim2006.tab:2102', 'uvim2006.tab:2164', 'uvim2006.tab:2226']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0280', 'uvim2006.tab:0282', 'uvim2006.tab:0283', 'uvim2006.tab:0284', 'uvim2006.tab:0366', 'uvim2006.tab:0428', 'uvim2006.tab:0490', 'uvim2006.tab:0552', 'uvim2006.tab:0614', 'uvim2006.tab:0676', 'uvim2006.tab:0738', 'uvim2006.tab:0800', 'uvim2006.tab:0862', 'uvim2006.tab:0924', 'uvim2006.tab:0986', 'uvim2006.tab:1048', 'uvim2006.tab:1110', 'uvim2006.tab:1172', 'uvim2006.tab:1234', 'uvim2006.tab:1296', 'uvim2006.tab:1358', 'uvim2006.tab:1420', 'uvim2006.tab:1482', 'uvim2006.tab:1544', 'uvim2006.tab:1606', 'uvim2006.tab:1668', 'uvim2006.tab:1730', 'uvim2006.tab:1792', 'uvim2006.tab:1854', 'uvim2006.tab:1916', 'uvim2006.tab:1978', 'uvim2006.tab:2040', 'uvim2006.tab:2102']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0280', 'uvim2006.tab:0282', 'uvim2006.tab:0283', 'uvim2006.tab:0284', 'uvim2006.tab:0366', 'uvim2006.tab:0428', 'uvim2006.tab:0490', 'uvim2006.tab:0552', 'uvim2006.tab:0614', 'uvim2006.tab:0676', 'uvim2006.tab:0738', 'uvim2006.tab:0800', 'uvim2006.tab:0862', 'uvim2006.tab:0924', 'uvim2006.tab:0986', 'uvim2006.tab:1048', 'uvim2006.tab:1110', 'uvim2006.tab:1172', 'uvim2006.tab:1234', 'uvim2006.tab:1296', 'uvim2006.tab:1358', 'uvim2006.tab:1420', 'uvim2006.tab:1482', 'uvim2006.tab:1544', 'uvim2006.tab:1606', 'uvim2006.tab:1668', 'uvim2006.tab:1730', 'uvim2006.tab:1792', 'uvim2006.tab:1854', 'uvim2006.tab:1916', 'uvim2006.tab:1978', 'uvim2006.tab:2040', 'uvim2006.tab:2102']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0281', 'uvim2006.tab:2164', 'uvim2006.tab:2226']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0281', 'uvim2006.tab:2164', 'uvim2006.tab:2226']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0285', 'uvim2006.tab:0286', 'uvim2006.tab:0287', 'uvim2006.tab:0288', 'uvim2006.tab:0289', 'uvim2006.tab:0367', 'uvim2006.tab:0429', 'uvim2006.tab:0491', 'uvim2006.tab:0553', 'uvim2006.tab:0615', 'uvim2006.tab:0677', 'uvim2006.tab:0739', 'uvim2006.tab:0801', 'uvim2006.tab:0863', 'uvim2006.tab:0925', 'uvim2006.tab:0987', 'uvim2006.tab:1049', 'uvim2006.tab:1111', 'uvim2006.tab:1173', 'uvim2006.tab:1235', 'uvim2006.tab:1297', 'uvim2006.tab:1359', 'uvim2006.tab:1421', 'uvim2006.tab:1483', 'uvim2006.tab:1545', 'uvim2006.tab:1607', 'uvim2006.tab:1669', 'uvim2006.tab:1731', 'uvim2006.tab:1793', 'uvim2006.tab:1855', 'uvim2006.tab:1917', 'uvim2006.tab:1979', 'uvim2006.tab:2041', 'uvim2006.tab:2103', 'uvim2006.tab:2165', 'uvim2006.tab:2227']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0285', 'uvim2006.tab:0286', 'uvim2006.tab:0287', 'uvim2006.tab:0288', 'uvim2006.tab:0289', 'uvim2006.tab:0367', 'uvim2006.tab:0429', 'uvim2006.tab:0491', 'uvim2006.tab:0553', 'uvim2006.tab:0615', 'uvim2006.tab:0677', 'uvim2006.tab:0739', 'uvim2006.tab:0801', 'uvim2006.tab:0863', 'uvim2006.tab:0925', 'uvim2006.tab:0987', 'uvim2006.tab:1049', 'uvim2006.tab:1111', 'uvim2006.tab:1173', 'uvim2006.tab:1235', 'uvim2006.tab:1297', 'uvim2006.tab:1359', 'uvim2006.tab:1421', 'uvim2006.tab:1483', 'uvim2006.tab:1545', 'uvim2006.tab:1607', 'uvim2006.tab:1669', 'uvim2006.tab:1731', 'uvim2006.tab:1793', 'uvim2006.tab:1855', 'uvim2006.tab:1917', 'uvim2006.tab:1979', 'uvim2006.tab:2041', 'uvim2006.tab:2103', 'uvim2006.tab:2165', 'uvim2006.tab:2227']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0285', 'uvim2006.tab:0287', 'uvim2006.tab:0288', 'uvim2006.tab:0289', 'uvim2006.tab:0367', 'uvim2006.tab:0429', 'uvim2006.tab:0491', 'uvim2006.tab:0553', 'uvim2006.tab:0615', 'uvim2006.tab:0677', 'uvim2006.tab:0739', 'uvim2006.tab:0801', 'uvim2006.tab:0863', 'uvim2006.tab:0925', 'uvim2006.tab:0987', 'uvim2006.tab:1049', 'uvim2006.tab:1111', 'uvim2006.tab:1173', 'uvim2006.tab:1235', 'uvim2006.tab:1297', 'uvim2006.tab:1359', 'uvim2006.tab:1421', 'uvim2006.tab:1483', 'uvim2006.tab:1545', 'uvim2006.tab:1607', 'uvim2006.tab:1669', 'uvim2006.tab:1731', 'uvim2006.tab:1793', 'uvim2006.tab:1855', 'uvim2006.tab:1917', 'uvim2006.tab:1979', 'uvim2006.tab:2041', 'uvim2006.tab:2103']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0285', 'uvim2006.tab:0287', 'uvim2006.tab:0288', 'uvim2006.tab:0289', 'uvim2006.tab:0367', 'uvim2006.tab:0429', 'uvim2006.tab:0491', 'uvim2006.tab:0553', 'uvim2006.tab:0615', 'uvim2006.tab:0677', 'uvim2006.tab:0739', 'uvim2006.tab:0801', 'uvim2006.tab:0863', 'uvim2006.tab:0925', 'uvim2006.tab:0987', 'uvim2006.tab:1049', 'uvim2006.tab:1111', 'uvim2006.tab:1173', 'uvim2006.tab:1235', 'uvim2006.tab:1297', 'uvim2006.tab:1359', 'uvim2006.tab:1421', 'uvim2006.tab:1483', 'uvim2006.tab:1545', 'uvim2006.tab:1607', 'uvim2006.tab:1669', 'uvim2006.tab:1731', 'uvim2006.tab:1793', 'uvim2006.tab:1855', 'uvim2006.tab:1917', 'uvim2006.tab:1979', 'uvim2006.tab:2041', 'uvim2006.tab:2103']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0286', 'uvim2006.tab:2165', 'uvim2006.tab:2227']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0286', 'uvim2006.tab:2165', 'uvim2006.tab:2227']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0290', 'uvim2006.tab:0291', 'uvim2006.tab:0292', 'uvim2006.tab:0293', 'uvim2006.tab:0294', 'uvim2006.tab:0368', 'uvim2006.tab:0430', 'uvim2006.tab:0492', 'uvim2006.tab:0554', 'uvim2006.tab:0616', 'uvim2006.tab:0678', 'uvim2006.tab:0740', 'uvim2006.tab:0802', 'uvim2006.tab:0864', 'uvim2006.tab:0926', 'uvim2006.tab:0988', 'uvim2006.tab:1050', 'uvim2006.tab:1112', 'uvim2006.tab:1174', 'uvim2006.tab:1236', 'uvim2006.tab:1298', 'uvim2006.tab:1360', 'uvim2006.tab:1422', 'uvim2006.tab:1484', 'uvim2006.tab:1546', 'uvim2006.tab:1608', 'uvim2006.tab:1670', 'uvim2006.tab:1732', 'uvim2006.tab:1794', 'uvim2006.tab:1856', 'uvim2006.tab:1918', 'uvim2006.tab:1980', 'uvim2006.tab:2042', 'uvim2006.tab:2104', 'uvim2006.tab:2166', 'uvim2006.tab:2228']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0290', 'uvim2006.tab:0291', 'uvim2006.tab:0292', 'uvim2006.tab:0293', 'uvim2006.tab:0294', 'uvim2006.tab:0368', 'uvim2006.tab:0430', 'uvim2006.tab:0492', 'uvim2006.tab:0554', 'uvim2006.tab:0616', 'uvim2006.tab:0678', 'uvim2006.tab:0740', 'uvim2006.tab:0802', 'uvim2006.tab:0864', 'uvim2006.tab:0926', 'uvim2006.tab:0988', 'uvim2006.tab:1050', 'uvim2006.tab:1112', 'uvim2006.tab:1174', 'uvim2006.tab:1236', 'uvim2006.tab:1298', 'uvim2006.tab:1360', 'uvim2006.tab:1422', 'uvim2006.tab:1484', 'uvim2006.tab:1546', 'uvim2006.tab:1608', 'uvim2006.tab:1670', 'uvim2006.tab:1732', 'uvim2006.tab:1794', 'uvim2006.tab:1856', 'uvim2006.tab:1918', 'uvim2006.tab:1980', 'uvim2006.tab:2042', 'uvim2006.tab:2104', 'uvim2006.tab:2166', 'uvim2006.tab:2228']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0290', 'uvim2006.tab:0292', 'uvim2006.tab:0293', 'uvim2006.tab:0294', 'uvim2006.tab:0368', 'uvim2006.tab:0430', 'uvim2006.tab:0492', 'uvim2006.tab:0554', 'uvim2006.tab:0616', 'uvim2006.tab:0678', 'uvim2006.tab:0740', 'uvim2006.tab:0802', 'uvim2006.tab:0864', 'uvim2006.tab:0926', 'uvim2006.tab:0988', 'uvim2006.tab:1050', 'uvim2006.tab:1112', 'uvim2006.tab:1174', 'uvim2006.tab:1236', 'uvim2006.tab:1298', 'uvim2006.tab:1360', 'uvim2006.tab:1422', 'uvim2006.tab:1484', 'uvim2006.tab:1546', 'uvim2006.tab:1608', 'uvim2006.tab:1670', 'uvim2006.tab:1732', 'uvim2006.tab:1794', 'uvim2006.tab:1856', 'uvim2006.tab:1918', 'uvim2006.tab:1980', 'uvim2006.tab:2042', 'uvim2006.tab:2104']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0290', 'uvim2006.tab:0292', 'uvim2006.tab:0293', 'uvim2006.tab:0294', 'uvim2006.tab:0368', 'uvim2006.tab:0430', 'uvim2006.tab:0492', 'uvim2006.tab:0554', 'uvim2006.tab:0616', 'uvim2006.tab:0678', 'uvim2006.tab:0740', 'uvim2006.tab:0802', 'uvim2006.tab:0864', 'uvim2006.tab:0926', 'uvim2006.tab:0988', 'uvim2006.tab:1050', 'uvim2006.tab:1112', 'uvim2006.tab:1174', 'uvim2006.tab:1236', 'uvim2006.tab:1298', 'uvim2006.tab:1360', 'uvim2006.tab:1422', 'uvim2006.tab:1484', 'uvim2006.tab:1546', 'uvim2006.tab:1608', 'uvim2006.tab:1670', 'uvim2006.tab:1732', 'uvim2006.tab:1794', 'uvim2006.tab:1856', 'uvim2006.tab:1918', 'uvim2006.tab:1980', 'uvim2006.tab:2042', 'uvim2006.tab:2104']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0291', 'uvim2006.tab:2166', 'uvim2006.tab:2228']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0291', 'uvim2006.tab:2166', 'uvim2006.tab:2228']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0295', 'uvim2006.tab:0296', 'uvim2006.tab:0297', 'uvim2006.tab:0298', 'uvim2006.tab:0299', 'uvim2006.tab:0369', 'uvim2006.tab:0431', 'uvim2006.tab:0493', 'uvim2006.tab:0555', 'uvim2006.tab:0617', 'uvim2006.tab:0679', 'uvim2006.tab:0741', 'uvim2006.tab:0803', 'uvim2006.tab:0865', 'uvim2006.tab:0927', 'uvim2006.tab:0989', 'uvim2006.tab:1051', 'uvim2006.tab:1113', 'uvim2006.tab:1175', 'uvim2006.tab:1237', 'uvim2006.tab:1299', 'uvim2006.tab:1361', 'uvim2006.tab:1423', 'uvim2006.tab:1485', 'uvim2006.tab:1547', 'uvim2006.tab:1609', 'uvim2006.tab:1671', 'uvim2006.tab:1733', 'uvim2006.tab:1795', 'uvim2006.tab:1857', 'uvim2006.tab:1919', 'uvim2006.tab:1981', 'uvim2006.tab:2043', 'uvim2006.tab:2105', 'uvim2006.tab:2167', 'uvim2006.tab:2229']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0295', 'uvim2006.tab:0296', 'uvim2006.tab:0297', 'uvim2006.tab:0298', 'uvim2006.tab:0299', 'uvim2006.tab:0369', 'uvim2006.tab:0431', 'uvim2006.tab:0493', 'uvim2006.tab:0555', 'uvim2006.tab:0617', 'uvim2006.tab:0679', 'uvim2006.tab:0741', 'uvim2006.tab:0803', 'uvim2006.tab:0865', 'uvim2006.tab:0927', 'uvim2006.tab:0989', 'uvim2006.tab:1051', 'uvim2006.tab:1113', 'uvim2006.tab:1175', 'uvim2006.tab:1237', 'uvim2006.tab:1299', 'uvim2006.tab:1361', 'uvim2006.tab:1423', 'uvim2006.tab:1485', 'uvim2006.tab:1547', 'uvim2006.tab:1609', 'uvim2006.tab:1671', 'uvim2006.tab:1733', 'uvim2006.tab:1795', 'uvim2006.tab:1857', 'uvim2006.tab:1919', 'uvim2006.tab:1981', 'uvim2006.tab:2043', 'uvim2006.tab:2105', 'uvim2006.tab:2167', 'uvim2006.tab:2229']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0295', 'uvim2006.tab:0297', 'uvim2006.tab:0298', 'uvim2006.tab:0299', 'uvim2006.tab:0369', 'uvim2006.tab:0431', 'uvim2006.tab:0493', 'uvim2006.tab:0555', 'uvim2006.tab:0617', 'uvim2006.tab:0679', 'uvim2006.tab:0741', 'uvim2006.tab:0803', 'uvim2006.tab:0865', 'uvim2006.tab:0927', 'uvim2006.tab:0989', 'uvim2006.tab:1051', 'uvim2006.tab:1113', 'uvim2006.tab:1175', 'uvim2006.tab:1237', 'uvim2006.tab:1299', 'uvim2006.tab:1361', 'uvim2006.tab:1423', 'uvim2006.tab:1485', 'uvim2006.tab:1547', 'uvim2006.tab:1609', 'uvim2006.tab:1671', 'uvim2006.tab:1733', 'uvim2006.tab:1795', 'uvim2006.tab:1857', 'uvim2006.tab:1919', 'uvim2006.tab:1981', 'uvim2006.tab:2043', 'uvim2006.tab:2105']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0295', 'uvim2006.tab:0297', 'uvim2006.tab:0298', 'uvim2006.tab:0299', 'uvim2006.tab:0369', 'uvim2006.tab:0431', 'uvim2006.tab:0493', 'uvim2006.tab:0555', 'uvim2006.tab:0617', 'uvim2006.tab:0679', 'uvim2006.tab:0741', 'uvim2006.tab:0803', 'uvim2006.tab:0865', 'uvim2006.tab:0927', 'uvim2006.tab:0989', 'uvim2006.tab:1051', 'uvim2006.tab:1113', 'uvim2006.tab:1175', 'uvim2006.tab:1237', 'uvim2006.tab:1299', 'uvim2006.tab:1361', 'uvim2006.tab:1423', 'uvim2006.tab:1485', 'uvim2006.tab:1547', 'uvim2006.tab:1609', 'uvim2006.tab:1671', 'uvim2006.tab:1733', 'uvim2006.tab:1795', 'uvim2006.tab:1857', 'uvim2006.tab:1919', 'uvim2006.tab:1981', 'uvim2006.tab:2043', 'uvim2006.tab:2105']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0296', 'uvim2006.tab:2167', 'uvim2006.tab:2229']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0296', 'uvim2006.tab:2167', 'uvim2006.tab:2229']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0300', 'uvim2006.tab:0301', 'uvim2006.tab:0302', 'uvim2006.tab:0303', 'uvim2006.tab:0304', 'uvim2006.tab:0370', 'uvim2006.tab:0432', 'uvim2006.tab:0494', 'uvim2006.tab:0556', 'uvim2006.tab:0618', 'uvim2006.tab:0680', 'uvim2006.tab:0742', 'uvim2006.tab:0804', 'uvim2006.tab:0866', 'uvim2006.tab:0928', 'uvim2006.tab:0990', 'uvim2006.tab:1052', 'uvim2006.tab:1114', 'uvim2006.tab:1176', 'uvim2006.tab:1238', 'uvim2006.tab:1300', 'uvim2006.tab:1362', 'uvim2006.tab:1424', 'uvim2006.tab:1486', 'uvim2006.tab:1548', 'uvim2006.tab:1610', 'uvim2006.tab:1672', 'uvim2006.tab:1734', 'uvim2006.tab:1796', 'uvim2006.tab:1858', 'uvim2006.tab:1920', 'uvim2006.tab:1982', 'uvim2006.tab:2044', 'uvim2006.tab:2106', 'uvim2006.tab:2168', 'uvim2006.tab:2230']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0300', 'uvim2006.tab:0301', 'uvim2006.tab:0302', 'uvim2006.tab:0303', 'uvim2006.tab:0304', 'uvim2006.tab:0370', 'uvim2006.tab:0432', 'uvim2006.tab:0494', 'uvim2006.tab:0556', 'uvim2006.tab:0618', 'uvim2006.tab:0680', 'uvim2006.tab:0742', 'uvim2006.tab:0804', 'uvim2006.tab:0866', 'uvim2006.tab:0928', 'uvim2006.tab:0990', 'uvim2006.tab:1052', 'uvim2006.tab:1114', 'uvim2006.tab:1176', 'uvim2006.tab:1238', 'uvim2006.tab:1300', 'uvim2006.tab:1362', 'uvim2006.tab:1424', 'uvim2006.tab:1486', 'uvim2006.tab:1548', 'uvim2006.tab:1610', 'uvim2006.tab:1672', 'uvim2006.tab:1734', 'uvim2006.tab:1796', 'uvim2006.tab:1858', 'uvim2006.tab:1920', 'uvim2006.tab:1982', 'uvim2006.tab:2044', 'uvim2006.tab:2106', 'uvim2006.tab:2168', 'uvim2006.tab:2230']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0300', 'uvim2006.tab:0302', 'uvim2006.tab:0303', 'uvim2006.tab:0304', 'uvim2006.tab:0370', 'uvim2006.tab:0432', 'uvim2006.tab:0494', 'uvim2006.tab:0556', 'uvim2006.tab:0618', 'uvim2006.tab:0680', 'uvim2006.tab:0742', 'uvim2006.tab:0804', 'uvim2006.tab:0866', 'uvim2006.tab:0928', 'uvim2006.tab:0990', 'uvim2006.tab:1052', 'uvim2006.tab:1114', 'uvim2006.tab:1176', 'uvim2006.tab:1238', 'uvim2006.tab:1300', 'uvim2006.tab:1362', 'uvim2006.tab:1424', 'uvim2006.tab:1486', 'uvim2006.tab:1548', 'uvim2006.tab:1610', 'uvim2006.tab:1672', 'uvim2006.tab:1734', 'uvim2006.tab:1796', 'uvim2006.tab:1858', 'uvim2006.tab:1920', 'uvim2006.tab:1982', 'uvim2006.tab:2044', 'uvim2006.tab:2106']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0300', 'uvim2006.tab:0302', 'uvim2006.tab:0303', 'uvim2006.tab:0304', 'uvim2006.tab:0370', 'uvim2006.tab:0432', 'uvim2006.tab:0494', 'uvim2006.tab:0556', 'uvim2006.tab:0618', 'uvim2006.tab:0680', 'uvim2006.tab:0742', 'uvim2006.tab:0804', 'uvim2006.tab:0866', 'uvim2006.tab:0928', 'uvim2006.tab:0990', 'uvim2006.tab:1052', 'uvim2006.tab:1114', 'uvim2006.tab:1176', 'uvim2006.tab:1238', 'uvim2006.tab:1300', 'uvim2006.tab:1362', 'uvim2006.tab:1424', 'uvim2006.tab:1486', 'uvim2006.tab:1548', 'uvim2006.tab:1610', 'uvim2006.tab:1672', 'uvim2006.tab:1734', 'uvim2006.tab:1796', 'uvim2006.tab:1858', 'uvim2006.tab:1920', 'uvim2006.tab:1982', 'uvim2006.tab:2044', 'uvim2006.tab:2106']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0301', 'uvim2006.tab:2168', 'uvim2006.tab:2230']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0301', 'uvim2006.tab:2168', 'uvim2006.tab:2230']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0305', 'uvim2006.tab:0306', 'uvim2006.tab:0307', 'uvim2006.tab:0308', 'uvim2006.tab:0309', 'uvim2006.tab:0371', 'uvim2006.tab:0433', 'uvim2006.tab:0495', 'uvim2006.tab:0557', 'uvim2006.tab:0619', 'uvim2006.tab:0681', 'uvim2006.tab:0743', 'uvim2006.tab:0805', 'uvim2006.tab:0867', 'uvim2006.tab:0929', 'uvim2006.tab:0991', 'uvim2006.tab:1053', 'uvim2006.tab:1115', 'uvim2006.tab:1177', 'uvim2006.tab:1239', 'uvim2006.tab:1301', 'uvim2006.tab:1363', 'uvim2006.tab:1425', 'uvim2006.tab:1487', 'uvim2006.tab:1549', 'uvim2006.tab:1611', 'uvim2006.tab:1673', 'uvim2006.tab:1735', 'uvim2006.tab:1797', 'uvim2006.tab:1859', 'uvim2006.tab:1921', 'uvim2006.tab:1983', 'uvim2006.tab:2045', 'uvim2006.tab:2107', 'uvim2006.tab:2169', 'uvim2006.tab:2231']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="['uvim2006.tab:0305', 'uvim2006.tab:0306', 'uvim2006.tab:0307', 'uvim2006.tab:0308', 'uvim2006.tab:0309', 'uvim2006.tab:0371', 'uvim2006.tab:0433', 'uvim2006.tab:0495', 'uvim2006.tab:0557', 'uvim2006.tab:0619', 'uvim2006.tab:0681', 'uvim2006.tab:0743', 'uvim2006.tab:0805', 'uvim2006.tab:0867', 'uvim2006.tab:0929', 'uvim2006.tab:0991', 'uvim2006.tab:1053', 'uvim2006.tab:1115', 'uvim2006.tab:1177', 'uvim2006.tab:1239', 'uvim2006.tab:1301', 'uvim2006.tab:1363', 'uvim2006.tab:1425', 'uvim2006.tab:1487', 'uvim2006.tab:1549', 'uvim2006.tab:1611', 'uvim2006.tab:1673', 'uvim2006.tab:1735', 'uvim2006.tab:1797', 'uvim2006.tab:1859', 'uvim2006.tab:1921', 'uvim2006.tab:1983', 'uvim2006.tab:2045', 'uvim2006.tab:2107', 'uvim2006.tab:2169', 'uvim2006.tab:2231']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0305', 'uvim2006.tab:0307', 'uvim2006.tab:0308', 'uvim2006.tab:0309', 'uvim2006.tab:0371', 'uvim2006.tab:0433', 'uvim2006.tab:0495', 'uvim2006.tab:0557', 'uvim2006.tab:0619', 'uvim2006.tab:0681', 'uvim2006.tab:0743', 'uvim2006.tab:0805', 'uvim2006.tab:0867', 'uvim2006.tab:0929', 'uvim2006.tab:0991', 'uvim2006.tab:1053', 'uvim2006.tab:1115', 'uvim2006.tab:1177', 'uvim2006.tab:1239', 'uvim2006.tab:1301', 'uvim2006.tab:1363', 'uvim2006.tab:1425', 'uvim2006.tab:1487', 'uvim2006.tab:1549', 'uvim2006.tab:1611', 'uvim2006.tab:1673', 'uvim2006.tab:1735', 'uvim2006.tab:1797', 'uvim2006.tab:1859', 'uvim2006.tab:1921', 'uvim2006.tab:1983', 'uvim2006.tab:2045', 'uvim2006.tab:2107']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0305', 'uvim2006.tab:0307', 'uvim2006.tab:0308', 'uvim2006.tab:0309', 'uvim2006.tab:0371', 'uvim2006.tab:0433', 'uvim2006.tab:0495', 'uvim2006.tab:0557', 'uvim2006.tab:0619', 'uvim2006.tab:0681', 'uvim2006.tab:0743', 'uvim2006.tab:0805', 'uvim2006.tab:0867', 'uvim2006.tab:0929', 'uvim2006.tab:0991', 'uvim2006.tab:1053', 'uvim2006.tab:1115', 'uvim2006.tab:1177', 'uvim2006.tab:1239', 'uvim2006.tab:1301', 'uvim2006.tab:1363', 'uvim2006.tab:1425', 'uvim2006.tab:1487', 'uvim2006.tab:1549', 'uvim2006.tab:1611', 'uvim2006.tab:1673', 'uvim2006.tab:1735', 'uvim2006.tab:1797', 'uvim2006.tab:1859', 'uvim2006.tab:1921', 'uvim2006.tab:1983', 'uvim2006.tab:2045', 'uvim2006.tab:2107']"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0306', 'uvim2006.tab:2169', 'uvim2006.tab:2231']"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.subset=False
        self.etcid="['uvim2006.tab:0306', 'uvim2006.tab:2169', 'uvim2006.tab:2231']"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2232"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2232"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2234"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase191(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2234"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2235"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase192(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2235"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2236"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase193(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2236"
        self.setglobal(__file__)
        self.runpy()
class countrateCase193(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2237"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase194(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2237"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2238"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase195(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2238"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase196(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2240"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase197(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2240"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2241"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase198(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2241"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2242"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase199(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2242"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2244(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase199(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2243"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase200(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2243"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2244"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase201(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2244"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase202(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2246"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase203(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2246"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2247"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase204(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2247"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2248"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase205(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2248"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2249"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase206(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2249"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2250"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase207(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2250"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase208(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2252"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase209(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2252"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2253"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase210(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2253"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2254"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase211(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2254"
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
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2255"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase212(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2255"
        self.setglobal(__file__)
        self.runpy()
class countrateCase212(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2256"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase213(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2256"
        self.setglobal(__file__)
        self.runpy()
class countrateCase213(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase214(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase214(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2258"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase215(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2258"
        self.setglobal(__file__)
        self.runpy()
class countrateCase215(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2259"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase216(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2259"
        self.setglobal(__file__)
        self.runpy()
class countrateCase216(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2260"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase217(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2260"
        self.setglobal(__file__)
        self.runpy()
class countrateCase217(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2261"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase218(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2261"
        self.setglobal(__file__)
        self.runpy()
class countrateCase218(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2262"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase219(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2262"
        self.setglobal(__file__)
        self.runpy()
class countrateCase219(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase220(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase220(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2264"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase221(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2264"
        self.setglobal(__file__)
        self.runpy()
class countrateCase221(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase222(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase222(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase223(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase223(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2273"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase224(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2273"
        self.setglobal(__file__)
        self.runpy()
class countrateCase224(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2268"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase225(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2268"
        self.setglobal(__file__)
        self.runpy()
class countrateCase225(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase226(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase226(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2270"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase227(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2270"
        self.setglobal(__file__)
        self.runpy()
class countrateCase227(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase228(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase228(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase229(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase229(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase230(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase230(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase231(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase231(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase232(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase232(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase233(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase233(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase234(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase234(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase235(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase235(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase236(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase236(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2274"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase237(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2274"
        self.setglobal(__file__)
        self.runpy()
class countrateCase237(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase238(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase238(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase239(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase239(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase240(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase240(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase241(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase241(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase242(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase242(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2286"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase243(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2286"
        self.setglobal(__file__)
        self.runpy()
class countrateCase243(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase244(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase244(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2288"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase245(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2288"
        self.setglobal(__file__)
        self.runpy()
class countrateCase245(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase246(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase246(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase247(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase247(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase248(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase248(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase249(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase249(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase250(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase250(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase251(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase251(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2295"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase252(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2295"
        self.setglobal(__file__)
        self.runpy()
class countrateCase252(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2296"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase253(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2296"
        self.setglobal(__file__)
        self.runpy()
class countrateCase253(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2279"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase254(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2279"
        self.setglobal(__file__)
        self.runpy()
class countrateCase254(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2298"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase255(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2298"
        self.setglobal(__file__)
        self.runpy()
class countrateCase255(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase256(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase256(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2300"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase257(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2300"
        self.setglobal(__file__)
        self.runpy()
class countrateCase257(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2301"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase258(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2301"
        self.setglobal(__file__)
        self.runpy()
class countrateCase258(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2302"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase259(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2302"
        self.setglobal(__file__)
        self.runpy()
class countrateCase259(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=True
        self.etcid="uvim2006.tab:2303"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase260(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2303"
        self.setglobal(__file__)
        self.runpy()
class countrateCase260(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase261(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase261(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase262(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase262(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase263(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase263(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase264(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=True
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase264(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2308"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase265(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2308"
        self.setglobal(__file__)
        self.runpy()
class countrateCase265(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2285"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase266(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2285"
        self.setglobal(__file__)
        self.runpy()
class countrateCase266(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2310"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase267(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2310"
        self.setglobal(__file__)
        self.runpy()
class countrateCase267(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase268(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase268(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2312"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase269(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2312"
        self.setglobal(__file__)
        self.runpy()
class countrateCase269(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2313"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase270(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2313"
        self.setglobal(__file__)
        self.runpy()
class countrateCase270(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2314"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase271(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2314"
        self.setglobal(__file__)
        self.runpy()
class countrateCase271(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2315"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase272(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="uvim2006.tab:2315"
        self.setglobal(__file__)
        self.runpy()
class countrateCase272(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2316"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase273(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="uvim2006.tab:2316"
        self.setglobal(__file__)
        self.runpy()
class countrateCase273(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase274(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase274(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2318"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase275(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="uvim2006.tab:2318"
        self.setglobal(__file__)
        self.runpy()
class countrateCase275(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2319"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase276(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="uvim2006.tab:2319"
        self.setglobal(__file__)
        self.runpy()
class countrateCase276(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2320"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase277(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="uvim2006.tab:2320"
        self.setglobal(__file__)
        self.runpy()
class countrateCase277(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase278(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase278(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase279(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase279(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase280(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase280(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase281(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase281(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase282(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase282(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase283(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase283(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase284(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase284(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase285(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase285(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase286(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase286(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase287(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase287(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase288(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase288(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase289(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase289(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2333"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase290(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2333"
        self.setglobal(__file__)
        self.runpy()
class countrateCase290(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2334"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase291(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2334"
        self.setglobal(__file__)
        self.runpy()
class countrateCase291(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2335"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase292(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2335"
        self.setglobal(__file__)
        self.runpy()
class countrateCase292(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2336"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase293(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2336"
        self.setglobal(__file__)
        self.runpy()
class countrateCase293(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase294(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase294(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2338"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase295(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2338"
        self.setglobal(__file__)
        self.runpy()
class countrateCase295(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2339"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase296(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2339"
        self.setglobal(__file__)
        self.runpy()
class countrateCase296(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase297(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase297(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase298(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase298(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase299(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase299(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase300(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase300(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2344"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase301(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2344"
        self.setglobal(__file__)
        self.runpy()
class countrateCase301(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase302(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase302(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2346"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase303(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2346"
        self.setglobal(__file__)
        self.runpy()
class countrateCase303(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase304(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase304(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase305(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase305(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2349"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase306(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2349"
        self.setglobal(__file__)
        self.runpy()
class countrateCase306(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2350"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase307(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2350"
        self.setglobal(__file__)
        self.runpy()
class countrateCase307(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2351"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase308(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2351"
        self.setglobal(__file__)
        self.runpy()
class countrateCase308(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2352"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase309(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2352"
        self.setglobal(__file__)
        self.runpy()
class countrateCase309(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2353"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase310(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2353"
        self.setglobal(__file__)
        self.runpy()
class countrateCase310(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2354"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase311(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2354"
        self.setglobal(__file__)
        self.runpy()
class countrateCase311(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2355"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase312(basecase.calcphotOverlapCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2355"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class countrateCase312(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2356"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase313(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2356"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase314(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2357"
        self.setglobal(__file__)
        self.runpy()
class countrateCase313(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2357"
        self.setglobal(__file__)
        self.runpy()
class countrateCase314(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2357"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase315(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2357"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase316(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2358"
        self.setglobal(__file__)
        self.runpy()
class countrateCase315(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2358"
        self.setglobal(__file__)
        self.runpy()
class countrateCase316(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2358"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase317(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2358"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase318(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2359"
        self.setglobal(__file__)
        self.runpy()
class countrateCase317(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2359"
        self.setglobal(__file__)
        self.runpy()
class countrateCase318(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2359"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase319(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2359"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase320(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2360"
        self.setglobal(__file__)
        self.runpy()
class countrateCase319(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2360"
        self.setglobal(__file__)
        self.runpy()
class countrateCase320(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2360"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase321(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2360"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase322(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2361"
        self.setglobal(__file__)
        self.runpy()
class countrateCase321(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2361"
        self.setglobal(__file__)
        self.runpy()
class countrateCase322(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2361"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase323(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2361"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2263(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.subset=False
        self.etcid="None"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase324(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2362"
        self.setglobal(__file__)
        self.runpy()
class countrateCase323(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2362"
        self.setglobal(__file__)
        self.runpy()
class countrateCase324(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2362"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase325(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2362"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase326(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2363"
        self.setglobal(__file__)
        self.runpy()
class countrateCase325(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2363"
        self.setglobal(__file__)
        self.runpy()
class countrateCase326(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2363"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase327(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2363"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase328(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2364"
        self.setglobal(__file__)
        self.runpy()
class countrateCase327(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.subset=False
        self.etcid="uvim2006.tab:2364"
        self.setglobal(__file__)
        self.runpy()
class countrateCase328(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2364"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase329(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2364"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase330(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="uvim2006.tab:2365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase329(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.subset=False
        self.etcid="uvim2006.tab:2365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase330(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2365"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase331(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2365"
        self.setglobal(__file__)
        self.runpy()
class countrateCase331(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="uvim2006.tab:2366"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase332(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.subset=False
        self.etcid="uvim2006.tab:2366"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase333(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="uvim2006.tab:2367"
        self.setglobal(__file__)
        self.runpy()
class countrateCase332(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.subset=False
        self.etcid="uvim2006.tab:2367"
        self.setglobal(__file__)
        self.runpy()
class countrateCase333(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2367"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase334(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2367"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase335(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase334(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase335(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=False
        self.etcid="uvim2006.tab:2368"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase336(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.subset=True
        self.etcid="uvim2006.tab:2368"
        self.setglobal(__file__)
        self.runpy()
class countrateCase336(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=True
        self.etcid="uvim2006.tab:2369"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase337(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.subset=False
        self.etcid="uvim2006.tab:2369"
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
