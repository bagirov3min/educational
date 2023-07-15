import math


class Shape:
    def area(self):
        pass

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return True
        else:
            return False


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semiperimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semiperimeter
            * (semiperimeter - self.side1)
            * (semiperimeter - self.side2)
            * (semiperimeter - self.side3)
        )
