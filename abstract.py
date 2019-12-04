from abc import ABC
import math


# by inheriting from ABC, we create an abstract class
class Shape(ABC):
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        return "{0}: [{1},{2}]".format(self.__class__.__name__, self._a, self._b)

    # there is a need of at least one abstract method to make the class abstract
    @abstractmethod
    def calc_surface(self):
        pass


class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self._b


class Circle(Shape):
    def calc_surface(self):
        return math.pi * self._a ** 2

    # example of polymorphism
    def __str__(self):
        return "{0}: [{1}]".format(self.__class__.__name__, self._a)


s = Shape(4, 5)
r = Rectangle(4, 5)
print(r.calc_surface())
c = Circle(5)
print(c.calc_surface())