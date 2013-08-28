#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
from distutils.core import setup
from distutils.extension import Extension

import numpy as np


setup(name='synphot',
      version='3.0.0.dev',
      description='Synthetic Photometry Utilities',
      requires=['numpy (>=1.5.1)', 'astropy (>=0.3)'],
      provides=['synphot'],
      author='Vicki Laidler, Matt Davis, Robert Jedrzejewski, Ivo Busko, Christopher Hanley, Pey Lian Lim',
      author_email='help@stsci.edu',
      url='http://www.github.com/spacetelescope/pysynphot',
      classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
      packages=['synphot', 'synphot.tests'],
      package_dir={'synphot': 'synphot'},
      package_data={'synphot.tests': ['data/*.fits']},
      ext_modules = [
        Extension('synphot.synphot_utils', ['synphot/src/synphot_utils.c'],
                  include_dirs=[np.get_include()])]
)
