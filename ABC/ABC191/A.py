v, t, s, d = map(int, input().split())

x = v*t
y = v*s

if x <= d <= y:
  print('No')
else:
  print('Yes')