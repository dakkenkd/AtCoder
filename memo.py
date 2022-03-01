from bisect import bisect_left, bisect_right

class FenwickTree:

    def __init__(self, n, lst):
        self.arr = lst
        self.x2i = {d:i+1 for i, d in enumerate(sorted(set(lst)))}
        self.i2x = {i+1:d for i, d in enumerate(sorted(set(lst)))}
        self.comp_arr = [self.x2i[d] for d in lst]
        self.bit = [0] * (len(lst) + 10)
        self.n = n

    def bit_add(self, x, w): # x: 加算したい場所, w: 加算したい値
        x = self.x2i[x]
        while x <= self.n:
            self.bit[x] += w
            x += x & -x

    def bit_sum(self, l, r):
        l, r = self.x2i[l]-1, self.x2i[r]
        r_sum = 0
        l_sum = 0
        while r > 0:
            r_sum += self.bit[r] # 現在のブロックの値を足していく
            r -= r & -r # 左上のブロックに移動していく
        while l > 0:
            l_sum += self.bit[l]
            l -= l & -l
        return r_sum - l_sum

# bit_sum() に入れるのは index なので, BIT.x2i[x] などで座標圧縮後の index に直してからつっこむ

q = int(input())
query = []
X = []

# クエリ先読み
for _ in range(q):
    L = tuple([*map(int, input().split())])
    X.append(L[1])
    if L[0] != 1:
        X.append(L[2])
    query.append(L)
X.sort()
BIT = FenwickTree(len(X), X)

for d in query:
    if d[0] == 1:
        BIT.bit_add(d[1], 1)
    elif d[0] == 2:
        x, k = d[1], d[2]
        idx = BIT.x2i[x]
        ok = 0
        ng = idx
        s = BIT.bit_sum(0, idx)
        if s < k:
            print(-1)
            continue
        while ng - ok > 1:
            mid = (ng+ok)//2
            if BIT.bit_sum(mid, idx) >= k:
                ok = mid
            else:
                ng = mid
        print(BIT.i2x[ok])
    else:
        x, k = d[1], d[2]
        idx = BIT.x2i[x]
        ng = idx-1
        ok = BIT.n
        s = BIT.bit_sum(idx, BIT.n)
        if s < k:
            print(-1)
            continue
        while ok - ng > 1:
            mid = (ok+ng) // 2
            if BIT.bit_sum(idx-1, mid) >= k:
                ok = mid
            else:
                ng = mid
        print(BIT.i2x[ok])
