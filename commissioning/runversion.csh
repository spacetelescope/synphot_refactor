#! /bin/csh -x

# Check out, build, and test a specific version of pysynphot against
# the syn_pysyn test suite.
set root = /data/gaudete1/dg2/pysyn_version_compare/
setenv PYSYN_CDBS /eng/ssb/syn_pysyn/cdbs_pinned/
setenv crrefer $PYSYN_CDBS

if $1 == '' then
  echo "You must specify a revision"
  exit
else
  set revset = $1
  setenv PYSYN_BUILDDIR $root/install/$revset
endif
#make directory
mkdir $revset
mkdir install/$revset

# set path: stick pyssg on the end so we don't lose nose
setenv PYTHONPATH ${PYSYN_BUILDDIR}/lib/python/:${root}/${revset}/pysynphot/commissioning/:/usr/stsci/pyssgdev/2.5.1:/usr/stsci/pyssg/2.5.1/

#check out
cd $revset
svn checkout https://www.stsci.edu/svn/ssb/astrolib/trunk/pysynphot@{$revset}

#build
cd pysynphot
python setup.py install --home=$PYSYN_BUILDDIR
#
#
# take the path stuff OUT of runset
cd commissioning
grep -v codeplace runset.csh > runset_clean.csh
chmod +x runset_clean.csh
#
# Now run the tests
runset_clean.csh $root/syn_pysyn/ >& ${root}runset_clean_r$revset.log &
