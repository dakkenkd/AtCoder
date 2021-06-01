s = input()
count = 0
for i in range(len(s)-3):
  strings = s[i] + s[i+1] + s[i+2] + s[i+3]
  if strings == 'ZONe':
    count += 1
print(count)