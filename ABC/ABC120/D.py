n, m = map(int, input().split())
lst = []
for _ in range(m):
    a,b = map(int, input().split())
    lst.append((a,b))

par = [-1] * (n+1)

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

ans = [n*(n-1)//2]
inc = n*(n-1)//2
for i in range(m-1, -1, -1):
    a,b = lst[i]
    if not same(a, b):
        inc -= par[root(a)] * par[root(b)]
        union(a, b)
    ans.append(inc)
for i in range(len(ans)-2, -1, -1):
    print(ans[i])
