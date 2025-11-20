# def search(arr, n, m):
#     low =0
#     high = n - 1

#     while low<= high:
#         mid =(low + high)//2
#         if arr[mid] == m:
#             return mid
#         elif arr[mid]<m:
#             low = mid +1
#         else:
#             high = mid -1
#     return-1
        
# n = int(input("enter"))
# arr = list(map(int, input().split()))
# m = int(input("enter"))


# result = search(arr, n, m)
#  print(result)
# //given an array elements every element is  repatet twise  find that unique elements
def find_unique_element(arr):
    unique = 0
    for num in arr:
        unique ^= num
    


    




    