import sys
sys.setrecursionlimit(10**7)
n = int(input())
c = [*map(int, input().split())]
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
ans = [0] * n
color = [0] * (10**6)
visited = [-1] * n
visited[0] = 0
color[c[0]] = 1
def dfs(v, color):
    for vv in edges[v]:
        if visited[vv] != -1: continue
        if color[c[vv]] == 0:
            ans[vv] = 1
        color[c[vv]] += 1
        visited[vv] = v
        dfs(vv, color)
        color[c[vv]] -= 1

dfs(0, color)
print(1)
for i in range(n):
    if ans[i] == 1:
        print(i+1)
