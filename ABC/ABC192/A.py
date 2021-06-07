x = int(input())
h = 100
while True:
  if x < h:
    break
  else:
    h += 100
print(h-x)