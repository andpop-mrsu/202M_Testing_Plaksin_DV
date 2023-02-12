import pytest
from Triangle import Triangle
from triangle_func import IncorrectTriangleSides


class TestTriangleClass:
    def test_triangle_create(self):
        triangle = Triangle(8, 9, 10)
        assert triangle.side1 == 8
        assert triangle.side2 == 9
        assert triangle.side3 == 10

    def test_triangle_create_with_type_error(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle('a', 'b', 3)

    def test_triangle_create_with_incorrect_sides(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 3)

    def test_triangle_type_nonequilateral(self):
        assert Triangle(9, 8, 10).triangle_type() == 'nonequilateral'

    def test_triangle_type_equilateral(self):
        assert Triangle(1, 1, 1).triangle_type() == 'equilateral'

    def test_triangle_type_isosceles(self):
        assert Triangle(2, 3, 2).triangle_type() == 'isosceles'

    def test_triangle_perimeter(self):
        assert Triangle(8, 9, 10).perimeter() == 27
