# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division

"""
This module handles the wavecat.dat table presently used by the
synphot countrate task (and thus the ETC) to select an appropriate wavelength
set for a given obsmode.

"""

import re
import numpy as np
import locations


class Wavetable(object):
    """
    Class to handle wavecat.dat initialization and access. (This class
    may need a better name; wavetable and waveset are awfully close.)
    Also, put the default waveset into this object with a key of NONE.

    """

    def __init__(self, fname):
        """
        Instantiate a Wavetable from a file

        """
        self.file = fname
        self.lookup = {}
        self.setlookup = {}
        fs = open(wavecat_file, mode='r')
        lines = fs.readlines()
        fs.close()

        regx = re.compile(r'\S+', re.IGNORECASE)
        for line in lines:
            if not line.startswith("#"):
                try:
                    [obm, coeff] = regx.findall(line)
                    self.lookup[obm] = coeff
                    self.setlookup[frozenset(obm.split(','))] = coeff
                except ValueError:
                    raise ValueError("Error processing line: %s" % line)


    def __getitem__(self, key):
        """
        Fairly smart lookup: if no exact match, find the most complete
        match.

        """

        ans = None
        try:
            #Try an exact match
            ans = self.lookup[key]

        except KeyError:
            ans = None
            #Try a setwise match.
            #The correct key will be a subset of the input key.
            setkey = set(key.split(','))
            candidates = []
            for k in self.setlookup:
                if k.issubset(setkey):
                    candidates.append(k)
                #We may have 1, 0, or >1 candidates.
            if len(candidates) == 1:
                ans = self.setlookup[candidates[0]]
            elif len(candidates) == 0:
                raise KeyError("%s not found in %s; candidates:%s" % (
                    setkey, self.file, str(candidates))
                )
            elif len(candidates) > 1:
                setlens = np.array([len(k) for k in candidates])
                srtlen = setlens.argsort()
                k, j = srtlen[-2:]
                if setlens[k] == setlens[j]:
                    #It's really ambiguous
                    raise ValueError("Ambiguous key %s; candidates %s" % (
                        setkey, candidates)
                    )
                else:
                    #We have a winner
                    k = candidates[srtlen[-1]]
                    ans = self.setlookup[k]
        return ans

wavecat_file = locations.wavecat
wavetable = Wavetable(wavecat_file)

