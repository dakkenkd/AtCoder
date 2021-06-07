import itertools

n,m = map(int, input().split())
ab_list = []
cd_list = []
for i in range(m):
  a,b = map(int,input().split())
  ab_list.append((a,b))

k = int(input())
for i in range(k):
  c,d = map(int, input().split())
  cd_list.append((c,d))
ans = 0
for d in itertools.product(*cd_list):
  count = 0
  d = set(d)
  for a,b in ab_list:
    if a in d and b in d:
      count += 1
  if ans < count:
    ans = count
print(ans)
