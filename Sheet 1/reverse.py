#WAP to reverse a number
n = int(input("Enter a number to reverse: "))
rev = 0
while(n>0):
    digit = n%10
    rev = rev * 10 + digit
    n = n//10
print(rev)

n = int(input())
rev = 0
while n>0:
    digit = n%10
    rev = rev *10+digit
    n = n//10
print(rev)