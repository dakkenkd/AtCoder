from collections import deque

inf = 10**9
dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
int1 = lambda x: int(x) - 1

h,w = map(int, input().split())
rs, cs = map(int1, input().split())
rt, ct = map(int1, input().split())
c = [x == "#" for _ in range(h) for x in input()]

dp = [[inf]*h*w for _ in range(4)]
q = deque()

# 初期化
for k in range(4):
  q.append((rs*w + cs, k))
  dp[k][rs*w+cs] = 0

while q:
  ij, k = q.popleft()
  cost = dp[k][ij]

  if ij == (rt*w+ct):
    print(cost)
    exit()

  # マスの中で方向転換
  for nk in range(4):
    # 四方のマスでコストが同じ（進む必要がないます）は飛ばす
    if cost+1 >= dp[nk][ij]: continue
    dp[nk][ij] = cost+1
    q.append((ij, nk)) # 現在地よりもコストが高ければ更新するために進む

  # 向いている方向に1マス進む
  i, j = divmod(ij, w)
  di, dj = dij[k]
  ni, nj = i+di, j+dj
  if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
  nij = ni*w+nj
  if c[nij]: continue
  if cost >= dp[k][nij]: continue
  dp[k][nij] = cost
  q.appendleft((nij, k))
