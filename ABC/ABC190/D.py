N = int(input())
count = 0

def divisor(n): 
  i = 1
  table = []
  while i * i <= n:
    if n%i == 0:
      table.append(i)
      table.append(n//i)
    i += 1
  table = list(set(table))
  return table

for i in divisor(N):
  if i%2 == 1 and N%i == 0:
    count += 1
print(count*2)