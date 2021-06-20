n,m = map(int, input().split())
if m == 0:
  print(1)
  exit()
lst = [int(i) for i in input().split()]
lst = sorted(lst)
sa_lst = []
mn = n
pre = 0
for i in range(m):
  x = lst[i] - pre - 1
  if x >= 1:
    mn = min(mn, lst[i]-pre-1)
    sa_lst.append(x)
  pre = lst[i]

if n - pre > 1:
  mn = min(mn, n-pre)
  sa_lst.append(n - pre)

count = 0
for d in sa_lst:
  if d%mn == 0:
    count += d//mn
  else:
    count += d//mn + 1
    
print(count)