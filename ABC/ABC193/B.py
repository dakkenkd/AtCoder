n = int(input())
mn = 10**10
flag = False
for i in range(n):
  a,p,x = map(int, input().split())
  if x - a > 0:
    if mn > p:
      mn = p
      flag = True

if flag == True:
  print(mn)
else:
  print(-1)