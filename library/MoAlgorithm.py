# https://atcoder.jp/contests/abc293/submissions/39711700
class MoAlgorithm():
    def __init__(self, block_size = -1, r_max = -1, query_list = []):
        if query_list:
            # 3次元だった場合
            if len(query_list[0]) == 3:
                self.query_list = query_list
            elif len(query_list[0]) == 2:
                self.query_list = [(q, l, r) for q, (l, r) in enumerate(query_list)]
            else:
                assert 0
        else:
            self.query_list = []

        self.data = self.Data()
        self.block_size = block_size
        if self.block_size < 0:
            self.block_size = int(len(query_list) ** 0.5 + 1)

        self.r_max = r_max
        if self.r_max < 0:
            self.r_max = 10**9
        self.ANS = []

    def solve(self):
        m = self.r_max
        if m < 0:
            for q, l, r in self.query_list:
                m = max(m, r)
        m += 1
        if len(self.ANS) < len(self.query_list):
            self.ANS += [0] * (len(self.query_list) - len(self.ANS))

        def key(I):
            _, x, y = I
            xx = x // self.block_size
            return xx * m * 2 + (y if x % 2 == 0 else ~y)

        self.query_list.sort(key=lambda x: key(x))

        l, r = 0, 0
        for q, ll, rr in self.query_list:
            while r < rr:
                self.data._add(r)
                r += 1
            while l > ll:
                l -= 1
                self.data._add(l)
            while r > rr:
                r -= 1
                self.data._del(r)
            while l < ll:
                self.data._del(l)
                l += 1
            self.ANS[q] = self.data.res

        return self.ANS

    class Data():
        def __init__(self):
            self.cnt = [0] * M
            self.res = 0

        def _add(self, i):
            a = A[i]
            c = self.cnt[i]
            self.res += c * (c - 1) // 2
            self.cnt += 1

        def _del(self, i):
            a = A[i]
            self.cnt[a] -= 1
            c = self.cnt[a]
            self.res -= c * (c - 1) // 2
