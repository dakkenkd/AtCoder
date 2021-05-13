h, w = map(int, input().split())
lst = [ [int(i) for i in input().split()] for j in range(h) ]

mn = 1000000
for d in lst:
  m = min(d)
  if m < mn:
    mn = m

count = 0
for d in lst:
  for j in range(len(d)):
    if d[j] != mn:
      count += d[j] - mn
print(count)