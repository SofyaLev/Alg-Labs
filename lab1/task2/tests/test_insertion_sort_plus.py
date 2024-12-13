import unittest
from utils import memory_data, time_data
from lab1.task2.src.insertion_sort_plus import insertion_sort_plus, main


class TestInsertionSortPlus(unittest.TestCase):

    def test_should_check_basic_case(self):
        # given
        n = 4
        array = [4, 3, 2, 1]
        exp_array = [1, 2, 3, 4]
        exp_indexes = [1, 1, 1, 1]

        # when
        indexes, sorted_array = insertion_sort_plus(n, array)

        # then
        self.assertEqual(indexes, exp_indexes)
        self.assertEqual(array, exp_array)

    def test_should_check_array_with_duplicates(self):
        # given
        n = 5
        array = [3, 3, 1, 2, 3]
        exp_array = [1, 2, 3, 3, 3]
        exp_indexes = [1, 2, 1, 2, 5]

        # when
        indexes, sorted_array = insertion_sort_plus(n, array)

        # then
        self.assertEqual(indexes, exp_indexes)
        self.assertEqual(array, exp_array)

    def test_should_check_sorted_array(self):
        # given
        n = 5
        array = [1, 2, 3, 4, 5]
        exp_array = [1, 2, 3, 4, 5]
        exp_indexes = [1, 2, 3, 4, 5]

        # when
        indexes, sorted_array = insertion_sort_plus(n, array)

        # then
        self.assertEqual(indexes, exp_indexes)
        self.assertEqual(array, exp_array)

    def test_should_check_single_element(self):
        # given
        n = 1
        array = [22]
        exp_array = [22]
        exp_indexes = [1]

        # when
        indexes, sorted_array = insertion_sort_plus(n, array)

        # then
        self.assertEqual(indexes, exp_indexes)
        self.assertEqual(array, exp_array)

    def test_should_check_empty_array(self):
        # given
        n = 0
        array = []
        exp_array = []
        exp_indexes = [1]

        # when
        indexes, sorted_array = insertion_sort_plus(n, array)

        # then
        self.assertEqual(indexes, exp_indexes)
        self.assertEqual(array, exp_array)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 256

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()
