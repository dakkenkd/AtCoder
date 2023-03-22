n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

order = [0] * n
dep = [0] * n
parent = [[-1]*18 for _ in range(n)]
parent[0][0] = -2
pp = 0
q = [0]
while q:
    v = q.pop()
    order[v] = pp
    pp += 1
    for vv in g[v][::-1]:
        if parent[vv][0] == -1:
            parent[vv][0] = v
            q.append(vv)

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
