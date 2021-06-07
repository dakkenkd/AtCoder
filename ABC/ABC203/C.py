n,k = map(int, input().split())

dic = {}

for i in range(n):
  a,b = map(int, input().split())
  if a not in dic.keys():
    dic[a] = b
  else:
    dic[a] += b
pre = 0
ans = 0
for key in sorted(dic.keys()):
  if k >= key:
    k += dic[key]
  else:
    break
print(k)