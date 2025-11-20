def printSubarray(a,start,end):
    sumA = 0
    for i in range(start,end+1):
        print(a[i],end=" ")
        sumA =sumA + a[i]
    print("=",sumA)

def printAllSubarray(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            printSubarray(a,i,j)
a = [2,5,6]
printAllSubarray(a)
