import math

class Shape:
       

    def area(self):
        raise NotImplementedError
        pass

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

        pass

    def area(self):
        return self.length * self.width

        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        pass
    def area(self):
        return math.pi*(self.radius** 2)
