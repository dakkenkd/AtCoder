from collections import deque
import math
import pprint
h,w = map(int, input().split())
g = [[] for i in range(h)]
for i in range(h):
  s = list(input())
  for j in range(w):
    if s[j] == ".":
      g[i].append(True)
    elif s[j] == "#":
      g[i].append(False)
    if s[j] == "s":
      start = (i,j)
      g[i].append(True)
    elif s[j] == "g":
      goal = (i,j)
      g[i].append(True)

dp = [[3]*w for i in range(h)]
dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dp[start[0]][start[1]] = 0
q = deque()
q.append(start)

while q:
  ij = q.popleft()
  i, j = ij[0], ij[1]
  cost = dp[i][j]
  if ij == goal:
    break
  for d in dij:
    ni, nj = i+d[0], j+d[1]

    if ni < 0 or ni >= h or nj < 0 or nj >= w: continue

    if g[ni][nj]:
      if dp[ni][nj] > dp[i][j]:
        dp[ni][nj] = cost
        q.appendleft((ni,nj))
    else:
      if dp[i][j] + 1 > 2 or dp[ni][nj] != 3:
        continue
      dp[ni][nj] = dp[i][j] + 1
      q.append((ni,nj))

if dp[goal[0]][goal[1]] > 2:
  print("NO")
else:
  print("YES")
