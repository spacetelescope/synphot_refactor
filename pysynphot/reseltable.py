"""
This module handles the reselcat.dat table presently used by the
synphot countrate task (and thus the ETC) to select an appropriate wavelength
set for a given obsmode.

"""
from __future__ import division, print_function

import re
import numpy as np

from . import locations


class Reseltable(object):
    """
    Class to handle Reselcat.dat initialization and access.

    Default reselset into this object with a key of NONE.

    """
    def __init__(self, fname):
        """
        Instantiate a Reseltable from a file

        """
        self.file = fname
        self.lookup = {}
        self.setlookup = {}
        fs = open(reselcat_file, mode='r')
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
            # Try an exact match
            ans = self.lookup[key]
        except KeyError:
            ans = None
            # Try a setwise match.
            # The correct key will be a subset of the input key.
            setkey = set(key.split(','))
            candidates = []
            for k in self.setlookup:
                if k.issubset(setkey):
                    candidates.append(k)
            # We may have 1, 0, or >1 candidates.
            if len(candidates) == 1:
                ans = self.setlookup[candidates[0]]

            elif len(candidates) == 0:
                raise KeyError("%s not found in %s; candidates:%s" %
                               (setkey, self.file, str(candidates)))

            elif len(candidates) > 1:
                setlens = np.array([len(k) for k in candidates])
                srtlen = setlens.argsort()
                k, j = srtlen[-2:]
                if setlens[k] == setlens[j]:
                    # It's really ambiguous
                    raise ValueError("Ambiguous key %s; candidates %s" %
                                     (setkey, candidates))
                else:
                    # We have a winner
                    k = candidates[srtlen[-1]]
                    ans = self.setlookup[k]
        return ans

reselcat_file = locations.reselcat
reseltable = Reseltable(reselcat_file)

