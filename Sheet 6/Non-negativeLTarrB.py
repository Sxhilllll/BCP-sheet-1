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
