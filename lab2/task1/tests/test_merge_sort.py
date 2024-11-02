import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_example(self):
        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 1, 2, 2, 3, 3, 4, 6, 7, 8])

    def test_sorted(self):
        array = [1, 2, 3, 4, 5, 6]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_reverse_sorted(self):
        array = [6, 5, 4, 3, 2, 1]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_single_element(self):
        array = [0]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [0])

    def test_empty_array(self):
        array = []
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [])

    def test_large_numbers(self):
        array = [1000000000, 999999999, 999999998]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [999999998, 999999999, 1000000000])


if __name__ == '__main__':
    unittest.main()
