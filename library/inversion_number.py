n = int(input())
lst = [int(i) for i in input().split()]
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
for i in range(n):
    ans += i - sum(lst[i])
    add(lst[i], 1)

print(ans)