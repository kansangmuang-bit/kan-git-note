# Method lookup is a form of polymorphism
# A subclass will lookup a method in the superclass if
# that subclass doesn't have that method.

# Polymorphism - "multiple forms"
# The idea of having the multiple interfaces to accomplish something

class Shape:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width 
        
    def draw(self):
        for _ in range(self.width):
            print("* " * self.length)


class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().__init__(length, width)
        
        

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side) 


class Triangle(Shape):
    
    def __init__(self, side):
        super().__init__(side, side) 
        
    def draw(self):
        for i in range(self.width):
            print("* " * (self.width - i))


s = Shape(5, 3)
s.draw()

print()

r = Rectangle(7, 2)
r.draw()

print()

s2 = Square(5)
s2.draw()

print()

t = Triangle(6)
t.draw()