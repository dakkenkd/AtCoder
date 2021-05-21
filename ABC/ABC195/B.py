a,b,w = map(int, input().split())
w = w*1000
mx = w//a
if w%b == 0:
  mn = w//b
else:
  mn = w//b + 1

lst = []
for i in range(mn,mx+1):
  if a <= w//i <= b:
    lst.append(i)
if lst==[]:
  print('UNSATISFIABLE')
  exit()
print(min(lst), max(lst))