import unittest

from lab2.task5.src.majority_element import majority_element


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


if __name__ == '__main__':
    unittest.main()
