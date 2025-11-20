import math

a = int(input("Enter the semi-major axis:"))
b = int(input("Enter the semi-minor axis:"))

def AreaOfEllipse(a,b):
    area = math.pi * a * b
    return area
print("Area of Ellipse:",AreaOfEllipse(a,b))