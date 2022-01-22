# s=x+y, t=x-yとして、(x,y)を(s,t)に変換する
# すると、xy座標におけるマンハッタン距離はst座標におけるチェビシェフ距離になる
# 事前にs,tそれぞれの最大値、最小値を求めておく
# これにより、クエリの点からの上下左右への最大距離がわかるので、そのうち最大値が答え

inf = 10**10

n, q = map(int, input().split())

p = []
min_s = min_t = inf
max_s = max_t = -inf
for _ in range(n):
    x, y = map(int, input().split())
    s = x+y
    t = x-y
    p.append((s, t))
    min_s = min(min_s, s)
    min_t = min(min_t, t)
    max_s = max(max_s, s)
    max_t = max(max_t, t)

for _ in range(q):
    i = int(input()) - 1
    s, t = p[i]
    ans = max(s-min_s, t-min_t, max_s-s, max_t-t)
    print(ans)
