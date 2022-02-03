from heapq import *
n, m = map(int, input().split())
g = [[] for _ in range(n)]

# グラフの作成
for _ in range(m):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    g[a].append((c, b))
    g[b].append((c, a))

hq = [(-1, 0)]
dist1 = [float("inf")] * n
dist1[0] = 0

while hq:
    c, v = heappop(hq)
    if dist1[v] != c: continue
    for cc, vv in g[v]:
        if dist1[vv] > dist1[v] + cc:
            dist1[vv] = dist1[v] + cc
            heappush(hq, (dist1[vv], vv))


hq = [(-1, n-1)]
dist2 = [float("inf")] * n
dist2[0] = 0

while hq:
    c, v = heappop(hq)
    if dist2[v] != c: continue
    for cc, vv in g[v]:
        if dist2[vv] > dist2[v] + cc:
            dist2[vv] = dist2[v] + cc
            heappush(hq, (dist2[vv], vv))

for i in range(n):
    if i == 0 or i == n-1:
        print(dist1[n-1])
    else:
        print(dist1[i] + dist2[i])
