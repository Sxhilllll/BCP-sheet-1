# Ques. Given an integer array n, except which number occur odd number of times 
# First line of the input contains integer n, denoting the size of array
# Second line contains n space separated  integers denoting the elements of the array
arr = [2,3,4,2,3,1,1]
n = len(arr)
unique = 0
for i in arr:
    unique ^= 1
print(unique)
