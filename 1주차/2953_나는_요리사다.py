score = []
for i in range(5):
    num = list(map(int,input().split(" ")))
    sum = 0
    for j in num:
        sum += j
    score.append(sum)

max_num = 0
max_idx = 0

for i in range(5):
    if score[i] > max_num:
        max_num = score[i]
        max_idx = i

print(max_idx + 1, max_num)

# 다섯 번 입력을 받고 sum 저장 => 5개의 sum을 하나의 리스트에 넣기
#  => 가장 큰 값, 인덱스 + 1 구하기