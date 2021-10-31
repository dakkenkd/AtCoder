n = int(input())
bit = [0] * (n+1)

def add(x, w): # x: 加算したい場所, w: 加算したい値
    while x <= n: 
        bit[x] += w
        x += x & -x # 上のブロックに移動していく

def sum(x):
    ret = 0
    while x > 0:
        ret += bit[x] # 現在のブロックの値を足していく
        x -= x & -x # 左上のブロックに移動していく
    return ret

# 二分探索
NO = 2**(n-1).bit_length()
def lower_bound(x):
    w = i = 0
    k = NO
    while k > 0:
        if i + k <= n and w + bit[i + k] <= x:
            w += bit[i + k]
            i += k
        k >>= 1
    return i + 1