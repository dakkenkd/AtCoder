n = int(input())
lst = [int(i) for i in input().split()]
dic = {}
count = 0
for i in range(n-1,-1,-1):
  x = lst[i]%200
  shou = lst[i]//200
  if x in dic.keys():
    dic[x].append(shou)
  else:
    dic[x] = [shou]
for d in dic.keys():
  num = len(dic[d])
  if num == 1:
    continue
  else:
    count += num*(num-1)//2
print(count)
    