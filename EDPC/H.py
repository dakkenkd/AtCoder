from collections import deque
import pprint
h, w = map(int, input().split())
g = [["." == d for d in input()] for _ in range(h)]
nxt = [(1,0),(0,1)] # 進む方向によって適宜変えること
q = deque([(0,0)])
dist = [[-1]*w for _ in range(h)]
dist[0][0] = 1
mod = 10**9+7

while q:
    ij = q.popleft()
    i, j = ij[0], ij[1]
    for d in nxt:
        ni, nj = i+d[0], j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if g[ni][nj] == False: continue
        if dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j]
            q.append((ni,nj)) # 0-1BFSの場合appendleft
        else:
            dist[ni][nj] += dist[i][j]
            dist[ni][nj] %= mod

print(max(0, dist[h-1][w-1]))
