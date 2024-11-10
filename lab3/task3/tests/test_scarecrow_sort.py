import unittest

from lab3.task3.src.scarecrow_sort import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):

    def test_should_check_the_possibility_of_sorting_example1_array(self):
        # given
        n, k = 3, 2
        array = [2, 1, 3]
        # when
        result = scarecrow_sort(n, k, array)
        # then
        self.assertEqual(result, 'NO')

    def test_should_check_the_possibility_of_sorting_example2_array(self):
        # given
        n, k = 5, 3
        array = [1, 5, 3, 4, 1]
        # when
        result = scarecrow_sort(n, k, array)
        # then
        self.assertEqual(result, 'YES')

    def test_should_check_the_possibility_of_sorting_sorted_array(self):
        # given
        n, k = 5, 3
        array = [1, 2, 3, 4, 5]
        # when
        result = scarecrow_sort(n, k, array)
        # then
        self.assertEqual(result, 'YES')

    def test_should_check_the_possibility_of_sorting_reverse_sorted_array(self):
        # given
        n, k = 5, 3
        array = [5, 4, 3, 2, 1]
        # when
        result = scarecrow_sort(n, k, array)
        # then
        self.assertEqual(result, 'NO')

    def test_should_check_the_possibility_of_sorting_single_element_array(self):
        # given
        n, k = 1, 3
        array = [1]
        # when
        result = scarecrow_sort(n, k, array)
        # then
        self.assertEqual(result, 'YES')


if __name__ == '__main__':
    unittest.main()
