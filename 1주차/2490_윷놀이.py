for i in range(3):
    user_input = list(map(int, input().split(" ")))

    count = 0

    for j in user_input:
        if j == 1:
            count += 1
    
    if count == 4:
        print("E")
    elif count == 3:
        print("A")
    elif count == 2:
        print("B")
    elif count == 1:
        print("C")
    else:
        print("D")
