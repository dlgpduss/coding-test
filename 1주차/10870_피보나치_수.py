def fibo(n):
   if n == 0:
      return 0
   elif n <= 2:
      return 1
   else:
      res = fibo(n-1) + fibo(n-2)
      return res

s = int(input())

print(fibo(s))