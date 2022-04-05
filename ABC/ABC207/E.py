n = int(input())
lst = [*map(int, input().split())]
acc = [0]
for i in range(n):
    acc.append(acc[-1]+lst[i])
mod = 10**9+7
dp = [[0]*(n+1) for _ in range(n+1)]
memo = [[0]*(n+1) for _ in range(n+1)]
memo[1][0] = 1

for i in range(n):
    for j in range(1,n+1):
        dp[i+1][j] = memo[j][acc[i+1]%j]
    for j in range(2,n+1):
        memo[j][acc[i+1]%j] += dp[i+1][j-1]
        memo[j][acc[i+1]%j] %= mod

print(sum(dp[n])%mod)
