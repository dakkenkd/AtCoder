from collections import deque
n = int(input())
m = n-1
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v,w))
    edges[v].append((u,w))

dist = [-1] * n
dist[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    for vv in edges[v]:
        nxt = vv[0]
        w = vv[1]
        if dist[nxt] != -1: continue
        if w % 2 == 1:
            dist[nxt] = dist[v] ^ 1
        else:
            dist[nxt] = dist[v]
        q.append(nxt)

for d in dist:
    print(d)
