# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synphot configurable items.

The default configuration heavily depends on STScI CDBS structure
but it can be easily re-configured as the user wishes via
`astropy.config`.

"""
from __future__ import absolute_import, division, print_function, unicode_literals

# TODO: Use https://github.com/astropy/astropy/pull/2094 instead.
# ASTROPY
from astropy.config.configuration import ConfigurationItem


__all__ = ['VEGA_FILE', 'LMC30DOR_FILE', 'LMCAVG_FILE', 'MWAVG_FILE',
           'MWDENSE_FILE', 'MWRV21_FILE', 'MWRV40_FILE', 'SMCBAR_FILE',
           'XGAL_FILE', 'BESSEL_H_FILE', 'BESSEL_J_FILE', 'BESSEL_K_FILE',
           'COUSINS_I_FILE', 'COUSINS_R_FILE', 'JOHNSON_B_FILE',
           'JOHNSON_I_FILE', 'JOHNSON_J_FILE', 'JOHNSON_K_FILE',
           'JOHNSON_R_FILE', 'JOHNSON_U_FILE', 'JOHNSON_V_FILE']

# STANDARD STARS
VEGA_FILE = ConfigurationItem(
    'vega_file',
    'ftp://ftp.stsci.edu/cdbs/calspec/alpha_lyr_stis_007.fits',
    'Vega')

# REDDENING/EXTINCTION LAWS
LMC30DOR_FILE = ConfigurationItem(
    'lmc30dor_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/lmc_30dorshell_001.fits',
    'Gordon et al. 2003, ApJ, 594, 279; R_V = 2.76')
LMCAVG_FILE = ConfigurationItem(
    'lmcavg_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/lmc_diffuse_001.fits',
    'Gordon et al. 2003, ApJ, 594, 279; R_V = 3.41')
MWAVG_FILE = ConfigurationItem(
    'mwavg_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/milkyway_diffuse_001.fits',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 3.10')
MWDENSE_FILE = ConfigurationItem(
    'mwdense_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/milkyway_dense_001.fits',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 5.00')
MWRV21_FILE = ConfigurationItem(
    'mwrv21_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/milkyway_rv21_001.fits',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 2.1')
MWRV40_FILE = ConfigurationItem(
    'mwrv40_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/milkyway_rv4_001.fits',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 4.0')
SMCBAR_FILE = ConfigurationItem(
    'smcbar_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/smc_bar_001.fits',
    'Gordon et al. 2003, ApJ, 594, 279; R_V=2.74')
XGAL_FILE = ConfigurationItem(
    'xgal_file',
    'ftp://ftp.stsci.edu/cdbs/extinction/xgal_starburst_001.fits',
    'Calzetti et al. 2000, ApJ, 533, 682')

# COMMON FILTER BANDPASS
BESSEL_H_FILE = ConfigurationItem(
    'bessel_h_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/bessell_h_004_syn.fits',
    'Bessel H')
BESSEL_J_FILE = ConfigurationItem(
    'bessel_j_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/bessell_j_003_syn.fits',
    'Bessel J')
BESSEL_K_FILE = ConfigurationItem(
    'bessel_k_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/bessell_k_003_syn.fits',
    'Bessel K')
COUSINS_I_FILE = ConfigurationItem(
    'cousins_i_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/cousins_i_004_syn.fits',
    'Cousins I')
COUSINS_R_FILE = ConfigurationItem(
    'cousins_r_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/cousins_r_004_syn.fits',
    'Cousins R')
JOHNSON_B_FILE = ConfigurationItem(
    'johnson_b_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_b_004_syn.fits',
    'Johnson B')
JOHNSON_I_FILE = ConfigurationItem(
    'johnson_i_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_i_003_syn.fits',
    'Johnson I')
JOHNSON_J_FILE = ConfigurationItem(
    'johnson_j_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_j_003_syn.fits',
    'Johnson J')
JOHNSON_K_FILE = ConfigurationItem(
    'johnson_k_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_k_003_syn.fits',
    'Johnson K')
JOHNSON_R_FILE = ConfigurationItem(
    'johnson_r_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_r_003_syn.fits',
    'Johnson R')
JOHNSON_U_FILE = ConfigurationItem(
    'johnson_u_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_u_004_syn.fits',
    'Johnson U')
JOHNSON_V_FILE = ConfigurationItem(
    'johnson_v_file',
    'ftp://ftp.stsci.edu/cdbs/comp/nonhst/johnson_v_004_syn.fits',
    'Johnson V')
