from heapq import *
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((c, b))
    g[b].append((c, a))

hq = [(0, 0)]
dist = [float("inf")] * n
path = [-1] * n
dist[0] = 0

while hq:
    c, v = heappop(hq)
    if dist[v] != c: continue
    for cc, vv in g[v]:
        if dist[vv] > dist[v] + cc:
            dist[vv] = dist[v] + cc
            path[vv] = v
            heappush(hq, (dist[vv], vv))

print(path)
print(dist)
