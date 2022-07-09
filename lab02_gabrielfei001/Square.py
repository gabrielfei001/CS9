#Square
from Shape2D import Shape2D

class Square(Shape2D):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def setSide(self, side):
        self.side = side
    
    def getSide(self):
        return self.side
    
    def computeArea(self):
        area = self.side ** 2
        return area

    def computePerimeter(self):
        perimeter = self.side * 4
        return perimeter

    def getShapeProperties(self):
        txt = "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}"\
            .format(Shape2D.getColor(self), self.side, self.computeArea(), self.computePerimeter())
        return txt