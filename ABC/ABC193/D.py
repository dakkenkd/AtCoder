k = int(input())
s = list(input())
t = list(input())
point_s = 0
point_t = 0
dic = {}
for i in range(1,10):
  dic[i] = k
for i in range(1,10):
  if str(i) in s:
    dic[i]-= s.count(str(i))
  point_s += i * (10 ** s.count(str(i)))

for i in range(1,10):
  if str(i) in t:
    dic[i]-= t.count(str(i))
  point_t += i * (10 ** t.count(str(i)))
sa = point_s - point_t

count = 0
for i in range(1,10):
  for j in range(1,10):
    ps = point_s + i * ( 10 ** (s.count(str(i))+1) ) - i * ( 10 ** s.count(str(i)) )
    pt = point_t + j * ( 10 ** (t.count(str(j))+1) ) - j * ( 10 ** t.count(str(j)) )
    if ps > pt:
      ci = dic[i]
      dic[i] -= 1
      cj = dic[j]
      count += ci * cj
      dic[i] += 1

m = (9*k-8)

print(count / (m*(m-1)))