s = input()

sure = []
pro = []
nan = []

for i in range(len(s)):
  if s[i] == "o":
    sure.append(str(i))
  elif s[i] == "?":
    pro.append(str(i))
  else:
    nan.append(str(i))
slen = len(sure)
plen = 4-slen
ans = set()
lst = sure+pro
ko = "".join(lst)
for i in range(len(lst)):
  for j in range(len(lst)):
    for k in range(len(lst)):
      for p in range(len(lst)):
        flag = True
        x = ko[i] + ko[j] + ko[k] + ko[p]
        for d in sure:
          if d not in x:
            flag = False
            break
        if flag:
          if int(x) not in ans:
            ans.add(int(x))
print(len(ans))

# 別解

import itertools as it
s = input()
sure = [str(i) for i,d in enumerate(s) if d=="o"]
pro = [str(i) for i,d in enumerate(s) if d=="?"]
print(len({ "".join(list(d)) for d in it.product(sure+pro,repeat=4) if set(d)&set(sure) == set(sure) }))