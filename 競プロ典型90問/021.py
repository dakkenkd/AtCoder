from collections import deque
import sys
sys.setrecursionlimit(10**6)
def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def union(x, y):
    xx = root(x)
    yy = root(y)
    if xx == yy:
        return
    else:
        par[xx] += par[yy]
        par[yy] = xx

def same(x, y):
    xx = root(x)
    yy = root(y)
    return xx == yy

n, m = map(int, input().split())
g = [[] for _ in range(n)]
edges = []
for i in range(n):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    edges.append([a,b])

dist = [-1] * n
par = [-1] * n

# 道をたどって同じ連結成分に入れる
def union_nodes(v):
    if not same(v, dist[v]):
        union(v, dist[v])
        union_nodes(dist[v])

for i in range(n):
    if dist[i] != -1: continue
    q = deque([i])
    while q:
        v = q.pop()
        for vv in g[v]:
            if dist[vv] != -1:
                union_nodes(vv)
            dist[vv] = v
            q.append(vv)

print(par)
print(dist)
