import unittest

from lab3.task8.src.closest_points import closest_points


class TestClosestPoints(unittest.TestCase):

    def test_should_find_closest_points_example1_array(self):
        # given
        k = 1
        array = [[1, 3], [-2, 2]]
        # when
        result = closest_points(array, k)
        # then
        self.assertEqual(result, [[-2, 2]])

    def test_should_find_closest_points_example2_array(self):
        # given
        k = 2
        array = [[3, 3], [5, -1], [-2, 4]]
        # when
        result = closest_points(array, k)
        # then
        self.assertEqual(result, [[3, 3], [-2, 4]])

    def test_should_find_closest_points_sorted_array(self):
        # given
        k = 2
        array = [[1, 1], [-2, 2], [4, -3], [-7, -4]]
        # when
        result = closest_points(array, k)
        # then
        self.assertEqual(result, [[1, 1], [-2, 2]])

    def test_should_find_closest_points_reverse_sorted_array(self):
        # given
        k = 2
        array = [[-7, -4], [4, -3], [-2, 2], [1, 1]]
        # when
        result = closest_points(array, k)
        # then
        self.assertEqual(result, [[1, 1], [-2, 2]])

    def test_should_find_closest_points_empty_array(self):
        # given
        k = 4
        array = []
        # when
        result = closest_points(array, k)
        # then
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
