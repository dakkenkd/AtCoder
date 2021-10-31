import heapq
n, m = map(int, input().split())
in_cnt = [0]*(n+1) # 入ノードを数える配列
outs = {i:set() for i in range(1, n+1)} # 出ノードの向かう先
for _ in range(m):
    a, b = map(int, input().split())
    if b not in outs[a]: # もしかぶっていたら加えない
        in_cnt[b] += 1 # 入ってくる辺の数を＋１
        outs[a].add(b) # aから出る辺を保存

res = [-1] * n # 答えを保存する配列
k = 0 # 答えを保存するためのindex
hq = [i for i in range(1,n+1) if in_cnt[i] == 0] # 入ノードが0のエッジをheapに追加
heapq.heapify(hq)
while hq:
    v = heapq.heappop(hq)
    res[k] = v
    k += 1
    for v2 in outs[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            heapq.heappush(hq, v2)
print(*res) if res[n-1] > 1 else print(-1)