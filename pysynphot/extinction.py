from __future__ import division
import string
import numpy as N
import spectrum
import units
import refs

_seatonx = N.array([0.,  1.0, 1.1, 1.2, 1.3, 1.4, 1.5, \
                                1.6, 1.7, 1.8, 1.9, 2.0, 2.1, \
                                2.2, 2.3, 2.4, 2.5, 2.6, 2.7])
_seatone = N.array([0., 1.36, 1.64, 1.84, 2.04, 2.24, 2.44, \
                               2.66, 2.88, 3.14, 3.36, 3.56, 3.77, \
                               3.96, 4.15, 4.26, 4.40, 4.52, 4.64])

_lmcx = N.array([0.00, 0.29, 0.45, 0.80, 1.11, 1.43, 1.83])
_lmce = N.array([0.00, 0.16, 0.38, 0.87, 1.50, 2.32, 3.1])


#Coefficients taken from Prevot et al, 1984, out to 1/lambda=7.84.
#Additional coefficient & value to extrapolate to 1000 Angstroms,
#and the value of R =3.1 necessary to return A_lambda/E(B-V) as all the
#other extinction functions do, were provided by Scott Friedman
#-- see ticket # 63.
_smcx = N.array([ 0.00,  0.29,  0.45,  0.80,  1.11,  1.43,  1.82,  \
                         2.35,  2.70,  3.22,  3.34,  3.46,  3.60,  3.75,  \
                         3.92,  4.09,  4.28,  4.50,  4.73,  5.00,  5.24,  \
                         5.38,  5.52,  5.70,  5.88,  6.07,  6.27,  6.48,  \
                         6.72,  6.98,  7.23,  7.52,  7.84, 10])

_smce = N.array([-3.10, -2.94, -2.72, -2.23, -1.60, -0.78,  0.00,  \
                         1.00,  1.67,  2.29,  2.65,  3.00,  3.15,  3.49,  \
                         3.91,  4.24,  4.53,  5.30,  5.85,  6.38,  6.76,  \
                         6.90,  7.17,  7.71,  8.01,  8.49,  9.06,  9.28,  \
                         9.84, 10.80, 11.51, 12.52, 13.54, 20.64]) + 3.1


def _buildDefaultWaveset():
    wave = refs._default_waveset.copy()[::10]

    result = N.empty(shape=[wave.shape[0]+1,],dtype=N.float64)

    result[0:-1] = wave
    result[-1] = refs._default_waveset[-1]

    return 10000.0 / result     # convert to 1/micron

def _interp(xdata, x, y):
    xx = xdata[::-1]     # xdata is arranged in descending order
    xind = N.searchsorted(x, xx)-1
    xind = N.clip(xind, 0, x.size-2)
    xfract = (xx - x[xind]) / (x[xind+1] - x[xind])
    xfract = N.clip(xfract, 0.0, 1.0)
    result =  y[xind] + xfract * (y[xind+1] - y[xind])
    return result[::-1]

def _computeSeaton(x):
    result = _seatone[1] * x * x

    mask = N.where(x > 1.0, 1, 0) * N.where(x <= 2.7, 1, 0)
    result = N.where(mask == 1, \
             _interp(x, _seatonx, _seatone), result)

    mask = N.where(x > 2.7, 1, 0) * N.where(x <= 3.65, 1, 0)
    result = N.where(mask == 1, \
             1.56 + 1.048 * x + 1.01 / ((x-4.6)*(x-4.6) + 0.28), result)

    mask = N.where(x > 3.65, 1, 0) * N.where(x <= 7.14, 1, 0)
    result = N.where(mask == 1, \
             2.29 + 0.848 * x + 1.01 / ((x-4.6)*(x-4.6) + 0.28), result)

    result = N.where(x > 7.14, \
             16.17 + x * (-3.20 + 0.2975 * x), result)

    return result

