n = int(input())
lst = []
for i in range(n):
  lst.append(input())
lst = list(set(lst))
dic = {}

alst = []
for i in range(len(lst)):
  alst.append(lst[i].lstrip("!"))

for i in range(len(alst)):
  if alst[i] not in dic.keys():
    dic[alst[i]] = 1
  else:
    print(alst[i])
    exit()
print("satisfiable")