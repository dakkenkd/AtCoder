n, m, k = map(int, input().split())
lst = [*map(lambda x: int(x)-1, input().split())]
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append((b-1, i))
    g[b-1].append((a-1, i))

edge_cnt = [0] * (n-1)

def dfs(v, end):
    print(edge_cnt)
    if v == end:
        return True
    flag = False
    seen[v] = True
    for vv, i in g[v]:
        if seen[vv]: continue
        edge_cnt[i] += 1
        flag = dfs(vv, end)
        if flag:
            break
        edge_cnt[i] -= 1
    return flag

for i in range(m-1):
    seen = [False] * n
    dfs(lst[i], lst[i+1])

# R = K + B
# S = R + B とすると, B = S - R
# R = K + (S - R)
# R = (K + S) / 2 となる辺の選び方を求める -> DP
k = abs(k)
if (sum(edge_cnt) - k)%2 == 1 or sum(edge_cnt)<k:
    exit(print(0))

ans = (sum(edge_cnt) + k) // 2 

dp = [[0]*(ans+1) for _ in range(n)]

dp[0][0] = 1
mod = 998244353

for i in range(n-1):
    for j in range(ans+1):
        if j-edge_cnt[i-1] >= 0:
            dp[i+1] = (dp[i][j-edge_cnt[i-1]] + dp[i][j]) % mod
        else:
            dp[i+1] = dp[i][j] % mod

print(dp[n-1][ans])
