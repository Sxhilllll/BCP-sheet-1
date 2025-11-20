# Ques. Given N array elements, every element repeats twice except 1. Find the unique element
arr=[1,2,2,3,3,4,4]
def unique(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans^arr[i]
    return ans
print(unique(arr))