def _computeLMC(x):
    result = N.zeros(x.shape, dtype=N.float64)

    mask = N.where(x < 1.83, 1, 0)
    result = N.where(mask == 1, _interp(x, _lmcx, _lmce), result)

    mask = N.where(x >= 1.83, 1, 0) * N.where(x <= 2.75, 1, 0)
    result = N.where(mask == 1, \
             3.1 + (2.04 + 0.094 * (x - 1.83)) * (x - 1.83), result)

    mask = N.where(x > 2.75, 1, 0)
    result = N.where(mask == 1, \
             3.1 - 0.236 + 0.462 * x + 0.105 * x * x + \
             0.454 / ((x - 4.557)**2 + 0.293), result)

    return result

def _computeSMC(x):
    x1 = N.where (x > 10.0, 10.0, x)
    return _interp(x1, _smcx, _smce)

def _computeXgal(x):
    return 2.43 * ((0.011 * x - 0.198) * x + 1.509) * x

# extinction curves are computed at load time, once and for all, on top
# of the default wave set. Note that this is not thread safe.

_waveset = _buildDefaultWaveset()

_seaton  = _computeSeaton(_waveset)
_lmc     = _computeLMC(_waveset)
_smc     = _computeSMC(_waveset)
_xgal    = _computeXgal(_waveset)



class _ExtinctionLaw(object):

    def _computeTransparency(self, extval, curve):
        return 10.0 ** (-0.4 * extval * curve)


class Gal1(_ExtinctionLaw):
    citation = 'Seaton 1979 (MNRAS 187:75)'
    name = 'gal1'
    def __init__(self, extval):

        global _seaton
        self._wavetable = _waveset.copy()
        self.transparencytable = self._computeTransparency(extval, _seaton)


class Gal2(_ExtinctionLaw):
    citation = 'Savage & Mathis 1979 (ARA&A 17:73)'
    name = 'gal2'
    def __init__(self, extval):
        raise NotImplementedError("Sorry, %s is not yet implemented" % self.name)
    
class Gal3(_ExtinctionLaw):
    citation='Cardelli, Clayton & Mathis 1989 (ApJ 345:245)'
    name='gal3'

    def __init__(self, extval):
        raise NotImplementedError("Sorry, %s is not yet implemented" % self.name)


class Smc(_ExtinctionLaw):
    citation='Prevot et al.1984 (A&A 132:389)'
    name='SMC'
    def __init__(self, extval):
        global _smc
        self._wavetable = _waveset.copy()
        self.transparencytable = self._computeTransparency(extval, _smc)


class Lmc(_ExtinctionLaw):
    citation='Howarth 1983 (MNRAS 203:301)'
    name='LMC'
    def __init__(self, extval):
        self.name = 'LMC'
        global _lmc
        self._wavetable = _waveset.copy()
        self.transparencytable = self._computeTransparency(extval, _lmc)


class Xgal(_ExtinctionLaw):
    citation = 'Calzetti, Kinney and Storchi-Bergmann, 1994 (ApJ 429:582)'
    name='XGAL'
    def __init__(self, extval):
        global _xgal
        self._wavetable = _waveset.copy()
        self.transparencytable = self._computeTransparency(extval, _xgal)


reddeningClasses = {'gal1': Gal1,
                    'gal2': Gal2,
                    'gal3': Gal3,
                    'smc':  Smc,
                    'lmc':  Lmc,
                    'xgal': Xgal}

def factory(redlaw, *args, **kwargs):
    return apply(reddeningClasses[string.lower(redlaw)], args, kwargs)

class DeprecatedExtinction(spectrum.SpectralElement):
    """extinction = Extinction(extinction in magnitudes,
    'gal1|smc|lmc reddening laws)"""
    def __init__(self, extval, redlaw):
        ''' Extinction mimics as a spectral element.
        '''
        law = factory(redlaw, extval)
        self._wavetable = 10000.0 / law._wavetable
        self._throughputtable = law.transparencytable
        self.name=law.name
        self.citation=law.citation
        self.waveunits=units.Units('angstrom')
        self.isAnalytic=False
        self.warnings={}

