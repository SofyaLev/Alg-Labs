import unittest

from lab3.task6.src.sum_of_tenths import sum_of_tenths


class TestSumOfTenths(unittest.TestCase):

    def test_should_count_sum_of_tenths_example_array(self):
        # given
        A = [7, 1, 4, 9]
        B = [2, 7, 8, 11]
        # when
        result = sum_of_tenths(A, B)
        # then
        self.assertEqual(result, 51)

    def test_should_count_sum_of_tenths_sorted_array(self):
        # given
        A = [1, 2, 3, 4, 5]
        B = [1, 1, 1, 1, 1]
        # when
        result = sum_of_tenths(A, B)
        # then
        self.assertEqual(result, 9)

    def test_should_count_sum_of_tenths_reverse_sorted_array(self):
        # given
        A = [5, 4, 3, 2, 1]
        B = [1, 2, 3, 4, 5]
        # when
        result = sum_of_tenths(A, B)
        # then
        self.assertEqual(result, 22)

    def test_should_count_sum_of_tenths_empty_array(self):
        # given
        A = []
        B = []
        # when
        result = sum_of_tenths(A, B)
        # then
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
