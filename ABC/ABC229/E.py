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
edges = [[] for _ in range(n)]
par = [-1] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
ans = [0]
cnt = 0

for i in range(n-1, 0, -1):
    cnt += 1
    for v in edges[i]:
        if v < i: continue
        if not same(v, i):
            cnt -= 1
            union(v, i)
    ans.append(cnt)

for d in reversed(ans):
  print(d)
