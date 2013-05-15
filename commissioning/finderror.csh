#! /bin/csh 
# Find the unique errors in all the log files.
unalias grep
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter logfile name or wildcard pattern: "
  set errlog = $<
else
  set errlog = $1
endif
#

cat $errlog | grep -i "^.*error[ :]" | sort -u | grep -v AssertionError | grep -v "ERROR: test" 
