# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synphot configurable items.

The default configuration heavily depends on STScI CDBS structure
but it can be easily re-configured as the user wishes via
`astropy.config`.

"""
from __future__ import absolute_import, division, print_function

# ASTROPY
from astropy.config import ConfigNamespace, ConfigItem

__all__ = ['conf']


class Conf(ConfigNamespace):
    """Configuration parameters."""

    # TODO: Add more options here in the future
    default_integrator = ConfigItem(
        ['trapezoid'],
        'Default integrator to use when analytical integration is unavailable')

    # STANDARD STARS
    vega_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/calspec/alpha_lyr_stis_008.fits', 'Vega')

    # REDDENING/EXTINCTION LAWS
    lmc30dor_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/lmc_30dorshell_001.fits',
        'Gordon et al. 2003, ApJ, 594, 279; R_V = 2.76')
    lmcavg_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/lmc_diffuse_001.fits',
        'Gordon et al. 2003, ApJ, 594, 279; R_V = 3.41')
    mwavg_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/milkyway_diffuse_001.fits',
        'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 3.10')
    mwdense_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/milkyway_dense_001.fits',
        'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 5.00')
    mwrv21_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/milkyway_rv21_001.fits',
        'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 2.1')
    mwrv40_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/milkyway_rv4_001.fits',
        'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 4.0')
    smcbar_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/smc_bar_001.fits',
        'Gordon et al. 2003, ApJ, 594, 279; R_V=2.74')
    xgal_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/extinction/xgal_starburst_001.fits',
        'Calzetti et al. 2000, ApJ, 533, 682')

    # COMMON FILTER BANDPASS
    bessel_h_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/bessell_h_004_syn.fits',
        'Bessel H')
    bessel_j_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/bessell_j_003_syn.fits',
        'Bessel J')
    bessel_k_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/bessell_k_003_syn.fits',
        'Bessel K')
    cousins_i_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/cousins_i_004_syn.fits',
        'Cousins I')
    cousins_r_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/cousins_r_004_syn.fits',
        'Cousins R')
    johnson_b_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_b_004_syn.fits',
        'Johnson B')
    johnson_i_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_i_003_syn.fits',
        'Johnson I')
    johnson_j_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_j_003_syn.fits',
        'Johnson J')
    johnson_k_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_k_003_syn.fits',
        'Johnson K')
    johnson_r_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_r_003_syn.fits',
        'Johnson R')
    johnson_u_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_u_004_syn.fits',
        'Johnson U')
    johnson_v_file = ConfigItem(
        'http://ssb.stsci.edu/cdbs/comp/nonhst/johnson_v_004_syn.fits',
        'Johnson V')


conf = Conf()
