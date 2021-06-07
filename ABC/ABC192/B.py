lst = list(input())
flag = True
for i in range(len(lst)):
  if i%2 == 0:
    if lst[i].lower() != lst[i]:
      flag = False
  else:
    if lst[i].upper() != lst[i]:
      flag = False
if flag == True:
  print('Yes')
else:
  print('No')