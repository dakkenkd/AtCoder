h,w = map(int, input().split())
row_dic = {}
col_dic = {}
lst = []
for i in range(h):
  lst_ = [int(i) for i in input().split()]
  lst.append(lst_)
  row_dic[i] = sum(lst_)
  for j,d in enumerate(lst_):
    if j not in col_dic.keys():
      col_dic[j] = d
    else:
      col_dic[j] += d

for r in range(h):
  ans = []
  for c in range(w):
    ans.append(str(row_dic[r] + col_dic[c] - lst[r][c]))
  print(" ".join(ans))