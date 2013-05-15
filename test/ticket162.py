from __future__ import division
import os
import testutil
import pysynphot as S
from pysynphot import spparser
from pysynphot import locations, refs


class ETCTestCase(testutil.FPTestCase):

    def setUp(self):
        self.spectrum = "spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.obsmode = "cos,fuv,g140l,c1105"
        # These tests were defined using this graph table
        self.oldref = refs.getref()
        S.setref(comptable='$PYSYN_CDBS/mtab/tad1851am_tmc.fits')
        self.setup2()
        self.tda = dict(obsmode=self.obsmode,
                        spectrum=self.spectrum)
        self.tda.update(refs.getref())

    def setup2(self):
        try:
            self.oldpath = os.path.abspath(os.curdir)
            if os.path.isdir(os.path.join(locations.specdir, 'generic')):
                os.chdir(os.path.join(locations.specdir, 'generic'))
            else:
                os.chdir(locations.specdir)
            self.sp = spparser.parse_spec(self.spectrum)
            self.bp = S.ObsBandpass(self.obsmode)
            self.parameters = ["spectrum=%s" % self.spectrum,
                               "instrument=%s" % self.obsmode,
                               "obsmode=%s" % self.obsmode]
        except AttributeError:
            pass

    def tearDown(self):
        os.chdir(self.oldpath)
        S.setref(comptable=self.oldref['comptable'])

    def testwarn(self):
        obs=S.Observation(self.sp,self.bp,force='taper')
        self.assert_('PartialOverlap' in obs.warnings)

