fac = [0] * (n+1)
finv = [0] * (n+1)
inv = [0] * (n+1)

fac[0] = fac[1] = 1
inv[1] = 1
finv[0] = finv[1] = 1
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % mod
    inv[i] = mod - mod // i * inv[mod%i] % mod
    finv[i] = finv[i-1] * inv[i] % mod
def binom(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    else:
        return fac[n] * finv[r] % mod * finv[n-r] % mod
