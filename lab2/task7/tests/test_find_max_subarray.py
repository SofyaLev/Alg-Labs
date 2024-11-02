import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from find_max_subarray import find_max_subarray


class TestFindMaxSubarray(unittest.TestCase):

    def test_example(self):
        array = [1, 8, 2, 10]
        self.assertEqual(find_max_subarray(len(array), array), [21, [0, 3]])

    def test_single_element(self):
        array = [1]
        self.assertEqual(find_max_subarray(len(array), array), [1, [0, 0]])

    def test_empty_array(self):
        array = []
        self.assertEqual(find_max_subarray(len(array), array), [0, [0, 0]])


if __name__ == '__main__':
    unittest.main()
