#! /bin/csh
set d=/eng/ssb
if ( ! -d $d ) then
 set prefix = $HOME/CentralStore/
else
 set prefix = /
endif


#Define path containing tests
setenv PYTHONPATH $prefix/user/laidler/syn_pysyn/:{$PYTHONPATH}
setenv PYSYN_CDBS $prefix/grp/hst/cdbs/
#go to place
cd $prefix/eng/ssb/syn_pysyn/platform
#set up subdir for platform tests
set h = `hostname`
set h2 = `basename $h .stsci.edu`
mkdir $h2

#go there & run the test
cd $h2
nosetests platform_cases >& $h2.log
