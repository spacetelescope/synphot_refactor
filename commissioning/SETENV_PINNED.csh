#! /bin/csh
setenv PYSYN_CDBS /eng/ssb/syn_pysyn/cdbs_pinned/
setenv crrefer /eng/ssb/syn_pysyn/cdbs_pinned/
setenv PYTHONPATH .:/usr/stsci/pyssgdev/2.5.1/:/user/laidler/pyinstall/lib/:/data/gaudete1/dg1/laidler/code/mypython:/data/gaudete1/dg1/laidler/ssb/checkout/pysynphot/test/commissioning:/data/gaudete1/dg2/laidler/testplay/nose/
alias nosetests /data/gaudete1/dg2/laidler/testplay/nose/nosetests
