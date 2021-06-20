import itertools
n, k = map(int, input().split())
lst = [[int(i) for i in input().split()] for j in range(n)]
time = []
visit = []
comb_lst = []
for d in itertools.permutations(range(1,n)):  # 0, 1, 2
    comb = list(d)
    comb_lst.append(comb)

for d in comb_lst:
  count = 0
  road = [0] + d + [0]
  for i in range(len(road)-1):
    count += lst[road[i]][road[i+1]]
  time.append(count)
print(time.count(k))