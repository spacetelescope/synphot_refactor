"""
https://github.com/astropy/astropy/pull/7311 is tested here because
Astropy tests cannot have include_astropy_deprecations=True
"""
import warnings
import pytest


@pytest.mark.xfail
def test_deprecation_warning():
    from astropy.utils.exceptions import AstropyDeprecationWarning

    warnings.warn('This should fail', AstropyDeprecationWarning)


def test_pending_deprecation_warning_1():
    from astropy.utils.exceptions import AstropyPendingDeprecationWarning

    warnings.warn('This should not fail', AstropyPendingDeprecationWarning)


def test_pending_deprecation_warning_2():
    warnings.warn('This should not fail', PendingDeprecationWarning)
