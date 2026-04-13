# Method Lookup is a form of polymorphism
# A subclass will lookup a method in the superclass if
# that subclass dosen't have that method.

# Polymorpphism - "multiple forms"
# The idea of having the multiple interfaces to accomplish something


class Shape:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def draw(self):
        for _ in range(self.width):
            print("*" * self.length)


class Rectangle(Shape):

    def __init__(self, length, width):
        super()._init__(length, width)



class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

class Triangle(Shape):
    def __init__(self, leg_a, leg_b):
        super().__init__(leg_a, leg_b)

    def draw(self):
        for i in range(self.width):
            print("*" * (self.width - 1))

s = Shape(5, 3)
s.draw()

r = Rectangle(7,2)
r.draw()

t = Triangle(6, 8)
t.draw()