from __future__ import division
import unittest
import numpy as N
import pysynphot as S

class TestDefault(unittest.TestCase):
    def setUp(self):
        self.sp=S.BlackBody(4400)
        #Note that this bandpass has a simple 1A-spacing binwave
        self.bp=S.ObsBandpass('acs,hrc,f555w')
        self.refwave = 5500 #Angstroms
        self.obs=S.Observation(self.sp,self.bp)
        self.obs.convert('counts')
        self.tda=dict(thresh=0.001)
        self.tra=dict()
        self.tda['spectrum']=str(self.sp)
        self.tra['bandpass']=str(self.bp)

    def testref(self):
        self.tda['wave']=self.refwave
        #Computed by hand for a case that matches exactly:
## >>> sp=S.BlackBody(4400)
## >>> bp=S.ObsBandpass('acs,hrc,f555w')
## >>> obs=S.Observation(sp,bp)
## >>> obs.convert('counts')
## >>> import numpy as N
## >>> N.where(obs.binwave == 5500)
## (array([4500]),)
## >>> obs.binwave[4500]
## 5500.0
## >>> obs.binflux[4500]
## 2.9944715270345599
## >>> print obs.bandpass.obsmode.gtname
## /grp/hst/cdbs/mtab/t2605492m_tmg.fits
## >>> print obs.bandpass.obsmode.ctname
## /grp/hst/cdbs/mtab/t8h1822tm_tmc.fits

        ref = self.obs.binflux[self.obs.binwave == 5500.0]
        tst = self.obs.sample(self.refwave,
                              binned=True,
                              fluxunits='counts')

        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tda['test']=tst
        #Since we're getting the ref out of the same array, the
        #numbers really should be exactly the same
        self.assert_(abs(self.tra['discrep']) == 0,
                     'expected %f, got %f'%(ref,tst))

    def testp3(self):
        self.tda['wave']=5523.3
        #Important note: binwave contains bin _centers_.
        ref=self.obs.binflux[self.obs.binwave == 5523.0]

        tst = self.obs.sample(self.tda['wave'],binned=True,fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tda['test']=tst
        self.assert_(abs(self.tra['discrep']) == 0.0,
                     'expected %f, got %f'%(ref,tst))

    def testp8(self):
        self.tda['wave']=5523.8
        #Important note: binwave contains bin _centers_.
        ref=self.obs.binflux[self.obs.binwave == 5524.0]

        tst = self.obs.sample(self.tda['wave'],binned=True,fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tda['test']=tst
        self.assert_(abs(self.tra['discrep']) ==0.0,
                     'expected %f, got %f'%(ref,tst))

class TestStisDef(unittest.TestCase):
    #Same tests for an actual disperser
    def setUp(self):
        #Use a defined comptab here: we're examining native arrays
        self.oldref = S.refs.getref()
        S.setref(comptable='$PYSYN_CDBS/mtab/u4c18498m_tmc.fits')
        self.sp=S.BlackBody(4400)
        self.bp=S.ObsBandpass('stis,fuvmama,g140m,c1470,s52x01')
        self.obs=S.Observation(self.sp,self.bp)
        self.refwave=1450
        self.tda=dict(thresh=0.001)
        self.tra=dict()
        self.tda['spectrum']=str(self.sp)
        self.tra['bandpass']=str(self.bp)

    def tearDown(self):
        S.setref(comptable=self.oldref['comptable'])

## >>> bp=S.ObsBandpass('stis,fuvmama,g140m,c1470,s52x01')
## >>> sp=S.BlackBody(4400)
## >>> obs=S.Observation(sp,bp)
## >>> obs.convert('counts')
## >>> N.where(obs.binwave == 1450)
## (array([150]),)
## >>> obs.binwave[150:152]
## array([ 1450.  ,  1450.05])
## >>> obs.binflux[150:152]
## array([  4.43311555e-08,   4.43461351e-08])



    def testref(self):
        ref= 4.43311555e-08
        tst = self.obs.sample(self.refwave, binned=True, fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'],
                     'expected %f, got %f'%(ref,tst))

    def testp3(self):
        ref=4.43311555e-08
        tst = self.obs.sample(self.refwave + 0.03, binned=True, fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'],
                     'expected %f, got %f'%(ref,tst))

    def testp8(self):
        ref=4.43461351e-08
        tst = self.obs.sample(self.refwave + 0.08, binned=True, fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'],
                     'expected %f, got %f'%(ref,tst))

    def testnativeref(self):

        #Look up the reference in the correct units
        self.obs.convert('counts')
        ref=self.obs.flux[self.obs.wave==self.refwave]
        self.obs.convert('photlam')

        tst = self.obs.sample(self.refwave,
                              binned=False,
                              fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        #This one may not be an exact match. Although refwave is
        #an exact match in the lookup,
        self.assert_(ref == tst,
                     'expected %f, got %f'%(ref,tst))

## >>> N.where(obs.wave == 1450)
## (array([3940]),)
## >>> print obs.wave[3940:3950]
## [ 1450.          1450.21671168  1450.25        1450.5         1450.75
##   1450.78984087  1451.          1451.25        1451.36319656  1451.5       ]
## [  2.06898932e-07   1.10989755e-07   1.25796555e-07   2.22402574e-07
##    1.29139263e-07   1.11417857e-07   2.05368961e-07   1.62366229e-07
##    1.11846665e-07   1.73209096e-07]
## >>> x=[1450.0, 1450.03, 1450.1, 1450.20]
## >>> N.interp(x,obs.wave,obs.flux)
## array([  2.06898932e-07,   1.93621958e-07,   1.62642353e-07,
##          1.18385774e-07])

    def testnp03(self):
        self.refwave=1450.03
        ref=1.93621958e-07
        tst = self.obs.sample(self.refwave,
                              binned=False,
                              fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'])

    def testnp1(self):
        self.refwave=1450.1
        ref=1.62642353e-07
        tst = self.obs.sample(self.refwave,
                              binned=False,
                              fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'])

    def testnp2(self):
        self.refwave=1450.2
        ref= 1.18385774e-07
        tst = self.obs.sample(self.refwave,
                              binned=False,
                              fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'])

    def testnlast(self):
        self.refwave=self.obs.binwave[-1]
        ref = self.obs.binflux[-1]
        tst = self.obs.sample(self.refwave,
                              binned=False,
                              fluxunits='counts')
        self.tra['discrep']=(ref-tst)/ref
        self.tda['ref']=ref
        self.tra['test']=tst
        self.assert_(self.tra['discrep']<=self.tda['thresh'])
