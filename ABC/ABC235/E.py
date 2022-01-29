from heapq import *
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

n, m, q = map(int, input().split())
edges = []
for i in range(m):
    a,b,c = map(int, input().split())
    heappush(edges, (c, a-1, b-1, i, 0))
for i in range(q):
    u, v, w = map(int, input().split())
    heappush(edges, (w, u-1, v-1, i, 1))

par = [-1] * n
ans = [-1] * m
while edges:
    c, a, b, i, flag = heappop(edges)
    print(flag, i, par)
    if flag and not same(a, b):
        ans[i] = 1
        continue
    if not same(a, b):
        union(a, b)
for d in ans:
    if d:
        print("Yes")
    else:
        print("No")
