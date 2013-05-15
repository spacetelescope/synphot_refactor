#! /bin/csh
# Parse the new logfile to produce the lookup
python parselog.py nicmosPysynphotLog_13oct.txt 
echo "*******  nicmos_etc_cases  *******"
cd ../
python gencases.py nicmos_etc_cases.txt nicmos_etc_cases_subset.txt log2cases/nicmosPysynphotLog_13oct_lookup.pickle

# Now the thermback cases. 
echo "# "
echo "#####  nicmos_etc_thermback_cases  *********"
python gencases.py nicmos_etc_thermback_cases.txt nicmos_etc_cases_subset.txt log2cases/nicmosPysynphotLog_13oct_lookup.pickle

