#You are given 3 integer angles of a triangle.Tell whether the triangle is valid or not.
a1= int(input("Enter the first angle of the triangle:"))
a2= int(input("Enter the seccond angle of the triangle:"))
a3= int(input("Enter the third angle of the triangle:"))
if a1+a2+a3 ==180:
    print("Triangle is valid")
else : print("Triangle is not valid")