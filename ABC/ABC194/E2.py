n, m = map(int, input().split())
lst = [*map(int, input().split())]
def ng_ok(limit):
    cnt = [0] * (10**8)
    s = set()
    j = set()
    for i in range(m):
        a = lst[i]
        if cnt[a] == 0:
            s.add(a)
            if a < limit:
                j.add(a)
        cnt[a] += 1
    print(j)

    if len(j) == limit:
        return True

    for i in range(m, n):
        l = lst[i-m]
        r = lst[i]
        print(j)
        if cnt[l] == 1:
            s.remove(l)
            if l in j:
                j.remove(l)
        if cnt[r] == 0:
            s.add(r)
            if r < limit:
                j.add(r)
        cnt[l] -= 1
        cnt[r] += 1
        if len(j) == limit:
            return True

    return False

print(ng_ok(1))
