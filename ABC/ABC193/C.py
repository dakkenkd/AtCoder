import math
n = int(input())
count = 0
dic = {}
for i in range(2,int(math.sqrt(n))+1):
  if i in dic.keys():
    continue
  x = 2
  c = -1
  while c <= n:
    c = i ** x
    count += 1
    dic[c] = 1
    x += 1
  count -= 1
print(n-count)