import sys

a = int(input())
num = sys.stdin.read(a)

total = 0
for i in num:
    total += int(i)

print(total)