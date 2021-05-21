n = int(input())
c = 1
ans = 0
while True:
  num = int(str(c) + str(c))
  if num <= n:
    ans += 1
  else:
    break
  c += 1
print(ans)