from collections import deque
import sys
sys.setrecursionlimit(10**7)
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

child = [-1] * n
dist = [-1] * n
dist[0] = 0
def dfs(v, pre):
    cnt = 0
    for vv in G[v]:
        if pre == vv: continue
        dist[vv] = dist[v] + 1
        cnt += dfs(vv, v)
    child[v] = cnt+1
    return cnt + 1
answer = [0] * n
answer[0] = sum(dist)
def dfs2(v, pre, ans):
    answer[v] = ans + n - child[v]
    for vv in G[v]:
        if vv == pre: continue
        dfs(vv, v, answer[v])
print(answer)
