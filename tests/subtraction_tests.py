import unittest

import numpy
import test_utils

class TestBasicSubtraction(unittest.TestCase):
    # Test basic subtraction of all combinations of all types, not checking for any edge cases specifically.

    ZERO = numpy.float32(0)
    ONE = numpy.float32(1)
    MIN_SUBNORM = numpy.float32(1e-45)
    MAX_SUBNORM = numpy.float32(1.1754942e-38)
    MIN_NORM = numpy.float32(1.1754944e-38)
    MAX_NORM = numpy.float32(3.4028235e38)
    INF = numpy.float32(numpy.inf)
    NAN = numpy.float32(numpy.nan)

    # Initialise the tester object used to run the assembled code.
    @classmethod
    def setUpClass(cls):
        cls.tester = test_utils.SubroutineTester("test_subtraction.s")
        cls.tester.initialise()

    # Run a test to compare the expected difference of two floats to the actual difference.
    def run_test(self, float1: numpy.float32, float2: numpy.float32):
        expected = float1 - float2
        if numpy.isnan(expected):
            self.assertTrue(numpy.isnan(TestBasicSubtraction.tester.run_test(float1, float2)))
        else:
            self.assertEqual(float1 - float2,
                             TestBasicSubtraction.tester.run_test(float1, float2))

    def test_zero(self):
        # Test that ±0 - x = -x for all types of x.
        self.run_test(self.ZERO, self.ZERO)
        self.run_test(self.ZERO, -self.ZERO)
        self.run_test(-self.ZERO, self.ZERO)
        self.run_test(-self.ZERO, -self.ZERO)

        self.run_test(self.ZERO, self.ONE)
        self.run_test(self.ZERO, -self.ONE)
        self.run_test(-self.ZERO, self.ONE)
        self.run_test(-self.ZERO, -self.ONE)

        self.run_test(self.ZERO, self.MIN_SUBNORM)
        self.run_test(self.ZERO, -self.MIN_SUBNORM)
        self.run_test(-self.ZERO, self.MIN_SUBNORM)
        self.run_test(-self.ZERO, -self.MIN_SUBNORM)

        self.run_test(self.ZERO, numpy.float32(9.060464e-39))
        self.run_test(self.ZERO, -numpy.float32(9.060464e-39))
        self.run_test(-self.ZERO, numpy.float32(9.060464e-39))
        self.run_test(-self.ZERO, -numpy.float32(9.060464e-39))

        self.run_test(self.ZERO, self.MAX_SUBNORM)
        self.run_test(self.ZERO, -self.MAX_SUBNORM)
        self.run_test(-self.ZERO, self.MAX_SUBNORM)
        self.run_test(-self.ZERO, -self.MAX_SUBNORM)

        self.run_test(self.ZERO, self.MIN_NORM)
        self.run_test(self.ZERO, -self.MIN_NORM)
        self.run_test(-self.ZERO, self.MIN_NORM)
        self.run_test(-self.ZERO, -self.MIN_NORM)

        self.run_test(self.ZERO, numpy.float32(395.6166))
        self.run_test(self.ZERO, -numpy.float32(395.6166))
        self.run_test(-self.ZERO, numpy.float32(395.6166))
        self.run_test(-self.ZERO, -numpy.float32(395.6166))

        self.run_test(self.ZERO, self.MAX_NORM)
        self.run_test(self.ZERO, -self.MAX_NORM)
        self.run_test(-self.ZERO, self.MAX_NORM)
        self.run_test(-self.ZERO, -self.MAX_NORM)

        self.run_test(self.ZERO, self.INF)
        self.run_test(self.ZERO, -self.INF)
        self.run_test(-self.ZERO, self.INF)
        self.run_test(-self.ZERO, -self.INF)

        self.run_test(self.ZERO, self.NAN)
        self.run_test(-self.ZERO, self.NAN)
    
    def test_one(self):
        # Test ±1 - x for all types of x.
        self.run_test(self.ONE, self.ZERO)
        self.run_test(self.ONE, -self.ZERO)
        self.run_test(-self.ONE, self.ZERO)
        self.run_test(-self.ONE, -self.ZERO)

        self.run_test(self.ONE, self.ONE)
        self.run_test(self.ONE, -self.ONE)
        self.run_test(-self.ONE, self.ONE)
        self.run_test(-self.ONE, -self.ONE)

        self.run_test(self.ONE, self.MIN_SUBNORM)
        self.run_test(self.ONE, -self.MIN_SUBNORM)
        self.run_test(-self.ONE, self.MIN_SUBNORM)
        self.run_test(-self.ONE, -self.MIN_SUBNORM)

        self.run_test(self.ONE, numpy.float32(1.902965e-39))
        self.run_test(self.ONE, -numpy.float32(1.902965e-39))
        self.run_test(-self.ONE, numpy.float32(1.902965e-39))
        self.run_test(-self.ONE, -numpy.float32(1.902965e-39))

        self.run_test(self.ONE, self.MAX_SUBNORM)
        self.run_test(self.ONE, -self.MAX_SUBNORM)
        self.run_test(-self.ONE, self.MAX_SUBNORM)
        self.run_test(-self.ONE, -self.MAX_SUBNORM)

        self.run_test(self.ONE, self.MIN_NORM)
        self.run_test(self.ONE, -self.MIN_NORM)
        self.run_test(-self.ONE, self.MIN_NORM)
        self.run_test(-self.ONE, -self.MIN_NORM)

        self.run_test(self.ONE, numpy.float32(7918.158))
        self.run_test(self.ONE, -numpy.float32(7918.158))
        self.run_test(-self.ONE, numpy.float32(7918.158))
        self.run_test(-self.ONE, -numpy.float32(7918.158))

        self.run_test(self.ONE, self.MAX_NORM)
        self.run_test(self.ONE, -self.MAX_NORM)
        self.run_test(-self.ONE, self.MAX_NORM)
        self.run_test(-self.ONE, -self.MAX_NORM)

        self.run_test(self.ONE, self.INF)
        self.run_test(self.ONE, -self.INF)
        self.run_test(-self.ONE, self.INF)
        self.run_test(-self.ONE, -self.INF)

        self.run_test(self.ONE, self.NAN)
        self.run_test(-self.ONE, self.NAN)

    def test_min_subnorm(self):
        # Test ±MIN_SUBNORM - x for all types of x.
        self.run_test(self.MIN_SUBNORM, self.ZERO)
        self.run_test(self.MIN_SUBNORM, -self.ZERO)
        self.run_test(-self.MIN_SUBNORM, self.ZERO)
        self.run_test(-self.MIN_SUBNORM, -self.ZERO)

        self.run_test(self.MIN_SUBNORM, self.ONE)
        self.run_test(self.MIN_SUBNORM, -self.ONE)
        self.run_test(-self.MIN_SUBNORM, self.ONE)
        self.run_test(-self.MIN_SUBNORM, -self.ONE)

        self.run_test(self.MIN_SUBNORM, self.MIN_SUBNORM)
        self.run_test(self.MIN_SUBNORM, -self.MIN_SUBNORM)
        self.run_test(-self.MIN_SUBNORM, self.MIN_SUBNORM)
        self.run_test(-self.MIN_SUBNORM, -self.MIN_SUBNORM)

        self.run_test(self.MIN_SUBNORM, numpy.float32(6.927885e-39))
        self.run_test(self.MIN_SUBNORM, -numpy.float32(6.927885e-39))
        self.run_test(-self.MIN_SUBNORM, numpy.float32(6.927885e-39))
        self.run_test(-self.MIN_SUBNORM, -numpy.float32(6.927885e-39))

        self.run_test(self.MIN_SUBNORM, self.MAX_SUBNORM)
        self.run_test(self.MIN_SUBNORM, -self.MAX_SUBNORM)
        self.run_test(-self.MIN_SUBNORM, self.MAX_SUBNORM)
        self.run_test(-self.MIN_SUBNORM, -self.MAX_SUBNORM)

        self.run_test(self.MIN_SUBNORM, self.MIN_NORM)
        self.run_test(self.MIN_SUBNORM, -self.MIN_NORM)
        self.run_test(-self.MIN_SUBNORM, self.MIN_NORM)
        self.run_test(-self.MIN_SUBNORM, -self.MIN_NORM)

        self.run_test(self.MIN_SUBNORM, numpy.float32(466603.3))
        self.run_test(self.MIN_SUBNORM, -numpy.float32(466603.3))
        self.run_test(-self.MIN_SUBNORM, numpy.float32(466603.3))
        self.run_test(-self.MIN_SUBNORM, -numpy.float32(466603.3))

        self.run_test(self.MIN_SUBNORM, self.MAX_NORM)
        self.run_test(self.MIN_SUBNORM, -self.MAX_NORM)
        self.run_test(-self.MIN_SUBNORM, self.MAX_NORM)
        self.run_test(-self.MIN_SUBNORM, -self.MAX_NORM)

        self.run_test(self.MIN_SUBNORM, self.INF)
        self.run_test(self.MIN_SUBNORM, -self.INF)
        self.run_test(-self.MIN_SUBNORM, self.INF)
        self.run_test(-self.MIN_SUBNORM, -self.INF)

        self.run_test(self.MIN_SUBNORM, self.NAN)
        self.run_test(-self.MIN_SUBNORM, self.NAN)

    def test_subnorm(self):
        # Test ±x - y for subnormal x and all types of y.
        self.run_test(numpy.float32(7.518523e-39), self.ZERO)
        self.run_test(numpy.float32(7.518523e-39), -self.ZERO)
        self.run_test(-numpy.float32(7.518523e-39), self.ZERO)
        self.run_test(-numpy.float32(7.518523e-39), -self.ZERO)

        self.run_test(numpy.float32(2.028916e-39), self.ONE)
        self.run_test(numpy.float32(2.028916e-39), -self.ONE)
        self.run_test(-numpy.float32(2.028916e-39), self.ONE)
        self.run_test(-numpy.float32(2.028916e-39), -self.ONE)

        self.run_test(numpy.float32(4.042427e-39), self.MIN_SUBNORM)
        self.run_test(numpy.float32(4.042427e-39), -self.MIN_SUBNORM)
        self.run_test(-numpy.float32(4.042427e-39), self.MIN_SUBNORM)
        self.run_test(-numpy.float32(4.042427e-39), -self.MIN_SUBNORM)

        self.run_test(numpy.float32(9.636327e-39), numpy.float32(1.0185049e-38))
        self.run_test(numpy.float32(9.636327e-39), -numpy.float32(1.0185049e-38))
        self.run_test(-numpy.float32(9.636327e-39), numpy.float32(1.0185049e-38))
        self.run_test(-numpy.float32(9.636327e-39), -numpy.float32(1.0185049e-38))

        self.run_test(numpy.float32(1.989006e-39), self.MAX_SUBNORM)
        self.run_test(numpy.float32(1.989006e-39), -self.MAX_SUBNORM)
        self.run_test(-numpy.float32(1.989006e-39), self.MAX_SUBNORM)
        self.run_test(-numpy.float32(1.989006e-39), -self.MAX_SUBNORM)

        self.run_test(numpy.float32(2.952435e-39), self.MIN_NORM)
        self.run_test(numpy.float32(2.952435e-39), -self.MIN_NORM)
        self.run_test(-numpy.float32(2.952435e-39), self.MIN_NORM)
        self.run_test(-numpy.float32(2.952435e-39), -self.MIN_NORM)
        
        self.run_test(numpy.float32(1.154907e-38), numpy.float32(4.0687437e-36))
        self.run_test(numpy.float32(1.154907e-38), -numpy.float32(4.0687437e-36))
        self.run_test(-numpy.float32(1.154907e-38), numpy.float32(4.0687437e-36))
        self.run_test(-numpy.float32(1.154907e-38), -numpy.float32(4.0687437e-36))

        self.run_test(numpy.float32(9.79494e-39), self.MAX_NORM)
        self.run_test(numpy.float32(9.79494e-39), -self.MAX_NORM)
        self.run_test(-numpy.float32(9.79494e-39), self.MAX_NORM)
        self.run_test(-numpy.float32(9.79494e-39), -self.MAX_NORM)

        self.run_test(numpy.float32(1.54569e-39), self.INF)
        self.run_test(numpy.float32(1.54569e-39), -self.INF)
        self.run_test(-numpy.float32(1.54569e-39), self.INF)
        self.run_test(-numpy.float32(1.54569e-39), -self.INF)

        self.run_test(numpy.float32(3.974073e-39), self.NAN)
        self.run_test(-numpy.float32(3.974073e-39), self.NAN)

    def test_max_subnorm(self):
        # Test ±MAX_SUBNORM - x for all types of x.
        self.run_test(self.MAX_SUBNORM, self.ZERO)
        self.run_test(self.MAX_SUBNORM, -self.ZERO)
        self.run_test(-self.MAX_SUBNORM, self.ZERO)
        self.run_test(-self.MAX_SUBNORM, -self.ZERO)

        self.run_test(self.MAX_SUBNORM, self.ONE)
        self.run_test(self.MAX_SUBNORM, -self.ONE)
        self.run_test(-self.MAX_SUBNORM, self.ONE)
        self.run_test(-self.MAX_SUBNORM, -self.ONE)

        self.run_test(self.MAX_SUBNORM, self.MIN_SUBNORM)
        self.run_test(self.MAX_SUBNORM, -self.MIN_SUBNORM)
        self.run_test(-self.MAX_SUBNORM, self.MIN_SUBNORM)
        self.run_test(-self.MAX_SUBNORM, -self.MIN_SUBNORM)

        self.run_test(self.MAX_SUBNORM, numpy.float32(2.736488e-39))
        self.run_test(self.MAX_SUBNORM, -numpy.float32(2.736488e-39))
        self.run_test(-self.MAX_SUBNORM, numpy.float32(2.736488e-39))
        self.run_test(-self.MAX_SUBNORM, -numpy.float32(2.736488e-39))

        self.run_test(self.MAX_SUBNORM, self.MAX_SUBNORM)
        self.run_test(self.MAX_SUBNORM, -self.MAX_SUBNORM)
        self.run_test(-self.MAX_SUBNORM, self.MAX_SUBNORM)
        self.run_test(-self.MAX_SUBNORM, -self.MAX_SUBNORM)

        self.run_test(self.MAX_SUBNORM, self.MIN_NORM)
        self.run_test(self.MAX_SUBNORM, -self.MIN_NORM)
        self.run_test(-self.MAX_SUBNORM, self.MIN_NORM)
        self.run_test(-self.MAX_SUBNORM, -self.MIN_NORM)

        self.run_test(self.MAX_SUBNORM, numpy.float32(8.027242e-35))
        self.run_test(self.MAX_SUBNORM, -numpy.float32(8.027242e-35))
        self.run_test(-self.MAX_SUBNORM, numpy.float32(8.027242e-35))
        self.run_test(-self.MAX_SUBNORM, -numpy.float32(8.027242e-35))

        self.run_test(self.MAX_SUBNORM, self.MAX_NORM)
        self.run_test(self.MAX_SUBNORM, -self.MAX_NORM)
        self.run_test(-self.MAX_SUBNORM, self.MAX_NORM)
        self.run_test(-self.MAX_SUBNORM, -self.MAX_NORM)

        self.run_test(self.MAX_SUBNORM, self.INF)
        self.run_test(self.MAX_SUBNORM, -self.INF)
        self.run_test(-self.MAX_SUBNORM, self.INF)
        self.run_test(-self.MAX_SUBNORM, -self.INF)

        self.run_test(self.MAX_SUBNORM, self.NAN)
        self.run_test(-self.MAX_SUBNORM, self.NAN)

    def test_min_norm(self):
        # Test ±MIN_NORM - x for all types of x.
        self.run_test(self.MIN_NORM, self.ZERO)
        self.run_test(self.MIN_NORM, -self.ZERO)
        self.run_test(-self.MIN_NORM, self.ZERO)
        self.run_test(-self.MIN_NORM, -self.ZERO)

        self.run_test(self.MIN_NORM, self.ONE)
        self.run_test(self.MIN_NORM, -self.ONE)
        self.run_test(-self.MIN_NORM, self.ONE)
        self.run_test(-self.MIN_NORM, -self.ONE)

        self.run_test(self.MIN_NORM, self.MIN_SUBNORM)
        self.run_test(self.MIN_NORM, -self.MIN_SUBNORM)
        self.run_test(-self.MIN_NORM, self.MIN_SUBNORM)
        self.run_test(-self.MIN_NORM, -self.MIN_SUBNORM)

        self.run_test(self.MIN_NORM, numpy.float32(7.235862e-39))
        self.run_test(self.MIN_NORM, -numpy.float32(7.235862e-39))
        self.run_test(-self.MIN_NORM, numpy.float32(7.235862e-39))
        self.run_test(-self.MIN_NORM, -numpy.float32(7.235862e-39))

        self.run_test(self.MIN_NORM, self.MAX_SUBNORM)
        self.run_test(self.MIN_NORM, -self.MAX_SUBNORM)
        self.run_test(-self.MIN_NORM, self.MAX_SUBNORM)
        self.run_test(-self.MIN_NORM, -self.MAX_SUBNORM)

        self.run_test(self.MIN_NORM, self.MIN_NORM)
        self.run_test(self.MIN_NORM, -self.MIN_NORM)
        self.run_test(-self.MIN_NORM, self.MIN_NORM)
        self.run_test(-self.MIN_NORM, -self.MIN_NORM)

        self.run_test(self.MIN_NORM, numpy.float32(3.0655702e-37))
        self.run_test(self.MIN_NORM, -numpy.float32(3.0655702e-37))
        self.run_test(-self.MIN_NORM, numpy.float32(3.0655702e-37))
        self.run_test(-self.MIN_NORM, -numpy.float32(3.0655702e-37))

        self.run_test(self.MIN_NORM, self.MAX_NORM)
        self.run_test(self.MIN_NORM, -self.MAX_NORM)
        self.run_test(-self.MIN_NORM, self.MAX_NORM)
        self.run_test(-self.MIN_NORM, -self.MAX_NORM)

        self.run_test(self.MIN_NORM, self.INF)
        self.run_test(self.MIN_NORM, -self.INF)
        self.run_test(-self.MIN_NORM, self.INF)
        self.run_test(-self.MIN_NORM, -self.INF)

        self.run_test(self.MIN_NORM, self.NAN)
        self.run_test(-self.MIN_NORM, self.NAN)

    def test_norm(self):
        # Test ±x - y for normal x and all types of y.
        self.run_test(numpy.float32(3.2528998e8), self.ZERO)
        self.run_test(numpy.float32(3.2528998e8), -self.ZERO)
        self.run_test(-numpy.float32(3.2528998e8), self.ZERO)
        self.run_test(-numpy.float32(3.2528998e8), -self.ZERO)

        self.run_test(numpy.float32(5781.5137), self.ONE)
        self.run_test(numpy.float32(5781.5137), -self.ONE)
        self.run_test(-numpy.float32(5781.5137), self.ONE)
        self.run_test(-numpy.float32(5781.5137), -self.ONE)

        self.run_test(numpy.float32(4.0233208e-35), self.MIN_SUBNORM)
        self.run_test(numpy.float32(4.0233208e-35), -self.MIN_SUBNORM)
        self.run_test(-numpy.float32(4.0233208e-35), self.MIN_SUBNORM)
        self.run_test(-numpy.float32(4.0233208e-35), -self.MIN_SUBNORM)

        self.run_test(numpy.float32(3.4244755e-37), numpy.float32(7.951416e-39))
        self.run_test(numpy.float32(3.4244755e-37), -numpy.float32(7.951416e-39))
        self.run_test(-numpy.float32(3.4244755e-37), numpy.float32(7.951416e-39))
        self.run_test(-numpy.float32(3.4244755e-37), -numpy.float32(7.951416e-39))

        self.run_test(numpy.float32(1.772688e-35), self.MAX_SUBNORM)
        self.run_test(numpy.float32(1.772688e-35), -self.MAX_SUBNORM)
        self.run_test(-numpy.float32(1.772688e-35), self.MAX_SUBNORM)
        self.run_test(-numpy.float32(1.772688e-35), -self.MAX_SUBNORM)

        self.run_test(numpy.float32(9.7266296e-36), self.MIN_NORM)
        self.run_test(numpy.float32(9.7266296e-36), -self.MIN_NORM)
        self.run_test(-numpy.float32(9.7266296e-36), self.MIN_NORM)
        self.run_test(-numpy.float32(9.7266296e-36), -self.MIN_NORM)

        self.run_test(numpy.float32(9.964942e17), numpy.float32(3.0321312e16))
        self.run_test(numpy.float32(9.964942e17), -numpy.float32(3.0321312e16))
        self.run_test(-numpy.float32(9.964942e17), numpy.float32(3.0321312e16))
        self.run_test(-numpy.float32(9.964942e17), -numpy.float32(3.0321312e16))

        self.run_test(numpy.float32(3.3541464e35), self.MAX_NORM)
        self.run_test(numpy.float32(3.3541464e35), -self.MAX_NORM)
        self.run_test(-numpy.float32(3.3541464e35), self.MAX_NORM)
        self.run_test(-numpy.float32(3.3541464e35), -self.MAX_NORM)

        self.run_test(numpy.float32(1.8177568e25), self.INF)
        self.run_test(numpy.float32(1.8177568e25), -self.INF)
        self.run_test(-numpy.float32(1.8177568e25), self.INF)
        self.run_test(-numpy.float32(1.8177568e25), -self.INF)

        self.run_test(numpy.float32(2.2122593e-30), self.NAN)
        self.run_test(-numpy.float32(2.2122593e-30), self.NAN)

    def test_max_norm(self):
        # Test ±MAX_NORM - x for all types of x.
        self.run_test(self.MAX_NORM, self.ZERO)
        self.run_test(self.MAX_NORM, -self.ZERO)
        self.run_test(-self.MAX_NORM, self.ZERO)
        self.run_test(-self.MAX_NORM, -self.ZERO)

        self.run_test(self.MAX_NORM, self.ONE)
        self.run_test(self.MAX_NORM, -self.ONE)
        self.run_test(-self.MAX_NORM, self.ONE)
        self.run_test(-self.MAX_NORM, -self.ONE)

        self.run_test(self.MAX_NORM, self.MIN_SUBNORM)
        self.run_test(self.MAX_NORM, -self.MIN_SUBNORM)
        self.run_test(-self.MAX_NORM, self.MIN_SUBNORM)
        self.run_test(-self.MAX_NORM, -self.MIN_SUBNORM)

        self.run_test(self.MAX_NORM, numpy.float32(6.985955e-39))
        self.run_test(self.MAX_NORM, -numpy.float32(6.985955e-39))
        self.run_test(-self.MAX_NORM, numpy.float32(6.985955e-39))
        self.run_test(-self.MAX_NORM, -numpy.float32(6.985955e-39))

        self.run_test(self.MAX_NORM, self.MAX_SUBNORM)
        self.run_test(self.MAX_NORM, -self.MAX_SUBNORM)
        self.run_test(-self.MAX_NORM, self.MAX_SUBNORM)
        self.run_test(-self.MAX_NORM, -self.MAX_SUBNORM)

        self.run_test(self.MAX_NORM, self.MIN_NORM)
        self.run_test(self.MAX_NORM, -self.MIN_NORM)
        self.run_test(-self.MAX_NORM, self.MIN_NORM)
        self.run_test(-self.MAX_NORM, -self.MIN_NORM)

        self.run_test(self.MAX_NORM, numpy.float32(5.0028173e34))
        self.run_test(self.MAX_NORM, -numpy.float32(5.0028173e34))
        self.run_test(-self.MAX_NORM, numpy.float32(5.0028173e34))
        self.run_test(-self.MAX_NORM, -numpy.float32(5.0028173e34))

        self.run_test(self.MAX_NORM, self.MAX_NORM)
        self.run_test(self.MAX_NORM, -self.MAX_NORM)
        self.run_test(-self.MAX_NORM, self.MAX_NORM)
        self.run_test(-self.MAX_NORM, -self.MAX_NORM)

        self.run_test(self.MAX_NORM, self.INF)
        self.run_test(self.MAX_NORM, -self.INF)
        self.run_test(-self.MAX_NORM, self.INF)
        self.run_test(-self.MAX_NORM, -self.INF)

        self.run_test(self.MAX_NORM, self.NAN)
        self.run_test(-self.MAX_NORM, self.NAN)

    def test_infinity(self):
        # Test ±∞ - x for all types of x.
        self.run_test(self.INF, self.ZERO)
        self.run_test(self.INF, -self.ZERO)
        self.run_test(-self.INF, self.ZERO)
        self.run_test(-self.INF, -self.ZERO)

        self.run_test(self.INF, self.ONE)
        self.run_test(self.INF, -self.ONE)
        self.run_test(-self.INF, self.ONE)
        self.run_test(-self.INF, -self.ONE)

        self.run_test(self.INF, self.MIN_SUBNORM)
        self.run_test(self.INF, -self.MIN_SUBNORM)
        self.run_test(-self.INF, self.MIN_SUBNORM)
        self.run_test(-self.INF, -self.MIN_SUBNORM)

        self.run_test(self.INF, numpy.float32(5.804845e-39))
        self.run_test(self.INF, -numpy.float32(5.804845e-39))
        self.run_test(-self.INF, numpy.float32(5.804845e-39))
        self.run_test(-self.INF, -numpy.float32(5.804845e-39))

        self.run_test(self.INF, self.MAX_SUBNORM)
        self.run_test(self.INF, -self.MAX_SUBNORM)
        self.run_test(-self.INF, self.MAX_SUBNORM)
        self.run_test(-self.INF, -self.MAX_SUBNORM)

        self.run_test(self.INF, self.MIN_NORM)
        self.run_test(self.INF, -self.MIN_NORM)
        self.run_test(-self.INF, self.MIN_NORM)
        self.run_test(-self.INF, -self.MIN_NORM)

        self.run_test(self.INF, numpy.float32(2.0581173e8))
        self.run_test(self.INF, -numpy.float32(2.0581173e8))
        self.run_test(-self.INF, numpy.float32(2.0581173e8))
        self.run_test(-self.INF, -numpy.float32(2.0581173e8))

        self.run_test(self.INF, self.MAX_NORM)
        self.run_test(self.INF, -self.MAX_NORM)
        self.run_test(-self.INF, self.MAX_NORM)
        self.run_test(-self.INF, -self.MAX_NORM)

        self.run_test(self.INF, self.INF)
        self.run_test(self.INF, -self.INF)
        self.run_test(-self.INF, self.INF)
        self.run_test(-self.INF, -self.INF)

        self.run_test(self.INF, self.NAN)
        self.run_test(-self.INF, self.NAN)

    def test_nan(self):
        # Test ±NaN - x for all types of x.
        self.run_test(self.NAN, self.ZERO)
        self.run_test(self.NAN, -self.ZERO)

        self.run_test(self.NAN, self.ONE)
        self.run_test(self.NAN, -self.ONE)

        self.run_test(self.NAN, self.MIN_SUBNORM)
        self.run_test(self.NAN, -self.MIN_SUBNORM)

        self.run_test(self.NAN, numpy.float32(1.0764164e-38))
        self.run_test(self.NAN, -numpy.float32(1.0764164e-38))

        self.run_test(self.NAN, self.MAX_SUBNORM)
        self.run_test(self.NAN, -self.MAX_SUBNORM)

        self.run_test(self.NAN, self.MIN_NORM)
        self.run_test(self.NAN, -self.MIN_NORM)

        self.run_test(self.NAN, numpy.float32(2.0617456e23))
        self.run_test(self.NAN, -numpy.float32(2.0617456e23))

        self.run_test(self.NAN, self.MAX_NORM)
        self.run_test(self.NAN, -self.MAX_NORM)

        self.run_test(self.NAN, self.INF)
        self.run_test(self.NAN, -self.INF)

        self.run_test(self.NAN, self.NAN)

