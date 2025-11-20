n = int(input())
count = 0
for i in range(n):
    data = input().split()
    marks = int(data[0])
    att = int(data[1])
    if(marks>=75 and att>=80):
        count +=1
print(count)
