n,C = map(int, input().split())
dic = {}
for i in range(n):
  a,b,c = map(int, input().split())
  if a not in dic.keys():
    dic[a] = c
  else:
    dic[a] += c
  if b+1 not in dic.keys():
    dic[b+1] = -c
  else:
    dic[b+1] -= c
p_time = 0
ans = 0
count = 0
start = 0
s = list(dic.keys())[0]
subsc = False
for d in sorted(dic.keys()):
  if s != d:
    ans += (d - s) * min(C, count)
  count += dic[d]
  s = d
print(ans)