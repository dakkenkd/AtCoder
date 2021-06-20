n = int(input())
i = 1
count = 1
while True:
  if i >= n:
    print(count)
    exit()
  count += 1
  i += count
