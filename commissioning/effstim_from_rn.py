import re
def extract():
    pat=re.compile("rn\((.*),band\((.*)\),")

    ins=('acs','nicmos','stis')
    for iname in ins:
           fname="%s_rn_cases.py"%iname
           f=open(fname)
           out=open(fname.replace('rn','effstim').replace('.py','.txt'),'w')
           for line in f:
               if '.spectrum' in line:
                   x=re.search(pat,line)
                   out.write("%s ! %s\n"%(x.group(1),x.group(2)))
           out.close()
           f.close()
                                                       
def construct():

    header="""from pytools import testutil
import sys
import basecase

"""
    pattern="""
class E%d%s(basecase.effstimCase):
    def setUp(self):
        self.spectrum="%s"
        self.obsmode="%s"
        self.form="%s"
        self.setglobal(__file__)
        self.runpy()

"""
    ulist=('photlam','flam',
           'fnu',
           'vegamag',
           'abmag',
           'stmag',
           'obmag',
           'counts')
    
    ins=('acs','nicmos','stis')
    for iname in ins:
        fname="%s_effstim_cases.txt"%iname
        f=open(fname)
        out=open(fname.replace('.txt','.py'),'w')
        out.write(header)
        count=1
        for line in f:
            sp,bp=line.strip().split('!')
            for u in ulist:
                out.write(pattern%(count,u,sp,bp.strip().lower(),u))
            count+=1
        f.close()
        out.close()
