#Print all factors/divisors of a given +ve number
n = int(input("Enter a number to check factors: "))
i=1
while(i<=n):
    if(n%i==0):       # i is factor of n
     print(i)
    i = i + 1