n = input()
nlst = list(n)
alst = []
for i in range(len(n)):
  alst.append(int(nlst[i])%3)
sm = sum(alst)%3
if sm%3 == 0:
  print(0)
  exit()
c1 = alst.count(1)
c2 = alst.count(2)
if sm == 1:
  if c1 >= 1:
    if len(n) == 1:
      print(-1)
      exit()
    else:
      print(1)
      exit()
  elif c2 >= 2:
    if len(n) <= 2:
      print(-1)
      exit()
    else:
      print(2)
      exit()
  print(-1)
  exit()
if sm == 2:
  if c2 >=1:
    if len(n) == 1:
      print(-1)
      exit()
    else:
      print(1)
      exit()
  elif c1 >= 2:
    if len(n) <= 2:
      print(-1)
      exit()
    else:
      print(2)
      exit()
