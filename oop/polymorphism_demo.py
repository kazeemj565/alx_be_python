import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass
        

    def area(self):
        raise NotImplementedError
        pass

class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)


        pass

    def area(self):
        return self.length * self.width

        pass

class Circle(Shape):
    def __init__(self,length, width, radius):
        super().__init__(length, width)
        self.radius = radius
        pass
    def area(self):
        return math.pi*(self.radius**2)
