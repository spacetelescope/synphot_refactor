from pytools import testutil
import pysynphot as S
import numpy as N
import pyfits
from pysynphot import etc
from pyraf import iraf
from iraf import stsdas,hst_calib,synphot
import os,time,re
from pysynphot.wavetable import wavetable as Wavecat
from pysynphot.observationmode import ObservationMode


class calcspecCase(testutil.LogTestCase):
    def setUp(self):
        self.obsmode=None
        self.spectrum=None
        self.runpy()
        self.skip=True

    def hasSkyLines(self):
        lnames="el1215a|el1302a|el1356a|el2471a"
        ans=re.findall(lnames,self.spectrum)
        if len(ans) > 0:
            return True
        else:
            return False
        
    def setglobal(self,fname=None):
        if fname is None:
            fname=__file__
        self.propername=self.id()
        base,ext=os.path.splitext(os.path.basename(fname))
        main,case,test=self.propername.split('.')
        self.name=os.path.join(base,test,case)
        self.wavename=self.name+'_wave.fits'
        #Make sure the directories exist
        dirname=os.path.dirname(self.name)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
            
        self.file=self.name
        self.thresh=0.01
        self.superthresh=0.20
        self.sigthresh=0.01
        self.discrep=-99
        self.tda={'Obsmode':self.obsmode,
                 'Spectrum':self.spectrum,
                  'ETCid':None, #placeholder
                 'Thresh':self.thresh,
                  'Superthresh':self.superthresh,
                  'SigThresh':self.sigthresh,
                  'crrefer':iraf.osfn('crrefer$'),
                  'pysyn_cdbs':os.environ['PYSYN_CDBS'],
                  'SkyLines':self.hasSkyLines()}
        try:
            self.tda['Subset']=self.subset
        except AttributeError:
            pass
        try:
            self.tda['ETCid']=self.etcid
        except AttributeError:
            pass
        try:
            self.tda['form']=self.form
        except AttributeError:
            pass
        
        self.tra={}

    def run_crbox(self,spstring,form,output="",wavecat="INDEF",
                  lowave=0,hiwave=30000):
        """Calcspec has a bug. We will use countrate instead, and force it
        to use a box function of uniform transmission as the obsmode."""

        range=hiwave-lowave
        midwave=range/2.0
        iraf.countrate(spectrum=spstring, magnitude="",
                       instrument="box(%f,%f)"%(midwave,range),
                       form=form,
                       wavecat=wavecat,
                       output=output)
        

    def run_countrate(self,form,output=None):
        if output is None:
            output=""
        count=0
        while count < 10:
            try:
                iraf.countrate(spectrum=self.spectrum,magnitude="",
                               instrument=self.obsmode,
                               output=output,form=form)
                break
            except iraf.IrafError,e:
                count+=1
                pass

        if count == 10:
            raise(e)
        
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.csname=self.name+'.fits'
        self.specname=self.name+'_spec.fits'
        for name in (self.csname, self.specname, self.wavename):
            try:
                os.remove(name)
            except OSError:
                pass

    def arraydiff(self,test,ref):
        idx=N.nonzero(ref)
        ans=(test[idx]-ref[idx])/ref[idx]
        return ans

    def arraysigtest(self,test,ref):
        #Raise an error if the arrays are not the same size
        if test.shape != ref.shape:
            raise ValueError("Array size mismatch")
        tt=test[2:-2]
        rr=ref[2:-2]
        #Identify the significant elements
        tidx=N.where(tt>(self.sigthresh*tt.max()))[0]
        ridx=N.where(rr>(self.sigthresh*rr.max()))[0]
        #Set a flag if they're not the same set
        if not (N.alltrue(tidx == ridx)):
            self.tra['SigElemDiscrep']=True
            tidx=ridx

        #Now compare only the significant elements.
        #We no longer need to exclude points with zero value, because
        #those points were already excluded as insignificant.
        self.arraytest(tt[ridx],rr[ridx])


    def count_outliers(self,Nsigma=3):
        mean=self.adiscrep.mean()
        std=self.adiscrep.std()
        outliers=N.where(abs(self.adiscrep) > mean + Nsigma*std)
        return len(outliers[0])
    
    def arraytest(self,test,ref):
        #Exclude the endpoints where the gradient is very steep
        self.adiscrep=self.arraydiff(test,ref)#[2:-2]
        count=N.where(abs(self.adiscrep)>self.thresh)[0].size
        try:
            self.tra['Discrepfrac']=float(count)/self.adiscrep.size
            self.tra['Discrepmin']=self.adiscrep.min()
            self.tra['Discrepmax']=self.adiscrep.max()
            self.tra['Discrepmean']=self.adiscrep.mean()
            self.tra['Discrepstd']=self.adiscrep.std()
            self.tra['Outliers']=self.count_outliers(5)
            if (self.tra['Discrepfrac'] > self.superthresh):
                self.tra['Extreme']=True
            self.failUnless(N.alltrue(abs(self.adiscrep)<self.thresh),
                            msg="Worst case %f"%abs(self.adiscrep).max())
        except ZeroDivisionError:
            self.tra['Discrepfrac']=0.0
            self.tra['Discrepmin']=0.0
            self.tra['Discrepmax']=0.0


    def savepysyn(self,wave,flux,fname,units=None):
        """ Cannot ever use the .writefits() method, because the array is
        frequently just sampled at the synphot waveset; plus, writefits
        is smart and does things like tapering."""
        if units is None:
            ytype='throughput'
            units=' '
        else:
            ytype='flux'
        col1=pyfits.Column(name='wavelength',format='D',array=wave)
        col2=pyfits.Column(name=ytype,format='D',array=flux)
        tbhdu=pyfits.new_table(pyfits.ColDefs([col1,col2]))
        tbhdu.header.update('tunit1','angstrom')
        tbhdu.header.update('tunit2',units)
        tbhdu.writeto(fname.replace('.fits','_pysyn.fits'))

    def testcrspec(self):
        #Use countrate with a box; use the native waveset as the waveset
        wname='/tmp/%s_box.cat'%os.path.basename(self.name)
        self.sptest.convert('photlam')
        self.sptest.writefits(self.csname.replace('.fits','_pysyn.fits'),
                              precision='single')

        out=open(wname,'w')
        out.write('box    %s\n'%self.csname.replace('.fits','_pysyn.fits'))
        out.close()

        #Put this in a loop to compensate for an apparent race condition
        #that sometimes prevents the IRAF task from opening the file.
        count=0
        while count<10:
            try:
                self.run_crbox(self.spectrum,'photlam',
                               output=self.csname,
                               wavecat=wname,
                               hiwave=self.sptest.wave.max())
                break
            except iraf.IrafError,e:
                count+=1
                pass

        if count == 10:
            raise e
        
        os.unlink(wname)

        #Now do the comparison
        spref=S.FileSpectrum(self.csname)
        ridx=N.where(spref.wave >= 900.0)
        rflux=spref.flux[ridx]
        tflux=self.sptest(spref.wave[ridx])
        self.arraysigtest(tflux,rflux)
        
