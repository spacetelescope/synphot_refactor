"""This script will operate on throughput files to bound them
with zeros. There are three kinds of files to be considered:
  - simple files with wavelength and throughput only
  - simple files with wavelength, throughput, and error
  - parameterized files with multiple throughput columns

  The procedure will be:
  - determine what kind of file it is
  - determine whether it needs to be zero-bounded
  - apply the zero-bounding to all necessary columns
  - update the history or comment records accordingly
"""

import re, time, os, sys
import pyfits
import numpy as N

__version__='1.1d'


def classify_file(f):
    """Examine the column names to determine which type of file
    this is. Return a tuple:
    retvalue[0] = "file is non-parameterized"
    retvalue[1] = "file contains error column"
    """
    cols=f[1].columns
    if len(cols) == 2:
        #Then we must have a simple file
        return (True,False)
    elif len(cols) == 3 and ('ERROR' in cols.names):
        return (True,True)
    elif len(cols) > 2 and ('ERROR' not in cols.names):
        return (True,False)
    else:
        return (False,True)

def run(fname,outdir=None):

    if outdir is not None and not os.path.isdir(outdir):
        os.mkdir(outdir)
        
    dwave=0.001
    f=pyfits.open(fname)
    nonparam,error=classify_file(f)
    #Check whether a fix is needed
    if nonparam: #just check column 1 = throughput
        t=f[1].data.field(1)
        ok = (t[0]==0.0) and (t[-1]==0.0)
    else:
        ok=False
        cols=f[1].columns
        for k in range(1,len(cols)):
            if 'err' not in cols[k].name.lower():
                t=f[1].data.field(k)
                ok = ok and ( (t[0]==0.0) and (t[-1]==0.0) )

    if ok:
        f.close()
        return "%s: no change necessary"%fname
    

    #If not ok, we fall through to here.
    #We're going to have to make a new hdu
    clist=[]
    #And we need column info from the existing hdu
    cols=f[1].columns
    #Always make a new wavelength array
    w=f[1].data.field(0)
    nrows=len(w)
    wave=N.zeros((nrows+2,),dtype=w.dtype)
    wave[1:-1]=w
    wave[0]=w[0]-dwave
    wave[-1]=w[-1]+dwave
    wc=pyfits.Column(name=cols[0].name,
                     format=cols[0].format,
                     array=wave)
    clist.append(wc)
    #Stick zeros on the ends of all other columns, unless
    #there's an "ERR" in their name

    padval={True:100,False:0}
    for k in range(1,len(cols)):
        t=f[1].data.field(k)
        thru=N.zeros((nrows+2,),dtype=t.dtype)
        thru[1:-1]=t
        pv=padval[("err" in cols.names[k].lower())]
        thru[0]=thru[-1]=pv
        tc=pyfits.Column(name=cols[k].name,
                         format=cols[k].format,
                         array=thru)
        clist.append(tc)

    #Now we have all the columns; put them in an HDU
    tbhdu=pyfits.new_table(clist)
    #and copy in the header information we need
    h=f[1].header.copy()
    h.update('NAXIS1',tbhdu.header['NAXIS1'])
    h.update('NAXIS2',tbhdu.header['NAXIS2'])
    tbhdu.header=h


    #Replace the HDU
    f[1]=tbhdu

    #Update the primary header
    f[0].header.add_history(time.asctime())
    f[0].header.add_history("..Added a point with throughput=0 at each end of the")
    f[0].header.add_history("..throughput curves (dLambda=.001A) using the script")
    f[0].header.add_history("..extrap.py v%s. V. Laidler"%__version__)

    #And write out the new file
    if outdir is not None:
        newname=os.path.join(outdir,fincre(fname))
    else:
        newname=fincre(fname)
    f.writeto(newname)

    return("%s -> %s"%(fname, newname))



def blue(fname,outdir=None):
    """Cut&pasted from run, but to operate only on blue end."""
    if outdir is not None and not os.path.isdir(outdir):
        os.mkdir(outdir)
        
    dwave=0.001
    f=pyfits.open(fname)
    nonparam,error=classify_file(f)
    #Check whether a fix is needed
    if nonparam: #just check column 1 = throughput
        t=f[1].data.field(1)
        ok = (t[0]==0.0) and (t[-1]==0.0)
    else:
        ok=False
        cols=f[1].columns
        for k in range(1,len(cols)):
            if 'err' not in cols[k].name.lower():
                t=f[1].data.field(k)
                ok = ok and ( (t[0]==0.0) and (t[-1]==0.0) )

    if ok:
        f.close()
        return "%s: no change necessary"%fname
    

    #If not ok, we fall through to here.
    #We're going to have to make a new hdu
    clist=[]
    #And we need column info from the existing hdu
    cols=f[1].columns
    #Always make a new wavelength array
    w=f[1].data.field(0)
    nrows=len(w)
    wave=N.zeros((nrows+1,),dtype=w.dtype)
    wave[1:]=w
    wave[0]=w[0]-dwave

    wc=pyfits.Column(name=cols[0].name,
                     format=cols[0].format,
                     array=wave)
    clist.append(wc)
    #Stick zeros on the ends of all other columns, unless
    #there's an "ERR" in their name

    padval={True:100,False:0}
    for k in range(1,len(cols)):
        t=f[1].data.field(k)
        thru=N.zeros((nrows+1,),dtype=t.dtype)
        thru[1:]=t
        pv=padval[("err" in cols.names[k].lower())]
        thru[0]=pv
        tc=pyfits.Column(name=cols[k].name,
                         format=cols[k].format,
                         array=thru)
        clist.append(tc)

    #Now we have all the columns; put them in an HDU
    tbhdu=pyfits.new_table(clist)
    #and copy in the header information we need
    h=f[1].header.copy()
    h.update('NAXIS1',tbhdu.header['NAXIS1'])
    h.update('NAXIS2',tbhdu.header['NAXIS2'])
    tbhdu.header=h


    #Replace the HDU
    f[1]=tbhdu

    #Update the primary header
    f[0].header.add_history(time.asctime())
    f[0].header.add_history("..Added a point with throughput=0 at blue end of the")
    f[0].header.add_history("..throughput curves (dLambda=.001A) using the script")
    f[0].header.add_history("..extrap.py v%s. V. Laidler"%__version__)

    #And write out the new file
    if outdir is not None:
        newname=os.path.join(outdir,fincre(fname))
    else:
        newname=fincre(fname)
    f.writeto(newname)

    return("%s -> %s"%(fname, newname))

def fincre(oldname):
    """Increment the synphot version number from a filename"""
    x=re.search('_(?P<version>[0-9][0-9][0-9])_syn',oldname)
    version=x.group('version')
    newversion="%03d"%(int(version)+1)
    ans=oldname.replace(version,newversion)
    return ans


if __name__ == '__main__':
    for fname in sys.argv[1:]:
        retval=run(fname)
        print retval

def buildtmc(tmcname):
    from pyraf import iraf
    from iraf import stsdas,hst_calib,synphot
    out=open('buildtmc.log','w')
    f=pyfits.open(tmcname)
    flist=f[1].data.field('filename')
    iraf.set(crrefer='./') #work locally

    for k in range(len(flist)):
        oldname=iraf.osfn(flist[k]).split('[')[0]
        newname=fincre(oldname)
        if os.path.exists(newname):
            flist[k]=fincre(flist[k])
        else:
            out.write("%s: no change necessary\n"%oldname)
    f.writeto(tmcname.replace(".fits","_new.fits"))
    out.close()
