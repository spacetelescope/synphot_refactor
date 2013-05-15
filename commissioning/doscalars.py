import kwfile_dict
import glob, os, sys
import numpy as N
import pyfits
import pylab as P
import matplotlib

def getdata(dirpath,fieldname,instr,save=True):
    #get the list of files
    flist=glob.glob("%s/*.log"%dirpath)
    #make the arrays
    nfiles=len(flist)
    if nfiles == 0:
        raise ValueError('No files found')
    
    val=N.zeros((nfiles,),dtype=N.float64)
    obsmode=N.zeros((nfiles,),dtype=N.float64)
    spectrum=N.zeros((nfiles,),dtype=N.float64)
    #
    # Make the dicts
    olist=[]
    odict={}
    ocount=0
    sdict={}
    scount=0
    namedict={}
    i=0
    
    #
    # Start processing
    for fname in flist:
        d=kwfile_dict.read_kwfile(fname)
        namedict[i]=fname

        om=d['tda_obsmode']
        olist.append(om)
        if om not in odict:
            odict[om]=ocount
            ocount+=1
        obsmode[i]=odict[om]

        sp=d['tda_spectrum']
        if sp not in sdict:
            sdict[sp]=scount
            scount+=1
        spectrum[i]=sdict[sp]
        
        try:
            val[i]=float(d['tra_discrep'])
        except KeyError:
            #Cases with errors don't have results.
            pass
        i+=1

    #Save our results as a FITS table
    if save:
        tmp=[len(x) for x in flist]
        c1=pyfits.Column(name='logfile',format='%dA'%max(tmp),
                         array=N.array(flist))
        tmp=[len(x) for x in olist]
        c2=pyfits.Column(name='obsmode',format='%dA'%max(tmp),
                         array=N.array(olist))
        c3=pyfits.Column(name='obscode',format='I',
                         array=obsmode)
        c4=pyfits.Column(name='spcode',format='I',
                         array=spectrum)
        c5=pyfits.Column(name='discrep',format='D',
                         array=val)

        tbhdu=pyfits.new_table(pyfits.ColDefs([c1,c2,c3,c4,c5]))
        outname=os.path.join(os.path.abspath(os.path.dirname(dirpath)),
                             "%s_%s_table.fits"%(instr,fieldname))
        tbhdu.writeto(outname,clobber=True)

    #and return the values for immediate use
    return namedict,odict,sdict,obsmode,spectrum,val

def reverse(d):
    """Return a reverse lookup dictionary for the input dictionary"""
    r={}
    for k in d:
        r[d[k]]=k
    return r

def plotdata(obsmode,spectrum,val,odict,sdict,
             instr,fieldname,outdir,outname):
    isetting=P.isinteractive()
    P.ioff()
    
    P.clf()
    P.plot(obsmode,val,'.')
    P.ylabel('(pysyn-syn)/syn')
    P.xlabel('obsmode')
    P.title("%s: %s"%(instr,fieldname))
    P.savefig(os.path.join(outdir,outname+'_obsmode.ps'))

    P.clf()
    P.plot(spectrum,val,'.')
    P.ylabel('(pysyn-syn)/syn')
    P.xlabel('spectrum')
    P.title("%s: %s"%(instr,fieldname))
    P.savefig(os.path.join(outdir,outname+'_spectrum.ps'))

    matplotlib.interactive(isetting)

def run(dirpath, fieldname, instr):
    
    namedict,odict,sdict,obsmode,spectrum,val = getdata(dirpath,
                                                        fieldname,
                                                        instr)
    outdir=os.path.abspath(os.path.dirname(dirpath))
    outname="%s_%s"%(instr,fieldname)
    plotdata(obsmode,spectrum,val,odict,sdict,
             instr,fieldname,outdir,outname)

if __name__ == '__main__':
    #dirpath, fieldname, instr=sys.argv[1:]
    try:
        run(*sys.argv[1:])
    except TypeError,e:
        print "sys.argv[1:] = ",sys.argv[1:]
        raise e
