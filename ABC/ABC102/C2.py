from bisect import bisect_left, bisect_right
n = int(input())
lst = [int(x)-(i+1) for i,x in enumerate(input().split())]
lst.sort()
BIT = [0] * (n+1)

def add(x, w):
    while x <= n:
        BIT[x] += w
        x += x & -x

def sum(x):
    ret = 0
    while x > 0:
        ret += BIT[x]
        x -= x & -x
    return ret

# BITの構築
for i in range(n):
    add(i+1, lst[i])

ans = float("inf")
for d in set(lst):
    cnt = 0
    x = bisect_left(lst, d)
    # d以上の数
    cnt += (sum(n) - sum(x)) - d * (n - x)
    # dより小さい数
    cnt += d * x - sum(x)
    ans = min(ans, cnt)
print(ans)
