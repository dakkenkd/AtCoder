from collections import deque
from pprint import pprint
h, w = map(int, input().split())
g = [["." == d for d in input()] for _ in range(h)]
q = deque([(0,0)])
dist = [[-1]*w for _ in range(h)]
dist[0][0] = 0
nxt = [(0,1), (1,0), (-1,0), (0,-1)]
while q:
    ij = q.popleft()
    i, j = ij[0], ij[1]
    for d in nxt:
        ni, nj = i+d[0], j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if g[ni][nj] == False: continue
        if dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + 1
            q.append((ni,nj)) # 0-1BFSの場合appendleft
print(g)
print(dist)
