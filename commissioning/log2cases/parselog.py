"""This script *replaces* the processlog.csh shell script. It has
more sophisticated logic to add the etc test name to the pysynphot
command as another keyword-value pair.

Modified to parse the modified line, then write a dictionary that will
be read by the gencases tool.
"""

import sys,re, pickle
from pysynphot import etc
import gencases

def run(fname):
    log=open(fname)
    out=open(fname.replace('.txt','_lookup.pickle'),'w')
    d={}

    line='unopened'
    while len(line)>0:
        line = log.readline().strip()
        if "] starting" in line or "] running" in line:
            x=re.search("'(?P<name>.*)'",line)
            testname=x.group('name')
        elif 'command is' in line:
            prefix,value=line.lstrip().split('command is')
            cmd='%s&etcid="%s"\n'%(value[0:-2],
                                   testname)
            #Entry in the new dictionary
            ktuple=gencases.line2ktuple(cmd)
            try:
                d[ktuple].append(testname)
            except KeyError:
                d[ktuple]=[testname]
                
    log.close()
    #Save the resulting library
    pickle.dump(d,out)
    out.close()
            
if __name__ == '__main__':
    run(sys.argv[1])
