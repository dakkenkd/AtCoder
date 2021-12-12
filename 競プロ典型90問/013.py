n, m = map(int, input().split())
G = [[] for _ in range(n)]

# グラフの作成
for _ in range(m):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b, c))
    G[b].append((a, c))
