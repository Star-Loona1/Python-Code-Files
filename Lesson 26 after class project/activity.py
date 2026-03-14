import math
class Circle:
    def __init__(self):
        print()
    def inpu(self):
        self.radius = int(input('Enter the radius: '))
    def area(self):
        self.a = math.pi * (self.radius ** 2)
        print('The area of the circle is ', self.a)
    def perimeter(self):
        self.p = 2 * math.pi * self.radius
        print('The perimeter of the circle is ', self.p)
calculate = Circle()
calculate.inpu()
calculate.area()
calculate.perimeter()