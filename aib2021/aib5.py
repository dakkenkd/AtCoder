from pprint import pprint
from collections import deque
g = []

# while True:
#     try:
#         s = list(input().split())
#         g.append(s)
#     except:
#         break

n = int(input())
for i in range(n):
    s = list(input().split())
    g.append(s)

w = len(g[0])
h = len(g)
dij = [(0,1), (1,0), (-1,0), (0,-1)]
danchi = []
for i in range(h):
    for j in range(w):
        if g[i][j] == "X":
            danchi.append((i,j))
def bfs(start):
    q = deque([start])
    dist = [[-1]*w for _ in range(h)]
    dist[start[0]][start[1]] = 0
    # bfsをする
    while q:
        v = q.popleft()
        ii, jj = v[0], v[1]
        for d in dij:
            ni, nj = ii+d[0], jj+d[1]
            if ni< 0 or ni >= h or nj < 0 or nj >= w: continue
            if g[ni][nj] == "1": continue
            if dist[ni][nj] == -1:
                dist[ni][nj] = dist[ii][jj] + 1
                q.append((ni,nj))
    ret = 0
    for d in danchi:
        if dist[d[0]][d[1]] == -1:
            ret = float("inf")
            break
        ret += dist[d[0]][d[1]]
    return ret, dist

ans = float("inf")
zahyou = (-1,-1)
for i in range(h):
    for j in range(w):
        if g[i][j] == "0":
            x, dist = bfs((i,j))
            if ans > x:
                ans = x
                zahyou  = (i,j)

print(zahyou[1], zahyou[0])
