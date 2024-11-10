import unittest

from lab3.task1.src.randomized_quick_sort_p3 import randomized_quick_sort_p3


class TestRandomizedQuickSortP3(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        array = [2, 3, 9, 2, 2]
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [2, 2, 2, 3, 9])

    def test_should_sort_sorted_array(self):
        # given
        array = [1, 2, 3, 4, 5, 6]
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_should_sort_reverse_sorted_array(self):
        # given
        array = [6, 5, 4, 3, 2, 1]
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [1, 2, 3, 4, 5, 6])

    def test_should_sort_single_element_array(self):
        # given
        array = [0]
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [0])

    def test_should_sort_empty_array(self):
        # given
        array = []
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [])

    def test_should_sort_large_numbers_array(self):
        # given
        array = [1000000000, 999999999, 999999998]
        # when
        randomized_quick_sort_p3(array, 0, len(array) - 1)
        # then
        self.assertEqual(array, [999999998, 999999999, 1000000000])


if __name__ == '__main__':
    unittest.main()
