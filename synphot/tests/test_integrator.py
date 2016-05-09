# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Test integrator.py module.

.. note:: ``TrapezoidFluxIntegrator`` is tested in test_spectrum.py.

"""
from __future__ import absolute_import, division, print_function

# THIRD-PARTY
import numpy as np

# LOCAL
from .. import integrator
from ..models import Box1D


class DummySource(object):
    """Fake source with its own analytic integral."""
    def analytic_integral(self):
        return 42


class TestTrapezoidIntegrator(object):
    """Test trapezoid integrator."""
    def setup_class(self):
        self.integrator = integrator.TrapezoidIntegrator()

    def test_analytic_source(self):
        assert self.integrator(DummySource()) == 42

    def test_box_model(self):
        # Ascending
        m = Box1D(amplitude=1, x_0=5000, width=10)
        x = m.sampleset()
        np.testing.assert_allclose(self.integrator(m, x), 10.01)

        # Descending
        np.testing.assert_allclose(self.integrator(m, x[::-1]), 10.01)
