n,k = map(int, input().split())
lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]

ans = 0

for i in range(n):
  ans += abs(lst1[i] - lst2[i])
if ans > k:
  print("No")
elif ans%2 != k%2:
  print("No")
else:
  print("Yes")