n, x = map(int, input().split())
s = list(input())

for d in s:
  if d == "o":
    x += 1
  else:
    if x > 0:
      x -= 1
print(x)