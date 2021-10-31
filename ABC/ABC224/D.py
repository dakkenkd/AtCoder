m = int(input())

# 1-indexedの隣接行列
edge = [[False] * 10 for _ in range(10)]

for _ in range(m):
    u, v = map(int, input().split())
    edge[u][v] = True
    edge[v][u] = True

p = input().split()

# 存在しない番号のコマを"空きスペース"として追加する
for i in range(1,10):
    if str(i) not in p:
        p.append(str(i))
        break

# 初期化
p = int("".join(p))
dist = {p: 0}

vec = [p]

while len(vec) != 0:
    new_vec = []
    for p in vec:
        now = list(str(p)) # 現在の状態を配列化
        nine = int(now[8]) # 空き状態の場所
        for i in range(8):
            pos = int(now[i]) # 場所 i にあるコマ
            if edge[pos][nine]: # もし空き場所に移動できるなら
                now[i], now[8] = now[8], now[i] # 空き場所に移動させる
                nxt = int("".join(now)) # 状態を数値化
                if nxt not in dist: # もしその状態の距離が保存されていなかったら
                    dist[nxt] = dist[p] + 1 # distに保存する
                    new_vec.append(nxt) # 次の状態を調べるためにnew_vecに追加
                now[i], now[8] = now[8], now[i] # forが終わっていないので元に戻す
    vec = new_vec # 調べる状態を更新
    # もし、全ての状態遷移を調べることができたらDFSが停止する

goal = 123456789

if goal in dist: # もしgoalの状態への最短距離があったら
    print(dist[goal]) # 出力
else: # ないならその状態に到達できないグラフが与えられているので -1 を出力
    print(-1)
