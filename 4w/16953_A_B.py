f, l = map(int, input().split())

# 끝 => 처음
count = 1

while (f != l):
    count += 1
    if f == l:
        break
    tmp = l
    if l % 10 == 1:
        l //= 10
    elif l % 2 == 0:
        l //= 2
    if  tmp == l:
        count -= 1
        break
print(count)