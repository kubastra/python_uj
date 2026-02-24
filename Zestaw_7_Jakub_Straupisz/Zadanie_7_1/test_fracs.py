
import unittest
from fracs import Frac

class TestFrac(unittest.TestCase):
    def test_str_repr(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(3)), "3")
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_sub(self):
        self.assertEqual(Frac(3, 4) - Frac(1, 4), Frac(1, 2))
        self.assertEqual(Frac(3, 4) - 1, Frac(-1, 4))
        self.assertEqual(1 - Frac(1, 4), Frac(3, 4))

    def test_mul(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(2, 3) * 3, Frac(2, 1))
        self.assertEqual(3 * Frac(1, 6), Frac(1, 2))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(1, 2) / 2, Frac(1, 4))
        self.assertEqual(2 / Frac(1, 4), Frac(8, 1))
        with self.assertRaises(ValueError):
            Frac(1, 2) / Frac(0, 1)

    def test_comparisons(self):
        self.assertTrue(Frac(1, 2) < Frac(2, 3))
        self.assertTrue(Frac(3, 2) > Frac(1, 1))
        self.assertTrue(Frac(1, 2) <= Frac(1, 2))
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertTrue(Frac(3, 4) != Frac(2, 3))

    def test_unary_ops(self):
        self.assertEqual(+Frac(1, 3), Frac(1, 3))
        self.assertEqual(-Frac(1, 3), Frac(-1, 3))
        self.assertEqual(~Frac(2, 5), Frac(5, 2))
        with self.assertRaises(ValueError):
            ~Frac(0)

    def test_float_support(self):
        self.assertEqual(Frac(0.5), Frac(1, 2))
        self.assertEqual(Frac(1, 2) + 0.25, Frac(3, 4))
        self.assertEqual(Frac(1.5) * 2, Frac(3, 1))

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)


if __name__ == "__main__":
    unittest.main()