n, x = map(int, input().split())
s = ""
for i in map(int,input().split()):
  if i != x:
    s += str(i)
    s += ' '
print(s.rstrip(' '))