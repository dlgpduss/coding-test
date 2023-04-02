# n = int(input()) # 6

# num = []
# for i in range(1, n+1):
#     num.append(i)

# while len(num) > 1:
#         num.pop(0)
#         a = num[0]
#         num.append(a)

# print(num)

'''
1234 => 1버리기 1번쨰
234 => 2 아래로 옮기기 2번쨰
342 => 3 버리기 3번째
42 => 4 아래로 옮기기 4번째
24 => 2 버리기 5번째
4

'''
# from collections import deque

# n = int(input()) # 6
# # 1 2 3 4 5 6
# card = deque(map(int, range(1, n+1)))
# while len(card) > 1:
#     card.popleft() # 맨 앞 카드를 버린다.
#     card.append(card.popleft())
# print(card[0]) # 4


from collections import deque

n = int(input())
card = deque(map(int, range(1, n + 1)))

while (len(card) > 1):
    card.popleft() # 맨 앞 카드 버리기
    card.append(card.popleft())
print(card[0])