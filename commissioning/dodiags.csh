#! /bin/csh
#
#Just run the diagnostics on everything in a given directory
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter dirname: "
  set dirname = $<
else
  set dirname = $1
endif

cd $dirname

#.........................................
# Hardcode the lists of tests for the moment.
set tlist = "acs_etc_cases nicmos_etc_cases stis_etc_cases wfc3_ir_imaging_78_cases wfc3_ir_spec_61_cases wfc3_uvis1_imaging_61_cases wfc3_uvis1_spec_62_cases wfc3_uvis2_imaging_18_cases wfc3_uvis2_spec_18_cases"
#.........................................
echo $PYTHONPATH
set codeplace = /data/gaudete1/dg1/laidler/ssb/checkout/pysynphot/test/commissioning
setenv PATH {$PATH}:{$codeplace}
foreach tname ($tlist)
  echo $tname
  casestats.csh $tname > $tname.stats
  set instr = `echo $tname | awk -F _ '{print $1}'`
  python $codeplace/doscalars.py $tname/testefflam efflam $instr
  python $codeplace/doscalars.py $tname/testcountrate countrate $instr
end
