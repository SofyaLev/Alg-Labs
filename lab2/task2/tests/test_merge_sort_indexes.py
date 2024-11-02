import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort_indexes import merge_sort_indexes


class TestMergeSortIndexes(unittest.TestCase):

    def test_example(self):
        array = [9, 7, 5, 8]
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [5, 7, 8, 9])

    def test_sorted(self):
        array = [1, 2, 3, 4]
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4])

    def test_reverse_sorted(self):
        array = [10, 9, 8, 7]
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [7, 8, 9, 10])

    def test_single_element(self):
        array = [0]
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [0])

    def test_empty_array(self):
        array = []
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [])

    def test_large_numbers(self):
        array = [1000000000, 999999999, 999999998]
        merge_sort_indexes(array, 0, len(array) - 1)
        self.assertEqual(array, [999999998, 999999999, 1000000000])


if __name__ == '__main__':
    unittest.main()
