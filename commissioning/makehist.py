import numpy as N
from pylab import *
import pylab
import pickle


#Load the data extracted from the database
f=open('countrate_discrep.pickle')
d2=pickle.load(f)

#oops, we sucked in some testefflam cases
d = dict()
for k in d2:
    if 'testcountrate' in k:
        d[k] = d2[k]

f.close()
f=open('countrate_discrep.pickle','w')
pickle.dump(d,f)
f.close()


#Break it up by instrument
acs=N.array([d[k] for k in d if 'acs' in k])
acsid = N.array([k for k in d if 'acs' in k])
nicmos=N.array([d[k] for k in d if 'nicmos' in k])
stis=N.array([d[k] for k in d if 'stis' in k])
wfc3=N.array([d[k] for k in d if 'wfc3' in k])
ilist=['acs','nicmos','stis','wfc3']


#Make the histograms, with a bin width of half a percent
clf()
bar_width=.001
for i,x in enumerate((acs,nicmos,stis,wfc3)):
    subplot(221+i)
    bins = N.arange(min(x),max(x)+bar_width,bar_width)          
    a,b,c = pylab.hist(x, bins)
    xlim(-0.15,0.15)
    ylim(0,40)
    ylabel('clipped at 40')
    legend([ilist[i]])
    xlabel('(min,max) = %g, %g'%(x.min(),x.max()))
    if i == 0:
        title('countrate: (syn-pysyn)/syn')

savefig('countrate.png')

#Zoom in both x and y
for i in range(4):
    subplot(221+i)
    xlim(-0.03,0.03)
    ylim(0,40)
    ylabel('clipped at 40')
    grid()

savefig('countrate_zoomed.png')
