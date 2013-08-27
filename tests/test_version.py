# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division, print_function

import pysynphot as pysyn


def test_version():
    version = pysyn.__version__
    assert(version == "3.0.0.dev")

