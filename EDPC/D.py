N,W = map(int, input().split())
lst = []
for _ in range(N):
  w,v = map(int, input().split())
  lst.append([w,v])

dp = [[0]*100010 for _ in range(110)]

# DP
for i in range(N):
  w = lst[i][0]
  v = lst[i][1]
  for j in range(W+1):
    if j - w < 0:
      dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    else:
      dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j])

print(max(dp[N]))