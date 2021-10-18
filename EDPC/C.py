n = int(input())
lst = []
for _ in range(n):
  a,b,c = map(int, input().split())
  lst.append([a,b,c])

dp = [[-1,-1,-1] for _ in range(n)]
s = [0,1,2]
for i in s:
  dp[0][i] = lst[0][i]

for day in range(1,len(lst)):
  for i in s:
    for j in s:
      if i == j: continue
      dp[day][j] = max(dp[day-1][i] + lst[day][j], dp[day][j])
print(max(dp[-1]))