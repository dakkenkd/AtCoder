from heapq import *
step = int(input())
h, w = map(int, input().split())

lst = []
trainer = []
dic = {"E":(0, 1), "W":(0, -1), "N":(1, 0), "S":(-1, 0)}
for i in range(h):
    L = list(input())
    for j in range(n):
        if L[j] == "A":
            start = (i, j)
        elif L[j] == "B":
            goal = (i, j)
        elif L[j] != ".":
            trainer.append((i, j, L[j]))
    lst.append(L)

g = [[-1]*w for _ in range(h)]
INF = 10**10
dist = [[INF]*w for _ in range(h)]
dist[start[0]][start[1]] = 0
# 重みグラフ
for num, d in enumerate(trainer):
    i, j, ii, jj = d[0], d[1], dic[d[2]][0], dic[d[2]][1]
    while True:
        if i+ii < 0 or i+ii >= h or j+jj < 0 or j+jj >= w: break
        if lst[i+ii][j+jj] != ".": break
        i += ii
        j += jj
        g[i][j] = num


# dijkstra
hq = deque([start])
nxt = [(0,1), (1,0), (-1,0), (0,-1)] # 進む方向によって適宜変えること
while q:
    c, v = heappop(hq)
    i, j = v[0], v[1]
    for d in nxt:
        ni, nj = i+d[0], j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if lst[ni][nj] == "#": continue
        if dist[ni][nj] > dist[i][j] + cc:
            dist[ni][nj] = dist[i][j] + cc
            heappush(hq, (dist[ni][nj], (ni, nj)))
