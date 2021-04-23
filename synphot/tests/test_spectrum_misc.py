# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test spectrum.py module and related functionalities that are not covered
by ``test_spectrum_source.py`` nor ``test_spectrum_bandpass.py``."""

# STDLIB
import os
import shutil
import tempfile

# THIRD-PARTY
import numpy as np
import pytest

# ASTROPY
from astropy import units as u
from astropy.io import fits
from astropy.modeling.models import Const1D, RedshiftScaleFactor
from astropy.tests.helper import assert_quantity_allclose

# LOCAL
from synphot.tests.test_units import _wave, _flux_jy, _flux_photlam
from synphot import exceptions, units
from synphot.compat import ASTROPY_LT_4_0
from synphot.models import Box1D, Empirical1D, GaussianFlux1D, get_waveset
from synphot.spectrum import SourceSpectrum, SpectralElement


def setup_module(module):
    import astropy.constants as const
    from astropy.constants import si, astropyconst13

    const.h = si.h = astropyconst13.h


def teardown_module(module):
    import astropy.constants as const

    if ASTROPY_LT_4_0:
        from astropy.constants import si, astropyconst20
        const.h = si.h = astropyconst20.h
    else:
        from astropy.constants import si, astropyconst40
        const.h = si.h = astropyconst40.h


class TestCheckOverlap:
    """Test spectrum overlap check. This method is ever only used
    in the form of ``bp.check_overlap(sp)``, so that is what is
    tested here.
    """
    def setup_class(self):
        self.bp = SpectralElement(
            Empirical1D, points=[2999.9, 3000, 6000, 6000.1],
            lookup_table=[0, 1, 1, 0])

    def test_full(self):
        """As long as we don't have to extrapolate or taper
        source spectrum, it's okay.
        """
        sp = SourceSpectrum(
            Empirical1D, points=[999.9, 1000, 9000, 9000.1],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'full'

        sp = SourceSpectrum(
            Empirical1D, points=[3999.9, 4000, 4500, 4500.1],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'full'

    def test_partial_most(self):
        """99% overlap."""
        sp = SourceSpectrum(
            Empirical1D, points=[3005, 3005.1, 6000.1, 6000.2],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'partial_most'

    def test_partial_notmost(self):
        """Extrapolation or taper required."""
        sp = SourceSpectrum(
            Empirical1D, points=[3999.9, 4500.1], lookup_table=[1, 1])
        assert self.bp.check_overlap(sp) == 'partial_notmost'

    def test_none(self):
        """No overlap at all."""
        sp = SourceSpectrum(
            Empirical1D, points=[99.9, 100, 2999.8, 2999.9],
            lookup_table=[0, 1, 1, 0])
        assert self.bp.check_overlap(sp) == 'none'

    def test_special_cases(self):
        """One of them has no waveset defined."""
        # Other has no waveset
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert self.bp.check_overlap(sp) == 'full'

        # Self has no waveset
        bp = SpectralElement(Const1D, amplitude=1)
        sp = SourceSpectrum(Box1D, amplitude=1, x_0=5000, width=10)
        assert bp.check_overlap(sp) == 'partial_notmost'

    def test_exceptions(self):
        """Invalid input."""
        with pytest.raises(exceptions.SynphotError):
            self.bp.check_overlap(1)


class TestForceExtrap:
    """Test forcing extrapolation on a source spectrum."""

    @pytest.mark.parametrize('z', [0, 0.03])
    def test_empirical(self, z):
        sp = SourceSpectrum(Empirical1D, points=[1000, 2000, 3000, 4000],
                            lookup_table=[0.5, 0.6, 10.6, 1.5], fill_value=0)
        sp.z = z
        w = [900, 4300]
        assert_quantity_allclose(sp(w), 0 * units.PHOTLAM)  # No extrapolation

        is_forced = sp.force_extrapolation()  # Force extrapolation
        assert is_forced
        assert_quantity_allclose(sp(w), [0.5, 1.5] * units.PHOTLAM)

    def test_analytical(self):
        """Forcing is not possible."""
        sp = SourceSpectrum(GaussianFlux1D, mean=5500, total_flux=1, fwhm=10)
        w = [100, 10000]
        assert_quantity_allclose(sp(w), 0 * units.PHOTLAM)

        is_forced = sp.force_extrapolation()
        assert not is_forced
        assert_quantity_allclose(sp(w), 0 * units.PHOTLAM)


class TestWaveset:
    """Tests related to spectrum waveset."""
    def test_none(self):
        sp = SourceSpectrum(Const1D, amplitude=1)
        assert sp.waveset is None

    def test_sampleset(self):
        tf_unit = u.erg / (u.cm * u.cm * u.s)
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=(1 * tf_unit), mean=5000, fwhm=10)
        np.testing.assert_array_equal(sp.waveset.value, sp.model.sampleset())

    def test_box1d(self):
        bp = SpectralElement(Box1D, x_0=2000, width=1)
        w = bp.waveset.value
        w_true = bp.model.sampleset()

        np.testing.assert_array_equal(w, w_true)
        np.testing.assert_allclose(
            w[([0, 1, -2, -1], )], bp.model.sampleset(minimal=True))

        # Make sure scale does not change waveset
        bp2 = bp * 2
        bp3 = 0.5 * bp
        np.testing.assert_array_equal(bp2.waveset.value, w_true)
        np.testing.assert_array_equal(bp3.waveset.value, w_true)

    def test_composite_none(self):
        bp1 = SpectralElement(Box1D, amplitude=1, x_0=5000, width=10)
        bp2 = SpectralElement(Const1D, amplitude=2)
        bp = bp1 * bp2
        np.testing.assert_array_equal(bp.waveset, bp1.waveset)

    def test_composite(self):
        totflux = 1 * (u.erg / (u.cm * u.cm * u.s))
        g1 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=5000, fwhm=10)
        g2 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=6500, fwhm=100)
        g3 = SourceSpectrum(
            GaussianFlux1D, total_flux=totflux, mean=7500, fwhm=5)
        sp = SpectralElement(Box1D, x_0=1000, width=1) * (g1 + g2 + g3)
        assert_quantity_allclose(
            sp.waveset[::100],
            [999.49, 1000.49, 5019.95906231, 6699.59062307,
             7509.7672007] * u.AA)

    def test_redshift(self):
        tf_unit = u.erg / (u.cm * u.cm * u.s)
        sp = SourceSpectrum(
            GaussianFlux1D, total_flux=(1 * tf_unit), mean=5000, fwhm=10)
        sp.z = 1.3
        m = RedshiftScaleFactor(z=1.3)
        w_step25_z0 = [4978.76695499, 4989.3834775, 5000, 5010.6165225] * u.AA
        assert_quantity_allclose(sp.waveset[::25], m(w_step25_z0))

    def test_redshift_none(self):
        sp = SourceSpectrum(Const1D, amplitude=1, z=1.3)
        assert sp.waveset is None

    def test_complicated_tree(self):
        """Throw everything in and insert redshift and scale in the middle."""

        # On one side, we have a composite bandpass.
        bp1 = SpectralElement(Const1D, amplitude=1.01)
        bp2 = SpectralElement(
            Empirical1D, points=[4999, 5000.001, 5030], lookup_table=[0, 1, 0])
        bp = bp1 * (0.8 * bp2)  # [4999, 5000.001, 5030]

        # On the other side, we have composite spectrum with
        # scale and redshift.
        sp1 = SourceSpectrum(
            Empirical1D, points=[5001, 5011, 5020], lookup_table=[0, 1, 0])
        sp2 = SourceSpectrum(
            Empirical1D, points=[5000, 5010, 5020], lookup_table=[0, 1, 0])
        sp3 = sp2 + (sp1 * 0.5)  # [5000, 5001, 5010, 5011, 5020]
        sp3.z = 0.01  # [5050, 5051.01, 5060.1, 5061.11, 5070.2]
        sp = sp1 + sp3  # [5001, 5011, 5020, 5050, 5051.01, 5060.1, 5061.11, 5070.2]  # noqa

        sp_final = sp * bp
        np.testing.assert_array_equal(
            sp_final.waveset.value,
            [4999, 5000.001, 5001, 5011, 5020, 5030, 5050, 5051.01,
             5060.1, 5061.11, 5070.2])

    def test_exceptions(self):
        with pytest.raises(exceptions.SynphotError):
            get_waveset('foo')


class TestMathOperators:
    """Test spectrum math operators."""
    def setup_class(self):
        self.sp_1 = SourceSpectrum(
            Empirical1D, points=[3999.9, 4000.0, 5000.0, 6000.0, 6000.1],
            lookup_table=[0, 3.5e-14, 4e-14, 4.5e-14, 0] * units.FLAM)
        self.sp_2 = SourceSpectrum(
            Empirical1D, points=_wave, lookup_table=_flux_jy,
            meta={'PHOTLAM': [9.7654e-3, 1.003896e-2, 9.78473e-3]})
        self.bp_1 = SpectralElement(
            Empirical1D, points=[399.99, 400.01, 500.0, 590.0, 600.1] * u.nm,
            lookup_table=[0, 0.1, 0.2, 0.3, 0])

    def test_source_add(self):
        """Compare with ASTROLIB PYSYNPHOT."""
        ans = self.sp_1 + self.sp_2
        assert_quantity_allclose(
            ans(ans.waveset),
            [0.00976521, 0.01681283, 0.01970276, 0.01998463, 0.0197387,
             0.01985257, 0.02337638, 0.00978454] * units.PHOTLAM, rtol=1e-4)

    def test_source_sub(self):
        """Compare with ASTROLIB PYSYNPHOT."""
        ans = self.sp_1 - self.sp_2
        assert_quantity_allclose(
            ans(ans.waveset),
            [-9.76520783e-03, -2.71758275e-03, 1.72346256e-04, -9.29051118e-05,
             1.69629843e-04, 2.83499328e-04, 3.80731187e-03,
             -9.78453651e-03] * units.PHOTLAM,
            rtol=1e-4)

    def test_source_addsub_circular(self):
        """sp = sp + sp - sp"""
        ans = self.sp_1 + self.sp_1 - self.sp_1
        assert_quantity_allclose(ans(ans.waveset), self.sp_1(ans.waveset))

    def test_source_addsub_exception(self):
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 + self.bp_1

    @pytest.mark.parametrize('x', [2, 2 * u.dimensionless_unscaled])
    def test_source_mul_div_scalar(self, x):
        w = self.sp_1.waveset

        ans1 = self.sp_1 * x
        assert_quantity_allclose(
            ans1(w),
            [0, 0.01409552, 0.02013646, 0.02718424, 0] * units.PHOTLAM,
            rtol=1e-6)

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.sp_1
            assert_quantity_allclose(ans1(w), ans2(w), rtol=0)

        ans3 = self.sp_1 / x
        assert_quantity_allclose(
            ans3(w),
            [0, 0.00352388, 0.00503411, 0.00679606, 0] * units.PHOTLAM,
            atol=1e-7 * units.PHOTLAM)

    def test_source_mul_div_spec(self):
        """Compare mul with ASTROLIB PYSYNPHOT. Also test bp * sp."""
        ans1 = self.sp_1 * self.bp_1
        ans2 = self.bp_1 * self.sp_1
        w = ans1.waveset[:-1]
        assert_quantity_allclose(
            ans1(w),
            [0, 3.52381254e-04, 7.04792712e-04, 2.01360717e-03, 3.97184014e-03,
             4.03718269e-05, 0] * units.PHOTLAM, rtol=1e-4)
        assert_quantity_allclose(ans1(w), ans2(w), rtol=0)

        ans3 = self.sp_1 / self.bp_1
        assert_quantity_allclose(
            ans3(w),
            [0, 0.14095528, 0.07048066, 0.05034117, 0.04413243, 4.57601236,
             0] * units.PHOTLAM)

        ans4 = self.sp_1 / self.sp_1
        assert_quantity_allclose(
            ans4([4000, 5000, 6000]), 1 * u.dimensionless_unscaled)

        # Dividing throughput by flux does not make sense.
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 / self.sp_1

    def test_source_mul_div_exceptions(self):
        """Only mul is tested but truediv uses the same validation."""
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * self.sp_2

        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * (1 - 1j)

        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * u.Quantity([1, 2])
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * u.Quantity(1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            self.sp_1 * (1 * u.AA)

    def test_bandpass_addsub(self):
        """Not supported."""
        with pytest.raises(NotImplementedError):
            self.bp_1 + self.bp_1
        with pytest.raises(NotImplementedError):
            self.bp_1 + 2.0
        with pytest.raises(NotImplementedError):
            self.bp_1 - self.bp_1
        with pytest.raises(NotImplementedError):
            self.bp_1 - 2.0

    @pytest.mark.parametrize('x', [2.0, 2.0 * u.dimensionless_unscaled])
    def test_bandpass_mul_div_scalar(self, x):
        w = self.bp_1.waveset

        ans1 = self.bp_1 * x
        assert_quantity_allclose(ans1(w), [0, 0.2, 0.4, 0.6, 0])

        # rmul does not work with Quantity
        if not isinstance(x, u.Quantity):
            ans2 = x * self.bp_1
            assert_quantity_allclose(ans1(w), ans2(w), rtol=0)

        ans3 = self.bp_1 / x
        assert_quantity_allclose(ans3(w), [0, 0.05, 0.1, 0.15, 0])

    def test_bandpass_mul_div_bandpass(self):
        ans1 = self.bp_1 * self.bp_1
        assert_quantity_allclose(
            ans1(ans1.waveset), [0, 0.01, 0.04, 0.09, 0])

        w = [4000.1, 5000, 5900]  # Avoid div by zero
        ans2 = self.bp_1 / self.bp_1
        assert_quantity_allclose(ans2(w), 1)

    def test_bandpass_mul_div_exceptions(self):
        """Only mul is tested but truediv uses the same validation."""
        class DummyObject:
            pass

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * DummyObject()

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * u.Quantity([1, 2])
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * u.Quantity(1 - 1j)
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * (1 * u.AA)

        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * [1, 2]
        with pytest.raises(exceptions.IncompatibleSources):
            self.bp_1 * (1 - 1j)


class TestWriteSpec:
    """Test spectrum to_fits() method."""
    def setup_class(self):
        self.outdir = tempfile.mkdtemp()
        self.sp = SourceSpectrum(
            Empirical1D, points=_wave, lookup_table=_flux_photlam,
            meta={'expr': 'Test source'})
        self.bp = SpectralElement(
            Empirical1D, points=_wave, lookup_table=np.ones(_wave.shape),
            meta={'expr': 'Test bandpass'})

    @pytest.mark.parametrize(
        ('is_sp', 'ext_hdr'),
        [(True, None),
         (True, {'foo': 'foo'}),
         (False, None),
         (False, {'foo': 'foo'})])
    def test_write(self, is_sp, ext_hdr):
        outfile = os.path.join(self.outdir, 'outspec.fits')

        if is_sp:
            sp1 = self.sp
        else:
            sp1 = self.bp

        if ext_hdr is None:
            sp1.to_fits(outfile, overwrite=True, trim_zero=False,
                        pad_zero_ends=False)
        else:
            sp1.to_fits(outfile, overwrite=True, trim_zero=False,
                        pad_zero_ends=False, ext_header=ext_hdr)

        # Read it back in and check
        sp2 = sp1.__class__.from_file(outfile)
        np.testing.assert_allclose(sp2(sp2.waveset), sp1(sp1.waveset))
        hdr = fits.getheader(outfile, 1)
        assert 'expr' in hdr
        if ext_hdr is not None:
            assert 'foo' in hdr

    def teardown_class(self):
        shutil.rmtree(self.outdir)
