import unittest

from lab2.task3.src.inversions_count import inversions_count


class TestInversionsCount(unittest.TestCase):

    def test_should_count_inversions_example_array(self):
        # given
        n = 10
        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        temp_array = [0] * n
        expected_result = 17

        # when
        result = inversions_count(array, temp_array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_inversions_no_inversions_array(self):
        # given
        n = 4
        array = [1, 2, 3, 4]
        temp_array = [0] * n
        expected_result = 0

        # when
        result = inversions_count(array, temp_array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_inversions_reverse_sorted_array(self):
        # given
        n = 4
        array = [4, 3, 2, 1]
        temp_array = [0] * n
        expected_result = 6

        # when
        result = inversions_count(array, temp_array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_inversions_empty_array(self):
        # given
        n = 0
        array = []
        temp_array = []
        expected_result = 0

        # when
        result = inversions_count(array, temp_array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
