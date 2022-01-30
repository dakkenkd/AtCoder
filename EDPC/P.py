from collections import deque
import itertools
from optparse import make_option
import sys
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    x, y = map(lambda t: int(t)-1, input().split())
    edges[x].append(y)
    edges[y].append(x)

white = [-1] * n
white[0] = 1
black = [-1] * n
black[0] = 1
seen = [-1] * n
seen[0] = 1
mod = 10**9+7

def dfs(v, pre):
    cnt_b = 1
    cnt_w = 1
    for vv in edges[v]:
        if vv == pre: continue
        now_b, now_w = dfs(vv, v)
        cnt_b *= now_w
        cnt_w *= now_w + now_b
        cnt_b %= mod
        cnt_w %= mod
    if cnt_b == 0 and cnt_w == 0:
        return 1, 1
    return cnt_b, cnt_w
print(sum(dfs(0, -1))%mod)