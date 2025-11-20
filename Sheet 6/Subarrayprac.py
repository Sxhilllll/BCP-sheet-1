a = list(map(int,input().strip()))
def printSubarray(a,start,end):
    for i in range(start,end+1):
        print(a[i], end=' ')
    print()

def printAllSubarray(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            printSubarray(a,i,j)
printAllSubarray(a)













a = list(map(int,input().split()))
def printSubarray(a,start,end):
    for i in range(start,end+1):
        print(a[i], end=" ")
    print()

def printAllSubarray(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            printSubarray(a,i,j)
printAllSubarray(a)