n = int(input())
lst = [int(i) for i in input().split()]
r=p=q=x=0
for i in range(n):
  p += lst[i]
  q = max(q, p)
  r = max(r, x+q)
  x += p
print(r)