R, B = map(int, input().split())
x, y = map(int, input().split())

def ng_ok(k):
    X = R - k
    Y = B - k
    return X//(x-1) + Y//(y-1) >= k and X >= 0 and Y >= 0
l, r = -1, 10**18+1
while r-l > 1:
    mid = (r - l) // 2
    if ng_ok(mid):
        l = mid
    else:
        r = mid

print(l)
