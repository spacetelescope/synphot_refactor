#! /bin/csh 
#---------------------
#-x -- turn on this flag to make it echo everything
# Grep -I through the log files produced by a test run to count up
# passes, failures, and unique obsmode/spectrum combinations that
# went into each of them.
#
# First get the prefix associated with the set of tests.
# If none is supplied, prompt for one.
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter test run prefix: "
  set idstring = $<
else
  set idstring = $1
endif
#
#Collect stats from the full set
set allfiles = `find $idstring -name "*.log" `
set ntests = `echo $allfiles | wc -w`
set ncases = `find $idstring -name "*.log" | awk -F / '{print $3}' | sort -u | wc -l`

set nobstot=`grep da_obs $allfiles | awk '{print $2}' | sort -u | wc -l`
set nspectot=`grep da_spec $allfiles | awk '{print $2}' | sort -u | wc -l`
echo Test statistics for "$idstring*.log":
echo $ncases test cases
echo $ntests total tests
echo $nobstot unique obsmodes
echo $nspectot unique spectra
echo ================================================
#
chdir $idstring
# Work with one type of test at a time
foreach tname (`ls`)
  chdir $tname 
#.....**Warning, not robust against other junk in directory
# Count the total number of tests
  set ntests = `ls -1 *.log | wc -l`
  echo $tname : $ntests total tests
# Count the errors
  set nerr = ` grep -l Status=E *.log | wc -l`
  echo Error cases: $nerr
# Count the number that failed
  set ffiles=`grep -l Status=F *.log`
  set nfailed = `grep -i -l Status=F *.log | wc -l` 
  echo Failed cases: $nfailed
  if ($nfailed > 0) then
    set nobs = `grep -i da_obsmode $ffiles | awk '{print $2}' | sort -u | wc -l`
    set nspec = `grep -i da_spectrum $ffiles | awk '{print $2}' | sort -u | wc -l`
  else
    set nobs = 0
    set nspec = 0
  endif

# Count the number of extreme failures
  set efiles=`grep -l ra_extreme *.log`
  set nextreme = `grep -i -l ra_extreme *.log | wc -l` 
  echo Extreme failures: $nextreme
  if ($nextreme > 0) then
    set nobs_e = `grep -i da_obsmode $efiles | awk '{print $2}' | sort -u | wc -l`  
    set nspec_e = `grep -i da_spectrum $efiles | awk '{print $2}' | sort -u | wc -l`
  else
    set nobs_e = 0
    set nspec_e = 0
  endif

  echo Unique obsmodes: $nobs_e extreme / $nobs all failures / $nobstot total

  echo -n Unique spectra : $nspec_e extreme / $nspec all failures / $nspectot total

  echo 
  echo -------------------------------------------------------
  echo
#Go back up
 
  chdir ..

  end
chdir ..
