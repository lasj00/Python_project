import math


class Rectangle:

    # the init method is not mandatory
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.set_parameters(10,20)

    def calc_surface(self):
        return self.a * self.b


# Encapsulation

class Rectangle2():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        # self.set_parameters(10,20)

    def calc_surface(self):
        return self.__a * self.__b


r = Rectangle2(4, 6)
r.__a = 10  # can't change the parameters - the field (__a) cannot be accessed - creates another filed inside the object
r.a = 10  # a is created as a different value
print(r.calc_surface())


# Special methods

class Rectangle3:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a * self.b

    def __str__(self):
        return "Rect: {0} by {1}".format(self.a, self.b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Rectangle(a, b)

    def __lt__(self, other):
        self_area = self.calc_surface()
        other_area = other.calc_surface()
        return self_area < other_area


r1 = Rectangle3(4, 6)
r2 = Rectangle3(6, 8)
r = r1 + r2
print(r)
print(r2 < r1)


# inheritance

class Shape:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        return "{0}: [{1},{2}]".format(self.__class__.__name__, self._a, self._b)


class RectangleIn(Shape):
    def calc_surface(self):
        return self._a * self._b


class Circle(Shape):
    def calc_surface(self):
        return math.pi * self._a ** 2

    # example of polymorphism
    def __str__(self):
        return "{0}: [{1}]".format(self.__class__.__name__, self._a)


s = Shape(4, 5)
r = RectangleIn(4, 5)
print(r.calc_surface())
c = Circle(5)
print(c.calc_surface())