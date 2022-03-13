from collections import deque
w, n = map(int, input().split())

dp = [-1] * (w+1)
dp[0] = 0

for _ in range(n):
    l, r, v = map(int, input().split())
    # iv ... dpの区間[i-r, i-l]の最大値を得るためのスライド最大値
    # ivとは(index, value)を意味してる
    iv = deque()

    # スライド最大値の初期化
    for i in range(w-l, w-r, -1):
        while iv and iv[-1][-1] <= dp[i]:
            iv.pop()
        iv.append((i, dp[i]))

    # DP本体
    for i in range(w, l-1, -1):
        # スライド最大値に対する処理
        if iv and iv[0][0] == i-l+1:
            iv.popleft()
        if i-r >= 0:
            while iv and iv[-1][-1] <= dp[i-r]:
                iv.pop()
            iv.append((i-r, dp[i-r]))
        if iv[0][1] == -1: continue

        # DP更新
        dp[i] = max(dp[i], iv[0][1]+v)

print(dp[1])
