h, n = map(int, input().split())
lst = []
cost_dic = {}
for i in range(n):
    a, b = map(int, input().split())
    k = a/b
    lst.append(k,a,b)
    if b in cost_dic:
        cost_dic[b].append(a)
    else:
        cost_dic[b] = [a]

lst.sort()

cnt = h//lst[0][1]
ans = cnt * lst[0][2]
h = h%lst[0][1]

while True:
    
