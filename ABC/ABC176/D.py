from collections import deque
from heapq import *
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
g = [["." == d for d in input()] for _ in range(h)]
q = deque([(ch-1, cw-1)])
INF = 10**9
dist = [[INF]*w for _ in range(h)]
dist[ch-1][cw-1] = 0
nxt = [(0,1), (1,0), (-1,0), (0,-1)] # 進む方向によって適宜変えること
nxt_warp = []
for i in range(-2,3):
    for j in range(-2,3):
        if i == j == 0: continue
        if (i,j) in nxt: continue
        nxt_warp.append((i, j))

# BFS
while q:
    ij = q.popleft()
    i, j = ij[0], ij[1]
    flag = False
    for d in nxt:
        ni, nj = i+d[0], j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if g[ni][nj] == False:
            flag = True
            continue
        if dist[ni][nj] > dist[i][j]:
            dist[ni][nj] = dist[i][j]
            q.appendleft((ni,nj)) # 0-1BFSの場合appendleft
    if flag:
        for d in nxt_warp:
            ni, nj = i+d[0], j+d[1]
            if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
            if g[ni][nj] == False: continue
            if dist[ni][nj] > dist[i][j] + 1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni,nj)) # 0-1BFSの場合appendleft

print(dist[dh-1][dw-1] if dist[dh-1][dw-1] != INF else -1)
