import unittest

from lab2.task4.src.binary_search import search_elements


class TestBinarySearch(unittest.TestCase):

    def test_should_binary_search_example_array(self):
        # given
        array = [1, 5, 8, 12, 13]
        targets = [8, 1, 23, 1, 11]
        # when
        result = search_elements(array, targets)
        # then
        self.assertEqual(result, [2, 0, -1, 0, -1])

    def test_should_binary_search_target_is_not_found(self):
        # given
        array = [1, 2, 3, 4, 5]
        targets = [8]
        # when
        result = search_elements(array, targets)
        # then
        self.assertEqual(result, [-1])

    def test_should_binary_search_empty_array(self):
        # given
        array = []
        targets = [8]
        # when
        result = search_elements(array, targets)
        # then
        self.assertEqual(result, [-1])

    def test_should_binary_search_single_element_is_found(self):
        # given
        array = [8]
        targets = [8]
        # when
        result = search_elements(array, targets)
        # then
        self.assertEqual(result, [0])

    def test_should_binary_search_single_element_not_found(self):
        # given
        array = [0]
        targets = [8]
        # when
        result = search_elements(array, targets)
        # then
        self.assertEqual(result, [-1])


if __name__ == '__main__':
    unittest.main()
