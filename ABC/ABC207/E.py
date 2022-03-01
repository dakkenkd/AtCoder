n = int(input())
lst = [*map(int, input().split())]

sum_ = [0]*(n+1)
for i in range(n):
    sum_[i+1] = sum[i] + A[i]

mem = [[0]*(n+1) for i in range(n+1)]
dp = [[0]*(n+1) for i in range(n+1)]
mem[1][0] = dp[0][0] = 1
mod = int(1e9+7)

for i in range(n):
    for j in range(1, n+1):
        dp[i+1][j] = mem[j][sum_[i+1]%j]
    for j in range(2, n+1):
        mem[j][sum_[i+1]%j] += dp[i+1][j-1]
        mem[j][sum_[i+1]%j] %= mod

ans = sum(dp[n])%mod
print(ans)
