# n = int(input())
# stack = []
# answer = []
# flag = 0
# cur = 1

# for i in range(n):
#     num = int(input())
#     while cur <= num:
#         stack.append(cur)
#         answer.append("+")
#         cur += 1

#     if stack[-1] == num:
#         stack.pop()
#         answer.append("-")
#     else:
#         print("No")
#         flag = 1
#         break

# if flag == 0:
#     for i in answer:
#         print(i)




import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
last = 1
result = ''
num = []

for i in range(n):
    num.append(int(input()))

for j in num:
    if j > stack[-1]:
        while j > stack[-1]:
            stack.append(last)
            last += 1
            result += '+\n'
        stack.pop()
        result += '-\n'
    elif j == stack[-1]:
        stack.pop()
        result += '-\n'
    else:
        result = 'No'
        break

print(result)