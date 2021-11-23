# segfunc
def segfunc(x, y):
    return

# ide_ele
ide_ele = 0

class SegTree:
    """
    init(int_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l,r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        sefunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2の冪乗
        tree: セグメント木(1-index)
        """

        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length() # 2^p nを超える最小の2の冪乗
        self.tree = [ide_ele] * 2 * self.num # SegTreeには 2num - 1 個保存場所がいる。(1-indexなので 2 * num 個)
        # 配列の値を葉にセット
        for i in range(n): # SegTreeの一番下の段に値をセットしていく(num ~ num + n)
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1): # SegTreeの２段目以上に値をセットしていく
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1: # SegTreeのインデックスは1までなので
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k^1]) # k^1 は排他的論理和で、下位１ビットの1,0を入れ替える。（隣り合う箱を表現できる）
            k >>= 1 # (k //= 2)

    def query(self, l, r):
        """
        [l,r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
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
