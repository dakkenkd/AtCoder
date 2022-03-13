from operator import mul
from functools import reduce

def cmb(n,r):
    if n < r: return 0
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

a = cmb(n, r)

# modをとりながらのnCr
def ncr(n, r, mod):
    ret = 1
    for i in range(1, r+1):
        ret = (ret * (n-i+1) * pow(i, mod-2, mod)) % mod
    return ret
