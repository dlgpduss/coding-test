import sys 

num = int(sys.stdin.readline())

height_list = []

for i in range(num):
    height_list.append(int(sys.stdin.readline())
)

height_list.reverse()

max_height = height_list[0]
count = 1

for j in height_list:
    if j > max_height:
        max_height = j
        count += 1

print(count)

# import sys
# input = sys.stdin.readline
# n = int(input())
# height = [] # 6 9 7 6 4 6
# for i in range(n):
#     height.append(int(input()))

# mx = 0
# cnt = 0
# for i in range(len(height)-1,-1,-1):
#     if mx < height[i]:
#         cnt += 1
#         mx = height[i]
# print(cnt)