import unittest
from utils import memory_data, time_data
from lab2.task4.src.binary_search import search_elements, main


class TestBinarySearch(unittest.TestCase):

    def test_should_binary_search_example_array(self):
        # given
        array = [1, 5, 8, 12, 13]
        targets = [8, 1, 23, 1, 11]
        expected_result = [2, 0, -1, 0, -1]

        # when
        result = search_elements(array, targets)

        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search_target_is_not_found(self):
        # given
        array = [1, 2, 3, 4, 5]
        targets = [8]
        expected_result = [-1]

        # when
        result = search_elements(array, targets)

        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search_empty_array(self):
        # given
        array = []
        targets = [8]
        expected_result = [-1]

        # when
        result = search_elements(array, targets)

        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search_single_element_is_found(self):
        # given
        array = [8]
        targets = [8]
        expected_result = [0]

        # when
        result = search_elements(array, targets)

        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search_single_element_not_found(self):
        # given
        array = [0]
        targets = [8]
        expected_result = [-1]

        # when
        result = search_elements(array, targets)

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
