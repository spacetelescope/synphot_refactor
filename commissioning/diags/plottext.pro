pro plottext,file

record=''
get_lun, filein
openr,filein,file

plot,[0,1],[0,1],/nodata,xstyle=4,ystyle=4,title=file,charsize=0.5

ypos=1
yinc=.02
iy=1

while (not eof(filein)) do begin

   readf,filein,record
   xyouts,[0],[1-iy*yinc],record,charsize=0.5
   iy=iy+1
   endwhile
   
free_lun,filein
end
