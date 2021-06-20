n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
count = 0
for i in range(n):
  count += a_lst[i] * b_lst[i]
if count == 0:
  print('Yes')
else:
  print('No')