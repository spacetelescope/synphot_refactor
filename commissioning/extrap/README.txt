EXTRAP.PY

PURPOSE:
=======
This script was written to automatically force the endpoints of a 
synphot throughput file to zero. 

- it can safely be run on files that already meet this condition; it
  will detect that the file does not need to be changed.

- it can handle simple files (wavelength/throughput only),
  parameterized files (wavelength + many throughput) with or without
  an error column, and simple files with an error column 
  (wave, thru, error). If an error column is
  present, the error value of the extra points is set to 100.
  
- it automatically updates the version number in the filename and
  writes history into the primary header

FILES:
=====
This directory also contains one file of each known type that can be
used for testing:

hst_ota_007_syn.fits:      no change necessary
acs_hrc_win_005_syn.fits:  simple file
acs_sbc_aper_002_syn.fits: parameterized file
wfpc2_f814w_006_syn.fits:  simple file + error


Usage:
=====
- From the shell:
    python extrap.py *syn.fits

  The script will correctly handle the shell expansion of the
  filenames, and loop over all of them, printing the return value.

- From within python:
     import extrap
     extrap.run(fname,outdir='update')

  If run from within the python interpreter, an optional 'outdir'
  keyword can be supplied so that the new files will be written to
  this directory, which will be created if it does not already exist. 

  Typical use from the shell would include a loop:

     import glob
     flist=glob.glob('/some/dir/*_syn.fits')
     for fname in flist: 
        extrap.run(fname,outdir='other/dir/')


Buildtmc:
========

An extra function was added that can be used to construct a new TMC
file from an existing TMC file and a directory tree containing a
mixture of updated and non-updated files. It must be run from within
python and takes the tmcname as an argument.

  import extrap
  extrap.buildtmc('uniqname.tmc')

