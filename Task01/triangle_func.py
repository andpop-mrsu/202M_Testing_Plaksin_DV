import doctest


class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(side1: int, side2: int, side3: int) -> str:
    """
    Function for checking type of triangle
    :param side1: first side of triangle (int)
    :param side2: second side of triangle (int)
    :param side3: third side of triangle (int)
    :return: type of triangle (str)
    :raises: IncorrectTriangleSides: if sides was set incorrectly
    >>> get_triangle_type(8, 9, 10)
    'nonequilateral'
    >>> get_triangle_type(1, 1, 1)
    'equilateral'
    >>> get_triangle_type(2, 3, 2)
    'isosceles'
    >>> get_triangle_type('a','b',3)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect triangle sides: All sides values must be int
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect triangle sides: Triangle with given sides does not exist
    """

    if not isinstance(side1, int) or not isinstance(side2, int) or not isinstance(side3, int):
        raise IncorrectTriangleSides('Incorrect triangle sides: All sides values must be int')
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise IncorrectTriangleSides('Incorrect triangle sides: Triangle with given sides does not exist')

    if side1 != side2 and side1 != side3 and side2 != side3:
        return 'nonequilateral'
    elif side1 is side2 is side3:
        return 'equilateral'
    else:
        return 'isosceles'


if __name__ == '__main__':
    doctest.testmod()
