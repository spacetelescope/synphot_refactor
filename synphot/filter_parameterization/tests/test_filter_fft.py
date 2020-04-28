import pytest
from astropy import units as u
from astropy.table import Table
from astropy.tests.helper import assert_quantity_allclose
from astropy.utils.data import get_pkg_data_filename

from synphot.filter_parameterization.filter_fft import filter_from_fft


class TestSVOFilters:
    """Unit test adapted from tynt package."""
    def setup_class(self):
        self.fft_table = Table.read(
            get_pkg_data_filename('data/fft_test_data.fits'))
        self.fft_table.add_index('filter')
        self.fft_cols = self.fft_table.colnames[5:]
        self.lambda_unit = self.fft_table['lambda_0'].unit
        self.dlamb_unit = self.fft_table['delta_lambda'].unit

    # Answers from:
    # http://svo2.cab.inta-csic.es/theory/fps/index.php?mode=browse&gname=SLOAN
    # http://svo2.cab.inta-csic.es/theory/fps/index.php?mode=browse&gname=2MASS
    # http://svo2.cab.inta-csic.es/theory/fps/index.php?mode=browse&gname=Generic&gname2=Johnson
    @pytest.mark.parametrize(
        ('filtername', 'lambda_mean_true', 'w_eff_true'),
        [('SLOAN/SDSS.u', 3561.8 * u.AA, 558.4 * u.AA),
         ('SLOAN/SDSS.g', 4718.9 * u.AA, 1158.4 * u.AA),
         ('SLOAN/SDSS.r', 6185.2 * u.AA, 1111.2 * u.AA),
         ('SLOAN/SDSS.i', 7499.7 * u.AA, 1044.6 * u.AA),
         ('SLOAN/SDSS.z', 8961.5 * u.AA, 1124.6 * u.AA),
         ('2MASS/2MASS.J', 12350 * u.AA, 1624.1 * u.AA),
         ('2MASS/2MASS.H', 16620 * u.AA, 2509.4 * u.AA),
         ('2MASS/2MASS.Ks', 21590 * u.AA, 2618.9 * u.AA),
         ('Generic/Johnson.U', 3531.1 * u.AA, 657 * u.AA),
         ('Generic/Johnson.B', 4430.4 * u.AA, 972.7 * u.AA),
         ('Generic/Johnson.V', 5537.2 * u.AA, 889.7 * u.AA),
         ('Generic/Johnson.R', 6939.6 * u.AA, 2070 * u.AA),
         ('Generic/Johnson.I', 8780.7 * u.AA, 2316 * u.AA)])
    def test_lambda_eff_w_eff(self, filtername, lambda_mean_true, w_eff_true):
        row = self.fft_table.loc[filtername]
        n_lambda = row['n_lambda']
        lambda_0 = row['lambda_0'] * self.lambda_unit
        delta_lambda = row['delta_lambda'] * self.dlamb_unit
        tr_max = row['tr_max']
        fft_pars = list(row[self.fft_cols])

        bp = filter_from_fft(
            n_lambda, lambda_0, delta_lambda, tr_max, fft_pars)
        assert_quantity_allclose(bp.avgwave(), lambda_mean_true, rtol=0.03)
        assert_quantity_allclose(bp.rectwidth(), w_eff_true, rtol=0.1)
