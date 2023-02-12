import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type


class TestGetTriangleTypeFunction(unittest.TestCase):

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(8, 9, 10), 'nonequilateral')

    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(1, 1, 1), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(2, 3, 2), 'isosceles')

    def test_type_error(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type('a', 'b', 3)

    def test_incorrect_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
