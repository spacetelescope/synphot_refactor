from pytools import testutil
import sys
import basecase
class thermbackCase1(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="None"
        self.subset=False
        self.etcid="SpecA:S001"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase2(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="None"
        self.subset=False
        self.etcid="SpecA:S002"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase3(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="None"
        self.subset=False
        self.etcid="SpecA:S003"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase5(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.001"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase6(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase7(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.EXT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase8(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase9(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.EXT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase10(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.EXT.IMAG.011"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase11(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase12(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase13(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="None"
        self.subset=True
        self.etcid="ImagingB:37"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase14(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase15(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase16(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.EXT.IMAG.016"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase17(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.EXT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase18(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.009"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase19(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.033"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase20(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1008"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase21(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="None"
        self.subset=True
        self.etcid="NICIMAG1001"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase22(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1015"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase23(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.015"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase24(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.030"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase25(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.003"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase26(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1006"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase27(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.026"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase28(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1012"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase29(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.PT.IMAG.017"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase30(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.007"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase31(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1013"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase32(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.025"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase33(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="None"
        self.subset=True
        self.etcid="NICIMAG1018"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase34(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.PT.IMAG.022"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase35(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.014"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase36(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.005"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase37(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.PT.IMAG.034"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase38(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1005"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase39(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1014"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase40(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.012"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase41(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.004"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase42(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.008"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase43(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.002"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase44(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1011"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase45(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.027"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase46(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.028"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase47(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.021"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase48(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.024"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase49(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.023"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase50(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1009"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase51(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="None"
        self.subset=True
        self.etcid="NIC.PT.IMAG.031"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase52(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NICIMAG1016"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase53(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="None"
        self.subset=False
        self.etcid="NIC.PT.IMAG.013"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:0 - 0 dup =0
#thermback:53 - 1 dup =52
#calcphot:0 - 0 dup =0
#countrate:0 - 0 dup =0
#SpecSourcerateSpec:0 - 0 dup =0
