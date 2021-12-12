import math
n, k = map(int, input().split())
lst = [*map(int, input().split())]

def ng_ok(limit):
    cnt = 0
    for d in lst:
        cnt += math.ceil(d/limit)-1

    return cnt <= k

l, r = 0, 10**10

while r-l > 1:
    mid = (r+l) // 2
    if ng_ok(mid):
        r = mid
    else:
        l = mid

print(r)
