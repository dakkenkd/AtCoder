s = input()
t = input()

ls = len(s)
lt = len(t)

# dp[i][j] -> sのi文字目までとtのj文字目までのLCS
dp = [[-1] * (max(ls, lt) + 10) for _ in range(max(ls, lt) + 10)]

# 初期化
for i in range(ls+1):
    dp[i][0] = 0
for j in range(lt+1):
    dp[0][j] = 0
s_lst = []
t_lst = []
mx = 0
for i in range(ls+1):
    for j in range(lt+1):
        if i==0 or j==0:
            dp[i][j] == 0
            continue
        dp1 = dp[i-1][j]
        dp2 = dp[i][j-1]
        dp3 =  dp[i-1][j-1] + 1 if s[i-1] == t[j-1] else -1
        if (dp3 > dp1 or dp3 > dp2):
            dp[i][j] = dp3
        else:
            dp[i][j] = max(dp1, dp2)
n = ls
m = lt
ans = ""
while n > 0 and m > 0:
    if dp[n][m] == dp[n-1][m]:
        n -= 1
    elif dp[n][m] == dp[n][m-1]:
        m -= 1
    else:
        ans += s[n]
print(ans[::-1])
