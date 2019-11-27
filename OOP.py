class Rectangle():

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
