a = list(input())
s = []
b = 0

for i in range(len(a)):
    if a[i] == "(":
        s.append("(")
    else:
        if a[i - 1] == "(":
            s.pop()
            b = b + len(s)
        else:
            s.pop()
            b = b + 1

print(b)



s = input()

stack = []
pieces = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':  #레이저가 발사되어 잘린 쇠막대기 개수
            stack.pop()
            pieces += len(stack)
        else:  # 쇠막대기 하나 빼내고 잘린 쇠막대기 증가
            stack.pop()
            pieces += 1

print(pieces)