mod = 998244353

fact = [1] * 220000
invfact = [1] * 220000

for i in range(1, 220000):
    fact[i] = fact[i-1] * i % mod

invfact[-1] = pow(fact[-1], mod-2, mod)
for i in range(220000-1, 0, -1):
    invfact[i-1] = invfact[i] * i % mod

def nCk(n, k):
    if k < 0 or n-k < 0: return 0
    return fact[n] * invfact[n-k] * invfact[k]
