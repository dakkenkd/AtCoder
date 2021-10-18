n = int(input())
lst = [int(i) for i in input().split()]
lst = lst
dp = [0]*n

for i in range(1,n):
  if i == 1:
    x = abs(lst[i] - lst[i-1])
    dp[i] = x
    continue
  x1 = dp[i-1] + abs(lst[i] - lst[i-1])
  x2 = dp[i-2] + abs(lst[i] - lst[i-2])

  dp[i] = min(x1, x2)
print(dp[-1])