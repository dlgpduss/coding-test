### 모르겠음

num = int(input())

str_list = []

for i in range(num):
    a = list(map(str, input().split(" ")))
    str_list.append(a)

count = 0
for i in range(len(str_list)):
    str = str_list[i]
    for j in range(len(str)):
        if str[j - 1] == "O" and str[j] == "O":
            count += 1


print(str_list)
print(count)