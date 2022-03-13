import sys
sys.setrecursionlimit(10**7)

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

order = [0] * n
dep = [0] * n
parent = [[-1]*18 for _ in range(n)]

pp = 0

def dfs(x, last=-1):
    global pp
    order[x] = pp # 行き掛け順
    pp += 1
    if last != -1:
        parent[x][0] = last # xの親
    for to in g[x]:
        if to == last: continue
        dep[to] = dep[x] + 1
        dfs(to, x)

dfs(0)

# ダブリング
for i in range(1, 18):
    for v in range(0, n):
        parent[v][i] = parent[parent[v][i-1]][i-1] # vの親の親

def la(x, k):
    for i in range(17, -1, -1):
        if (1 << i) <= k:
            k -= (1 << i)
            x = parent[x][i]
    return x

def lca(x, y):
    if dep[x] > dep[y]:
        x = la(x, dep[x] - dep[y]) # Level Ancestor
    if dep[x] < dep[y]:
        y = la(y, dep[y] - dep[x])

    if x == y: return x
    for i in range(17, -1, -1):
        if parent[x][i] != parent[y][i]:
            x, y = parent[x][i], parent[y][i]
    return parent[x][0]
