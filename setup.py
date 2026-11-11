#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os

import numpy as np
from setuptools import Extension, setup

cfg = {
    "sources": [os.path.join("synphot", "src", "synphot_utils.c")],
    "include_dirs": [np.get_include(), os.path.join("synphot", "include")],
    "define_macros": [("NUMPY", "1")],
    "libraries": [],
    "extra_compile_args": [],
}

setup(ext_modules=[Extension("synphot.synphot_utils", **cfg)])
