from __future__ import division

import os
import shutil
import tempfile

import numpy as np
from pyraf import iraf
# Initialize the relevant iraf packages
from iraf import stsdas, hst_calib, synphot

import pysynphot as S
from pysynphot.units import Units
from pysynphot import spectrum, renorm


#----------------------------------------------------------
def testRenormSynPysyn():
    jv = S.ObsBandpass('johnson,v')
    acs = S.ObsBandpass('acs,hrc,f555w')
    abox = S.Box(5500,1)

    #Removing vegamag from this list because it introduces
    # a data dependency. Pysynphot has upgraded the version of
    # vega that it uses for vegamag conversions (11/5/2010, r1629)
    # but synphot has not. This caused the emission line test
    # to fail (since the numbers were so small anyway, the small
    # difference exceeded the tolerance).
    uset = ['photlam', 'flam', 'photnu', 'fnu', 'jy', 'mjy', 'counts',
            'stmag' ,'abmag', 'obmag'] #, 'vegamag'


    ucounts = ['counts', 'obmag']

    bb = S.BlackBody(5000)
    bb.syndescrip = 'bb(5000)'

    em = S.GaussianSource(1e-13,5500,250)
    em.syndescrip = 'em(5500,250,1e-13,flam)'

    foo = {bb:'bb', em:'em'}

    rnfuncs = {renorm.StdRenorm:'Std'} #Just this one,
    #        renorm.renormTweak:'tweak',
    #        renorm.renormRevEng:'RevEng'
    #         renorm.renormSVN:'SVN'} - ignore SVN for now, we know it doesn't work
    for method in rnfuncs:
        for sp in (bb, em):
          for u in uset:  # ucounts
            rnunit = Units(u)
            if u == 'counts':
                bp = acs
                bp.syndescrip = "band(%s) " % bp
            elif rnunit.isMag:
                bp = jv
                bp.syndescrip = 'band(johnson,v)'
            else:
                bp = abox
                bp.syndescrip = 'box(5500,1)'


            def renorm_compare(sp, rnval, rnunits, bp, callable):
                """Sp and bp must have a special .syndescrip attribute that
                contains the string needed to make it with synphot"""

                # Renormalize the spectrum
                pysyn = callable(sp, bp, rnval, rnunits)
                #pysyn=sp.renorm(rnval,rnunits,bp)
                #pysyn = spectrum.StdRenorm(sp,bp,rnval,rnunits)


                userdir = tempfile.mkdtemp(suffix='pysynphot')
                old_cwd = os.getcwd()
                iraf.chdir(userdir)

                # Make a wavetable and a wavecat
                fname = "%s.fits" % rnunits
                pysyn.writefits(fname, clobber=True)
                wname = "%s.cat" % rnunits

                f = open(wname, 'w')
                f.write("box   %s\n" % fname)
                f.close()

                oname = "syn_%s" % fname

                try:
                    #Run countrate
                    spstring = "rn(%s,%s,%s,%s) " % (sp.syndescrip,
                                                     bp.syndescrip, rnval,
                                                     rnunits)
                    iraf.countrate(spectrum=spstring, magnitude="",
                                   instrument="box(15000,30000)",
                                   form=str(pysyn.fluxunits), wavecat=wname,
                                   output=oname)
                    syn = S.FileSpectrum(oname)

                    # Check that they have the same shape and fluxunits
                    assert (syn.flux.shape == pysyn.flux.shape)
                    assert (type(syn.fluxunits) == type(pysyn.fluxunits))

                    # Now a real test
                    idx = np.where(syn.flux != 0)
                    rat = (syn.flux[idx] / pysyn.flux[idx])
                    q = abs(1 - rat[2:-2])
                    qtrunc = (10**4*q).astype(np.int)
                    assert np.alltrue(qtrunc < 110), \
                           "Min/max ratio = %f,%f" % (q.min(),q.max())
                finally:
                    iraf.chdir(old_cwd)
                    shutil.rmtree(userdir)

            renorm_compare.description = (
                "%s.test%s_%s_%s" % (__name__, rnfuncs[method], foo[sp], u))

            yield renorm_compare, sp, 10, u, bp, method

