from bisect import bisect_left, bisect_right
n = int(input())
lst = [*map(int, input().split())]
lst.sort()

for i in range(n-1):
    for j in range(i, n):
        a = lst[i]
        b = lst[j]
        left = bisect_right(lst, b-a)
        right = bisect_left(lst, a+b)
        print(a,b, left, right)
