class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length*self.width)

print("Length of small rectangle:")
smallLength = int(input())
print("Width of small rectangle:")
smallWidth = int(input())
smallRectangle = Rectangle(smallLength,smallWidth)

print("Area: ",smallRectangle.area())
print("Perimeter: ",smallRectangle.perimeter())

print("Length of large rectangle:")
largeLength = int(input())
print("Width of large rectangle:")
largeWidth = int(input())
largeRectangle = Rectangle(largeLength,largeWidth)

print("Area: ",largeRectangle.area())
print("Perimeter: ",largeRectangle.perimeter())