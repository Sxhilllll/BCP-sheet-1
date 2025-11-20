n = int(input())
id = list(map(int,input().split()))

if(n>0 and n<1000):
    for i in range(n):
        if(i%5==0):
            print(list(reversed(id)))
        else:
            print(-1)