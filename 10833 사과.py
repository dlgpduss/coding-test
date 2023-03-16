num = int(input())

result = 0

for i in range(num):
    info = list(map(int, input().split()))
    result += info[1] % info[0]
print(result)