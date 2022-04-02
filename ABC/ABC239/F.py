from collections import deque
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

def get_all_members():
    pare_dic = {}
    for i in range(n):
        parent = find(i)
        pare_dic.setdefault(parent, [])
        pare_dic[parent].append(i)
    return list(pare_dic)

n, m = map(int, input().split())
deg = [*map(int, input().split())]

# 次数の総和は偶数であり、木の場合は(n-1)*2でないといけない
if sum(deg) != (n-1)*2: exit(print(-1))

rem = deg[:]

par = [-1] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    rem[a] -= 1
    rem[b] -= 1
    # 次数が一致しないことがわかった場合終了
    if rem[a] < 0 or rem[b] < 0: exit(print(-1))
    # ループができてしまった場合木を構築できないので終了
    if same(a, b): exit(print(-1))

    union(a, b)

# グループを配列にまとめたもの
uf_group = get_all_members()
gs = []

for vs in uf_group:
    q = deque()
    for v in vs:
        # 残っている次数の分だけqueにブチ込む
        for _ in range(rem[v]):
            q.append(v)
    # 連結成分から辺が出ていない場合木を構築できないので終了
    if q == []: eixt(print(-1))

    gs.append(q)

# グループ内の残り次数が大きい順にソート
gs.sort(key=lambda x: len(x), reverse=True)


chi_i = 1
ans = []

for pare_i in range(len(gs)):
    length = len(gs[pare_i])
    for i in range(length):
        pare_p = gs[pare_i].popleft()
        chi_p = gs[chi_i].popleft()
        chi_i += 1 # 配列外参照してしまわないか心配だが木なので大丈夫
        ans.append((pare_p+1, chi_p+1))

for a, b in ans:
    print(a, b)
