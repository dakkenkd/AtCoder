import math
x, y, r = map(float, input().split())
start = math.ceil(x-r)
end = math.floor(x+r)
ans = 0
print(start, end)
for i in range(start, end+1):
    p = (r**2 - (x-y)**2) ** 0.5
    up = math.floor(y+p)
    down = math.ceil(y-p)
    ans += up - down + 1

print(ans)
