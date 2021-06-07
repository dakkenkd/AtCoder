n = int(input())
a_lst = [int(i) for i in input().split()]
b_lst = [int(i) for i in input().split()]
c_lst = [int(i) for i in input().split()]

a_dic = {}
b_dic = {}
c_dic = {}

for i,d in enumerate(a_lst):
  if d not in a_dic.keys():
    a_dic[d] = 1
  else:
    a_dic[d] += 1
for i,d in enumerate(b_lst):
  if d not in b_dic.keys():
    b_dic[d] = [i]
  else:
    b_dic[d].append(i)
for i,d in enumerate(c_lst):
  if d-1 not in c_dic.keys():
    c_dic[d-1] = 1
  else:
    c_dic[d-1] += 1
ans = 0
for k in b_dic.keys():
  lst = b_dic[k]
  if k not in a_dic.keys():
    continue
  count = 0
  for d in lst:
    if d in c_dic.keys():
      count += c_dic[d]
  ans += count * a_dic[k]

print(ans)
  