n = int(input())
lst = [int(i) for i in input().split()]
a = [int(i) for i in range(1,n+1)]
if sorted(lst) == a:
  print("Yes")
else:
  print("No")