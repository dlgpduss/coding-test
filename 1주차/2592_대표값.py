# num = []
# total = 0

# for i in range(10):
#     a = (int(input()))
#     total += a
#     num.append(i)


# print(int(total / 10))


  # 최빈값 구하는거 => 딕셔너리 가능한지?

  
'''
x = 10 / 10 =? 1
40 / 10
30 
6
3
2
6
3
4
5

list = [0, 1, 1, 3, 2, 1, 2, 0, 0, 0]
list[x/10] += 1
list.index(max(list)) => 3(index (30)) * 10 => 30
'''
list = [0]*1000
sum = 0
for i in range(10):
    x = int(input())
    list[x] += 1
    sum += x
res = list.index(max(list))
print("%d\n%d"%(sum//10, res))
