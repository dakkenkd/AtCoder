n = int(input())
lst = [*map(int, input().split())]
c = [1,0,0,0]
for d in lst:
    c[a] += 1
c0, c1, c2, c3 = c

dp = [[[0]*(c1+c2+c3+1) for _ in range(c2+c3+1)] for _ in range(c3+1)]

for i in range(c3+1):
    for j in range(c2+c3+1-i):
        for k in range(c1+c2+c3+1-i-j):
            if i+j+k == 0: continue
            dp[i][j][k] = n
            if i != 0:
                dp[i][j][k] += dp[i-1][j+1][k]*i
            if j != 0:
                dp[i][j][k] += dp[i][j-1][k+1]*j
            if k != 0:
                dp[i][j][k] += dp[i][j][k-1]*k
            dp[i][j][k] /= i+j+k

print(dp[c3][c2][c1])
