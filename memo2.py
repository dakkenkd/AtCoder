n = int(input())
lst = [*map(int, input().split())]
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
# 制約からindexを全探索するのは無理。

# いろいろ式をいじってみる
# |idx_a - idx_b| = A + B
# -A - (idx_a - ?) = ?
# -A + (idx_a - ?) = ?

# この二つの式を満たす組み合わせを探せばOK
# -A - idx_a (3)  = B - idx_b (1)
# -A + idx_a (4) = B + idx_b (2)

# A1 = 2, idx = 1
# A4 = 1, idx = 4
dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}
for i in range(n):
    idx = i+1
    if lst[i] - idx not in dic1:
        dic1[lst[i] - idx] = 1
    else:
        dic1[lst[i] - idx] += 1
    if lst[i] + idx not in dic2:
        dic2[lst[i] + idx] = 1
    else:
        dic2[lst[i] + idx] += 1
    if -(lst[i] + idx) not in dic3:
        dic3[-(lst[i] + idx)] = 1
    else:
        dic3[-(lst[i] + idx)] += 1
    if -lst[i] + idx not in dic4:
        dic4[-lst[i] + idx] = 1
    else:
        dic4[-lst[i] + idx] += 1

ans = 0
for i in range(n):
    idx = i+1
    A = lst[i]
    if (-A-idx) in dic1 and dic1[-A-idx] >= 2:
        ans += cmb(dic1[-A-idx]+1, 2)
    if (-A+idx) in dic2 and dic2[-A+idx] >= 2:
        ans += cmb(dic2[-A+idx]+1, 2)
print(ans)
