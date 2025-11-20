a = list(map(int,input().split()))
def printsubArray(a,start,end):
    sum=0
    for i in range(start,end+1):
        print(a[i], end=" ")
        sum = sum+a[i]
    print("Sum = ",sum)

def printAllSubarray(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            printsubArray(a,i,j)
printAllSubarray(a)

