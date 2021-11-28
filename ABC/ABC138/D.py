n, q = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
P = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    P[p-1] += x

print(P)
cnt = [0] * n

def dfs(pre, v, p):
    p += P[v]
    cnt[v] = p
    for vv in edges[v]:
        if vv == pre: continue
        dfs(v, vv, p)

print(cnt)
