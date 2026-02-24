import unittest
from SingleList import SingleList, Node

class TestSingleList(unittest.TestCase):

    def test_search(self):
        l = SingleList()
        l.push_front(3)
        l.push_front(2)
        l.push_front(1)

        n = l.search(2)
        self.assertEqual(n.data, 2)

        n2 = l.search(10)
        self.assertIsNone(n2)

    def test_min(self):
        l = SingleList()
        l.push_front(5)
        l.push_front(2)
        l.push_front(8)

        n = l.min()
        self.assertEqual(n.data, 2)

    def test_min_empty(self):
        l = SingleList()
        self.assertIsNone(l.min())

    def test_find_max(self):
        l = SingleList()
        l.push_front(5)
        l.push_front(2)
        l.push_front(8)

        n = l.find_max()
        self.assertEqual(n.data, 8)

    def test_find_max_empty(self):
        l = SingleList()
        self.assertIsNone(l.find_max())

    def test_reverse(self):
        l = SingleList()
        l.push_front(3)
        l.push_front(2)
        l.push_front(1)

        l.reverse()

        self.assertEqual(l.head.data, 3)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next.data, 1)
        self.assertIsNone(l.head.next.next.next)


if __name__ == "__main__":
    unittest.main()