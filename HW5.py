import math
from abc import ABC, abstractmethod


# Master abstract class
class Shape(ABC):
    def __init__(self, a, b, c):
        self.set_params(a, b, c)

    @abstractmethod
    def calc_surface(self):
        pass

    def set_params(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self._b) + " by " + str(
            self._c) + "] at " + str(hex(id(self)))


# Rectangle
class Rectangle(Shape):

    def __init__(self, a, b):
        super().__init__(a, b, 0)

    def calc_surface(self):
        return self._a * self._b

    def calc_perimeter(self):
        return (self._a + self._b) * 2

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self._b) + "] at " + str(hex(id(self)))


# testing rectangle
rec = Rectangle(10, 5)
print(rec.calc_perimeter())
print(rec.calc_surface())


# Circle
class Circle(Shape):
    def __init__(self, a):
        super().__init__(a, 0, 0)

    def calc_surface(self):
        return math.pi * self._a ** 2

    def calc_perimeter(self):
        return 2 * math.pi * self._a

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


# testing circle
cir = Circle(10)
print(cir.calc_perimeter())
print(cir.calc_surface())


# Triangle
class Triangle(Shape):
    def calc_surface(self):
        s = (self._a + self._b + self._c) / 2
        try:
            if math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c)) == 0:
                return "0 - the result is just a line"

            else:
                return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

        except:
            return "NaN - With the given parameters it is not possible to construct a triangle"

    def calc_perimeter(self):
        if self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._c > self._a:
            return self._a + self._b + self._c

        elif self._a + self._b == self._c or self._a + self._c == self._b or self._b + self._c == self._a:
            return "The result is just a line"

        else:
            return "NaN - With the given parameters it is not possible to construct a triangle"


# testing triangle
tri = Triangle(2, 3, 2)
print(tri.calc_surface())
print(tri.calc_perimeter())

tri2 = Triangle(2, 10, 3)
print(tri2.calc_surface())
print(tri2.calc_perimeter())

tri3 = Triangle(2, 3, 5)
print(tri3.calc_surface())
print(tri3.calc_perimeter())


# Equilateral triangle
class EquilateralTriangle(Shape):
    def __init__(self, a):
        super().__init__(a, a, a)

    def calc_surface(self):
        return ((math.sqrt(3)) / 4) * self._a ** 2

    def calc_perimeter(self):
        return self._a * 3


# testing equilateral triangle
equitri = EquilateralTriangle(1)
print(equitri.calc_surface())
print(equitri.calc_perimeter())


# Square with inheritance from rectangle
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


# testing square
sqr = Square(5)
print(sqr.calc_perimeter())
print(sqr.calc_surface())