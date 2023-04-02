'''
N = 7, K = 3 

1 2 3 4 5 6 7 

<3, 6, 2, 5, 1, 4>

'''

import queue

n, k = map(int, input().split(" "))

num = []
for i in range(1, n+1): # range (1, 8) => 1, 2, 3, 4, 5, 6, 7
    num.append(i)

res = []
idx = 0

for j in range(n): # range(7)
    idx += (k - 1) # idx = 2 + 2  => 4
    if idx >= len(num):
        idx = idx % len(num)
    res.append(str(num[idx]))
    num.pop(idx)
res_join = ", ".join(res)
print("<" , res_join, ">", sep="")