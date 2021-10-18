import math
n,k = map(int, input().split())
lst = [int(i) for i in input().split()]
dp = [0]*n

for i in range(1,n):
  mn = float("inf")
  if i == 1:
    dp[i] = abs(lst[i] - lst[i-1])
    continue
  for j in range(i-1,max(-1, i-1-k),-1):
    x = dp[j] + abs(lst[i] - lst[j])
    mn = min(mn, x)
  dp[i] = mn
print(dp[-1])