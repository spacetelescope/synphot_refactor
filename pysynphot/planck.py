# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division
## Automatically adapted for numpy.numarray Mar 05, 2007 by

import numpy as np


H  = 6.6262E-27                # Planck's constant in cgs units
HS = 6.6262E-34                # Planck's constant in standard units
C  = 2.997925E+8               # speed of light in standard units
K  = 1.38062E-23               # Boltzmann constant in standard units

C1 = 2.0 * HS * C * C          # Power * unit area / steradian
C2 = HS * C / K

F = 2.3504386381829069E-25     # convert from m^2/steradian/m to
                               # cm^2/sq.arcsec/A (see below)

LOWER = 1.0E-4                 # taken from synphot's bbfunc.
UPPER = 85.


def bbfunc(wave, temperature):
    ''' Planck function in photlam.
    wavelength in Angstrom, temperature in Kelvin.
    Adapted from bbfunc in synphot.
    '''
    x = wave * temperature

    mask = np.where(x > 0.0, 1, 0)
    x = np.where(mask==1, 1.43883E8 / x, 0.0)

    factor = np.zeros(wave.shape, dtype=np.float64)

    mask1 = np.where(x < LOWER, 0, 1)
    factor = np.where(mask1 == 0, 2.0 / (x * (x + 2.0)), factor)

    mask2 = np.where(x < UPPER, 1, 0)
    mask = mask1 * mask2
    factor = np.where(mask == 1, 1.0 / (np.exp(x) - 1.0), factor)

    x = x * temperature / 1.95722E5
    x = factor * x * x * x

    return x / (H * wave)     # cgs -> photlam conversion



def llam_SI(wave, temperature):
    ''' Planck function in standard units.
    wavelength in meters, temperature in Kelvin.
    Adapted from Anand's spp code in synphot.
    '''
    exponent = C2 / (wave * temperature)

    result = np.zeros(wave.shape, dtype=np.float64)

    mask1 = np.where(exponent <= LOWER, 0, 1)
    result = np.where(mask1==0, (2.0 * C1 * (wave**-5.0)) / (exponent * (exponent + 2.0)), result)

    mask2 = np.where(exponent <= UPPER, 1, 0)
    mask = mask1 * mask2
    exponent = np.where(mask2==1, exponent, UPPER)
    expfactor = np.exp(exponent)
    result = np.where(mask==1, (C1 * (wave**-5.0) / (expfactor - 1.0)), result)

    return result


def bb_photlam_arcsec(wave, temperature):
    ''' Planck function in photlam / square arcsec.
    wavelength in Angstrom, temperature in Kelvin.
    Translated from Anand's spp code in synphot.
    '''
    lam = wave * 1.0E-10    # Angstrom -> meter

    return F * llam_SI(lam, temperature) / (HS * C / lam)




#  Anand's original comments for the F factor:
#
#       >>> af = 0.01 * 0.01    # per m^2  -->  per cm^2
#       >>> af
#       0.0001
#       >>> sf = 206265.0 * 206265.0
#       >>> sf = 1/sf
#       >>> sf                  # per sr  -->  per sqarcsec
#       2.3504386381829067e-11
#       >>> af * sf
#       2.3504386381829069e-15
#       >>> af * sf * 1.0e-10   # per m  -->  per Angstrom
#       2.3504386381829069e-25
#
