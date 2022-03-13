
# Binary Indexed Tree (Fenwick Tree)
# @kuruton456
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
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        while k:
            print("k =", k)
            if i+k <= self.n and w + self.data[i+k] < x:
                w += self.data[i+k]
                i += k
            k >>= 1
        # assert self.get(0, i) <= x < self.get(0, i+1)
        return i+1, w

n = 5

bit = BIT(n)
for i in range(5):
    bit.add(i+1, 1)
print(bit.data)
print(bit.lower_bound(2))
