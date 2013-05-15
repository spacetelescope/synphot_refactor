#! /bin/csh
#Create the pickled dictionary from the new file
python parselog.py acsPysynphotLog_9oct.txt
#Generate from the old logfile using the new mapping
cd ..
python gencases.py acs_etc_cases.txt acs_etc_cases_subset.txt log2cases/acsPysynphotLog_9oct_lookup.pickle

