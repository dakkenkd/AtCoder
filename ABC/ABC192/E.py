from heapq import heapify, heappush, heappop
n, m, x, y = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a,b,t,k = map(int, input().split())
    g[a-1].append((k, t, b-1))
    g[b-1].append((k, t, a-1))

INF = float("inf")
dist = [INF] * n
dist[x-1] = 0

hq = [(0, x-1)]

while hq:
    time, v = heappop(hq)
    if time != dist[v]: continue
    for interval, time, nxt_v in g[v]:
        wait_time = (interval - time) % interval
        if dist[v] + time + wait_time < dist[nxt_v]:
            dist[nxt_v] = dist[v] + wait_time + time
            heappush(hq, (dist[v] + wait_time + time, nxt_v))
if dist[y-1] == INF:
    print(-1)
else:
    print(dist[y-1])
