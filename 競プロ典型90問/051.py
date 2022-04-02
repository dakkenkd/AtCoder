from bisect import bisect_left, bisect_right
n, k, p = map(int, input().split())
lst = [*map(int, input().split())]

left = lst[:n//2]
right = lst[n//2:]

def half_combination(items):
    L = len(items)
    ret = [[] for _ in range(k+1)]
    ret[0].append(0)
    for i in range(2**L):
        cnt = 0
        num = 0
        for j in range(L):
            if i >> j & 1:
                cnt += items[j]
                num += 1
        if cnt <= p:
            ret[num].append(cnt)
    for i in range(len(ret)):
        ret[i] = sorted(ret[i])
    return ret

left_cmb = half_combination(left)
right_cmb = half_combination(right)

ans = 0

for i in range(len(right_cmb)):
    A = right_cmb[i]
    num = k - i
    for j in range(len(A)):
        money = p - A[i]
        x = bisect_right(left_cmb, money)
        ans += x

print(ans)
