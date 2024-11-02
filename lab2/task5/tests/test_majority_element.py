import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from majority_element import majority_element


class TestMajorityElement(unittest.TestCase):

    def test_example1(self):
        array = [2, 3, 9, 2, 2]
        self.assertEqual(majority_element(array), 1)

    def test_example2(self):
        array = [1, 2, 3, 4]
        self.assertEqual(majority_element(array), 0)

    def test_single_element(self):
        array = [1]
        self.assertEqual(majority_element(array), 1)

    def test_empty_array(self):
        array = []
        self.assertEqual(majority_element(array), 0)

    def test_majority_element_equally(self):
        array = [1, 1, 1, 2, 2, 2]
        self.assertEqual(majority_element(array), 0)


if __name__ == '__main__':
    unittest.main()
