rootdir='/eng/ssb/syn_pysyn/24jun_r487/stis_etc_cases/testcrphotlam/'
files1=findfile(rootdir+'SpecSourcerateSpecCase*_cr_pysyn.fits')
files2=findfile(rootdir+'SpecSourcerateSpecCase*_cr.fits')

for i=0,n_elements(files1)-1 do begin

    data1=mrdfits(files1(i),1,head1)
    data2=mrdfits(files2(i),1,head2)
    
    index=where(data1.flux gt 0 and data2.flux gt 0)
    data1=data1[index]
    data2=data2[index]
    fratio=1.-data1.flux/data2.flux
    temp=moment(fratio,sdev=sdev)
    bad=where( abs(fratio) gt 3.*sdev)
    print,'No bad points = ',n_elements(bad)
    print,'Sigma: ',sdev
    fratio=fratio[where(abs(fratio) lt 3.*sdev)]
    temp=moment(fratio,sdev=sdev)
    bad=where( abs(fratio) gt 3.*sdev)
    print,'No bad points = ',n_elements(bad)
    print,'Sigma: ',sdev
    fratio=fratio[where(abs(fratio) lt 3.*sdev)]
    
    
;    data1.flux = median(data1.flux,7)
;    data2.flux = median(data2.flux,7)
    
     plot,data1.wavelength,alog10(data1.flux),title=strmid(files1(i),77)
     plot,data2.wavelength,alog10(data2.flux),title=strmid(files2(i),77)
     plot,1-data1.flux/data2.flux, $
            title='1-'+strmid(files1(i),77)+'/'+strmid(files2(i),77)
     plot,fratio[where(abs(fratio) lt 3.*sdev)], $
            title='1-'+strmid(files1(i),77)+'/'+strmid(files2(i),77)
     
     endfor
    
end
