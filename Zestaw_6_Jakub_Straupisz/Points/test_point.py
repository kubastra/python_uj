import unittest
from points import *

class TestPoints(unittest.TestCase):
    def test_of_print(self):
        self.assertEqual(str(Point(1,2)), "(1, 2)")

    def test_of_repr(self):
        self.assertEqual(repr(Point(1,2)), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(Point(1,2) == Point(1,2))
        self.assertFalse(Point(1,2) == Point(2,3))

    def test_add(self):
        self.assertEqual(Point(1,2) + Point(3,4), Point(4,6))

    def test_sub(self):
        self.assertEqual(Point(5,2) - Point(3,1), Point(2,1))

    def test_mul(self):
        self.assertEqual(Point(1,2) * Point(3,4), 11)

    def test_cross(self):
        self.assertEqual(Point(1,2).cross(Point(3,4)), -2)

    def test_length(self):
        self.assertAlmostEqual(Point(4,3).length(), 5)

if __name__ == '__main__':
    unittest.main()