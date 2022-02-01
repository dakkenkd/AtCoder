from heapq import *
n, m = map(int, input().split())
lst = [*map(int, input().split())]
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    cost = lst[a-1] - lst[b-1]
    # プラスを優先したいので正負反転
    if cost >= 0:
        c_ab = 0
        c_ba = cost
    else:
        c_ab = -cost
        c_ba = 0
    g[a-1].append((c_ab, b-1))
    g[b-1].append((c_ba, a-1))

# dijkstra
hq = [(0,0)]
dist = [float("inf")] * n
dist[0] = 0

while hq:
    cost, v = heappop(hq)
    if dist[v] != cost: continue # 辺の候補のうち、最短経路に使われなかったものを飛ばす
    for cc, vv in g[v]:
        if dist[vv] > dist[v] + cc: # すでに確定された点ではなかった場合
            dist[vv] = dist[v] + cc
            heappush(hq, (dist[vv], vv))

ans = [0]

for i in range(1,n):
    ans.append(lst[0] - (lst[i] + dist[i]))

print(max(ans))
