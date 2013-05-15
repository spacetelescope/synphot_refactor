rootdir='/eng/ssb/syn_pysyn/24jun_r487/stis_etc_cases/testspecphotlam/'
files1=findfile(rootdir+'SpecSourcerateSpecCase*_cs_pysyn.fits')
files2=findfile(rootdir+'SpecSourcerateSpecCase*_cs.fits')

openw,1,'checkresults.txt'
printf,1
printf,1,rootdir
printf,1
for i=0,n_elements(files1)-1 do begin


    data1=mrdfits(files1(i),1,head1)
    data2=mrdfits(files2(i),1,head2)
    
    npts=n_elements(data1.flux)
    edge=fix(0.02*npts)
     data1 = data1[edge:npts-edge-1]
     data2 = data2[edge:npts-edge-1]
    
    index=where(data1.flux gt 0 and data2.flux gt 0)
    print,'Number zeros: ',n_elements(index)
    data1=data1[index]
    data2=data2[index]
    fratio=1.-data1.flux/data2.flux
    
    temp=moment(fratio,sdev=sdev)
    bad=where( abs(fratio) gt 0.2)
    print,'No bad points = ',n_elements(bad)
    print,'Sigma: ',sdev
    
    plot,data1.wavelength,alog10(data1.flux),title=strmid(files1(i),61)
    plot,data2.wavelength,alog10(data2.flux),title=strmid(files2(i),61)
    plot,fratio, $
            title=strmid(files1(i),61)+'/'+strmid(files2(i),61)

    printf,1
    printf,1,files1(i)
    printf,1,files2(i)
    printf,1,'sdev = ', sdev, '  Bad points = ', n_elements(bad),'  Edge= ',edge
    endfor

rootdir='/eng/ssb/syn_pysyn/24jun_r487/stis_etc_cases/testcrphotlam/'
files1=findfile(rootdir+'SpecSourcerateSpecCase*_cr_pysyn.fits')
files2=findfile(rootdir+'SpecSourcerateSpecCase*_cr.fits')
printf,1
printf,1,rootdir
printf,1

for i=0,n_elements(files1)-1 do begin

    data1=mrdfits(files1(i),1,head1)
    data2=mrdfits(files2(i),1,head2)
    
    npts=n_elements(data1.flux)
    edge=fix(0.02*npts)
     data1 = data1[edge:npts-edge-1]
     data2 = data2[edge:npts-edge-1]
    
    index=where(data1.flux gt 0 and data2.flux gt 0)
    print,'Number zeros: ',n_elements(index)
    data1=data1[index]
    data2=data2[index]
    fratio=1.-data1.flux/data2.flux
    
    temp=moment(fratio,sdev=sdev)
    bad=where( abs(fratio) gt .2)
    nbad=0
    if (size(bad,/n_dimensions) gt 0) then nbad =n_elements(bad)
    print,'No bad points = ',nbad
    print,'Sigma: ',sdev
    
    if (nbad gt 0) then begin
    plot,data1.wavelength,alog10(data1.flux),title=strmid(files1(i),77)
    plot,data2.wavelength,alog10(data2.flux),title=strmid(files2(i),77)
    plot,fratio, $
            title=strmid(files1(i),77)+'/'+strmid(files2(i),77)
    endif
    
    printf,1
    printf,1,files1(i)
    printf,1,files2(i)
    printf,1,'sdev = ', sdev, '  Bad points = ', n_elements(bad),'  Edge= ',edge
    printf,1,npts
    printf,1,bad
    
    endfor

close,1
    
end
