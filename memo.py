n, w = map(int, input().split())
a = [int(i) for i in input().split()]

# DP
dp = [[False] * (w + 1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(w+1):
        # a[i]を選ばない場合
        if dp[i][j] == True:
            dp[i+1][j] = True
        
        # a[i]を選ぶ場合
        if j >= a[i] and dp[i][j-a[i]] == True:
            dp[i+1][j] = True

if dp[n][w] == True:
    print("Yes")
else:
    print("N")