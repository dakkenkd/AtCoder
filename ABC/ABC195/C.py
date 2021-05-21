n = input()

x = len(n)//3
p = len(n)%3
if p==0:
  q = x-1
else:
  q = x
count = 0
for i in range(1,q+1):
  if i != q:
    count += 999 * 10 ** (3*i) * i
if p==0:
  x = x-1
count += (int(n) - 10 ** (x*3) + 1) * x
print(count)