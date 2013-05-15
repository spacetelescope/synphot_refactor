import basecase
import sys,os


pattern="""class stisS%d(countrateCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.setglobal(__file__)
        self.runpy()\n"""

speclist=['/grp/hst/cdbs/calspec/gd71_mod_005.fits',
          '/grp/hst/cdbs/calspec/gd153_mod_004.fits',
          '/grp/hst/cdbs/calspec/g191b2b_mod_004.fits']


def genacs(inname):
    f=open(inname)
    out=open(inname+'.py','w')
    count=0
    for line in f:
        for sp in speclist:
            out.write(pattern%(count,line.strip(),sp))
            count+=1
    out.close()
    f.close()
    
def genstis(outname):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    pattern="""class stisS%d(countrateCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.setglobal(__file__)
        self.runpy()\n"""

    speclist=['/grp/hst/cdbs/calspec/gd71_mod_005.fits',
              '/grp/hst/cdbs/calspec/gd153_mod_004.fits',
              '/grp/hst/cdbs/calspec/g191b2b_mod_004.fits']

    glist={'g140l':'fuvmama','g230l':'nuvmama','g430l':'ccd','g750l':'ccd',
    'g230lb':'ccd']

    out=open(outname,'a')
    out.write("""from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase\n
""")
    count=0
    for g in glist:
        for sp in speclist:
            obsmode='stis,%s,fuvmama,s52x2'%g
            defn=pattern%(count,obsmode,sp)
            out.write(defn)
            count+=1

    out.write("""\n\n
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
""")

    out.close()
    
