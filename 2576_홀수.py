odd_sum = 0
num = []

for i in range(0,7):
    data = int(input())
    if data % 2 != 0:
        odd_sum += data
        num.append(data)
if odd_sum == 0:
    print(-1)
else:
    print(odd_sum)
    print(min(num))