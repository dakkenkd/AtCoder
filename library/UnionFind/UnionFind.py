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
