a,b = map(int, input().split())
c,d = map(int, input().split())

sa1 = a-b
sa2 = c-d
if a==c and b==d:
  print(0)
  exit()
if (a+b == c+d) or (a-b == c-d):
  print(1)
  exit()
elif abs(a-c) + abs(b-d) <= 3:
  print(1)
  exit()
elif sa1 % 2 == sa2 % 2:
  print(2)
  exit()
elif abs(a-c) + abs(b-d) <= 6:
  print(2)
  exit()
elif abs(a-c + b-d) <= 3 or abs(a-c - (b-d)) <= 3:
  print(2)
  exit()
else:
  print(3)
  exit()