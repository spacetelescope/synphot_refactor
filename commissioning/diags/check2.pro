rootdir='/eng/ssb/syn_pysyn/24jun_r487/stis_etc_cases/testcrphotlam/'
files1=findfile(rootdir+'SpecSourcerateSpecCase*_cr_pysyn.fits')
files2=findfile(rootdir+'SpecSourcerateSpecCase*_cr.fits')

for i=0,n_elements(files1)-1 do begin

    data1=mrdfits(files1(i),1,head1)
    data2=mrdfits(files2(i),1,head2)
    
    plot,data1.wavelength,alog10(data1.flux),title=strmid(files1(i),59)
    plot,data2.wavelength,alog10(data2.flux),title=strmid(files2(i),59)
    plot,data1.wavelength,data1.flux/data2.flux, $
            title=strmid(files1(i),61)+'/'+strmid(files2(i),59)
    plot,data1.wavelength,data1.flux/data2.flux, $
            title=strmid(files1(i),61)+'/'+strmid(files2(i),59),yrange=[.9,1.1]
    endfor
    
end
