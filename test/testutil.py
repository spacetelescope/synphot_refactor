"""
Copied from stsci_python.pytools so that pysynphot can be tested without
an extra dependency.

This module extends the built-in unittest capabilities to facilitate
performing floating point comparisons on scalars and numpy arrays. It also
provides functions that automate building a test suite from all tests
present in the module, and running the tests in standard or debug mode.

To use this module, import it along with unittest [QUESTION: should this
module import everything from unittest into its namespace to make life
even easier?]. Subclass test cases from testutil.FPTestCase instead of
unittest.TestCase. Call testall or debug from this module:

import testutil

class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        assorted_test_setup

    def testone(self):
        self.assertEqual(1,2)

    def testtwo(self):
        self.assertApproxNumpy(arr1,arr2,accuracy=1e-6)

    def tearDown(self):
        assorted_test_teardown

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)

To run the tests in normal mode from the shell, then do the following:
    python my_module.py
It will run all tests, success or failure, and print a summary of the results.

To run the tests in debug mode from the shell, do the following:
    python -i my_module.py debug
    >>> import pdb
    >>> pdb.pm()
In debug mode, it will run until it encounters the first failed test, then
stop. Thus if you run with the -i switch, you can then import pdb and
proceed with the usual debugger commands.

If you prefer to run your tests from within the python interpreter,
you may import this module and call its testall() and debug() functions
explicitly. The modules you are testing must be visible in your sys.path.

>>>import testutil as U
>>> U.testall('ui_test')

"""

from __future__ import division

import math
import unittest
import numpy as N

try:
    from nose.tools import nottest
except ImportError:
    # A noop placeholder
    def nottest(func):
        return func

def skip(func):
    """A decorator to indicate to nose that a test should be skipped."""

    try:
        from nose.plugins.skip import SkipTest
        import functools

        @functools.wraps(func)
        def test_skipped(*args, **kwargs):
            raise SkipTest('Test %s is marked as skipped' % func.__name__)
        return test_skipped
    except ImportError:
        return func


class FPTestCase(unittest.TestCase):
    ''' Base class to hold some functionality related to floating-point
    precision and array comparisons'''

    def assertApproxFP(self, testvalue, expected, accuracy=1.0e-5):
        ''' Floating point comparison  '''
        result = math.fabs((testvalue - expected) / expected)
        self.failUnless(result <= accuracy,"test: %g, ref: %g"%(testvalue,expected))

    def assertApproxNumpy(self, testarray, expected, accuracy=1.0e-5):
        ''' Floating point array comparison '''
        result=N.abs(testarray-expected)/expected
        self.failUnless(N.alltrue(result <= accuracy))

    def assertEqualNumpy(self, testarray, expected):
        ''' Identical FP array comparison '''
        self.failUnless(N.alltrue(testarray == expected))

def buildsuite(module):
    """Builds a test suite containing all tests found in the module.
    Returns the suite."""
    M = __import__(module)
    suite = unittest.defaultTestLoader.loadTestsFromModule(M)
    return suite

def debug(module):
    """ Build the test suite, then run in debug mode, which allows for postmortems"""
    buildsuite(module).debug()

@nottest
def testall(module,verb=0):
    """ Build and run the suite through the testrunner. Verbosity level
    defaults to quiet but can be set to 2 to produce a line as it runs
    each test. A summary of the number of tests run, errors, and failures
    is always printed at the end."""
    result=unittest.TextTestRunner(verbosity=verb).run(buildsuite(module))
    return result
