from heapq import heapify, heappush, heappop
n, m = map(int, input().split())
G = [[] for _ in range(n)]
in_dic = {}
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    in_dic.setdefault(v,0)
    in_dic[v] += 1

# トポロジカルソート順を保存する配列
order = []
# 入力辺を持たないすべてのノードの集合
hq = list(set([i for i in range(n)]) ^ set(in_dic.keys()))

heapify(hq)

while hq:
    v = heappop(hq)
    order.append(v+1)
    for e in G[v]:
        in_dic[e] -= 1
        if in_dic[e] == 0:
            heappush(hq, e)

dp = [0] * n

for i in order:
    for v in G[i]:
        dp[v] = max(dp[i] + 1, dp[v])

print(dp)
