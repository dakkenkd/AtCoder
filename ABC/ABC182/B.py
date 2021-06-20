n = int(input())
lst = [ int(i) for i in input().split()]
mx = max(lst)
ans = 0
gcd = 0
for i in range(2,mx+1):
  k_max = 0
  for d in lst:
    if d % i == 0:
      k_max += 1
  if k_max > gcd:
    ans = i
    gcd = k_max
print(ans)