#! /bin/csh 

#Parse the new logfiles to create the lookups
python parselog.py wfc3UVIS1ImagingPysynphotLog.txt
python parselog.py wfc3UVIS2ImagingPysynphotLog.txt
python parselog.py wfc3UVIS1SpecPysynphotLog.txt
python parselog.py wfc3UVIS2SpecPysynphotLog.txt
python parselog.py wfc3IRImagingPysynphotLog.txt
python parselog.py wfc3IRSpecPysynphotLog.txt

#Then regenerate the cases.
cd ../
echo "### WFC3 UVIS1 Imaging"
python gencases.py wfc3_uvis1_imaging_61_cases.txt wfc3_uvis1_imaging_61_cases_subset.txt log2cases/wfc3UVIS1ImagingPysynphotLog_lookup.pickle
echo "# "
echo "### WFC3 UVIS2 Imaging"
python gencases.py wfc3_uvis2_imaging_18_cases.txt wfc3_uvis2_imaging_18_cases_subset.txt log2cases/wfc3UVIS2ImagingPysynphotLog_lookup.pickle
echo "# "
echo "### WFC3 UVIS1 Spec"
python gencases.py wfc3_uvis1_spec_62_cases.txt wfc3_uvis1_spec_62_cases_subset.txt log2cases/wfc3UVIS1SpecPysynphotLog_lookup.pickle
echo "# "
echo "### WFC3 UVIS2 Spec"
python gencases.py wfc3_uvis2_spec_18_cases.txt wfc3_uvis2_spec_18_cases_subset.txt log2cases/wfc3UVIS2SpecPysynphotLog_lookup.pickle
echo "# "
echo "### WFC3 IR Imaging"
python gencases.py wfc3_ir_imaging_78_cases.txt wfc3_ir_imaging_78_cases_subset.txt log2cases/wfc3IRImagingPysynphotLog_lookup.pickle
echo "# "
echo "#######  wfc3_ir_imaging_thermback *********"
python gencases.py wfc3_ir_imaging_80_thermback.txt wfc3_ir_imaging_80_thermback_subset.txt log2cases/wfc3IRImagingPysynphotLog_lookup.pickle
echo "# "
echo "### WFC3 IR Spec"
python gencases.py wfc3_ir_spec_61_cases.txt wfc3_ir_spec_61_cases_subset.txt log2cases/wfc3IRSpecPysynphotLog_lookup.pickle
echo "# "
echo "#######  wfc3_ir_spec_thermback *********"
python gencases.py wfc3_ir_spec_62_thermback.txt /dev/null log2cases/wfc3IRSpecPysynphotLog_lookup.pickle

