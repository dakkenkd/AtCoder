n, k = map(int, input().split())

if k == 0:
  print(n)
  exit()

def func_down(x):
  lst = list(str(x))
  lst = sorted(lst, reverse=True)
  return int(''.join(lst))

def func_up(x):
  lst = list(str(x))
  lst = sorted(lst)
  return int(''.join(lst))
x = n
for i in range(k):
  x = func_down(x) - func_up(x)
print(x)