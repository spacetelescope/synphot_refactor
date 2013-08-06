# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division, print_function
import os.path
import warnings
import numpy as np

from . import locations

_default_waveset = None
_default_waveset_str = None

# Constants to hold tables.
GRAPHTABLE = ''
GRAPHDICT = {}
COMPTABLE = ''
COMPDICT = {}
THERMTABLE = ''
THERMDICT = {}

PRIMARY_AREA = 45238.93416  # cm^2 - default to HST mirror


def set_default_waveset(minwave=500, maxwave=26000, num=10000.,
                        delta=None, log=True):
    """
    Set the default waveset for pysynphot spectral types. Calculated wavesets
    are inclusive of `minwave` and exclusive of `maxwave`.

    Parameters
    ----------
    minwave: float, optional
        The starting point of the waveset.

    maxwave: float, optional
        The end point of the waveset.

    num: int, optional
        The number of elements in the waveset. If `delta` is not None this
        is ignored.

    delta: float, optional
        Delta between values in the waveset. If not None, this overrides
        the `num` parameter. If `log` is True then `delta` is assumed to be
        the spacing in log space.

    log: bool, optional
        Sets whether the waveset is evenly spaced in log or linear space. If
        `log` is True then `delta` is assumed to be the delta in log space.
        `minwave` and `maxwave` should be given in normal space regardless
        of the value of `log`.

    """
    global _default_waveset
    global _default_waveset_str

    s = 'Min: %s, Max: %s, Num: %s, Delta: %s, Log: %s'

    if log and not delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, num, None, log)])

        logmin = np.log10(minwave)
        logmax = np.log10(maxwave)

        _default_waveset = np.logspace(logmin, logmax, num, endpoint=False)

    elif log and delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, None, delta, log)])

        logmin = np.log10(minwave)
        logmax = np.log10(maxwave)

        _default_waveset = 10 ** np.arange(logmin, logmax, delta)

    elif not log and not delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, num, None, log)])

        _default_waveset = np.linspace(minwave, maxwave, num, endpoint=False)

    elif not log and delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, None, delta, log)])

        _default_waveset = np.arange(minwave, maxwave, delta)

    _default_waveset_str = s


def _set_default_refdata():
    global GRAPHTABLE, COMPTABLE, THERMTABLE, PRIMARY_AREA
    # Component tables are defined here.

    try:
        GRAPHTABLE = locations._refTable(os.path.join('mtab', '*_tmg.fits'))
        COMPTABLE = locations._refTable(os.path.join('mtab', '*_tmc.fits'))
    except IOError as e:
        GRAPHTABLE = None
        COMPTABLE = None
        warnings.warn('No graph or component tables found; '
                      'functionality will be SEVERELY crippled. ' + str(e))

    try:
        THERMTABLE = locations._refTable(os.path.join('mtab', '*_tmt.fits'))
    except IOError as e:
        THERMTABLE = None
        warnings.warn('No thermal tables found, '
                      'no thermal calculations can be performed. ' + str(e))

    PRIMARY_AREA = 45238.93416  # cm^2 - default to HST mirror

    set_default_waveset()

# Do this on import
_set_default_refdata()


def setref(graphtable=None, comptable=None, thermtable=None,
           area=None, waveset=None):
    """
    provide user access to global reference data.
    Graph/comp/therm table names must be fully specified.

    """

    global GRAPHTABLE, COMPTABLE, THERMTABLE, PRIMARY_AREA, GRAPHDICT, \
        COMPDICT, THERMDICT

    GRAPHDICT = {}
    COMPDICT = {}
    THERMDICT = {}

    # Check for all None, which means reset
    kwds = set([graphtable, comptable, thermtable, area, waveset])
    if kwds == set([None]):
        #then we should reset everything.
        _set_default_refdata()
        return

    # Otherwise, check them all separately
    if graphtable is not None:
        GRAPHTABLE = locations.irafconvert(graphtable)

    if comptable is not None:
        COMPTABLE = locations.irafconvert(comptable)

    if thermtable is not None:
        THERMTABLE = locations.irafconvert(thermtable)

    # Area is a bit different:
    if area is not None:
        PRIMARY_AREA = area

    if waveset is not None:
        if len(waveset) not in (3, 4):
            raise ValueError('waveset tuple must contain 3 or 4 values')

        minwave = waveset[0]
        maxwave = waveset[1]
        num = waveset[2]

        if len(waveset) == 3:
            log = True
        elif len(waveset) == 4:
            if waveset[3].lower() == 'log':
                log = True
            elif waveset[3].lower() == 'linear':
                log = False
            else:
                raise ValueError('fourth waveset option must be "log" or '
                                 '"linear"')

        set_default_waveset(minwave, maxwave, num, log=log)

    # That's it.
    return


def getref():
    """
    Collects & returns the current refdata as a dictionary

    """

    ans = dict(graphtable=GRAPHTABLE,
             comptable=COMPTABLE,
             thermtable=THERMTABLE,
             area=PRIMARY_AREA,
             waveset=_default_waveset_str)
    return ans


def showref():
    """
    Prints the values settable by setref

    """
    refdata = getref()
    for k, v in refdata.items():
        print("{O:10s}: {1:s}".format(k, v))
