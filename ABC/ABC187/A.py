a, b = map(str, input().split())
alst = list(a)
blst = list(b)

ca = 0
cb = 0

for i in range(3):
  ca += int(alst[i])
  cb += int(blst[i])

if ca >= cb:
  print(ca)
else:
  print(cb)