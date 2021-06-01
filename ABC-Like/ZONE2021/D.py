from collections import deque
s = input()
t = deque()
count = 0
for i in range(len(s)):
  if s[i] == "R":
    count += 1
  else:
    if t == deque():
      t.append(s[i])
      continue
    if count%2 == 0:
      if s[i] != t[-1]:
        t.append(s[i])
      else:
        t.pop()
    else:
      if s[i] != t[0]:
        t.appendleft(s[i])
      else:
        t.popleft()

if count%2 == 1:
  print("".join(reversed(t)))
else:
  print("".join(t))