class TestNearBaseSubtraction(unittest.TestCase):
    # Test subtraction of floats separated by a minimal Hamming distance.

    ZERO = numpy.float32(0)
    ONE = numpy.float32(1)
    MIN_SUBNORM = numpy.float32(1e-45)
    MAX_SUBNORM = numpy.float32(1.1754942e-38)
    MIN_NORM = numpy.float32(1.1754944e-38)
    MAX_NORM = numpy.float32(3.4028235e38)

    # Initialise the tester object used to run the assembled code.
    @classmethod
    def setUpClass(cls):
        cls.tester = test_utils.SubroutineTester("test_subtraction.s")
        cls.tester.initialise()

    # Run a test by flipping one bit of the second float's mantissa and testing that the difference is correct.
    def run_test(self, float1: numpy.float32, float2: numpy.float32, flip_bit: int):
        # The code to flip one bit of the second float is kind of a mess.
        float2 = numpy.frombuffer(bytes(map(lambda a, b: a ^ b, numpy.float32.tobytes(float2), numpy.int32.tobytes(numpy.int32(1 << flip_bit)))), dtype=numpy.float32)[0]
        # After flipping a bit, proceed as normal.
        expected = float1 - float2
        if numpy.isnan(expected):
            self.assertTrue(numpy.isnan(TestNearBaseSubtraction.tester.run_test(float1, float2)))
        else:
            self.assertEqual(expected,
                             TestNearBaseSubtraction.tester.run_test(float1, float2))

    def test_zero(self):
        for flip_bit in range(23):
            self.run_test(self.ZERO, self.ZERO, flip_bit)
            self.run_test(self.ZERO, -self.ZERO, flip_bit)
            self.run_test(-self.ZERO, self.ZERO, flip_bit)
            self.run_test(-self.ZERO, -self.ZERO, flip_bit)

            self.run_test(self.ZERO, self.ONE, flip_bit)
            self.run_test(self.ZERO, -self.ONE, flip_bit)
            self.run_test(-self.ZERO, self.ONE, flip_bit)
            self.run_test(-self.ZERO, -self.ONE, flip_bit)

            self.run_test(self.ZERO, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.ZERO, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.ZERO, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.ZERO, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.ZERO, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.ZERO, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.ZERO, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.ZERO, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.ZERO, self.MIN_NORM, flip_bit)
            self.run_test(self.ZERO, -self.MIN_NORM, flip_bit)
            self.run_test(-self.ZERO, self.MIN_NORM, flip_bit)
            self.run_test(-self.ZERO, -self.MIN_NORM, flip_bit)

            self.run_test(self.ZERO, self.MAX_NORM, flip_bit)
            self.run_test(self.ZERO, -self.MAX_NORM, flip_bit)
            self.run_test(-self.ZERO, self.MAX_NORM, flip_bit)
            self.run_test(-self.ZERO, -self.MAX_NORM, flip_bit)

    def test_one(self):
        for flip_bit in range(23):
            self.run_test(self.ONE, self.ZERO, flip_bit)
            self.run_test(self.ONE, -self.ZERO, flip_bit)
            self.run_test(-self.ONE, self.ZERO, flip_bit)
            self.run_test(-self.ONE, -self.ZERO, flip_bit)

            self.run_test(self.ONE, self.ONE, flip_bit)
            self.run_test(self.ONE, -self.ONE, flip_bit)
            self.run_test(-self.ONE, self.ONE, flip_bit)
            self.run_test(-self.ONE, -self.ONE, flip_bit)

            self.run_test(self.ONE, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.ONE, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.ONE, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.ONE, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.ONE, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.ONE, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.ONE, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.ONE, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.ONE, self.MIN_NORM, flip_bit)
            self.run_test(self.ONE, -self.MIN_NORM, flip_bit)
            self.run_test(-self.ONE, self.MIN_NORM, flip_bit)
            self.run_test(-self.ONE, -self.MIN_NORM, flip_bit)

            self.run_test(self.ONE, self.MAX_NORM, flip_bit)
            self.run_test(self.ONE, -self.MAX_NORM, flip_bit)
            self.run_test(-self.ONE, self.MAX_NORM, flip_bit)
            self.run_test(-self.ONE, -self.MAX_NORM, flip_bit)

    def test_min_subnorm(self):
        for flip_bit in range(23):
            self.run_test(self.MIN_SUBNORM, self.ZERO, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.ZERO, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.ZERO, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.ZERO, flip_bit)

            self.run_test(self.MIN_SUBNORM, self.ONE, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.ONE, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.ONE, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.ONE, flip_bit)

            self.run_test(self.MIN_SUBNORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.MIN_SUBNORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.MIN_SUBNORM, self.MIN_NORM, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.MIN_NORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.MIN_NORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.MIN_NORM, flip_bit)

            self.run_test(self.MIN_SUBNORM, self.MAX_NORM, flip_bit)
            self.run_test(self.MIN_SUBNORM, -self.MAX_NORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, self.MAX_NORM, flip_bit)
            self.run_test(-self.MIN_SUBNORM, -self.MAX_NORM, flip_bit)

    def test_max_subnorm(self):
        for flip_bit in range(23):
            self.run_test(self.MAX_SUBNORM, self.ZERO, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.ZERO, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.ZERO, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.ZERO, flip_bit)

            self.run_test(self.MAX_SUBNORM, self.ONE, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.ONE, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.ONE, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.ONE, flip_bit)

            self.run_test(self.MAX_SUBNORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.MAX_SUBNORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.MAX_SUBNORM, self.MIN_NORM, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.MIN_NORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.MIN_NORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.MIN_NORM, flip_bit)

            self.run_test(self.MAX_SUBNORM, self.MAX_NORM, flip_bit)
            self.run_test(self.MAX_SUBNORM, -self.MAX_NORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, self.MAX_NORM, flip_bit)
            self.run_test(-self.MAX_SUBNORM, -self.MAX_NORM, flip_bit)

    def test_min_norm(self):
        for flip_bit in range(23):
            self.run_test(self.MIN_NORM, self.ZERO, flip_bit)
            self.run_test(self.MIN_NORM, -self.ZERO, flip_bit)
            self.run_test(-self.MIN_NORM, self.ZERO, flip_bit)
            self.run_test(-self.MIN_NORM, -self.ZERO, flip_bit)

            self.run_test(self.MIN_NORM, self.ONE, flip_bit)
            self.run_test(self.MIN_NORM, -self.ONE, flip_bit)
            self.run_test(-self.MIN_NORM, self.ONE, flip_bit)
            self.run_test(-self.MIN_NORM, -self.ONE, flip_bit)

            self.run_test(self.MIN_NORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.MIN_NORM, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MIN_NORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MIN_NORM, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.MIN_NORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.MIN_NORM, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MIN_NORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MIN_NORM, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.MIN_NORM, self.MIN_NORM, flip_bit)
            self.run_test(self.MIN_NORM, -self.MIN_NORM, flip_bit)
            self.run_test(-self.MIN_NORM, self.MIN_NORM, flip_bit)
            self.run_test(-self.MIN_NORM, -self.MIN_NORM, flip_bit)

            self.run_test(self.MIN_NORM, self.MAX_NORM, flip_bit)
            self.run_test(self.MIN_NORM, -self.MAX_NORM, flip_bit)
            self.run_test(-self.MIN_NORM, self.MAX_NORM, flip_bit)
            self.run_test(-self.MIN_NORM, -self.MAX_NORM, flip_bit)

    def test_max_norm(self):
        for flip_bit in range(23):
            self.run_test(self.MAX_NORM, self.ZERO, flip_bit)
            self.run_test(self.MAX_NORM, -self.ZERO, flip_bit)
            self.run_test(-self.MAX_NORM, self.ZERO, flip_bit)
            self.run_test(-self.MAX_NORM, -self.ZERO, flip_bit)

            self.run_test(self.MAX_NORM, self.ONE, flip_bit)
            self.run_test(self.MAX_NORM, -self.ONE, flip_bit)
            self.run_test(-self.MAX_NORM, self.ONE, flip_bit)
            self.run_test(-self.MAX_NORM, -self.ONE, flip_bit)

            self.run_test(self.MAX_NORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(self.MAX_NORM, -self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MAX_NORM, self.MIN_SUBNORM, flip_bit)
            self.run_test(-self.MAX_NORM, -self.MIN_SUBNORM, flip_bit)

            self.run_test(self.MAX_NORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(self.MAX_NORM, -self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MAX_NORM, self.MAX_SUBNORM, flip_bit)
            self.run_test(-self.MAX_NORM, -self.MAX_SUBNORM, flip_bit)

            self.run_test(self.MAX_NORM, self.MIN_NORM, flip_bit)
            self.run_test(self.MAX_NORM, -self.MIN_NORM, flip_bit)
            self.run_test(-self.MAX_NORM, self.MIN_NORM, flip_bit)
            self.run_test(-self.MAX_NORM, -self.MIN_NORM, flip_bit)

            self.run_test(self.MAX_NORM, self.MAX_NORM, flip_bit)
            self.run_test(self.MAX_NORM, -self.MAX_NORM, flip_bit)
            self.run_test(-self.MAX_NORM, self.MAX_NORM, flip_bit)
            self.run_test(-self.MAX_NORM, -self.MAX_NORM, flip_bit)

if __name__ == "__main__":
    numpy.seterr(over="ignore", invalid="ignore")
    unittest.main()