import math

a = int(input("Enter a perfect square: "))
def sqRoot(a):
    sqrt_val = int(math.sqrt(a))
    if sqrt_val * sqrt_val == a:
        return sqrt_val
    else:
        return -1
print(sqRoot(a))