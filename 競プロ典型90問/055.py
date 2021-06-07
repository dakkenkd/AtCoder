n,p,q = map(int, input().split())
lst = [int(i)%p for i in input().split()]
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for x in range(k+1,n):
        for y in range(x+1,n):
          if lst[i]%p*lst[j]%p*lst[k]%p*lst[x]%p*lst[y]%p == q:
            ans += 1
print(ans)
