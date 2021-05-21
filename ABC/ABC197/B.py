h,w,x,y = map(int, input().split())
lst = []
for i in range(h):
  s = list(input())
  lst.append(s)

count = 0
c = 0
search = []
for i in range(h):
  if lst[i][y-1] == '.':
    search.append(i)
    if i == h-1:
      if x-1 in search:
        count += len(search)
  else:
    if x-1 in search:
      count += len(search)
      search = []
    else:
      search = []
search = []
for i in range(w):
  if lst[x-1][i] == '.':
    search.append(i)
    if i == w-1:
      if y-1 in search:
        count += len(search)
  else:
    if y-1 in search:
      count += len(search)
      search = []
    else:
      search = []

print(count-1)