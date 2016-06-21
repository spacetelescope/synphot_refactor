# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Different types of integrators.

The integrator is meant to be a low-level arithmetic machine.
Therefore, there are minimal checks on the inputs.

"""
from __future__ import absolute_import, division, print_function

# THIRD-PARTY
import numpy as np

__all__ = ['trapezoid_integrator']


def trapezoid_integrator(x, y):
    """Trapezoid integrator.

    Parameters
    ----------
    x, y : array_like
        1D array for integration.
        The array representing wavelengths is assumed to be sorted.

    Returns
    -------
    result : float
        Integrated result.

    Examples
    --------
    >>> from synphot import models
    >>> from synphot.integrator import trapezoid_integrator
    >>> source = models.Box1D(amplitude=1, x_0=5000, width=100)
    >>> x = source.sampleset()
    >>> y = source(x)
    >>> result = trapezoid_integrator(x.value, y.value)
    >>> print('{0:.4f}'.format(result))
    100.0000

    """
    result = np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1]))
    if x[-1] < x[0]:  # If monotonic descending.
        result *= -1.0
    return result
