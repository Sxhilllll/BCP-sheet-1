#Read N, Print No of digits in N.
num = int(input("Enter a number to check digits: "))
digit=0
while num>0:
    num //= 10
    digit= digit+1
print("Number of digits is: " , digit)