n, w = map(int, input().split())
lst = [[*map(int, input().split())] for _ in range(n)]
dp = [[float("inf")] * 100010 for i in range(110)]
dp[0][0] = 0

for i in range(n):
    V = lst[i][1]
    W = lst[i][0]
    for j in range(100010):
        if j - V >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-V] + W)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

ans = 0
L = []
for i in range(100001):
    if dp[n][i] <= w:
        ans = i

print(ans)