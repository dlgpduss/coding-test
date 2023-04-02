n = int(input())

t = list(map(int, input().split()))

# 시간이 적게 걸리는 사람 순서대로 정렬
t.sort()

'''
1
1 + 2 => 3
1 + 2 + 3 => 6
1 + 2 + 3 + 3 => 9
1 + 2 + 3 + 3 + 4 => 13

총 시간: 1 + 3 + 6 + 9 + 13 => 32

세로 기준
1 * 5
2 * 4
3 * 3
3 * 2
4
로 생각해서 계산
'''

total = 0

for i in range(n):
    total += t[i] * n
    n -= 1

print(total)