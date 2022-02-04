from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    rg[b-1].append(a-1)

dist = [-1] * n
come = [-1] * n
backorder = [-1] * n
components = []

def dfs(v):
    come[v] = True
    for to in g[v]:
        if come[to]: continue
        dfs(to)
    backorder.append(v)

def rdfs(v):
    come[v] = True
    components[-1].append(v)
    for to in rg[v]:
        if come[to]: continue
        rdfs(to)

for i in range(n):
    if come[i]: continue
    dfs(i)

backorder.reverse()
come = [-1] * n
for v in backorder:
    if come[v]: continue
    components.append([])
    rdfs(v)

ans = 0

for component in components:
    n = len(component)
    ans += n * (n-1) // 2

print(ans)
