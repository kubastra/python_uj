import unittest
from Polynomial import Polynomial

class TestPolynomial(unittest.TestCase):
    def test_is_zero(self):
        self.assertTrue(Polynomial([0]).is_zero())
        self.assertTrue(Polynomial([0, 0, 0]).is_zero())
        self.assertFalse(Polynomial([0, 1]).is_zero())

    def test_degree(self):
        self.assertEqual(Polynomial([0]).degree(), 0)
        self.assertEqual(Polynomial([1]).degree(), 0)
        self.assertEqual(Polynomial([1, 0, 0]).degree(), 0)
        self.assertEqual(Polynomial([0, 2, 3]).degree(), 2)

    def test_getitem(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p[0], 1)
        self.assertEqual(p[1], 2)
        self.assertEqual(p[2], 3)
        self.assertEqual(p[5], 0)

    def test_addition(self):
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 1])

        r = p + q

        self.assertEqual(r, Polynomial([4, 3, 3]))

    def test_subtraction(self):
        p = Polynomial([5, 4, 3])
        q = Polynomial([2, 1])
        r = p - q
        self.assertEqual(r, Polynomial([3, 3, 3]))

    def test_multiplication(self):
        p = Polynomial([1, 2]) # 1 + 2x
        q = Polynomial([3, 4]) # 3 + 4x
        r = p * q # 3 + 10x + 8x^2
        self.assertEqual(r, Polynomial([3, 10, 8]))

    def test_multiplication_by_zero(self):
        p = Polynomial([1, 2, 3])
        z = Polynomial([0])
        self.assertEqual(p * z, Polynomial([0]))
        self.assertEqual(z * p, Polynomial([0]))

    def test_horner_call(self):
        p = Polynomial([1, 2, 3]) # 1 + 2x + 3x^2
        self.assertEqual(p(0), 1)
        self.assertEqual(p(1), 6)
        self.assertEqual(p(2), 17)

    def test_equality(self):
        p = Polynomial([1, 2, 3])
        q = Polynomial([1, 2, 3, 0, 0])
        self.assertTrue(p == q)
        self.assertFalse(p != q)

    def test_equality_by_difference(self):
        p = Polynomial([1, 2])
        q = Polynomial([1, 2])
        self.assertTrue((p - q).is_zero())
        self.assertTrue(p == q)

    def test_string(self):
        self.assertEqual(str(Polynomial([0])), "0")
        self.assertEqual(str(Polynomial([1])), "1")
        self.assertEqual(str(Polynomial([0, 1])), "x")
        self.assertEqual(str(Polynomial([1, 1])), "1 + x")
        self.assertEqual(str(Polynomial([1, -1])), "1 - x")
        self.assertEqual(str(Polynomial([0, 0, 2])), "2x^2")

    def test_add_number(self):
        p = Polynomial([1, 2])   # 1 + 2x
        self.assertEqual(p + 3, Polynomial([4, 2]))
        self.assertEqual(3 + p, Polynomial([4, 2]))

    def test_sub_number(self):
        p = Polynomial([5, 1])   # 5 + x
        self.assertEqual(p - 2, Polynomial([3, 1]))
        self.assertEqual(2 - p, Polynomial([-3, -1]))

    def test_mul_number(self):
        p = Polynomial([1, -2, 3])
        self.assertEqual(p * 2, Polynomial([2, -4, 6]))
        self.assertEqual(2 * p, Polynomial([2, -4, 6]))

    def test_div_number(self):
        p = Polynomial([2, 4, 6])
        self.assertEqual(p / 2, Polynomial([1, 2, 3]))

if __name__ == "__main__":
    unittest.main()


