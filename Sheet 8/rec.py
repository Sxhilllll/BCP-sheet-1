# Ques. Given a string calculate the length of the largest palindromic substring...

str = "abacab"
m = len(str)
max_len = 1
for i in range(m):
    for j in range(i,m):
        sub = str[i:j+1]
        if sub == sub[::-1]:
            if len(sub) > max_len:
                max_len = len(sub)
print(max_len)

# Ques. given a numer and index i, print ith bit of n



