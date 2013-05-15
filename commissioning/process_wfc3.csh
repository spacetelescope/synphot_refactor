#! /bin/csh -x

set newfiles = (wfc3IRImagingPysynphotLog.txt wfc3IRSpecPysynphotLog.txt wfc3UVIS1ImagingPysynphotLog.txt wfc3UVIS1SpecPysynphotLog.txt wfc3UVIS2ImagingPysynphotLog.txt wfc3UVIS2SpecPysynphotLog.txt)

foreach x ($newfiles)
   python parselog.py $x
end

set irfiles = ( wfc3IRImagingPysynphotLog_parsed.txt wfc3IRSpecPysynphotLog_parsed.txt )
foreach x ($irfiles)
   cull_thermback.csh $x
end

set allfiles = (wfc3IRImagingPysynphotLog_parsed_thermback.txt wfc3IRSpecPysynphotLog_parsed_thermback.txt wfc3IRImagingPysynphotLog_parsed_nonthermback.txt wfc3IRSpecPysynphotLog_parsed_nonthermback.txt wfc3UVIS1ImagingPysynphotLog_parsed.txt wfc3UVIS1SpecPysynphotLog_parsed.txt wfc3UVIS2ImagingPysynphotLog_parsed.txt wfc3UVIS2SpecPysynphotLog_parsed.txt)

set oldfiles = (wfc3_ir_imaging_80_thermback.txt wfc3_ir_spec_62_thermback.txt wfc3_ir_imaging_78_cases.txt wfc3_ir_spec_61_cases.txt wfc3_uvis1_imaging_61_cases.txt wfc3_uvis1_spec_62_cases.txt wfc3_uvis2_imaging_18_cases.txt wfc3_uvis2_spec_18_cases.txt)

foreach i (1 2 3 4 5 6 7 8)
   echo $oldfiles[$i] 
   python ../gencases.py $oldfiles[$i]
   echo $allfiles[$i]
   ln -s `basename $oldfiles[$i] txt`pickle `basename $newfiles[$i] txt`pickle
   python ../gencases.py $allfiles[$i] 
   diff `basename $oldfiles[$i] txt`py `basename $allfiles[$i] txt`py
   echo ".............."
end
