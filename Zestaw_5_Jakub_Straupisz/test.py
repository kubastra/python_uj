import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.one = [1, 0]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([-2, 5], [3, 4]), [-3, 10])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([-1, -2]))


    def test_is_zero(self):
        self.assertTrue(is_zero([0, 5]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([3, 4]), 0.75)


if __name__ == '__main__':
    unittest.main()