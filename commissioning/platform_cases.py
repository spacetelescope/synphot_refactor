"""These test cases are generated from reports that synphot performs
differently on different platforms:

Mode = band(acs,wfc1,f814w)
Spectrum:  rn(icat(k93models,3500,0.0,4.6),band(v),18.0,vegamag)
Task: Countrate

Mode = band(acs,wfc1,f555w)
Spectrum: rn(spec(/usr/stsci/stdata/calspec/gd71_mod_005.fits),box(5125.0,1.0), 1.0e-18, flam)
Task: countrate"""

from pytools import testutil
import sys, socket
from basecase import countrateCase


class P1(countrateCase):
    def setUp(self):
        self.obsmode='acs,wfc1,f814w'
        self.spectrum='rn(icat(k93models,3500,0.0,4.6),band(v),18.0,vegamag)'
        self.setglobal(__file__)
        self.tda['Hostname']=socket.gethostname()
        self.runpy()
        
class P2(countrateCase):
    def setUp(self):
        self.obsmode='acs,wfc1,f555w'
        self.spectrum='rn(spec(crcalspec$gd71_mod_005.fits),box(5125.0,1.0), 1.0e-18, flam)'
        self.setglobal(__file__)
        self.tda['Hostname']=socket.gethostname()
        self.runpy()

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
