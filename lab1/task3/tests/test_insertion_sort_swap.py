import unittest
from utils import memory_data, time_data
from lab1.task3.src.insertion_sort_swap import insertion_sort_swap, main


class TestInsertionSortSwap(unittest.TestCase):
    
    def test_should_sort_sorted_array(self):
        # given
        n = 5
        array = [5, 4, 3, 2, 1]
        expected_result = [5, 4, 3, 2, 1]

        # when
        result = insertion_sort_swap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_reverse_sorted_array(self):
        # given
        n = 5
        array = [1, 2, 3, 4, 5]
        expected_result = [5, 4, 3, 2, 1]

        # when
        result = insertion_sort_swap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_example_array(self):
        # given
        n = 6
        array = [31, 41, 59, 26, 41, 58]
        expected_result = [59, 58, 41, 41, 31, 26]

        # when
        result = insertion_sort_swap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_single_element_array(self):
        # given
        n = 1
        array = [22]
        expected_result = [22]

        # when
        result = insertion_sort_swap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = []

        # when
        result = insertion_sort_swap(n, array)

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


if __name__ == "__main__":
    unittest.main()
