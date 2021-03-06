from typing import List


class Rectangle():
    def set_params(self,a,b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b


r = Rectangle()
r.set_params(5,6)
r2 = r # this is the pointer
r2.set_params(5,8)
r3 = Rectangle()
r3.set_params(7,9)
print(r.calc_surface())
print(r2.calc_surface())
print(r3.calc_surface())

#other demonstration
x = [r, r2, r3]
#y = x.copy()
from copy import deepcopy
y = deepcopy(x)

y[2].set_params(10, 8)
print(y[2].calc_surface())
print(x[2].calc_surface())

