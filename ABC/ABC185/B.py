n,m,t = map(int, input().split())
lst = [[int(i) for i in input().split()] for j in range(m)]
nx = n-lst[0][0]
if nx == 0:
  print('No')
  exit()
time = lst[0][0]
for d in lst:
  nx = max(nx - (d[0] - time), 0)
  if nx == 0:
    print("No")
    exit()
  nx = min(nx + (d[1] - d[0]), n)
  time = d[1]
nx = max(nx - (t-time), 0)
if nx == 0:
  print("No")
  exit()
print('Yes')