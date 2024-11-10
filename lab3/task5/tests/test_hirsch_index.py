import unittest

from lab3.task5.src.hirsch_index import hirsch_index


class TestHirschIndex(unittest.TestCase):

    def test_should_find_hirsch_index_example1_array(self):
        # given
        array = [3, 0, 6, 1, 5]
        # when
        result = hirsch_index(array)
        # then
        self.assertEqual(result, 3)

    def test_should_find_hirsch_index_example2_array(self):
        # given
        array = [1, 3, 1]
        # when
        result = hirsch_index(array)
        # then
        self.assertEqual(result, 1)

    def test_should_find_hirsch_index_sorted_array(self):
        # given
        array = [1, 2, 3, 4]
        # when
        result = hirsch_index(array)
        # then
        self.assertEqual(result, 2)

    def test_should_find_hirsch_index_reverse_sorted_array(self):
        # given
        array = [4, 3, 2, 1]
        # when
        result = hirsch_index(array)
        # then
        self.assertEqual(result, 2)

    def test_should_count_inversions_empty_array(self):
        # given
        array = []
        # when
        result = hirsch_index(array)
        # then
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
