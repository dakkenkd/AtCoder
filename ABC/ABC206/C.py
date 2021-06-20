import collections
n = int(input())
lst = [int(i) for i in input().split()]
L = collections.Counter(lst)
x = n
ans = 0

for k in sorted(L.keys()):
  x -= L[k]
  ans += x*L[k]
print(ans)