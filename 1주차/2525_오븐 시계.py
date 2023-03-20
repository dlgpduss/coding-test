h, m = map(int, input().split())
time = int(input())

hour = int(time / 60)
minute = time % 60

total_hour = h + hour
total_min = m + minute

if total_min == 60:
    if total_hour >= 23:
        print(total_hour - 23, 0)
    else:
        print(total_hour + 1, 0)
elif total_min > 60:
    if total_hour >= 23:
        print(total_hour - 23, total_min - 60)
    else:
        print(total_hour + 1, total_min - 60)
elif total_min < 60:
    if total_hour >= 24:
        print(total_hour - 24, total_min)
    else:
        print(total_hour, total_min)


# 더 간단한 방법 있는지 ㅜㅜ

# H, M = map(int, input().split())
# A = int(input())
# M = M + A
# H = H + M//60
# M = M % 60
# if (H>=24):
#     H = H - 24
# print(H, M)