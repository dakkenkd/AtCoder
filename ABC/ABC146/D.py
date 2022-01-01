from collections import deque
n = int(input())
g = [[] for _ in range(n)]
edges = []
for  _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    if a > b:
        a, b = b, a
    edges.append((a-1,b-1))

dist = [-1] * n
q = deque([(0,-1)])
dist[0] = -100000000
color = 2
dic = {}
dic[(0,1)] = 0
while q:
    e = q.popleft()
    v = e[0]
    color = 0
    for vv in g[v]:
        if dist[vv] != -1: continue
        if color == e[1]:
            color += 1
        dist[vv] = color
        q.append((vv, color))
        dic[( min(v,vv), max(v,vv) )] = color
        color += 1

print(max(dic.values())+1)
for e in edges:
    print(dic[e]+1)
