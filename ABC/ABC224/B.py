h,w = map(int, input().split())
lst = []
for _ in range(h):
  L = list(map(int, input().split()))
  lst.append(L)

for i in range(h-1):
  for ii in range(i+1, h):
    for j in range(w-1):
      for jj in range(j+1, w):
        if lst[i][j] + lst[ii][jj] > lst[ii][j] + lst[i][jj]:
          print("No")
          exit()
print("Yes")