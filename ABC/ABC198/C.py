r,x,y = map(int, input().split())

uc = (x**2 + y**2)**0.5

if uc % r == 0:
  print(int(uc//r))
else:
  if r > uc:
    print(2)
  else:
    print(int(uc//r + 1))