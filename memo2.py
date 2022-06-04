from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = int(input())

def dfs(v, pre, dist, k):
    if dist > k:return
    global ans
    ans += v+1
    visited.add(v)
    for vv in g[v]:
        if vv in visited: continue
        dfs(vv, v, dist+1, k)

for _ in range(q):
    x, k = map(int, input().split())
    x -= 1
    dist = dict()
    dist[x] = 0
    ans = x
    q = deque([x])
    while q:
        v = q.popleft()
        for vv in g[v]:
            if vv in dist: continue
            if dist[v] + 1 <= k:
                ans += vv+1
                dist[vv] = dist[v] + 1
                q.append(vv)
    print(ans)
