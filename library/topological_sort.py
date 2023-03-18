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

def topological_sort(N, M, in_dic):
    # トポロジカルソート順を保存する配列
    order = []
    # 入力辺を持たないすべてのノードの集合
    hq = list(set([i for i in range(n)]) ^ set(in_dic.keys()))

    heapify(hq)

    # トポロジカル順が一意かどうか判定
    flag1 = True
    if len(hq) >= 2:
        flag1 = False

    while hq:
        # 入次数が 0 のノードが複数あればトポロジカル順が一意でない
        if len(hq) >= 2:
            flag1 = False
        v = heappop(hq)
        order.append(v+1)
        for e in G[v]:
            in_dic[e] -= 1
            if in_dic[e] == 0:
                heappush(hq, e)

    # トポロジカルソートできなければ（有向閉路があればorderは空）
    if len( set(in_dic.values()) ^ set([0]) ) == 0:
        return order, flag1
    else:
        return [], False
