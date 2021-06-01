N,D,H = map(int, input().split())
ans = 0
for i in range(N):
  d, h = map(int, input().split())
  h -= d*(H-h)/(D-d)
  if h > ans:
    ans = h
print(ans)