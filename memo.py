n = int(input())
lst = [*map(int, input().split())]
dic1 = {}
dic2 = {}
for i in range(0,n,2):
    if lst[i] in dic1:
        dic1[lst[i]] += 1
    else:
        dic1[lst[i]] = 1
for i in range(0,n,2):
    if lst[i] in dic1:
        dic2[lst[i]] += 1
    else:
        dic2[lst[i]] = 1
lst1 = []
lst2 = []
for k in dic1:
    lst1.append((dic1[k], k))
for k in dic2:
    lst2.append((dic2[k], k))
lst1.sort()
lst2.sort()

cnt1 = 0
cn2 = 0
