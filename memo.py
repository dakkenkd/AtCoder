n = int(input())
for i in range(n):
    a, s = map(str, input().split())
    p = max(len(a), len(s))
    L = len(a)
    a = a.zfill(p)
    s = s.zfill(p)
    ans = ""
    idx_a = -1
    idx_s = -1
    lst = []
    flag = True
    for _ in range(L):
        if idx_a < -p or idx_s < -p:
            print(-1)
            flag = False
            break
        if int(a[idx_a]) <= int(s[idx_s]):
            lst.append(idx_s)
            idx_a -= 1
            idx_s -= 1
        else:
            lst.append(idx_s-1)
            idx_a -= 1
            idx_s -= 2
    pre = 0
    if flag:
        flag2 = True
        for k in range(L):
            d = lst[k]
            if k == 0:
                # print(s[d:], a[-(k+1)])
                if int(s[d:]) >= 19:
                    flag2 = False
                    break
                ans = str(int(s[d:]) - int(a[-(k+1)])) + ans
                pre = d
            else:
                # print(s[d:pre], a[-(k+1)])
                if int(s[d:pre]) >= 19:
                    flag2 = False
                    break
                ans = str(int(s[d:pre]) - int(a[-(k+1)])) + ans
            pre = d
            # ans += ans + str(int(s[pre:d-1]) - int(a[k]))

        if flag2:
            if str(int(ans[0])) == "0":
                ans = s[0] + ans
            print(int(ans))
        else:
            print(-1)
