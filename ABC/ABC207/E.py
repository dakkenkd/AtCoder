n = int(input())
A = [*map(int, input().split())]

sum_ = [0]*(n+1)
for i in range(n):
    sum_[i+1] = sum_[i] + A[i]

mem = [[0]*(n+1) for i in range(n+1)]
dp = [[0]*(n+1) for i in range(n+1)]
mem[1][0] = dp[0][0] = 1
mod = int(1e9 + 7)
for 
