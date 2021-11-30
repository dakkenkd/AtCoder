from collections import deque
import heapq
from bisect import bisect_left
n, m = map(int, input().split())
lst = [*map(int, input().split())]
dic = {}
for i in range(m):
    if lst[i] not in dic:
        dic[lst[i]] = 1
    else:
        dic[lst[i]] += 1

q = deque()
for i in range(1,max(dic.keys())+2):
    if i not in dic:
        q.append(i)

for i in range(m):
    mn = q[0]
    if lst[i] < q[0]:
        q[0].appendleft(lst[i])
        dic[lst[i]] += 1
    if lst[i+m] in dic:
        dic[lst[i+m]] += 1
    else:
        x = bisect_left(q, lst[i+m])
        lst[x] = float("inf")
