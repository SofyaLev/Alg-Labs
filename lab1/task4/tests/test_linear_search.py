import unittest
from utils import memory_data, time_data
from lab1.task4.src.linear_search import linear_search, main


class TestLinearSearch(unittest.TestCase):

    def test_should_check_element_found(self):
        # given
        array = [1, 2, 3, 4, 5]
        n = 2
        expected_result = [2]

        # when
        result = linear_search(array, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_element_not_found(self):
        # given
        array = [1, 2, 3, 4, 5]
        n = 6
        expected_result = [-1]

        # when
        result = linear_search(array, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_multiple_occurrences(self):
        # given
        array = [1, 2, 2, 3, 4, 5]
        n = 2
        expected_result = (2, [2, 3])

        # when
        result = linear_search(array, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_single_element_found(self):
        # given
        array = [2]
        n = 2
        expected_result = [1]

        # when
        result = linear_search(array, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_single_element_not_found(self):
        # given
        array = [2]
        n = 10
        expected_result = [-1]

        # when
        result = linear_search(array, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_empty_array(self):
        # given
        array = []
        n = 2
        expected_result = [-1]

        # when
        result = linear_search(array, n)

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
