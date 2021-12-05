# https://atcoder.jp/contests/abc216/submissions/25445916

n, k = map(int, input().split())
lst = [*map(int, input().split())]

def ng_ok(p):
    cnt = 0
    for d in lst:
        cnt += max(d-p, 0)
    return cnt, cnt <= k

l, r = -1, 10**20

while r-l > 1:
    mid = (r + l) // 2
    cnt, judge = ng_ok(mid)
    if judge:
        r = mid
    else:
        l = mid

cnt, judge = ng_ok(r)
ans = 0
if r == 0:
    for i in range(n):
        ans += (lst[i]+1) * lst[i] // 2
    print(ans)
else:
    ans += (k - cnt) * max(r, 0) # cnt個 r 以上の数を選ぶので 残り位の(cnt - k)個 を rから選ぶ
    for i in range(n):
        if r < lst[i]:
            ans += (lst[i] + 1) * lst[i] // 2 - (r + 1) * r // 2
    print(ans)
