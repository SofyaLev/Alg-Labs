import unittest

from lab2.task7.src.find_max_subarray import find_max_subarray


class TestFindMaxSubarray(unittest.TestCase):

    def test_should_find_max_subarray_example_array(self):
        # given
        n = 4
        array = [1, 8, 2, 10]
        expected_result = [21, [0, 3]]

        # when
        result = find_max_subarray(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_max_subarray_single_element_array(self):
        # given
        n = 1
        array = [1]
        expected_result = [1, [0, 0]]

        # when
        result = find_max_subarray(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_max_subarray_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = [0, [0, 0]]

        # when
        result = find_max_subarray(n, array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
