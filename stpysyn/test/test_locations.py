import os
import warnings

from nose import tools

PYSYN_CDBS = os.environ['PYSYN_CDBS']

@tools.nottest
def set_test_cdbs():
    os.environ['PYSYN_CDBS'] = os.path.join(os.path.dirname(__file__),
                                            'data', 'cdbs')
    # the fake cdbs is incomplete and pysynphot prints some warnings,
    # this will suppress them.
    warnings.simplefilter('ignore')

    import pysynphot.locations as locations
    reload(locations)


def restore_cdbs():
    os.environ['PYSYN_CDBS'] = PYSYN_CDBS
    import pysynphot.locations as locations
    reload(locations)


# test the ability of pysynphot.locations to auto-gather extinction laws
# from $PYSYN_CDBS/extinction/
@tools.with_setup(set_test_cdbs, restore_cdbs)
def test_get_RedLaws():
    import pysynphot.locations as locations
    RedLaws = locations.RedLaws.copy()

    shouldbe = {'lmc30dor': 'lmc_30dorshell_001.fits',
                'lmcavg': 'lmc_diffuse_002.fits',
                'mwdense': 'milkyway_dense_001.fits',
                'mwavg': 'milkyway_diffuse_001.fits',
                'smcbar': 'smc_bar_001.fits',
                'xgalsb': 'xgal_starburst_003.fits'}

    for name in shouldbe:
      assert shouldbe[name] == os.path.basename(RedLaws[name])


# test that we can add a new conversion to the CONVERTDICT and
# irafconvert will find and use it.
def test_CONVERTDICT():
    import pysynphot.locations as locations

    locations.CONVERTDICT['testjref'] = './data/cdbs/jref/'

    refpath = './data/cdbs/jref/empty_test_file.txt'

    filename = locations.irafconvert('testjref$empty_test_file.txt')

    assert refpath == filename
