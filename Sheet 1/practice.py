# # # # # # # # # # # # # a=[1,2,"rahul",[25,85],True]
# # # # # # # # # # # # # print(a[0])
# # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # print(a[-1])
# # # # # # # # # # # # # print([-4])
# # # # # # # # # # # # # print(a[3][0])
# # # # # # # # # # # # # print(a[2])
# # # # # # # # # # # # arr=[0,1,2,3,4,5,6,0]
# # # # # # # # # # # # print(arr{0)

# # # # # # # # # # # l=[10,20,30,40,50]
# # # # # # # # # # # sum = 0
# # # # # # # # # # # for i in range(len(l)):
# # # # # # # # # # #     sum+=l[i]
# # # # # # # # # # # print(sum)

# # # # # # # # # # list=[10,20,30,40,50] #insert method takes two arguments(pos,value)
# # # # # # # # # # list.insert(2,25)
# # # # # # # # # # print(list)

# # # # # # # # # list=[12,54,62,64]         #extend method inserts a new list in the existing list
# # # # # # # # # list.extend([8,'Sahil',True])
# # # # # # # # # print(list)


# # # # # # # # list=[25,64,85]  #remove method removes the first occurrence of the element in the list
# # # # # # # # list.remove(25)
# # # # # # # # print(list)

# # # # # # # list=[2,6,5,8]  #
# # # # # # # list.pop()
# # # # # # # print(list)

# # # # # # list=[2,5,4,6]
# # # # # # list.pop(2)  #takes the index and deletes the element at the particular index
# # # # # # print(list)

# # # # # list=[1,2,3,4,5]   #reverse method reverses the whole list
# # # # # list.reverse()
# # # # # print(list)

# # list2=[1,2,3,4,5]
# # list1 = reversed(list2)
# # print(list(list1))

# # list=[25,65,45,95]
# # n=len(list)
# # for i in range(0,n//2):
# #     list[i],list[n-1-i] = list[n-1-i],list[i]
# #     print(list)

# # a = ("Hello How are you?")
# # print(a.split())

# # b = "Hello_How_are_you?"
# # print(b.split("_"))

# num =("1 2 3 4")
# print(num.split())

a = map(int,input().split())
print(a)
for i in a:
    print(i)
b = map(int,input().split())
print(b)