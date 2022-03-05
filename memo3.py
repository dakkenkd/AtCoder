n = int(input())
mod = 998244353

dp = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(1,n):
    for j in range(1,10):
        if 1 <= j-1:
            dp[i+1][j] += dp[i][j-1]
        if j+1 <= 9:
            dp[i+1][j] += dp[i][j+1]
        dp[i+1][j] %= mod

print(sum(dp[n]))
