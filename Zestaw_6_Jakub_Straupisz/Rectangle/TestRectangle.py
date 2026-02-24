import unittest
from points import Point
from Rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(1, 2, 5, 7)
        self.assertEqual(str(r), "[(1, 2), (5, 7)]")

    def test_repr(self):
        r = Rectangle(1, 2, 5, 7)
        self.assertEqual(repr(r), "Rectangle(1, 2, 5, 7)")

    def test_eq(self):
        r1 = Rectangle(1, 2, 5, 7)
        r2 = Rectangle(1, 2, 5, 7)
        r3 = Rectangle(0, 0, 1, 1)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)
        self.assertTrue(r1 != r3)

    def test_center(self):
        r = Rectangle(0, 0, 4, 6)
        c = r.center()
        self.assertEqual(c, Point(2, 3))

    def test_area(self):
        r = Rectangle(1, 2, 5, 7)
        self.assertEqual(r.area(), 20)

    def test_move(self):
        r = Rectangle(1, 2, 5, 7)
        r.move(3, -1)
        self.assertEqual(r.pt1, Point(4, 1))
        self.assertEqual(r.pt2, Point(8, 6))

if __name__ == "__main__":
    unittest.main()
