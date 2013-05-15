"""
This tests whether the .components attribute of observationmode.ObservationMode
objects reflects the currently set COMPTABLE variable after the COMPTABLE
variable is switched within the same code.

"""

from __future__ import division

import os
from unittest import TestCase

from pysynphot import observationmode, locations, refs

class TestCompSwitch(TestCase):
    def setUp(self):
        self.cdbs = os.environ['PYSYN_CDBS']

        graphtab = os.path.join('mtab','u921351jm_tmg.fits')
        self.old_refs = refs.getref()
        refs.GRAPHTABLE = locations._refTable(graphtab)

    def tearDown(self):
        refs.setref(graphtable=self.old_refs['graphtable'])
        refs.setref(comptable=self.old_refs['comptable'])

    def test_one(self):
        throughput_list = ['comp/ota/hst_ota_007_syn.fits',
                           'comp/acs/acs_hrc_m12_005_syn.fits',
                           'comp/acs/acs_hrc_m3_005_syn.fits',
                           'comp/acs/acs_f435w_005_syn.fits',
                           'comp/acs/acs_hrc_win_005_syn.fits',
                           'comp/acs/acs_hrc_ccd_013_syn.fits']

        for i, f in enumerate(throughput_list):
            throughput_list[i] = os.path.join(self.cdbs, f)

        cmptb_name = os.path.join('mtab', 'ub31649mm_tmc.fits')
        refs.COMPTABLE = locations._refTable(cmptb_name)

        obs = observationmode.ObservationMode('acs,hrc,f435w')

        n = self.check_list(throughput_list,
                            [c.throughput_name for c in obs.components])

        if n:
            raise AssertionError(n)

    def test_two(self):
        throughput_list = ['comp/ota/hst_ota_007_syn.fits',
                           'comp/acs/acs_hrc_m12_005_syn.fits',
                           'comp/acs/acs_hrc_m3_005_syn.fits',
                           'comp/acs/acs_f435w_004_syn.fits',
                           'comp/acs/acs_hrc_win_005_syn.fits',
                           'comp/acs/acs_hrc_ccd_011_syn.fits']

        for i, f in enumerate(throughput_list):
            throughput_list[i] = os.path.join(self.cdbs, f)

        cmptb_name = os.path.join('mtab', 'r1j2146sm_tmc.fits')
        refs.COMPTABLE = locations._refTable(cmptb_name)

        obs = observationmode.ObservationMode('acs,hrc,f435w')

        n = self.check_list(throughput_list,
                            [c.throughput_name for c in obs.components])

        if n:
            raise AssertionError(n)

    def check_list(self, expect_list, in_list) :
        missing = []

        for i, x in enumerate(expect_list) :
            x = os.path.normpath(x)
            x = os.path.normcase(x)
            expect_list[i] = x
            print "EXPECT", expect_list[i]

        for i, x in enumerate(in_list) :
            x = os.path.normpath(x)
            x = os.path.normcase(x)
            in_list[i] = x
            print "IN    ", in_list[i]

        for x in expect_list :
            if not x in in_list :
                missing.append(x)

        if len(missing) == 0 :
            return False

        self.tra = {'missing' : str(missing)}
        return "Missing: %s" % missing
