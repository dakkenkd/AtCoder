# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.n0 = 2**(n-1).bit_length()
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def init(self, A):
        self.data[1:] = A
        for i in range(1, self.n):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i)] += self.data[i]
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)
    def lower_bound(self, x):
        w = i = 0
        k = self.n0
        while k:
            if i+k <= self.n and w + self.data[i+k] < x:
                w += self.data[i+k]
                i += k
            k >>= 1
        # assert self.get(0, i) <= x < self.get(0, i+1)
        return i+1


q = int(input())
query = []
X = set()

# クエリ先読み
for _ in range(q):
    L = tuple([*map(int, input().split())])
    X.add(L[1])
    if L[0] != 1:
        X.add(L[2])
    query.append(L)

# 座標圧縮
x2i = {x:i for i, x in enumerate(sorted(X), 1)}
i2x = {i:x for i, x in enumerate(sorted(X), 1)}
n = len(X)
bit = BIT(n)

for d in query:
    if d[0] == 1:
        bit.add(x2i[d[1]], 1)
    elif d[0] == 2:
        x, k = d[1], d[2]
        tmp = bit.sum(x2i[x])
        if tmp < k:
            print(-1)
        else:
            print(i2x[bit.lower_bound(tmp - k)])
    else:
        x, k = d[1], d[2]
        total = bit.sum(n)
        l = bit.sum(max(0, x2i[x]-1))
        if total - l < k:
            print(-1)
        else:
            print(i2x[bit.lower_bound(l+k)])
