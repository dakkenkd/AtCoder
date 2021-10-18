n = int(input())
lst = list(map(int, input().split()))
ans = [0 for i in range(n)]

for i,d in enumerate(lst):
  ans[d-1] = i+1
print(*ans)
