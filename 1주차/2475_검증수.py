num = list(map(int, input().split()))

total = 0

for i in num:
    total += i ** 2

result = total % 10
print(result)