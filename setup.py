#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from setuptools import setup


def get_extensions():
    import os
    from collections import defaultdict

    import numpy
    from setuptools import Extension

    cfg = defaultdict(list)
    cfg['include_dirs'].extend([
        numpy.get_include(),
        os.path.join('synphot', 'include')])
    cfg['sources'] = [
        os.path.join('synphot', 'src', 'synphot_utils.c')]
    cfg = dict((str(key), val) for key, val in cfg.items())

    return [Extension('synphot.synphot_utils', **cfg)]


setup(ext_modules=get_extensions())
