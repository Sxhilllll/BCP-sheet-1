# ans = 0
# for i in range(i,n):
# total = (i+1)*(n-i)
# count = a[i] * total
# ans = ans + count
# print ans

# Ques Given an array A of non negative number A and non negative number B,You need to find the number of subarrays with a sum less than B


# Ques an  array of integer A, a subarray of an array is set to be good,if it fulfills anyone of the criteria:
# length of subarray is to be even and and sum of all elements of the subarray must be less than B
# length of subarray is to be odd and and sum of all elements of the subarray must be greater than B
# count of good subarrays in A

# You have given an integer array of size A, now you need to find a subarray so that the sum of the continuous element is 
# maximum but the sum must not exceed B

A = 3
B = 1
C = [2,2,2]
output = 0

A = 5
B = 12
C = [2,1,3,4,5]
output = 12,12



A = [2,5,6]
B = 10
n = len(A)
count  = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + A[i]
        if(sum < B):
            count+=1
print(count)
