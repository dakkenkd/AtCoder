l = int(input())
x = l - 12
def factorial_cor(n):
  fact = 1
  for integer in range(1, n + 1):
      fact *= integer
  return fact
ans = factorial_cor(11 + x)//(factorial_cor(11)*factorial_cor(x))
print(int(ans))