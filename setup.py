#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os
import sysconfig

import numpy as np
from setuptools import Extension, setup

GIL_ENABLED_PYTHON = sysconfig.get_config_var("Py_GIL_DISABLED") != 1

cfg = {
    "sources": [os.path.join("synphot", "src", "synphot_utils.c")],
    "include_dirs": [np.get_include(), os.path.join("synphot", "include")],
    "define_macros": [("NUMPY", "1")],
    "libraries": [],
    "extra_compile_args": [],
    "py_limited_api": GIL_ENABLED_PYTHON,
}

if GIL_ENABLED_PYTHON:
    cfg["define_macros"].append(("Py_LIMITED_API", "0x030C0000"))  # PY_VERSION_HEX for 3.12

SETUPTOOLS_OPTIONS = {}
if GIL_ENABLED_PYTHON:
    SETUPTOOLS_OPTIONS["bdist_wheel"] = {"py_limited_api": "cp312"}

setup(ext_modules=[Extension("synphot.synphot_utils", **cfg)], options=SETUPTOOLS_OPTIONS)
