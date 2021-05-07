# pypy3でないと通りませんでした
n=int(input())
a=list(map(int,input().split()))
ans=0
data=0
for i in range(n):
  data=a[i]
  for j in range(i,n):
    data=min(data,a[j])
    ans=max(data*(j-i+1),ans)
print(ans)