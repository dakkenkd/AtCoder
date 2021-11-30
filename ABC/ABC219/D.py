n = int(input())
x, y = map(int, input().split())
lst = [[*map(int, input().split())] for _ in range(n)]
INF = 10**10

dp = [[INF for j in range(y+1)] for i in range(x+1)]
dp[0][0] = 0

for i in range(n):
    a, b = lst[i][0], lst[i][1]
    for X in range(x, -1, -1):
        for Y in range(y, -1, -1):
            if dp[X][Y] != INF:
                A = min(x, X+a)
                B = min(y, Y+b)
                dp[A][B] = min(dp[A][B], dp[X][Y] + 1)

print(dp[x][y] if dp[x][y] != INF else -1)
