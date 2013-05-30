from __future__ import division

import os
from stpysyn.test import testutil

import pysynphot as S
from pysynphot import spparser
from pysynphot import locations, refs

class SuccessCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5000)
        self.bp=S.ObsBandpass('Johnson,V')
        self.oldref = S.refs.getref()
        S.setref(comptable='$PYSYN_CDBS/mtab/t260548pm_tmc.fits')
        self.tda=dict(spectrum=str(self.sp),
                      bp=str(self.bp)
                      )
        self.tda.update(refs.getref())

    def tearDown(self):
        S.setref(comptable=self.oldref['comptable'])

    def testok(self):
        obs=S.Observation(self.sp,self.bp)
        self.assert_('PartialOverlap' not in obs.warnings)


class RenormCase(testutil.FPTestCase):
    def setUp(self):
        self.oldcwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        self.spectrum="data/qso_template.fits"
        self.obsmode="cos,fuv,g140l,c1230,PSA"
        self.bp=S.ObsBandpass(self.obsmode)
        self.sp=S.FileSpectrum(self.spectrum)
        self.tst=self.sp.renorm(17.0,'vegamag',self.bp)

        self.tda=dict(spectrum=self.spectrum,
                      obsmode=self.obsmode,
                      file=S.__file__)

    def tearDown(self):
        os.chdir(self.oldcwd)

    def testwarn(self):
        self.tra=dict(name=str(self.tst),
                      spwarn=str(self.tst.warnings))
        self.failUnless('PartialRenorm' in self.tst.warnings,
                        "Warnings: %s"%self.tst.warnings)

class ParserRenormCase(testutil.FPTestCase):
    #The parser always uses force, so generates no warnings
    def setUp(self):
        self.oldcwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        self.spectrum = "data/qso_template.fits"
        self.obsmode = "cos,fuv,g140l,c1230,PSA"
        self.syncmd = "rn(spec(%s),band(%s),17.0,vegamag)" % (self.spectrum,
                                                              self.obsmode)
        self.tda = dict(spectrum=self.spectrum,
                        obsmode=self.obsmode,
                        syncmd=self.syncmd,
                        file=S.__file__)

    def tearDown(self):
        os.chdir(self.oldcwd)

    def testwarn(self):
        self.sp = spparser.parse_spec(self.syncmd)
        self.tra = dict(spwarn=str(self.sp.warnings),
                        name=str(self.sp))
        self.failIf('PartialRenorm' not in self.sp.warnings)


class ETCTestCase(testutil.FPTestCase):

    # TODO: Much of this setup code is repeated in so many different places
    # that I think some version of it could be centralized somewhere...
    def setUp(self):
        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "acs,sbc,F140LP"
        self.refrate = 0.0877036
        self.oldref = S.refs.getref()
        S.setref(comptable='$PYSYN_CDBS/mtab/t260548pm_tmc.fits')
        self.tda = dict(spectrum=str(self.spectrum), bp=str(self.obsmode))
        self.tda.update(refs.getref())
        self.setup2()

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
                               "instrument=%s" % self.obsmode]
        except AttributeError:
            pass

    def tearDown(self):
        os.chdir(self.oldpath)
        S.setref(comptable=self.oldref['comptable'])

    def testwarn(self):
        obs = S.Observation(self.sp, self.bp, force='taper')
        self.tra = dict(warnings=obs.warnings)
        self.assert_('PartialOverlap' in obs.warnings)



class TestComposite(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5500)
        self.sp.warnings['FakeWarn'] = True

    def testmult(self):
        sp2=self.sp*45
        self.assert_('FakeWarn' in sp2.warnings)

    def testsum(self):
        sp2=self.sp + S.FlatSpectrum(1)
        self.assert_('FakeWarn' in sp2.warnings)
