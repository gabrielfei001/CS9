#Shape 2D
class Shape2D:
    def __init__(self, color):
        self.color = color

    def setColor(self, color):
        self.color = str(color)

    def getColor(self):
        return self.color

    def getShapeProperties(self):
        txt = "Shape: N/A, Color: {}".format(self.color)
        return txt
