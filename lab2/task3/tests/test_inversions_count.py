import unittest

from lab2.task3.src.inversions_count import inversions_count


class TestInversionsCount(unittest.TestCase):

    def test_should_count_inversions_example_array(self):
        # given
        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        temp_array = [0] * len(array)
        # when
        result = inversions_count(array, temp_array, 0, len(array) - 1)
        # then
        self.assertEqual(result, 17)

    def test_should_count_inversions_no_inversions_array(self):
        # given
        array = [1, 2, 3, 4]
        temp_array = [0] * len(array)
        # when
        result = inversions_count(array, temp_array, 0, len(array) - 1)
        # then
        self.assertEqual(result, 0)

    def test_should_count_inversions_reverse_sorted_array(self):
        # given
        array = [4, 3, 2, 1]
        temp_array = [0] * len(array)
        # when
        result = inversions_count(array, temp_array, 0, len(array) - 1)
        # then
        self.assertEqual(result, 6)

    def test_should_count_inversions_empty_array(self):
        # given
        array = []
        temp_array = []
        # when
        result = inversions_count(array, temp_array, 0, len(array) - 1)
        # then
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
