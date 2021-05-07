n = int(input())
s = input()
q = int(input())
lst = [ list(s[:n]), list(s[n:]) ]

for i in range(q):
  t,a,b = map(int, input().split())
  a -= 1
  b -= 1
  if t == 1:
    lst[a//n][a%n], lst[b//n][b%n] = lst[b//n][b%n], lst[a//n][a%n]
  else:
    lst[0], lst[1] = lst[1], lst[0]
print("".join(lst[0]+lst[1]))