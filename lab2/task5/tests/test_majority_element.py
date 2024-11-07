import unittest

from lab2.task5.src.majority_element import majority_element


class TestMajorityElement(unittest.TestCase):

    def test_should_find_majority_element_example1_array(self):
        array = [2, 3, 9, 2, 2]
        self.assertEqual(majority_element(array), 1)

    def test_should_find_majority_element_example2_array(self):
        array = [1, 2, 3, 4]
        self.assertEqual(majority_element(array), 0)

    def test_should_find_majority_element_single_element_array(self):
        array = [1]
        self.assertEqual(majority_element(array), 1)

    def test_should_find_majority_element_empty_array(self):
        array = []
        self.assertEqual(majority_element(array), 0)

    def test_should_find_majority_element_equally(self):
        array = [1, 1, 1, 2, 2, 2]
        self.assertEqual(majority_element(array), 0)


if __name__ == '__main__':
    unittest.main()
