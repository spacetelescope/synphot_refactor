pro checkfiles,filein

rootdir='/eng/ssb/syn_pysyn/'

filelist=filein+'.lis'
file=''
output = filein+'.output'
openw,2,output
openw,3,filein+'.max'

openr,1,filelist
while(not eof(1)) do begin 
  readf,1,file
  dir=file_dirname(file)
  fname=file_basename(file,'.log')
  files=findfile(rootdir+dir+'/'+fname+'*'+'.fits')
  if (n_elements(files) lt 2) then begin
    printf,2,'*** NO FITS FILES FOUND  ***'
    printf,2,file
    printf,2
  endif else begin
   print,files
  
   files1=files(0)
   files2=files(1)


     data1=mrdfits(files1,1,head1)
     data2=mrdfits(files2,1,head2)
     index=where(data1.flux gt 0 and data2.flux gt 0, count)
     print,'Number of non-zeros: ', count
     if (count gt 1) then begin
      data1=data1[index]
      data2=data2[index]
     
      plottext,rootdir+file
     
      plot,data1.wavelength,alog10(data1.flux),title=fname,$ 
         subtitle=dir,charsize=0.7
      oplot,data2.wavelength,alog10(data2.flux),line=1
      plot,data1.wavelength,1-data1.flux/data2.flux, $
             title=fname + ' 1-SYNPHOT/PYSYN',subtitle=dir,charsize=0.7
      plot,data1.wavelength,(data2.flux-data1.flux)/max(data2.flux),$
             title=fname+' PSYN-SYNPHOT',subtitle=dir,charsize=0.7
      printf,3,max((data2.flux-data1.flux)/max(data2.flux))
      if(max(abs((data2.flux-data1.flux)/max(data2.flux))) gt 0.1) then begin
         printf,2,'**** FAILURE: MAX DIFF GT 0.1 ***'
	 printf,2,file
	 printf,2
	 endif
      endif else begin
         data1=data1[index]
         data2=data2[index]
         printf,2,'*** NOT ENOUGH NON-ZERO POINTS TO PLOT ***'
	 printf,2,file,'Ratio of non-zero point',data2.flux/data1.flux
	 printf,2
	 endelse
     endelse
     
  endwhile
close,1
close,2
close,3

end
