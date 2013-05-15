#! /bin/csh
set inst = (acs stis nicmos)
foreach k ($inst)
   cleanup_{$k}.csh
end
