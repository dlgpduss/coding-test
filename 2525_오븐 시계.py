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