from collections import Counter
n = int(input())
lst = [int(x)-(i+1) for i,x in enumerate(input().split())]

ans = 0
mn = min(lst)
mx = max(lst)
print(lst)
if mn > 0:
    cnt = 0
    for d in lst:
        if d == mn:
            cnt += 1
    print(sum(lst)-mn*cnt)
elif mx < 0:
    cnt = 0
    for d in lst:
        if d == mx:
            cnt += 1
    print(cnt*mx - sum(lst))
elif mn == 0:
    c = Counter(lst)
    mx_num = -1
    for d in c:
        if c[d] > len(lst)//2:
            mx_num = d
            break
    if mx_num == -1:
        print(sum(lst))
    else:
        print(sum(lst)-mx_num*len(lst))
elif mx == 0:
    c = Counter(lst)
    mx_num = 1
    for d in c:
        if c[d] > len(lst)//2:
            mx_num = d
            break
    if mx_num == 1:
        print(-sum(lst))
    else:
        print(abs(mx_num*len(lst) - sum(lst)))
else:
    print(sum([abs(i) for i in lst]))
