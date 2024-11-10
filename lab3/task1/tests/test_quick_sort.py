import unittest

from lab3.task1.src.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        array = [2, 3, 9, 2, 2]
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [2, 2, 2, 3, 9])

    def test_should_sort_sorted_array(self):
        # given
        array = [1, 2, 3, 4, 5, 6]
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_should_sort_reverse_sorted_array(self):
        # given
        array = [6, 5, 4, 3, 2, 1]
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_should_sort_single_element_array(self):
        # given
        array = [0]
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [0])

    def test_should_sort_empty_array(self):
        # given
        array = []
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [])

    def test_should_sort_large_numbers_array(self):
        # given
        array = [1000000000, 999999999, 999999998]
        # when
        quick_sort(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [999999998, 999999999, 1000000000])


if __name__ == '__main__':
    unittest.main()
