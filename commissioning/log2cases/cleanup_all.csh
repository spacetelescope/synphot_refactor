#! /bin/csh
set inst = (acs stis nicmos wfc3)
foreach k ($inst)
   cleanup_{$k}.csh
end
