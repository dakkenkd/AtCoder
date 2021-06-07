n,k = map(int, input().split())

a = n*(n+1)//2
b = k*(k+1)//2

print(a*100*k + b*n)