n = int(input())
lst = [int(i) for i in input().split()]
L = []
bit = [0] * (n + 1)
mod = 998244353

# BIT
def bit_add(x, w):
    while x <= n:
        bit[x] += w
        x += x & -x

def bit_sum(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret
def query(i,j):
    return 
# 座標圧縮
dic = {k:i+1 for i,k in enumerate(sorted(set(lst)))}
L = [dic[i] for i in lst]

ans = 0

for i, b in enumerate(L):
    if i:
        res = bit_sum(b)
        ans += bit_sum(b) * pow(2, i-1, mod)
        ans %= mod
    bit_add(b, pow(2, mod-i-1, mod))

print(ans)