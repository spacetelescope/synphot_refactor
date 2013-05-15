import re,os,glob
import numpy as N
import pylab as P

def read_kwfile(fname):
    """Syntax used as of r452 in commissioning tests"""
    d={}
    f=open(fname)
    for line in f:
        try:
            kvpair=re.findall("(.*):: (.*)=(.*)$",line)[0]
            d['name']=os.path.basename(kvpair[0])
            key,val=kvpair[1:]
            d[key.lower()]=val
        except (ValueError,IndexError):
            break
        
    f.close()
    return d

def accumdict(fulldict,adict):
    if len(fulldict) == 0:
        fulldict=fulldict.fromkeys(adict)
        for k in fulldict:
            fulldict[k]=[adict[k]]
    else:
        for k in fulldict:
            fulldict[k].append(adict.get(k,0.0))
    return fulldict

def setstruct(mystruct,fulldict):
    for k in fulldict:
        try:
            setattr(mystruct,k,N.array([float(x) for x in fulldict[k]]))
        except ValueError:
            setattr(mystruct,k,N.array(fulldict[k]))
    return mystruct

class Container(object):
    def __init__(self,fulldict):
        for k in fulldict:
            try:
                setattr(self,k,N.array([float(x) for x in fulldict[k]]))
            except ValueError:
                setattr(self,k,N.array(fulldict[k]))

    def plot(self,label,outname):
        P.clf()
        P.plot(self.tra_Discrep,'.')
        P.ylabel('(pysyn-syn)/syn')    
        P.title(label)
        P.savefig(outname)
        
def getcountrate(dirname):
    flist=glob.glob("%s/*.log"%dirname)
    if len(flist) == 0:
        raise ValueError("No files found")
    crdict={}
    for fname in flist:
        d=read_kwfile(fname)
        crdict=accumdict(crdict,d)

    crdata=Container(crdict)
    return crdata
    
