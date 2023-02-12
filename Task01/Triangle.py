from triangle_func import IncorrectTriangleSides


class Triangle:
    def __init__(self, side1: int, side2: int, side3: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if not isinstance(side1, int) or not isinstance(side2, int) or not isinstance(side3, int):
            raise IncorrectTriangleSides('Incorrect triangle sides: All sides values must be int')
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise IncorrectTriangleSides('Incorrect triangle sides: Triangle with given sides does not exist')

    def triangle_type(self) -> str:
        if self.side1 and self.side1 != self.side3 and self.side2 != self.side3:
            return "nonequilateral"
        elif self.side1 == self.side2 == self.side3:
            return "equilateral"
        else:
            return "isosceles"

    def perimeter(self) -> int:
        return self.side1 + self.side2 + self.side3
