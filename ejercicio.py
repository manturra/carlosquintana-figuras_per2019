import math
class Shape():
    def __init__(self):
        pass
    def CalculateArea(self):
        return None
    def CalculatePerimeter(self):
        return None

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def CalculateArea(self):
        area = self.side**2
        return area
    def CalculatePerimeter(self):
        perimeter = 4*self.side
        return perimeter

class Rectangule(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def CalculateArea(self):
        area = self.base*self.height
        return area
    def CalculatePerimeter(self):
        perimeter = 2*self.base+2*self.height
        return perimeter

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def CalculateArea(self):
        area = math.pi*(self.radius**2)
        return area
    def CalculatePerimeter(self):
        perimeter = 2*self.radius*math.pi
        return perimeter

class Elipse(Shape):
    def __init__(self,rmajor, rminor):
        self.rmajor = rmajor
        self.rminor = rminor
    def CalculateArea(self):
        area = self.rmajor*self.rminor*math.pi
        return area
    def CalculatePerimeter(self):
        perimeter = 2*math.pi*(((self.rminor**2+self.rmajor**2)/2)**(1/2))
        return perimeter
