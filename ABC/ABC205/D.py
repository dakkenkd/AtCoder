import bisect

n,q = map(int, input().split())
lst = [int(i) for i in input().split()]

for i in range(q):
    k = int(input())
    idx = bisect.bisect_right(lst, k)
    pre = 0
    while True:
        idx = bisect.bisect_right(lst, k)
        if idx + pre == idx:
            print(k)
            break
        pre = idx
        k += idx