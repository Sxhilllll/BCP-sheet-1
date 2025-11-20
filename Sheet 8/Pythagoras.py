import math

base = int(input("Enter the base:"))
height = int(input("Enter the height:"))

def pythagoras(a,b):
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse
print("Hypotenuse:",pythagoras(base,height))
