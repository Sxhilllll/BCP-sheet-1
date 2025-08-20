n = int(input("Enter the number to sum: "))
sum = 0
while(n>0):
    rem= n%10
    n=n//10
    sum = sum + rem
print("Sum of digits is: ",sum)