class calcphotCase(calcspecCase):
    Extrap=None
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.cbname=self.name+'.fits'
        self.csname=self.name+'_cs.fits'

        for fname in (self.cbname, self.csname):
            try:
                os.remove(fname)
                os.remove(fname.replace('.fits','_pysyn.fits'))
            except OSError:
                pass
        self.discrep=-99
        

     
                    
    def testthru(self):
        iraf.calcband(obsmode=self.obsmode,output=self.cbname)
        ref=S.FileBandpass(self.cbname)
        rthru=ref.throughput
        rwave=ref.wave
        tthru=self.bp(rwave)
        self.savepysyn(rwave,tthru,self.cbname)
        self.arraysigtest(tthru,rthru)

        
    def testefflam(self):
        iraf.calcphot(obsmode=self.obsmode,spectrum=self.spectrum,
                      form='photlam', func='efflerg')
        rlam=iraf.calcphot.getParam('calcphot.result',native=1)
        obs=S.Observation(self.sptest,self.bp,force=self.Extrap)
        tlam=obs.efflam()
        if rlam != 0:
            self.discrep=(tlam-rlam)/rlam
        else:
            self.discrep=tlam-rlam
        self.tra['Discrep']=self.discrep
        if abs(self.discrep)>self.superthresh:
            self.tra['Extreme']=True
        self.tra['Syn']=rlam
        self.tra['Pysyn']=tlam

        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)

class calcphotOverlapCase(calcphotCase):
    Extrap='taper'

class effstimCase(calcphotCase):
    def testeffstim(self):
        iraf.calcphot(obsmode=self.obsmode,spectrum=self.spectrum,
                      form=self.form,func='effstim')
        rcounts=iraf.calcphot.getParam('calcphot.result',native=1)
        obs=S.Observation(self.sptest,self.bp)
        tcounts=obs.effstim(self.form)
        self.tra['Syn']=rcounts
        self.tra['Pysyn']=tcounts

        if rcounts != 0:
            self.discrep=(tcounts-rcounts)/rcounts
        else:
            self.discrep=tcounts-rcounts
        self.tra['Discrep']=self.discrep
        if abs(self.discrep)>self.superthresh:
            self.tra['Extreme']=True

        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)
    def testthru(self):
        __test__ = False
    def testefflam(self):
        __test__ = False
        

