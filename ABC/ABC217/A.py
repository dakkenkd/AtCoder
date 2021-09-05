s,t = map(str, input().split())

lst = [s,t]

if sorted(lst) == lst:
  print("Yes")
else:
  print("No")