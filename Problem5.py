import math

class Shape:
    def calculateArea(self):
        pass

class Circle():
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        return math.pi*self.radius**2

class Rectangle():
    def __init__(self,length,width):
        self.length =length
        self.width =width
    def calculateArea(self):
        return self.length*self.width

class Triangle():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculateArea(self):
        return 0.5*self.base*self.height

class Shapes:
    def createShape(shapeType, *args):
        if shapeType=='circle':
            return Circle(*args)
        elif shapeType=='rectangle':
            return Rectangle(*args)
        elif shapeType =='triangle':
            return Triangle(*args)
        else:
            raise ValueError("Invalid shape")

myCircle = Shapes.createShape('circle', 9)
myRectangle = Shapes.createShape('rectangle', 3, 6)
myTriangle = Shapes.createShape('triangle', 4, 6)

circleArea = myCircle.calculateArea()
rectangleArea = myRectangle.calculateArea()
triangleArea = myTriangle.calculateArea()

print("Area of the circle:",circleArea)
print("Area of the rectangle:",rectangleArea)
print("Area of the triangle:",triangleArea)
