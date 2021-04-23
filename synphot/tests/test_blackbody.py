"""This should be updated if blackbody.py is removed from synphot."""

import numpy as np
from astropy import constants as const
from astropy import units as u

from synphot.blackbody import blackbody_nu
from synphot.units import FNU


# This test was removed from astropy in
# https://github.com/astropy/astropy/pull/9282
# but the rest of blackbody.py tests are still over there on astropy.
def test_blackbody_synphot():
    """Test that it is consistent with IRAF SYNPHOT BBFUNC."""
    # Solid angle of solar radius at 1 kpc
    fac = np.pi * (const.R_sun / const.kpc) ** 2 * u.sr

    with np.errstate(all='ignore'):
        flux = blackbody_nu([100, 1, 1000, 1e4, 1e5] * u.AA, 5000) * fac
    assert flux.unit == FNU

    # Special check for overflow value (SYNPHOT gives 0)
    assert np.log10(flux[0].value) < -143

    np.testing.assert_allclose(
        flux.value[1:], [0, 2.01950807e-34, 3.78584515e-26, 1.90431881e-27],
        rtol=0.01)  # 1% accuracy
