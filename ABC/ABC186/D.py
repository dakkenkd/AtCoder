n = int(input())
lst = [int(i) for i in input().split()]
lst = sorted(lst)
r = sum(lst)
r_lst = []
for i in range(len(lst)-1):
  r -= lst[i]
  r_lst.append(r)

ans = 0
for i in range(len(lst)-1):
  ans += r_lst[i] - (n-(i+1))*lst[i]
print(ans)