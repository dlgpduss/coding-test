cnt = 0

a = input()
list = []
for i in range(len(a)):
    if i == 0:
        cnt += 10
    
    if i >= 1:
        if a[i] == a[i-1]:
            cnt += 5
        else:
            cnt += 10

print(cnt)