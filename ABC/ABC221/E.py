n = int(input())
lst = [int(i) for i in input().split()]
lst = list(reversed(lst))
bit = [0] * (n+1) # これまでの数字がどんなふうになっているのかをメモるためのBIT
ruiseki = [0] * n
mod = 998244353
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

T = 0
pre = 0

for i in range(n):
    T += i - sum(lst[i])
    add(lst[i], 1)
    ruiseki[i] = T - pre
    pre = T

ans = 0

for i in range(1, n):
    n1 = ruiseki[i]
    n2 = (i+1) - ruiseki[i]
    if n1 >= 2:
        ans += pow(2, ruiseki[i]) - ruiseki[i] - 1
        ans %= mod
    if n2 >= 2:
        ans += pow(2, (i+1) - ruiseki[i]) - ((i+1) - ruiseki[i]) - 1
        ans %= mod

    if ans > mod:
        ans %= mod

print(ruiseki)
print(ans)