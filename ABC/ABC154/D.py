n, k = map(int, input().split())
x = lambda x: int(x)*(int(x)-1)//2        
lst = [*map(x, input().split())]

ans = 0

for i in range(k):
    ans += lst[i]
mx = ans
for i in range(n-k):
    ans -= lst[i]
    ans += lst[i+k]
    mx = max(mx, ans)
print(mx)