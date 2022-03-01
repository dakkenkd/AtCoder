n = 5
lst = [8,6,4,3,2]

"""
l 以上 r以下の値を調べたいときは配列をソートしてからBITを作り、
l, r = bisect_left(lst, ), bisect_right(lst, 10) - 1
みたいな感じで区間を絞ってください
"""

from collections import Counter
class FenwickTree:

    def __init__(self, n, lst):
        self.arr = lst
        self.x2i = {d:i+1 for i, d in enumerate(sorted(set(lst)))}
        self.i2x = {i+1:d for i, d in enumerate(sorted(set(lst)))}
        self.comp_arr = [self.x2i[d] for d in lst]
        self.bit = [0] * (len(lst) + 1)
        self.n = n

    def bit_add(self, x, w): # x: 加算したい場所, w: 加算したい値
        x += 1
        while x <= self.n:
            self.bit[x] += w
            x += x & -x

    def bit_sum(self, l, r): # (l, r) の合計
        r += 1
        r_sum = 0
        l_sum = 0
        while r > 0:
            r_sum += self.bit[r] # 現在のブロックの値を足していく
            r -= r & -r # 左上のブロックに移動していく
        while l > 0:
            l_sum += self.bit[l]
            l -= l & -l
        return r_sum - l_sum



BIT = FenwickTree(n, lst)


# 二分探索
# NO = 2**(n-1).bit_length()
# def lower_bound(x):
#     w = i = 0
#     k = NO
#     while k > 0:
#         if i + k <= n and w + bit[i + k] <= x:
#             w += bit[i + k]
#             i += k
#         k >>= 1
#     return i + 1
