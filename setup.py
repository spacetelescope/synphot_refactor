#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os
import sys
from setuptools import setup, Extension


def get_extensions():
    from collections import defaultdict
    import numpy

    cfg = defaultdict(list)
    cfg['include_dirs'].extend([
        numpy.get_include(),
        os.path.join('synphot', 'include')])
    cfg['sources'] = [
        os.path.join('synphot', 'src', 'synphot_utils.c')]
    cfg = dict((str(key), val) for key, val in cfg.items())

    return [Extension('synphot.synphot_utils', **cfg)]


TEST_HELP = """
Note: running tests is no longer done using 'python setup.py test'. Instead
you will need to run:

    pip install -e .
    pytest

For more information, see:

  https://docs.astropy.org/en/latest/development/testguide.html#running-tests
"""

if 'test' in sys.argv:
    print(TEST_HELP)
    sys.exit(1)

DOCS_HELP = """
Note: building the documentation is no longer done using
'python setup.py build_docs'. Instead you will need to run:

    cd docs
    make html

For more information, see:

  https://docs.astropy.org/en/latest/install.html#builddocs
"""

if 'build_docs' in sys.argv or 'build_sphinx' in sys.argv:
    print(DOCS_HELP)
    sys.exit(1)

# Note that requires and provides should not be included in the call to
# ``setup``, since these are now deprecated. See this link for more details:
# https://groups.google.com/forum/#!topic/astropy-dev/urYO8ckB2uM

setup(use_scm_version={'write_to': 'synphot/version.py'},
      ext_modules=get_extensions())