class thermbackCase(calcspecCase):
        
    def runpy(self):

        #self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.cbname=self.name+'.fits'
        self.csname=self.name+'_cs.fits'

        for fname in (self.cbname, self.csname):
            try:
                os.remove(fname)
                os.remove(fname.replace('.fits','_pysyn.fits'))
            except OSError:
                pass
        self.discrep=-99

        #Both tests need this
        omode=ObservationMode(self.obsmode)
        self.sptest=omode.ThermalSpectrum()
        self.ttherm=self.sptest.integrate()*omode.pixscale**2*omode.area
        self.sptest.convert('counts')


    def testcrspec(self):
        iraf.thermback(obsmode=self.obsmode,form='counts',
                       output=self.csname)

        spref=S.FileSpectrum(self.csname)
        self.savepysyn(spref.wave,self.sptest.sample(spref.wave),
                       self.csname,units='counts')

        ridx=N.where(spref.wave >= 900.0)
        rflux=spref.flux[ridx]
        tflux=self.sptest.sample(spref.wave[ridx])
        self.arraysigtest(tflux,rflux)


##-----------------------------------------------------------------------
## The wave arrays are never equal; comment out this test.
##........................................................................
##     def testthermspec(self):
##         ref=S.FileSpectrum(self.csname)
##         if N.any(self.sp.wave != ref.wave):
##             raise ValueError('wave arrays not equal')
##         self.arraysigtest(self.sp.flux,ref.flux)
        
    def testthermback(self):
        iraf.thermback(obsmode=self.obsmode,form='counts')
        rtherm=iraf.thermback.getParam('thermback.thermflux',native=1)
        ttherm=self.ttherm
        if rtherm != 0:
            self.discrep=(ttherm-rtherm)/rtherm
        else:
            self.discrep=ttherm-rtherm
        self.tra['Discrep']=self.discrep
        if abs(self.discrep)>self.superthresh:
            self.tra['Extreme']=True
        self.tra['Syn']=rtherm
        self.tra['Pysyn']=ttherm

        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)



class countrateCase(calcphotCase):
    Extrap=None
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.csname=self.name+'_cs.fits'
        self.crname=self.name+'_cr.fits'
        self.cbname=self.name+'.fits'
        for fname in (self.cbname, self.csname, self.crname):
            try:
                os.remove(fname)
                os.remove(fname.replace('.fits','_pysyn.fits'))
            except OSError:
                pass
    def testcrphotlam(self):
        self.run_countrate('photlam',self.crname)
        spref=S.FileSpectrum(self.crname)
        obs=S.Observation(self.sptest,self.bp,binset=spref.wave,force=self.Extrap)
        obs.convert('photlam')
        ridx=N.where(spref.wave >= 900.0)
        rflux=spref.flux[ridx]
        tidx=N.where(obs.binwave >= 900.0)
        tflux=obs.binflux[tidx]
        self.savepysyn(obs.binwave,obs.binflux,
                       self.crname,units='photlam')
        
        self.arraysigtest(tflux,rflux)

    def testcrcounts(self):
        self.run_countrate('counts',self.crname.replace('.fits','_counts.fits'))
        spref=S.FileSpectrum(self.crname.replace('.fits','_counts.fits'))
        obs=S.Observation(self.sptest,self.bp,binset=spref.wave,force=self.Extrap)
        obs.convert('counts')
        ridx=N.where(spref.wave >= 900.0)
        rflux=spref.flux[ridx]
        tidx=N.where(obs.binwave >= 900.0)
        tflux=obs.binflux[tidx]
        self.savepysyn(obs.binwave,obs.binflux,
                       self.crname.replace('.fits','_counts.fits'),
                       units='counts')
        if N.any(obs.binwave != spref.wave):
            raise ValueError('wave arrays not equal')
        
        self.arraysigtest(tflux,rflux)

    def testcountrate(self):
        obs=S.Observation(self.sptest,self.bp,force=self.Extrap)
        self.run_countrate('counts')
        rval=iraf.countrate.getParam('flux_tot',native=1)
        tval=obs.countrate()
        if rval != 0:
            self.discrep=(tval-rval)/rval
        else:
            self.discrep=tval-rval
        self.tra['Discrep']=self.discrep
        self.tra['Syn']=rval
        self.tra['Pysyn']=tval
        if abs(self.discrep)>self.superthresh:
            self.tra['Extreme']=True
        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)

class countrateOverlapCase(countrateCase):
    Extrap='taper'

class SpecSourcerateSpecCase(countrateCase):
    Extrap=None
    def placeholder(self):
        pass

class SpecSourcerateSpecOverlapCase(countrateCase):
    Extrap='taper'
