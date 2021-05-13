n = int(input())

a_lst = []
b_lst = []
lst = []
for i in range(n):
  a,b = map(int, input().split())
  a_lst.append(a)
  b_lst.append(b)
  lst.append(2*a + b)

lst = sorted(lst,reverse=True)
ans = 0
count = -sum(a_lst)
for i in range(n):
  if count > 0:
    count += lst[i]
    ans += 1
  else:
    break
print(ans)