# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synphot configurable items.

The default configuration heavily depends on STScI CDBS structure
but it can be easily re-configured as the user wishes via
`astropy.config`.

:func:`set_files` set the default filenames to the latest version
available based on their respective templates.

"""
from __future__ import absolute_import, division, print_function, unicode_literals

# STDLIB
import os

# ASTROPY
from astropy.config.configuration import ConfigurationItem

# LOCAL
from . import io


__all__ = ['STDSTAR_DIR', 'VEGA_FILE', 'EXTINCTION_DIR', 'LMC30DOR_FILE',
           'LMCAVG_FILE', 'MWAVG_FILE', 'MWDENSE_FILE', 'MWRV21_FILE',
           'MWRV40_FILE', 'SMCBAR_FILE', 'XGAL_FILE', 'PASSBAND_DIR',
           'BESSEL_H_FILE', 'BESSEL_J_FILE', 'BESSEL_K_FILE', 'set_files']

# STANDARD STARS
STDSTAR_DIR = ConfigurationItem(
    'stdstar_dir', 'ftp://ftp.stsci.edu/cdbs/current_calspec/',
    'Location of standard star spectra.')
VEGA_FILE = ConfigurationItem('vega_file', '', 'Vega')

# REDDENING/EXTINCTION LAWS
EXTINCTION_DIR = ConfigurationItem(
    'extinction_dir', 'ftp://ftp.stsci.edu/cdbs/extinction/',
    'Location of extinction files.')
LMC30DOR_FILE = ConfigurationItem(
    'lmc30dor_file', '', 'Gordon et al. 2003, ApJ, 594, 279; R_V = 2.76')
LMCAVG_FILE = ConfigurationItem(
    'lmcavg_file', '', 'Gordon et al. 2003, ApJ, 594, 279; R_V = 3.41')
MWAVG_FILE = ConfigurationItem(
    'mwavg_file', '',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 3.10')
MWDENSE_FILE = ConfigurationItem(
    'mwdense_file', '',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 5.00')
MWRV21_FILE = ConfigurationItem(
    'mwrv21_file', '',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 2.1')
MWRV40_FILE = ConfigurationItem(
    'mwrv40_file', '',
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 4.0')
SMCBAR_FILE = ConfigurationItem(
    'smcbar_file', '', 'Gordon et al. 2003, ApJ, 594, 279; R_V=2.74')
XGAL_FILE = ConfigurationItem(
    'xgal_file', '', 'Calzetti et al. 2000, ApJ, 533, 682')

# COMMON FILTER PASSBANDS
PASSBAND_DIR = ConfigurationItem(
    'passband_dir', 'ftp://ftp.stsci.edu/cdbs/comp/nonhst/',
    'Location of passband files.')
BESSEL_H_FILE = ConfigurationItem('bessel_h_file', '', 'Bessel H')
BESSEL_J_FILE = ConfigurationItem('bessel_j_file', '', 'Bessel J')
BESSEL_K_FILE = ConfigurationItem('bessel_k_file', '', 'Bessel K')
COUSINS_I_FILE = ConfigurationItem('cousins_i_file', '', 'Cousins I')
COUSINS_R_FILE = ConfigurationItem('cousins_r_file', '', 'Cousins R')
JOHNSON_B_FILE = ConfigurationItem('johnson_b_file', '', 'Johnson B')
JOHNSON_I_FILE = ConfigurationItem('johnson_i_file', '', 'Johnson I')
JOHNSON_J_FILE = ConfigurationItem('johnson_j_file', '', 'Johnson J')
JOHNSON_K_FILE = ConfigurationItem('johnson_k_file', '', 'Johnson K')
JOHNSON_R_FILE = ConfigurationItem('johnson_r_file', '', 'Johnson R')
JOHNSON_U_FILE = ConfigurationItem('johnson_u_file', '', 'Johnson U')
JOHNSON_V_FILE = ConfigurationItem('johnson_v_file', '', 'Johnson V')


def set_files():
    """Convenience function to update paths of configurable
    filenames. Useful for when these files are installed locally
    (see `stsynphot.config`).

    """
    std_dir = STDSTAR_DIR()
    VEGA_FILE.set(io.get_latest_file(
        os.path.join(std_dir, 'alpha_lyr_stis_*.fits')))

    ext_dir = EXTINCTION_DIR()
    LMC30DOR_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'lmc_30dorshell_*.fits')))
    LMCAVG_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'lmc_diffuse_*.fits')))
    MWAVG_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'milkyway_diffuse_*.fits')))
    MWDENSE_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'milkyway_dense_*.fits')))
    MWRV21_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'milkyway_rv21_*.fits')))
    MWRV40_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'milkyway_rv4_*.fits')))
    SMCBAR_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'smc_bar_*.fits')))
    XGAL_FILE.set(io.get_latest_file(
        os.path.join(ext_dir, 'xgal_starburst_*.fits')))

    pb_dir = PASSBAND_DIR()
    BESSEL_H_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'bessell_h_*_syn.fits')))
    BESSEL_J_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'bessell_j_*_syn.fits')))
    BESSEL_K_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'bessell_k_*_syn.fits')))
    COUSINS_I_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'cousins_i_*_syn.fits')))
    COUSINS_R_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'cousins_r_*_syn.fits')))
    JOHNSON_B_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_b_*_syn.fits')))
    JOHNSON_I_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_i_*_syn.fits')))
    JOHNSON_J_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_j_*_syn.fits')))
    JOHNSON_K_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_k_*_syn.fits')))
    JOHNSON_R_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_r_*_syn.fits')))
    JOHNSON_U_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_u_*_syn.fits')))
    JOHNSON_V_FILE.set(io.get_latest_file(
        os.path.join(pb_dir, 'johnson_v_*_syn.fits')))


# Set default filenames
set_files()
