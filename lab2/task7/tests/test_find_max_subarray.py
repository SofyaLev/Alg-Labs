import unittest

from lab2.task7.src.find_max_subarray import find_max_subarray


class TestFindMaxSubarray(unittest.TestCase):

    def test_should_find_max_subarray_example_array(self):
        array = [1, 8, 2, 10]
        self.assertEqual(find_max_subarray(len(array), array), [21, [0, 3]])

    def test_should_find_max_subarray_single_element_array(self):
        array = [1]
        self.assertEqual(find_max_subarray(len(array), array), [1, [0, 0]])

    def test_should_find_max_subarray_empty_array(self):
        array = []
        self.assertEqual(find_max_subarray(len(array), array), [0, [0, 0]])


if __name__ == '__main__':
    unittest.main()
