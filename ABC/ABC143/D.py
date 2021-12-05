from bisect import bisect_left, bisect_right
n = int(input())
lst = [*map(int, input().split())]
lst.sort()
ans = 0
for i in range(n-1):
    for j in range(i, n):
        a = lst[i]
        b = lst[j]
        x = bisect_right(lst, a-b)
        y = bisect_right(lst, b-a)
        z = bisect_left(lst, a+b)
        x, y = min(x,y), max(x,y)
        cnt = z - y
        if cnt <= 0: continue
        if y <= a <= z: cnt -= 1
        if y <= b <= z: cnt -= 1
        ans += cnt

print(ans)
