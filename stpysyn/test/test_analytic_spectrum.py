import numpy as np
from stpysyn.test import testutil

import pysynphot as S

class TestPowerLaw(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)

  def test_values(self):
    ref = np.array([ 16.        ,  15.78843266,  15.58035072,  15.37568551,
                     15.17436992,  14.97633838,  14.78152682,  14.5898726 ,
                     14.40131453,  14.21579277])

    pl = S.PowerLaw(6000,-4,'angstrom','photlam')

    test = pl.sample(self.wave[:10])

    self.assertApproxNumpy(test,ref)

  def test_conversion1(self):
    pl = S.PowerLaw(6000,-4,'angstrom','photlam')

    angflux = pl.sample(self.wave)

    pl.convert('nm')

    nmflux = pl.sample(self.wave/10.)

    self.assertEqualNumpy(nmflux,angflux)

  def test_conversion2(self):
    pl = S.PowerLaw(6000,-4,'angstrom','photlam')

    self.assertEqualNumpy(pl.sample(self.wave)[:10],pl.sample(self.wave[:10]))

    pl.convert('nm')

    self.assertEqualNumpy(pl.sample(self.wave)[:10],pl.sample(self.wave[:10]))


class TestGaussian(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)

  def test_values(self):
    ref = np.array([  3.63805721e-123,   9.05875032e-121,   2.13395205e-118,
                      4.75574568e-116,   1.00269809e-113,   2.00004310e-111,
                      3.77421053e-109,   6.73799198e-107,   1.13802672e-104,
                      1.81841090e-102])

    g = S.GaussianSource(1,4000,100,'angstrom','photlam')

    test = g.sample(self.wave[:10])

    self.assertApproxNumpy(test,ref)

  def test_symmetry1(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')

    self.assertApproxFP(g.sample(3950),g.sample(4050))

  def test_symmetry2(self):
    g = S.GaussianSource(1,400,100,'nm','flam')

    self.assertApproxFP(g.sample(395),g.sample(405))

  def test_conversion1(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')

    angflux = g.sample(self.wave)

    g.convert('nm')

    nmflux = g.sample(self.wave/10.)

    self.assertEqualNumpy(nmflux,angflux)

  def test_conversion2(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')

    self.assertEqualNumpy(g.sample(self.wave)[:10],g.sample(self.wave[:10]))

    g.convert('nm')

    self.assertEqualNumpy(g.sample(self.wave)[:10],g.sample(self.wave[:10]))

  def test_conversion3(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')

    tf1 = g.total_flux

    g.convert('nm')

    tf2 = g.factor * g.sigma * np.sqrt(2.0 * np.pi)

    self.assertEqual(tf1,tf2)

class TestFlatSpec(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)

  def test_values(self):
    ref = np.array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])

    f = S.FlatSpectrum(1,'angstrom','photlam')

    test = f.sample(self.wave[:10])

    self.assertEqualNumpy(test,ref)

  def test_conversion1(self):
    f = S.FlatSpectrum(1,'angstrom','photlam')

    angflux = f.sample(self.wave)

    f.convert('nm')

    nmflux = f.sample(self.wave/10.)

    self.assertEqualNumpy(nmflux,angflux)

  def test_conversion2(self):
    f = S.FlatSpectrum(1,'angstrom','photlam')

    self.assertEqualNumpy(f.sample(self.wave)[:10],f.sample(self.wave[:10]))

    f.convert('nm')

    self.assertEqualNumpy(f.sample(self.wave)[:10],f.sample(self.wave[:10]))

class TestBlackBody(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)

  def test_values(self):
    ref = np.array([ 0.00019318,  0.00019623,  0.0001993 ,  0.00020238,  0.00020549,
                     0.00020861,  0.00021175,  0.00021491,  0.00021809,  0.00022128])

    bb = S.BlackBody(5500)

    test = bb.sample(self.wave[:10])

    self.assertApproxNumpy(test,ref,accuracy=3.e-5)
