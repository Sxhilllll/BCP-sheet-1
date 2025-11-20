# Ques. Given an integer N,count how many set bit are there in N.
n = int(input("Enter  a numner: "))
def Total_Setbits(n):
    count = 0
    while n>0:
        if n & 1 == 1:
           count +=1
        n = n>> 1
        return n
print(Total_Setbits(n))