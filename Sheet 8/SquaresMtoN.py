a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))

def Square(a,b):
    for i in range(a, b+1):
        print(i**2)
Square(a,b)