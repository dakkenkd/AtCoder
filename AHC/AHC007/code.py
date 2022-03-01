import sys
import random
input = lambda: sys.stdin.readline().rstrip()

N = 400
M = 1995

graph = [[] for _ in range(N)]

# 座標取得
XY = [list(map(int,input().split())) for _ in range(N)]

# 辺の関係取得
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
 
for _ in range(M):
    candidate = int(input())
    print(1)
    sys.stdout.flush() # ←これは絶対に行う
