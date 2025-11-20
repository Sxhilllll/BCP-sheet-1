import math

a = int(input("Enter the radius of the circle: "))
def AreaOfCircle(a):
    area = math.pi*a*a
    return area

print(AreaOfCircle(a))
