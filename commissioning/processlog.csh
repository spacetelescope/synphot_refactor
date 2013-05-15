#! /bin/csh
# Pull only the pysynphot commands out of an ETC logfile
# *** Run this first, then run the resulting .txt file through
# *** gencases.py.
#.....................................................................
#Get the input filename
if ( "$1" == "" ) then
  echo -n "Enter filename: "
  set fname = $<
else
  set fname = $1
endif

#Create the output filename
set outname=`echo $fname | sed 's/\.log$/.txt/'  ` 

#Pull out only the pysynphot commands & send them to the output file.
grep command $fname | awk '{print $4}' > $outname
