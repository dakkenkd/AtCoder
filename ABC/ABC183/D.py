n,w = map(int, input().split())
lst = [ [int(i) for i in input().split()] for j in range(n)]
dic = {}
for i in range(len(lst)):
  d = lst[i]
  if d[0] not in dic.keys():
    dic[d[0]] = d[2]
  else:
    dic[d[0]] += d[2]
  if d[1] not in dic.keys():
    dic[d[1]] = -d[2]
  else:
    dic[d[1]] -= d[2]

simu = 0
for d in sorted(dic.keys()):
  simu += dic[d]
  if simu > w:
    print("No")
    exit()
print('Yes')