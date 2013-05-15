from pytools import testutil
import sys
import basecase
class thermbackCase1(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0000"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase3(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0005"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase4(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0010"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase5(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0015"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase6(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0020"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase7(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0025"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase8(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0030"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase9(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0035"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase10(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0040"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase11(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0045"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase12(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0050"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase13(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0055"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase14(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0060"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase15(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0065"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase16(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="None"
        self.subset=True
        self.etcid="irim006.tab:0070"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:0 - 0 dup =0
#thermback:16 - 1 dup =15
#calcphot:0 - 0 dup =0
#countrate:0 - 0 dup =0
#SpecSourcerateSpec:0 - 0 dup =0
