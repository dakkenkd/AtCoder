n, k = map(int, input().split())
lst = [*map(int, input().split())]
food = [*map(int, input().split())]
mx = max(lst)
def is_ok(x):
    if x >= mx: return True
    cnt = 0
    for d in lst:
        cnt += max(d-x, 0)
    return cnt <= k

l, r = 0, 10**20

while r - l > 1:
    mid = (r + l) // 2
    if is_ok(mid):
        r = mid
    else:
        l = mid

food = sorted(food, reverse=True)
cnt = 0
for i in range(n):
    if lst[i] > r:
        cnt += lst[i] - r
        lst[i] = r
lst = sorted(lst, reverse=True)
for i in range(k - cnt):
    lst[i] -= 1

lst = sorted(lst)
mx = -1
for i in range(n):
    mx = max(mx, lst[i] * food[i])

print(mx)
