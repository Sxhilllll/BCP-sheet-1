import math

r = int(input("Enter the radius:"))

def VolOfSphere(r):
    vol = (4 * math.pi * (r**3)) / 3
    return vol
print(VolOfSphere(r))