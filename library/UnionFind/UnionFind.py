n = int(input())
par = [i for i in range(1+n)]

# find (経路圧縮)
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

# お互いの親が一緒であるかを確認して同じグループかどうかを判断する
def same(x,y):
    return find(x) == find(y)

# それぞれの親を確認して異なる場合のみ親を統一する
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y