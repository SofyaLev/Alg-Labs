import unittest
from utils import memory_data, time_data
from lab2.task1.src.merge_sort import merge_sort, main
from utils import generate_random_array


class TestMergeSort(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        n = 10
        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_result = [1, 1, 2, 2, 3, 3, 4, 6, 7, 8]

        # when
        result = merge_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_sorted_array(self):
        # given
        n = 6
        array = [1, 2, 3, 4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = merge_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_reverse_sorted_array(self):
        # given
        n = 6
        array = [6, 5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = merge_sort(array, 0, len(array) - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_single_element_array(self):
        # given
        n = 1
        array = [0]
        expected_result = [0]

        # when
        result = merge_sort(array, 0, len(array) - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_large_numbers_array(self):
        # given
        n = 10 ** 5
        array = generate_random_array(n, -10 ** 9, 10 ** 9)
        expected_result = sorted(array)

        # when
        result = merge_sort(array, 0, n - 1)

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
