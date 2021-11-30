n, k, m = map(int, input().split())
mod = 998244353
if m % mod == 0:
    print(0)
    exit()
r = pow(k, n, mod - 1)
ans = pow(m, r, mod)

print(ans)
