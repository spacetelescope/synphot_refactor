from stpysyn.test import testutil

import pysynphot as S

# The function S.spectrum.MergeWaveSets is designed so that merged wave sets
# have no two adjacent values which differ by less than 1e-10. This tests that.
class TestMergeWaveSets(testutil.FPTestCase):
  def test_merge_wave_sets(self):
    bb = S.BlackBody(20000)
    ext = S.Extinction(0.04,'gal1')

    new_wave = S.spectrum.MergeWaveSets(bb.wave,ext.wave)

    delta = new_wave[1:] - new_wave[:-1]

    self.assertTrue((new_wave > 1.e-12).all(),msg='Deltas < 1e-12, max delta = %f' % (delta.max(),))
