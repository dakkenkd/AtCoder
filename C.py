def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
n = int(input())
lst = []
for _ in range(n):
  x,y = map(int, input().split())
  lst.append([x,y])
cnt = cmb(n,3)
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      x1, y1 = lst[i]
      x2, y2 = lst[j]
      x3, y3 = lst[k]
      x2 -= x1
      y2 -= y1
      x3 -= x1
      y3 -= y1
      if x2 * y3 == x3 * y2:
        cnt -= 1
print(cnt)