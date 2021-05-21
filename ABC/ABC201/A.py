a1,a2,a3 = map(int, input().split())
lst = [a1,a2,a3]
lst = sorted(lst)

if lst[2] - lst[1] == lst[1] - lst[0]:
  print("Yes")
else:
  print("No")