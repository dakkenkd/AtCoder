n = int(input())

lst_a = [int(i) for i in input().split()]
lst_b = [int(i) for i in input().split()]
ans = min(lst_b) - max(lst_a) +1
if ans < 0:
  print(0)
else:
  print(ans)
