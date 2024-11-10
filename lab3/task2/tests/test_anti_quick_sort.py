import unittest

from lab3.task2.src.anti_quick_sort import anti_quick_sort


class TestAntiQuickSort(unittest.TestCase):

    def test_should_create_check_permutation_of_n_nums(self):
        # given
        # example n
        n1 = 3
        # another average n
        n2 = 10
        # when
        result1 = anti_quick_sort(n1)
        result2 = anti_quick_sort(n2)
        # then
        self.assertEqual(result1, [1, 3, 2])
        self.assertEqual(result2, [1, 4, 6, 8, 10, 5, 3, 7, 2, 9])

    def test_should_create_permutation_of_max_nums(self):
        # given
        n = 10**6
        # when
        result = anti_quick_sort(n)
        # then
        return result


if __name__ == '__main__':
    unittest.main()
