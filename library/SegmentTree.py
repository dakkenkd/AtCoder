def segfunc(x, y):
    return x+y
"""
操作 segfunc 単位元
最小値 min(x,y) math.inf
最大値 max(x,y) -math.inf
区間和 x+y 0
区間積 x*y 1
最大公約数 math.gcd(x,y) 0
"""
class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele] * (2 * self.num)

        # セグ木の初期化
        for i in range(n):
            self.tree[self.num+i] = init_val[i]

        # 上まで値を計算しておく
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k>>1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k>>1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

    def query(self, l, r):
        # [l, r)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
