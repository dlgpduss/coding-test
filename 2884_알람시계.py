H, M = map(int, input().split())

if M <= 44:
    if H == 0:
        print(23 , (M + 60) - 45)
    else:
        print(H-1, (M + 60) - 45)
else:
    print(H, M -45)