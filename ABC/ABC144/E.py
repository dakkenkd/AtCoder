import math
n, k = map(int, input().split())
lst = [*map(int, input().split())]
food = [*map(int, input().split())]
lst.sort()
food.sort(reverse=True)
# 最大値をlimitに抑えられるかどうか
def ng_ok(limit):
    cnt = 0
    for i in range(n):
        cnt += max(0, lst[i]-limit//food[i])
    if cnt <= k:
        return True
    else:
        return False

l, r = -1, 10**20
while r-l > 1:
    mid = (r+l) // 2
    if ng_ok(mid):
        r = mid
    else:
        l = mid

print(r)
