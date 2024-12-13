import unittest
from utils import memory_data, time_data
from lab2.task2.src.merge_sort_indexes import merge_sort_indexes, main


class TestMergeSortIndexes(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        n = 4
        array = [9, 7, 5, 8]
        expected_result = [5, 7, 8, 9]

        # when
        result = merge_sort_indexes(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_sorted_array(self):
        # given
        n = 4
        array = [1, 2, 3, 4]
        expected_result = [1, 2, 3, 4]

        # when
        result = merge_sort_indexes(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_reverse_sorted_array(self):
        # given
        n = 4
        array = [10, 9, 8, 7]
        expected_result = [7, 8, 9, 10]

        # when
        result = merge_sort_indexes(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_single_element_array(self):
        # given
        n = 1
        array = [0]
        expected_result = [0]

        # when
        result = merge_sort_indexes(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = []

        # when
        result = merge_sort_indexes(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 256

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == '__main__':
    unittest.main()
