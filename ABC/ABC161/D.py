from heapq import heappush, heappop
k = int(input())

q = []
for i in range(1,10):
    heappush(q,str(i))
dic = {}
lun = [-1,0,1]
cnt = 1
while  q:
    num = heappop(q)
    dic[len(dic)+1] = num
    if len(dic) > 10**5+1: break
    if cnt > 10**5 + 10: break
    x = int(num[-1])
    for d in lun:
        if x - d < 0 or x + d >= 10: continue
        heappush(q,num+str(x-d))

print(dic[k])
