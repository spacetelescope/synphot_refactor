# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Different types of integrators."""
from __future__ import absolute_import, division, print_function

# THIRD-PARTY
import numpy as np

__all__ = ['BaseIntegrator', 'TrapezoidIntegrator', 'TrapezoidFluxIntegrator']


class BaseIntegrator(object):
    """Base class for integrator."""
    def __init__(self):
        self._source = None

    def _integrate(self, *args, **kwargs):
        """Use this if source does not have its own integration algorithm."""
        raise NotImplementedError('To be implemented by subclasses.')

    def __call__(self, source, *args, **kwargs):
        """Perform integration on given source.

        A source must have a ``__call__`` method that performs
        evaluation. For example, a spectrum or a model. If it has
        a built-in ``integrate`` method, that will be used instead.

        Parameters
        ----------
        source : obj
            Object to be integrated.

        args, kwargs
            Arguments needed for integration, depending on the algorithm.

        Returns
        -------
        result : float
            Integrated value.

        """
        self._source = source

        if hasattr(self._source, 'analytic_integral'):
            result = self._source.analytic_integral(*args, **kwargs)
        else:
            result = self._integrate(*args, **kwargs)

        return result


class TrapezoidIntegrator(BaseIntegrator):
    """Trapezoid integrator.

    Examples
    --------
    >>> from synphot import models
    >>> source = models.Box1D(amplitude=1, x_0=5000, width=100)
    >>> TrapezoidIntegrator()(source, source.sampleset())
    100.01

    """
    @staticmethod
    def _raw_math(x, y):
        result = np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1]))
        if x[-1] < x[0]:  # If monotonic descending.
            result *= -1.0
        return result

    def _integrate(self, x):
        """Perform trapezoid integration.

        Parameters
        ----------
        x : array_like
            Sampling values. Assumed to be either monotonic
            ascending or descending.

        Returns
        -------
        result : array_like
            Integrated result.

        """
        return self._raw_math(x, self._source(x))


class TrapezoidFluxIntegrator(TrapezoidIntegrator):
    """Trapezoid integrator that handles flux conversion."""
    def _integrate(self, x, flux_unit='photlam', **kwargs):
        """Perform trapezoid integration.

        Parameters
        ----------
        x : array_like
            Sampling values. Assumed to be either monotonic
            ascending or descending.

        flux_unit : str or `astropy.units.core.Unit`
            Flux is converted to this unit first prior to integration.

        kwargs : dict
            Keywords accepted by :func:`synphot.units.convert_flux`.

        Returns
        -------
        result : array_like
            Integrated result.

        """
        from . import units
        y = units.convert_flux(x, self._source(x), flux_unit, **kwargs)
        return self._raw_math(x, y)
