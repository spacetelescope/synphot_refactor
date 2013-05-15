#! /bin/csh 
#
# Generate a test run for all test cases, organizing the output into
# a subdirectory of the cwd.
#
# Presently hardcodes a bunch of information: where to get the test data,
# and the list of ***python modules*** that contain the tests. Uses 
# nosetests to run the tests.
#
# Accepts a run name as an argument, or prompts for one.
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter test run name (to which revision will be appended): "
  set rname = $<
else
  set rname = $1
endif

#..................................................
#Append the revision number; silly humans get it wrong
set revset = `svnversion | awk -F: '{print $2}'`
if ( "$revset" == "") then
  set revset = `svnversion`
endif 

set dirname = {$rname}_r{$revset}

#.........................................
# User may specify the list of tests; if not, use the full set.
if ( "$2" == "" ) then
  set tlist = "science_cases acs_etc_cases nicmos_etc_cases stis_etc_cases wfc3_ir_imaging_78_cases wfc3_ir_spec_61_cases wfc3_uvis1_imaging_61_cases wfc3_uvis1_spec_62_cases wfc3_uvis2_imaging_18_cases wfc3_uvis2_spec_18_cases nicmos_etc_thermback_cases wfc3_ir_imaging_80_thermback wfc3_ir_spec_62_thermback acs_rn_cases nicmos_rn_cases stis_rn_cases wfc3_rn_ir1_cases invalid_rn_cases"
else
  shift 
  set tlist = "$*"
endif

#set tlist = "fewcases science_cases"
#.........................................
#irafdev
set codeplace = /data/gaudete1/dg1/laidler/ssb/checkout/pysynphot/test/commissioning
setenv PATH {$PATH}:{$codeplace}
setenv PYTHONPATH {$PYTHONPATH}:{$codeplace}

if ( ! $?PYSYN_CDBS ) then
  echo PYSYN_CDBS must be defined.... aborting.
  exit 1
endif

echo crrefer is $crrefer

echo $PYTHONPATH
python -c "import pysynphot ; print pysynphot.__file__"
python printversion.py
echo $PYSYN_CDBS
#...................................................
# Set up a test directory
mkdir -p $dirname
cd $dirname
tar -xzf /eng/ssb/syn_pysyn/testdata.tar.gz
#....................................................
foreach tname ($tlist)
  echo $tname
###  nosetests $tname >& `echo "$tname" | sed 's/.py/.log/'`
  nosetests $tname >& $tname.log
  casestats.csh $tname > $tname.stats
  set instr = `echo $tname | awk -F _ '{print $1}'`
  python $codeplace/doscalars.py $tname/testefflam efflam $instr
  python $codeplace/doscalars.py $tname/testcountrate countrate $instr
end
