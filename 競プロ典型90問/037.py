from collections import deque
w, n = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, input().split())))

INF = 10**18
dp = [[-INF] * (w+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    l, r, v = lst[i-1]
    deq = deque() # スライド最大値をとる
    nxt = 0
    print("i =", i)
    for w in range(w+1):
        dp[i][w] = max(dp[i][w], dp[i-1][w])
        lower = w - r
        upper = w - l
        while nxt <= w and nxt <= upper:
            print("upper", deq)
            val = dp[i-1][nxt]
            while len(deq) > 0 and deq[-1][0] <= val:
                deq.pop()
            deq.append((val, nxt))
            nxt += 1
        while len(deq) > 0 and deq[0][1] < lower:
            print("lower", deque)
            deq.popleft()

        if len(deq) == 0: continue
        dp[i][w] = max(dp[i][w], deq[0][0] + v)

if dp[n][w] < 0:
    print(-1)
else:
    print(dp[n][w])
