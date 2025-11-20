# Recursion is a programming technique where a function calls itself directly or indirectly in order to solve the problem
# In a recursive function, the function makes one or more calls to itself as a part of its execution
# The process continues a base case is reached, at which point the function stops calling itself and returns a result
# Why we use:
# reusability of code
# to solve complex problems

# Steps:
# Make an assumption --> 1. decide what your function does and trust what that it will do it
# Make logic --> 2. solve a bigger problem using a sub problem
# Base-case --> 3. when a recursion stops...

# Ques. Sum of n natural numbers

# n = int(input())
# sum = 0
# for i in range(0,n+1):
#     sum+=i
# print(sum)
# prints sum of n natural numbers


# sum using recursion
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return (sum(n-1)+n)
# print(sum(5))

# Ques factorial using recursion
# n = int(input())
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return(fact(n-1)*(n))
# print(fact(n))

# Ques. Using recursion print numbers from 1 to n
# Ques. Using recursion print numbers from n to 1
# Ques. Using a recursive function, find the  Nth fibonacci number

# 1 to N
# n = int(input())
# def num(n):
#     if n == 0:
#         return 1
#     else:
#         num(n-1)
#         print(n)
# num(n)


# N to 1
# n = int(input())
# def numbers(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         numbers(n-1)
# numbers(n)

# n = int(input())
# def fibonacci(n):
#     if n <=1:
#         return n
#     else:
#         return(fibonacci(n-1)+fibonacci(n+1))
# print(fibonacci(n))

# Ques Find the sum of digits using recursion
# Ques Reverse a string using recursion

# Ques binary search
arr = [10,20,30,40,50,60]
L = 0
M = len(arr)-1
while(L<=M):
    mid = (L+M)//2


