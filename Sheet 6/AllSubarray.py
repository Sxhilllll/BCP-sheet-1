# WAP to print all the subarrays of given arrays[1 2 3]
def printSubarray(a,start,end):
    for i in range(start,end+1):
        print(a[i],end =" ")
    print()

def printAllSubarray(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            printSubarray(a,i,j)
a = [1,2,3]
n=len(a)
printAllSubarray(a)
count = n*(n+1)//2
print("Total subarrays will be:",count)

