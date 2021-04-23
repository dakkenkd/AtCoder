n = map(int, input().split())
ans = 1
for i in range(n):
    ans *= i+1
print(ans)