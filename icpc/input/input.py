lst = []
with open("./A", mode="r", encoding='UTF-8') as f:
    for s_line in f:
        lst.append([*map(int, s_line.split())])

ans = []
idx = 0
while True:
    n = lst[idx][0]
    if n == 0: break
    idx += 1
    L = lst[idx]
    cnt = 0
    for i in range(1,n-1):
        if L[i-1] < L[i] < L[i+1]:
            cnt += 1
    ans.append(str(cnt))

with open("./A_out", mode='w') as f:
    f.write('\n'.join(ans))
