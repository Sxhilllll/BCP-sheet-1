#WAP to reverse a number
n = int(input("Enter a number to reverse: "))
reversed_num=0
while(n>0):
    digit = n%10
    reversed_num = reversed_num*10+digit
    n = n//10
print(reversed_num)

