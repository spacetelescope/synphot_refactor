# Late in the process, it was discovered that a number of these
# test cases provide only partial overlap between the spectrum and
# bandpass. For some of these, the instrument teams determined that
# the correct thing to do was to emulate the behavior that the ETC will
# use, ie, force the Observation to be simulated anyway, with the 
# force='taper' behavior.
#
# To support this, a new countrateOverlapCase class was defined, and
# the relevant subset of cases must be redefined to subclass from this
# new class.
#
# This script modifies the relevant .py file in place to apply these
# changes.
#
# The input filename is hardcoded as apply_overlap_input.txt. This
# file, and all relevant .py files, must be present in the working 
# directory.

import os, stat
import re

pat = "sed -i '/%s/ s:%s):%s):' %s.py \n"
cshname='apply_overlap.csh'
f=open('apply_overlap_input.txt')
out=open(cshname,'w')
out.write('#! /bin/csh \n')
x=re.compile('[0-9]')


for line in f:
    fname,cname=line.strip().split()
    ctype=re.split(x,cname)[0]
    cmd=pat%(cname,ctype,ctype.replace('Case','OverlapCase'),fname)
    out.write(cmd)
out.close()

#Fix the permissions

os.chmod(cshname,stat.S_IRWXU)
retstat=os.spawnl(os.P_WAIT,cshname)
exit(retstat)
