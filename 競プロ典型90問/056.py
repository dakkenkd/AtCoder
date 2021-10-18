n,s = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-1]*(s+1) for _ in range(n+1)]
dp[0][0] = 0

for i, (a,b) in enumerate(ab):
  for j in range(s-min(a,b)+1):
    if dp[i][j] == -1: continue
    for p in [a,b]:
      if j + p > s: continue
      dp[i+1][j+p] = (p == b)

if dp[n][s] == -1:
  print("Impossible")
else:
  ans = ""
  j = s
  for i in range(n-1, -1, -1):
    k = dp[i+1][j]
    ans += "AB"[k]
    j -= ab[i][k]
  print(ans[::-1])