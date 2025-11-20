# Q.1 Given an array compute the sum of all elements
arr = list(map(int,input("Input numbers:").split()))
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
print("Sum =",sum)



# Q.2 Given an array find the maximum value in it
arr = list(map(int,input("Input numbers:").split()))      #ans = -float("inf")
max_val = arr[0]
for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
print("Maximum value:",max_val)



# Q.3 Given an array and an target, find number of occurrence of target number in the  array
arr = list(map(int,input("Input numbers:").split()))
print(arr)
target = int(input("Enter a target number from the array: "))
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count = count + 1
print("Occurrences of",target, "=",count)



#Q.4 Given an array and increment number,generate a new array which contains all values of original array increased by Increment value
arr = list(map(int,input("Input numbers: ").split()))
print(arr)
inc_val = int(input("Enter the value to increment to each num in the arr: "))
new_arr = []
for i in range(len(arr)):
    new_arr.append(arr[i] + inc_val)
print("New array is:", new_arr)



# Q.5 Given an array and a new array which contains all values squared
arr = list(map(int,input("Enter numbers:").split()))
new_arr = []
for i in range(len(arr)):
    new_arr.append(arr[i] * arr[i])
print("New array is:",new_arr)




# Q.6 Given an array, filter out all odd numbers
# Take input from user, split by spaces, convert to integers
arr = list(map(int, input("Enter numbers separated by space:").split()))


arr = list(map(int,input("Input:").split()))
odd_num = []
for x in arr:
    if x%2 != 0:
        odd_num.append(x)
print("Odd numbers are: ",odd_num)