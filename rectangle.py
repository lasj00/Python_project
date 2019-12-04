class Rectangle:
    num_rect = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        Rectangle.num_rect += 1

    def calc_surface(self):
        return self.a * self.b

    def __str__(self):
        return "Rect: {0} by {1}".format(self.a, self.b)

    # deletion method
    def __del__(self):
        Rectangle.num_rect -= 1
        print(self.__class__.__name__ + " destroyed")

    @classmethod
    def how_many(cls):
        print("We have {0} rectangles".format(Rectangle.num_rect))


r1 = Rectangle(4, 6)
print(r1)
r1.how_many()
r2 = Rectangle(6, 8)
print(r2)
r2.how_many()
del r1
r2.how_many()
print("The End")
