a, b, x = map(int, input().split())

def ng_ok(p):
    yen = b * len(str(p))
    yen += a * p
    return yen <= x

l, r = 0, 10**9+1

while r - l > 1:
    mid = (r + l) // 2
    if ng_ok(mid):
        l = mid
    else:
        r = mid

print(r)
