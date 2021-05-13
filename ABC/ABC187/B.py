n = int(input())
lst = []
for i in range(n):
  a,b = map(int, input().split())
  lst.append([a,b])

count = 0  

for i in range(len(lst)-1):
  for j in range(i+1, len(lst)):
    x1 = lst[i][0]
    x2 = lst[j][0]
    y1 = lst[i][1]
    y2 = lst[j][1]
    x = x1 - x2
    y = y1 - y2
    if x == 0:
      ans = y
    else:
      ans = abs(y/x)
    if ans <= 1:
      count += 1
      
print(count)