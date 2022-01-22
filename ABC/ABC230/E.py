n = int(input())
lst = []
ans = 0
i = 1
while i ** 2 <= n:
    x, y = n//i,  n//(i+1)
    ans += (x-y) * i + x
    i += 1
print(ans)
