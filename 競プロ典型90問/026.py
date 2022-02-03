n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
ans = [0]*n
seen = [False]*n
def dfs(v, flag):
    seen[v] = True
    ans[v] = flag
    for vv in g[v]:
        if seen[vv]: continue
        dfs(vv, flag ^ 1)

dfs(0, 0)
if len([i+1 for i in range(n) if ans[i]==1]) >= len([i+1 for i in range(n) if ans[i]==0]):
    flag = 1
else:
    flag = 0
if flag == 1:
    print(*[i+1 for i in range(n) if ans[i]==1][:n//2])
else:
    print(*[i+1 for i in range(n) if ans[i]==0][:n//2])
