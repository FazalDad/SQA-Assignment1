import unittest
from list import SortedList


class TestList(unittest.TestCase):

    # Ran before each test
    def setUp(self):
        self.test_list = SortedList()  # List sorted in ascending order

        self.test_list.insert(4)
        self.test_list.insert(16)
        self.test_list.insert(8)
        self.test_list.insert(-2)

    def test_is_empty(self):
        self.assertEqual(self.test_list.is_empty(), False)

    def test_insert(self):
        self.assertEqual(self.test_list.insert(100), 4)

    def test_pop_smallest(self):
        self.assertEqual(self.test_list.head(), self.test_list.pop_smallest())

    def test_pop_highest(self):
        self.assertEqual(self.test_list.tail(), self.test_list.pop_highest())

    def test_get_length(self):
        self.assertEqual(self.test_list.length, 4)


if __name__ == "__main__":
    unittest.main()
