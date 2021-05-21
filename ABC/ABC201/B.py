n = int(input())
mn = 1000000
name = ""
lst = []
for i in range(n):
  s,t = map(str, input().split())
  lst.append([s,int(t)])
lst = sorted(lst, reverse=True, key=lambda x: x[1])
print(lst[1][0])