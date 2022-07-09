#testFile
import pytest
from Shape2D import Shape2D
from Circle import Circle
from Square import Square

def test_Constructors():
    s1 = Shape2D("blue")
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    assert "blue" == s1.color
    assert "blue" == s2.color
    assert 3.5 == s2.radius
    assert "blue" == s3.color
    assert 4 == s3.side

def test_Setters():
    s1 = Shape2D("blue")
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    s1.color = "red"
    s2.color = "red"
    s2.radius = 4.5
    s3.color = "red"
    s3.side = 8
    assert "red" == s1.color
    assert "red" == s2.color
    assert 4.5 == s2.radius
    assert "red" == s3.color
    assert 8 == s3.side

def test_Getters():
    s1 = Shape2D("blue")
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    assert "blue" == s1.getColor()
    assert "blue" == s2.getColor()
    assert 3.5 == s2.getRadius()
    assert "blue" == s3.getColor()
    assert 4 == s3.getSide()

def test_Perimeter():
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    s4 = Circle("red", 15)
    s5 = Square("red", 20)
    assert 21.99113 == s2.computePerimeter()
    assert 16 == s3.computePerimeter()
    assert 94.2477 == s4.computePerimeter()
    assert 80 == s5.computePerimeter()

def test_Area():
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    s4 = Circle("red", 15)
    s5 = Square("red", 20)
    assert 38.4844775 == s2.computeArea()
    assert 16 == s3.computeArea()
    assert 706.85775 == s4.computeArea()
    assert 400 == s5.computeArea()

def test_getShapeProperties():
    s1 = Shape2D("blue")
    s2 = Circle("blue", 3.5)
    s3 = Square("blue", 4)
    assert "Shape: N/A, Color: blue" == s1.getShapeProperties()
    assert "Shape: CIRCLE, Color: blue, Radius: 3.5, Area: 38.4844775, Perimeter: 21.99113"\
        == s2.getShapeProperties()
    assert "Shape: SQUARE, Color: blue, Side: 4, Area: 16, Perimeter: 16"\
        == s3.getShapeProperties()