This directory contains utility scripts that were used to modify WFC3
test cases from Bruzual to Pickles models.

Only the replace.csh script should be necessary to apply these
changes again. The files in its foreach loop might need to be updated
to select only the files of interest. 

The procedure used to develop this script is as follows:


Substitutions were made on the basis of spectral type described in the
bzspectype.ascii table (taken from /grp/hst/cdbs/grid/bz77). In some
cases, exact matches to the spectral
type were available in the pickles_spectype.txt table (extracted from
the /grp/hst/cdbs/grid/pickles/AA_README file).

When this was not the case, a list of candidates that matched the
basic spectral type (OBAFGKM) were extracted and printed out for
review (candidates.txt). Howard Bushouse selected one of the
candidates in each case, and this hand-selected substitution was
recorded in the dictionary 'subs' in match.py.

This python module contains the following functions:

run(): construct and return dictionaries of bz and pickles
gencand(nomatch,pickles): generate the candidate review list
replace(bz,pickles): perform the matching and write a file containing
                    replacement commands for sed (replace.txt)

The shell script replace.csh was then hand-edited from replace.txt to
include a loop over the relevant filenames, and run to make the
filename substitutions.

An additional loop was run interactively in the shell to replace the
grid/bz77 directory string with the grid/pickles/dat_uvk/ string.
The replace.csh was subsequently edited to include this step.


V. Laidler, 22-23 Sep 2008


