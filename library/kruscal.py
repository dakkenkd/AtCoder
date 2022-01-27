import sys
sys.setrecursionlimit(10**6)
def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def union(x, y):
    xx = root(x)
    yy = root(y)
    if xx == yy:
        return
    else:
        par[xx] += par[yy]
        par[yy] = xx

def same(x, y):
    xx = root(x)
    yy = root(y)
    return xx == yy

n, m = map(int, input().split())
G = [[] for _ in range(n)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    edges.append(c,a,b)

# 重みが小さい順に辺を並べ替える
edges.sort()
par = [-1] * n

for e in edges:
    # この辺を使っても閉路ができない場合最小全域木に使う辺である
    if not same(e[1], e[2]):
        G[e[1]].append(e[2])
        G[e[2]].append(e[1])
        union(e[1], e[2])
