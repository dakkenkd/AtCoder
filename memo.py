n = int(input())
lst = [*map(int, input().split())]
acc = [lst[0]] * n
for i, d in enumerate(lst[1:], 1):
    acc[i] = acc[i-1] + lst[i]
print(acc)
acc = [0] + acc
dp = [[0] * 3001 for _ in range(n+1)]
memo = [[0] * 3001 for _ in range(n+1)]
dp[0][0] = 1
memo[0][0] = 1
s = acc[-1]
for i in range(1,n+1):
    for j in range(1, 3001):
        dp[i][j] = memo[j][acc[i]%j] # (j-1)分割できる通り数できてかつacc[i]%jあまるものの通り数
    for j in range(2, 3001):
        memo[j][]
