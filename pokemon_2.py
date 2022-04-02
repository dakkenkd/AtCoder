from collections import deque
step = int(input())
h, w = map(int, input().split())

lst = []
trainer = []
dic = {"E":(0, 1), "W":(0, -1), "N":(-1, 0), "S":(1, 0)}
for i in range(h):
    L = list(input())
    for j in range(w):
        if L[j] == "A":
            start = (i, j)
        elif L[j] == "B":
            goal = (i, j)
        elif L[j] != "." and L[j] != "#":
            trainer.append((i, j, L[j]))
    lst.append(L)

g = [[-1]*w for _ in range(h)]
INF = 10**10
dist = [[-1]*w for _ in range(h)]
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

# print(*g,sep="\n")

q = deque([start])

nxt = [(0,1), (1,0), (-1,0), (0,-1)] # 進む方向によって適宜変えること
while q:
    i, j = q.popleft()
    for d in nxt:
        ni, nj = i+d[0], j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if (lst[ni][nj] == "." or lst[ni][nj] == "B") and dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + 1
            q.append((ni,nj)) # 0-1BFSの場合appendleft

ans_dist = dist[goal[0]][goal[1]]
if len(trainer) >= 1:
    mx = 0
    gi, gj = goal[0], goal[1]
    colors = [0] * len(trainer)
    def dfs(v, d):
        i, j = v[0], v[1]
        if i == gi and j == gj and d == ans_dist:
            global mx
            mx = max(mx, sum([d >= 1 for d in colors]))
            return
        for ii, jj in nxt:
            ni, nj = i+ii, j+jj
            if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
            if dist[ni][nj] != d + 1: continue
            if g[ni][nj] != -1:
                colors[g[ni][nj]] += 1
            dfs((ni, nj), d+1)
            if g[ni][nj] != -1:
                colors[g[ni][nj]] -= 1

    dfs(start, 0)
else:
    mx = 0
# print(*dist,sep="\n")
print(ans_dist, mx)
