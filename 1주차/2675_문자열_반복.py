def concat(N, S):
    res = ""
    for i in S:
        res += i * int(N)
    return res

t = int(input())

for _ in range(t):
    N, S = input().split()
    N = int(N)
    print(concat(N, S))