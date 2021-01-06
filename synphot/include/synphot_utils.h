#ifndef SYNPHOT_UTILS__H
#define SYHPHOT_UTILS__H

#define doc_calcbinflux \
"\
\n\
\n\
\n\
calcbinflux(len_binwave, i_beg, i_end, avflux, deltaw)\n\
\n\
Sum over each bin.\n\
\n\
Parameters\n\
----------\n\
len_binwave : int\n\
    Number of wavelength bin centers.\n\
\n\
i_beg, i_end : array-like\n\
    Locations of bin edges in ``deltaw``.\n\
\n\
avflux : array-like\n\
    Average flux associated with ``deltaw``.\n\
\n\
deltaw : array-like\n\
    Delta of merge wavelengths (native + centers + edges).\n\
    Values are in ascending order.\n\
\n\
Returns\n\
-------\n\
binflux : array-like\n\
    Integrated flux associated with given bins in ascending order.\n\
\n\
intwave : array-like\n\
    Integrated delta wavelength associated with ``binflux``.\n\
\n\
\0"

#endif
