import unittest
from utils import memory_data, time_data
from lab2.task5.src.majority_element import majority_element, main


class TestMajorityElement(unittest.TestCase):

    def test_should_find_majority_element_example1_array(self):
        # given
        array = [2, 3, 9, 2, 2]
        expected_result = 1

        # when
        result = majority_element(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_majority_element_example2_array(self):
        # given
        array = [1, 2, 3, 4]
        expected_result = 0

        # when
        result = majority_element(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_majority_element_single_element_array(self):
        # given
        array = [1]
        expected_result = 1

        # when
        result = majority_element(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_majority_element_empty_array(self):
        # given
        array = []
        expected_result = 0

        # when
        result = majority_element(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_majority_element_equally(self):
        # given
        array = [1, 1, 1, 2, 2, 2]
        expected_result = 0

        # when
        result = majority_element(array)

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
