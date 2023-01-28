mod = 998244353
invmod = pow(2, mod-2, mod)

"""
a : 初項
n : 項数
d : 公差
"""
def a_sum(a, n, d):
    return n % mod * (2*a % mod + (n-1)*d % mod) * invmod % mod



"""
a1 : 初項
an : 末項
"""

def arithmetic_sum(a1, an, n):
    return (a1+an) * n * pow(2, mod-2, mod)
