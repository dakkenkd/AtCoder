n,k = map(int, input().split())
s = str(n)
for i in range(k):
  if n%200 == 0:
    n = n//200
    s = str(n)
  else:
    s = s+'200'
    n = int(s)
print(n)