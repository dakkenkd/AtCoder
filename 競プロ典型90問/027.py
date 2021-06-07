n = int(input())
dic = {}

for i in range(n):
  s = input()
  if s not in dic.keys():
    dic[s] = 1
    print(i+1)
  