#Circle
from Shape2D import Shape2D

class Circle(Shape2D):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def computeArea(self):
        area = 3.14159 * (self.radius ** 2)
        return area

    def computePerimeter(self):
        perimeter = 2 * 3.14159 * self.radius
        return perimeter

    def getShapeProperties(self):
        txt = "Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}"\
            .format(Shape2D.getColor(self), self.radius, self.computeArea(), self.computePerimeter())
        return txt