pro plothists,root

read_tabular,root+'_acs.max',1,maxdiff,nrows=100000
mmax = max(maxdiff)
plot,histogram(maxdiff,min=0.,max=mmax,bin=0.01),psym=10, title='ACS'

read_tabular,root+'_nicmos.max',1,maxdiff,nrows=100000
mmax = max(maxdiff)
plot,histogram(maxdiff,min=0.,max=mmax,bin=0.01),psym=10, title='NICMOS'

read_tabular,root+'_stis.max',1,maxdiff,nrows=100000
mmax = max(maxdiff)
plot,histogram(maxdiff,min=0.,max=mmax,bin=0.01),psym=10, title='stis'

read_tabular,root+'_wfc3.max',1,maxdiff,nrows=100000
mmax = max(maxdiff)
plot,histogram(maxdiff,min=0.,max=mmax,bin=0.01),psym=10, title='WFC3'

end
