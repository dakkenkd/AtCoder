n = int(input())
lst = [int(i) for i in input().split()]

ans = 0

for d  in lst:
  if d > 10:
    ans += d-10
print(ans)