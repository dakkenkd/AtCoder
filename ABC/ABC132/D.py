from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n, k = map(int, input().split())
r = n-k
mod = 10**9+7

for i in range(1,k+1):
    ans = 1
    try:
        ans = cmb(k-i + i-1, i-1) % mod
    except:
        print(k-i + i-1, i-1) # 青の配置を決定
    red = r - (i-1)
    try:
        ans *= cmb(red + i, i) % mod
    except:
        print(red + i, i)
    print(ans % mod)
