a,b,c = map(int, input().split())

lst = [a,b,c]
lst = sorted(lst)

if lst[0] == lst[1]:
  print(lst[2])
elif lst[1] == lst[2]:
  print(lst[0])
else:
  print(0)