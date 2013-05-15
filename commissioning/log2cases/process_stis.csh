#! /bin/csh
#Parse the new logfile to create the mapping
python parselog.py stisPysynphotLog_9oct.txt
#Generate from the new logfile
cd ../
python gencases.py stis_etc_cases.txt stis_etc_cases_subset.txt log2cases/stisPysynphotLog_9oct_lookup.pickle
