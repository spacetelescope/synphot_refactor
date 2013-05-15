pro procfiles,filein

rootdir='/eng/ssb/syn_pysyn/'

filelist=filein+'.lis'
file=''
openw,2,filein+'.nofits'
openw,3,filein+'.max'
openw,4,filein+'_fail.lis'
openw,5,filein+'.scalar'

openr,1,filelist
while(not eof(1)) do begin 
  readf,1,file
  dir=file_dirname(file)
  fname=file_basename(file,'.log')
  files=findfile(rootdir+dir+'/'+fname+'_'+'*'+'.fits')
  if (n_elements(files) lt 2) then begin
    printf,2,file
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
     
      printf,3,max((data2.flux-data1.flux)/max(data2.flux))
      if(max(abs((data2.flux-data1.flux)/max(data2.flux))) gt 0.1) then begin
	 printf,4,file
	 endif
      endif else begin
         data1=data1[index]
         data2=data2[index]
	 printf,5,file,'Ratio of non-zero point',data2.flux/data1.flux
	 endelse
     endelse
     
  endwhile
close,1
close,2
close,3
close,4
close,5

end
