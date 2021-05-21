n = input()

x = n.strip('0')

for i in range(len(x)//2):
  if x[i] != x[-(i+1)]:
    print('No')
    exit()
print('Yes')