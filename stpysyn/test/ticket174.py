import pysynphot as S
from pysynphot.spparser import parse_spec

class ForcePartial(object):
    __test__ = True

    def setUp(self):
        #Test with the discovery case
        self.rband=(1146,1213)
        bp=S.ObsBandpass('cos,fuv,g130m,c1318,psa')
        sp=parse_spec("rn(icat(k93models,44500,0.0,5.0),box(1330.000000,1.),2e-013,flam)")
        self.obs=S.Observation(sp,bp)

    def test_noforce(self):
        try:
            x=self.obs.countrate(range=self.rband)
            raise AssertionError('exception not raised')
        except ValueError:
            pass

    def test_force(self):
        try:
            x=self.obs.countrate(range=self.rband,force=True)
        except ValueError:
            raise AssertionError("exception still raised")
                           
