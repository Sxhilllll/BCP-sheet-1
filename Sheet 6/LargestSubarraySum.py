"Kadaene's Algorithm"
#Given an integer array nums=[]. Find the subarray with the largest sum and return its sum
nums=[-2,1,-3,4,-1,2,1]
output = 6
num=[5,4,-1,7,8]




def printSubarray(a,start,end):
    for i in range(start,end+1):
        print(a[i],end =" ")
    print()
def printAllSubarray(a):
    n = len(a)
    max_sum = float('-inf')
    max_start = max_end = 0
    for i in range(n):
        for j in range(i,n):
            current_sum = sum(a[i:j+1])
            printSubarray(a,i,j)
            if current_sum > max_sum:
                max_sum = current_sum
                max_start = i
                max_end = j
    return max_sum,max_start,max_end

a = [1,2,3]
max_sum,max_start,max_end = printAllSubarray(a)
print("\nLargest Subarray is:",end=" ")
printSubarray(a,max_start,max_end)
print("\nAnd it's sum=",max_sum)

