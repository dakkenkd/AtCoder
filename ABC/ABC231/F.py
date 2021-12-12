from bisect import bisect_left, bisect_right
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

from bisect import bisect_left, bisect_right
n = int(input())
alst = [*map(int, input().split())]
blst = [*map(int, input().split())]
L = []
for i in range(n):
    L.append([alst[i], blst[i]])
L.sort(key=lambda x: (x[0],-x[1]))

# 座標圧縮
A = [d[0] for d in L]
lst = [d[1] for d in L]
dic = {}
for i, d in enumerate(sorted(set(lst))):
    dic[d] = i+1
lst = [dic[d] for d in lst]
bit = [0] * (n+1) # これまでの数字がどんなふうになっているのかをメモるためのBIT

def add(x, w):
    while x <= n:
        bit[x] += w
        x += x & -x

def sum(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret

ans = 0

# 転倒数
cnt = 0
temp_a = -1
temp_b = -1
for i in range(n):
    add(lst[i], 1)
    ans += i - sum(lst[i]-1)
    if temp_a == A[i] and temp_b == lst[i]:
        cnt += 1
        ans += cnt
    else:
        temp_a = A[i]
        temp_b = lst[i]
        cnt = 0

print(n+ans)
