from pysynphot import etc
import sys,os
import pickle

def run(cmdfile,subsetfile=None, lookupfile=None):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    #Define the test case pattern
    pattern="""class %s(basecase.%sCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.subset=%s
        self.etcid="%s"
        self.setglobal(__file__)
        self.runpy()\n"""

    #Open the (params:etcid) dictionary if it exists
    if lookupfile is not None:
        f=open(lookupfile)
        lookup=pickle.load(f)
        f.close()
    else:
        lookup={}
        
    #Process the subsetfile if present
    subsetflag={}
    if subsetfile is not None:
        #Then this file contains a list of case names that should have a
        #subset flag set.
        f=open(subsetfile)
        for line in f:
            if not line.startswith('#') and len(line.strip())>0:
                cols=line.strip().split()
                subsetflag[cols[0]]=True
        f.close()

    #Open the main input and output files
    f=open(cmdfile)
    out=open(cmdfile.replace('.txt','.py'),'w')
    out.write("""from pytools import testutil
import sys
import basecase
""")

    #Set up some bookkeeping
    count={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}
    dupcatcher={}
    dupcounter={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}
    
    #Now start the main loop
    for line in f:
    
    #parse the line
        ktuple=line2ktuple(line)
        cmd,obsmode,spectrum=ktuple
        count[cmd]+=1
        casename="%sCase%d"%(cmd,count[cmd])        
        if ktuple in dupcatcher:
            dupcounter[cmd]+=1
            dupcatcher[ktuple].append(casename)
        else:
            dupcatcher[ktuple]=[casename]
            etcid=lookup.get(ktuple,None)
            if etcid is not None and len(etcid) == 1:
                etcid=etcid[0]
            defn=pattern%(casename,cmd,obsmode,spectrum,subsetflag.get(casename,False),etcid)
            out.write(defn)

    out.write("""\n\n
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
""")

    f.close()

    for k in count:
        total= "#%s:%d - %d dup =%d\n"%(k,count[k],dupcounter[k],count[k]-dupcounter[k])
        sys.stdout.write(total)
        out.write(total)
    out.close()

        
    return dupcatcher

def line2ktuple(line):
    parts=line.strip().split('&')
    cmd=(parts[0].lstrip())[1:] #strip off leading quote
    kwd=etc.getparms(parts[1:])
    
    #do the substitutions
    try:
        obsmode=kwd['instrument']
    except KeyError:
        obsmode=kwd.get('obsmode','None')
        
    #fix the CDBS specification
    try:
        kwd['spectrum']=kwd['spectrum'].replace('/cdbs',os.environ['PYSYN_CDBS'])
        kwd['spectrum']=kwd['spectrum'].replace('/usr/stsci/stdata',
                                                os.environ['PYSYN_CDBS'])
    except KeyError:
        kwd['spectrum']=None
        
        
    #Construct the name and pattern
    ktuple=(cmd,obsmode,kwd['spectrum'])
    return ktuple

if __name__ == '__main__':
    dups = run(*sys.argv[1:])
    
