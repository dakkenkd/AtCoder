path = 'A'
# path = 'sample'

with open(path) as f:
    l = [s.strip() for s in f.readlines()]
ans = []
for i in range(len(l)):
    if i%2 == 0:
        n = l[i]
    else:
        a = list(map(int, l[i].split()))
        print(a)
        cnt = 0
        for j in range(1, len(a)-1):
            if a[j] > a[j+1] and a[j] > a[j-1]:
                cnt += 1
        print(cnt)
        ans.append(str(cnt))
print(ans)
path_w = 'A.answer'
with open(path_w, mode='w') as f:
    f.write('\n'.join(ans))
