n = int(input()) # 6
res = []
for i in range(n):
    str = input()
    myStack = []
    chk = 0 # chk == 0 YES / 1 NO
    for j in range(len(str)):
        if str[j] == "(":
            myStack.append(str[j])
        else:
            if len(myStack) == 0:
                chk = 1
                break
            else:
                myStack.pop()
    if chk == 1 or len(myStack) != 0:
        res.append("NO")
    else:
        res.append("YES")
print(*res, sep='\n')