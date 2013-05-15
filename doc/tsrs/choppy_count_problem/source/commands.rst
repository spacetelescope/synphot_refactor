Appendix: Commands used to generate plots
==========================================

The version of pysynphot used for this investigation was::

    URL: https://svn.stsci.edu/svn/ssb/astrolib/tags/pysynphot_v0.61_ETC18.0
    Repository Root: https://svn.stsci.edu/svn/ssb/astrolib
    Revision: 1143
    Last Changed Author: laidler
    Last Changed Rev: 1080
    Last Changed Date: 2009-08-14 14:57:05 -0400 (Fri, 14 Aug 2009)

#Examine spectrum as presented in CDBS::

    sp=S.FileSpectrum('/grp/hst/cdbs/calspec/lds749b_mod_001.fits')
    clf()
    plot(sp.wave,sp.flux)
    xlabel(sp.waveunits)
    ylabel(sp.fluxunits)
    title(sp)
    xlim(1100,1500)
    savefig('cdbs_flam.png')

#Examine bin widths of spectrum::

   dw=sp.wave[1:]-sp.wave[:-1]
   plot(sp.wave[1:],dw,'.')
   xlabel('angstrom')
   ylabel('binwidth')
   title(sp)
   savefig('binwidth.png')
   xlim(1100,1500)
   ylim(0,0.6)
   savefig('binwidth_zoom.png')
                                                          

#Previously obtain and save SYNPHOT spectrum using calcspec task::

#--> lpar calcspec
#     spectrum = "crcalspec$lds749b_mod_001.fits" Spectrum to calculate
#       output = "lds749b.fits"  Output table name
#        (form = "counts")       Desired form of output spectrum

#Read in this spectrum to examine its wavelength array::

   synspec=S.FileSpectrum('lds749b.fits')
   syndw=synspec.wave[1:]-synspec.wave[:-1]
   plot(synspec.wave[1:],syndw,'.')
   xlabel('angstrom')
   ylabel('binwidth')
   title('crcalspec$lds749b_mod_001.fits rendered in SYNPHOT')
   savefig('syn_binwidth.png')
   xlim(1100,1500)
   ylim(0,.6)
   savefig('syn_binwidth_zoom.png')

#Examine the spectrum in pysynphot on the SYNPHOT waveset::

   sp.convert('counts')
   plot(synspec.wave,sp.sample(synspec.wave),'.-')
   xlim(1100,1500)
   ylim(0,30)
   xlabel(synspec.waveunits)
   ylabel(sp.fluxunits)
   title("%s sampled on SYNPHOT wavelength array"%os.path.basename(str(sp)))
   savefig('syn_sampled_counts.png')
                                                      
