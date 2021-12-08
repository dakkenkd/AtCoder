from collections import deque
import sys
sys.setrecursionlimit(10**7)
h, w = map(int, input().split())
edges = [[] for _ in range(h*w)]
def f(s):
    if s==".":
        return 1
    else:
        return 0
# 0と1の配列に変える(変える必要ないけど)
lst = [[*map(f, list(input()))] for _ in range(h)]

move = [[0,1], [1,0], [-1,0], [0,-1]]
start = 0
for i in range(h):
    for j in range(w):
        if lst[i][j] == 0: continue
        for d in move:
            x, y = i+d[0], j+d[1]
            if 0 <= x <= h-1 and 0 <= y <= w-1:
                if lst[x][y] == 1:
                    edges[i*w + j].append(x*w + y)
                    start = x*w + y

# 全ての始点からBFSしてdistの最大値を出力

def bfs(start):
    q = deque([start])
    dist = [-1]* (h*w)
    dist[start] = 0
    while q:
        v = q.popleft()
        for vv in edges[v]:
            if dist[vv] != -1: continue
            dist[vv] = dist[v] + 1
            q.append(vv)
    return max(dist)


ans = 0

for i in range(h):
    for j in range(w):
        if lst[i][j] == 0: continue
        ans = max(bfs(i*w+j), ans)
print(ans)
