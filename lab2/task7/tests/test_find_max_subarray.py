import unittest

from lab2.task7.src.find_max_subarray import find_max_subarray


class TestFindMaxSubarray(unittest.TestCase):

    def test_should_find_max_subarray_example_array(self):
        # given
        array = [1, 8, 2, 10]
        # when
        result = find_max_subarray(len(array), array)
        # then
        self.assertEqual(result, [21, [0, 3]])

    def test_should_find_max_subarray_single_element_array(self):
        # given
        array = [1]
        # when
        result = find_max_subarray(len(array), array)
        # then
        self.assertEqual(result, [1, [0, 0]])

    def test_should_find_max_subarray_empty_array(self):
        # given
        array = []
        # when
        result = find_max_subarray(len(array), array)
        # then
        self.assertEqual(result, [0, [0, 0]])


if __name__ == '__main__':
    unittest.main()
