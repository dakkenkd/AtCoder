n, m = map(int, input().split())
lst = [*map(int, input().split())]

def ng_ok(limit):
    cnt = [0] * (10**8)
    s = set()
    for i in range(m):
        a = lst[i]
        if cnt[a] == 0:
            s.add(a)
        cnt[a] += 1

    if len(s) <= limit:
        return True

    for i in range(m, n):
        l = lst[i-m]
        r = lst[i]
        if cnt[l] == 1:
            s.remove(l)
        if cnt[r] == 0:
            s.add(r)
        cnt[l] -= 1
        cnt[r] += 1
        if len(s) <= limit:
            return True

    return False

l, r = 0, 10**20
ans = 10**10

while r-l > 1:
    mid = (l+r) // 2
    if ng_ok(mid):
        ans = min(ans, mid)
        r = mid
    else:
        l = mid

print(r)
